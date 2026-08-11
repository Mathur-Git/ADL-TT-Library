# Design Patterns & Recipe Index

"I need to do X — which blocks, and where is the worked example?"
Every recipe links to the TT page that demonstrates it.

[ADL KB Home](../ADL-KB-Home.md) · [Block Catalog](block-catalog.md) · [Core Semantics](core-semantics.md) · [Formulas](formula-reference.md) · [Gotchas](gotchas-and-limits.md)

---

## Order entry

| Goal | Construction | Reference |
|---|---|---|
| Single working order tracking the market | [Order](../reference/trading-blocks/order-block.md) block; Field → `price`, Number → `qty`, Bool/logic → `on/off` | [Algos in ADL](../reference/adl-overview/introduction-to-adl/description-introduction-to-adl/algos-in-adl.md) |
| One-shot order on an event | [Discrete Order](../reference/trading-blocks/discrete-order-block.md), price/qty via formula | [Discrete Order](../reference/trading-blocks/discrete-order-block.md) |
| Order stack / scale ("up or down the book") | [Loop](../reference/miscellaneous-blocks/loop-block.md) `loop` port → Discrete Order; `index` × tick + offset = price | [Order stack logic](../reference/adl-overview/advanced-concepts/description/order-stack-logic-with-flip-for-sell-functionality.md) · [Scale Order algo](../reference/adl-overview/advanced-concepts/task/creating-a-scale-order-algo.md) · [Stacked Q holder](../reference/adl-overview/advanced-concepts/task/stacked-q-holder-example.md) |
| Time-sliced / TWAP-style entry | Generator `TimeInterval` → Discrete Order; compare working qty vs total qty for the enable condition | [TT time sliced order](../reference/adl-overview/advanced-concepts/task/creating-a-tt-time-sliced-order.md) |
| Iceberg with randomised clip and delay | [Random Number](../reference/miscellaneous-blocks/random-number-block.md) → qty and → [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md); [State](../reference/discrete-blocks/state-block.md) tracks fill status | [Submit iceberg with random qty and delay](../reference/adl-overview/advanced-concepts/task/submit-iceberg-with-random-quantity-and-delay.md) |
| Reload / replenish without relaunching | `floor(fills / clip) * clip + clip`, then [Math](../reference/arithmetic-blocks/math-block.md) `Min` against total qty → `qty` | [Clip size reload functionality](../reference/adl-overview/advanced-concepts/description/clip-size-reload-functionality.md) |
| Manual "reload button" | user-defined [Bool](../reference/basic-blocks/bool-block.md) toggled TRUE/FALSE | [Clip size reload functionality](../reference/adl-overview/advanced-concepts/description/clip-size-reload-functionality.md) |

## Exits and position management

| Goal | Construction | Reference |
|---|---|---|
| Exit N ticks off the average open price | MsgInfoExtractor → Value Accumulator (fill qty and fill notional) → divide → add ticks | [Building your first algo](../reference/adl-overview/building-your-first-algo/introduction.md) · [Creating the exit order](../reference/adl-overview/building-your-first-algo/lessons/creating-the-exit-order.md) |
| **Independent exit per fill** | fill message → **virtualized** group containing the exit logic | [Virtualization](../reference/adl-overview/advanced-concepts/description/virtualization.md) |
| Scratch the order if queue thins out | monitor qty at your price; pull when below threshold | [Profit or scratch algo](../reference/adl-overview/advanced-concepts/task/creating-a-profit-or-scratch-algo.md) |
| Pay up one tick when the opposite side thins | OMA on an existing order; threshold on opposing qty | [With a tick algo](../reference/adl-overview/advanced-concepts/task/creating-a-with-a-tick-algo.md) · [Submitting with-a-tick orders](../reference/adl-overview/advanced-concepts/task/submitting-with-a-tick-orders.md) |
| Delay between fill and follow-up order | [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) on the fill message | [Time and timers](../reference/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl.md) |
| Automated hedge of a cash position | market-order hedge driven from notional exposure | [Fixed income futures hedge](../reference/adl-overview/advanced-concepts/case-studies-advanced-concepts/automating-a-fixed-income-futures-hedge-order.md) |

## Time and scheduling

→ [Time and timers in TT ADL](../reference/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl.md) — the five canonical use cases.

| Goal | Construction |
|---|---|
| Delay a discrete event | [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) (formula = ms, min 25) |
| Act at a specific UTC date **and** time | Generator `AtStartTime` with UTCDate **and** UTCTime connectors |
| Act at a time **every day** | Generator `AtStartTime` with **only** UTCTime connectors (repeats daily) |
| Act on a calendar-picked datetime | Generator `AtStartTime-Combined` (also outputs epoch ms) |
| Repeating heartbeat | Generator `TimeInterval` with `enabled` / `repeating` / `periodMs` (min 100 ms) |
| Know when an event occurred | MsgInfoExtractor year/month/day/hour/minute/second/ms connectors |
| Trade only between start and stop times | two `AtStartTime` Generators → two Value Accumulators → AND → Order `on/off` |
| UTC→local conversion and a seconds counter | subtract hours; 1000 ms Generator → Value Extractor formula `1` |

→ [Submit orders between specific start/stop times](../reference/adl-overview/advanced-concepts/task/submit-orders-between-specific-start-stop-times.md) ·
→ [UTC time trigger and time counter](../reference/adl-overview/advanced-concepts/task/creating-a-utc-time-trigger-and-time-counter.md)

## Market data, bars and indicators

| Goal | Construction | Reference |
|---|---|---|
| Bars + indicators, server-side | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) block (max 5/algo, ≤250 bars, Production only) | [Analytics block](../reference/miscellaneous-blocks/analytics-block.md) |
| OHLC / VWAP built by hand | [Time and Sales](../reference/trading-blocks/time-and-sales-block.md) → Discrete Min/Max for H/L, Value Bucket (`Last`) for O/C | [OHLC and VWAP time bars](../reference/adl-overview/advanced-concepts/task/creating-ohlc-and-vwap-time-bars.md) · [Time series bars](../reference/adl-overview/advanced-concepts/task/time-series-bars-for-ohlc-and-vwap-values.md) |
| Moving average of any value | [Moving Average](../reference/discrete-blocks/moving-average-block.md) driven by a Generator; **gate on `ready`** | [Moving Average](../reference/discrete-blocks/moving-average-block.md) |
| MA crossover signal | two Moving Average blocks → [Formula](../reference/arithmetic-blocks/formula-block.md) block comparing the two `avg` outputs | [Formula block](../reference/arithmetic-blocks/formula-block.md) |
| Volume in the last N seconds | Value Bucket keyed on second-of-day, `Sum` mode; Stopwatch to age out | [Tracking recent volume](../reference/adl-overview/advanced-concepts/task/tracking-recent-volume.md) · [Summarize volume](../reference/adl-overview/advanced-concepts/task/summarize-volume.md) |
| Uptick / downtick counter | two Value Extractors holding successive bid prices + two State blocks | [Uptick and downtick counters](../reference/adl-overview/advanced-concepts/task/creating-uptick-and-downtick-counters.md) |
| Accumulated LTQ (ADL gives unaccumulated) | sum LTQ while LTP is unchanged | [Accumulated vs unaccumulated LTQ](../reference/adl-overview/advanced-concepts/description/displaying-accumulated-or-unaccumulated-ltq.md) |
| Estimated position in queue | start with qty at your price, subtract trades at that price, clamp to BidQty | [EPIQ](../reference/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq.md) |
| Queue priority before the open | work orders during the pre-open state | [Position in queue during pre-open](../reference/adl-overview/advanced-concepts/case-studies-advanced-concepts/generating-position-in-queue-during-pre-open.md) |

## Control flow

| Goal | Construction |
|---|---|
| Deterministic ordering of branches | [Sequence](../reference/discrete-blocks/sequence-block.md) block — never fan out a discrete output |
| Merge several event sources into one input | [Funnel](../reference/discrete-blocks/funnel-block.md) |
| Route by message type | Single Order Container → [Demultiplexer](../reference/discrete-blocks/demultiplexer-block.md) |
| Route by condition, immediately | [Branch](../reference/discrete-blocks/branch-block.md) |
| Route by first-true among many states | [State](../reference/discrete-blocks/state-block.md) |
| Latch a condition permanently | [Once True](../reference/logic-blocks/once-true-block.md) |
| Snapshot the market at an instant | [Value Extractor](../reference/discrete-blocks/value-extractor-block.md) |
| Count events | [Value Accumulator](../reference/discrete-blocks/value-accumulator-block.md) with formula `1` |
| Carry a value out of a virtualized block | [Value Injector](../reference/discrete-blocks/value-injector-block.md) → `userField1..4` → [Value Extractor](../reference/discrete-blocks/value-extractor-block.md) |
| Stop the algo on a condition | [Terminal](../reference/miscellaneous-blocks/terminal-block.md) |

## Risk

| Goal | Construction | Reference |
|---|---|---|
| Cap loss per algo instance | [Pnl](../reference/miscellaneous-blocks/pnl-block.md) block (positive max-loss input) | [Pnl block](../reference/miscellaneous-blocks/pnl-block.md) |
| Cap position per side | [Position Risk](../reference/miscellaneous-blocks/position-risk-block.md) — one block per side | [Position Risk block](../reference/miscellaneous-blocks/position-risk-block.md) |
| Cut order latency | Position Risk with `Enable Position Reserve` (**dedicated Algo Servers only**) | [Position Risk block](../reference/miscellaneous-blocks/position-risk-block.md) |
| Halt on market state change | [Market State](../reference/trading-blocks/market-state-block.md) → [Terminal](../reference/miscellaneous-blocks/terminal-block.md) | [Market State block](../reference/trading-blocks/market-state-block.md) |
| Audit-trail an event | [Alert](../reference/miscellaneous-blocks/alert-block.md) with `Audit Trail` action | [Alert block](../reference/miscellaneous-blocks/alert-block.md) |

## Bi-directional algos

Build the **buy side only**, then enable **Flip for Sell Order** on the pivot blocks — Add/Subtract,
Greater/Less Than, Field, Order, Discrete Order, Position Risk. A `Side` variable appears automatically
and must be set before launch.
→ [Flip for Sell Order functionality](../reference/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) ·
→ [Order stack with Flip for Sell](../reference/adl-overview/advanced-concepts/description/order-stack-logic-with-flip-for-sell-functionality.md)

## Organisation and reuse

| Goal | Construction |
|---|---|
| Declutter the canvas | [Group blocks](../reference/group-blocks/group-blocks-overview.md) |
| Remove long edges | [Jump blocks](../reference/jump-blocks/jump-blocks-overview.md) (cannot cross virtual boundaries) |
| Reuse logic across algos | [Library blocks](../reference/library-blocks/library-blocks-overview.md) — **rename before saving** |
| Navigate a large algo | Bookmarks; search `@blockname` or `.bookmark` in the Blocks panel |
| Document intent | [Note blocks](../reference/miscellaneous-blocks/note-block.md) |
| Surface live values to the trader | right-click an output port → **Export value** → [Exporting block outputs](../reference/adl-overview/advanced-concepts/task/exporting-block-outputs.md) |

## Testing

| Goal | How |
|---|---|
| Run in the canvas | Play/pause/stop in the toolbar; blocks display live values |
| Vary inputs while running | **Variables** tab of the Information Panel (does not alter block defaults) |
| Test an OMA without a manual order | [Funnel](../reference/discrete-blocks/funnel-block.md) + a switchable "test order" branch feeding the Single Order Container → [Testing OMA logic](../reference/adl-overview/advanced-concepts/task/testing-oma-logic.md) |
| Find design errors | **Problems** tab of the Information Panel |
| Full walkthrough | [Building your first algo](../reference/adl-overview/building-your-first-algo/introduction.md) → [entry logic](../reference/adl-overview/building-your-first-algo/lessons/building-the-entry-logic.md) → [testing](../reference/adl-overview/building-your-first-algo/lessons/testing-the-entry-logic.md) → [fills data](../reference/adl-overview/building-your-first-algo/lessons/capturing-fills-data.md) → [exit order](../reference/adl-overview/building-your-first-algo/lessons/creating-the-exit-order.md) |

> Time and Sales behaves differently in live vs simulation because of message coalescing. Analytics
> blocks do not work in UAT or Production-Delayed at all.

---

## Standard sub-assemblies

**Price N ticks from the market**
```
Field(Bid Price) ─┐
                  ├─ Add ── Round(inc = MinPriceIncrement) ── price
Number(N) ── Multiply ──┘
        Field(Min Price Increment) ──┘
```
Enable Flip for Sell on the Field and Add blocks to make it bi-directional. Always Round to a valid tick.

**Average open price from fills**
```
Order.fills ── MsgInfoExtractor ┬─ fillQuantity ── ValueAccumulator ── cumQty
                                └─ fillPrice ×fillQty ── ValueAccumulator ── notional
                                          notional / cumQty = avg open price
```

**Gate an order on a condition**
```
condition ── (And / Once True / IsNumber) ── Order.on/off
```
`on/off` FALSE deletes the working order; TRUE re-adds it.

**Per-fill independent exit**
```
Order.fills ── [ VIRTUALIZED GROUP: MsgInfoExtractor → exit price calc → Discrete Order → SOC → Exit block ]
```
The Exit block is not optional at scale — undisposed instances degrade latency.

**Deterministic multi-branch handling**
```
Order.fills ── Sequence ┬─#1─ logging / alert
                        ├─#2─ position update
                        └─#3─ exit order submission
```
