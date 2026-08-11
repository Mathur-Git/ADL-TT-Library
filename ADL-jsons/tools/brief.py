#!/usr/bin/env python3
"""
brief.py - the whole session-start orientation in one command.

Run this FIRST, before any ls / find / grep / cat of README, INDEX.md,
OPEN-QUESTIONS.md or PROJECT.md. It exists because re-deriving the repo's shape
from the filesystem every session is the single largest recurring token cost
here - measured at roughly a quarter of all shell output across 23 sessions,
spent rediscovering facts that had not changed.

    python tools/brief.py            # full briefing (~2 KB)
    python tools/brief.py --routing  # just the question -> artifact table
    python tools/brief.py --no-git   # skip the git section

Everything printed is read from disk at run time, so it cannot go stale the way
a checked-in summary would. Corpus and catalog numbers come from
block-catalog.json's precomputed `_meta`/`perFile`, never from the 8 MB corpus,
so this stays fast.

What it deliberately does NOT do: interpret. It tells you what exists and where
to look next. The looking is still your job, and the routing table says which
single file answers which kind of question - open that one, not five.
"""

import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adlkit as K

REPO = os.path.dirname(K.ROOT)                      # the workbench root
W = 76

# Question -> the ONE artifact that answers it. The point of this table is to
# stop a survey of five files when one would do. Ordered by how often the
# question actually comes up.
ROUTING = [
    ("how a block behaves at runtime",   "adl-kb/guides/block-catalog.md (then reference/)"),
    ("execution model, discrete/continuous",
                                         "adl-kb/guides/core-semantics.md"),
    ("a hard limit or a known trap",     "adl-kb/guides/gotchas-and-limits.md"),
    ("writing a formula",                "adl-kb/guides/formula-reference.md"),
    ("how to build a known shape",       "adl-kb/guides/design-patterns.md"),
    ("OTA / SOA / OMA, deployment",      "adl-kb/guides/algo-types.md"),
    ("a block's defId or connector GUIDs",
                                         "tools/lookup.py <Block>   [NOT the catalog JSON]"),
    ("what TT named its blocks (intent)","tools/lookup.py --names <Block>"),
    ("how one TT algo works, end to end","ADL-jsons/corpus-analysis/<algo>.md  [NOT profile_algo]"),
    ("a specific block's properties",    "tools/q.py props <algo> <Type>"),
    ("find a name/formula across corpus","tools/q.py grep <regex>"),
    ("a reusable Group to lift",         "tools/patterns.py --search <term>"),
    ("how .adl.json is encoded",         "ADL-jsons/ADL-JSON-Format-Spec.md"),
    ("TT platform, not ADL",             "trade-kb/guides/"),
    ("what is still unverified",         "OPEN-QUESTIONS.md"),
]


def rule(title):
    print(f"\n-- {title} " + "-" * max(0, W - len(title) - 4))


def count_md(folder):
    n = 0
    for _root, _dirs, files in os.walk(os.path.join(REPO, folder)):
        n += sum(1 for f in files if f.endswith(".md"))
    return n


def table_rows(path, first_cell_re):
    """Markdown table rows whose first cell matches. Returns list of cell-lists."""
    out = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells and first_cell_re.match(cells[0]):
                out.append(cells)
    return out


def clip(s, n):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 3] + "..."


def strip_md(s):
    """Markdown link/emphasis noise out of a table cell, so it fits on one line."""
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s or "")
    return s.replace("**", "").replace("`", "")


def section_repo():
    rule("REPO")
    cat = K.load_catalog()
    meta = (cat or {}).get("_meta", {})
    inv = (cat or {}).get("_invariants", {})
    print(f"  {REPO}")
    print(f"  adl-kb    {count_md('adl-kb'):>4} md   guides/ = the authored layer, "
          f"reference/ = TT mirror")
    print(f"  trade-kb  {count_md('trade-kb'):>4} md   platform docs (not ADL)")
    print(f"  corpus    {len(meta.get('corpusFiles', [])):>4} algos "
          f"{meta.get('totalBlocks', '?')} blocks, {meta.get('distinctBlockTypes', '?')} types, "
          f"max nesting {meta.get('maxGroupNestingDepth', '?')}")
    if inv:
        # jumpsWithNoTarget is a known non-zero in TT's own files; the rest must be 0.
        bad = {k: v for k, v in inv.items() if v and k != "jumpsWithNoTarget"}
        state = "clean" if not bad else "BROKEN: " + ", ".join(f"{k}={v}" for k, v in bad.items())
        print(f"  catalog   invariants {state}"
              + (f"  (jumpsWithNoTarget={inv['jumpsWithNoTarget']}, expected)"
                 if inv.get("jumpsWithNoTarget") else ""))


def section_projects():
    rule("ACTIVE PROJECTS")
    rows = table_rows(os.path.join(REPO, "projects", "INDEX.md"), re.compile(r"^\["))
    if not rows:
        print("  none listed in projects/INDEX.md")
        return
    for cells in rows:
        name = strip_md(cells[0])
        status = strip_md(cells[1]) if len(cells) > 1 else ""
        updated = strip_md(cells[3]) if len(cells) > 3 else ""
        print(f"  {name:<32} {clip(status, 30):<30} {updated}")
        if len(cells) > 2 and cells[2] and cells[2] != "-":
            print(f"      blocker: {clip(strip_md(cells[2]), W - 15)}")
    print("  full record: projects/<name>/PROJECT.md   (gitignored - no history to recover)")


def section_questions():
    rule("OPEN QUESTIONS")
    rows = table_rows(os.path.join(REPO, "OPEN-QUESTIONS.md"), re.compile(r"^Q\d+$"))
    if not rows:
        print("  OPEN-QUESTIONS.md has no summary table")
        return
    for cells in rows:
        q = strip_md(cells[1]) if len(cells) > 1 else ""
        state = strip_md(cells[3]) if len(cells) > 3 else ""
        print(f"  {cells[0]:<4} {clip(q, W - 22):<{W - 22}} {state}")
    print("  Check here before promising any behaviour is verified.")


def section_corpus():
    rule("CORPUS (blocks / edges / graphs / vars)")
    cat = K.load_catalog() or {}
    per = cat.get("perFile", {})
    if not per:
        print("  block-catalog.json missing - run: python tools/extract_schema.py")
        return
    for fname in sorted(per, key=lambda f: -per[f].get("blocks", 0)):
        d = per[fname]
        stem = fname.replace(".adl.json", "").strip()
        flags = []
        if d.get("isSOA"):
            flags.append("SOA")
        if d.get("isOmaOta"):
            flags.append("OMA/OTA")
        if d.get("ignoreMarketState"):
            flags.append("ignoreMktState")
        print(f"  {stem:<26} {d.get('blocks', 0):>4} {d.get('edges', 0):>5} "
              f"{d.get('graphs', 0):>4} {d.get('variables', 0):>4}   "
              f"{' '.join(flags)}".rstrip())
    print("  prose for each: ADL-jsons/corpus-analysis/<algo>.md - read that before")
    print("  reaching for profile_algo.py, which prints ~15 KB for a single file.")


def section_routing():
    rule("ROUTING - one question, ONE artifact")
    for q, where in ROUTING:
        print(f"  {q:<36} {where}")
    print("  Never answer an ADL question from priors. Cite the file you used.")


def section_git():
    rule("GIT")
    try:
        branch = subprocess.run(["git", "-C", REPO, "rev-parse", "--abbrev-ref", "HEAD"],
                                capture_output=True, text=True, timeout=10).stdout.strip()
        st = subprocess.run(["git", "-C", REPO, "status", "--porcelain"],
                            capture_output=True, text=True, timeout=10).stdout
        last = subprocess.run(["git", "-C", REPO, "log", "-1", "--format=%h %s"],
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError) as e:
        print(f"  git unavailable ({e.__class__.__name__})")
        return
    dirty = [l for l in st.splitlines() if l.strip()]
    print(f"  branch {branch or '?'}   {len(dirty)} uncommitted path(s)")
    print(f"  last   {clip(last, W - 10)}")
    print("  Don't commit unless asked.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--routing", action="store_true", help="only the routing table")
    ap.add_argument("--no-git", action="store_true", help="skip the git section")
    a = ap.parse_args()

    if a.routing:
        section_routing()
        return 0

    print("=" * W)
    print("ADL WORKBENCH BRIEFING   (tools/brief.py - read this instead of surveying)")
    print("=" * W)
    section_repo()
    section_projects()
    section_questions()
    section_corpus()
    section_routing()
    if not a.no_git:
        section_git()
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
