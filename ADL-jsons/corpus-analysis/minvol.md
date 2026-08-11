# MinVol

An OMA that pulls your order off a price level when the resting volume there gets too thin,
and puts it back when the volume returns. 78 blocks, one Group, three user variables — and
**three `Note` blocks in which TT explains their own reasoning**. Eight corpus files carry
`Note` blocks, but most are empty canvas furniture ([market-base.md](market-base.md) has 28, of
which 27 are blank); only this file, [oco-2.md](oco-2.md), [single-theo.md](single-theo.md) and
the theo family carry written rationale, and MinVol's three are the only ones that document
**bugs-in-waiting** a reader would otherwise never see.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `MinVol.adl.json` |
| Algo id | `336570a4-4b90-4e26-9b62-5e2c6a20ef13` |
| Last modified | **2025-09-12** 21:57:08 UTC — by five years the newest file in the corpus |
| Size | 105,594 bytes |
| Flat blocks / true blocks | 65 / **78** |
| Subgraphs / max depth | 1 / 1 |
| Edges | 68 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta: true` |

**[V]** An **OMA** (one `ExistingOrder` block) that is also OTA-shaped: its `Price` variable has
`type: "orderPrice"`, which is the Order-Price variable type
([algo-types](../../adl-kb/guides/algo-types.md)), and its `DiscreteOrder` has
`flipForSell: true`. **[I]** So it is meant to be attached to a resting order on a ladder and
to work on either side.

## Operator surface

**[V]**

| Variable | Block | Default | Bounds |
|---|---|---:|---|
| `Min Qty` | Number, `userDefined` | **0** | none |
| `Requote Max` | Number, `userDefined` | 10 | none |
| `Price` | Number, `orderPrice` | 10 | none |

**[V] One export:** `RequoteCount` (a `ValueAccumulator`) becomes a live dashboard column. This
is the only corpus file whose export is a *diagnostic counter* rather than a price or quantity
— the operator watches how hard the algo is churning.

**[I] `Min Qty` defaults to 0, which makes the algo inert.** The comparison is
`(volumeAtMyPrice − 0) < MinQty`; with `MinQty = 0` that is `vol < 0`, never true. Shipping
with a safe-but-useless default is defensible, but note it is also *unbounded* — nothing stops
an operator typing a `Min Qty` so large the order can never rest. Compare `Quote Throttle` in
the theo algos, which carries `minValue: 100` (format spec §5).

## What it does

### The detector — `Group0`, the only Group in the file

**[V]** 13 blocks, one output port `TooLittleVol` (bool). Inside:

```
Order:instrument (jump landing) --> BidQty (Field: bidQuantity, lookupType "price")
                                --> AskQty (Field: askQuantity, lookupType "price")
Price (jump landing)            --> both Fields' price input
Order:isBuy (jump landing)      --> IfThen0  selects BidQty or AskQty
IfThen0 --> Subtract0 --> LessThan "TooLittleVol" <-- Min Qty
Number0 (static 0) --> Subtract0
TooLittleVol --> Connector "TooLittleVol"  (the Group's out port)
```

**[I]** "How much quantity is resting at my price on my side of the book, minus my own order,
and is that less than `Min Qty`?" `lookupType: "price"` is the Field block's price-lookup mode
— quantity at a *specific* price rather than a depth index
([block-catalog](../../adl-kb/guides/block-catalog.md)).

**[V] The subtraction of "my own order" is hard-coded to zero**, and TT's own `Note` inside the
Group says why:

> *"When we want to enhance this algo to consider the users own orders, we must replace this
> hard-coded 0 number block with the SOC:workingQuantity jump landing block."*

**[V]** And the `SOC:workingQuantity` jump *already exists* in the file, with a landing block
sitting inside the Group, **wired to nothing**. TT staged the enhancement and did not finish
it. **[I]** As shipped, the algo counts its own resting quantity as part of the volume it is
measuring — so a large order on a thin level partly justifies its own presence. If you adopt
this Group, making that one substitution is the first thing to do.

### Intake and the suspended-order swap

**[V]**

```
ExistingOrder0 --> ExistingOrderPlaced (ValueAccumulator, formula 1)
               --> Order (MsgInfoExtractor: instrument, isBuy, msg)
   out0 instrument --> Jump "Order:instrument"
   out4 isBuy      --> Jump "Order:isBuy"
   out7 msg        --> IsSuspended? (Branch, formula {isSuspended})
        out0 --> Jump "IsSuspended?:no"  --> Funnel0 -> SOC
                                         --> Funnel2 -> State0
                                         --> Funnel3 -> OrderIsWorking
        out1 --> Suspended (Sequence)
                 out1 --> Jump "Suspended:output_1" --> InitOrderQty (VA, {orderQuantity})
                 out2 --> Jump "Suspended:output_2" --> Funnel2 -> State0
                                                    --> SingleOrderContainer0 (del <- Boolean0 TRUE)
```

**[V] This file settles a question the rest of the corpus leaves open: `Branch` `out0` is the
FALSE/"no" output and `out1` is TRUE/"yes".** TT's own jump names prove it — the jump hanging
off `out0` of `IsSuspended?` is literally named **`IsSuspended?:no`**, and the same convention
holds for `External Delete?:no` (out0) and `IsFirstRun:yes` (out1). The catalog cannot tell you
this; the labels can. Every other doc in this folder relies on it.

**[I]** The suspended path is the same swap idiom as [conditional.md](conditional.md): capture
the original quantity, delete the suspended original through a dedicated SOC driven by a static
TRUE, and let the state machine place a live replacement.

### The gate — one working order at a time

**[V]** `State0`'s only formula:

```
!TooLittleVol AND OrderIsWorking == 0
```

and TT's `Note` sitting next to it:

> *"This State block above is where the most sensitive part of this algo lives: this determines
> when it's safe to place a new order. It relies on the value of OrderIsWorking to prevent
> multiple working orders at the same time."*

**[V]** `OrderIsWorking` is a `ValueAccumulator` with formula `1` — an event counter, the
documented idiom for counting messages ([block-catalog](../../adl-kb/guides/block-catalog.md)).
It is incremented on every path that results in a live order and reset on every path that
retires one.

**[I]** This is a **mutex built out of an accumulator and a State block**, and it is the single
most transferable idea in the file. ADL has no lock primitive; the pattern is:

1. a counter incremented by every "resource acquired" pathway,
2. a `State` block whose formula includes `counter == 0`,
3. every "resource released" pathway routed to the counter's reset port,
4. a `Funnel` looping the State's downstream back into its own input so the condition is
   re-evaluated the moment anything changes.

**[V]** Release path:

```
State0 --> NewOrder (Sequence)
    out1 --> Jump "NewOrder:output_1" --> Funnel3 --> OrderIsWorking  (increment)
    out2 --> Jump "NewOrder:output_2" --> DiscreteOrder1              (place the order)
    out0 --> Funnel2                                                  (loop back into State0)
```

**[V]** `DiscreteOrder1`'s field formulas:

```
price    = @Price
quantity = if(@InitOrderQty > 0, @InitOrderQty, @DeletedOrder.<remaining qty field>)
```

**[I]** Requote at the original size if we know it, else at whatever was left on the order we
just pulled. `cloneIncomingOrder: true`, `flipForSell: true`, `TIF: day`, `onExtMod: Ignore`.

### The pull

**[V]** `Group0`'s `TooLittleVol` output leaves through `Jump "Group0:TooLittleVol"` and lands
directly on `SOC`'s delete input. There is no delay, no hysteresis and no throttle between the
book thinning out and the order being pulled.

**[I]** That is the design's sharpest edge. A level whose quantity oscillates around `Min Qty`
produces delete/requote churn at market-data speed. The only brake is `Requote Max`, which
counts churn *after the fact* and pauses the algo:

```
Sequence3 out2 --> RequoteCount (VA, formula 1)
RequoteCount msg --> Branch1 (@RequoteCount >= @Requote Max) --> out1 --> Terminal1 (mode: pause)
```

**[I]** Compare the theo algos, which put a `Stopwatch`-based throttle *in front of* each quote
and delete action, split per side (format spec §7). MinVol has one 25 ms `Stopwatch` and it is
not a throttle — see below. If you reuse this detector, add a throttle between it and the SOC.

### The delete-settle path, and the pause bug TT documented

**[V]**

```
SOC msgs --> Demultiplexer "SOC"
   out0 --> External Delete? (Branch, {isExternalEvent})
        out0 (no)  --> Jump "External Delete?:no" --> Sequence3
                        out1 --> DeletedOrder (MsgInfoExtractor) --> msg --> Stopwatch0 (25)
                                   --> Jump "Stopwatch0" --> Funnel4 --> OrderIsWorking (reset)
                        out2 --> RequoteCount (increment)
        out1 (yes) --> Funnel5 --> Terminal2 (mode: stop)
   out1 --> IsFullyFilled? (Branch, {workingQuantity} == 0)
        out1 --> Funnel5 --> Terminal2 (mode: stop)
   out2 --> Jump "SOC:chg"   <-- DEAD: no landing anywhere
```

**[I]** The 25 ms `Stopwatch` is the file's settle-delay: after *our own* delete is
acknowledged, wait the minimum permitted interval and only then clear the mutex, so the State
block cannot re-fire against a half-retired order. 25 is the documented Stopwatch floor
([gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md)) — the same "shortest legal
delay" trick as in [conditional.md](conditional.md).

**[V]** And that Stopwatch is exactly what TT's third `Note` is about:

> *"This `is first run?` check is here strictly because we cannot rely on the stopwatch block
> to reset the OrderIsWoring accumulator. When the algo is paused, and the child order is
> deleted, this delete will get lost inside the Stopwatch block because Stopwatches do not fire
> in a paused state. And we don't want to reset the OrderIsWorking on the *first* start because
> then that would reset a VALID value of 1."*

**[V]** The repair:

```
Generator0 (mode: everyStart) --> IsFirstRun (Branch, @ExistingOrderPlaced == 1)
     out1 (yes) --> Jump "IsFirstRun:yes" --> ExistingOrderPlaced (reset)
     out0 (no)  --> Funnel4 --> OrderIsWorking (reset)
```

**[I]** `everyStart` fires on launch *and* on every resume. First start: `ExistingOrderPlaced`
is 1, so the algo only clears that marker and leaves the mutex alone. Any later start: the
marker is 0, so the mutex is force-cleared — repairing the state a paused Stopwatch silently
swallowed.

**[I] This is the most valuable single lesson in the corpus for anyone building stateful
algos.** A `Stopwatch` mid-pathway is a place where a discrete message can *disappear* across a
pause, and any state it was going to update is left stale. The general repair is TT's: an
`everyStart` Generator plus a first-run discriminator that re-establishes invariants on resume.
adl-kb documents that a timer elapsing during algo-server *recovery* fails the algo
([block-catalog](../../adl-kb/guides/block-catalog.md)); it does **not** document this
pause-swallows-the-message case. **[V]** The Note is the only source for it.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 | `Terminal1` **pause** on requote cap; `Terminal2` **stop** on external delete or full fill |
| `Alert` | **[V]** none | both terminals fire silently — the operator sees a stopped algo and no reason |
| `IsNumber` | **[V]** none | see below |
| `MarketState` | **[V]** none | and `ignoreMarketState: false`, so the algo auto-pauses out of session — which, given the Note above, is a state transition it has to repair on resume |
| Bounds on variables | **[V]** none | `Min Qty` and `Requote Max` are both unbounded |
| Throttle | **[V]** none | the 25 ms Stopwatch is a settle-delay, not a rate limiter |
| Position / P&L cap | **[V]** none | inherent — an OMA that only requotes an existing order |

**[I] The NaN exposure is genuinely low here, and for an instructive reason.** There is no
division anywhere in the file, and the two `Field` lookups return **quantity** fields:
adl-kb states that a lookup past available depth yields `0` for quantity fields and `NaN` only
for price fields ([block-catalog](../../adl-kb/guides/block-catalog.md)). So the absence of
`IsNumber` is a considered omission, not an oversight — which is the useful takeaway. Copy the
detector into a design that reads a *price* at that level and you have inherited a NaN path
that TT never had.

**[V] Two loose ends in the file as shipped:** the `SOC:chg` jump has no landing at all (one of
the six dead jumps the format spec counts corpus-wide), and the `SOC:workingQuantity` landing
inside `Group0` is placed but unwired. Both are inert. **[I]** Both are also evidence that TT
ships work-in-progress, which is worth remembering before treating any corpus file as a
finished specification.

## Reuse

**[V]** One Group, tier **AMBER**:

| | |
|---|---|
| Name | `Group0` (auto-named — no design intent in the title) |
| Size | 13 blocks, 12 edges |
| Port | `TooLittleVol` — **out**, `bool` |
| Required inbound jumps | `Order:instrument`, `Order:isBuy`, `Price`, `SOC:workingQuantity` |
| Formula leaks | none |

```bash
python tools/patterns.py --show "Group0" --from MinVol
python tools/patterns.py --extract "Group0" --from MinVol -o thin-level-detector.json
python tools/validate.py thin-level-detector.json
```

**The `--from` filter is not optional here.** TT reused the name `Group0` for twelve different
Groups across the corpus, and `--extract` refuses an ambiguous name rather than guessing. (Use
`--guid <prefix>` if one file contains several identically named Groups.)

Adopting it costs four jump feeds, and **[I]** three of the four are trivial — an instrument, a
side boolean and a price. The fourth, `SOC:workingQuantity`, is the one the Note says to
actually wire up.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Thin-level detector** | `Group0` | "quantity resting at my price, my side, excluding me" — side-aware via one `IfThen`, self-contained apart from its jumps |
| **Accumulator mutex** | `ValueAccumulator(1)` + `State` + `Funnel` loop-back | **[I]** the corpus's only single-actor guard; ADL has no lock primitive and adl-kb documents none |
| **everyStart state repair** | `Generator(everyStart)` + first-run `Branch` + reset | repairs invariants a pause corrupted; TT's Note is the only documentation of the failure it fixes |
| **Diagnostic export** | `RequoteCount` in `exports` | export the churn counter, not just the price — the operator can see the algo thrashing before the cap trips |

Not worth taking as-is: the delete path, which needs a throttle between the detector and the
SOC before it is fit for a fast market.

## Jump inventory

**[V]** 15 jumps → 19 landings, of which one jump is dead and one landing is unwired.

| Name | Source | Consumers |
|---|---|---|
| `IsSuspended?:no` | `IsSuspended?` (Branch out0) | `Funnel0`, `Funnel2`, `Funnel3` |
| `Order:instrument` | `Order` (MsgInfoExtractor) | `DiscreteOrder1`, `BidQty`, `AskQty` |
| `Order:isBuy` | `Order` (MsgInfoExtractor) | `IfThen0` |
| `Price` | `Price` (Number) | `BidQty`, `AskQty`, `SOC` |
| `Suspended:output_1` / `:output_2` | `Suspended` (Sequence) | `InitOrderQty` / `Funnel2`, `SingleOrderContainer0` |
| `NewOrder:output_1` / `:output_2` | `NewOrder` (Sequence) | `Funnel3` / `DiscreteOrder1` |
| `Group0:TooLittleVol` | `Group0` (Group) | `SOC` |
| `External Delete?:no` | `External Delete?` (Branch out0) | `Sequence3` |
| `Stopwatch0` | `Stopwatch0` | `Funnel4` |
| `IsFirstRun:yes` | `IsFirstRun` (Branch out1) | `ExistingOrderPlaced` |
| `Generator0:messageOut` | `Generator0` | `RequoteCount` |
| `SOC:workingQuantity` | `SOC` (SingleOrderContainer) | landing exists, **wired to nothing** |
| `SOC:chg` | `SOC` (Demultiplexer) | **no landing — dead** |

**[V]** The naming convention is rigid and worth stealing wholesale:
`<producerBlock>:<outputName>`, with Branch outputs named `:yes` / `:no` and Sequence outputs
named `:output_1` / `:output_2`. In a 41%-routing-blocks language, a jump name *is* the wire
label.

## Related

Same suspended-order swap and 25 ms settle-delay in [conditional.md](conditional.md). For the
throttling this file lacks, see the per-side `Stopwatch` throttles in
[bid-ask-theo.md](bid-ask-theo.md). `With A Tick` ([with-a-tick.md](with-a-tick.md)) is the
other small requoting algo and makes the opposite trade-off.

**Cited from:** [conditional.md](conditional.md) and [oco-2.md](oco-2.md) for the
suspended-order swap · [tt-sniper.md](tt-sniper.md) for the count-afterwards approach to rate
limiting · [single-theo.md](single-theo.md) and [oco-2.md](oco-2.md) for the pause/resume state
repair · [market-base.md](market-base.md) for the inert-by-default parameter.
