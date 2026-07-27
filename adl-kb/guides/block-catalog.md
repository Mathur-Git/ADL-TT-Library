# ADL Block Catalog

Every block ADL provides, with ports, purpose, and the gotcha that most often bites.
Sorted by category. `→` marks the linked reference page.

[KB Home](../README.md) · [Core Semantics](core-semantics.md) · [Formulas](formula-reference.md) · [Patterns](design-patterns.md) · [Gotchas](gotchas-and-limits.md) · [Full Index](../INDEX.md)

## Port type legend

ADL has five port types; **edges may only connect ports of the same type**.

| Type | Colour | Carries |
|---|---|---|
| Numeric | light/dark red | integer or decimal |
| True/False (Boolean) | green | TRUE / FALSE |
| Instrument | blue | instrument + its market data |
| Variable | yellow | *becomes* numeric/bool/instrument on first connection; all variable ports on that block convert together |
| Discrete event message | white/black | a pulse of event data (fill, add, change, delete, trade) |

An **input port accepts only one edge**; an **output port may fan out to many**. Circular
connections (a block's output back into its own input) are rejected.
→ [Blocks](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/blocks.md) ·
→ [Edges](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/edges.md)

---

## Trading blocks

Market access: instruments, market data, order submission, order management.
→ [Trading blocks overview](../reference/trading-blocks/trading-blocks-overview.md)

### Instrument → [ref](../reference/trading-blocks/instrument-block.md)
Identifies the instrument. Feeds `inst` ports on Order, Field, Market State, Time and Sales.

- **Out:** instrument
- **Type property:** `Static` · `User Defined` · **`Order Instrument`**
- Setting Type = **Order Instrument** is what makes the algo an [OTA](algo-types.md) (and is a
  prerequisite for an [SOA](algo-types.md)).
- A user-defined Instrument **cannot be changed while the algo is running** — it must be set before launch.

### Field → [ref](../reference/trading-blocks/field-block.md)
Retrieves one market-data field for a connected Instrument. The primary source of continuous data.

- **In:** instrument (+ `index` or `price` port depending on Lookup Type)
- **Out:** numeric (the field value)
- **Lookup Type:** `Best` (inside market) · `Index` (N levels deep, **max 20**) · `Price` (at a specific price)
- Supports [Flip for Sell](#flip-for-sell-order) on the bid/ask, high/low, and direct-bid/ask pairs.
- **Field blocks are snapshots** — on fast markets they can miss an LTP/LTQ between snapshots. Use
  Time and Sales when you must see *every* trade.
- Index beyond available depth → `0` for quantity fields, `NaN` for price fields.
- ADL reports **unaccumulated** LTQ (TT Web shows accumulated).
  → [Accumulated vs unaccumulated LTQ](../reference/adl-overview/advanced-concepts/description/displaying-accumulated-or-unaccumulated-ltq.md)

Field names include: Ask/Bid Price, Ask/Bid Quantity, Ask/Bid Order Count, Ask/Bid Market Quantity,
Direct Ask/Bid Price & Quantity, Implied Ask/Bid Quantity, Open/High/Low/Close/Settle Price,
Last Trade Price, Last Trade Quantity, Volume, **Min Price Increment**, **Min Tick Increment**,
Round Lot Quantity, Workup Price, Settle Price Unit (B3), Working Days to Expiry (B3).

> Min Price Increment ≠ Min Tick Increment. ES outright ticks 25 but its spread ticks 5.

### Order → [ref](../reference/trading-blocks/order-block.md)
Submits **and continuously manages** an exchange order. The workhorse entry block.

- **In:** `inst`, `price`, `qty`, `on/off`, `disc qty` (iceberg), `trigger` (stop) — which ports appear
  depends on the **Type** property
- **Out:** `wrk qty` (continuous) · `Add Req`, `Add OK`, `Chg Req`, `Chg OK`, `Del Req`, `Del OK`, `fills` (discrete)
- **Type:** Limit · Market · Iceberg · StopLimit · StopMarket
- Key properties: **`Ignore Inputs After Add`** (makes it one-shot), **`AutoResubmit`**,
  `When Ext Mod Occurs` (Ignore/StopManaging/Detach), `Leave Child Order On`, `Submit in Suspended State`,
  `Autospreader`, `Order Tag`, `Order Color`, TIF (Day/GTC/IOC/FOK)
- Live input tracking (when `Ignore Inputs After Add` is off): price/qty change → **modify**;
  instrument change → **delete + add**; `on/off` FALSE → **delete**, back to TRUE → **add**.
- `wrk qty` for Stop orders outputs **0 until triggered**.
- Manual user modification/deletion → the block **relinquishes control** (ignores left-side inputs) but
  still emits right-side discrete messages.
- With **Autospreader** enabled the outputs change: adds `Hedge Add OK`, `Quote Fills`, `Hedge Fills`.

### Discrete Order → [ref](../reference/trading-blocks/discrete-order-block.md)
Fires a **one-shot** order every time a discrete message arrives. Does **not** manage the order afterward.

- **In:** discrete message (`msg`)
- **Out:** `Add OK` (discrete)
- Price/qty/condition come from **formulas**, not input ports — see [Formula reference](formula-reference.md).
- Will not resubmit if its order is deleted; *will* delete the order on pause/stop.
- Pair its `Add OK` with a [Single Order Container](#single-order-container) if you need management.
- `Clone incoming order` lets an OMA be launched from MD Trader.
- This is the block to use inside a [Loop](#loop) when each iteration must actually place an order.

### Single Order Container (SOC) → [ref](../reference/trading-blocks/single-order-container-block.md)
Takes over and manages **exactly one** order handed to it via a discrete message carrying an order key.

- **In:** discrete message (the order key), `price`, `qty`, `del`, optionally `trigger` / `disc qty`
- **Out:** `wrk qty`, `cum qty`, `msgs` (discrete)
- Accepts **only** these sources: Order `Add OK`, Order `Hedge Add OK`, Discrete Order `Add OK`,
  Existing Order `Add OK`.
- **It never creates orders** — it only modifies/deletes. `del` TRUE deletes; returning to FALSE does not resubmit.
- Can add a disclosed qty to an order that had none; **cannot** add a stop trigger to an order created without one.
- Only one order at a time — a new inbound order message forces it to forfeit the current one.
- Feed its `msgs` into a [Demultiplexer](#demultiplexer) to split add/change/delete/fill handling.

### Existing Order → [ref](../reference/trading-blocks/existing-order-block.md)
Lets an algo attach to an order that already exists — this is what makes an algo an **OMA**.

- **Out:** discrete message containing the order key → feed to a Single Order Container
- Attaching **does not lose queue priority**. An OMA can be applied to another OMA's child order.
- Applied from the Order Book widget after deploy.

### Market State → [ref](../reference/trading-blocks/market-state-block.md)
Boolean: "is this instrument's market currently in state X?" (Open, Closed, Halted, …)

- **In:** instrument · **Out:** Boolean
- **You must enable the algo's `Ignore market state` setting for this block to be useful** — otherwise the
  algo auto-pauses whenever a market isn't in session, which is exactly the case you were testing for.

### Time and Sales → [ref](../reference/trading-blocks/time-and-sales-block.md)
Emits a discrete message on **every** trade — no snapshot gaps.

- **In:** instrument · **Out:** discrete message
- Carries: `tradePrice`, `tradeQuantity`, `tradeIsHit`, `tradeIsTake`, `tradeIsUnknown`, `tradeIsOTC`,
  `tradeIsImplied`, `tradeIsLeg`, instrument, and full timestamp fields.
- Use with MsgInfoExtractor / Value Extractor / Value Bucket / Moving Average / Discrete Min-Max /
  Branch / State / Value Accumulator / Discrete Order.
- Live vs simulation can differ because of message coalescing.

### Price → [ref](../reference/trading-blocks/price-block.md)
Like a Number block, but validated and displayed in the instrument's native price format (e.g. `150'20`).

- **In:** instrument · **Out:** numeric price
- Variable Type: `Static` · `User Defined` · `Order Price`

---

## Discrete blocks

Act on discrete events; each can read fields out of the message.
→ [Discrete blocks overview](../reference/discrete-blocks/discrete-blocks-overview.md)

### MsgInfoExtractor → [ref](../reference/discrete-blocks/msginfoextractor-block.md)
Splits selected fields out of a message into continuous output ports; passes the message through unchanged.
This is how you read `fillPrice` / `fillQuantity` / `tradePrice` etc. into ordinary numeric wiring.

Selectable connectors include `limitPrice`, `orderQuantity`, `workingQuantity`, `fillPrice`,
`fillQuantity`, `cumQuantity`, `disclosedQuantity`, `deletedQuantity`, `tradeQuantity`, `tradePrice`,
`tradeIsHit/Take/Unknown/OTC/Implied/Leg`, `stopTrigger`, `isBuy`, `isQuotingOrder`, `isHedgeOrder`,
`isExternalEvent`, `isTriggered`, `isSuspended`, `instrument`, `account`, `orderType`, `timeInForce`,
`userField1..4`, and full date/time parts.

> Ports only produce meaningful values if that field is actually present in the inbound message.

### Value Extractor → [ref](../reference/discrete-blocks/value-extractor-block.md)
**Snapshot.** On each message, freezes a formula's value and holds it until the next message.

- **Out:** variable-typed value + the pass-through message
- The canonical way to capture "the market as it was at the moment of the fill".
- Trick: formula = `1` turns it into a latch/toggle indicating "this event has happened" (outputs 0 before).

### Value Accumulator → [ref](../reference/discrete-blocks/value-accumulator-block.md)
**Running total.** Adds a formula's value to a running sum on each message; `reset` port zeroes it.

- Formula = `{fillQuantity}` → cumulative filled qty. Formula = `1` → an **event counter**.
- **Terminates** the discrete pathway (see [Core Semantics](core-semantics.md)).

### Value Injector → [ref](../reference/discrete-blocks/value-injector-block.md)
Writes values **into** message fields (including `userField1..4`) and forwards the modified message.
The counterpart to Value Extractor — use it to carry data along a discrete pathway, notably **out of a
virtualized block**.

### Value Bucket → [ref](../reference/discrete-blocks/value-bucket-block.md)
A key→value hash table driven by formulas.

- **In:** `store` (discrete), `lookup` (numeric key), `reset` · **Out:** `val`, pass-through message
- **Mode** resolves duplicate keys: `Sum` · `Average` · `Last`
- Classic uses: volume-at-price ladders, per-second volume buckets, OHLC storage.

### Generator → [ref](../reference/discrete-blocks/generator-block.md)
Manufactures **empty** discrete messages — the algo's clock and trigger source.

Modes: `TimeInterval` (`enabled`, `repeating`, `periodMs`; **min 100 ms**) · `BoolChange` · `BoolTrue` ·
`EveryStart` (every launch *and* resume) · `InitialStart` (once) · `AtStartTime` (UTC time, and optionally
date; **repeats daily if no date given**) · `AtStartTime-Combined` (calendar widget; also outputs UTC epoch ms) ·
`UserTrigger` (button in Autotrader; requires deploy to test).

> Timing: on `InitialStart`/`EveryStart`/`BoolChange`/`BoolTrue`, **actor blocks act first**, then the
> generator fires. Do not assume your generator pulse precedes the first order.

### State → [ref](../reference/discrete-blocks/state-block.md)
Routes an inbound message to the **first** output port whose Boolean formula is TRUE (top-most wins).

- Default 2 outputs, extensible. Does not re-evaluate until the next message arrives.
- **Does not queue messages** — one message in, at most one message out.
- **Terminates** the pathway.
- Contrast with Branch: State *waits* for a formula to be true; Branch routes *immediately*.

### Branch → [ref](../reference/discrete-blocks/branch-block.md)
Immediate two-way router: formula TRUE → `yes` port, else `no` port. Formula must be Boolean.

### Funnel → [ref](../reference/discrete-blocks/funnel-block.md)
Merges several discrete pathways into one. Needed because a discrete input accepts only one edge.
Messages always pass **one at a time**, never simultaneously.

### Demultiplexer → [ref](../reference/discrete-blocks/demultiplexer-block.md)
Splits a Single Order Container's `msgs` stream by message type into
`Add Requested` / `Added` / `Change Requested` / `Changed` / `Delete Requested` / `Deleted` / `Filled`.

> **Only** a Single Order Container can feed it.

### Sequence → [ref](../reference/discrete-blocks/sequence-block.md)
Emits copies of the inbound message through `#1`, then `#2`, then `#3` — **waiting for each downstream
pathway to fully complete** before the next. The tool for deterministic ordering.
→ [Correctly sequencing discrete events](../reference/adl-overview/advanced-concepts/task/correctly-sequencing-discrete-events.md)

### Discrete Min / Discrete Max → [ref](../reference/discrete-blocks/discrete-min-max-blocks.md)
Maintains an internal collection; on each message adds the formula's value and outputs the running
min/max. `reset` clears the collection and returns `NaN`.

### Moving Average → [ref](../reference/discrete-blocks/moving-average-block.md)
Rolling average of a formula's value over the last `#bars` messages.

- **In:** `intervals` (discrete), `#bars`, `reset` · **Out:** `avg`, `ready`, pass-through `msg`
- **`ready` is FALSE until `#bars` samples have been collected** — gate your logic on it or you will trade
  on a half-formed average.
- Drive `intervals` from a Generator (time-based) or Time and Sales (trade-based).

---

## Basic blocks

### Number → [ref](../reference/basic-blocks/number-block.md)
Constant / user-input numeric value.
Variable Type: `Static` · `User Defined` · `Order Quantity` · `Order Price` ·
`User Defined (TIF)` · `User Defined (Order Type)`.

- **`Order Quantity` is required for an [SOA](algo-types.md)** (algo terminates when it reaches 0).
- TIF codes: 1 Day · 2 GTC · 3 At the opening · 4 IOC · 5 FOK · 6 Good till crossing · 7 GTDate ·
  8 At the close · 9 Good through crossing · 10 At crossing · 13 Auction · 14 Good in session ·
  15 Day plus · 16 GTC plus · 17 GTDate plus
- Order Type codes: 1 Market · 2 Limit · 3 Stop · 4 Stop limit · 5 Iceberg · 20 Market w/ leftover as limit ·
  21 Market limit market w/ leftover as limit · 30 Stop market to limit · 31 If-touched market ·
  32 If-touched limit · 33 If-touched market to limit · 37 Limit post-only

### Bool → [ref](../reference/basic-blocks/bool-block.md)
TRUE/FALSE constant or user switch; the standard on/off gate.
Variable Type: `Static` · `UserDefined` · `OrderSide`.

---

## Arithmetic blocks

| Block | Behaviour | Notes |
|---|---|---|
| [Add](../reference/arithmetic-blocks/add-block.md) | `in1 + in2` | supports [Flip for Sell](#flip-for-sell-order) → becomes subtract; **input order matters** |
| [Subtract](../reference/arithmetic-blocks/subtract-block.md) | `in1 - in2` | supports Flip for Sell → becomes add |
| [Multiply](../reference/arithmetic-blocks/multiply-block.md) | `in1 * in2` | typical use: `ticks * MinPriceIncrement` |
| [Divide](../reference/arithmetic-blocks/divide-block.md) | `in1 / in2` | `0/0` → `-nan`; `n/0` → ±infinity. **Both invalid as ADL inputs** |
| [Mod](../reference/arithmetic-blocks/mod-block.md) | remainder | divide by zero → `NaN` |
| [Round](../reference/arithmetic-blocks/round-block.md) | rounds `num` to `inc` | Mode: `Normal` · `Always Down` · `Always Up`. **Essential for snapping prices to tick** |
| [Average](../reference/arithmetic-blocks/average-block.md) | mean of connected inputs | divides by count of *used* ports only |
| [Math](../reference/arithmetic-blocks/math-block.md) | one of ~27 functions | Abs, Sqrt, Pow, Log, Floor, Ceiling, **Min, Max**, Sign, Truncate, trig… ports change per function |
| [Formula](../reference/arithmetic-blocks/formula-block.md) | arbitrary expression | outputs bool/numeric/instrument; **referencing a connector creates an implicit connection** and recalculation trigger |

---

## Logic blocks

| Block | Behaviour | Notes |
|---|---|---|
| [Greater Than / ≥](../reference/logic-blocks/greater-than-blocks.md) | numeric compare | supports Flip for Sell → flips to Less Than |
| [Less Than / ≤](../reference/logic-blocks/less-than-blocks.md) | numeric compare | supports Flip for Sell |
| [Equal](../reference/logic-blocks/equal-block.md) | equality | yellow **variable** ports; type locks to the first thing you connect |
| [And / Or / Not](../reference/logic-blocks/and-or-and-not-blocks.md) | Boolean logic | — |
| [If Then](../reference/logic-blocks/if-then-block.md) | `if` bool → ThenValue else ElseValue | variable ports; **nest right-to-left** to read nested If-Thens |
| [Once True](../reference/logic-blocks/once-true-block.md) | latches TRUE forever | one-way latch for the life of the algo |
| [IsNumber](../reference/logic-blocks/isnumber-block.md) | FALSE if input is `NaN` | **the standard NaN guard — see below** |

> **NaN discipline.** A `NaN` fed to a smart trading block means *no new order*; and if it reaches a block
> managing a working order, **the order is deleted**. Guard division and depth lookups with IsNumber.

---

## Miscellaneous blocks

### Analytics → [ref](../reference/miscellaneous-blocks/analytics-block.md)
Server-side OHLCV bars plus technical indicators. The heavyweight of the block set.

- **In:** `instrument`, `interval`, `index` · **Out:** `open`, `close`, `high`, `low`, `volume`, `start`,
  `onBarChange` — each also available as `*_i` for the indexed historical bar
- Interval: Time **1–1440 min**, or Volume **50–999,999**
- **Max 250 bars stored; max 5 Analytics blocks per algo**
- **Only works in Production-Live and Production-Simulation** — *not* Production-Delayed, *not* UAT
- Indicators: ATR, Bollinger Bands, MACD, SMA, EMA, DEMA, TEMA, WMA, RSI, Standard Deviation,
  Stochastic Oscillator. All period parameters accept **2–250**.
- Array loads with historical data at algo start; index 1 = most recent completed bar.

### Stopwatch → [ref](../reference/miscellaneous-blocks/stopwatch-block.md)
Delays a discrete message by a formula-computed number of ms.

- **Minimum 25 ms.** Negative computes as 0.
- **Each new inbound message restarts the timer** — it is a debounce, not a queue.
- **Terminates** the pathway.
- If a timer elapses during algo-server recovery, the algo goes to **Failed**.

### Loop → [ref](../reference/miscellaneous-blocks/loop-block.md)
Emits N empty messages in sequence.

- **In:** `enter` (discrete), `times` · **Out:** `index` (numeric, updated *before* each message), `loop`, `Exit`
- **Actor blocks cannot act during a loop.** An Order block downstream of the loop only acts once, with
  the final values. To place an order per iteration, drive a **Discrete Order** block from the `loop` port.

### Terminal → [ref](../reference/miscellaneous-blocks/terminal-block.md)
Pauses or stops the algo on a TRUE Boolean or an inbound message. Resume is manual. **Terminates** the pathway.

### Pnl → [ref](../reference/miscellaneous-blocks/pnl-block.md)
Per-instance P&L limit. Input is the **positive** maximum loss; algo auto-pauses when breached.
Outputs current `pnl` continuously plus an empty discrete message on each update.

### Position Risk → [ref](../reference/miscellaneous-blocks/position-risk-block.md)
Pre-trade position check performed **before** the TT risk system; failing it **stops the algo**.

- **Side** = long or short; supports Flip for Sell. Buy-only and sell-only blocks leave the other side to
  TT risk. Use both blocks to cover both sides.
- Set limits **below** the user's real TT risk limits, or TT risk rejects first.
- **`Enable Position Reserve`** pre-reserves risk at launch and lets subsequent orders bypass the TT risk
  system — a significant latency win, but **dedicated Algo Servers only** (not gen-pool).

### Alert → [ref](../reference/miscellaneous-blocks/alert-block.md)
Audit Trail message and/or sound on a TRUE Boolean or inbound message.
Formula supports string literals and `+` concatenation but **not the IF operator**. `Frequency` throttles
repeat Boolean alerts. **Terminates** the pathway. In canvas simulation it writes to the Alerts tab, not
the real Audit Trail. Only the launching user hears the sound.

### Random Number → [ref](../reference/miscellaneous-blocks/random-number-block.md)
Random value between `min` and `max` on each message; passes the message through.
Used for order-quantity and delay randomisation.

### Note → [ref](../reference/miscellaneous-blocks/note-block.md)
Canvas documentation only. No effect on logic or speed.

---

## Structural blocks

### Group → [ref](../reference/group-blocks/group-blocks-overview.md)
Collapses any selection into one block. Ports can be added from outside (right-click) or inside
(right-click canvas). Supports Boolean / Numeric / Instrument / Discrete connectors.
`Collapsed` display saves space but **blocks new connections while collapsed**.
→ [Creating](../reference/group-blocks/creating-a-group-block.md) ·
→ [Adding ports](../reference/group-blocks/adding-inputs-and-outputs-to-a-group-block.md)

### Virtualized (a Group with `Virtual = True`) → [ref](../reference/virtualized-blocks/virtualized-blocks-overview.md)
Spawns an **independent copy** each time a discrete message enters. The answer to "each fill needs its own
exit order that doesn't get clobbered by the next fill".

Rules → [ref](../reference/virtualized-blocks/rules-of-virtualization.md):
- **Must** have a discrete message input.
- **May not have any continuous output ports** — discrete outputs only.
- Data leaves only inside a discrete message, and only order-event or Time-and-Sales information.
  Ordinary continuous values (e.g. Bid Price) inside the block are unreachable from outside.
  Use a **Value Injector** into `userField1..4` to smuggle arbitrary values out.
- Jump blocks **cannot cross a virtual boundary** (they may cross group boundaries).
- Exported values are **not supported** inside virtualized blocks.
- The canvas will not reliably display live values inside a virtualized block.

**Exit block** (right-click inside a virtualized group → *add exit block*) disposes of an instance.
Without it, instances accumulate in memory and progressively slow the algo.
→ [Advanced Exit Block Functionality](../reference/adl-overview/advanced-concepts/description/advanced-exit-block-functionality.md)

### Library → [ref](../reference/library-blocks/library-blocks-overview.md)
A saved Group block, reusable across algos. **Rename before saving** — the default name (`Group0`) is
permanent once saved.
→ [Creating](../reference/library-blocks/creating-a-library-block.md) ·
→ [Using](../reference/library-blocks/using-library-blocks-in-an-algo.md)

### Jump → [ref](../reference/jump-blocks/jump-blocks-overview.md)
Anchor (green, on an output) + one or more destinations (pink, feeding an input) replace a long edge.
Works for continuous and discrete. **Cannot cross virtual block boundaries.**
Deleting the green anchor deletes every pink destination. TT recommends using these liberally.

---

## Flip for Sell Order

One algo, both directions. Blocks with **Flip for Sell Order** enabled invert their behaviour based on the
**Order Side** variable the user sets at launch.
→ [Flip for Sell Order functionality](../reference/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md)

Supporting blocks: **Add ↔ Subtract**, **Greater Than ↔ Less Than**, **Order**, **Discrete Order**,
**Position Risk**, and **Field** on these pairs — Bid/Ask Price, Bid/Ask Qty, High/Low,
Direct Bid/Ask Qty, Bid/Ask Order Count, Direct Bid/Ask Price.

Rules:
- **Always design the buy side first**, then enable flipping on the pivot blocks.
- Order Side must be set **before launch** and cannot change afterwards.
- Set it via the Designer toolbar dropdown, the Algo Dashboard Variables tab, or — for OTAs — by clicking
  the bid (Buy) or ask (Sell) column in MD Trader.
- **Input order matters** on Add/Subtract, because flipping reverses the operation.
