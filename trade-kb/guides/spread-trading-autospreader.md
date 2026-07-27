# Spread Trading: AutoSpreader, Aggregator, Hedge Manager

"How does TT build a synthetic spread market, and where does its tick size actually come from?"
Every claim below links to the TT reference page that supports it.

[KB Home](../README.md) · [Full Index](../INDEX.md) · [Order Types & Execution](order-types-and-execution.md) · [Market Data & Depth](market-data-and-depth.md) · [Algo Ops](algo-ops.md) · [Order Management & Risk](order-management-and-risk.md)

---

## What AutoSpreader is

AutoSpreader® builds a **synthetic spread instrument** out of two or more outright legs, runs it on a
colocated Autospreader Server, and quotes/hedges the legs to realize a target spread price. It is TT's native
answer to "I want to trade the difference (or ratio) between two markets as one instrument."
→ [Introduction to Autospreader](../reference/spread-trading/autospreader/description-autospreader/introduction-to-autospreader.md) ·
[Autospreader Configuration Interface](../reference/spread-trading/autospreader/description-autospreader/autospreader-configuration-interface.md)

**Synthetic spread ≠ exchange-listed spread.** A CFE VX calendar spread that trades natively on the exchange
order book (viewed via the **Exchange Listed** tab of Spread Matrix) is a *different object* from an
AutoSpreader synthetic spread built out of the two VX outright legs. The exchange sets the exchange-listed
spread's tick size directly; AutoSpreader *computes* a synthetic spread's tick size from the legs (see below).
Don't assume AutoSpreader's tick-sizing rules explain an exchange-listed spread's tick — they explain what
happens if you rebuild that same spread synthetically.
→ [Spread Matrix overview](../reference/viewing-market-data/spread-matrix/description-spread-matrix/spread-matrix-overview.md) ·
[Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md) ·
[Market data for inter-product spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-inter-product-spreads.md)

---

## Spread definition & formulas

| Field | What it does | Reference |
|---|---|---|
| Spread Formula | Selects the pricing model: **Price Differential** (A−B), **Ratio** (A/B), **Net change (in ticks)** (each leg's change from prior settle), **Custom** (formula editor, no exponents), or **TT Splicer** (drives a Sub-strategy — TT Brisk/Close/TWAP+/VWAP+) | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) |
| Contract selection | Any exchange instrument, or an **Aggregator** instrument as a leg (Aggregator's synthetic book is treated like a native instrument) | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) · [Creating spreads with aggregated instruments](../reference/spread-trading/autospreader/use-cases/creating-spreads-with-aggregated-instruments.md) |
| Ratio | Quantity of each leg relative to the others (negative = short leg). **Does not affect the spread price** — only how many contracts trade per spread unit. | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) |
| Multiplier | Weights each leg's *price* in the formula: `Spread_Price = (LegA_Price × LegA_Multiplier) − (LegB_Price × LegB_Multiplier)`. Can be a whole number, decimal, or fraction — fractional form (e.g. `0.333333` → `1/3`) optimizes ticking accuracy. | [Autospreader Reference](../reference/spread-trading/autospreader/reference-autospreader/autospreader-reference.md) |
| Pricing-only leg | Uncheck **Active Quoting** *and* **Enable Hedging** on a leg to include its price in the formula without quoting or hedging it (no position limits needed for that leg) | [Using instruments as pricing components of a spread](../reference/spread-trading/autospreader/use-cases/using-instruments-as-pricing-components-of-a-spread.md) |
| Custom formula editor | Free-form arithmetic (`+ - / *`) over leg identifiers with intellisense; used for cross-currency spreads (e.g. converting one leg's price into the other leg's currency) | [Autospreader Custom Spread Formulas](../reference/spread-trading/autospreader/videos-autospreader/autospreader-custom-spread-formulas.md) |

Ratio and Multiplier are independent knobs: Ratio sizes the hedge, Multiplier prices it. A basis trade with a
5000-ounce silver future against spot XAG/USD sets **Ratio = 5000** (contract size) on the spot leg but
**Multiplier = 1.0** (same sign magnitude, opposite sign) on both legs, because both instruments already quote
in the same units (USD/oz).
→ [Basis Trading Metals and FX](../reference/spread-trading/autospreader/use-cases/basis-trading-metals-and-fx.md)

Common pre-built spread configurations (Crush, Crack, calendar-roll spreads on the Treasury curve) show how
Ratio/Multiplier/tick-size settings combine in practice:

| Spread | Formula | Legs (Ratio) | Tick Size |
|---|---|---|---|
| Crush (ZS/ZM/ZL) | Price Differential | -10.0 / 11.0 / 9.0 | 1/100 |
| CRACK (CL/RB/HO) | Price Differential | -3.0 / 2.0 / 1.0 | 1/100 |
| ES/YM Ratio | Ratio | 5.0 / -6.0 | default |
| TUT (ZT/ZN) | Net Change | 2.0 / -1.0 | 1/8 |
| NOB (ZN/ZB) | Net Change | 3.0 / -1.0 | 1/2 |

→ full parameter tables: [Configuring Common Spreads](../reference/spread-trading/autospreader/use-cases/configuring-common-spreads.md)

---

## Tick size and the synthetic spread

This is the mechanic most directly analogous to the outright/spread tick-granularity question (CFE VX
outright at 0.05, calendar spread at 0.01 — a 5× finer grid). AutoSpreader exposes the same relationship as
three linked fields:

| Field | Meaning | Reference |
|---|---|---|
| **Min Tick Increment** | The exchange-defined minimum increment for *each leg's own instrument* (e.g. one leg may tick in 64ths, another in 32nds) | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) |
| **Calculated Tick Size** (a.k.a. Tick Size) | TT-derived minimum tradeable increment of the *synthetic spread*, computed from the legs' Min Tick Increments and Multipliers. If the legs tick at different increments, this field shows the resulting minimum tick size for the spread. | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) · [Autospreader Reference](../reference/spread-trading/autospreader/reference-autospreader/autospreader-reference.md) |
| **Delta** | The effect on the spread price of a **one-tick move in an outright leg** — this is the field that answers "how many spread ticks does one outright tick move correspond to?" | [Spread Configuration](../reference/spread-trading/autospreader/description-autospreader/spread-configuration.md) |
| **Override Tick Size** | Lets you manually override the Calculated Tick Size, previewed live in the Spread Preview ladder. Framed by TT as a way to *widen* the tick (view a greater price range without losing quantity visibility) rather than to force a finer one. | [Spread Configuration Spread Review](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-spread-review.md) · [Autospreader Reference](../reference/spread-trading/autospreader/reference-autospreader/autospreader-reference.md) |

**Worked example — same 5× structure as VX outright/spread.** A silver basis spread (cash spot XAG/USD vs. the
SI future) has a future that ticks at **5/1000** and a spot instrument that ticks at **1/1000** — a 5:1 ratio
between the coarser and finer leg, structurally identical to VX's 0.05 outright vs. 0.01 spread. The resulting
synthetic spread ticks at **1/1000**: TT resolves the Calculated Tick Size to the *finer* of the two
scaled increments, not their average or the coarser leg's grain.
→ [Basis Trading Metals and FX](../reference/spread-trading/autospreader/use-cases/basis-trading-metals-and-fx.md)

**Decimal ratios.** For hedge ratios that aren't whole numbers (e.g. matching a DV01-weighted Treasury hedge),
AutoSpreader supports decimal Ratio values so the accumulated position tracks the true hedge ratio more
precisely than rounding to whole contracts would allow.
→ [Autospreader Decimal Ratios](../reference/spread-trading/autospreader/videos-autospreader/autospreader-decimal-ratios.md)

**Fill-quantity math is bounds-based, not simple division.** Because legs can carry fractional ratios,
AutoSpreader computes parent fill quantity from a per-leg `lowerBound`/`upperBound` range and takes
`execQty = min(max(lowerBound), min(upperBound))` across all legs — for a leg with ratio < 1,
`lowerBound = filledQty / ratio` and `upperBound = filledQty + 1 − ratio`; for ratio > 1 the bounds collapse to
the exact value. → [Autospreader Orders — Parent Order Fill Quantity Calculation](../reference/spread-trading/autospreader/description-autospreader/autospreader-orders.md)

The Aggregator widget computes tick size the same way for combining venues that tick differently — see
[Aggregator](#aggregator) below.

---

## Quoting and hedging

| Goal | Mechanism | Reference |
|---|---|---|
| Choose which leg(s) post the resting quote | **Active Quoting** per leg (max 5 legs at spread creation; more can be enabled by amending afterward). At least one leg must be actively quoted. | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) |
| Size how deep to walk the other leg's book before quoting | **Minimum Lean Quantity** — a constant, a formula (e.g. `ThisLeg.DisclosedRemainingQuantity + 10`), or `1` to lean only on the inside market | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) |
| Hold queue position while requoting | **Queue Holder** — trailing duplicate orders at consecutive price levels behind the primary quote (up to 5 legs, 20 levels); adds a **QH** button in MD Trader | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) · [Submitting a queue holder order](../reference/spread-trading/autospreader/task-autospreader/submitting-an-queue-holder-order.md) |
| Reuse a filled quote order as the hedge itself | **Convert Quote to Hedge** — three modes trading off latency vs. overfill risk vs. queue position (*Attempt*, *Always Use*, *Always Preserve Queue Position*) | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) |
| Work the hedge away from the touch instead of crossing it | **Payup Ticks** — number of ticks the hedge order is priced away from the best bid/offer instead of hitting/lifting it | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) |
| Include a leg without ever hedging it | Uncheck **Active Quoting** and **Enable Hedging** together → pricing-only leg | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) |
| Split a spread order into disclosed clips | **Reload** — Disclosed Qty, Max Exposure (clips), Offset, Delay (ms); adds an **RLD** button in MD Trader | [Spread Configuration Order Execution](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-order-execution.md) · [Submitting a reload order](../reference/spread-trading/autospreader/task-autospreader/submitting-a-reload-order.md) · [Autospreader Reload](../reference/spread-trading/autospreader/videos-autospreader/autospreader-reload.md) |
| Execute without quoting any leg | **Sniper** — waits for the full spread price/liquidity to appear, then fires hedge orders on all legs simultaneously (Active Quoting is ignored; Pre-/Post-Hedge rules still apply) | [Submitting a sniper order](../reference/spread-trading/autospreader/task-autospreader/submitting-a-sniper-order.md) |

**Pre-trade risk and legging.** Every potential outright order across every leg — quote and hedge — is
risk-checked before any order reaches the market; if any leg would fail, the whole spread order is rejected and
nothing is sent. If any leg's contract closes while a spread is working, AutoSpreader pulls all quoting orders
(to avoid getting legged); working hedge orders are left resting in a legged state if they exist.
→ [Autospreader Orders](../reference/spread-trading/autospreader/description-autospreader/autospreader-orders.md)

**GTC behavior across session boundaries** — quote and hedge orders are both submitted GTC; AutoSpreader leaves
them alone across a closed session and resumes managing them at reopen (including Pre-Open), except that a
leaning leg's quote is canceled/resubmitted around that leg's own close if legs have different session times.
→ [Autospreader Orders](../reference/spread-trading/autospreader/description-autospreader/autospreader-orders.md)

---

## AutoSpreader Rules — custom quoting/hedging logic

AutoSpreader Rules override or extend the default Autospreader Server logic at three points in the order
lifecycle: **before a quoting order** is added/changed, **before a hedge order** is sent, and **after a hedge
order** is working (managing it). Rules are ranked by their position in the spread's Rules list — top has
highest priority. → [Autospreader rules overview](../reference/spread-trading/autospreader/description-autospreader/autospreader-rules-overview.md) ·
[Spread Configuration Rules](../reference/spread-trading/autospreader/description-autospreader/spread-configuration-rules.md)

### Rule anatomy

| Piece | Detail | Reference |
|---|---|---|
| Rule type | **Quoting Order**, **Pre-Hedge Order**, or **Post-Hedge Order** — one per rule | [Autospreader rules configuration](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration.md) |
| Condition type | **ThisLeg** (only the evaluated leg must pass), **ANY legs**, **ALL legs**, or **Always execute** | [Autospreader rules configuration Logic](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-logic.md) |
| Leg identifiers | `ThisLeg` (the leg being evaluated), `Leg` (the leg being iterated), `Leg#` (an absolute leg reference, unvalidated) | [Autospreader rules configuration Logic](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-logic.md) |
| Bid/ask auto-reversal | Build the rule for the buy side only, wrap the expression in `{ }`; Autospreader Rules auto-flips `+`/`-` and `<`/`>`/`≤`/`≥` when evaluating from the sell side | [Autospreader rules configuration Logic](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-logic.md) |
| Custom variables | Declared per rule, then referenced in Condition/Action logic; values are set at **application time** when the rule is added to a spread | [Autospreader rules configuration Custom Variable](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-custom-variable.md) |
| Actions | Quote: override **price**/**quantity** of this leg. Pre-Hedge: override hedge **price**/**quantity**/**order type**, or **Forfeit** the hedge (with "submitted but legged" vs "submitted and filled" bookkeeping). Post-Hedge: override working hedge **price**/**quantity**. | [Autospreader rules configuration Actions](../reference/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-actions.md) |

This buy-side-only-then-mirror pattern is the same idea as ADL's **Flip for Sell Order** on Add/Subtract and
comparison blocks — build one direction, let the platform derive the other.
→ [Flip for Sell Order functionality](../../adl-kb/reference/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) ·
[Design Patterns — Bi-directional algos](../../adl-kb/guides/design-patterns.md#bi-directional-algos)

### Leg attributes worth knowing for tick/price logic

| Attribute | Use |
|---|---|
| `MinimumPriceIncrement` | The leg's own tick size, available inside rule conditions/actions |
| `BidPriceAtIndex(#)` / `AskPriceAtIndex(#)` | Depth N ticks from the touch, ignoring depth gaps |
| `Delta` (pre-hedge only) | How many contracts a leg is off from perfectly hedged vs. another leg, recalculated continuously |
| `LeanPrice` / `MinimumLeanQuantity` | Cached lean price, and the only leg attribute that's user-controlled rather than server-calculated |
| `CalculatedQuoteOrderPrice` / `CalculatedHedgeOrderPrice` | The server's pre-rule price, for rules that adjust rather than replace it |

→ full attribute list: [Autospreader Rules reference](../reference/spread-trading/autospreader-rules/reference-autospreader-rules/autospreader-rules-reference.md)

### TT's built-in rules most relevant to thin/one-tick-wide markets

| Rule | Behavior | Type |
|---|---|---|
| (TT) Basic Slop | Defines an acceptable spread price band so Autospreader doesn't requote the outright legs on every tick within it | Pre-Quote |
| (TT) Liquidity Based Backoff Tick / Payup Tick | Backs off a hedge tick when the target price has heavy size; pays up a tick when opposing size at one-tick-away thins out — designed as a pair | Pre-Hedge / Post-Hedge |
| (TT) Inside Smart Quote (with LIMIT) | Suppresses requoting toward the market unless the new price is close enough to the inside; LIMIT variant adds a resume threshold | Pre-Quote |
| (TT) Quote Throttle | Rate-limits requoting via separate inside/outside millisecond throttles | Pre-Quote |
| (TT) Max Order Move | Caps how far a single requote can jump; pulls the order until price re-enters range | Pre-Quote |
| (TT) Hedge Price Limit | Caps how far through the opposite inside market a hedge can be sent — built for unequal-multiplier spreads that could otherwise blow through exchange price bands | Pre-Hedge |
| (TT) Ticks Away Based Go To Market | Crosses the market if a legged hedge order drifts too far from the opposite inside market | Post-Hedge |

→ full catalog with variables: [Autospreader Rules reference](../reference/spread-trading/autospreader-rules/reference-autospreader-rules/autospreader-rules-reference.md)

---

## Aggregator

Aggregator combines multiple contracts (different venues, accounts, or brokers) into one tradeable synthetic
instrument with smart order routing, distinct from AutoSpreader's spread-pricing focus.
→ [Aggregator Overview](../reference/spread-trading/aggregator/description-aggregator/aggregator-overview.md)

| Goal | Mechanism | Reference |
|---|---|---|
| Route an aggressive (crossing) order to the best price | **Taking** mode — always the best-priced exchange first; split across venues by **Rank Ratio**, **Split Ratio**, or **Size Ratio** if the best price is tied | [Aggregator Reference](../reference/spread-trading/aggregator/reference-aggregator/aggregator-reference.md) |
| Route a passive (joining) order | **Joining** mode — **Split Ratio** or **EPIQ** (Estimated Position in Queue)-weighted allocation | [Aggregator Reference](../reference/spread-trading/aggregator/reference-aggregator/aggregator-reference.md) |
| Shift resting quantity toward a leg that suddenly has liquidity | **Rebalance** (with a millisecond timer between cycles) | [Aggregator Reference](../reference/spread-trading/aggregator/reference-aggregator/aggregator-reference.md) |
| Combine legs that tick differently | Same pattern as AutoSpreader: **Min Tick Increment** per leg, a computed common tick size, with an **Override** option | [Aggregator Reference](../reference/spread-trading/aggregator/reference-aggregator/aggregator-reference.md) |
| Use an aggregated instrument as a spread leg | Select it like any native contract in AutoSpreader's leg picker | [Creating spreads with aggregated instruments](../reference/spread-trading/autospreader/use-cases/creating-spreads-with-aggregated-instruments.md) |

Aggregator orders and fills route through the normal Order Book / Fills / Audit Trail widgets, filterable by
the **Exch** column. → [Aggregator order management](../reference/spread-trading/aggregator/description-aggregator/aggregator-order-management.md)

---

## Hedge Manager

Hedge Manager is a single grid of every working AutoSpreader hedge order across all spreads, with quick manual
overrides and OMA attachment.
→ [Hedge Manager overview](../reference/spread-trading/hedge-manager/description-hedge-manager/hedge-manager-overview.md)

| Goal | Mechanism | Reference |
|---|---|---|
| Improve fill odds with minimal impact | **Payup** button — one tick toward the market | [Paying up one tick](../reference/spread-trading/hedge-manager/task-hedge-manager/paying-up-one-tick.md) |
| Fill immediately | **Cross Inside** — reprices to the opposite inside market; remainder rests if liquidity is short | [Crossing the inside market](../reference/spread-trading/hedge-manager/task-hedge-manager/crossing-the-inside-market.md) |
| Guarantee a full fill | **Fill w/ Limit** — prices through enough depth to sweep the full working quantity | [Hedge Manager reference](../reference/spread-trading/hedge-manager/reference-hedge-manager/hedge-manager-reference.md) |
| Declutter the grid | **Clear** — removes filled/deleted rows (shown in italics until cleared) | [Clearing filled and deleted hedge orders](../reference/spread-trading/hedge-manager/task-hedge-manager/clearing-filled-and-deleted-hedge-orders.md) |
| Hand a stuck hedge to custom logic | Launch an ADL-built **OMA** against a working hedge order | [Support for Order Management Algos (OMAs)](../reference/spread-trading/hedge-manager/description-hedge-manager/support-for-order-management-algos-omas.md) |

**Precedence**: if a spread has a Post-Hedge rule, that rule keeps running against manual or OMA changes to the
hedge order and takes priority over an attached OMA — the OMA stops managing the order the moment the rule
modifies it. → [Hedge Manager overview](../reference/spread-trading/hedge-manager/description-hedge-manager/hedge-manager-overview.md)

An ADL OMA attached here is a plain [Single Order Container](../../adl-kb/reference/trading-blocks/single-order-container-block.md)
consumer managing someone else's order — the same "manage an existing order" pattern as any other OMA target.
→ [Order block vs Discrete Order vs Single Order Container](../../adl-kb/guides/core-semantics.md#9-order-block-vs-discrete-order-block-vs-single-order-container)

---

## Trading in Yield

The Yield widget lets you configure and trade US Treasury Bond/futures products in yield terms rather than
price; yield configurations created in Autospreader or MD Trader also surface here, and can be imported/exported
as JSON. Off-thesis for tick-granularity work, but relevant if a leg of a spread needs a yield display.
→ [Yield Widget Overview](../reference/spread-trading/trading-in-yield/description-trading-in-yield/yield-widget-overview.md) ·
[Yield type calculations](../reference/spread-trading/trading-in-yield/use-cases-trading-in-yield/yield-type-calculations.md)

---

## Cross-references

| Question | Where |
|---|---|
| Where does an *exchange-listed* calendar spread's own tick size come from (not a synthetic rebuild)? | [Spread Matrix — market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md), and the [Market Data & Depth](market-data-and-depth.md) guide |
| How do TT Iceberg/TWAP/Timed order types behave when routed through an Autospreader parent order? | [Autospreader Orders — supported order types](../reference/spread-trading/autospreader/description-autospreader/autospreader-orders.md), [Using TT TWAP to drive TT Autospreader instruments](../reference/basic-order-entry/tt-order-types/case-studies/using-tt-twap-to-drive-tt-autospreader-instruments.md) |
| How would an ADL algo read fill/price data per fill independently, the way a Pre-Hedge rule reads `TriggeringFillPrice`? | [Virtualization](../../adl-kb/reference/adl-overview/advanced-concepts/description/virtualization.md) |
| Where are ADL's Instrument/Field/Order blocks documented, for building the equivalent logic in an ADL algo instead of an Autospreader Rule? | [Instrument block](../../adl-kb/reference/trading-blocks/instrument-block.md) · [Field block](../../adl-kb/reference/trading-blocks/field-block.md) · [Order block](../../adl-kb/reference/trading-blocks/order-block.md) |
