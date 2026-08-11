# With A Tick

An OMA that watches the volume sitting one tick in front of your resting order and, once that
volume thins to a threshold, **permanently** improves the order's price by one tick. 87 blocks,
one Group, one user variable.

Two things make it worth reading closely. It is the clearest corpus use of `OnceTrue` to make
a state change irreversible — the direct structural answer to the churn problem that
[minvol.md](minvol.md) solves with a counter and a pause. And it is the only one that
*cooperates* with external modification instead of ignoring or surrendering to it.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `With A Tick.adl.json` |
| Algo id | `a0fdb1b9-54f7-4bbf-aa6d-3f657d50eb5c` |
| Last modified | 2021-10-10 20:03:37 UTC |
| Size | 101,164 bytes |
| Flat blocks / true blocks | 79 / **87** |
| Subgraphs / max depth | 1 / 1 |
| Edges | 88 |
| Algo flags | `orderSide: true`, `ignoreMarketState: **false**`, `isOmaOta: **false**` |

**[V]** A pure **OMA** — one `ExistingOrder`, and `isOmaOta: false`, so unlike
[minvol.md](minvol.md) it is not launchable from a ladder. It is applied to an order from the
Order Book ([algo-types](../../adl-kb/guides/algo-types.md)).

## Operator surface

**[V]** One variable, `With a Tick` (Number, `userDefined`, value **0**, unbounded). No exports.

**[I]** The default of 0 is meaningful, not inert: the comparison is against the quantity
resting at the lean price, and a `Field` quantity lookup at a price with nothing on it returns
`0` ([block-catalog](../../adl-kb/guides/block-catalog.md)). So out of the box the algo means
*"step up a tick the moment the level in front of me empties"*. Contrast `Min Qty` in
[minvol.md](minvol.md), whose default of 0 disables the algo entirely. Same block, same value,
opposite consequence — read the comparison before assuming a default is safe.

## What it does

### Intake, and the `Ready` latch

**[V]**

```
ExistingOrder0 --> Sequence0
     out1 --> OrderDetails (MsgInfoExtractor: instrument, orderQuantity, limitPrice,
                            timeInForce, workingQuantity, msg)
     out2 --> Ready (ValueExtractor, formula TRUE) --> Jump "Ready:val"
```

**[I]** `Ready` is the documented latch trick: a `ValueExtractor` whose formula is a constant
outputs the default until its first message, then holds the constant forever
([block-catalog](../../adl-kb/guides/block-catalog.md)). Driven from the *second* output of a
`Sequence` whose first output distributes the order details, it means **"every continuous value
derived from the order is now populated"**.

**[V]** `Ready:val` gates three things — both price-improvement latches and the pause logic —
and nothing acts before it is true.

**[I] This is the corpus's answer to uninitialised continuous data, and it is better than the
alternative.** The algo has three `Field` blocks and no `IsNumber` anywhere; instead of
guarding each value, it gates the whole graph on a single sequence-ordered readiness flag. If
you are building something that derives continuous values from a discrete event, this is the
cheaper pattern: one `Sequence` + one `ValueExtractor(TRUE)` + one `And` per consumer.

### The lean price and the trigger

**[V]** Both sides are built symmetrically and run simultaneously; the inbound message picks
which SOC manages the order:

```
Buy? (Branch, {isBuy})  out1 -> Jump "Buy?:yes" -> SingleOrderContainer0   (buy path)
                        out0 -> Jump "Buy?:no"  -> SingleOrderContainer1   (sell path)

MPI          = Field(minPriceIncrement) of the order instrument
BuyLeanPrc   = Add(      limitPrice, MPI )
SellLeanPrc  = Subtract( limitPrice, MPI )
Field1 = Field(askQuantity, lookupType "price") at BuyLeanPrc
Field3 = Field(bidQuantity, lookupType "price") at SellLeanPrc

LessThanEqual1( Field1, @With a Tick ) AND Ready:val --> OnceTrue0 --> IfThen0.cond
LessThanEqual0( Field3, @With a Tick ) AND Ready:val --> OnceTrue1 --> IfThen1.cond
IfThen0( cond, BuyLeanPrc,  limitPrice ) --> SingleOrderContainer0.price
IfThen1( cond, SellLeanPrc, limitPrice ) --> SingleOrderContainer1.price
```

**[I]** "Is the quantity at the price one tick in front of me at or below my threshold? If so,
move there." `minPriceIncrement` rather than a hardcoded tick size is the correct habit — and
note adl-kb's warning that **Min Price Increment ≠ Min Tick Increment**, since a spread ticks
differently from its outrights ([block-catalog](../../adl-kb/guides/block-catalog.md)).

**[U] Operand order is not recoverable.** Taken at their catalog index positions the edges
read `Subtract(MPI, limitPrice)` and `LessThanEqual(WithATick, Field1)`, both of which are
nonsense; the block labels (`SellLeanPrc`) say otherwise. This is the second independent case
in the corpus — see [conditional.md](conditional.md) — where the positional reading of a
non-commutative block contradicts TT's own label. **Treat `in0`/`in1` ordering as unknown for
`Subtract`, `Divide`, `LessThan`, `GreaterThan` and friends, always.** The method note makes
the same point in general terms.

### `OnceTrue` — the design decision

**[V]** Each trigger passes through a `OnceTrue` block before reaching the `IfThen`.
`OnceTrue` latches TRUE for the life of the algo
([block-catalog](../../adl-kb/guides/block-catalog.md)). 15 `OnceTrue` blocks exist across 9
corpus files; [oco-2.md](oco-2.md) and [brackett.md](brackett.md) use it the same way, to latch
"this order is done" and "the stop has triggered" respectively.

**[I]** So the improvement is **one-way and permanent**. If the level in front refills a
millisecond later, the order does not move back. That single block converts a condition that
could flicker at market-data speed into a state transition that happens at most once — with no
throttle, no `Stopwatch`, no counter and no cap.

**[I] Read [minvol.md](minvol.md) next to this.** Both algos react to thin volume at a price.
MinVol's reaction is reversible, so it needs `Requote Max` and a `Terminal` to stop the churn
after the fact; With A Tick's is irreversible, so it needs nothing. **When a reaction does not
have to be undoable, `OnceTrue` is cheaper and safer than any throttle.** That is the single
most useful design lesson to carry out of this file.

### Cooperating with external modification

**[V]** Both SOCs are `onExtMod: Ignore` — the algo keeps managing an order a human has
touched. It then explicitly re-reads what the human did:

```
Demultiplexer{0,1} out2 (change) --> Funnel2 --> ExtMod (Branch, {isExternalEvent})
    out1 (yes) --> UpdatedOrderQty (ValueExtractor, {orderQuantity})
                   --> AdjustOrderQty (ValueExtractor, TRUE)
IfThen3( AdjustOrderQty, UpdatedOrderQty, OrderDetails:orderQuantity ) --> SOC0.qty
IfThen4( AdjustOrderQty, UpdatedOrderQty, OrderDetails:orderQuantity ) --> SOC1.qty
```

**[I]** Read: *until a human changes the quantity, drive the SOC from the original order
quantity; after that, drive it from whatever the human set.* `AdjustOrderQty` is another
constant-`TRUE` `ValueExtractor` latch, this time meaning "an external change has happened at
least once".

**[I]** That is a third distinct stance on interference, and the corpus contains all three:

| Stance | Setting | Seen in |
|---|---|---|
| Surrender | `onExtMod: StopManaging` | [conditional.md](conditional.md) (the primary order) |
| Ignore and overwrite | `onExtMod: Ignore`, no re-read | [minvol.md](minvol.md) |
| **Ignore and cooperate** | `onExtMod: Ignore` **+** explicit `{isExternalEvent}` re-read | **this file** |

The third is the most work and usually the right answer for anything a trader will supervise.
The mechanism is small enough to copy verbatim: `Branch{isExternalEvent}` → capture
`ValueExtractor` → latch `ValueExtractor(TRUE)` → `IfThen(latch, captured, original)`.

### Shutdown

**[V]** Two independent stops:

```
Fills (VA, {fillQuantity}) from both demuxes' fill outputs
GreaterThan0( Fills, 0 )                                    \
Equal0( 0, SOC0.workingQuantity + SOC1.workingQuantity )    /--> And "OrderFilled" --> Or0
OrderDeleted (ValueExtractor TRUE, from both demuxes' delete outputs) ------------> Or0
Or0 --> Terminal0 (mode: stop)
```

**[I]** "We have fills and nothing is working" **or** "the order went away" → stop. Summing the
two SOCs' working quantities is how the algo stays side-agnostic: only one of them is ever
non-zero.

### `GTD Pause Logic` — the Group, and a label that lies

**[V]** 8 blocks, **no ports at all**, three inbound jumps:

```
Equal1( OrderDetails:timeInForce, Number1 = 1 ) AND MarketClosed AND Ready:val
    --> Terminal1 (mode: stop)
```

**[V] `Number1` is 1, and TIF code 1 is `Day`, not GTD** — the code table is in
[block-catalog](../../adl-kb/guides/block-catalog.md) (GTC is 2, GTDate is 7). The Group is
named `GTD Pause Logic`; the logic it contains fires on a **Day** order. **[I]** Either the
name is stale or the intent is "stop managing anything that isn't good-till-something when the
session ends". Whichever, **do not trust a Group's name over its contents** — this is the
cleanest example in the corpus of the two disagreeing.

**[V] The `MarketState` block is also compromised by an algo setting.** `MarketClosed` is a
`MarketState` block with `state: "close"`, but the algo has **`ignoreMarketState: false`**.
adl-kb is explicit that the algo auto-pauses whenever the market leaves its session unless
that setting is enabled, *"which is exactly the case you were testing for"*
([block-catalog](../../adl-kb/guides/block-catalog.md),
[algo-types](../../adl-kb/guides/algo-types.md)). **[I]** So this Group is very likely dead
code in practice: the algo pauses before its own close-detection can fire. If you adopt it,
`ignoreMarketState` must be turned on — and that in turn removes the platform's own protection
from the *whole* algo, which is a much larger decision than adding one Group.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 | both `stop`; no pause tier at all |
| `Alert` | **[V]** none | again — three shutdown conditions, no operator message |
| `IsNumber` | **[V]** none | mitigated structurally by the `Ready` latch; and the `Field` lookups are quantity fields, which return `0` rather than `NaN` past available depth |
| `MarketState` | **[V]** 1 | present but **[I]** neutered by `ignoreMarketState: false` (above) |
| Throttle / `Stopwatch` | **[V]** none | by design — `OnceTrue` removes the need |
| Bounds | **[V]** none | `With a Tick` is unbounded |
| Position / P&L cap | **[V]** none | inherent to an OMA that never adds quantity |

**[V]** One dead jump: `OrderDetails:workingQuantity` has no landing. **[I]** The field is
extracted and thrown away — probably left over from an earlier version of the shutdown test,
which now sums the SOCs' working quantities instead.

## Reuse

**[V]** One Group, tier **AMBER**:

| | |
|---|---|
| Name | `GTD Pause Logic` |
| Size | 8 blocks, 7 edges |
| Ports | **none** |
| Required inbound jumps | `MarketClosed`, `OrderDetails:timeInForce`, `Ready:val` |

```bash
python tools/patterns.py --show "GTD Pause Logic"
python tools/patterns.py --extract "GTD Pause Logic" --from "With A Tick" -o gtd-pause.json
```

**[I]** A Group with **no ports** is worth pausing on: its entire interface is jump names, so
`patterns.py`'s signature line reads `(no ports)` and tells you nothing. Everything it needs
and everything it does travels by wormhole. That is legal and TT does it (the `Alerts` Group in
the theo algos is the same shape), but it means the *only* way to know what it touches is the
jump list — which is exactly why `profile_algo.py` prints one.

Given the `ignoreMarketState` problem and the Day-vs-GTD mismatch, **[I]** this particular
Group is a template to rebuild rather than a part to transplant.

The better reuse in this file is not the Group at all:

| Take | Blocks | Why |
|---|---|---|
| **`Ready` gate** | `Sequence` + `ValueExtractor(TRUE)` + one `And` per consumer | one flag that means "all continuous values derived from the order are populated"; replaces scattered `IsNumber` guards |
| **`OnceTrue` one-way reaction** | `LessThanEqual` + `And` + `OnceTrue` + `IfThen` | converts a flickering condition into a single irreversible state change — no throttle needed |
| **External-mod cooperation** | `Branch{isExternalEvent}` + 2 `ValueExtractor` + `IfThen` | keep managing an order a human edited, on the human's terms |
| **Side-symmetric SOC pair** | `Branch{isBuy}` + two SOCs + `Add` of both working quantities | handle both sides without `flipForSell`, and stay side-agnostic downstream |
| **Tick arithmetic** | `Field(minPriceIncrement)` + `Add`/`Subtract` | never hardcode a tick size |

## Jump inventory

**[V]** 15 jumps → 25 landings; one dead.

| Name | Source | Consumers |
|---|---|---|
| `OrderDetails:limitPrice` | `OrderDetails` | `IfThen0`, `IfThen1`, `BuyLeanPrc`, `SellLeanPrc` |
| `Ready:val` | `Ready` (ValueExtractor) | `And1`, `And2`, `And4` |
| `MPI` | `MPI` (Field) | `BuyLeanPrc`, `SellLeanPrc` |
| `With a Tick` | `With a Tick` (Number) | `LessThanEqual0`, `LessThanEqual1` |
| `OrderDetails:instrument` | `OrderDetails` | `Field1`, `Field3` |
| `OrderDetails:orderQuantity` | `OrderDetails` | `IfThen3`, `IfThen4` |
| `UpdatedOrderQty:val`, `AdjustOrderQty:val` | the two external-mod extractors | `IfThen3`, `IfThen4` |
| `Buy?:yes` / `Buy?:no` | `Buy?` (Branch out1 / out0) | `SingleOrderContainer0` / `1` |
| `SingleOrderContainer0:workingQuantity`, `…1:…` | both SOCs | `Add0` |
| `MarketClosed` | `MarketState` | `And3` (inside the Group) |
| `OrderDetails:timeInForce` | `OrderDetails` | `Equal1` (inside the Group) |
| `OrderDetails:workingQuantity` | `OrderDetails` | **no landing — dead** |

**[V]** Same `<producer>:<field>` convention as [minvol.md](minvol.md) and
[conditional.md](conditional.md), including `:yes` / `:no` on Branch outputs — which is what
established that `Branch` `out0` is FALSE and `out1` is TRUE.

## Related

[minvol.md](minvol.md) is the direct comparison: same input signal, reversible reaction,
therefore a throttle problem this file does not have. [conditional.md](conditional.md) shows
the surrender stance on external modification. For `MarketState` used in an algo that actually
enables `ignoreMarketState`, see [market-base.md](market-base.md).

**Cited from:** [minvol.md](minvol.md) for the opposite churn trade-off ·
[tt-sniper.md](tt-sniper.md) and [oco-2.md](oco-2.md) for the `OnceTrue` irreversibility latch ·
[market-base.md](market-base.md) and [bid-ask-theo.md](bid-ask-theo.md) for the constant-`TRUE`
`ValueExtractor` readiness gate · [tt-multi-level-bracket.md](tt-multi-level-bracket.md) for the
"ignore and cooperate" stance on external modification.
