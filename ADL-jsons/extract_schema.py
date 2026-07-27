#!/usr/bin/env python3
"""
extract_schema.py - derive the .adl.json schema from a corpus of exported ADL algos.

Reads every *.adl.json next to this script and writes `block-catalog.json`: the
machine-readable wiring table (defId, connector GUIDs, observed property values) that
makes generating an algo file possible at all, plus corpus-wide statistics and a set
of structural invariants re-checked on every run.

    python extract_schema.py

Re-run this whenever you drop a new ADL export into the folder. Coverage grows with
the corpus, and the unknowns in README.md section 8 close the same way.

Everything reported is OBSERVED. Absence here means "not present in these files",
never "impossible in ADL".

Parsing lives in adlkit.py so the recursion rules and format quirks are implemented
exactly once across every script in this folder.
"""

import json
import os
from collections import defaultdict, Counter

import adlkit as K


def main():
    files = K.corpus_files()
    if not files:
        raise SystemExit("No *.adl.json files found next to this script.")

    conns = defaultdict(lambda: {"IN": set(), "OUT": set()})
    props = defaultdict(lambda: defaultdict(Counter))
    prop_kind = defaultdict(dict)
    def_ids = defaultdict(Counter)
    block_files = defaultdict(set)
    counts = Counter()
    per_file = {}
    custom_names = defaultdict(list)
    top_keys = Counter()
    max_depth = 0

    # Per-instance wiring arity: how many DISTINCT inputs a single instance ever had
    # wired at once. The flat connector list conflates ports across instances, which
    # is what makes "how many inputs does a Funnel have" hard to answer (README §3).
    max_in_arity = Counter()
    max_out_arity = Counter()

    # Invariants re-verified on every run. If the corpus grows and one of these stops
    # holding, the number moves off zero and validate.py needs revisiting.
    inv = Counter()

    guid_files = defaultdict(set)  # cross-file GUID reuse

    for path in files:
        name = os.path.basename(path)
        algo = K.load_algo(path)
        top_keys.update(algo.keys())

        nb = ne = ng = 0
        file_guids = Counter()
        inst_in = defaultdict(set)
        inst_out = defaultdict(set)

        for gpath, blocks, edges in K.walk_graphs(algo.get("content", [])):
            ng += 1
            max_depth = max(max_depth, gpath.count("/"))
            nb += len(blocks)
            ne += len(edges)

            local = {}
            for b in blocks:
                dn = b.get("defName")
                guid = b.get("guid")
                local[guid] = dn
                file_guids[guid] += 1
                guid_files[guid].add(name)
                counts[dn] += 1
                block_files[dn].add(name)
                def_ids[dn][b.get("defId", "")] += 1
                for p in b.get("properties", []):
                    v = p.get("value")
                    key = (str(v)[:60] if isinstance(v, (str, bool, int, float))
                           else "<complex>")
                    props[dn][p.get("name")][key] += 1
                    prop_kind[dn][p.get("name")] = type(v).__name__
                    if p.get("hasCustomName") and isinstance(v, str) and v:
                        custom_names[dn].append((name, v))

            for e in edges:
                sb, tb = e.get("sourceBlock"), e.get("targetBlock")
                # INVARIANT: an edge's endpoints always live in its own graph.
                if sb not in local or tb not in local:
                    inv["edgesCrossingGraphBoundary"] += 1
                if sb in local:
                    conns[local[sb]]["OUT"].add(e.get("sourceConnector"))
                    inst_out[sb].add(e.get("sourceConnector"))
                if tb in local:
                    conns[local[tb]]["IN"].add(e.get("targetConnector"))
                    inst_in[tb].add(e.get("targetConnector"))

        index = K.all_blocks(algo)
        for guid, wired in inst_in.items():
            dn = (index.get(guid) or {}).get("defName")
            max_in_arity[dn] = max(max_in_arity[dn], len(wired))
        for guid, wired in inst_out.items():
            dn = (index.get(guid) or {}).get("defName")
            max_out_arity[dn] = max(max_out_arity[dn], len(wired))

        # INVARIANT: GUIDs are unique within a file.
        inv["duplicateGuidsWithinAFile"] += sum(1 for c in file_guids.values() if c > 1)

        # INVARIANT: every JumpLanding is claimed by exactly one Jump, and points back.
        landings = {g for g, b in index.items() if b.get("defName") == "JumpLanding"}
        referenced = Counter()
        for jump, targets in K.jump_links(algo):
            raw = K.prop(jump, "targetBlock")
            if raw is None:
                inv["jumpsWithNoTarget"] += 1
                continue
            for t in (raw if isinstance(raw, list) else [raw]):
                referenced[t] += 1
            for lb in targets:
                if lb is None:
                    inv["jumpsTargetingAGhost"] += 1
                elif K.prop(lb, "sourceBlock") != jump.get("guid"):
                    inv["landingsNotPointingBack"] += 1
        inv["orphanedLandings"] += len(landings - set(referenced))
        inv["landingsClaimedByMultipleJumps"] += sum(1 for g in landings
                                                     if referenced[g] > 1)

        # INVARIANT: Group <-> inner Connector three-way binding agrees.
        for g in K.iter_groups(algo):
            declared = K.prop(g, "connectors") or {}
            inner = {b.get("guid") for b in K.children(g)
                     if b.get("defName") == "Connector"}
            if isinstance(declared, dict) and set(declared) != inner:
                inv["groupConnectorBindingMismatch"] += 1

        per_file[name] = {
            "blocks": nb, "edges": ne, "graphs": ng,
            "variables": len(algo.get("variables", []) or []),
            "exports": len(algo.get("exports", []) or []),
            "isSOA": algo.get("isSOA"),
            "isOmaOta": algo.get("isOmaOta"),
            "ignoreMarketState": algo.get("ignoreMarketState"),
        }

    catalog = {}
    for dn in sorted(counts):
        ids = def_ids[dn]
        catalog[dn] = {
            "defId": ids.most_common(1)[0][0] if ids else None,
            "defIdStable": len(ids) == 1,
            "instances": counts[dn],
            "filesSeenIn": len(block_files[dn]),
            "connectors": {
                "in": sorted(c for c in conns[dn]["IN"] if c),
                "out": sorted(c for c in conns[dn]["OUT"] if c),
            },
            # Highest number of ports any SINGLE instance had wired. The connector
            # lists above are a union across instances and overstate a block's arity.
            "maxWiredArity": {"in": max_in_arity.get(dn, 0),
                              "out": max_out_arity.get(dn, 0)},
            "properties": {
                pn: {
                    "type": prop_kind[dn].get(pn),
                    "observedValues": [v for v, _ in vc.most_common(12)
                                       if v != "<complex>"],
                }
                for pn, vc in sorted(props[dn].items()) if pn
            },
        }

    shared = sum(1 for fs in guid_files.values() if len(fs) > 1)

    out = {
        "_meta": {
            "generatedBy": "extract_schema.py",
            "corpusFiles": [os.path.basename(f) for f in files],
            "totalBlocks": sum(counts.values()),
            "distinctBlockTypes": len(catalog),
            "maxGroupNestingDepth": max_depth,
            "topLevelKeys": dict(top_keys),
            "guidsAppearingInMoreThanOneFile": shared,
            "caveat": (
                "Connector GUIDs are those OBSERVED wired in this corpus - a floor, "
                "not a block's full port count. Use maxWiredArity for how many ports "
                "one instance ever had connected at once. Group connectors are "
                "per-instance (declared inline in the block's 'connectors' property) "
                "and are deliberately excluded from the stable-catalog claim. Block "
                "GUIDs are unique within a file but NOT across files."
            ),
        },
        # Every one of these must stay 0. A non-zero value means an invariant that
        # validate.py enforces has been contradicted by a real ADL-authored file -
        # believe the file and loosen the check.
        "_invariants": {k: inv[k] for k in sorted(set(inv) | {
            "edgesCrossingGraphBoundary", "duplicateGuidsWithinAFile",
            "orphanedLandings", "jumpsTargetingAGhost", "landingsNotPointingBack",
            "landingsClaimedByMultipleJumps", "groupConnectorBindingMismatch",
        })},
        "perFile": per_file,
        "blocks": catalog,
        "customNamesByBlock": {k: v for k, v in sorted(custom_names.items())},
    }

    dest = os.path.join(K.HERE, "block-catalog.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)

    print(f"Wrote {dest}")
    print(f"  files={len(files)} blocks={sum(counts.values())} "
          f"types={len(catalog)} maxdepth={max_depth}")
    print(f"  GUIDs shared between files: {shared} "
          f"(so always remint when transplanting)")
    print("\n  invariants (all must be 0):")
    for k, v in out["_invariants"].items():
        flag = "  <-- BROKEN" if v and k != "jumpsWithNoTarget" else ""
        print(f"    {v:>4}  {k}{flag}")
    print()
    for f, v in per_file.items():
        print(f"  {f[:36]:36} blocks={v['blocks']:4} edges={v['edges']:4} "
              f"graphs={v['graphs']:3}")


if __name__ == "__main__":
    main()
