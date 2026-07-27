#!/usr/bin/env python3
"""
test_validate.py - fault injection tests for validate.py.

A validator that only ever prints "ok" is worthless. The corpus self-test proves it
does not cry wolf on good files; this proves it actually bites on bad ones. Both
halves are needed before a green result means anything.

Each test deliberately corrupts a copy of Conditional.adl.json (the smallest algo:
43 blocks, one graph) in one specific way, and asserts the expected check fires.

    python test_validate.py

No third-party dependencies - plain asserts, so it runs anywhere Python does.
"""

import copy
import os
import sys

import adlkit as K
import validate as V

HERE = os.path.dirname(os.path.abspath(__file__))
# Smallest single-graph algo: 43 blocks, no Group. Good default subject.
BASE = os.path.join(HERE, "Conditional.adl.json")
# Conditional contains no Group, so the C7 binding tests need a different subject.
# TT Sniper is the smallest algo that has Groups (62 blocks, 3 groups).
GROUP_BASE = os.path.join(HERE, "TT Sniper .adl.json")

RESULTS = []


def check(name, algo, expect_check, expect_level="error"):
    """Validate a mutated algo and assert expect_check fired at expect_level."""
    rep = V.validate(algo, name, V.load_catalog_safe())
    fired = {cid for cid, _, _ in (rep.errors if expect_level == "error"
                                   else rep.warnings)}
    ok = expect_check in fired
    RESULTS.append((ok, name, expect_check, sorted(fired)))
    return ok


def find(algo, defname):
    """First block of a given type, at any depth."""
    for _, blocks, _ in K.walk_graphs(algo["content"]):
        for b in blocks:
            if b.get("defName") == defname:
                return b
    raise AssertionError(f"no {defname} in this base algo")


def fresh(path=BASE):
    return K.load_algo(path)


def main():
    if not os.path.exists(BASE):
        print(f"missing {BASE}")
        return 1

    # --- C1: top-level shape ------------------------------------------------
    a = fresh(); del a["content"]
    check("C1 missing content", a, "C1")

    a = fresh(); a["variables"] = "not-a-list"
    check("C1 variables not a list", a, "C1")

    # --- C2: duplicate GUIDs (the most likely generation bug) ---------------
    a = fresh()
    blocks = [x for x in a["content"] if "defName" in x]
    blocks[1]["guid"] = blocks[0]["guid"]
    check("C2 duplicate guid", a, "C2")

    a = fresh()
    [x for x in a["content"] if "defName" in x][0].pop("guid")
    check("C2 block with no guid", a, "C2")

    # --- C3: edge endpoints -------------------------------------------------
    a = fresh()
    edge = next(x for x in a["content"] if x.get("className") == "Edge")
    edge["targetBlock"] = "00000000-0000-0000-0000-000000000000"
    check("C3 edge to nowhere", a, "C3")

    # --- C4: a connector GUID that belongs to no known port of that block ---
    # Swapping an edge's two connectors moves the TARGET block's input GUID into the
    # SOURCE block's slot. Since the two are different block types, the result is an
    # unknown connector (C4), not a reversed one - C5 needs a same-type violation.
    a = fresh()
    edge = next(x for x in a["content"] if x.get("className") == "Edge")
    edge["sourceConnector"], edge["targetConnector"] = (edge["targetConnector"],
                                                        edge["sourceConnector"])
    check("C4 connector unknown for that block", a, "C4", expect_level="warn")

    # --- C5: connector used in the wrong direction --------------------------
    # Feed an edge's source slot a GUID the catalog knows as an INPUT of that very
    # block type. The GUID is legitimate; the direction is not.
    a = fresh()
    cat = V.load_catalog_safe()
    fired = False
    if cat:
        idx = K.all_blocks(a)
        for edge in [x for x in a["content"] if x.get("className") == "Edge"]:
            sb = idx.get(edge.get("sourceBlock"))
            if not sb or sb["defName"] in K.PER_INSTANCE_CONNECTOR_BLOCKS:
                continue
            c = cat["blocks"].get(sb["defName"], {}).get("connectors", {})
            in_only = set(c.get("in", [])) - set(c.get("out", []))
            if in_only:
                edge["sourceConnector"] = sorted(in_only)[0]
                check("C5 in-port used as a source", a, "C5")
                fired = True
                break
    if not fired:
        RESULTS.append((True, "C5 skipped - no suitable edge in base algo", "C5", []))

    # --- C6: defId that disagrees with the catalog --------------------------
    a = fresh()
    find(a, "Branch")["defId"] = "DEADBEEF-0000-0000-0000-000000000000"
    check("C6 wrong defId", a, "C6")

    # --- C7: the three-way Group binding (needs an algo that has a Group) ---
    a = fresh(GROUP_BASE)
    conns = K.prop(find(a, "Group"), "connectors")
    conns.pop(sorted(conns.keys())[0])
    check("C7 undeclared inner Connector", a, "C7")

    a = fresh(GROUP_BASE)
    conns = K.prop(find(a, "Group"), "connectors")
    conns[sorted(conns.keys())[0]]["name"] = "RenamedOnParentOnly"
    check("C7 parent/inner name disagree", a, "C7")

    # --- C8: Jump / JumpLanding wormhole ------------------------------------
    a = fresh()
    j = find(a, "Jump")
    for p in j["properties"]:
        if p["name"] == "targetBlock":
            p["value"] = ["00000000-0000-0000-0000-000000000000"]
    check("C8 jump targets a ghost", a, "C8")

    a = fresh()
    j = find(a, "Jump")
    landing_guid = K.prop(j, "targetBlock")[0]
    landing = K.all_blocks(a)[landing_guid]
    for p in landing["properties"]:
        if p["name"] == "sourceBlock":
            p["value"] = "00000000-0000-0000-0000-000000000000"
    check("C8 landing does not point back", a, "C8")

    # --- C9 / C10: user-facing surfaces -------------------------------------
    a = fresh()
    a["variables"] = ["00000000-0000-0000-0000-000000000000"]
    check("C9 variable names a ghost", a, "C9")

    a = fresh()
    a["exports"] = ["not-a-valid-export"]
    check("C10 malformed export", a, "C10")

    a = fresh()
    a["exports"] = ["00000000-0000-0000-0000-000000000000."
                    "11111111-1111-1111-1111-111111111111"]
    check("C10 export names a ghost", a, "C10")

    # --- C11: formula referencing a block that does not exist ---------------
    a = fresh()
    tgt = None
    for _, bl, _ in K.walk_graphs(a["content"]):
        for b in bl:
            if isinstance(K.prop(b, "formula"), str) and K.formula_refs(
                    K.prop(b, "formula")):
                tgt = b
                break
        if tgt:
            break
    if tgt:
        for p in tgt["properties"]:
            if p["name"] == "formula":
                p["value"] = ("[00000000-0000-0000-0000-000000000000."
                              "11111111-1111-1111-1111-111111111111] > 0")
        check("C11 formula references a ghost", a, "C11")
    else:
        RESULTS.append((True, "C11 skipped - no formula refs in base algo", "C11", []))

    # --- C12: unknown message field (warning) -------------------------------
    a = fresh()
    b = find(a, "Branch")
    for p in b["properties"]:
        if p["name"] == "formula":
            p["value"] = "{noSuchFieldAnywhere} == 1"
    check("C12 unknown message field", a, "C12", expect_level="warn")

    # --- negative control: an untouched file must stay clean ----------------
    rep = V.validate(fresh(), "control", V.load_catalog_safe())
    RESULTS.append((rep.ok, "control: unmutated file stays clean", "-",
                    sorted({c for c, _, _ in rep.errors})))

    # --- report -------------------------------------------------------------
    width = max(len(n) for _, n, _, _ in RESULTS) + 2
    print("fault injection - each row corrupts one thing and expects one check\n")
    for ok, name, expected, fired in RESULTS:
        mark = "PASS" if ok else "FAIL"
        detail = "" if ok else f"   (fired: {', '.join(fired) or 'nothing'})"
        print(f"  {mark}  {name:<{width}} expects {expected}{detail}")
    passed = sum(1 for ok, *_ in RESULTS if ok)
    print(f"\n{passed}/{len(RESULTS)} fault-injection tests passed.")
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
