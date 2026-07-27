#!/usr/bin/env python3
"""
lookup.py  -  query block-catalog.json without reading 375 KB of JSON.

The catalog is the wiring table for generating .adl.json files: it maps each block type
to its defId and its connector GUIDs, which appear nowhere else (blocks don't declare
their own ports; only edges reference connector GUIDs).

    python lookup.py                      # every block type, by frequency
    python lookup.py Number               # defId, connectors, properties for one type
    python lookup.py order                # substring search across type names
    python lookup.py --names Stopwatch    # custom instance names TT gave this block
    python lookup.py --props Order tif    # observed values for one property
    python lookup.py --missing            # blocks adl-kb documents but the corpus lacks

Everything reported is OBSERVED in the 13-algo corpus. Absence means "not in these
files", never "impossible in ADL". Connector lists are a floor, not a block's full
port count. See README.md §3.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG = os.path.join(HERE, "block-catalog.json")

# Blocks adl-kb documents that have no defName anywhere in the corpus, so their defId
# and connector GUIDs are unknown and cannot be guessed.
#
# Derived by walking every block page under adl-kb/reference/*-blocks/ and matching it
# against the corpus defNames  -  not guessed. Page titles and defNames differ (the
# "Bool block" is defName "Boolean"), so the mapping is by hand.
#
# NOT listed here, despite having no dedicated defName: Abs, Min, Max, Log, Pow, Sqrt,
# Floor, Ceiling, Sign, Truncate and the trig functions. Those are all values of the
# Math block's `mathFunction` property, not blocks. Use Math.
KNOWN_ABSENT = {
    "Analytics": "Analytics block  -  OHLCV bars + ATR/Bollinger/MACD/SMA/EMA/RSI/Stochastic",
    "Pnl": "Pnl block",
    "PositionRisk": "Position Risk block",
    "MovingAverage": "Moving Average block (discrete)",
    "RandomNumber": "Random Number block",
    "Average": "Average block (arithmetic)",
    "Mod": "Mod block",
    "DiscreteMin": "Discrete Min half of the Discrete Min/Max blocks (DiscreteMax IS in corpus)",
}


def load():
    if not os.path.exists(CATALOG):
        sys.exit("block-catalog.json not found  -  run: python extract_schema.py")
    with open(CATALOG, encoding="utf-8") as fh:
        return json.load(fh)


def list_all(cat):
    blocks = cat["blocks"]
    meta = cat["_meta"]
    print(f"{meta['distinctBlockTypes']} block types, {meta['totalBlocks']} instances, "
          f"{len(meta['corpusFiles'])} algos, max Group nesting depth {meta['maxGroupNestingDepth']}\n")
    rows = sorted(blocks.items(), key=lambda kv: -kv[1]["instances"])
    print(f"{'block':<22}{'count':>7}{'files':>7}{'in':>5}{'out':>5}")
    print("-" * 46)
    for name, b in rows:
        c = b["connectors"]
        print(f"{name:<22}{b['instances']:>7}{b['filesSeenIn']:>7}"
              f"{len(c['in']):>5}{len(c['out']):>5}")
    print("\n'in'/'out' = distinct connector GUIDs observed WIRED  -  a floor, not the")
    print("block's full port count. Group connectors are per-instance; ignore its counts.")


def show(cat, name):
    blocks = cat["blocks"]
    if name not in blocks:
        hits = [k for k in blocks if name.lower() in k.lower()]
        if not hits:
            if name in KNOWN_ABSENT:
                print(f"{name}: documented in adl-kb as '{KNOWN_ABSENT[name]}' but ABSENT "
                      f"from the corpus.\nNo defId or connector GUIDs are known. To close the "
                      f"gap: build a throwaway algo\ncontaining it in ADL, export it here, "
                      f"re-run extract_schema.py.")
            else:
                print(f"No block type matching '{name}'. Try: python lookup.py --missing")
            return
        if len(hits) > 1:
            print(f"{len(hits)} matches: {', '.join(sorted(hits))}")
            return
        name = hits[0]

    b = blocks[name]
    print(f"=== {name} ===")
    print(f"defId       {b['defId']}   (stable across corpus: {b['defIdStable']})")
    print(f"instances   {b['instances']} across {b['filesSeenIn']} files")

    if name == "Group":
        print("\n!! Group connectors are PER-INSTANCE, declared inline in its 'connectors'")
        print("   property, and must match Connector blocks inside internalAlgo.content.")
        print("   Mint fresh GUIDs; the lists below are a meaningless aggregate. README.md §3.")

    for role in ("in", "out"):
        guids = b["connectors"][role]
        print(f"\n{role.upper()} connectors ({len(guids)} observed wired):")
        for g in guids:
            print(f"  {g}")

    props = b.get("properties", {})
    if props:
        print(f"\nproperties ({len(props)}):")
        for pn, pv in props.items():
            vals = pv.get("observedValues", [])
            shown = ", ".join(vals[:6]) if vals else "<complex/none>"
            if len(vals) > 6:
                shown += f", ... (+{len(vals) - 6})"
            print(f"  {pn:<24} {pv.get('type') or '?':<8} {shown}")


def names(cat, name):
    by_block = cat.get("customNamesByBlock", {})
    if name not in by_block:
        print(f"No custom names recorded for '{name}'.")
        return
    seen = {}
    for fname, label in by_block[name]:
        seen.setdefault(label, []).append(fname)
    print(f"=== custom names on {name} ({len(seen)} distinct) ===")
    print("These are TT's own labels  -  the clearest evidence of design intent.\n")
    for label, files in sorted(seen.items(), key=lambda kv: -len(kv[1])):
        print(f"  {label:<44} ({len(files)}x)")


def props(cat, name, prop):
    b = cat["blocks"].get(name)
    if not b:
        print(f"No block type '{name}'.")
        return
    matches = {k: v for k, v in b["properties"].items() if prop.lower() in k.lower()}
    if not matches:
        print(f"{name} has no property matching '{prop}'. "
              f"Has: {', '.join(sorted(b['properties']))}")
        return
    for pn, pv in matches.items():
        print(f"{name}.{pn}  ({pv.get('type')})")
        for v in pv.get("observedValues", []):
            print(f"    {v}")


def missing(cat):
    present = set(cat["blocks"])
    absent = {k: v for k, v in KNOWN_ABSENT.items() if k not in present}
    print("Blocks adl-kb documents but the corpus does NOT contain.")
    print("defId and connector GUIDs unknown  -  these CANNOT be emitted into a .adl.json.\n")
    for defname, title in sorted(absent.items()):
        print(f"  {defname:<18} {title}")
    print(f"\n{len(absent)} blocks. Each is one throwaway ADL export away from being usable:")
    print("build it on a blank canvas, export here, run extract_schema.py.")
    print("\nAnalytics, Pnl and PositionRisk are the costly ones  -  indicators and live")
    print("risk are hard to substitute for. The rest have workarounds:")
    print("  Average / MovingAverage  -> ValueAccumulator + Divide, or Analytics")
    print("  Mod                      -> Math(IEEERemainder) or Subtract+Math(Floor)+Multiply")
    print("  DiscreteMin              -> negate, DiscreteMax, negate back")
    print("\nMath functions (Abs, Min, Max, Log, Pow, Sqrt, Floor, Ceiling, Sign, trig) are")
    print("NOT missing  -  they are values of Math.mathFunction. `python lookup.py Math`.")


def main():
    cat = load()
    args = sys.argv[1:]
    if not args:
        list_all(cat)
    elif args[0] == "--missing":
        missing(cat)
    elif args[0] == "--names" and len(args) > 1:
        names(cat, args[1])
    elif args[0] == "--props" and len(args) > 2:
        props(cat, args[1], args[2])
    else:
        show(cat, args[0])


if __name__ == "__main__":
    main()
