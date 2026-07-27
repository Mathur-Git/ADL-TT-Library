# Gotchas, Hard Limits & Platform Constraints

Every numeric limit and non-obvious behaviour stated in the ADL documentation, in one place.
Check this before committing to a design.

[KB Home](../README.md) · [Block Catalog](block-catalog.md) · [Core Semantics](core-semantics.md) · [Formulas](formula-reference.md) · [Patterns](design-patterns.md) · [Full Index](../INDEX.md)

---

## Hard numeric limits

| Limit | Value | Source |
|---|---|---|
| Analytics blocks per algo | **5** | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) |
| Analytics bars stored | **250** max | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) |
| Analytics time interval | **1–1440** minutes | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) |
| Analytics volume interval | **50–999,999** | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) |
| Indicator period parameters | **2–250** | [Analytics](../reference/miscellaneous-blocks/analytics-block.md) |
| Field block `Index` lookup depth | **max 20** | [Field](../reference/trading-blocks/field-block.md) |
| Generator `TimeInterval` minimum | **100 ms** | [Generator](../reference/discrete-blocks/generator-block.md) |
| Stopwatch minimum timer | **25 ms** | [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) |
| Formula Editor connectors shown per block | **100** | [Formula Editor](../reference/adl-overview/advanced-concepts/description/formula-editor.md) |
| `userField` slots per message | **4** | [Formula Editor](../reference/adl-overview/advanced-concepts/description/formula-editor.md) |

### Algo Server capacity

→ [Algo server limits](../reference/adl-overview/introduction-to-adl/reference-introduction-to-adl/algo-server-limits.md)

**Production, simultaneous instances (ADL algos / TT order types):**

| Facility | Guaranteed | Up to (load-dependent) |
|---|---|---|
| Aurora | 100 / 100 | 400 / 400 |
| Bangkok | 100 / 100 | 100 / 100 |
| All other co-los | 100 / 100 | 200 / 200 |

**Test environments (UAT and Simulation):**

- **200 order messages per second per algo instance** (new + change + cancel). Exceeding it
  **stops the algo automatically** and writes to the Audit Trail.
- **25 ADL algo instances and 25 TT order type instances per region** (may be higher under light load).

Neither set of limits applies to dedicated Algo Servers on TT Reserved instances.

---

## Environment restrictions

| Constraint | Detail |
|---|---|
| [Analytics block](../reference/miscellaneous-blocks/analytics-block.md) | **Production-Live and Production-Simulation only.** Does **not** work in Production-Delayed or UAT |
| Position Reserve orders | **Dedicated Algo Servers only** — not available on gen-pool servers |
| [Time and Sales](../reference/trading-blocks/time-and-sales-block.md) | logic can behave differently live vs simulation because of message coalescing |
| Time and Sales in the canvas | you must **start** the algo to see any time and sales data |
| [TT Mobile](../reference/adl-overview/advanced-concepts/description/adl-and-tt-mobile.md) | cannot **launch** algos; can only view running instances |
| Autospreader / Aggregator algos | **recovery after a server restart fails** |

---

## Behaviours that surprise people

### Execution model

- **Fanning out a discrete output is non-deterministic.** Which branch runs first is not guaranteed, and
  convergent results differ accordingly. Use a [Sequence](../reference/discrete-blocks/sequence-block.md) block.
- **Actor blocks act before Generators fire** on `InitialStart`/`EveryStart`/`BoolChange`/`BoolTrue`.
- **Actor blocks cannot act inside a [Loop](../reference/miscellaneous-blocks/loop-block.md).** An Order
  block after a Loop acts once, with the final values. Use a Discrete Order off the `loop` port.
- **Continuous data freezes** for the duration of discrete propagation — that is the feature, not a bug.
- Messages **terminate** at SOC, State, Value Accumulator, Discrete Order, Stopwatch, Terminal, Alert, and
  any `reset` port. → [Core Semantics §3](core-semantics.md#3-propagation-order-within-a-pathway)
- **Do not encode sequencing as a latency assumption.** TT optimises the platform continuously; such
  designs break. There is deliberately no Clock block in TT ADL.

### Orders

- `on/off` going TRUE→FALSE **deletes** the working order; FALSE→TRUE **adds a new one**.
- **`Ignore Inputs After Add`** converts the Order block into a one-shot. Without it, every input change
  modifies the live order — instrument change deletes and re-adds.
- **`AutoResubmit`** resubmits `OrderQty − FillQty` when the order is deleted. Without it the Order block
  gets exactly one order for the algo's life.
- A **manual** modify/delete makes the block relinquish control — left-side inputs ignored, right-side
  outputs still fire. Behaviour is governed by `When Ext Mod Occurs`.
- On pause/resume a block re-locates its order; failing that, the Order block submits the remaining balance.
- `wrk qty` is **0 for stop orders until triggered**.
- A [Single Order Container](../reference/trading-blocks/single-order-container-block.md) **never creates
  orders**, holds **one at a time**, and forfeits the current order if a new one arrives.
- An SOC can **add** a disclosed quantity to an order, but **cannot add a stop trigger** to an order that
  did not have one.
- Stop orders: for BUY the trigger must be **above** last traded price and `price >= trigger`; for SELL,
  **below** and `price <= trigger`.
- Selecting an order Type the exchange does not support natively → **rejected**.
- Iceberg: if disclosed qty > order qty, the exchange treats order qty as the total.

### Data

- **Field blocks are snapshots** and can miss trades. Use Time and Sales for every trade.
- ADL reports **unaccumulated** LTQ; TT Web shows accumulated.
- `Index` lookups skip price levels where the attribute is zero.
- Index beyond available depth or negative → `0` for quantities, **`NaN` for prices**.
- **Min Price Increment ≠ Min Tick Increment** (ES outright 25, ES spread 5).
- Some fields (Ask/Bid Order Count) return **0 on exchanges that don't support them** — indistinguishable
  from an empty market.
- `Settle Price Unit` and `Working Days to Expiry` are **B3 only**.
- Message fields irrelevant to the message read as **zero**, not null.

### NaN

- `0/0` → `-nan`; `n/0` → ±infinity; `mod 0` → `NaN`. All invalid as ADL inputs.
- `NaN` into a smart trading block → **no order created**.
- `NaN` price/qty on a **working** order → **the order is deleted**.
- Guard with [IsNumber](../reference/logic-blocks/isnumber-block.md).

### Virtualization

- Must have a discrete input; **must not** have continuous outputs.
- Only order-event and Time-and-Sales data escapes, inside a message. Use `userField1..4` for anything else.
- **Jump blocks cannot cross a virtual boundary** (group boundaries are fine).
- Exported values are unsupported inside a virtualized block.
- The canvas will not reliably show values inside virtualized blocks.
- **Instances persist until an Exit block disposes them.** Thousands of live instances measurably degrade
  latency — every instance updates on every tick.

### Blocks

- **[Market State](../reference/trading-blocks/market-state-block.md) is useless unless `Ignore market
  state` is enabled** — otherwise the algo auto-pauses in exactly the situations the block detects.
- [Moving Average](../reference/discrete-blocks/moving-average-block.md) `ready` is FALSE until `#bars`
  samples exist. Gate on it.
- [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) **restarts on every inbound message** —
  it debounces rather than queues.
- A Stopwatch timer that elapses during algo-server recovery puts the algo in **Failed**.
- [State](../reference/discrete-blocks/state-block.md) **does not queue** messages; top-most TRUE formula
  wins; it does not re-evaluate until the next message.
- [Demultiplexer](../reference/discrete-blocks/demultiplexer-block.md) accepts input **only** from an SOC.
- [Alert](../reference/miscellaneous-blocks/alert-block.md) does **not support `IF`**; in canvas simulation
  it writes to the Alerts tab, not the real Audit Trail; only the launching user hears the sound.
  The page is marked *"STILL IN DEVELOPMENT"*.
- [Add](../reference/arithmetic-blocks/add-block.md)/[Subtract](../reference/arithmetic-blocks/subtract-block.md)
  with Flip for Sell: **input order matters**, because flipping reverses the operation.
- [Equal](../reference/logic-blocks/equal-block.md) and [If Then](../reference/logic-blocks/if-then-block.md)
  lock their variable-port type to the first connection made.
- Nested If-Then blocks read **right to left**.
- A [Library block](../reference/library-blocks/creating-a-library-block.md) saved without renaming keeps
  `Group0` **permanently**.
- A **collapsed** Group block cannot accept new connections.
- Deleting a green anchor [Jump block](../reference/jump-blocks/deleting-jump-blocks.md) deletes all its
  pink destinations.
- A [Funnel](../reference/discrete-blocks/funnel-block.md) never passes two messages simultaneously, even
  if two instruments trade at the same instant.

### Wiring

- An **input accepts one edge**; an output may fan out to many.
- Connections are allowed only between **matching port types**.
- **Circular references are rejected** — a block's output cannot feed its own input.
- Yellow **variable** ports convert together, as a set, on the first connection.

### Users, launch, deployment

- A user-defined **Instrument cannot change while the algo runs** — set it before launch.
- **Order Side must be set before launch** and cannot change afterwards.
- Changing values in the **Variables** tab during testing does **not** change block defaults.
- Algos must be **deployed** to appear in Trade widgets; undeploying removes them everywhere.
- If your firm requires approval, algos need per-company approval before Live use. Enabling approval
  *after* deployment **removes already-deployed algos** until re-approved.
- `UserTrigger` Generators **require deployment** to test — the button lives in Autotrader.
- Sharing requires the recipient's **email address**; a duplicate email across companies defaults to the
  first company it was registered under.
- Shared algos needing approval require **Read** permission for that user.

### OTA / SOA

- An **OTA** produces fills only for **child** orders, not the parent.
- An **SOA** generates fills for the parent **and** children, always shows the parent on the ladder, and
  **auto-terminates when its `Order Quantity` Number block reaches 0**.
- SOA requires Instrument Type = `Order Instrument` **and** a Number block with Variable Type =
  `Order Quantity`.
- Enabling the SOA setting force-enables `Show algo order on ladder` (and it cannot be turned off).
- An OTA parent shows order qty and working qty as **0** on the ladder.
- If an SOA delays its first child order, the parent's working qty stays 0 until that order is submitted.

→ [Algo types](algo-types.md)

---

## Pre-flight checklist

Before deploying:

- [ ] Every division and depth-lookup guarded against `NaN`
- [ ] No discrete output fanned out without a [Sequence](../reference/discrete-blocks/sequence-block.md) block
- [ ] `Ignore market state` set correctly for the intended session behaviour
- [ ] Moving Average consumers gated on `ready`
- [ ] Virtualized groups have an **Exit block** and no continuous outputs
- [ ] `Leave Child Order On` reviewed for every trading block
- [ ] `When Ext Mod Occurs` chosen deliberately
- [ ] Prices [Round](../reference/arithmetic-blocks/round-block.md)ed to `Min Price Increment`
- [ ] [Pnl](../reference/miscellaneous-blocks/pnl-block.md) and/or
      [Position Risk](../reference/miscellaneous-blocks/position-risk-block.md) limits set **below** the
      user's TT risk limits
- [ ] Flip for Sell designed **from the buy side**, pivot blocks verified, input order checked on Add/Subtract
- [ ] Analytics usage within 5 blocks / 250 bars, and the target environment supports it
- [ ] Message rate comfortably under 200/sec if testing in UAT or Simulation
- [ ] Timer-driven algos stopped before weekend maintenance
- [ ] **Problems** tab clean
