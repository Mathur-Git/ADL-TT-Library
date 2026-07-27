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
| [`adl-kb/`](adl-kb/README.md) | ADL documentation - 132 pages mirrored from TT's help library, plus 6 authored guides. Start at [`guides/core-semantics.md`](adl-kb/guides/core-semantics.md). |
| [`trade-kb/`](trade-kb/README.md) | TT platform documentation - 638 pages: spread trading and Autospreader, order types, market data and depth, algo operations, risk. |
| [`ADL-jsons/`](ADL-jsons/README.md) | 13 TT-published algo exports (4,740 blocks, 51 block types), the [reverse-engineered format spec](ADL-jsons/README.md), and the toolchain. |
| [`projects/`](projects/INDEX.md) | One folder per algo being built. Each `PROJECT.md` is the durable record of its thesis, design and blockers. |
| [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md) | What is still unverified, and the cheapest way to settle each. **Read before trusting a generated file.** |

## The toolchain

Four scripts in `ADL-jsons/`. Python 3, no third-party dependencies.

```bash
cd ADL-jsons

python lookup.py Stopwatch            # defId, connector GUIDs, observed properties
python lookup.py --names Terminal     # TT's own labels on a block - i.e. design intent
python lookup.py --missing            # documented blocks the corpus can't give you

python patterns.py                    # reusable Groups from TT's algos, by adoption cost
python patterns.py --search throttle
python patterns.py --show "Mkt Price"
python patterns.py --extract "SynthStop" -o part.json

python validate.py                    # self-test against the 13 known-good algos
python validate.py mine.adl.json      # check a file you built
python validate.py --explain C7       # what a check means and why it matters

python extract_schema.py              # rebuild the catalog after adding an export
python test_validate.py               # fault injection - proves the validator bites
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
