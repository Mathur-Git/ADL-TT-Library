#!/usr/bin/env python3
"""
patterns.py - find reusable parts of TT's algos and transplant them into a new one.

## Why this exists

When you are building a new algo, some of it has almost certainly been solved already
inside one of the 13 TT algos in this folder. This tool answers three questions:

    what reusable parts exist?          python tools/patterns.py
    which one fits what I'm doing?      python tools/patterns.py --search throttle
    what would it cost me to use it?    python tools/patterns.py --show "Mkt Price"
    give me a copy I can paste in       python tools/patterns.py --extract "Mkt Price" -o out.json

## Why the unit is the Group block

A Group is ADL's own encapsulation: a subgraph with a DECLARED, TYPED interface (its
`connectors` property). That interface is what makes an apples-to-apples comparison
possible - two Groups are interchangeable when their port signatures match, and a
Group's cost to adopt is exactly its list of external dependencies.

It is also the safest thing to copy. Every byte of a transplanted Group except the
GUIDs was written by ADL itself, including the `formulaNodes` ASTs that you must never
hand-author (see OPEN-QUESTIONS.md Q2). Transplanting sidesteps the riskiest part of
generation entirely.

And TT does it themselves: `Alerts`, `Mkt Price`, `CalculatedOrder` and
`PriceOrQtyChanged` appear byte-identical across four different TT algos. This is how
these algos were built.

## The three tiers

    GREEN  self-contained. Wire its declared ports and it works.
    AMBER  needs named Jump wormholes re-pointed. Jump/JumpLanding cross group
           boundaries freely, so a Group commonly expects inbound data by jump name
           rather than through a port. Mechanical, but you must supply each one.
    RED    a formula inside references a block OUTSIDE the group. Those references
           dangle after extraction and can only be fixed by editing a formula - which
           means touching a formulaNodes AST. Avoid unless the pattern is worth it.
"""

import argparse
import copy
import json
import os
import sys
import uuid
from collections import Counter, defaultdict

import adlkit as K


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

class Pattern:
    """One Group instance found in one corpus file."""

    def __init__(self, group, source_file):
        self.group = group
        self.file = source_file
        self.name = K.block_name(group)
        self.guid = group.get("guid")

        self.inner = K.descendants(group)
        self.inner_guids = {b.get("guid") for b in self.inner}
        self.census = Counter(b.get("defName") for b in self.inner)

        declared = K.prop(group, "connectors") or {}
        self.ports = []
        for cguid, d in (declared.items() if isinstance(declared, dict) else []):
            self.ports.append({
                "guid": cguid,
                "name": d.get("name"),
                "type": d.get("type"),
                "input": bool(d.get("input")),
            })
        self.ports.sort(key=lambda p: (not p["input"], p["name"] or ""))

        self.jumps_in = set()      # landing inside, Jump outside -> we need a feeder
        self.jumps_out = set()     # Jump inside, landing outside -> we may need sinks
        self.formula_leaks = []    # (blockName, referencedGuid) - the RED problem
        self.edge_leaks = 0

        for b in self.inner:
            dn = b.get("defName")
            if dn == "JumpLanding" and K.prop(b, "sourceBlock") not in self.inner_guids:
                self.jumps_in.add(K.block_name(b))
            if dn == "Jump":
                for t in (K.prop(b, "targetBlock") or []):
                    if t not in self.inner_guids:
                        self.jumps_out.add(K.block_name(b))
            text = K.prop(b, "formula")
            for bg, _cg in K.formula_refs(text):
                if bg not in self.inner_guids:
                    self.formula_leaks.append((K.block_name(b), bg))
        for e in K.descendant_edges(group):
            if (e.get("sourceBlock") not in self.inner_guids
                    or e.get("targetBlock") not in self.inner_guids):
                self.edge_leaks += 1

    @property
    def tier(self):
        if self.formula_leaks or self.edge_leaks:
            return "RED"
        if self.jumps_in or self.jumps_out:
            return "AMBER"
        return "GREEN"

    @property
    def signature(self):
        """Port signature - two Groups with the same one are drop-in comparable."""
        return " ".join(f"{'in' if p['input'] else 'out'}:{p['type']}"
                        for p in self.ports) or "(no ports)"

    @property
    def identity(self):
        """Groups that are the same reusable part, even in different files."""
        return (self.name, self.signature, len(self.inner))

    def haystack(self):
        """Text a --search term is matched against."""
        bits = [self.name, self.signature]
        bits += [p["name"] or "" for p in self.ports]
        bits += list(self.census)
        bits += [K.block_name(b) for b in self.inner]
        bits += list(self.jumps_in) + list(self.jumps_out)
        return " ".join(str(x) for x in bits).lower()


def collect(folder=K.CORPUS_DIR):
    out = []
    for path in K.corpus_files(folder):
        algo = K.load_algo(path)
        for g in K.iter_groups(algo):
            out.append(Pattern(g, os.path.basename(path)))
    return out


def dedupe(patterns):
    """Collapse the same part appearing in several files. Returns [(pattern, [files])]."""
    by = defaultdict(list)
    for p in patterns:
        by[p.identity].append(p)
    rows = [(v[0], sorted({x.file for x in v})) for v in by.values()]
    rows.sort(key=lambda r: ({"GREEN": 0, "AMBER": 1, "RED": 2}[r[0].tier],
                             -len(r[1]), -len(r[0].inner)))
    return rows


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

TIER_NOTE = ("GREEN = wire its ports and go.  AMBER = also supply each inbound Jump "
             "by name.\nRED = a formula reaches outside the group; adopting it means "
             "formula surgery.")


def cmd_index(rows, show_all=False):
    counts = Counter(p.tier for p, _ in rows)
    print(f"{len(rows)} distinct reusable Groups across the corpus "
          f"({sum(len(f) for _, f in rows)} instances)")
    print(f"GREEN {counts['GREEN']}   AMBER {counts['AMBER']}   RED {counts['RED']}\n")
    print(f"{'tier':6}{'name':<30}{'blk':>4}{'port':>5}{'jIn':>4}{'jOut':>5}"
          f"{'files':>6}  signature")
    print("-" * 100)
    shown = rows if show_all else [r for r in rows if not r[0].name.startswith("Group")]
    for p, files in shown:
        print(f"{p.tier:6}{p.name[:29]:<30}{len(p.inner):>4}{len(p.ports):>5}"
              f"{len(p.jumps_in):>4}{len(p.jumps_out):>5}{len(files):>6}  "
              f"{p.signature[:38]}")
    hidden = len(rows) - len(shown)
    if hidden:
        print(f"\n({hidden} auto-named 'GroupN' patterns hidden - pass --all to see "
              f"them. TT left them\nunnamed, so they carry no design intent in their "
              f"title; judge those by signature.)")
    print(f"\n{TIER_NOTE}")


def cmd_search(rows, term):
    t = term.lower()
    hits = [(p, f) for p, f in rows if t in p.haystack()]
    if not hits:
        print(f"Nothing matches '{term}'. Try a block type (Stopwatch, Alert), a port "
              f"name,\nor a concept TT would have labelled (throttle, cover, requote).")
        return
    print(f"{len(hits)} pattern(s) matching '{term}':\n")
    for p, files in hits:
        print(f"  [{p.tier}] {p.name}  -  {len(p.inner)} blocks, {len(p.ports)} ports")
        print(f"        {p.signature}")
        top = ", ".join(f"{k}x{v}" for k, v in p.census.most_common(5))
        print(f"        contains: {top}")
        print(f"        in: {', '.join(files)}")
        print(f"        details: python tools/patterns.py --show \"{p.name}\"\n")


def cmd_show(rows, name):
    matches = [(p, f) for p, f in rows if p.name.lower() == name.lower()]
    if not matches:
        matches = [(p, f) for p, f in rows if name.lower() in p.name.lower()]
    if not matches:
        print(f"No pattern named '{name}'. Run `python tools/patterns.py` for the index.")
        return
    if len(matches) > 1:
        print(f"{len(matches)} patterns match '{name}':")
        for p, f in matches:
            print(f"  {p.name}  ({len(p.inner)} blocks, {p.tier}, in {f[0]})")
        return

    p, files = matches[0]
    print(f"=== {p.name} ===   tier {p.tier}")
    print(f"source     {p.file}   (identical copy also in: "
          f"{', '.join(x for x in files if x != p.file) or 'nowhere else'})")
    print(f"size       {len(p.inner)} blocks, {len(K.descendant_edges(p.group))} edges")

    print(f"\nPorts ({len(p.ports)}) - the declared interface:")
    if not p.ports:
        print("  (none - this Group talks to the rest of the algo entirely by Jump)")
    for port in p.ports:
        print(f"  {'IN ' if port['input'] else 'OUT'}  {str(port['name'])[:28]:<30}"
              f"{port['type']}")

    print(f"\nContents:")
    for dn, n in p.census.most_common():
        print(f"  {n:>4}x {dn}")

    labels = [K.block_name(b) for b in p.inner
              if K.block_name(b) != b.get("defName")
              and not K.block_name(b)[:-1].rstrip("0123456789") == b.get("defName")]
    if labels:
        print(f"\nTT's own labels inside (design intent):")
        for lab in sorted(set(labels))[:18]:
            print(f"  {lab}")

    print(f"\nWhat adopting it costs you:")
    if p.tier == "GREEN":
        print("  Nothing beyond wiring the ports above. Self-contained.")
    for j in sorted(p.jumps_in):
        print(f"  REQUIRED  inbound Jump named '{j}' - you must feed this")
    for j in sorted(p.jumps_out):
        print(f"  optional  outbound Jump '{j}' - add landings if you want its output")
    for bname, guid in p.formula_leaks[:10]:
        print(f"  BLOCKER   formula in '{bname}' references outside block {guid[:8]}")
    if p.edge_leaks:
        print(f"  BLOCKER   {p.edge_leaks} edges cross the group boundary")
    if p.tier == "RED":
        print("\n  RED means the formula references above will DANGLE after extraction.")
        print("  Fixing them requires editing a formula string whose formulaNodes AST")
        print("  must agree - the one edit OPEN-QUESTIONS.md Q2 says not to make blind.")

    print(f"\n  python tools/patterns.py --extract \"{p.name}\" "
          f"--from \"{p.file.replace('.adl.json', '')}\" -o {_slug(p.name)}.json")


def _slug(s):
    return "".join(c if c.isalnum() else "-" for c in s).strip("-").lower() or "pattern"


# ---------------------------------------------------------------------------
# Extraction - the actual transplant
# ---------------------------------------------------------------------------

def remint(group_block):
    """Deep-copy a Group with every INSTANCE guid replaced by a fresh one.

    Returns (new_group, mapping). Connector GUIDs that are global per block type are
    deliberately NOT reminted - they are part of the block's identity, not the
    instance's (see ADL-JSON-Format-Spec.md section 3).

    The remap is done on the serialised JSON text rather than by walking fields,
    because instance GUIDs also appear inside formula strings ("[guid.conn]"),
    inside formulaNodes ASTs, and inside Jump sourceBlock/targetBlock properties.
    A field walk would miss at least one of those; a text substitution cannot,
    since a GUID is a 36-character token that never occurs as a substring of
    anything else.
    """
    subject = copy.deepcopy(group_block)
    olds = {group_block.get("guid")}
    olds |= {b.get("guid") for b in K.descendants(group_block)}
    olds.discard(None)

    mapping = {o: str(uuid.uuid4()) for o in olds}
    text = json.dumps(subject)
    for old, new in mapping.items():
        text = text.replace(old, new)
    return json.loads(text), mapping


def cmd_extract(rows, name, out_path):
    matches = [p for p, _ in rows if p.name.lower() == name.lower()]
    if not matches:
        matches = [p for p, _ in rows if name.lower() in p.name.lower()]
    if len(matches) != 1:
        print(f"{'No' if not matches else len(matches)} patterns match '{name}' - "
              f"need exactly one.")
        for p in matches:
            print(f"  {p.name}")
        return 1

    p = matches[0]
    new_group, mapping = remint(p.group)

    # Re-analyse the reminted copy so the manifest describes what you actually got.
    after = Pattern(new_group, "<extracted>")

    manifest = {
        "_readme": [
            "A Group block lifted from a TT algo with every instance GUID reminted.",
            "Splice `group` into the target algo's top-level `content` array, then",
            "wire its ports and satisfy `requires` below. Run validate.py afterwards.",
            "Connector GUIDs are NOT reminted - they are global per block type.",
        ],
        "pattern": p.name,
        "tier": p.tier,
        "source": {"file": p.file, "originalGuid": p.guid},
        "blocks": len(after.inner),
        "ports": after.ports,
        "requires": {
            "inboundJumps": sorted(after.jumps_in),
            "outboundJumps": sorted(after.jumps_out),
            "danglingFormulaRefs": [
                {"block": b, "referencesGuid": g} for b, g in after.formula_leaks
            ],
        },
        "guidMap": mapping,
        "group": new_group,
    }

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1)

    print(f"Extracted '{p.name}' [{p.tier}] -> {out_path}")
    print(f"  {len(after.inner)} blocks, {len(mapping)} GUIDs reminted, "
          f"{len(after.ports)} ports")
    if after.jumps_in:
        print(f"  You must supply {len(after.jumps_in)} inbound Jump(s): "
              f"{', '.join(sorted(after.jumps_in))}")
    if after.formula_leaks:
        print(f"  {len(after.formula_leaks)} formula reference(s) now DANGLE and must "
              f"be repointed by hand:")
        for b, g in after.formula_leaks[:6]:
            print(f"      {b} -> {g[:8]}")
    print("\n  Splice manifest['group'] into your algo's `content`, wire the ports,")
    print("  then: python tools/validate.py <your-algo>.adl.json")
    return 0


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Find and transplant reusable Groups from the TT algo corpus.")
    ap.add_argument("--search", metavar="TERM", help="find patterns matching TERM")
    ap.add_argument("--show", metavar="NAME", help="full detail + adoption cost")
    ap.add_argument("--extract", metavar="NAME", help="emit a GUID-reminted copy")
    ap.add_argument("-o", "--out", metavar="FILE", help="output file for --extract")
    ap.add_argument("--all", action="store_true",
                    help="include auto-named 'GroupN' patterns in the index")
    ap.add_argument("--from", dest="from_file", metavar="FILE",
                    help="only patterns from this corpus file (substring). TT reused the "
                         "name 'Group0' 12 times, so --show/--extract need this to "
                         "disambiguate")
    ap.add_argument("--guid", metavar="PREFIX",
                    help="only the Group whose guid starts with PREFIX - the last resort "
                         "when one file has several identically named Groups")
    args = ap.parse_args()

    if not K.corpus_files():
        print("No *.adl.json files in ADL-jsons/corpus/.")
        return 1
    rows = dedupe(collect())

    if args.from_file:
        rows = [(p, f) for p, f in rows if args.from_file.lower() in p.file.lower()]
        if not rows:
            print(f"No patterns from a corpus file matching '{args.from_file}'.")
            return 1
    if args.guid:
        rows = [(p, f) for p, f in rows if p.guid.lower().startswith(args.guid.lower())]
        if not rows:
            print(f"No Group whose guid starts with '{args.guid}'.")
            return 1

    if args.search:
        cmd_search(rows, args.search)
    elif args.show:
        cmd_show(rows, args.show)
    elif args.extract:
        out = args.out or f"{_slug(args.extract)}.pattern.json"
        return cmd_extract(rows, args.extract, out)
    else:
        cmd_index(rows, show_all=args.all)
    return 0


if __name__ == "__main__":
    sys.exit(main())
