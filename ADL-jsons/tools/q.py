#!/usr/bin/env python3
"""
q.py - ad-hoc corpus queries, so they stop being hand-written every session.

This script exists for one measured reason: across 23 sessions, 28 near-identical
throwaway `python -c` scripts were written against adlkit, and 26 of them were the
same query - "dump the properties of blocks of type T in file F, minus the cosmetic
ones". That is a subcommand, not an inline script. Writing it inline costs tokens
twice (composing it, then reading its unbudgeted output) and silently drops adlkit's
recursion rules whenever the inline version forgets to use walk_graphs.

    python tools/q.py props MinVol Number Field      # the 26-times query
    python tools/q.py props MinVol                   # no types -> census, pick one
    python tools/q.py props Sniper Order --full      # include ASTs and port decls
    python tools/q.py props MinVol Group --name Vol  # filter by custom label

    python tools/q.py grep "throttle"                # names+formulas+notes, all 13
    python tools/q.py grep "\\{fillQuantity\\}" --in BrackeTT

    python tools/q.py notes Conditional              # TT's verbatim commentary
    python tools/q.py block MinVol 3f2a91bc          # one block + its wiring

Everything printed is [V] - read off the file, never interpreted. Which corpus file
a match came from is always shown, because a claim sourced to one TT algo is weaker
than the same claim in six.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adlkit as K

# Layout/appearance only - never load-bearing, always noise in a dump.
COSMETIC = {"dimensions", "bodyColor", "color", "x", "y", "position", "zOrder",
            "viewport", "bookmarks", "collapsed", "fontSize"}

# Load-bearing but enormous. Summarised rather than hidden, because a transplant
# decision genuinely depends on them - see the 3-way Group port agreement rule.
BULKY = {"formulaNodes", "connectors", "generic"}


def pick_file(name):
    """Resolve a substring to exactly one corpus file, or exit explaining why not."""
    files = K.corpus_files()
    if not name:
        return files
    hits = [f for f in files if name.lower() in os.path.basename(f).lower()]
    if not hits:
        avail = ", ".join(os.path.basename(f).replace(".adl.json", "") for f in files)
        sys.exit(f"no corpus file matching '{name}'.\navailable: {avail}")
    if len(hits) > 1:
        names = ", ".join(os.path.basename(f) for f in hits)
        sys.exit(f"'{name}' is ambiguous: {names}")
    return hits


def graph_of(algo):
    """{guid: graph_path} so a dump can say WHERE in the nesting a block lives."""
    out = {}
    for path, blocks, _edges in K.walk_graphs(algo.get("content", [])):
        for b in blocks:
            out[b.get("guid")] = path
    return out


def summarise_bulky(key, val):
    """A one-line stand-in for a property too big to print."""
    if val is None:
        return None
    if key == "formulaNodes":
        return f"<AST present, {len(json.dumps(val))} bytes - do not hand-author>"
    if key == "connectors" and isinstance(val, dict):
        parts = []
        for cguid, decl in val.items():
            d = decl if isinstance(decl, dict) else {}
            side = "in" if d.get("input") else "out"
            parts.append(f"{side}:{d.get('name', '?')}({d.get('type', '?')})~{cguid[:8]}")
        return f"<{len(val)} ports> " + ", ".join(parts)
    if key == "generic" and isinstance(val, dict):
        return "<port types> " + ", ".join(f"{k[:8]}={v}" for k, v in val.items())
    return f"<{len(json.dumps(val))} bytes>"


def dump_block(b, gpath, maxlen, full):
    guid = b.get("guid") or "?"
    label = K.block_name(b)
    print(f"### {b.get('defName')}  '{label}'  ~{guid[:8]}  [{gpath}]")
    for p in b.get("properties", []):
        key = p.get("name")
        if key == "name":
            continue
        if key in COSMETIC and not full:
            continue
        val = p.get("value")               # quirk 2: may be absent entirely
        if key in BULKY and not full:
            s = summarise_bulky(key, val)
            if s is None:
                continue
            print(f"    {key} = {s[:maxlen]}")
            continue
        if val in (None, "", [], {}):
            continue
        s = val if isinstance(val, str) else json.dumps(val)
        print(f"    {key} = {s[:maxlen]}")


def cmd_props(a):
    for path in pick_file(a.algo):
        algo = K.load_algo(path)
        idx = K.all_blocks(algo)
        gmap = graph_of(algo)

        if not a.types:
            from collections import Counter
            census = Counter(b.get("defName") for b in idx.values())
            print(f"=== {os.path.basename(path)} - {len(idx)} blocks, "
                  f"{len(census)} types. Name one or more: ===")
            items = list(census.most_common())
            for i in range(0, len(items), 3):
                print("  " + "".join(f"{k:<24}{v:<5}" for k, v in items[i:i + 3]))
            continue

        wanted = [t.lower() for t in a.types]
        hits = [b for b in idx.values()
                if any(w in (b.get("defName") or "").lower() for w in wanted)]
        if a.name:
            hits = [b for b in hits if a.name.lower() in str(K.block_name(b)).lower()]
        hits.sort(key=lambda b: (b.get("defName") or "", str(K.block_name(b))))

        print(f"=== {os.path.basename(path)} - {len(hits)} matching block(s) ===")
        for b in hits:
            dump_block(b, gmap.get(b.get("guid"), "?"), a.max, a.full)
        if not hits:
            print(f"  no block whose defName contains any of: {', '.join(a.types)}")
            print("  (defName != KB page title - check: python tools/lookup.py <name>)")


def cmd_grep(a):
    try:
        rx = re.compile(a.pattern, re.I)
    except re.error as e:
        sys.exit(f"bad regex: {e}")

    total = 0
    for path in pick_file(a.in_file):
        algo = K.load_algo(path)
        idx = K.all_blocks(algo)
        gmap = graph_of(algo)
        rows = []
        for b in idx.values():
            guid, dn = b.get("guid"), b.get("defName")
            label = str(K.block_name(b))
            where = gmap.get(guid, "?")
            if rx.search(label):
                rows.append((dn, "name", label, guid, where))
            for key in ("formula", "text", "message"):
                v = K.prop(b, key)
                if isinstance(v, str) and rx.search(v):
                    rows.append((dn, key, re.sub(r"\s+", " ", v), guid, where))
        if not rows:
            continue
        total += len(rows)
        print(f"=== {os.path.basename(path)} - {len(rows)} hit(s) ===")
        for dn, kind, text, guid, where in rows:
            print(f"  {dn:<20} {kind:<8} ~{guid[:8]}  {text[:a.max]}")
            if a.paths:
                print(f"      [{where}]")
    print(f"\n{total} hit(s) total. A pattern found in ONE algo is weaker evidence "
          f"than one found in six.")


def cmd_notes(a):
    for path in pick_file(a.algo):
        algo = K.load_algo(path)
        notes = [(K.block_name(b), K.prop(b, "text"))
                 for b in K.all_blocks(algo).values()
                 if b.get("defName") == "Note" and K.prop(b, "text")]
        print(f"=== {os.path.basename(path)} - {len(notes)} Note block(s) ===")
        for label, text in notes:
            print(f"  * [{label}] {re.sub(chr(10), ' ', str(text))[:1200]}")
        if not notes:
            print("  none - TT left no commentary in this file")


def cmd_block(a):
    for path in pick_file(a.algo):
        algo = K.load_algo(path)
        idx = K.all_blocks(algo)
        gmap = graph_of(algo)

        hits = [b for g, b in idx.items()
                if g.startswith(a.ref) or a.ref.lower() in str(K.block_name(b)).lower()]
        if not hits:
            print(f"no block in {os.path.basename(path)} matching '{a.ref}'")
            continue
        if len(hits) > 5:
            print(f"'{a.ref}' matches {len(hits)} blocks - narrow it:")
            for b in hits[:20]:
                print(f"  ~{b.get('guid')[:8]}  {b.get('defName'):<20} {K.block_name(b)}")
            continue

        for b in hits:
            guid = b.get("guid")
            dump_block(b, gmap.get(guid, "?"), a.max, a.full)

            # Edges touching it. Quirk 4: both endpoints share the block's own graph.
            for gp, blocks, edges in K.walk_graphs(algo.get("content", [])):
                local = {x.get("guid"): x for x in blocks}
                if guid not in local:
                    continue
                for e in edges:
                    if e.get("sourceBlock") == guid:
                        t = local.get(e.get("targetBlock"))
                        print(f"    --> {K.block_name(t) if t else '?'} "
                              f"({t.get('defName') if t else '?'})")
                    elif e.get("targetBlock") == guid:
                        s = local.get(e.get("sourceBlock"))
                        print(f"    <-- {K.block_name(s) if s else '?'} "
                              f"({s.get('defName') if s else '?'})")

            # Quirk 5: Jump/JumpLanding link by property, so edges alone miss them.
            for j, landings in K.jump_links(algo):
                if j.get("guid") == guid or any(L is not None and L.get("guid") == guid
                                                for L in landings):
                    src = idx.get(K.prop(j, "sourceBlock"))
                    print(f"    ~~> jump '{K.block_name(j)}' from "
                          f"{K.block_name(src) if src else '<none>'} "
                          f"to {len(landings)} landing(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max", type=int, default=300, help="truncate values (default 300)")
    ap.add_argument("--full", action="store_true",
                    help="include cosmetic props and full ASTs / port declarations")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("props", help="dump block properties in one algo")
    p.add_argument("algo", help="substring of a corpus file name")
    p.add_argument("types", nargs="*", help="defName substrings; omit for a census")
    p.add_argument("--name", help="only blocks whose custom label contains this")
    p.set_defaults(fn=cmd_props)

    p = sub.add_parser("grep", help="regex over custom names, formulas and notes")
    p.add_argument("pattern")
    p.add_argument("--in", dest="in_file", help="restrict to one corpus file")
    p.add_argument("--paths", action="store_true", help="also print the graph path")
    p.set_defaults(fn=cmd_grep)

    p = sub.add_parser("notes", help="TT's own Note-block commentary, verbatim")
    p.add_argument("algo")
    p.set_defaults(fn=cmd_notes)

    p = sub.add_parser("block", help="one block in full, with its edges and jumps")
    p.add_argument("algo")
    p.add_argument("ref", help="GUID prefix or custom-name substring")
    p.set_defaults(fn=cmd_block)

    a = ap.parse_args()
    a.fn(a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
