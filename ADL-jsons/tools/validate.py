#!/usr/bin/env python3
"""
validate.py - structural invariant checker for .adl.json files.

This is the safety net for generating or hand-editing algo files. ADL's importer is a
black box; this catches the classes of corruption we CAN detect locally, before you
waste an import cycle finding out.

    python tools/validate.py                       # self-test: check all 13 corpus algos
    python tools/validate.py myalgo.adl.json       # check one file
    python tools/validate.py --strict myalgo.json  # treat warnings as failures
    python tools/validate.py --explain C7          # what a check means and why it matters

## The self-test is the point

Every invariant here was derived FROM the corpus, so running `python tools/validate.py` with
no arguments must come back clean. If a check fires on a TT-authored file, the check is
wrong (or the corpus just taught us something new) - fix the checker, don't "fix" TT's
algo. That property is what makes a green result on YOUR file mean anything.

## What this cannot tell you

Structure only. A file can pass every check here and still be nonsense: wrong port
TYPES wired together (the format doesn't record them), a design that deadlocks, a
formula that computes garbage. And passing does NOT prove ADL will import it - that
remains untested. See OPEN-QUESTIONS.md.
"""

import os
import sys

import adlkit as K

# ---------------------------------------------------------------------------
# Check registry. Each check gets a stable ID so reports and docs can cite it.
# ---------------------------------------------------------------------------

CHECKS = {
    "C1": "Top-level keys present and correctly typed",
    "C2": "Block GUIDs unique within the file",
    "C3": "Every edge endpoint resolves to a block in the SAME graph",
    "C4": "Connector GUIDs are known for that block type",
    "C5": "Connector direction is right (source uses an out-port, target an in-port)",
    "C6": "defId matches the catalog for that defName",
    "C7": "Group <-> Connector three-way binding agrees",
    "C8": "Jump <-> JumpLanding cross-references agree",
    "C9": "Every entry in `variables` names a real block",
    "C10": "Every entry in `exports` resolves to a real block.connector",
    "C11": "Formula GUID references resolve to real blocks",
    "C12": "Formula message fields are recognised",
    "C13": "formula and formulaNodes are both present or both absent",
    "C14": "No block is completely unreferenced (orphan)",
}

EXPLAIN = {
    "C2": """GUIDs must be unique within one file - the corpus has 0 duplicates across
4,740 blocks. They are NOT unique ACROSS files (571 of 3,011 are shared between TT
algos), so when you transplant a subgraph you MUST remint every GUID. A duplicate
means two blocks are fighting over the same identity and every edge touching them is
ambiguous. This is the single most likely bug in a generated file.""",

    "C3": """Verified across 4,364 edges: an edge always lives in the same `content`
array as both blocks it connects. Nothing crosses a Group boundary via an edge - that
is what Connector blocks and Jump blocks are for. An edge naming a block in another
graph is unrepresentable in ADL, whatever the JSON says.""",

    "C4": """Blocks do not declare their own ports. Connector GUIDs appear ONLY inside
edges, so a wrong one is invisible until ADL rejects it. The catalog knows the GUIDs
observed wired in the corpus - a floor, not a ceiling. An unknown connector is a
WARNING because it may be a legitimate port TT's own algos never happened to use
(the 4th input of a Funnel, a port that only appears for a certain Order type).
Unknown on a common block is suspicious; unknown on a rare block may be fine.""",

    "C7": """A Group port's GUID must appear in three places that all agree: the parent
Group's `connectors` property (keyed by the GUID), a Connector block inside
internalAlgo.content whose OWN guid IS that GUID, and that Connector's `definition`
property mirroring name/type/input. Get any one wrong and the group boundary breaks.
This is mechanical to satisfy if you build all three together, and the most common way
a hand-built Group fails.""",

    "C8": """Jump/JumpLanding is a wormhole with no drawn edge - 41% of all blocks in
the corpus. The link is carried in properties: Jump.sourceBlock/.sourceConnector name
the real upstream, Jump.targetBlock is a LIST of landing GUIDs, and each landing
back-points at the Jump via its own sourceBlock. `generic` carries the port type as
{connectorGuid: type}. All 1,199 landings in the corpus are referenced by exactly one
Jump, with zero orphans and zero dangling references. A broken pair means data
silently never arrives.""",

    "C13": """Blocks with formulas carry both a `formula` source string and a
`formulaNodes` parsed AST, tied together by formulaGraphId. WHICH ONE THE RUNTIME
EVALUATES IS UNKNOWN. Editing the string without regenerating the AST is the most
likely way to corrupt a hand-edited file - the two would disagree and you cannot
predict which wins. Prefer changing a wired Number block's value, which has no AST.
See OPEN-QUESTIONS.md Q2.""",
}


def load_catalog_safe():
    """The catalog if it exists, else None. Checks C4/C5/C6 are skipped without it."""
    return K.load_catalog()


class Report:
    def __init__(self, label):
        self.label = label
        self.errors = []
        self.warnings = []
        self.notes = []
        self.stats = {}

    def error(self, cid, msg, where=""):
        self.errors.append((cid, msg, where))

    def warn(self, cid, msg, where=""):
        self.warnings.append((cid, msg, where))

    def note(self, msg):
        """Advisory. Never a failure, even under --strict."""
        self.notes.append(msg)

    @property
    def ok(self):
        return not self.errors

    def render(self, strict=False, limit=12):
        s = self.stats
        head = (f"{self.label}  "
                f"blocks={s.get('blocks', 0)} edges={s.get('edges', 0)} "
                f"graphs={s.get('graphs', 0)} groups={s.get('groups', 0)} "
                f"jumps={s.get('jumps', 0)}")
        bad = self.errors or (strict and self.warnings)
        print(f"{'FAIL' if bad else 'ok  '}  {head}")
        for tag, items in (("ERROR", self.errors), ("warn ", self.warnings)):
            for cid, msg, where in items[:limit]:
                loc = f"  @{where}" if where else ""
                print(f"        {tag} [{cid}] {msg}{loc}")
            if len(items) > limit:
                print(f"        ... and {len(items) - limit} more {tag.strip()}s")
        for n in self.notes:
            print(f"        note  {n}")


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def validate(algo, label, catalog=None):
    r = Report(label)

    # --- C1 top-level shape -------------------------------------------------
    for key, typ in (("content", list), ("name", str)):
        if key not in algo:
            r.error("C1", f"missing required top-level key '{key}'")
        elif not isinstance(algo[key], typ):
            r.error("C1", f"top-level '{key}' should be {typ.__name__}, "
                          f"got {type(algo[key]).__name__}")
    for key in ("variables", "exports", "bookmarks"):
        if key in algo and not isinstance(algo[key], list):
            r.error("C1", f"top-level '{key}' should be a list")
    if not isinstance(algo.get("content"), list):
        return r  # nothing else is checkable

    index = K.all_blocks(algo)
    r.stats["blocks"] = len(index)
    r.stats["groups"] = sum(1 for b in index.values() if b.get("defName") == "Group")
    r.stats["jumps"] = sum(1 for b in index.values() if b.get("defName") == "Jump")

    # --- C2 GUID uniqueness -------------------------------------------------
    seen = {}
    ngraphs = nedges = 0
    for gpath, blocks, edges in K.walk_graphs(algo["content"]):
        ngraphs += 1
        nedges += len(edges)
        for b in blocks:
            g = b.get("guid")
            if g is None:
                r.error("C2", f"{b.get('defName')} block has no guid", gpath)
            elif g in seen:
                r.error("C2", f"guid {g[:8]} used by both {seen[g]} and "
                              f"{b.get('defName')}", gpath)
            else:
                seen[g] = b.get("defName")
    r.stats["graphs"] = ngraphs
    r.stats["edges"] = nedges

    # --- C3/C4/C5 edges -----------------------------------------------------
    for gpath, blocks, edges in K.walk_graphs(algo["content"]):
        local = {b.get("guid"): b for b in blocks}
        for e in edges:
            sb, tb = e.get("sourceBlock"), e.get("targetBlock")
            sc, tc = e.get("sourceConnector"), e.get("targetConnector")
            for role, bg in (("source", sb), ("target", tb)):
                if bg not in local:
                    where = "another graph" if bg in index else "nowhere in the file"
                    r.error("C3", f"edge {role}Block {str(bg)[:8]} resolves to {where}",
                            gpath)
            if catalog and sb in local and tb in local:
                _check_connector(r, catalog, local[sb], sc, "out", gpath)
                _check_connector(r, catalog, local[tb], tc, "in", gpath)

    # --- C6 defId -----------------------------------------------------------
    if catalog:
        for b in index.values():
            dn, did = b.get("defName"), b.get("defId")
            known = (catalog["blocks"].get(dn) or {}).get("defId")
            if known and did and did.upper() != known.upper():
                r.error("C6", f"{dn} has defId {did[:8]}, catalog says {known[:8]}")
            elif dn and dn not in catalog["blocks"]:
                r.warn("C6", f"block type '{dn}' is not in the catalog "
                             f"(new to the corpus?)")

    _check_groups(r, algo)
    _check_jumps(r, algo, index)
    _check_surfaces(r, algo, index)
    _check_formulas(r, algo, index)
    _check_orphans(r, algo, index)
    return r


def _check_connector(r, catalog, block, conn, role, gpath):
    """C4/C5: is this connector GUID known, and used in the right direction?"""
    dn = block.get("defName")
    if dn in K.PER_INSTANCE_CONNECTOR_BLOCKS:
        return  # Group/Connector ports are per-instance; C7 covers them
    entry = catalog["blocks"].get(dn)
    if not entry:
        return
    ins = set(entry["connectors"]["in"])
    outs = set(entry["connectors"]["out"])
    if conn not in ins | outs:
        r.warn("C4", f"{dn}: connector {str(conn)[:8]} not observed in the corpus "
                     f"(may be a valid port TT never wired)", gpath)
    elif role == "out" and conn not in outs:
        r.error("C5", f"{dn}: {str(conn)[:8]} used as a source but the corpus only "
                      f"ever sees it as an INPUT", gpath)
    elif role == "in" and conn not in ins:
        r.error("C5", f"{dn}: {str(conn)[:8]} used as a target but the corpus only "
                      f"ever sees it as an OUTPUT", gpath)


def _check_groups(r, algo):
    """C7: the three-way Group <-> Connector binding."""
    for g in K.iter_groups(algo):
        declared = K.prop(g, "connectors") or {}
        gname = K.block_name(g)
        if not isinstance(declared, dict):
            r.error("C7", f"Group '{gname}' has a non-dict connectors property")
            continue
        # IMMEDIATE children only. Recursing here would attribute a nested Group's
        # Connector blocks to this one - which is exactly what the corpus self-test
        # caught when this check was first written.
        inner = {b.get("guid"): b for b in K.children(g)
                 if b.get("defName") == "Connector"}
        for cguid, decl in declared.items():
            cb = inner.get(cguid)
            if cb is None:
                r.error("C7", f"Group '{gname}' declares port {cguid[:8]} but no "
                              f"Connector block inside has that guid")
                continue
            defn = K.prop(cb, "definition") or {}
            for field in ("name", "type", "input"):
                dv, iv = decl.get(field), defn.get(field)
                if dv != iv:
                    r.error("C7", f"Group '{gname}' port {cguid[:8]}: parent says "
                                  f"{field}={dv!r}, inner Connector says {iv!r}")
        for cguid in inner:
            if cguid not in declared:
                r.error("C7", f"Group '{gname}' contains Connector {cguid[:8]} that "
                              f"the parent never declares")


def _check_jumps(r, algo, index):
    """C8: Jump/JumpLanding cross-references."""
    landings = {g for g, b in index.items() if b.get("defName") == "JumpLanding"}
    referenced = set()
    for jump, targets in K.jump_links(algo):
        jg = jump.get("guid")
        jname = K.block_name(jump)
        raw = K.prop(jump, "targetBlock")
        if raw is None:
            r.warn("C8", f"Jump '{jname}' has no targetBlock - it goes nowhere")
            continue
        for t in (raw if isinstance(raw, list) else [raw]):
            referenced.add(t)
        for t, lb in zip((raw if isinstance(raw, list) else [raw]), targets):
            if lb is None:
                r.error("C8", f"Jump '{jname}' targets {str(t)[:8]} which is not "
                              f"a block in this file")
            elif lb.get("defName") != "JumpLanding":
                r.error("C8", f"Jump '{jname}' targets a {lb.get('defName')}, "
                              f"expected JumpLanding")
            elif K.prop(lb, "sourceBlock") != jg:
                r.error("C8", f"JumpLanding {str(t)[:8]} does not point back at "
                              f"Jump '{jname}'")
    for g in landings - referenced:
        r.error("C8", f"JumpLanding {g[:8]} ('{K.block_name(index[g])}') is not "
                      f"targeted by any Jump - it can never receive data")


def _check_surfaces(r, algo, index):
    """C9/C10: user-facing variables and dashboard exports."""
    for v in algo.get("variables", []) or []:
        if v not in index:
            r.error("C9", f"variables lists {str(v)[:8]} which is not a block")
    for ex in algo.get("exports", []) or []:
        if not isinstance(ex, str) or "." not in ex:
            r.error("C10", f"export {ex!r} is not in 'blockGuid.connectorGuid' form")
            continue
        bg, _, cg = ex.partition(".")
        if bg not in index:
            r.error("C10", f"export references block {bg[:8]} which does not exist")
        elif not K.GUID_RE.fullmatch(cg):
            r.error("C10", f"export {ex[:20]}... has a malformed connector GUID")


def _check_formulas(r, algo, index):
    """C11/C12/C13: formula references, fields, and AST accounting.

    Two things the corpus taught us, both of which stop these from being errors:

      * Formulas routinely reference blocks in ANOTHER graph. 20 of 98 Groups do it.
        Graphs are not reference-isolated the way edges are (C3). It is normal - but
        it is precisely what makes a subgraph non-transplantable, so it is counted
        and surfaced rather than ignored. See patterns.py RED tier.
      * `formula` and `formulaNodes` do NOT reliably come as a pair. TT ships blocks
        with a string and no AST (several Alert blocks) and with an AST and no string
        (ValueInjector, DiscreteOrder). So their pairing proves nothing, and C13 is
        an advisory count, not a check you can fail.
    """
    xgraph = 0
    with_ast = 0
    for gpath, blocks, _ in K.walk_graphs(algo["content"]):
        local = {b.get("guid") for b in blocks}
        for b in blocks:
            text = K.prop(b, "formula")
            if K.prop(b, "formulaNodes") not in (None, {}, []):
                with_ast += 1
            if not (isinstance(text, str) and text.strip()):
                continue
            name = K.block_name(b)
            for bg, _cg in K.formula_refs(text):
                if bg not in index:
                    r.error("C11", f"{name}: formula references block {bg[:8]} "
                                   f"which does not exist anywhere in the file", gpath)
                elif bg not in local:
                    xgraph += 1
            for f in K.formula_fields(text) - K.KNOWN_MESSAGE_FIELDS:
                r.warn("C12", f"{name}: unrecognised message field {{{f}}}", gpath)

    r.stats["formulaAST"] = with_ast
    r.stats["xGraphRefs"] = xgraph
    if with_ast:
        r.note(f"{with_ast} blocks carry a formulaNodes AST - do not hand-edit their "
               f"formula strings (OPEN-QUESTIONS.md Q2)")
    if xgraph:
        r.note(f"{xgraph} formula references cross a graph boundary - normal in TT "
               f"algos, but they block clean subgraph reuse")


def _check_orphans(r, algo, index):
    """C14: blocks nothing references. Informational - some are legitimately isolated."""
    touched = set()
    for _, _, edges in K.walk_graphs(algo["content"]):
        for e in edges:
            touched.add(e.get("sourceBlock"))
            touched.add(e.get("targetBlock"))
    for b in index.values():
        if b.get("defName") in ("Jump", "JumpLanding"):
            touched.add(K.prop(b, "sourceBlock"))
            for t in (K.prop(b, "targetBlock") or []):
                touched.add(t)
    # Note blocks are decorative; Connectors are reached through their Group.
    exempt = {"Note", "Connector", "Group"}
    for g, b in index.items():
        if g is None:
            continue  # already reported by C2; nothing else can be said about it
        if g not in touched and b.get("defName") not in exempt:
            r.warn("C14", f"{b.get('defName')} '{K.block_name(b)}' ({g[:8]}) is wired "
                          f"to nothing")


# ---------------------------------------------------------------------------

def main():
    args = [a for a in sys.argv[1:]]
    strict = "--strict" in args
    args = [a for a in args if a != "--strict"]

    if args and args[0] == "--explain":
        if len(args) < 2:
            for cid, desc in CHECKS.items():
                print(f"{cid:<5} {desc}")
            return 0
        cid = args[1].upper()
        print(f"{cid}: {CHECKS.get(cid, 'unknown check')}\n")
        print(EXPLAIN.get(cid, "No extended note for this check."))
        return 0

    catalog = K.load_catalog()
    if catalog is None:
        print("warning: block-catalog.json missing - skipping C4/C5/C6 "
              "(run: python tools/extract_schema.py)\n")

    targets = args or K.corpus_files()
    if not targets:
        print("No .adl.json files found in ADL-jsons/corpus/.")
        return 1
    selftest = not args

    if selftest:
        print("SELF-TEST: validating the 13 TT-authored corpus algos.")
        print("These are known-good by definition. Any ERROR here is a bug in "
              "validate.py,\nnot in TT's algo - or a genuine new discovery about "
              "the format.\n")

    failed = 0
    for path in targets:
        label = os.path.basename(path)[:34].ljust(34)
        try:
            algo = K.load_algo(path)
        except ValueError as e:
            print(f"FAIL  {label}  {e}")
            failed += 1
            continue
        rep = validate(algo, label, catalog)
        rep.render(strict=strict)
        if rep.errors or (strict and rep.warnings):
            failed += 1

    print()
    if selftest:
        print(f"Self-test: {len(targets) - failed}/{len(targets)} corpus algos clean.")
        if failed:
            print("A corpus file failing means an invariant above is stated too "
                  "strongly. Loosen it\nrather than assuming TT shipped a broken algo.")
        else:
            print("All invariants hold across the corpus, so a clean result on your "
                  "own file is\nmeaningful. It still does NOT prove ADL will import "
                  "it - see OPEN-QUESTIONS.md Q1.")
    else:
        print(f"{len(targets) - failed}/{len(targets)} file(s) passed"
              f"{' (strict)' if strict else ''}.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
