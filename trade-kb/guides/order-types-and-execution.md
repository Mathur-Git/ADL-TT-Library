# Order Types & Execution

"What does this order type actually do, and how do I get the same behavior out of ADL?"
Every claim links to the TT page that supports it.

[Trade KB Home](../Trade-KB-Home.md) · [Spread Trading / Autospreader](spread-trading-autospreader.md) ·
[Order Management & Risk](order-management-and-risk.md) · [Algo Ops](algo-ops.md)

---

## The ADL bridge

ADL's [Order](../../adl-kb/reference/trading-blocks/order-block.md), [Discrete Order](../../adl-kb/reference/trading-blocks/discrete-order-block.md),
and [Single Order Container](../../adl-kb/reference/trading-blocks/single-order-container-block.md) blocks are thin
wrappers over the same order types, TIFs, and routing described on this page. Two gaps matter when moving between
"what the platform can do" and "what the block property dropdown shows":

| Platform surface | ADL surface | The gap |
|---|---|---|
| MD Trader/Order Ticket TIF selector — Day, GTC, IOC, FOK, GTDate, Day+, GTC+, plus exchange-specific (Auction, Good in session…) — see [Order Types](../reference/basic-order-entry/md-trader/description-md-trader/order-types-2.md) and [TIF selection](../reference/basic-order-entry/md-trader/description-md-trader/trading-with-md-trader.md#tif-selection) | Order/Discrete Order block **TIF property** dropdown = Day / GTC / IOC / FOK only (see the [Order block](../../adl-kb/reference/trading-blocks/order-block.md) and [Discrete Order block](../../adl-kb/reference/trading-blocks/discrete-order-block.md) property tables) | The property dropdown is the restricted path. Driving TIF from a **Number** block set to `User Defined (TIF)` reaches all 17 numeric codes (1 Day … 17 GTDate plus) — see the [Formula Reference TIF/order-type table](../../adl-kb/guides/formula-reference.md#formula-driven-order-parameters) |
| Native order type catalog — Market, Limit, Iceberg, Stop Market, Stop Limit, BOC, Post-Only, MLM, MinVol, LIT, MIT, MOO, MOC, FAK, Cross, Block (see [Order Types](../reference/basic-order-entry/md-trader/description-md-trader/order-types-2.md)) | Order block **Type property** = Limit / Market / Iceberg / StopLimit / StopMarket (5 values) | Formula-driven `orderType` codes reach 37 values including post-only (37) and if-touched market/limit variants (31–33). The Order block page itself warns: **selecting a type the exchange doesn't support natively gets the order rejected** |
| TT Order Type parent orders (TWAP, Iceberg, Time Sliced, With-a-Tick, Bracket, OCO, …) — synthetic parents running on a co-located Algo Server | Not a block. ADL rebuilds the same behavior from primitives (Loop + Discrete Order for slicing, OMA-style logic for With-a-Tick) | See the [Design Patterns](../../adl-kb/guides/design-patterns.md) recipes: [TT time sliced order](../../adl-kb/reference/adl-overview/advanced-concepts/task/creating-a-tt-time-sliced-order.md), [With-a-tick algo](../../adl-kb/reference/adl-overview/advanced-concepts/task/creating-a-with-a-tick-algo.md), [Iceberg with random qty/delay](../../adl-kb/reference/adl-overview/advanced-concepts/task/submit-iceberg-with-random-quantity-and-delay.md) |

The numeric TIF/order-type codes above are transcribed from
[adl-kb/guides/formula-reference.md](../../adl-kb/guides/formula-reference.md#formula-driven-order-parameters);
treat that page as the source of truth if the two ever drift.

---

## Native order types

These are managed directly by the exchange (subject to per-exchange support) and are the base vocabulary everything
else builds on. Full definitions: [Order Types](../reference/basic-order-entry/md-trader/description-md-trader/order-types-2.md).

| Type | Behavior |
|---|---|
| Market | Fills at the current best price(s); can partial-fill across multiple levels walking the book |
| Limit | Fixed price; unfilled remainder rests at that price |
| Iceberg | Large order broken into disclosed slices; next slice enters only after the current one **fully fills** |
| Stop Market | Trigger price → market order once touched/penetrated; can fill worse than trigger, across levels |
| Stop Limit | Trigger price → limit order; optional payup ticks set the fill-price range |
| Book or Cancel (BOC) | Rests like a limit order but deletes immediately if it would partial- or full-fill on entry |
| One Cancels Other (OCO) | Two same-qty orders at different prices, same side; a fill on one cancels the other |
| Minimum Volume (MinVol) | Requires a minimum qty fillable immediately at entry or the whole order is rejected; supported at B3, MX |
| Limit If Touched (LIT) | Trigger price → limit order at a set price; Buy LIT below LTP, Sell LIT above |
| Market If Touched (MIT) | Trigger price → market order; same side convention as LIT |
| Market On Open (MOO) | Market order for the opening auction; unfilled balance becomes a Day limit order |
| Market On Close (MOC) | Market order for the closing auction |
| Post Only (Limit) | Rejected outright if any part would take liquidity immediately (avoids taker fees) |
| FOK (Fill Or Kill) | Entire order fills immediately or the whole order cancels |
| FAK (Fill And Kill) | Fills what it can immediately (optionally requiring a minimum qty), cancels the rest |
| IOC (Immediate Or Cancel) | Fills what it can immediately, cancels the remainder |
| MLM (Market Limit Market) | Fills at best price; unfilled remainder becomes a resting limit order at that price |
| Cross | Prearranged trade with an internal or external counterparty — [Submitting a cross trade](../reference/basic-order-entry/order-ticket/task-order-ticket/submitting-a-cross-trade.md) |
| Block | High-volume prearranged OTC trade — see [Block trading](#block-trading) below |

TIF (order restriction) is orthogonal to order type — Day, GTC, IOC, FOK plus exchange-specific values, selected in
the same TIF dropdown described above.

---

## TT Order Type catalog (Standard license)

A TT Order Type is a **synthetic parent order** running on an Algo Server co-located with the exchange; it manages
native **child orders**. Overview and lifecycle: [TT Order Types Overview](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-order-types-overview.md).

Lifecycle facts worth keeping in mind:

- The parent defaults to **TIF=GTC**; the *child* order TIF is set separately at submission. If the child TIF isn't
  natively supported by the exchange, **the parent is rejected immediately** — not at first child submission.
- A synthetic parent fill message is generated for **every** native child fill (relevant if you're counting fills downstream).
- A future **Start** time shows as Order Book `Status=Working` / `SynthStatus=Waiting` until the start condition fires.
- If **End Time** is reached while the trading session is closed, the delete request fails and GTC child orders are
  left working on the exchange — deleting them is the user's responsibility.
- Held/paused TT Order Types have limited re-submission support: Bracket and OCO allow quantity changes only (price
  resumes at original); Iceberg allows quantity changes; If-Touched and Stop allow price *and* quantity changes; all
  other TT Order Types disallow changes to a held/paused order. See
  [Held and paused TT Order Type orders](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-order-types-overview.md#held-and-paused-tt-order-type-orders).

### Slicing family

TT Time Sliced / Time Duration / Volume Sliced / Volume Duration differ on exactly two axes: what triggers the next
slice, and whether you set the slice size or TT computes it.

| Order type | Slice trigger | You set → TT computes | Reference |
|---|---|---|---|
| [TT Time Sliced](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-sliced-order.md) | fixed time interval (min 10 ms) | interval + display qty → number of slices | |
| [TT Time Duration](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-duration-order.md) | total time budget | **Interval** slice type: interval+duration → disclosed qty; **Disclose** slice type: disclosed qty+duration → interval | |
| [TT Volume Sliced](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-sliced-order.md) | fixed traded-volume interval (exchange volume, not just LTQ) | interval + display qty → number of slices | |
| [TT Volume Duration](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-duration-order.md) | total traded-volume budget | same **Interval**/**Disclose** inversion as Time Duration | |

They all share the same child-order machinery, documented once on each page and repeated here rather than four
times: child order type Market/Limit with **Offset** (LTP/Ask/Bid/PrevSlice/Same Side/Opposite Side ticks), optional
**With a Tick** repricing (see [below](#with-a-tick)), **Variance** (± % randomization of slice qty, with a
distribution preview), a **Leftover action** for the unfilled remainder when the next slice is due (Leave / Payup at
End or Half Life / Go to Market at End or Half Life / Merge), and **Auto-Resubmit Upon GTD Expiry** for Day-TIF
children that expire at session close.

The behavioral discriminator against **TT Iceberg** (below): Iceberg enters the next child only once the current
child **fully fills**; the Sliced/Duration family enters on the clock (or volume tick) regardless of whether the
resting slice filled — the two children can overlap.

### Order type reference table

| TT Order Type | What it does | Reference |
|---|---|---|
| TT Bracket | Limit/Stop entry order; on any fill, launches a TT OCO (profit-target limit + protective stop) sized to the fill qty | [tt-bracket-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-bracket-order.md) |
| TT Iceberg | Large order sliced into disclosed child orders; next child enters only after the current one fully fills. Supports variable qty, price offset (incl. PrevSlice), With-a-Tick, Stop/If-Touched trigger to start, trailing trigger, start/end scheduling | [tt-iceberg-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-iceberg-order.md) |
| TT If-Touched | Triggers when market reaches/trades through a price **better** than current market (inverse of Stop); submits Market or Limit child with payup | [tt-if-touched-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-if-touched-order.md) |
| TT OCO | Two same-qty orders (Limit profit + Stop protective) on the same side; fill on one cancels/reduces the other. Trigger, trailing trigger, With-a-Tick child repricing all available | [tt-oco-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-oco-order.md) |
| TT Retry | Resubmits a rejected child order at a fixed interval up to N times; used to gain queue position pre-open | [tt-retry-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-retry-order.md) |
| TT Stop | Triggers when market reaches/penetrates a price **worse** than current market; ignores qty checks once triggered; FIFO processing at the same trigger price | [tt-stop-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-stop-order.md) |
| TT Time Duration | See [slicing family](#slicing-family) | [tt-time-duration-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-duration-order.md) |
| TT Time Sliced | See [slicing family](#slicing-family) | [tt-time-sliced-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-sliced-order.md) |
| TT Timed | Schedules a single order's start/end; can piggyback on any TT Order Type's Start/End fields | [tt-timed-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-timed-order.md) |
| TT Trailing Limit | Native limit order that trails the market by N ticks; moves only in the favorable direction, never reverses | [tt-trailing-limit-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-trailing-limit-order.md) |
| TT TWAP (Standard) | Slices into smaller orders at uniform time intervals to track average market price without signaling volume | [tt-time-weighted-average-price.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-weighted-average-price.md) |
| TT Volume Duration | See [slicing family](#slicing-family) | [tt-volume-duration-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-duration-order.md) |
| TT Volume Sliced | See [slicing family](#slicing-family) | [tt-volume-sliced-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-sliced-order.md) |
| TT With A Tick (WAT) | Limit order auto-repriced one tick toward the market when opposite-side qty (abs or %) drops below threshold at one tick away; can be layered onto child orders of most other TT Order Types (not Trailing Limit) | [tt-with-a-tick-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-with-a-tick-order.md) |
| TT Autohedger | On options fill, submits a Market order in the underlying sized to fill qty × delta (rounding: normal/up/down); requires Advanced Options Package | [tt-autohedger.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-autohedger.md) |
| TT OBV (Order by Volatility) | Options order entered/repriced continuously to hold a target implied volatility; requires Advanced Options Package | [tt-obv-order-by-volatility-order.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-obv-order-by-volatility-order.md) |
| TT Sniper (OTA) | Hides intent; submits a child Limit only when qty appears on the opposite side at your price, cancels/repeats until filled | [tt-sniper-ota.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-sniper-ota.md) |

<a id="with-a-tick"></a>

### Market-Making Algos (MMA)

All five share one parameter table (Bid/Ask Qty, Enable/Offset Cover Orders, Quote/Fill Throttle, Max Pos, Manual
Requote, Don't Cross Market, TIF, …) — see [Direct Entry](../reference/basic-order-entry/tt-order-types/description-tt-order-types/direct-entry-mma.md)
for the full property list, which the other four link back to. They differ only in what feeds the base quoting price:

| MMA variant | Base price | Reference |
|---|---|---|
| Direct Entry | Explicit **Bid Prc**/**Ask Prc** inputs | [direct-entry-mma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/direct-entry-mma.md) |
| Single Theo | One **Theo Price** ± Bid/Ask Offset ticks | [single-theo-mma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/single-theo-mma.md) |
| Bid/Ask Theo | Separate **Theo Bid**/**Theo Ask** ± offsets | [bid-ask-theo-mma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/bid-ask-theo-mma.md) |
| Market Base | Live inside market of the quoted instrument ± offsets | [market-base-mma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/market-base-mma.md) |
| Reference Base | Live inside market of a **Ref Instrument** (× multiplier) ± offsets | [reference-base-mma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/reference-base-mma.md) |

These are TT's shared Market-Making Algos and are themselves built in ADL — open one from ADL's **File → Open →
Shared Algos** to see the logic first-hand
([viewing/editing note](../reference/basic-order-entry/tt-order-types/description-tt-order-types/direct-entry-mma.md#viewing-and-editing-an-algo)).
`Cover Order Offset <= 0` combined with a fast requote can cause a fill/add loop — set **Fill Throttle** to let the
cover order reach the exchange before requoting.

### Order Management Algos (OMA) — applied to existing orders

OMAs adopt one or more **already-working** orders (exchange orders, TT Order Types, ADL Synthetic Order Algos, or
child orders of other algos) rather than being submitted as a new order type. None of them can adopt TT Order Type
*parent* orders, Autospreader parent orders, Aggregator parent orders, or OTC orders.

| OMA | What it does | Reference |
|---|---|---|
| OCO OMA | Applies one-cancels-other logic to 2+ already-adopted orders; optional cancel-on-market-state-change | [oco-oma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/oco-oma.md) |
| OCO 2 OMA | Same, restricted to exactly two orders; supports building new held orders directly in MD Trader before launch | [oco-2-oma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/oco-2-oma.md) |
| Conditional OMA | Primary order's fills increment the qty of a held conditional order, which then enters the market | [conditional-oma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/conditional-oma.md) |
| MinVol OMA | Cancels the adopted order if qty at its price drops below a threshold; resubmits when qty rebuilds, up to a max resubmit count | [minvol-oma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/minvol-oma.md) |
| With A Tick OMA | Applies WAT repricing to an adopted order from Order Book or Floating Order Book; canceling the WAT parent leaves the child order working | [with-a-tick-oma.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/with-a-tick-oma.md) |

### Order Ticket Algos (OTA) — TT Pro license

| OTA | What it does | Reference |
|---|---|---|
| BrackeTT | Simplified TT Bracket: Limit entry, then on each partial fill submits an OCO-style Limit + Stop Limit pair | [brackett-ota.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/brackett-ota.md) |
| TT Multi-Level Bracket | Limit entry; on fill, places OCO exits at up to four price levels by % allocation, single-side-only supported | [tt-multi-level-bracket-ota.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-multi-level-bracket-ota.md) |
| TT Sniper | See the [order type table](#order-type-reference-table) above | [tt-sniper-ota.md](../reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-sniper-ota.md) |

---

## TT Premium Order Types

Premium types require a dedicated FIX Order Gateway and are not available in Prod-SIM; access is granted per user/account
in Setup. Overview: [tt-premium-order-types-overview.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-premium-order-types-overview.md).
They share a common Order Details/Precondition Details parameter set (Order Type, Stop Price, Participation Rate,
**Aggression** 0–10, I Would Price/Qty/Qty%/Var%, Max Spread Cross Ticks, Start/End Time, If Touched Price, Post
Trigger Duration, End Time Override) built on historical volume forecasts and matching-engine-aware child sizing.

| Premium type | What it does | Reference |
|---|---|---|
| TT Brisk | Front-weighted trajectory vs. forecast volume — fills closer to arrival (Start Time) to minimize slippage from arrival price | [tt-brisk-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-brisk-order.md) |
| TT Close | Back-weighted trajectory — fills closer to a target end-time price (e.g., settlement/close) | [tt-close-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-close-order.md) |
| TT POV | Tracks a fixed user-defined participation rate of real-time market volume until filled | [tt-pov-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-pov-order.md) |
| TT Scale POV | Participation rate dynamically scales between a min/max range based on real-time conditions | [tt-scale-pov-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-scale-pov-order.md) |
| TT Prowler | Enhanced iceberg combining random display size, pegging, and sniping to minimize signaling | [tt-prowler-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-prowler-order.md) |
| TT TWAP+ | Executes at a near-linear rate across the time horizon | [tt-twap-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-twap-order.md) |
| TT VWAP+ | Uses historical intraday volume curves to track VWAP over the execution horizon | [tt-vwap-order.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-vwap-order.md) |
| TT Splicer | Executes a user-defined synthetic spread via a chosen sub-strategy (Brisk/Close/TWAP+/VWAP+) with leg-risk controls; launched from Autospreader by selecting the TT Splicer formula | [tt-splicer.md](../reference/basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-splicer.md) |

See also: [spread-trading-autospreader.md](spread-trading-autospreader.md) for how TT TWAP drives Autospreader
instruments — [worked example](../reference/basic-order-entry/tt-order-types/case-studies/using-tt-twap-to-drive-tt-autospreader-instruments.md).

---

## MD Trader mechanics

MD Trader is the primary ladder-trading widget: single-click order entry against a static, vertical price axis.
Overview: [md-trader-overview.md](../reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md).

**Order entry**: select account (required), order type, TIF, quantity (typed, quantity buttons, or the persistent
second-default quantity via right-click), then click a **Bids**/**Asks** cell at the target price to submit —
[entering-an-order.md](../reference/basic-order-entry/md-trader/task-md-trader/entering-an-order.md). Orders can be
submitted **on hold** (Hold button) and resubmitted later from the Order Book. Custom TT order type buttons seed a
template without opening the parameter flyout; right-click seeds the type *and* opens the flyout.

**Order management**: drag-and-drop a working-order cell to a new price to reprice all orders at that level; middle-click
opens a Floating Order Book to edit WrkQty/Price/TrgPrc or cancel; clicking a Work cell cancels all orders at that
price; **CXL B/S/All** buttons cancel by side —
[managing-orders.md](../reference/basic-order-entry/md-trader/task-md-trader/managing-orders.md). Right-clicking a
multi-order price level lets you reduce (never increase) the total working quantity — TT deletes the *newest* orders
first to preserve your best queue position (Limit, Stop Limit, Stop Market, TT Stop only).

**Ladder details**: PIQ (position-in-queue, FIFO, estimated on non-CME markets), BCnt/ACnt (order headcount per
level), average open-price shading per side, net position display (optionally aggregated across accounts), and
Work-column abbreviations (W working / B bought / S sold / E both-sides-sum / D disclosed / U undisclosed) — full
detail in [trading-with-md-trader.md](../reference/basic-order-entry/md-trader/description-md-trader/trading-with-md-trader.md).
Timed orders with a future start show as callouts on the Work column header until a price exists.

**Keyboard trading**: enabled per-widget in local settings (requires hotkeys enabled workspace-wide); single-alpha-key
hotkeys move/act on buy and sell markers independently of the mouse — full table in
[keyboard-trading-in-md-trader.md](../reference/basic-order-entry/md-trader/description-md-trader/keyboard-trading-in-md-trader.md):

| Action | Hotkey | Action | Hotkey |
|---|---|---|---|
| Increase/center/decrease buy marker | D / E / C | Increase/center/decrease sell marker | K / I / M |
| Buy at buy marker | A | Sell at sell marker | `;` |
| Delete buy orders at marker | S | Sweep buy up to marker | Ctrl+A |
| Sweep sell down to marker | Ctrl+`;` | Center both markers + ladder | Ctrl+Space |

Configuration reference (columns, display, market-data, trade-sound settings) is in
[md-trader-reference.md](../reference/basic-order-entry/md-trader/reference-md-trader/md-trader-reference.md); adding
instruments, laser lines, and ladder re-centering are covered under `task-md-trader/`.

---

## Order Ticket

The compact, single-instrument alternative to MD Trader for order entry — usable from Market Grid, Time and Sales,
Options Chain, Positions, and Spread Matrix. Overview:
[order-ticket-overview.md](../reference/basic-order-entry/order-ticket/description-order-ticket/order-ticket-overview.md).

Three flavors — [types-of-order-tickets.md](../reference/basic-order-entry/order-ticket/description-order-ticket/types-of-order-tickets.md):

| Type | Behavior |
|---|---|
| Floating | Pre-populates from the clicked market-data cell (Bid/Ask/Qty/Position); closes after the order is placed (green border) |
| Linked | Tracks the selected contract in its parent Market Grid; stays open after submission (yellow border) |
| Unlinked | Static contract, independent of Market Grid selection (no border) |

Order type, TIF, and account selectors mirror MD Trader's, auto-populated from what the exchange/instrument supports —
[order-entry-from-order-ticket.md](../reference/basic-order-entry/order-ticket/description-order-ticket/order-entry-from-order-ticket.md).
Notable Order Ticket–specific features: **Notional** entry (futures/crypto, not options/spreads), **Price Payup**
(configure a Limit price as a tick/percent payup from LTP/Bid/Ask/Same/Opposite Side — front-end computed, not an
algo), Floating Depth on hover, and a **Stage** checkbox to submit the order as a [care order](#care-orders--the-tt-oms-lifecycle)
for another user to claim — see
[submitting-an-order.md](../reference/basic-order-entry/order-ticket/task-order-ticket/submitting-an-order.md).

---

## Care orders & the TT OMS lifecycle

A care order is a synthetic **parent** order, processed entirely inside TT and never sent to the exchange, submitted
so another trader or desk can work it. Terms and roles —
[care-orders-overview.md](../reference/tt-oms/care-orders/description-care-orders/care-orders-overview.md):

- **Originator** — creates the care order (e.g., a portfolio manager).
- **Owner** — the user who has currently claimed the care order and enters child orders against it.
- **Parent order** — the care order itself (internal to TT, never routed to the exchange).
- **Child order** — the exchange-native or TT-synthetic order(s) the owner submits to fill the parent.

All care-order actions (claim, modify, cancel, assign fills, pass, bulk/stitch/split, release) require **OMS Allowed**
enabled for the user in Setup; without it the Order Book/OFW block these actions entirely.

**Lifecycle**:

1. **Submit** — from Order Ticket (Stage checkbox), a FIX-connected OMS, or another TT user — appears with
   `Status=Available`.
2. **Claim** — a permissioned user clicks the order (Available is an actionable button) or uses **Claim** in the
   toolbar; the claimer's alias appears in `CurrentUser` and the order becomes theirs to manage. Claiming can also
   happen from a staged-order pop-up alert. **Unclaim** returns it to Available (requires the "Unclaim Orders Owned
   by Others" permission to force-unclaim someone else's) —
   [claiming-and-unclaiming-care-orders.md](../reference/tt-oms/care-orders/task-care-orders/claiming-and-unclaiming-care-orders.md).
3. **Work it** — the owner submits **child orders** (own account or a different one), assigns existing **orders**
   or **fills** from their inventory (must match side/contract, be ≤ the care order qty, at the same-or-better
   price), or enters a **manual fill** —
   [assigning-fills-and-orders-to-care-orders.md](../reference/tt-oms/care-orders/task-care-orders/assigning-fills-and-orders-to-care-orders.md).
   Both owner and originator see fills in their Fills widget; if the owner fills from their *own* account, the
   originator sees only their own account's slice — [care-order-management.md](../reference/tt-oms/care-orders/description-care-orders/care-order-management.md).
4. **Resolve** — fully filled, canceled, or (for HKEX/JPX) executed as a **wholesale trade** by pairing two opposite-side
   staged orders and sending them to Blocktrader, which links the resulting fills back to both care orders —
   [executing-care-orders-as-wholesale-trades.md](../reference/tt-oms/care-orders/task-care-orders/executing-care-orders-as-wholesale-trades.md).

**Combining tools** (all require claiming first, and all interoperate):

| Tool | Does | Cannot be applied to | Reference |
|---|---|---|---|
| Bulking | Combines 2+ same-instrument, same-side care orders into one parent for execution, then allocates fills back | Orders that are already a bulk child; native/TT Order Type/ADL/bank-algo orders | [bulking-overview.md](../reference/tt-oms/bulking/description-bulking/bulking-overview.md) |
| Stitching | Combines care orders for **different** instruments into a spread, netting a calculated spread price; mismatched leg qty creates a remainder "tail" | Existing stitched parents with working children; partially/fully filled allocated orders; fully filled bulk/stitch/split orders | [stitching-and-splitting-overview.md](../reference/tt-oms/stitching-and-splitting/description-stitching-and-splitting/stitching-and-splitting-overview.md) |
| Splitting | Divides one claimed care order into two equal orders that can be stitched/bulked separately | Bulked orders (remove from bulk first); orders with working children; already-split orders; stitched orders | same as above |
| Combine | Previews/launches Bulk or Stitch for a selection of care orders in one screen | — | [combine-overview.md](../reference/tt-oms/combining/description-combining/combine-overview.md) |
| Lock and Release | Delays fill reporting to the originator until the order is fully filled/allocated, controlling reported price timing | — | [lock-and-release-overview.md](../reference/tt-oms/lock-and-release/description-lock-and-release/lock-and-release-overview.md) |
| Order Passing | Hands **visibility and management** of a *working* (non-care) order to another user group ("caretaker") without disrupting queue position; group-level, configured by an admin — cannot be "pulled," only pushed | — | [order-passing-overview.md](../reference/tt-oms/order-passing/description-order-passing/order-passing-overview.md) |
| Order Exceptions | Desk-level widget for repairing/rejecting FIX care-order rejections (not shown in the regular Order Book) — requires OMS Advanced enabled | — | [order-exceptions.md](../reference/tt-oms/order-exceptions/description-order-exceptions/order-exceptions.md) |

A `BulkFrom`/`SplitFrom`/`StitchFrom` order cannot itself be executed once it has been folded into a `BulkTo`/`SplitTo`/`StitchTo`
parent — the Execute button on such a selection is disabled or silently skips those rows.

---

## Routing rules

Routing Rules split a single submitted order across multiple brokers/accounts by percentage, direction, or a fixed
allocation — [routing-rules-overview.md](../reference/basic-order-entry/routing-rules/description-routing-rules/routing-rules-overview.md).
A rule is a set of **portions**, each with a Profile-or-Account, a **Portion** value (positive integer 1–999, treated
as a ratio not a literal percentage), and a **Side** (Buy/Sell/Both) —
[creating-a-routing-rule-in-tt.md](../reference/basic-order-entry/routing-rules/task-routing-rules/creating-a-routing-rule-in-tt.md).

At order entry, portions whose Side excludes the order's direction are dropped, then each remaining portion's ratio
is `portion / sum(remaining portions)`; quantities are rounded to best hit the target ratios, and any remainder is
assigned by random draw among the portions for fairness —
[routing-portion-calculations.md](../reference/basic-order-entry/routing-rules/description-routing-rules/routing-portion-calculations.md).
For a TT Order Type slicer split across accounts by a routing rule, the ratio applies to **both** the parent quantity
and each child's disclosed quantity, with a floor of 1 on the disclosed quantity per split.

---

## Block trading

Blocktrader submits options/futures block trades and other prearranged OTC trades for reporting and clearing —
[blocktrader-overview.md](../reference/basic-order-entry/blocktrader/description-blocktrader/blocktrader-overview.md).
Requires **Submit Block Orders** enabled per user in Setup. Per-exchange wholesale-trade mechanics (CME EFRP/block,
Eurex/EEX, Euronext, ICE, JPX J-NET, LME cross, MEFF cross, MX one-sided, HKEX OTC, TFEX OTC, GFO-X, NDAQ EU, NZX,
SGX) are documented individually under `reference-blocktrader/`; start from
[blocktrader-wholesale-trade-types-on-tt.md](../reference/basic-order-entry/blocktrader/description-blocktrader/blocktrader-wholesale-trade-types-on-tt.md)
and drill into the specific exchange page only as needed. Templates for repeat trades:
[creating-blocktrader-templates.md](../reference/basic-order-entry/blocktrader/task-blocktrader/creating-blocktrader-templates.md).
Crypto order entry (Coinbase-backed) is a separate flow under `trading-crypto-on-tt/`, and B3 has its own order-entry
notes under `trading-on-b3/trading-on-b3-overview.md`.

---

## Order profiles

Order Profiles seed order-entry widgets (account, order type, max size, TIF, MiFID II fields, …) by best-match on
market/product/product-group/product-type, so MD Trader and Order Ticket default correctly without per-order manual
entry — [order-profiles-overview.md](../reference/basic-order-entry/order-profiles/description-order-profiles/order-profiles-overview.md).
Fields you edit at order entry override the profile's seeded values; profiles with admin-set MiFID II fields cannot
be edited from the widget. An Autospreader profile rule with `Exch=Autospreader` seeds the parent and all legs; if
blank, each leg falls back to its own best-matched rule.

---

## Related guides

[Spread Trading / Autospreader](spread-trading-autospreader.md) · [Order Management & Risk](order-management-and-risk.md) ·
[Algo Ops](algo-ops.md) · ADL [Design Patterns](../../adl-kb/guides/design-patterns.md) ·
[Formula Reference](../../adl-kb/guides/formula-reference.md) (TIF/order-type numeric codes) ·
[Core Semantics](../../adl-kb/guides/core-semantics.md) (Order vs Discrete Order vs Single Order Container)
