# Reference Market

Quote a two-sided market on one instrument, priced off **another instrument's** market. 669
blocks — the largest algo in the theo family and the second largest in the corpus.

The shared quoting engine, its fourteen common Groups, its safety layer and the three
architectural ideas worth stealing are analysed once in
**[bid-ask-theo.md](bid-ask-theo.md)** and not repeated here. This doc covers the price source,
which is the only thing that differs — and which is the family member most likely to be the
starting point for a real spread or lead-lag design.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Reference Market.adl.json` |
| Algo id | `550f8ebb-7acd-4c49-a5ea-aea292fd49b0` |
| Last modified | 2025-10-10 21:30:38 UTC |
| Size | 1,186,881 bytes — the largest file in the corpus |
| Flat blocks / true blocks | **125** / **669** |
| Subgraphs / max depth | 21 / 3 |
| Edges | 593 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta` absent |

**[V]** 125 flat blocks against the family's 102–115: the extra ten are the reference-instrument
front end.

## The price source

**[V]** This is the **only corpus algo with two `Instrument` blocks**:

| Block | Type | Role |
|---|---|---|
| `Contract` | `orderInstrument` | the instrument being **quoted** |
| `Reference Instrument` | `userDefined` | the instrument being **watched** |

and the extra data path:

```
Reference Instrument --> Ref Bid (Field, bidPrice, "best")
                     --> Ref Ask (Field, askPrice, "best")
Ref Bid / Ref Ask  x  @Ref Prc Multiplier (Number, default 1)
                   ±  @Bid Offset / @Ask Offset
   --> Jump "Calculated Bid Prc" / "Calculated Ask Prc"   --> the shared engine
```

**[V]** Nine `Field` blocks against the family's seven — `Ref Bid` and `Ref Ask` are the two
extra. Six `Multiply` blocks against four, and 31 `Number` blocks against 30, the extra being
`Ref Prc Multiplier`.

**[V]** Eighteen variables. The three that are unique to this file: `Reference Instrument`,
`Contract`, `Ref Prc Multiplier` (default **1**, unbounded).

**[I] `Contract` being `orderInstrument` while `Reference Instrument` is `userDefined` is the
important detail.** The quoted instrument follows the ladder the algo was launched from
([algo-types](../../adl-kb/guides/algo-types.md)); the reference is chosen once at launch. So
the same deployed algo quotes whatever contract you launch it on, against a fixed reference.
**[V]** adl-kb also notes that a user-defined `Instrument` **cannot be changed while the algo is
running** — so the reference is fixed for the life of the run and the quoted contract is not.

## Why this one is the useful starting point

**[I]** Of the four family members, this is the only one whose price is derived from *market
data* rather than typed in by a human. That makes it the natural base for:

- **spread and lead-lag quoting** — quote the back month off the front, or the cash off the
  future
- **cross-venue or cross-product pricing** — one instrument's market, scaled
- **anything with a hedge ratio** — that is exactly what `Ref Prc Multiplier` is

**[I]** The multiplier is a single `Number` applied to both sides, so the model it supports is
strictly `price = ref × k ± offset`. A design needing a non-linear or two-sided-asymmetric
relationship replaces those `Multiply` blocks and leaves everything else — the entire 476-block
quoting engine — untouched. **That is the whole argument for starting here:** the front end is
ten blocks and the back end is six hundred.

**[U] `Ref Prc Multiplier` is unbounded and defaults to 1.** A multiplier of 0 produces a quote
price of `0 ± offset`, and nothing in the graph rejects it — there is no `Alert`/`Terminal`
parameter check on it, unlike `Loss Trigger Increments` in [brackett.md](brackett.md) or the
allocation sum in [tt-multi-level-bracket.md](tt-multi-level-bracket.md). Whether the engine's
`SafeToPlaceOrder` chain catches an absurd price downstream is **[U]**. **[I]** If you build on
this file, that is the first bound to add — a multiplier is a parameter where a typo is a
factor of ten.

## The gap that matters more here

**[I]** [bid-ask-theo.md](bid-ask-theo.md) notes the family has **no `IsNumber`** despite
reading depth by index. Reference Market adds two more unguarded reads: `Ref Bid` and `Ref Ask`
are `lookupType: "best"` on a **second instrument**, which may be illiquid, closed, or simply
not trading when the quoted contract is. adl-kb documents `NaN` for price fields read past
available depth ([block-catalog](../../adl-kb/guides/block-catalog.md)); **[U]** what a `best`
read returns on an empty book is not settled by the file or by adl-kb.

**[I]** [market-base.md](market-base.md) shows the correct handling in TT's own code —
`IsNumber` on the price read, feeding an `Alert` that says *"Unable to quote — no existing
market to lean on"*. **A reference-priced algo needs that more than a theo-priced one does**,
because its price source is a market that can vanish independently of the one it is quoting on.
Two blocks and one alert.

## Everything else

**[V]** Identical to [bid-ask-theo.md](bid-ask-theo.md), which has the detail:

- the fourteen shared Groups, byte-identical, with tiers, ports and adoption costs
- the three ideas worth stealing — side-selector Groups, the virtual-boundary event bridge, and
  `Mkt Price`'s "market without me"
- the same seven `Note` blocks (this file does **not** carry [single-theo.md](single-theo.md)'s
  four extra fill-throttle notes)
- 4 `Terminal` blocks (all **pause**), 8 `Alert` blocks, `Min 25ms`, `QuoteDelay`
- `Quote Throttle` as the only bounded variable, `[100, 99999999]`
- the same exported `Net Pos` block GUID as all three siblings

```bash
python tools/patterns.py --show    "Mkt Price"  --from "Reference Market"
python tools/patterns.py --extract "Group5"     --from "Reference Market" -o event-bridge.json
```

**[V]** `Orders` and `Order` here are the **pre-fix** versions (476 / 231 blocks). Take those
two from [single-theo.md](single-theo.md) instead, which carries the fill-throttle repair.

## Related

[bid-ask-theo.md](bid-ask-theo.md) — the family analysis ·
[single-theo.md](single-theo.md) — the maintained head, and where to take `Orders`/`Order` from ·
[direct-entry.md](direct-entry.md) — the minimal front end ·
[market-base.md](market-base.md) — the depth-guard and no-market-to-lean-on handling this file
should borrow.

**Cited from:** [bid-ask-theo.md](bid-ask-theo.md), [single-theo.md](single-theo.md) and
[direct-entry.md](direct-entry.md) as the family's market-derived front end ·
[brackett.md](brackett.md) for the missing bound on a multiplier-style parameter.
