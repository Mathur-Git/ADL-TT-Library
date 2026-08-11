# ADL-TT-Library

A workbench for designing **Trading Technologies ADL** (Algo Design Lab) algos and
turning them into importable `.adl.json` files.

ADL is a block-and-wire visual language: you place blocks on a canvas, connect ports,
and deploy to TT's Algo Server. This repo holds everything needed to design one
accurately offline - the documentation, a corpus of real algo files, tools that
reverse-engineer their format, and a per-project workspace.

Working with Claude Code here? Start with [`CLAUDE.md`](CLAUDE.md).

---

## What's in it

| Folder | Contents |
|---|---|
| [`adl-kb/`](adl-kb/ADL-KB-Home.md) | ADL documentation - 128 pages mirrored from TT's help library, plus 6 authored guides. Start at [`guides/core-semantics.md`](adl-kb/guides/core-semantics.md). |
| [`trade-kb/`](trade-kb/Trade-KB-Home.md) | TT platform documentation - 594 pages: spread trading and Autospreader, order types, market data and depth, algo operations, risk. |
| [`ADL-jsons/`](ADL-jsons/ADL-JSON-Format-Spec.md) | 13 TT-published algo exports (4,740 blocks, 51 block types), the [reverse-engineered format spec](ADL-jsons/ADL-JSON-Format-Spec.md), and the toolchain. |
| [`projects/`](projects/INDEX.md) | One folder per algo being built. Each `PROJECT.md` is the durable record of its thesis, design and blockers. |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | What is still unverified, and the cheapest way to settle each. **Read before trusting a generated file.** |

## The toolchain

Eight scripts in `ADL-jsons/tools/`, run from `ADL-jsons/`, all sharing `adlkit.py`.
Python 3, no third-party dependencies. The 13 exports they read live in
`ADL-jsons/corpus/`.

```bash
cd ADL-jsons

python tools/brief.py                    # START HERE: repo shape, projects, routing table

python tools/q.py props MinVol Number    # block properties in one algo, cosmetics stripped
python tools/q.py grep throttle          # regex over custom names, formulas and notes
python tools/q.py notes Conditional      # TT's verbatim Note-block commentary
python tools/q.py block MinVol "Min Qty" # one block plus its edges and jump links

python tools/profile_algo.py MinVol --brief   # what's in ONE algo and what can be lifted
python tools/profile_algo.py MinVol      # the same, in full (~15 KB)

python tools/lookup.py Stopwatch         # defId, connector GUIDs, observed properties
python tools/lookup.py --names Terminal  # TT's own labels on a block - i.e. design intent
python tools/lookup.py --missing         # documented blocks the corpus can't give you

python tools/patterns.py                 # reusable Groups from TT's algos, by adoption cost
python tools/patterns.py --search throttle
python tools/patterns.py --show "Mkt Price"
python tools/patterns.py --extract "SynthStop" -o part.json

python tools/validate.py                 # self-test against the 13 known-good algos
python tools/validate.py mine.adl.json   # check a file you built
python tools/validate.py --explain C7    # what a check means and why it matters

python tools/extract_schema.py           # rebuild the catalog after adding an export
python tools/test_validate.py            # fault injection - proves the validator bites
```

### Why these exist

Blocks don't declare their own ports. Connector GUIDs appear **only** inside edges, so
wiring a new block requires knowing its GUIDs in advance. They turn out to be globally
stable per block type, which makes [`block-catalog.json`](ADL-jsons/block-catalog.json)
a usable wiring table - and makes generating an algo file feasible at all.

`validate.py` is the safety net. It enforces 14 structural invariants, **self-tests
clean on all 13 TT-authored algos**, and is proven to catch 18 injected fault classes.
Both halves matter: the first shows it doesn't cry wolf, the second shows it actually
bites.

`patterns.py` exists because the corpus is full of solved problems. It indexes every
`Group` - ADL's own encapsulation unit, with a declared typed interface - and ranks them
by what adopting one costs you:

- **GREEN** - self-contained. Wire its ports and go.
- **AMBER** - also needs named `Jump` wormholes fed.
- **RED** - a formula reaches outside the group; adopting it means formula surgery.

Transplanting beats synthesizing, because every byte except the GUIDs was written by ADL
itself. TT does it too: `Alerts`, `Mkt Price` and `CalculatedOrder` appear byte-identical
across four different TT algos.

## The one thing that isn't verified

**No file produced here has been round-tripped through ADL.** The format was derived by
reading 13 real exports; whether ADL's importer *accepts* a file it didn't write is
untested, and it gates everything else. [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) has a
ten-minute test that settles it.

## Requirements

Python 3.8+ for the toolchain. A TT account with ADL access to actually build and deploy.

## Provenance

`adl-kb/` and `trade-kb/` are mirrored from
[TT's help library](https://library.tradingtechnologies.com/) with content preserved
verbatim; the `guides/` layers are authored from that material. The 13 algos in
`ADL-jsons/` are TT-published and available to all TT users - not hand-authored, so
every count in the format spec is reproducible via `extract_schema.py`.
