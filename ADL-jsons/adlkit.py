#!/usr/bin/env python3
"""
adlkit.py - shared parsing primitives for .adl.json files.

Every other script in this folder imports this one, so the recursion rules and the
quirks below are implemented exactly once. The quirks are the whole point: each was
found the hard way against the 13-algo corpus, and re-implementing them ad hoc is
how the pipeline rots.

Quirks this module absorbs (all [V] - verified against the corpus):

  1. `content` is RECURSIVE. Group blocks hide a whole subgraph under
     block['internalAlgo']['content'], up to 3 levels deep. A flat scan of the
     top-level array sees roughly one third of a real algo.
  2. A property entry may have NO 'value' key at all (1,104 occurrences). Always
     use .get, never [].
  3. Block GUIDs are unique WITHIN a file but NOT across files - 571 of 3,011
     GUIDs appear in more than one TT algo. Never key a cross-file index by GUID
     alone; use (file, guid).
  4. Edges never cross a graph boundary (0 of 4,364). Both endpoints of an edge
     always live in the same `content` array as the edge itself.
  5. Jump/JumpLanding are linked by PROPERTIES, not edges: Jump.targetBlock is a
     LIST of landing GUIDs, and each landing back-points via sourceBlock.
"""

import json
import os
import re
import glob

HERE = os.path.dirname(os.path.abspath(__file__))

GUID_RE = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
                     r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
# Reference to another block's output inside a formula string: [blockGuid.connectorGuid]
FORMULA_REF_RE = re.compile(r"\[(" + GUID_RE.pattern + r")\.(" + GUID_RE.pattern + r")\]")
# Discrete message field inside a formula string: {fillQuantity}
FORMULA_FIELD_RE = re.compile(r"\{(\w+)\}")

# Message fields observed in corpus formulas. Not exhaustive - the Formula Editor
# exposes more; these are simply the ones TT's own algos use. See adl-kb formula-reference.
KNOWN_MESSAGE_FIELDS = {
    "fillQuantity", "isExternalEvent", "orderQuantity", "workingQuantity",
    "limitPrice", "isBuy", "userField1", "userField2", "userField3", "userField4",
    "fillPrice", "isSuspended", "stopTrigger", "deletedQuantity",
}

# Blocks whose connector GUIDs are per-instance rather than global, so the catalog
# cannot validate them. Group declares its ports inline; Connector IS a port.
PER_INSTANCE_CONNECTOR_BLOCKS = {"Group", "Connector"}


def load_algo(path):
    """Parse one .adl.json. Raises ValueError with the file name on malformed input."""
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as e:
        raise ValueError(f"{os.path.basename(path)}: not valid JSON - {e}") from e


def corpus_files(folder=HERE):
    """Every .adl.json next to this script, sorted."""
    return sorted(glob.glob(os.path.join(folder, "*.adl.json")))


def props(block):
    """Block properties as a plain dict. Absorbs quirk 2 (missing 'value' key)."""
    return {p.get("name"): p.get("value") for p in block.get("properties", [])}


def prop(block, name, default=None):
    for p in block.get("properties", []):
        if p.get("name") == name:
            return p.get("value", default)
    return default


def block_name(block):
    """Display name: the custom label if the user set one, else the defName."""
    return prop(block, "name") or block.get("defName", "?")


def walk_graphs(content, path="root"):
    """Yield (graph_path, blocks, edges) for the root graph and every nested subgraph.

    Absorbs quirk 1. `path` is a readable breadcrumb like
    "root/Group:3f2a91bc/Group:88c1de04" - stable enough to cite in a report.
    """
    if not isinstance(content, list):
        return
    blocks = [x for x in content if "defName" in x]
    edges = [x for x in content if x.get("className") == "Edge"]
    yield path, blocks, edges
    for b in blocks:
        inner = b.get("internalAlgo")
        if isinstance(inner, dict) and isinstance(inner.get("content"), list):
            yield from walk_graphs(inner["content"],
                                   f"{path}/{b.get('defName')}:{b.get('guid', '?')[:8]}")


def all_blocks(algo):
    """Every block at every depth, as {guid: block}. Safe because of quirk 3
    (within one file, GUIDs are unique)."""
    out = {}
    for _, blocks, _ in walk_graphs(algo.get("content", [])):
        for b in blocks:
            out[b.get("guid")] = b
    return out


def children(group_block):
    """Blocks at a Group's IMMEDIATE level only - not inside its nested Groups.

    Use this for anything about the Group's own boundary (its Connector blocks).
    Using descendants() there wrongly attributes a nested Group's ports to its
    parent, which is a real bug this module exists to prevent.
    """
    inner = group_block.get("internalAlgo") or {}
    return [x for x in (inner.get("content") or []) if "defName" in x]


def descendants(group_block):
    """Every block nested anywhere inside a Group, at any depth."""
    out = []
    inner = group_block.get("internalAlgo") or {}
    for x in inner.get("content", []) or []:
        if "defName" in x:
            out.append(x)
            out.extend(descendants(x))
    return out


def descendant_edges(group_block):
    """Every edge nested anywhere inside a Group, at any depth."""
    out = []
    inner = group_block.get("internalAlgo") or {}
    for x in inner.get("content", []) or []:
        if x.get("className") == "Edge":
            out.append(x)
        elif "defName" in x:
            out.extend(descendant_edges(x))
    return out


def iter_groups(algo):
    """Yield every Group block at every depth."""
    for _, blocks, _ in walk_graphs(algo.get("content", [])):
        for b in blocks:
            if b.get("defName") == "Group":
                yield b


def formula_refs(text):
    """[(blockGuid, connectorGuid), ...] referenced by a formula string."""
    if not isinstance(text, str):
        return []
    return FORMULA_REF_RE.findall(text)


def formula_fields(text):
    """{fieldName, ...} referenced by a formula string."""
    if not isinstance(text, str):
        return set()
    return set(FORMULA_FIELD_RE.findall(text))


def load_catalog(folder=HERE):
    """block-catalog.json, or None if it hasn't been generated yet."""
    p = os.path.join(folder, "block-catalog.json")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def jump_links(algo):
    """Yield (jump_block, [landing_block, ...]) for every Jump in the algo.

    Absorbs quirk 5. Landings that cannot be resolved come back as None so callers
    can report them rather than silently skipping.
    """
    idx = all_blocks(algo)
    for guid, b in idx.items():
        if b.get("defName") != "Jump":
            continue
        targets = prop(b, "targetBlock") or []
        if not isinstance(targets, list):
            targets = [targets]
        yield b, [idx.get(t) for t in targets]
