# BrackeTT

An entry order that spawns a complete bracket — profit target plus synthetic stop — **for every
fill**, each in its own virtual instance, each disposed of when it finishes. 202 blocks, two
nested Groups, nine user variables.

Read it for four things: virtualization **with** an `Exit` block (only this file and
[market-base.md](market-base.md) dispose of their instances), the `Order` block — the managed
workhorse, as opposed to the one-shot `DiscreteOrder` — the corpus's only `TimeAndSales`-driven
synthetic stop, and live re-reading of user variables while the algo runs. It also registers
**`Order` blocks as user variables**, which adl-kb says is not possible.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `BrackeTT.adl.json` |
| Algo id | `b53a78e3-bb0d-49e2-92f2-b4dd9b963e7b` |
| Last modified | 2026-07-27 11:38:39 UTC — **[I]** the corpus collection date, so this is a re-save, not a design date |
| Size | 357,660 bytes |
| Flat blocks / true blocks | 58 / **202** — 71% of the algo is inside one Group |
| Subgraphs / max depth | 2 / **2** (root → `Group0` → `SynthStop`) |
| Edges | 192 |
| Algo flags | `orderSide: true`, **`ignoreMarketState: true`**, `isOmaOta` absent |

**[V]** No `ExistingOrder`, so not an OMA. `Instrument` is `type: "orderInstrument"` and `Qty`
is `type: "orderQty"` — the same OTA/SOA-adjacent shape as [tt-sniper.md](tt-sniper.md).

## Operator surface

**[V]** Nine variables, more than any corpus file except
[tt-multi-level-bracket.md](tt-multi-level-bracket.md) (19) and the theo family (16–18):

| Variable | Block | Type | Default | Bounds |
|---|---|---|---:|---|
| `Instrument` | Instrument | `orderInstrument` | — | — |
| `Price` | Price | `orderPrice` | 201050 | — |
| `Qty` | Number | `orderQty` | 5 | none |
| `Profit Increments` | Number | `userDefined` | 5 | none |
| `Loss Trigger Increments` | Number | `userDefined` | 10 | **[1, 10000]** |
| `On Trigger, Payup Increments` | Number | `userDefined` | 20 | none |
| **`Order`** | **Order** | limit / GTC / tag `EntryOrder` | — | — |
| **`Order0`** | **Order** | limit / GTC / tag `ProfitOrder` | — | — |
| **`Order2`** | **Order** | limit / GTC / tag `SynthStopOrder` | — | — |

> **[V] Three `Order` blocks are listed in the algo's `variables` array.** This directly
> contradicts [algo-types](../../adl-kb/guides/algo-types.md), which states that *only* Bool,
> Number, Instrument and Price blocks can become user-defined variables. The file is
> unambiguous and the format spec's rule applies: **the corpus wins on encoding, adl-kb wins on
> behaviour** — so `variables` demonstrably accepts `Order` GUIDs, and **[U] what the operator
> actually sees for them is unknown.** Most likely candidates are the order's TIF / type /
> tag / colour properties surfacing as launch-time settings. Do not copy this until you have
> seen it in the Designer; do not assume the four-type rule is complete either.

**[V] `Loss Trigger Increments` is the format spec's §5 belt-and-braces example**, and it is
one of only two places in the corpus carrying **both** layers of defence (the other is
[tt-multi-level-bracket.md](tt-multi-level-bracket.md)'s level percentages):

```
minValue: 1, maxValue: 10000          <- the operator cannot type a bad value
LessThan0( @Loss Trigger Increments, 1 ) --> Alert0 ("Loss Trigger Increment must be > 0")
                                         --> Terminal1 (mode: pause)
```

**[I]** Compare [tt-sniper.md](tt-sniper.md), which has the in-graph validator and *no* bound.
Here both are present, on the one parameter that decides where the stop sits — i.e. on the one
number whose corruption loses money. That is the right place to spend the effort.

**[V]** No exports. **[I]** Notable for an algo whose whole state is per-instance: with
virtualization, exported values are not supported inside the Group anyway
([block-catalog](../../adl-kb/guides/block-catalog.md)).

## What it does

### Entry, and re-arming on parameter change

**[V]**

```
Instrument --> Price (Price block) and Order.inst
MsgInfoExtractor2:limitPrice / :orderQuantity --> Order.price / Order.qty
Order (tag EntryOrder, limit, GTC, flipForSell, onExtMod Ignore,
       ignoreInputsAfterAdd false, autoResubmit false)
   out0 fills    --> Jump "Order:fills"
   out2 changeOK --> Jump "Order:changeOK"
```

**[I]** The entry uses `Order`, not `DiscreteOrder` — the block that *continuously manages* the
exchange order, tracking its inputs and modifying the live order when they change
([block-catalog](../../adl-kb/guides/block-catalog.md)). `ignoreInputsAfterAdd: false` keeps
that tracking on. Only three corpus files use `Order` at all — this one (3),
[market-base.md](market-base.md) (4) and [tt-multi-level-bracket.md](tt-multi-level-bracket.md)
(13); every OMA attaches to somebody else's order instead.

**[V] The re-arm loop is the interesting part:**

```
Equal0( @Price, MsgInfoExtractor1:limitPrice ) --> Not0 --> Generator2 (boolTrue)
Equal1( @Qty,   MsgInfoExtractor0:orderQuantity ) --> Not1 --> Generator1 (boolTrue)
Generator1/2 --> ValueInjector5/6 --> MsgInfoExtractor0/1 --> back into the Order's inputs
Generator0 (mode: initialStart) --> ValueInjector4 --> Funnel0 --> MsgInfoExtractor2
```

**[I]** Read: *compare the user variable against the value currently on the order; if they
differ, manufacture a message, inject the new value into it, and push it back through the
order's input chain.* `Generator` in `boolTrue` mode converts the "they differ" boolean into the
discrete pulse ([block-catalog](../../adl-kb/guides/block-catalog.md)); `Generator0` in
`initialStart` mode does the same once at launch to prime the whole chain.

**[I] This is the corpus's answer to "the operator changed a parameter while the algo is
running".** adl-kb notes that variable edits are picked up live for most blocks
([algo-types](../../adl-kb/guides/algo-types.md)), but an order whose price came in on a
discrete message does not re-read a continuous variable by itself. The
`Equal → Not → Generator(boolTrue) → ValueInjector` quartet is a **change detector for a
continuous value**, and it is four blocks. It generalises to anything: watch a value, fire once
per change, carry the new value in the message.

### One bracket per fill — virtualization done properly

**[V]**

```
Jump "Order:fills" --> MsgInfoExtractor3 --> ValueInjector3 --> ValueAccumulator0
                   --> Group0 port "Fill Msg"     [Group0: virtual = true, 144 blocks]
Jump "Instrument"  --> Group0 port "Inst"         [type: STRING]
Group0 port "done" --> ValueAccumulator1
```

**[I]** Exactly the case adl-kb names as virtualization's reason to exist: *"each fill needs its
own exit order that doesn't get clobbered by the next fill"*
([block-catalog](../../adl-kb/guides/block-catalog.md)). Each entry fill spawns an independent
bracket.

**[V] The instrument crosses the boundary as a `string` port.** Group port types are
`message`, `real`, `bool`, `string`, `generic` (format spec §3) — there is no instrument type.
**[I]** So an instrument reference into a Group travels as a string identifier and is
reconstituted inside. Worth knowing before you design a Group interface: `real`, `bool`,
`string`, `message`, and nothing else.

**[V] And this Group has an `Exit` block:**

```
Funnel9 --> Stopwatch0 (formula 1000) --> Branch0 (@OnceTrue0 == TRUE) --> Sequence1
      out1 --> Connector "done"   (tell the outside this bracket finished)
      out2 --> Exit0              (dispose of this instance)
```

**[V]** One of only 7 `Exit` blocks in the corpus. **[I]** The sequencing is the lesson: report
completion *first*, dispose *second*, with a `Sequence` guaranteeing the order — an instance
that exits before its "done" message escapes takes the message with it. The 1000 ms `Stopwatch`
in front is a settling delay an order of magnitude longer than OCO's 250 ms, **[I]** because
what it waits for is a whole bracket unwinding rather than a few deletes.

**[V] Compare [tt-sniper.md](tt-sniper.md) and [oco-2.md](oco-2.md): both virtualize, neither
disposes.** BrackeTT and [market-base.md](market-base.md) are the two files that show the
complete lifecycle. If you take a virtual Group
from either of those, take this exit sequence with it.

### Completion

**[V]**

```
Branch0: if( @Order == 0 AND @ValueAccumulator0 == @ValueAccumulator1, TRUE, FALSE )
      --> Terminal0 (mode: stop)
```

**[I]** "The entry order has no working quantity left **and** every bracket that was started has
reported done." Two counters, one incremented on spawn and one on completion, compared for
equality — the same instance-counting discipline as [oco-2.md](oco-2.md), used here as a
termination condition rather than a loop bound. **[I]** Note it terminates on *equality of
counters*, not on a timeout: an algo that stops while a bracket is still live would abandon a
stop order.

### `SynthStop` — the synthetic stop

**[V]** 78 blocks, **12 ports**, `virtual: false`, nested inside `Group0`:

| Direction | Ports |
|---|---|
| in | `Instrument` (string), `Qty` (real), `input0` (message) |
| out | `Change`, `Delete`, `Fill` (message); `isTriggered`, `trig` (bool); `limitPrice`, `orderQuantity`, `stopWorkingQty`, `workingQuantity` (real) |

```
Instrument --> TimeAndSales0 --> MsgInfoExtractor0
     out6 (trade price) --> LessThanEqual0( tradePrice, stopPrice ) --> OnceTrue0
OnceTrue0 --> Connector "isTriggered"
OnceTrue0 --> StopTrigger (Not) --> Order2 on/off
Order2  (tag SynthStopOrder, limit, GTC, submitInSuspendedState: TRUE, autoResubmit: TRUE)
DiscreteOrder0 (tag StopLimitOrder, cloneIncomingOrder, onExtMod StopManaging)
     --> SingleOrderContainer0 --> Demultiplexer0 --> Fill / Change / Delete connectors
```

**[V] The corpus's single `TimeAndSales` block is here — 1 instance, 1 file.** adl-kb's reason is exactly
this application: `Field` blocks are *snapshots* and can miss a trade between them, while
`TimeAndSales` emits a message on **every** trade
([block-catalog](../../adl-kb/guides/block-catalog.md)). **[I]** A stop that misses the tick
that triggered it is a stop that did not work — this is the one place in an algo where the
snapshot/every-trade distinction is not academic. **If you build any price-triggered exit, use
`TimeAndSales`, not `Field(lastTradePrice)`.**

**[V]** `OnceTrue0` latches the trigger: once hit, permanently hit. **[I]** Third use of
`OnceTrue` for irreversibility ([with-a-tick.md](with-a-tick.md), [oco-2.md](oco-2.md)) and the
most consequential — a stop that un-triggers because the next trade printed higher is not a
stop.

**[V] `Order2` carries `submitInSuspendedState: true`.** **[I]** The stop order is staged at the
exchange in a suspended state and released when `StopTrigger` (the `Not` of the latch) flips —
rather than being created from nothing at trigger time. That is a latency decision, and it is
the only instance of `submitInSuspendedState: true` in the corpus (checked across all 20
`Order` and 23 `DiscreteOrder` blocks).

**[V]** `autoResubmit: true` on both the profit order and the stop order, `false` on the entry.
**[I]** Deliberate: an exit order that vanishes must come back; an entry order that vanishes
should stay gone.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 | `Terminal0` **stop** on completion; `Terminal1` **pause** on bad parameter |
| `Alert` | **[V]** 1 | `"Loss Trigger Increment must be > 0"`, paired with the pause — the §7 idiom. 45 `Alert` blocks corpus-wide across 8 files; [market-base.md](market-base.md) has 8, [tt-multi-level-bracket.md](tt-multi-level-bracket.md) 3 |
| Bounds **and** in-graph validation | **[V]** both | on `Loss Trigger Increments`; only [tt-multi-level-bracket.md](tt-multi-level-bracket.md) does the same |
| `Exit` in the virtual Group | **[V]** **yes** | 7 `Exit` blocks corpus-wide across 6 files; [market-base.md](market-base.md) has 2, the theo family 1 each. [tt-sniper.md](tt-sniper.md) and [oco-2.md](oco-2.md) virtualize with none |
| `TimeAndSales` for the trigger | **[V]** yes | no snapshot gap on the stop |
| `IsNumber` | **[V]** none | **[I]** no `Divide` blocks anywhere in the file — the arithmetic is `Multiply(increments, minPriceIncrement)` and `Add`, which cannot produce `NaN` from valid inputs |
| `MarketState` | **[V]** none | and **`ignoreMarketState: true`** |
| Position / P&L cap | **[V]** none | bounded by `Qty` on the entry order; **[I]** but each fill spawns a bracket, so a partially-filling entry creates many |

**[I] `ignoreMarketState: true` with no `MarketState` block is the same gap as
[tt-sniper.md](tt-sniper.md), and it matters more here** — a bracket holding a live synthetic
stop through a session break is holding protection that depends on trades printing. Whether
`TimeAndSales` fires at all outside a session is **[U]**.

**[V]** One dead jump: `LimitPrc1:val` has no landing.

**[V] The tick arithmetic is clean and worth copying:** two `Field(minPriceIncrement)` blocks
feed `Multiply(Profit Increments, MPI)` and the payup calculation, so every offset in the algo
is expressed in **increments** at the operator surface and converted to price internally. No
hardcoded tick sizes anywhere.

## Reuse

**[V]** Two Groups, both **GREEN**:

| Group | Tier | Size | Virtual | Ports |
|---|---|---:|---|---|
| `Group0` | GREEN | **144** | **yes** | `Fill Msg` (message in), `Inst` (string in), `done` (message out) |
| `SynthStop` | GREEN | **78** | no | 12 — see above |

```bash
python tools/patterns.py --show    "SynthStop"
python tools/patterns.py --extract "SynthStop" --from BrackeTT -o synth-stop.json
python tools/patterns.py --extract "Group0"    --from BrackeTT -o bracket.json
python tools/validate.py synth-stop.json
```

**`SynthStop` is the first entry in `patterns.py`'s index and deserves the position.** 78
blocks, GREEN, twelve declared ports, zero inbound jumps, zero formula leaks — a complete
synthetic stop with a trade-driven trigger, a pre-staged suspended order, a stop-limit
follow-up and a full message interface. **[I]** For anyone building an execution algo that needs
protective exits, this is the single most valuable transplant in the corpus, and its 12 ports
are the price of that completeness: you must supply an instrument string, a quantity and a
message, and consume up to nine outputs.

`Group0` gives you the whole bracket — profit order, synthetic stop, exit lifecycle — behind
three ports. **[I]** A three-port interface on a 144-block subgraph is what virtualization's
constraints buy you (see [oco-2.md](oco-2.md) for the same effect at 66 blocks): no continuous
outputs allowed means no continuous couplings to break.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Synthetic stop** | `SynthStop` | GREEN, complete, `TimeAndSales`-triggered, `OnceTrue`-latched |
| **Per-fill bracket** | `Group0` | GREEN, virtual, and it disposes of itself |
| **Exit sequencing** | `Sequence` → `done` connector, then `Exit` | report before disposing |
| **Live parameter re-arm** | `Equal` → `Not` → `Generator(boolTrue)` → `ValueInjector` | push an edited user variable into a running order |
| **Both-layer validation** | `minValue`/`maxValue` **and** `LessThan` → `Alert` + `Terminal(pause)` | the format spec's §5 recommendation, actually implemented |
| **Increments-not-ticks** | `Field(minPriceIncrement)` × `Multiply` | operator thinks in increments, graph thinks in prices |
| **Spawn/complete counters** | two `ValueAccumulator(1)` + `Equal` in a `Branch` | terminate only when every instance has reported done |

## Jump inventory

**[V]** 36 jumps → 44 landings, one dead. Two `Jump` blocks share the name `Instrument`
(3 landings between them) — **[V]** duplicate jump names are legal and occur in 6 corpus files
(`MEMORY:val` in each theo member, three of them in [market-base.md](market-base.md)).
Selected:

| Name | Source | Consumers |
|---|---|---|
| `Order:fills` / `Order:changeOK` | the entry `Order` | the bracket spawn chain / the re-arm funnel |
| `Inst` | `Inst` Connector inside `Group0` | `Order0`, `SynthStop` |
| `SynthStop:Change` / `:Delete` / `:Fill` / `:trig` | the `SynthStop` Group's out ports | the profit order and the funnels |
| `Sequence0:output_3` | `Sequence0` | `SynthStop`'s message input |
| `StopPrice:limitPrice` | inside `SynthStop` | 3 landings |
| `MinTickInc`, `Field0` | the two `Field(minPriceIncrement)` blocks | the offset multipliers |
| `LimitPrc1:val` | `LimitPrc1` | **no landing — dead** |

**[V]** Note the naming shift inside `SynthStop`: ports carry semantic names (`Change`,
`Delete`, `Fill`, `trig`), and the jumps that carry them onward are `SynthStop:<port>`. Same
`<producer>:<output>` convention as every other file, with the Group standing in as producer —
as in [tt-sniper.md](tt-sniper.md)'s `OrderEntryEnabled:OK to Enter`.

## Related

[tt-multi-level-bracket.md](tt-multi-level-bracket.md) is the same problem at production scale.
[tt-sniper.md](tt-sniper.md) and [oco-2.md](oco-2.md) hold the corpus's other virtual Groups,
both missing the `Exit` this file gets right. For the parameter-validation idiom without the
bound, see [tt-sniper.md](tt-sniper.md).

**Cited from:** [tt-multi-level-bracket.md](tt-multi-level-bracket.md) for the
static-vs-virtual and native-vs-synthetic stop trade-offs · [market-base.md](market-base.md) for
the two files that virtualize *and* dispose · [oco-2.md](oco-2.md) and
[tt-sniper.md](tt-sniper.md) for the `Exit` block they lack · [reference-market.md](reference-market.md)
for parameter validation.
