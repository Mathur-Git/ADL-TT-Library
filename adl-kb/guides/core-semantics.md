# Core Semantics — How an ADL Algo Actually Executes

The execution model. Most ADL bugs are not wiring mistakes; they are misunderstandings of the rules
on this page.

[KB Home](../README.md) · [Block Catalog](block-catalog.md) · [Formulas](formula-reference.md) · [Patterns](design-patterns.md) · [Gotchas](gotchas-and-limits.md) · [Full Index](../INDEX.md)

---

## 1. Two kinds of message

→ [Continuous vs discrete event messages](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages.md)

**Continuous messages** are the always-on stream: bid quantity, last trade price, working quantity.
They enter through blocks like [Field](../reference/trading-blocks/field-block.md) and flow over
Numeric / Boolean / Instrument / Variable ports. Downstream blocks recompute whenever an input changes.

**Discrete event messages** are pulses at a single instant. The exchange-driven ones are:

- Fill confirmation
- Order add request / confirmation
- Order modify request / confirmation
- Order delete request / confirmation

Plus trade events from [Time and Sales](../reference/trading-blocks/time-and-sales-block.md), and
**empty** messages manufactured by [Generator](../reference/discrete-blocks/generator-block.md) and
[Loop](../reference/miscellaneous-blocks/loop-block.md) purely to trigger downstream action.

The distinction is not cosmetic — it decides which blocks you may use and whether your data is a live
value or a frozen one.

---

## 2. The freeze rule

> **While a discrete message propagates, the algo stops channelling continuous data from the exchange.**

→ [Message timing](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/message-timing.md)

Sequence of events:

1. A block emits a discrete pulse.
2. All continuous channels close. Every Field block's output **freezes** at its current value.
3. The pulse traverses its pathway, updating the blocks it passes through.
4. Propagation completes; continuous channels reopen.

This is *the* reason ADL can answer "what was the best ask **at the instant** my order filled?" — and it
is why a [Value Extractor](../reference/discrete-blocks/value-extractor-block.md) on a fill message
captures a coherent snapshot rather than a smeared one.

Propagation takes microseconds and is imperceptible in practice.

---

## 3. Propagation order within a pathway

→ [Order of discrete event message propagation](../reference/adl-overview/advanced-concepts/description/order-of-discrete-event-message-propagation.md)

For a **pass-through block** (any block that forwards the message unchanged), the order is:

1. The pass-through block's own **continuous outputs update first**.
2. Every downstream block consuming those continuous outputs updates.
3. **Only then** does the discrete message exit the block.
4. The message continues along the pathway until it terminates.

So the continuous side-effects of a block are fully settled before the message moves on. Design around
this rather than against it.

### Termination blocks

A discrete message travels as far as it can and **stops** on entering any of:

| Terminator |
|---|
| [Single Order Container](../reference/trading-blocks/single-order-container-block.md) |
| [State](../reference/discrete-blocks/state-block.md) |
| [Value Accumulator](../reference/discrete-blocks/value-accumulator-block.md) |
| [Discrete Order](../reference/trading-blocks/discrete-order-block.md) |
| [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) |
| [Terminal](../reference/miscellaneous-blocks/terminal-block.md) |
| [Alert](../reference/miscellaneous-blocks/alert-block.md) |
| any **`reset`** input port |
| a pass-through block with no discrete edge beyond it |

If you expected logic to run after one of these, it will not. Re-emit deliberately (e.g. Discrete Order's
`Add OK`, Stopwatch's output) or restructure with a [Sequence](../reference/discrete-blocks/sequence-block.md).

---

## 4. Branching a discrete output is non-deterministic

→ [Correctly sequencing discrete events](../reference/adl-overview/advanced-concepts/task/correctly-sequencing-discrete-events.md)

You *may* connect one discrete output port to several downstream inputs. **You should not.** The Algo
Server does not guarantee which branch runs first, and where the branches converge (e.g. into a shared
Value Extractor) the result differs by execution order.

**Fix:** insert a [Sequence](../reference/discrete-blocks/sequence-block.md) block immediately after the
discrete output and wire the branches to `#1`, `#2`, `#3` in the order you require. Sequence waits for
each downstream pathway to complete before firing the next.

Treat "one discrete output → one edge, or a Sequence block" as a design rule.

---

## 5. Actor blocks act before generators fire

→ [Generator block](../reference/discrete-blocks/generator-block.md)

An **actor block** is any block that can take a real action — principally the order blocks.

On `InitialStart` / `EveryStart`:
1. Actor blocks perform their actions.
2. *Then* the Generator emits its message.

On `BoolChange` / `BoolTrue`:
1. The continuous update propagates **fully** through the algo first.
2. Actor blocks act.
3. *Then* the Generator emits.

Consequence: you cannot use a Generator to set something up "before" the first order goes out. If order
submission must be gated, gate it with the Order block's `on/off` input, not with generator timing.

---

## 6. The Loop block suspends actors

→ [Loop block](../reference/miscellaneous-blocks/loop-block.md)

Inside a loop, **no actor block may act**. An [Order](../reference/trading-blocks/order-block.md) block
downstream of a Loop does not emit one order per iteration — it acts once, after the loop finishes,
using only the final values.

To place an order per iteration, drive a
[Discrete Order](../reference/trading-blocks/discrete-order-block.md) block from the Loop's **`loop`**
port. The outbound discrete message pauses the loop until that downstream action completes, then the
loop advances. Note `index` updates **before** each message is emitted.

This is the standard order-stack / scale-order construction.

---

## 7. Virtualization

→ [Virtualization](../reference/adl-overview/advanced-concepts/description/virtualization.md) ·
→ [Rules](../reference/virtualized-blocks/rules-of-virtualization.md)

**The problem it solves:** a single copy of exit logic can only manage one order. Take a market-maker
whose entry fills 1 lot at 1313.75 and offers it out at 1314.25. The market moves, 2 more fill at
1314.00, and the exit logic — which tracks *total* fill count and *most recent* fill price — reprices all
3 to 1314.50, **deleting the good 1314.25 offer**. Each fill needed its own independent exit.

**The mechanism:** group the exit logic, set `Virtual = True`, and route a discrete pathway (the fill
message) into it. Every message that enters spawns a fresh, independent instance.

**The constraints:**

- Must have a discrete input; instances exist only because a discrete event created them.
- **No continuous output ports.** Discrete outputs only.
- Information escapes only *inside* a discrete message, and only order-event or Time-and-Sales data.
  A Bid Price computed inside the block is invisible outside it.
  → to export an arbitrary value, inject it into `userField1..4` with a
  [Value Injector](../reference/discrete-blocks/value-injector-block.md) and read it outside with a
  [Value Extractor](../reference/discrete-blocks/value-extractor-block.md).
- [Jump blocks](../reference/jump-blocks/jump-blocks-overview.md) cannot cross the boundary.
- [Exported values](../reference/adl-overview/advanced-concepts/description/export-block-output-values.md)
  are unsupported inside.
- The Designer canvas will not reliably show live values inside a virtualized block — multiple instances
  exist at once.

**Instance lifecycle** → [Advanced Exit Block Functionality](../reference/adl-overview/advanced-concepts/description/advanced-exit-block-functionality.md)

On creation: blocks are created → continuous inputs populate → the triggering message flows through →
actor blocks execute.

Instances **persist in memory until explicitly disposed**. Add an **Exit block** inside the virtualized
group and drive it (Boolean or discrete) when the instance's work is done. Thousands of undisposed
instances measurably degrade algo latency, because every instance is updated on every tick.

Exit via *continuous* Boolean: exit is scheduled → other continuous values still update → any resulting
actor actions still occur → then the instance is disposed. Exit via *discrete* input: the whole pathway
completes (including everything downstream of the Exit block) → resulting actions occur → then disposal.

---

## 8. NaN is contagious and destructive

`NaN` (Not A Number) is an **invalid input** in ADL, and it is produced routinely:

- `0 / 0` → `-nan`; `n / 0` → ±infinity ([Divide](../reference/arithmetic-blocks/divide-block.md))
- modulo by zero ([Mod](../reference/arithmetic-blocks/mod-block.md))
- a [Field](../reference/trading-blocks/field-block.md) price lookup beyond available depth, or a
  negative index
- a reset [Moving Average](../reference/discrete-blocks/moving-average-block.md) or
  [Discrete Min/Max](../reference/discrete-blocks/discrete-min-max-blocks.md)

Consequences at a smart trading block:

- Feeding `NaN` as price or qty → **no new order is created**.
- Instructing a block to modify a *working* order to a `NaN` price or qty → **the order is deleted**.

Guard with [IsNumber](../reference/logic-blocks/isnumber-block.md) — typically IsNumber → `on/off`, or
IsNumber into an [If Then](../reference/logic-blocks/if-then-block.md) that substitutes a safe fallback.

---

## 9. Order block vs Discrete Order block vs Single Order Container

The single most consequential design choice in an ADL algo.

| | [Order](../reference/trading-blocks/order-block.md) | [Discrete Order](../reference/trading-blocks/discrete-order-block.md) | [Single Order Container](../reference/trading-blocks/single-order-container-block.md) |
|---|---|---|---|
| Creates orders | yes | yes (one per message) | **never** |
| Manages after submit | yes, continuously | no | yes |
| Driven by | continuous inputs | a discrete message | a discrete message carrying an order key |
| Price/qty from | input ports | **formulas** | input ports |
| Resubmits if deleted | only with `AutoResubmit` | no | no |
| Use for | a single managed working order | stacks, slices, per-event one-shots | taking over an order created elsewhere |

Common compositions:

- **Managed single order:** Order block alone.
- **One-shot per event:** Discrete Order alone.
- **Stack / scale:** Loop `loop` port → Discrete Order (× N).
- **Per-fill independent exits:** fill message → *virtualized* group containing exit logic.
- **Manage what you just created:** Discrete Order `Add OK` → Single Order Container.
- **Manage a pre-existing order (OMA):** [Existing Order](../reference/trading-blocks/existing-order-block.md)
  → Single Order Container.
- **Fine-grained order-event handling:** Single Order Container `msgs` →
  [Demultiplexer](../reference/discrete-blocks/demultiplexer-block.md).

### Losing control of an order

If a user manually modifies or deletes an algo-managed order, the block **relinquishes control**: it
ignores its left-side inputs but keeps emitting right-side discrete messages. On pause/resume the block
tries to re-locate and re-take its order; if it cannot, the Order block submits a new order for
`OrderQty − FillQty`.

The `When Ext Mod Occurs` property chooses the policy explicitly:
`Ignore` (keep using block inputs) · `Stop Managing` (accept the external change) · `Detach` (stop inputs
*and* outputs).
→ [Handling external events](../reference/adl-overview/advanced-concepts/task/handling-external-events.md)

---

## 10. What pauses or cancels an algo

→ [Leave orders on cancel or pause](../reference/adl-overview/advanced-concepts/description/leave-orders-on-cancel-or-pause.md)

| Event | Result |
|---|---|
| A market reported by an Instrument block closes | **pause** — unless `Ignore market state` is enabled |
| A trading block tries to submit at an invalid price | pause |
| [Pnl](../reference/miscellaneous-blocks/pnl-block.md) loss limit breached | pause |
| [Terminal](../reference/miscellaneous-blocks/terminal-block.md) block triggered | pause or stop (per Mode) |
| [Position Risk](../reference/miscellaneous-blocks/position-risk-block.md) check fails | **algo stopped** |
| TT risk system rejects an order | algo stopped |
| Dashboard **Pause** / **Cancel** | pause / cancel |
| Client disconnect | configurable per-instance: continue, pause, or cancel |

Every smart trading block has **`Leave Child Order On`** to decide whether its child orders survive a
pause or cancel.

> `Ignore market state` is off by default. Any algo intended to run pre-open, or that uses a
> [Market State](../reference/trading-blocks/market-state-block.md) block, must turn it on — otherwise the
> algo pauses in exactly the conditions it was written to handle.

---

## 11. Recovery and server maintenance

→ [Recovery and server maintenance](../reference/adl-overview/advanced-concepts/description/recovery-and-server-maintenance.md)

- Simulation Algo Servers restart **weekdays at 16:15 Chicago**. Production may restart on maintenance weekends.
- Algos are restored to their prior state — **except** any algo containing an Order block driving
  **Autospreader / Aggregator** orders, where **recovery fails**.
- Algos firing periodic non-exchange discrete events (Generator timers) may come back inaccurate or fail.
  **Stop these before weekend maintenance.**
- A [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) whose timer has already elapsed when
  recovery starts puts the algo into **Failed**.

---

## 12. Do not design around assumed latency

TT states this repeatedly across the documentation: the platform is continuously optimised, so
**sequencing logic that depends on a specific system latency will eventually break**. Express ordering
with a [Sequence](../reference/discrete-blocks/sequence-block.md) block or explicit discrete pathways —
never with a [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) delay chosen to "let the
other branch finish first".

Relatedly, the X_TRADER **Clock block does not exist** in TT ADL; TT advises against reconstructing it,
citing serious algo performance degradation.
→ [Time and timers in TT ADL](../reference/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl.md)
