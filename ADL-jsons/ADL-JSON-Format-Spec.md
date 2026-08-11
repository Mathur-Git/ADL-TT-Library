# The `.adl.json` Format — Reverse-Engineered Spec

What an exported TT ADL algo actually looks like on disk, derived from **13 TT-published
production algos** (4,740 blocks, 51 block types) sitting in [`corpus/`](corpus/).

**Read this instead of re-reading the JSONs.** Machine-readable companion:
[`block-catalog.json`](block-catalog.json) — every block type with its `defId`, connector
GUIDs, and observed property values. Regenerate with `python tools/extract_schema.py`.

**Query it with the tools, don't grep the corpus** — it's 8 MB, and the catalog alone is 375 KB:

| Script | Use |
|---|---|
| `lookup.py` | block `defId`s, connector GUIDs, properties, TT's own block labels, what's missing |
| `patterns.py` | find and transplant reusable `Group` subgraphs from TT's algos (§10) |
| `validate.py` | check a file against 14 structural invariants before you trust it (§9) |
| `profile_algo.py` | everything inside ONE algo — operator surface, resolved wiring and jumps, safety layer, per-Group reuse verdict. Behind [`corpus-analysis/`](corpus-analysis/how-these-were-derived.md) |
| `extract_schema.py` | rebuild the catalog after adding a new export |
| `test_validate.py` | fault injection — proves the validator actually catches breakage |
| `adlkit.py` | shared parsing primitives; every script imports it so the format quirks live in one place |

Sibling docs: [`adl-kb/`](../adl-kb/ADL-KB-Home.md) documents ADL *semantics* from TT's official
help library. This documents the *file format* and the *idioms TT's own algos actually use*.
Different sources — when they disagree, adl-kb wins on behaviour, this wins on encoding.

---

## Confidence labels

Everything below is tagged. Respect the tags.

| Tag | Meaning |
|---|---|
| **[V]** | **Verified** — directly observed across the corpus, counted |
| **[I]** | **Inferred** — consistent with all evidence, not provable from files alone |
| **[U]** | **Unknown** — flagged so it doesn't get assumed away |

> **[U] Nothing here has been round-tripped through ADL.** There is no ADL runtime on this
> machine. Whether a synthesized file *imports* is untested — and it gates everything else.
> **Before trusting any generated algo, run the ten-minute test in
> [OPEN-QUESTIONS.md Q1](../OPEN-QUESTIONS.md).**

---

## 1. Top-level shape **[V]**

```jsonc
{
  "id": "4a162ddd-…",          // algo GUID
  "name": "Conditional",
  "description": "",
  "orderSide": true,
  "variables": [ "<blockGuid>", … ],          // user-editable inputs — see §5
  "exports":   [ "<blockGuid>.<connGuid>", … ],// dashboard columns — see §5
  "bookmarks": [],
  "content":   [ …blocks and edges, interleaved… ],  // see §2
  "lastModifiedTime": 1554328212284,           // epoch ms
  "ignoreMarketState": false,
  "graphIdToViewport": { "<graphId>": {"x":…,"y":…,"scale":…} },  // canvas pan/zoom only
  "showInMDT": 0,
  "isSOA": false,
  "isOmaOta": true
}
```

`isSOA` / `isOmaOta` / `ignoreMarketState` are absent in some files **[V]** — treat missing as
false **[I]**. `graphIdToViewport` is pure cosmetics; it can be stale or partial without harm **[I]**.

---

## 2. `content` is a heterogeneous array **[V]**

Two record shapes share one array, distinguished by their keys:

**Block** — has `defName`:
```jsonc
{
  "defName": "ExistingOrder",              // block type
  "defId":   "C162872E-FED2-4125-B32C-E80057AF6CCC",  // stable per type — see §3
  "guid":    "e1a903e4-…",                 // unique per instance; edges reference this
  "x": 39, "y": 18,                        // canvas position
  "properties": [ {"name":"…","value":…,"hasCustomName":true}, … ],
  "exportValues": []
}
```

**Edge** — has `className: "Edge"`:
```jsonc
{
  "sourceBlock": "<block guid>", "sourceConnector": "<connector guid>",
  "targetBlock": "<block guid>", "targetConnector": "<connector guid>",
  "className": "Edge"
}
```

Edges carry no type information. Port-type compatibility (numeric / bool / instrument /
variable / message — see [block-catalog](../adl-kb/guides/block-catalog.md#port-type-legend))
is enforced by the editor, not recorded in the file **[V]**. **A hand-written file can encode an
illegal connection that the format itself won't catch** **[I]** — the importer may reject it, or
worse, may not.

**Edges never cross a graph boundary [V].** Both endpoints of an edge always live in the same
`content` array as the edge itself — **0 exceptions in 4,364 edges**. Data crosses a boundary
only via a `Connector` (through a Group port) or a `Jump` (§3a). An edge naming a block in
another graph is unrepresentable in ADL whatever the JSON says; `validate.py` treats it as an
error (C3).

### The nesting trap **[V]**

`content` is **recursive**. A `Group` block hides an entire subgraph under
`block.internalAlgo.content`, same shape, up to **3 levels deep** in this corpus.

A flat scan of top-level `content` sees roughly **⅓** of a real algo. Measured:

| Algo | flat blocks | true blocks | subgraphs |
|---|---:|---:|---:|
| `TT Multi-Level Bracket` | 57 | **682** | 3 |
| `Reference Market` | 125 | **669** | 22 |
| `Bid_Ask Theo` | 115 | **659** | 22 |
| `Market Base` | 550 | **622** | 3 |
| `Conditional` | 43 | **43** | 1 |

Always recurse. `extract_schema.py:walk_graphs()` is the reference implementation.

---

## 3. Block identity and connector GUIDs — the key finding **[V]**

Two GUID classes behave very differently:

**`defId` is globally stable per block type.** All 51 types show exactly one `defId` across all
13 files. `Number` is always `defId` X, everywhere.

**Connector GUIDs are also globally stable per block type.** `Number`'s output connector is
`1d65ec2f-0fdd-4d88-b01d-5393a4e6890e` in every file. `Branch` has 1 in / 2 out, same GUIDs
throughout. This holds for every fixed-arity block in the corpus.

**Why it matters:** connector GUIDs appear *only* inside edges — blocks don't declare their own
ports. So wiring a new block requires knowing its connector GUIDs in advance. Because they're
global constants, [`block-catalog.json`](block-catalog.json) **is** that lookup table, which is
what makes programmatic generation feasible at all **[I]**.

### The exceptions **[V]**

- **`Group`** — connectors are *per-instance*, declared inline in its `connectors` property:
  ```jsonc
  "connectors": { "<guid>": {"guid":"…","name":"Fill Msg","type":"message","input":true}, … }
  ```
  Observed `type` values: **`message` (108), `real` (55), `generic` (40), `bool` (33),
  `string` (8)**. You **mint fresh GUIDs** for these. The catalog's aggregate in/out figures for
  Group are a union across instances, not a schema — ignore them.
- **`Connector`** (244 instances) — the boundary-port block *inside* a subgraph.

### The Group ↔ Connector binding rule **[V]**

One GUID must appear in **three** places, all agreeing. For each port on a Group:

```jsonc
// 1. parent Group's `connectors` property, keyed by the GUID:
"connectors": { "70535e67-…": {"guid":"70535e67-…","name":"Fill Msg","type":"message","input":true} }

// 2. inside internalAlgo.content — a Connector block whose OWN guid IS that GUID:
{ "defName":"Connector", "guid":"70535e67-…",
  "properties":[ {"name":"name","value":"Fill Msg"},
                 // 3. …and a `definition` property mirroring the declaration:
                 {"name":"definition","value":{"guid":"70535e67-…","name":"Fill Msg",
                                               "type":"message","input":true}} ] }
```

Verified on a 3-port Group: all three inner `Connector` block GUIDs matched the parent's declared
keys exactly, and `name` / `type` / `input` were duplicated consistently. **[I]** Any mismatch
across the three almost certainly breaks the group boundary — this is the specific thing that makes
Group emission "risky" in §8, and it's mechanical enough to get right if you build all three together.

Edges *outside* the Group target the Group block's `guid` with the connector GUID; edges *inside*
target the `Connector` block's `guid`. Same GUID, two roles.

### 3a. Jump / JumpLanding — the property-linked wormhole **[V]**

41% of all blocks. **The link is carried in properties, not edges** — there is no `Edge` record
anywhere for a jump, so a tool that only reads edges sees a disconnected graph.

```jsonc
// Jump — one per source
{"defName":"Jump", "properties":[
  {"name":"name",            "value":"ConditionalOrder"},          // label, shared with its landings
  {"name":"sourceBlock",     "value":"3165fcca-…"},                // the REAL upstream block
  {"name":"sourceConnector", "value":"5b321cf2-…"},                // …and its output connector
  {"name":"targetBlock",     "value":["c2159f92-…","2862efd3-…"]}, // LIST of JumpLanding guids
  {"name":"generic",         "value":{"dfbb1c77-…":"message"}}     // {ownConnectorGuid: portType}
]}

// JumpLanding — N per Jump, each back-pointing at it
{"defName":"JumpLanding", "properties":[
  {"name":"name",            "value":"ConditionalOrder"},
  {"name":"sourceBlock",     "value":"259a11a0-…"},   // the JUMP's guid, not the original source
  {"name":"sourceConnector", "value":null},
  {"name":"generic",         "value":{"3b30f4bb-…":"message"}}
]}
```

Note `sourceBlock` means **different things on the two blocks**: on `Jump` it is the real
upstream data source; on `JumpLanding` it is the `Jump` itself. The pair is bidirectional.

Verified corpus-wide: **1,199 landings, every one claimed by exactly one Jump, 0 orphans,
0 dangling references, 0 landings failing to point back.** Six `Jump`s have no `targetBlock` at
all (a jump wired to nothing — legal, just useless). `validate.py` check C8 enforces all of this.

**Jumps cross Group boundaries freely**, which is why a Group commonly expects inbound data by
*jump name* rather than through a declared port — see the AMBER tier in `patterns.py`.

### Arity ceiling **[V] / [U]**

The catalog lists connectors **observed wired**, which is a floor, not the block's full port count.

| Block | max wired inputs seen |
|---|---|
| `And`, `Or`, `Add`, `Multiply`, `Subtract` | exactly 2 (every instance) |
| `Funnel` | 3 (44 instances used 2, 9 used 3) |
| `IfThen` | 3 |
| `SingleOrderContainer` | 4 |
| `Order` | 5 |

**[U] Beyond these, GUIDs are unknown.** ADL lets you add Funnel inputs in the UI; a 4th input's
GUID does not exist in this corpus and cannot be guessed. Blocks with configurable ports whose
port set changes with a property (`Order`'s type, `Field`'s lookup type) will expose connectors
not catalogued here.

`block-catalog.json` records `maxWiredArity` per block type — the most ports any **single
instance** ever had connected at once. The flat `connectors` lists are a union across all
instances and overstate what one block can take, so use `maxWiredArity` when the question is
"how many inputs can this block actually have".

### Two more traps worth knowing **[V]**

- **Block GUIDs are unique within a file but NOT across files.** 571 of 3,011 distinct GUIDs
  appear in more than one TT algo — they were derived from each other. **Always remint GUIDs when
  copying anything between files**; `patterns.py --extract` does it for you.
- **A property entry may have no `value` key at all** — 1,104 occurrences. Always `.get("value")`,
  never `p["value"]`. `adlkit.props()` absorbs this.

---

## 4. Formulas — two representations that must agree **[V]**

547 formula strings across the corpus. **The on-disk syntax is not the UI syntax.**

| Reference | On disk **[V]** | In the ADL Formula Editor |
|---|---|---|
| Another block's output | `[<blockGuid>.<connectorGuid>]` | `@BlockName` |
| Discrete message field | `{fillQuantity}` | `#FillQuantity` |

So [`adl-kb/guides/formula-reference.md`](../adl-kb/guides/formula-reference.md) documents `@`/`#`
correctly for the editor — the file stores resolved GUID references instead. Both are right about
their own layer. Real examples, verbatim:

```
{workingQuantity} == 0 AND ![33715390-….43d2cafc-…]
IF([87da1ba2-….1d65ec2f-…] > 25, [87da1ba2-….1d65ec2f-…], 25)
{isExternalEvent} OR [33715390-….43d2cafc-…] AND [6a6fa1fc-…]
```

Operators seen: `AND`, `OR`, `!`, `==`, `>`, `IF(cond, then, else)`. Message fields seen include
`fillQuantity`, `orderQuantity`, `workingQuantity`, `isExternalEvent`, `userField1`.

### `formulaNodes` — the parallel AST **[V]**

Blocks with formulas (`ValueAccumulator`, `Stopwatch`, `Branch`, `DiscreteOrder`, `ValueExtractor`)
carry **both**:
- `formula` — the source string
- `formulaNodes` — a parsed AST (`{type:"if"|"bool"|"connector", condition, then, else, loc:{…}}`)
- `formulaGraphId` — GUID tying them together

> ⚠️ **[I] Editing `formula` without regenerating `formulaNodes` is the single most likely way to
> corrupt a hand-edited file.** Which one the runtime actually evaluates is **[U]**. Until the
> round-trip test settles it, **do not hand-edit formulas** — prefer changing a wired `Number`
> block's value, which has no AST. Tracked as [Q2](../OPEN-QUESTIONS.md).

**The two do not reliably come as a pair [V].** TT ships blocks carrying a string with no AST
(several `Alert` blocks) and an AST with no string (`ValueInjector`, `DiscreteOrder`). So their
co-presence proves nothing, and neither can be used to infer the other's validity.

**Formulas routinely reference blocks in another graph [V].** Unlike edges (§2), formula
references are *not* graph-local: 20 of the 98 Groups in the corpus contain a formula pointing at
a block outside themselves. This is normal ADL, not corruption — but it is exactly what makes a
subgraph non-transplantable, because those references dangle once the subgraph is lifted out.
`patterns.py` calls it the RED tier.

---

## 5. User-facing surfaces **[V]**

- **`variables`** — a flat array of *block GUIDs*, typically `Number` / `Boolean` / `Instrument`
  blocks. Listing a block here promotes it to a launch-time editable parameter. That's the whole
  mechanism — no separate declaration block, no type annotation. Corpus range: 0–19 per algo.
- **`exports`** — array of `"<blockGuid>.<connectorGuid>"` strings; each becomes a live column on
  the Algo Dashboard. 0–1 per algo here, so multi-export layout is **[U]**.

### Bounds live on the block, and are used sparingly **[V]**

`Number` blocks carry `minValue` / `maxValue` properties. Of **68** Number blocks registered as
user variables, only **19 (28%)** set either bound — the rest are `null`, i.e. unbounded.

Where TT does use them, it's pointed:

| Variable | value | min | max |
|---|---:|---:|---:|
| `Quote Throttle` | 100 | **100** | 99999999 |
| `Loss Trigger Increments` | 10 | **1** | 10000 |
| `Max Pos`, `Bid Qty`, `Fill Throttle`, `TIF` … | 0 | — | — |

`Quote Throttle` with `minValue: 100` is a **throttle floor enforced at the parameter** — an
operator cannot type a value that would hammer the exchange. Compare the separate `Min 25ms`
Stopwatch in §7: the same concern defended twice, once at input and once in the graph.

**Consequence for design [I]:** bounds are available and cheap — use them on every safety-relevant
parameter. But they're not sufficient (they can't express cross-parameter rules), which is why TT
*also* validates in-graph — see `Incorrect Input values - Algo Stopped` in §7. Belt and braces.

---

## 6. Block inventory **[V]**

51 types, 4,740 instances. Full detail in [`block-catalog.json`](block-catalog.json).

**The headline: 41% of all blocks are routing, not logic.** `JumpLanding` (1,199) and `Jump` (748)
together are 1,947 blocks. Jump/JumpLanding is a named wormhole — one `Jump` in, N `JumpLanding`
out, no drawn edge, linked by properties (§3a). TT uses it as the default long-distance
connection; canvases would be unreadable otherwise. **Expect to emit far more Jump pairs than
you'd naively plan** **[I]**.

Next tier: `Connector` 244 (group boundaries), `And` 220, `Number` 202, `Funnel` 197,
`ValueExtractor` 173, `Branch` 153, `ValueAccumulator` 129, `Group` 98, `Generator` 97, `IfThen` 96.

Notably rare — these are specialist tools, not everyday building blocks: `TimeAndSales` (1),
`ValueBucket` (2), `Loop` (2), `DiscreteMax` (2), `MarketState` (3), `Formula` (4), `Round` (4),
`IsNumber` (7), `Exit` (7).

> `IsNumber` appearing only 7 times across 2 files is worth pausing on. adl-kb rule #7 says
> *"NaN deletes working orders — guard every division and depth lookup with IsNumber."* TT's own
> algos guard sparingly, because they mostly avoid division and deep-book lookups. **If your algo
> divides or reads depth, you need IsNumber more than this corpus suggests** **[I]**.

---

## 7. Risk, safety and redundancy idioms **[V]**

Custom block names (`hasCustomName: true`) are where TT's design intent is legible. These are
lifted verbatim from the corpus.

### Kill switches — `Terminal`
```
Net Pos Exceeds Max Pos  ·  Max Pos = 0  ·  Self Trade Prevention
Cover order setting violation  ·  Incorrect Input values - Algo Stopped  ·  Algo Paused
```

### Alert + Terminal fire together **[V]**
The same names appear on both `Alert` and `Terminal` blocks — `Net Pos Exceeds Max Pos`,
`Max Pos = 0`, `Cover order setting violation`. **The idiom is one condition driving two blocks:
`Alert` tells the human, `Terminal` stops the algo.** Neither alone. Alert-only names show the
softer tier — a warning that does *not* kill:
```
Cross Attmepted  ·  Unable to requote Buy / Sell  ·  Order Prices Crossed
Entry Deleted  ·  Allocation Failure  ·  No Cover Selected
```

### Throttling — `Stopwatch` (41 instances, 12 files)
```
Min 25ms  ·  QuoteDelay  ·  Quote Throttle (Bid) / (Ask)
Delete Throttle (Bid) / (Ask)  ·  Cancel Replace requote throttle (BID) / (ASK)
```
A block literally named **`Min 25ms`** — the adl-kb 25 ms Stopwatch floor, enforced in TT's own
production code. Throttles are consistently **split per side** (Bid/Ask separately) and **per
action** (quote / delete / cancel-replace separately), not one global governor **[V]**.

### Position and fill accounting — `ValueAccumulator`
```
BuyPos · SellPos            (tracked separately, netted downstream — not one signed counter)
Buy ext deletes · Sell ext deletes    (EXTERNAL interference, counted per side)
CumFills · CumFillCount · TotalFills · MyTotalFills · recent fills · Temporary fills
NumOpen · NumClosed · OrdersPlaced · DeletedOrderCount
Covers Submitted · Cover Fills · fill throttled · OrderPlacedTimerSet
Initial start tracker · ExternalEvent · qty inc wait for requote
```
Two patterns stand out: **sides tracked separately then netted**, and **external actions counted
as first-class state** (`Buy ext deletes`). Paired with `onExtMod` (`Ignore` vs `StopManaging`,
on `Order` / `DiscreteOrder` / `SingleOrderContainer`), that's a deliberate stance on what happens
when a human touches the algo's orders **[I]**.

### Safety toggles — `Boolean` user variables
```
Dont Cross Market · Enforce Mkt State · Delete Orphan · Use Cancel/Replace
If Quote Outside, Join Mkt · If Quote Inside, Join Mkt · Enable Cover Order?
```
Every risky behaviour is a **named, operator-visible switch**, not a hardcoded branch **[I]**.

### Tuning parameters — `Number` user variables
```
Max Pos · Quote Throttle · Fill Throttle · Cover Order Offset
Bid Offset / Ask Offset · Bid Qty / Ask Qty · Profit Increments · TIF · Qty · Epsilon
```
**`Epsilon`** is the tell: floating-point comparisons get an explicit tolerance parameter rather
than `==` **[I]**. Worth copying.

---

## 8. Practical constraints on generating a file

**Feasible [I]:** emit blocks with `defId` + catalogued connector GUIDs; mint fresh instance
`guid`s; wire edges; set scalar properties; register `variables` / `exports`; lay out `x`/`y`.

**Risky [I]:** anything with a `formulaNodes` AST (§4); `Group` subgraphs (mint per-instance
connectors *and* matching inner `Connector` blocks); virtualization (`Group.virtual: true` — the
`Exit` block appears only 7 times, so the pattern is thinly evidenced here).

**Not possible from this corpus [U]:** ports beyond observed arity (§3); property enums never
exercised; and **8 blocks documented in adl-kb with no `defName` anywhere in the corpus** —
`Analytics`, `Pnl`, `PositionRisk`, `MovingAverage`, `Average`, `Mod`, `RandomNumber`,
`DiscreteMin`. Their `defId`s and connector GUIDs are unknown and cannot be guessed. Run
`python tools/lookup.py --missing` for the live list and the workarounds.

> **`Abs`, `Min`, `Max`, `Log`, `Pow`, `Sqrt`, `Floor`, `Ceiling`, `Sign` and the trig functions
> are NOT missing** — they are values of the `Math` block's `mathFunction` property, not blocks
> of their own **[V]**. `Math` exposes a different number of ports depending on which function is
> selected, so its port set is property-dependent (§3).

> ⚠️ **Judge absence by `defName`, never by the KB's page title.** They differ: adl-kb documents
> the *"Bool block"*, whose `defName` is **`Boolean`** **[V]**. A block you think is missing may
> just be named differently on disk. Check [`block-catalog.json`](block-catalog.json)'s key list
> before concluding anything is absent.

**Extension path:** if a design needs an uncatalogued block, **build a throwaway algo in ADL
containing it, export it into `corpus/`, and re-run `tools/extract_schema.py`.** One export closes the
gap permanently, and the catalog gets better for every future algo.

### Practical rule **[I]**
In strict order of preference:

1. **Transplant** an existing `Group` (§10). Every byte except the GUIDs was written by ADL,
   including the `formulaNodes` ASTs you must not hand-author.
2. **Modify an export.** Open the closest TT algo, change wired `Number` values, add plain blocks.
3. **Synthesize from scratch.** Most assumptions stacked, most risk.

The further you get from a file ADL itself wrote, the more unverified assumptions you're stacking.

---

## 9. Validating a file before you trust it

```bash
python tools/validate.py                # self-test against the 13 known-good algos
python tools/validate.py mine.adl.json  # check your file
python tools/validate.py --strict mine.adl.json
python tools/validate.py --explain C7   # what a check means and why it matters
```

14 structural checks (C1–C14) covering GUID uniqueness, edge resolution, connector direction,
the Group three-way binding, the Jump wormhole, `variables`/`exports`, and formula references.

**Two properties make a green result mean something:**

- It **self-tests clean on all 13 TT-authored algos.** Every invariant was derived from them, so
  if a check fires on TT's own file the *check* is wrong — loosen it rather than "fixing" a
  shipped algo. (This is not hypothetical: writing C7 caught a bug where the checker recursed
  into nested Groups and blamed the parent for their ports.)
- `test_validate.py` **injects 18 fault classes and confirms each is caught.** A validator that
  only ever prints `ok` proves nothing.

**What it cannot tell you:** structure only. A file can pass every check and still wire
incompatible port *types* (the format doesn't record them), deadlock, or compute nonsense. And
passing does **not** prove ADL will import it — see
[OPEN-QUESTIONS.md Q1](../OPEN-QUESTIONS.md), which has the ten-minute round-trip test that
settles the whole question. **Do that test before relying on anything in §8.**

---

## 10. Reusing parts of TT's algos

```bash
python tools/patterns.py                     # index every reusable Group, by adoption cost
python tools/patterns.py --search throttle
python tools/patterns.py --show "Mkt Price"  # ports, contents, and what it needs wired
python tools/patterns.py --extract "SynthStop" --from BrackeTT -o part.json
```

**The unit is the `Group` block** because it's ADL's own encapsulation: a subgraph with a
declared, typed interface. That interface is what makes an apples-to-apples comparison possible —
two Groups are interchangeable when their port signatures match, and the cost of adopting one is
exactly its list of external dependencies.

**`--from <file substring>` is usually required.** TT reused the auto-name `Group0` for **12**
different Groups across the corpus, and 16 of the 35 patterns are auto-named `GroupN`. `--show`
lists every match; `--extract` **refuses** an ambiguous name rather than guessing. `--guid
<prefix>` is the fallback when a single file contains several identically named Groups. **[V]**

**35 distinct reusable Groups** across the corpus (86 instances), classified by what adopting one
costs you:

| Tier | Count | Meaning |
|---|---:|---|
| **GREEN** | 11 | Self-contained. Wire its declared ports and it works. |
| **AMBER** | 14 | Also needs named inbound `Jump`s fed — jumps cross group boundaries (§3a). |
| **RED** | 10 | A formula inside references a block outside (§4). Those dangle after extraction and can only be fixed by formula surgery. |

`--extract` remints **every instance GUID** (never the per-type connector GUIDs) and emits a
manifest listing the ports, the required inbound jumps, and any dangling formula references.
The remint is done by substitution on the serialised JSON, because instance GUIDs also appear
inside formula strings, inside `formulaNodes` ASTs, and inside Jump properties — a field walk
would miss at least one.

Verified: 0 original GUIDs survive extraction, the Group binding and Jump wormholes stay intact,
the result passes `validate.py`, and two extractions never collide. Whether ADL *imports* a
spliced subgraph is a special case of [Q1](../OPEN-QUESTIONS.md).

> **TT does this themselves [V].** `Alerts`, `Mkt Price`, `CalculatedOrder`, `PriceOrQtyChanged`,
> `DESIRED_QTY` and `InsideMarket` each appear byte-identical across four different TT algos.
> Transplanting isn't a workaround — it's how these algos were built.

---

## Regenerating

```bash
cd ADL-jsons
python tools/extract_schema.py  # rewrites block-catalog.json
python tools/validate.py        # confirm the corpus still self-tests clean
python tools/test_validate.py   # confirm the checks still bite
```

Drop new `*.adl.json` exports in `corpus/` first — coverage grows with the corpus, and the
`[U]` gaps in §8 close the same way.

`extract_schema.py` re-checks seven structural invariants on every run and prints them under
`_invariants` in the catalog. **All must stay 0.** A non-zero value means a real ADL-authored
file has contradicted something `validate.py` enforces — believe the file and loosen the check.
(`jumpsWithNoTarget` is the one non-zero count: 6 Jumps in the corpus are wired to nothing,
which is legal and merely useless.)

## Provenance

13 TT-published algos, pre-made by Trading Technologies and available to all TT users:
`Bid_Ask Theo` · `BrackeTT` · `Conditional` · `Direct Entry` · `Market Base` · `MinVol` ·
`OCO` · `OCO 2` · `Reference Market` · `Single Theo` · `TT Multi-Level Bracket` · `TT Sniper` ·
`With A Tick`. Analyzed 2026-07-27. Not hand-authored — every count above is reproducible
via `extract_schema.py`.
