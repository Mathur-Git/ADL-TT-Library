# Open Questions

Everything this repo does **not** know, in one place, with the cheapest way to settle
each. Check this before promising that a generated algo will work.

These are ordered by how much they block. **Q1 gates everything else.**

| # | Question | Blocks | Status |
|---|---|---|---|
| Q1 | Will ADL import a file it didn't write? | all file generation | **untested** |
| Q2 | Is `formula` or `formulaNodes` authoritative? | any conditional logic | **unknown** |
| Q3 | What are the GUIDs for 8 uncatalogued blocks? | indicators, live risk | **unknown** |
| Q4 | What are a block's ports beyond observed arity? | high-fan-in designs | **partial** |
| Q5 | Does a transplanted Group survive a real import? | pattern reuse | **untested** |

---

## Q1 - Will ADL import a file it didn't write?

**Everything rests on this.** `validate.py` proves a file is *structurally* consistent
with 13 real algos. It cannot prove ADL's importer accepts it. If ADL validates
something absent from the file - a checksum, a version stamp, server-side IDs - then no
amount of schema fidelity helps and the fallback is driving the ADL UI by hand.

Two tests, in order. **Ten minutes settles the entire question.**

**Test A - does an edited file import at all?**
1. Copy `ADL-jsons/Conditional.adl.json` (43 blocks, single graph, smallest algo).
2. Change exactly **one** `Number`-like wired value to something unmistakable - `7777`.
   Nothing else.
3. Import into ADL, **open the block in the editor, and read the value back.**

> Step 3 is the part people skip, and it is the part that matters. `Number` also carries
> a `currValue` property, so `value` may be a cached display field rather than the
> authoritative one. **A file that imports without showing 7777 is a failure, not a
> pass** - it means the edit was silently discarded, which is worse than rejection
> because it looks like success.

| Outcome | Meaning |
|---|---|
| Imports, shows 7777 | The writer path is real. Generation is live. |
| Imports, shows the old value | `value` is not authoritative. Find the field that is before editing anything else. |
| Rejected | ADL validates something not in the file. Fall back to driving the UI. |

**Test B - are minted GUIDs accepted?** Only if A passes. Add one new `Number` block
(fresh `guid`, `defId` from `lookup.py`) plus one edge wiring it somewhere harmless.
A proves ADL tolerates *edits*; **B proves it tolerates *additions***, which is the
actual load-bearing assumption.

**Report the result - it determines how every algo after this gets built.**

---

## Q2 - Which of `formula` / `formulaNodes` does the runtime evaluate?

Blocks with formulas (`ValueAccumulator`, `Stopwatch`, `Branch`, `DiscreteOrder`,
`ValueExtractor`) carry **both** a `formula` source string and a `formulaNodes` parsed
AST, tied by `formulaGraphId`. Which one executes is unknown.

**Why it blocks:** editing the string without regenerating the AST leaves two
disagreeing representations, and you cannot predict which wins. This is the single most
likely way to corrupt a hand-edited file.

Complicating it: the two do **not** reliably come as a pair. TT ships blocks with a
string and no AST (several `Alert` blocks) and with an AST and no string
(`ValueInjector`, `DiscreteOrder`). So their co-presence proves nothing.

**Current rule: do not hand-edit formulas.** Prefer changing a wired `Number` block's
value, which has no AST. `validate.py` reports how many AST-carrying blocks a file has.

**How to settle it:** after Q1 passes, take a file with a formula block, change the
`formula` string *only* (leave the AST stale), import, and see which behaviour appears.

---

## Q3 - The 8 blocks the corpus cannot give you

`python ADL-jsons/lookup.py --missing`

`Analytics`, `Pnl`, `PositionRisk`, `MovingAverage`, `Average`, `Mod`, `RandomNumber`,
`DiscreteMin`. Documented by TT, but with **no `defName` anywhere in the corpus**, so
their `defId` and connector GUIDs are unknown and cannot be guessed.

`Analytics`, `Pnl` and `PositionRisk` are the expensive ones - indicators and live risk
are hard to substitute. The rest have workarounds (`lookup.py --missing` lists them).

**Not missing, despite having no block of their own:** `Abs`, `Min`, `Max`, `Log`,
`Pow`, `Sqrt`, `Floor`, `Ceiling`, `Sign` and the trig functions. All are values of the
`Math` block's `mathFunction` property.

**How to close it permanently:** build a throwaway algo in ADL containing the block, put
one of everything on a blank canvas, export it into `ADL-jsons/`, and run
`python extract_schema.py`. **One export closes the gap for good and improves every
future algo.** This is the single highest-leverage thing available besides Q1.

---

## Q4 - Ports beyond observed arity

The catalog lists connector GUIDs **observed wired** in the corpus - a floor, not a
block's full port count. `block-catalog.json` now also records `maxWiredArity`: the most
ports any single instance ever had connected at once.

ADL lets you add inputs to a `Funnel` in the UI; a 4th input's GUID does not exist in
this corpus and **cannot be guessed**. Blocks whose port set changes with a property
(`Order`'s type, `Field`'s `lookupType`) will expose connectors not catalogued here.

`validate.py` reports an unknown connector as a **warning, not an error**, precisely
because it may be a legitimate port TT never happened to use.

**How to close it:** same as Q3 - export an algo that wires the block more widely.

---

## Q5 - Does a transplanted Group survive a real import?

`patterns.py --extract` produces a Group with every instance GUID reminted. This is
verified to be internally sound: zero original GUIDs leak, the three-way Group binding
and the Jump wormholes survive, `validate.py` passes on the result, and two extractions
never collide.

**All of that is local reasoning.** Whether ADL accepts a spliced subgraph is a special
case of Q1 and inherits its answer. Test it with the smallest GREEN pattern
(`MinAggressiveValueCheck`, 5 blocks) before relying on a large one.

---

## Settled - kept so they don't get re-litigated

- **`defId` and connector GUIDs are globally stable per block type.** All 51 types show
  exactly one `defId` across all 13 files. This is what makes generation feasible.
- **Block GUIDs are NOT unique across files** - 571 of 3,011 are shared. Always remint.
- **Edges never cross a graph boundary** - 0 of 4,364.
- **`Jump.targetBlock` is a list**, landings back-point via `sourceBlock`, and `generic`
  carries the port type. 1,199 landings, 0 orphans, 0 dangling.
- **Group port types** are `message`, `real`, `bool`, `string`, `generic` - not just
  `message`/`string` as an earlier draft of the spec claimed.
- **Formulas routinely reference other graphs.** Normal, not corruption - but it is what
  makes a subgraph non-transplantable (`patterns.py` RED tier).
- **ADL has no backtester.** Signal validation happens elsewhere, on tick data. Not a
  gap to close - a constraint to design around.
