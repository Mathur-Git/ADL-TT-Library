#!/usr/bin/env python3
"""
profile_algo.py - one-file structural profile of a .adl.json.

lookup.py answers "what does block type X look like across the corpus". This answers
the opposite question: "what is inside THIS algo, and which parts of it can I lift".
It is the script behind every number in corpus-analysis/*.md - rerun it and the docs
are reproducible.

    python tools/profile_algo.py                      # one-line summary of all 13
    python tools/profile_algo.py MinVol --brief       # reuse decision only, ~1 KB
    python tools/profile_algo.py Conditional          # full profile (substring match)
    python tools/profile_algo.py Conditional --json   # same, machine-readable
    python tools/profile_algo.py --all                # full profile of every file

Prefer --brief, and prefer the prose in corpus-analysis/*.md over both: the full
profile is ~15 KB for a single file and mostly answers questions you did not ask.
Reach for it when you need exact wiring, formulas or order properties.

Sections, in the order a reuse decision needs them:

  SOURCE        flat vs true block count, subgraph count, max depth, mtime
  OPERATOR      `variables` resolved to name/value/bounds, `exports` resolved
  GRAPH TREE    nesting, Groups by name with port signature and patterns.py tier
  CENSUS        per-file block-type counts (NOT the corpus-wide figure lookup.py gives)
  JUMPS         every Jump name with fan-out - AMBER groups need these fed BY NAME
  ORDERS        Order / DiscreteOrder / SingleOrderContainer properties, incl. onExtMod
  STOP GAPS     Terminal, Alert, Stopwatch, IsNumber, MarketState, Exit - the safety layer
  FORMULAS      every formula string with its owning block, refs resolved to names
  GROUPS        per-Group reuse verdict: tier, ports, required inbound jumps, leaks

Everything printed is [V] - read off the file. Nothing here interprets runtime
behaviour; that is adl-kb's job.
"""

import argparse
import datetime
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adlkit as K
from patterns import Pattern

# Blocks whose custom names encode the safety design (spec section 7).
SAFETY_BLOCKS = ["Terminal", "Alert", "Stopwatch", "IsNumber", "MarketState", "Exit",
                 "Pause", "TimeAndSales"]
ORDER_BLOCKS = ["Order", "DiscreteOrder", "SingleOrderContainer", "OrderPool",
                "TrailingOrder"]


# ---------------------------------------------------------------------------

def graph_tree(algo):
    """[(depth, path, defName, label, n_blocks, n_edges), ...] over every subgraph."""
    rows = []
    for path, blocks, edges in K.walk_graphs(algo.get("content", [])):
        depth = path.count("/")
        rows.append({"path": path, "depth": depth,
                     "blocks": len(blocks), "edges": len(edges)})
    return rows


def profile(path):
    algo = K.load_algo(path)
    idx = K.all_blocks(algo)
    tree = graph_tree(algo)

    flat = [x for x in algo.get("content", []) if "defName" in x]
    census = Counter(b.get("defName") for b in idx.values())

    # ---- operator surface -------------------------------------------------
    variables = []
    for guid in algo.get("variables", []) or []:
        b = idx.get(guid)
        if b is None:
            variables.append({"guid": guid, "missing": True})
            continue
        p = K.props(b)
        variables.append({
            "guid": guid, "defName": b.get("defName"), "name": K.block_name(b),
            "value": p.get("value"), "min": p.get("minValue"), "max": p.get("maxValue"),
        })

    exports = []
    for ref in algo.get("exports", []) or []:
        bg = ref.split(".")[0]
        b = idx.get(bg)
        exports.append({"ref": ref, "block": K.block_name(b) if b else None,
                        "defName": b.get("defName") if b else None})

    # ---- jumps ------------------------------------------------------------
    jumps = defaultdict(lambda: {"jumps": 0, "landings": 0, "dead": 0})
    for b in idx.values():
        dn = b.get("defName")
        if dn == "Jump":
            nm = K.block_name(b)
            jumps[nm]["jumps"] += 1
            tgt = K.prop(b, "targetBlock") or []
            if not isinstance(tgt, list):
                tgt = [tgt]
            jumps[nm]["landings"] += len(tgt)
            if not tgt:
                jumps[nm]["dead"] += 1
        elif dn == "JumpLanding":
            pass  # counted via their Jump's targetBlock list

    # ---- safety layer -----------------------------------------------------
    safety = {}
    for dn in SAFETY_BLOCKS:
        hits = [b for b in idx.values() if b.get("defName") == dn]
        if not hits:
            continue
        rows = []
        for b in hits:
            p = K.props(b)
            row = {"name": K.block_name(b),
                   "custom": any(pr.get("hasCustomName") for pr in b.get("properties", []))}
            for key in ("timeInterval", "interval", "milliseconds", "formula", "mode",
                        "message", "severity", "resetOnFire", "time"):
                if key in p and p[key] not in (None, ""):
                    row[key] = p[key]
            rows.append(row)
        safety[dn] = rows

    # ---- order blocks -----------------------------------------------------
    orders = []
    for b in idx.values():
        if b.get("defName") in ORDER_BLOCKS:
            p = K.props(b)
            orders.append({
                "defName": b.get("defName"), "name": K.block_name(b),
                "props": {k: v for k, v in p.items()
                          if k not in ("name",) and v not in (None, "", [], {})},
            })

    # ---- Note blocks - TT's own commentary, verbatim ----------------------
    notes = [K.prop(b, "text") for b in idx.values()
             if b.get("defName") == "Note" and K.prop(b, "text")]

    # ---- formulas ---------------------------------------------------------
    formulas = []
    for b in idx.values():
        f = K.prop(b, "formula")
        if isinstance(f, str) and f.strip():
            resolved = f
            for bg, cg in K.formula_refs(f):
                tgt = idx.get(bg)
                label = f"@{K.block_name(tgt)}" if tgt else f"@<EXTERNAL {bg[:8]}>"
                resolved = resolved.replace(f"[{bg}.{cg}]", label)
            formulas.append({"owner": K.block_name(b), "defName": b.get("defName"),
                             "raw": f, "resolved": resolved,
                             "fields": sorted(K.formula_fields(f)),
                             "hasAst": K.prop(b, "formulaNodes") is not None})

    # ---- wiring -----------------------------------------------------------
    # Edges resolved to block labels. Connectors are rendered as their INDEX in the
    # catalog's port list for that block type (in0/out1...), because the file records
    # only GUIDs and ADL never writes a port label. What each index MEANS is [U]
    # except where adl-kb documents the block.
    cat = (K.load_catalog() or {}).get("blocks", {})

    def port_label(block, cguid, side):
        entry = cat.get(block.get("defName"), {}) if block else {}
        lst = (entry.get("connectors") or {}).get(side, [])
        if cguid in lst:
            return f"{side}{lst.index(cguid)}"
        if block and block.get("defName") == "Group":
            decl = (K.prop(block, "connectors") or {}).get(cguid) or {}
            return decl.get("name") or f"{side}?"
        if block and block.get("defName") == "Connector":
            return K.block_name(block)
        return f"{side}?"

    wiring = []
    for gpath, blocks, edges in K.walk_graphs(algo.get("content", [])):
        local = {b.get("guid"): b for b in blocks}
        rows = []
        for e in edges:
            s = local.get(e.get("sourceBlock"))
            t = local.get(e.get("targetBlock"))
            rows.append({
                "src": K.block_name(s) if s else "?", "srcDef": s.get("defName") if s else "?",
                "srcGuid": (e.get("sourceBlock") or "")[:8],
                "srcPort": port_label(s, e.get("sourceConnector"), "out"),
                "dst": K.block_name(t) if t else "?", "dstDef": t.get("defName") if t else "?",
                "dstGuid": (e.get("targetBlock") or "")[:8],
                "dstPort": port_label(t, e.get("targetConnector"), "in"),
            })
        wiring.append({"path": gpath, "edges": rows})

    # Jump wormholes resolved end to end: real upstream -> landing consumers.
    jump_wiring = []
    for j, landings in K.jump_links(algo):
        src = idx.get(K.prop(j, "sourceBlock"))
        consumers = []
        for L in landings:
            if L is None:
                consumers.append("<UNRESOLVED>")
                continue
            lg = L.get("guid")
            for _p, _b, es in K.walk_graphs(algo.get("content", [])):
                for e in es:
                    if e.get("sourceBlock") == lg:
                        tb = idx.get(e.get("targetBlock"))
                        consumers.append(K.block_name(tb) if tb else "?")
        jump_wiring.append({
            "name": K.block_name(j),
            "from": K.block_name(src) if src else "<none>",
            "fromDef": src.get("defName") if src else None,
            "to": consumers,
        })
    jump_wiring.sort(key=lambda r: str(r["name"]))

    # ---- groups -----------------------------------------------------------
    groups = []
    for g in K.iter_groups(algo):
        pat = Pattern(g, os.path.basename(path))
        groups.append({
            "name": pat.name, "guid": pat.guid, "tier": pat.tier,
            "blocks": len(pat.inner), "ports": pat.ports, "signature": pat.signature,
            "jumps_in": sorted(pat.jumps_in), "jumps_out": sorted(pat.jumps_out),
            "leaks": pat.formula_leaks, "edge_leaks": pat.edge_leaks,
            "virtual": bool(K.prop(g, "virtual")),
            "census": dict(pat.census.most_common()),
        })
    groups.sort(key=lambda g: -g["blocks"])

    # ---- custom names by type (design intent) -----------------------------
    labels = defaultdict(list)
    for b in idx.values():
        for pr in b.get("properties", []):
            if pr.get("name") == "name" and pr.get("hasCustomName") and pr.get("value"):
                labels[b.get("defName")].append(pr.get("value"))
                break

    mtime = algo.get("lastModifiedTime")
    return {
        "file": os.path.basename(path),
        "algoName": algo.get("name"),
        "algoId": algo.get("id"),
        "description": algo.get("description"),
        "orderSide": algo.get("orderSide"),
        "ignoreMarketState": algo.get("ignoreMarketState"),
        "isSOA": algo.get("isSOA"), "isOmaOta": algo.get("isOmaOta"),
        "showInMDT": algo.get("showInMDT"),
        "lastModified": (datetime.datetime.utcfromtimestamp(mtime / 1000).isoformat() + "Z"
                         if isinstance(mtime, (int, float)) else None),
        "sizeBytes": os.path.getsize(path),
        "flatBlocks": len(flat), "trueBlocks": len(idx),
        "subgraphs": len(tree) - 1, "maxDepth": max(r["depth"] for r in tree),
        "edges": sum(r["edges"] for r in tree),
        "tree": tree, "census": dict(census.most_common()),
        "variables": variables, "exports": exports,
        "jumps": {k: v for k, v in sorted(jumps.items(), key=lambda kv: -kv[1]["landings"])},
        "safety": safety, "orders": orders, "formulas": formulas, "groups": groups,
        "wiring": wiring, "jumpWiring": jump_wiring, "notes": notes,
        "labels": {k: sorted(set(v)) for k, v in sorted(labels.items())},
    }


# ---------------------------------------------------------------------------

def show(p):
    W = 78
    print("=" * W)
    print(f"{p['algoName']}   [{p['file']}]")
    print("=" * W)
    print(f"  id {p['algoId']}   modified {p['lastModified']}   {p['sizeBytes']:,} bytes")
    print(f"  flat blocks {p['flatBlocks']}   TRUE blocks {p['trueBlocks']}   "
          f"edges {p['edges']}")
    print(f"  subgraphs {p['subgraphs']}   max depth {p['maxDepth']}   "
          f"orderSide={p['orderSide']}  ignoreMarketState={p['ignoreMarketState']}  "
          f"isOmaOta={p['isOmaOta']}")

    print("\n-- OPERATOR SURFACE " + "-" * (W - 20))
    if not p["variables"]:
        print("  variables: none (nothing is editable at launch)")
    for v in p["variables"]:
        if v.get("missing"):
            print(f"  !! variable {v['guid']} resolves to no block")
            continue
        b = ""
        if v["min"] is not None or v["max"] is not None:
            b = f"   bounds [{v['min']}, {v['max']}]"
        print(f"  {v['defName']:<10} {str(v['name'])[:34]:<34} = {v['value']}{b}")
    for e in p["exports"]:
        print(f"  export -> {e['block']} ({e['defName']})   {e['ref']}")
    if not p["exports"]:
        print("  exports: none (no dashboard column)")

    print("\n-- GRAPH TREE " + "-" * (W - 14))
    for r in p["tree"]:
        print(f"  {'  ' * r['depth']}{r['path'].split('/')[-1]:<28} "
              f"{r['blocks']:>4} blocks {r['edges']:>4} edges")

    print("\n-- BLOCK CENSUS (this file) " + "-" * (W - 28))
    items = list(p["census"].items())
    for i in range(0, len(items), 3):
        print("  " + "".join(f"{k:<22}{v:<5}" for k, v in items[i:i + 3]))

    print("\n-- JUMP NAMES " + "-" * (W - 14))
    for nm, d in p["jumps"].items():
        dead = "  (DEAD - no landing)" if d["dead"] else ""
        print(f"  {str(nm)[:40]:<40} {d['jumps']} jump -> {d['landings']} landings{dead}")
    if not p["jumps"]:
        print("  none")

    print("\n-- ORDER BLOCKS " + "-" * (W - 16))
    for o in p["orders"]:
        print(f"  {o['defName']}  '{o['name']}'")
        for k, v in o["props"].items():
            s = json.dumps(v) if not isinstance(v, str) else v
            print(f"      {k}: {s[:120]}")
    if not p["orders"]:
        print("  none")

    print("\n-- STOP GAPS " + "-" * (W - 13))
    for dn, rows in p["safety"].items():
        print(f"  {dn} ({len(rows)}):")
        for r in rows:
            extra = "  ".join(f"{k}={json.dumps(v)[:60]}" for k, v in r.items()
                              if k not in ("name", "custom"))
            print(f"      {str(r['name'])[:44]:<44} {extra}")
    if not p["safety"]:
        print("  NONE - no Terminal, Alert, Stopwatch, IsNumber or MarketState anywhere")

    if p["notes"]:
        print("\n-- NOTE BLOCKS (TT's own commentary, verbatim) " + "-" * (W - 46))
        for n in p["notes"]:
            print("  * " + str(n).replace("\n", " ")[:900])

    print("\n-- FORMULAS " + "-" * (W - 12))
    for f in p["formulas"]:
        ast = "" if f["hasAst"] else "   [no formulaNodes AST]"
        print(f"  {f['defName']} '{f['owner']}'{ast}")
        print(f"      {f['resolved'][:160]}")
    if not p["formulas"]:
        print("  none")

    print("\n-- WIRING (edges, per graph) " + "-" * (W - 29))
    for g in p["wiring"]:
        if not g["edges"]:
            continue
        print(f"  [{g['path']}]")
        for e in g["edges"]:
            s = f"{e['src']}~{e['srcGuid']} ({e['srcDef']})"
            d = f"{e['dst']}~{e['dstGuid']} ({e['dstDef']})"
            print(f"    {s[:44]:<44} {e['srcPort']:>5} -> {e['dstPort']:<5} {d[:44]}")

    print("\n-- JUMP WORMHOLES (resolved) " + "-" * (W - 29))
    for j in p["jumpWiring"]:
        print(f"  {str(j['name'])[:34]:<34} {j['from']} ({j['fromDef']})"
              f"  ->  {', '.join(j['to']) or '<nothing>'}")

    print("\n-- GROUPS / REUSE " + "-" * (W - 18))
    for g in p["groups"]:
        v = " virtual" if g["virtual"] else ""
        print(f"  [{g['tier']}] {str(g['name'])[:32]:<32} {g['blocks']:>4} blocks{v}")
        print(f"        ports: {g['signature']}")
        for port in g["ports"]:
            print(f"          {'in ' if port['input'] else 'out'} {port['type']:<8} "
                  f"{port['name']}")
        if g["jumps_in"]:
            print(f"        REQUIRES inbound jumps: {', '.join(g['jumps_in'])}")
        if g["jumps_out"]:
            print(f"        emits jumps consumed outside: {', '.join(g['jumps_out'])}")
        if g["leaks"]:
            print(f"        FORMULA LEAKS ({len(g['leaks'])}): "
                  + ", ".join(sorted({n for n, _ in g['leaks']}))[:100])
        if g["edge_leaks"]:
            print(f"        EDGE LEAKS: {g['edge_leaks']}")
    if not p["groups"]:
        print("  none - single flat graph")

    print("\n-- CUSTOM LABELS BY BLOCK TYPE " + "-" * (W - 31))
    for dn, names in p["labels"].items():
        print(f"  {dn} ({len(names)}): " + " | ".join(names)[:400])
    print()


def brief(p):
    """The reuse decision only - shape, operator surface, Groups, safety headcount.

    Full `show` runs to ~15 KB for one file, which is far more than "is there
    anything in here worth lifting" needs. Drops census, jumps, orders, formulas,
    wiring, wormholes and labels; reach for those, or for the prose in
    corpus-analysis/, once this says there is something to reach for.
    """
    W = 78
    stem = p["file"].replace(".adl.json", "").strip()
    flags = " ".join(f for f, on in [("SOA", p["isSOA"]), ("OMA/OTA", p["isOmaOta"]),
                                     ("ignoreMktState", p["ignoreMarketState"])] if on)
    print("=" * W)
    print(f"{p['algoName']}   [{p['file']}]   {flags}")
    print(f"  {p['trueBlocks']} blocks / {p['edges']} edges / {p['subgraphs']} subgraphs "
          f"/ depth {p['maxDepth']} / {len(p['formulas'])} formulas")

    print(f"\n  OPERATOR ({len(p['variables'])} variables, {len(p['exports'])} exports)")
    for v in p["variables"]:
        if v.get("missing"):
            print(f"    !! {v['guid']} resolves to no block")
            continue
        b = (f"  [{v['min']}, {v['max']}]"
             if v["min"] is not None or v["max"] is not None else "")
        print(f"    {str(v['name'])[:38]:<38} = {str(v['value'])[:14]}{b}")
    if not p["variables"]:
        print("    none - nothing is editable at launch")

    print(f"\n  GROUPS ({len(p['groups'])})")
    for g in p["groups"]:
        need = f"  needs jumps: {', '.join(g['jumps_in'])}" if g["jumps_in"] else ""
        leak = f"  {len(g['leaks'])} formula leak(s)" if g["leaks"] else ""
        print(f"    [{g['tier']}] {str(g['name'])[:26]:<26} {g['blocks']:>4}b  "
              f"{g['signature']}{need}{leak}")
    if not p["groups"]:
        print("    none - single flat graph, nothing to lift")

    safety = ", ".join(f"{dn}x{len(rows)}" for dn, rows in p["safety"].items())
    print(f"\n  SAFETY   {safety or 'NONE - no Terminal/Alert/Stopwatch/IsNumber/MarketState'}")
    print(f"  prose    ADL-jsons/corpus-analysis/ - read that before the full profile")
    print(f'  full     python tools/profile_algo.py "{stem}"\n')


def one_line(p):
    return (f"{p['file']:<34} {p['trueBlocks']:>5} blocks  {p['subgraphs']:>3} subgraphs  "
            f"depth {p['maxDepth']}  {len(p['variables']):>2} vars  "
            f"{len(p['groups']):>3} groups  {len(p['formulas']):>3} formulas")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name", nargs="?", help="substring of a corpus file name")
    ap.add_argument("--all", action="store_true", help="full profile of every file")
    ap.add_argument("--brief", action="store_true",
                    help="shape, operator surface, Groups and safety headcount only "
                         "(~1 KB vs ~15 KB) - enough for a reuse decision")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()

    files = K.corpus_files()
    if a.name:
        files = [f for f in files if a.name.lower() in os.path.basename(f).lower()]
        if not files:
            print(f"no corpus file matching '{a.name}'")
            return 1

    if a.name or a.all or a.brief:
        profs = [profile(f) for f in files]
        if a.json:
            print(json.dumps(profs if len(profs) > 1 else profs[0], indent=1))
        else:
            for p in profs:
                (brief if a.brief else show)(p)
        return 0

    for f in files:
        print(one_line(profile(f)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
