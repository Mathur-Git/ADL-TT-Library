# Market Data & Depth

[Trade KB Home](../Trade-KB-Home.md) · [Spread Trading (Autospreader)](spread-trading-autospreader.md) · [Order Types and Execution](order-types-and-execution.md) · [Algo Ops](algo-ops.md) · [Order Management and Risk](order-management-and-risk.md) · [Platform and Workspace](platform-and-workspace.md)

"Which widget shows me X, and how do I configure it to see book imbalance, spread ticks, or a trade print the moment it happens?" This guide covers the five market-data widgets in Trade: Spread Matrix, Depth, Time & Sales, Position in Queue (PIQ), and Market Grid / Product Grid.

For a calendar-spread strategy — watching a thin outright side get taken out and how the exchange-listed spread reprices — the three that matter most are **Spread Matrix** (the spread's own top-of-book), **Depth** (the outright's book imbalance), and **Time & Sales** (the print that confirms the take-out). PIQ and Market/Product Grid are supporting tools.

---

## Spread Matrix (exchange-listed & inter-product spreads)

Spread Matrix is TT's dedicated widget for viewing and trading the market for a **calendar spread as its own instrument**, side by side with the two outright legs that make it up. It is the one place to watch a CFE-listed VX calendar spread's own bid/ask tick by tick rather than inferring it from two separate outright quotes.

Outright contracts run across the top and diagonally; spread markets are shown in the middle, at the intersection of the two legs they're built from. [Spread Matrix overview](../reference/viewing-market-data/spread-matrix/description-spread-matrix/spread-matrix-overview.md) · [Spread Matrix Display](../reference/viewing-market-data/spread-matrix/description-spread-matrix/spread-matrix-display.md)

| Goal | How | Reference |
|---|---|---|
| View an exchange-listed calendar spread's own market | Open Spread Matrix, **Exchange-listed** tab, search the product | [Opening Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix.md) · [Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md) |
| View a synthetic inter-product spread priced by Autospreader® | **Autospreader** tab (existing spread) or **Custom** tab (pick front/back leg products, set Ratio/Multiplier) | [Market data for inter-product spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-inter-product-spreads.md) · [Opening Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix.md) |
| Restrict the matrix to specific expiries | Right-click → **Choose legs…**, uncheck unwanted months, **Save legs** | [Displaying market data in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/displaying-market-data-in-spread-matrix.md) |
| See Butterfly / Condor pricing (3- and 4-leg) alongside Calendar | Toolbar **Butterfly/Calendar** toggle | [Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md) |
| Filter out implied prices, see only direct exchange quotes | Right-click → **Settings…** → **Only show direct prices** | [Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md) |
| Flag partially/fully implied quantities | Widget setting **Show implieds with an asterisk (\*)** (only valid when direct-only is off) | [Spread Matrix reference](../reference/viewing-market-data/spread-matrix/reference-spread-matrix/spread-matrix-reference.md) |
| See last traded price/qty per spread and outright | Enable **LTP/LTQ** (adds a third column) | [Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md) |
| Trade the spread with one click from the matrix | Left-click a spread cell → floating order entry (MD Trader® or Order Ticket), pre-populated with the spread's exchange price | [Order entry for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/order-entry-for-exchange-listed-spreads.md) · [Entering orders in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/entering-orders-in-spread-matrix.md) |
| Trade with single-click order entry (no floating window) | Right-click → **Settings…** → **Enable single click order entry**; panel appears on the left | [Entering orders in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/entering-orders-in-spread-matrix.md) |
| Preview 3 levels of depth for a cell without leaving the matrix | Hover a price/quantity to pop up **Floating Depth**; enable **Show floating depth widget on hover** in settings | [Displaying market data in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/displaying-market-data-in-spread-matrix.md) |
| Manage/cancel a working spread order | Floating Order Book, launched from the Bid/Ask price cell | [Entering orders in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/entering-orders-in-spread-matrix.md) |
| Jump to Chart or Time & Sales for the spread itself | Right-click a spread cell → **Open** → **Chart** / **Time and Sales** | [Displaying market data in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/displaying-market-data-in-spread-matrix.md) |
| Populate a matrix directly from a watchlist | Market Grid: right-click an instrument → **Open** → **Spread Matrix** (all expiries, or Ctrl-click to select specific contracts first) | [Opening the Spread Matrix from the Market Grid](../reference/viewing-market-data/market-grid/task-market-grid/opening-the-spread-matrix-from-the-market-grid.md) |

**Reading the cells.** Each outright or spread grouping shows four data points — Ask Price, Ask Qty, Bid Price, Bid Qty — colorable independently for bid/ask, and green cell shading marks a working order at the best price (a green border means working but away from best). [Spread Matrix Display](../reference/viewing-market-data/spread-matrix/description-spread-matrix/spread-matrix-display.md)

**Direct vs. implied matters for a thin-outright thesis.** On the Exchange-listed tab, best bid/ask price and quantity are computed off *total* (direct + implied) quantity by default. If your read on outright thinness depends on genuinely resting, non-implied size, turn on **Only show direct prices** — otherwise a thin outright can look deeper than it is because of implied quantity flowing in from the spread market. [Market data for exchange-listed spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads.md). On the inter-product/Autospreader tab, implieds are calculated by TT itself (not the exchange) and are shown even off the touch. [Market data for inter-product spreads](../reference/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-inter-product-spreads.md)

**Custom cross-product spreads** (front leg / back leg / Ratio / Multiplier, with fractional multiplier support for tick accuracy) are built via the **Custom** tab and, once an order is entered against them, become a managed Autospreader® synthetic instrument you can edit later. [Opening Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix.md) · [Creating spreads in Spread Matrix](../reference/viewing-market-data/spread-matrix/task-spread-matrix/creating-spreads-in-spread-matrix.md). For the Autospreader engine itself — leg ratios, synthetic-price formulas, working the spread as a managed strategy — see [Spread Trading (Autospreader)](spread-trading-autospreader.md).

---

## Depth widget & book imbalance

Depth is the widget for reading one instrument's **full book** — every price level, detailed per-order depth where the exchange provides it, and running Bid vs. Ask quantity at each level. This is where you actually watch the outright's thin side and confirm imbalance before it gets taken out.

**CFE is one of the exchanges TT supports detailed (order-by-order) depth for** — alongside ASX, ATHEX, B3, CME, CME_BrokerTec, EPEX, JPX, NASDAQ_NED, NDAQ_EU, Nord Pool, OSE, TFEX and SGX — so a CFE VX Depth widget can show individual resting orders per level, not just aggregate size. [Depth widget overview](../reference/viewing-market-data/depth/description-depth/depth-widget-overview.md)

| Goal | How | Reference |
|---|---|---|
| Open Depth for an instrument | Widgets → Market Views → search/Explore; or right-click a Market Grid row → **Open** → **Depth** | [Depth widget overview](../reference/viewing-market-data/depth/description-depth/depth-widget-overview.md) · [Launching Depth from Market Grid](../reference/viewing-market-data/depth/task-depth/launching-depth-from-market-grid.md) |
| See total size at each level instead of individual orders | Right-click → **Hide Detailed Depth** (toggles to aggregate) | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| See how size stacks up moving away from the touch | **BidCum** / **AskCum** columns — cumulative quantity added level by level, away from the inside market | [Depth widget display](../reference/viewing-market-data/depth/description-depth/depth-widget-display.md) |
| See per-level total Bid/Ask size at a glance | **BidQty** / **AskQty** columns (plus **Show Summary Rows** for per-price-level totals in detailed mode) | [Depth widget display](../reference/viewing-market-data/depth/description-depth/depth-widget-display.md) · [Depth reference](../reference/viewing-market-data/depth/reference-depth/depth-reference.md) |
| Identify which counterparty is resting size (where disclosed) | Right-click column headers → **Edit columns…** → add **BidMbr** / **AskMbr** | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| Submit an order directly off a depth level | Click a cell in **BidQty**, **Bid**, **Ask**, or **AskQty** at the level you want → seeded order entry widget | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| Modify/cancel a working order from Depth | Launch Floating Order Book directly on the bid/ask cell | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| Watch the outright and its spread book side by side | Add tabs for multiple instruments in one Depth widget | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| Correlate depth with your own working/filled orders | Group Depth + Order Book widgets; selecting an order shows that instrument's depth | [Using the Depth widget](../reference/viewing-market-data/depth/task-depth/using-the-depth-widget.md) |
| Highlight your own resting orders in the book | Widget setting **Highlight my orders in depth** | [Depth reference](../reference/viewing-market-data/depth/reference-depth/depth-reference.md) |

Net change, Last, LTQ, session High/Low are shown at the top of the widget as instrument-level context alongside the book itself. [Depth widget display](../reference/viewing-market-data/depth/description-depth/depth-widget-display.md)

**Reading imbalance directly.** BidQty vs. AskQty at the touch is the immediate imbalance read; BidCum vs. AskCum a few ticks out tells you how much size stands behind the touch before the level truly runs out — the number that matters for judging whether a "thin" bid or offer is genuinely one clip from disappearing or has support stacked just behind it. On a 0.05-tick outright, the corresponding 0.01-tick spread can and typically will move well before the outright's own next 0.05 print — Depth on the outright is your leading indicator; Spread Matrix or a Depth widget on the spread itself is where you'd watch that reprice happen tick by tick.

For building this logic into an algo instead of watching it by eye, ADL reads live book state through the [Field block](../../adl-kb/reference/trading-blocks/field-block.md) attached to an [Instrument block](../../adl-kb/reference/trading-blocks/instrument-block.md) (BidPrice/BidQty/AskPrice/AskQty and their `MinPriceIncrement` for tick math) — see [Market data, bars and indicators](../../adl-kb/guides/design-patterns.md#market-data-bars-and-indicators) in the ADL design-patterns guide for the corresponding recipes (queue estimation, uptick/downtick counters, moving averages on depth-derived values).

---

## Time and Sales

Time & Sales is the trade-print tape — every real-time and historical trade for the selected instrument(s), reverse-chronological, color-coded by aggressor side. This is the widget that confirms *when* a thin side actually got taken out, as opposed to Depth, which shows the standing book before/after.

[Time & Sales Overview](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md) · [Time & Sales Data](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data.md)

| Goal | How | Reference |
|---|---|---|
| Add one or many instruments (up to 5,000) | Context menu → **Choose Instruments**; add a whole product to auto-include new listed instruments/strategies | [Adding instruments to Time & Sales](../reference/viewing-market-data/time-and-sales/task-time-and-sales/adding-instruments-to-time-sales.md) |
| Show only prints in a price/quantity band | **Price** / **Qty** column filters (filter by Contract first, then Price) | [Time & Sales Data](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data.md) |
| Filter quantity at different scopes | Global / Product / Type / Instrument levels — most specific wins | [Time & Sales Data](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data.md) |
| See millisecond/microsecond print timing | Settings → **Show milliseconds** (then optionally **Show microseconds**) | [Time & Sales reference](../reference/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference.md) |
| Distinguish a genuine large single print from several consolidated prints | Enable **Highlight aggregated quantity cells**; hover a highlighted qty to see up to 20 underlying trades | [Time & Sales Data](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-data.md) |
| Turn off 1-second trade consolidation entirely | Uncheck **Accumulate trades by time (1 sec)** to see every individual print as it occurs | [Time & Sales reference](../reference/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference.md) |
| Get an audible cue on size | **Trade Sounds**: rules on Qty Min/Max + Side + Sound | [Time & Sales reference](../reference/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference.md) |
| Trade off a print's price/qty | Enable **Launch floating order entry on left click on price or quantity**, then click the print | [Entering orders from Time and Sales](../reference/viewing-market-data/time-and-sales/task-time-and-sales/entering-orders-from-time-and-sales.md) |
| Jump to MD Trader / Order Ticket for the printed instrument | Right-click a row → **Open** submenu | [Launching widgets from Time & Sales](../reference/viewing-market-data/time-and-sales/task-time-and-sales/launching-widgets-from-time-sales.md) |

A trade reported between the bid/ask (indeterminate aggressor) prints in **black** rather than the usual buy/sell color. [Time & Sales Overview](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md). The full column set — Date, Time, Contract, Price, Quantity, Term (front-month label for a strategy), Type (Vole/Block/Basis/OTC identifiers) — is listed in [Time & Sales reference](../reference/viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference.md).

**In ADL**, the equivalent primitive is the [Time and Sales block](../../adl-kb/reference/trading-blocks/time-and-sales-block.md), which streams every trade message for hand-built OHLC/VWAP bars, uptick/downtick counters, or recent-volume tracking — see the [Market data, bars and indicators](../../adl-kb/guides/design-patterns.md#market-data-bars-and-indicators) table for the exact block wiring. One documented gotcha carries over conceptually: Time and Sales message coalescing behaves differently live vs. in simulation, so don't tune a "print size confirms take-out" threshold purely against sim behavior.

---

## Position in Queue (PIQ)

PIQ tracks your own order's place in the queue at its price level — either supplied directly by the exchange's feed or estimated by TT when the feed doesn't carry queue position. This matters for a tick-granularity spread strategy because passive resting orders at a stale or thinning price are exactly where queue position decides whether you get filled before the level runs out.

[Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md)

* **Exchange-provided (actual) PIQ**: CME (Market by Order), ICE, BIST send real per-order queue position on their feed.
* **TT-estimated PIQ**: for everything else (this includes CFE), TT estimates queue position conservatively — decremented as trades occur in front of your order, left unchanged if an order in front is *canceled* (TT can't tell if it was ahead of or behind you), and clamped so it never exceeds total quantity at that price. Estimated PIQ resets on logout/refresh and is only tracked while your order price stays within visible depth. In **Simulation**, PIQ is estimated for *all* markets. [Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md)

| Where displayed | Notes | Reference |
|---|---|---|
| MD Trader | Optional **PIQ** column, FIFO ordering for multiple orders at a price; black text, black background + white "0" for first-in-queue, yellow background at the inside market | [Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md) |
| Market Grid | **PIQ Buys** / **PIQ Sells** columns after order submission; same yellow/white color cues | [Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md) |
| Floating Order Book | **PIQ** column per working order, enabled via Preferences → Orders | [Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md) |

Shared-account visibility: by default only the user who placed an order sees its PIQ; **Enable PIQ for orders from other users** in Preferences opens it up account-wide. [Position in Queue (PIQ) Overview](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md)

**In ADL**, the same idea is built by hand as **Estimated Position in Queue (EPIQ)**: start from resting quantity at your price, subtract trades printing at that price, and clamp to BidQty — see [EPIQ](../../adl-kb/reference/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq.md) for the construction and [Generating Position in Queue During Pre-open](../../adl-kb/reference/adl-overview/advanced-concepts/case-studies-advanced-concepts/generating-position-in-queue-during-pre-open.md) for tracking it before the market opens (when there's no live trade feed to decrement against). This is the natural pairing with any algo that quotes the spread passively rather than crossing it — you need queue position on the spread order to know whether you're actually first when the outright's thin side finally trades through.

---

## Market Grid / Product Grid

Market Grid and Product Grid are the multi-instrument watchlist views — one row per instrument, configurable columns, expandable to show depth inline. Market Grid organizes by instruments you add or by product subscription (auto-rolling, auto-adding new listings); Product Grid is built around comparing the same column set across several *products* at once. [Introduction to Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/introduction-to-market-grid.md) · [Introduction to Product Grid](../reference/viewing-market-data/product-grid/description-product-grid/introduction-to-product-grid.md)

| Goal | How | Reference |
|---|---|---|
| Watch a whole product, auto-rolling and auto-adding new expiries | Add tab **From a Product** rather than individual instruments (names show in *italics*) | [Subscribing to Products in the Market Grid](../reference/viewing-market-data/market-grid/task-market-grid/subscribing-to-products-in-the-market-grid.md) |
| Hide rows without breaking a product subscription | Use the **Contract** column filter, not row delete | [Subscribing to Products in the Market Grid](../reference/viewing-market-data/market-grid/task-market-grid/subscribing-to-products-in-the-market-grid.md) |
| Expand a row to see the book inline | Click to expand; detailed depth shown for exchanges that support it (CFE included) | [Market data in Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid.md) |
| Preview 3 levels of depth without expanding the row | Hover a price/qty cell for **Floating Depth** (same widget as in Spread Matrix) | [Market data in Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid.md) |
| See only instruments that are actually trading | **Live Only** mode (hides anything without an active bid/offer/LTP) | [Market data in Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid.md) |
| See TT's calculated implied bid/ask on a calendar spread from the outright legs | **ImpBidQty** / **ImpAskQty** columns ("Implied In"); or the reverse ("Implied Out") for an outright implied from spread + other outright | [Market data in Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid.md) |
| Open every expiry of a product straight into Spread Matrix | Right-click a single-instrument row → **Open** → **Spread Matrix** (Ctrl-click first to restrict to specific contracts) | [Opening the Spread Matrix from the Market Grid](../reference/viewing-market-data/market-grid/task-market-grid/opening-the-spread-matrix-from-the-market-grid.md) |
| Set a price alert straight from a watchlist row | Right-click → **Create price alert** → seeds Alert Manager | [Creating an Alert from the Market Grid](../reference/viewing-market-data/market-grid/task-market-grid/creating-an-alert-from-the-market-grid.md) |
| Compare the same contract across multiple related products | Product Grid — products across the top, expiries down the side | [Introduction to Product Grid](../reference/viewing-market-data/product-grid/description-product-grid/introduction-to-product-grid.md) |

Full column glossary (BidQty/AskQty, BidCnt/AskCnt — number of orders comprising size at a level —, WrkBuys/WrkSells, IndPrc/IndQty for pre-open/auction states, and the options Greeks columns) is in [Market Grid Reference](../reference/viewing-market-data/market-grid/reference-market-grid/market-grid-reference.md).

---

## Quick lookup

**Watch the spread's own tick-by-tick market** → [Spread Matrix, Exchange-listed tab](../reference/viewing-market-data/spread-matrix/task-spread-matrix/opening-spread-matrix.md)

**Read outright book imbalance / thinness** → [Depth widget](../reference/viewing-market-data/depth/description-depth/depth-widget-overview.md), detailed mode (CFE supported), BidQty/AskQty at touch + BidCum/AskCum a few ticks out

**Confirm a level got taken out** → [Time & Sales](../reference/viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md), per-instrument, individual-print mode (not 1-sec accumulated) if you need exact sequencing

**Know if you'd have been filled first** → [Position in Queue](../reference/viewing-market-data/position-in-queue-piq/position-in-queue-piq.md) (estimated for CFE) or [EPIQ in ADL](../../adl-kb/reference/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq.md) if building the estimate inside an algo

**Scan many expiries/products at once** → [Market Grid](../reference/viewing-market-data/market-grid/description-market-grid/introduction-to-market-grid.md) / [Product Grid](../reference/viewing-market-data/product-grid/description-product-grid/introduction-to-product-grid.md)

**Build any of this into a running algo instead of watching by eye** → [Instrument](../../adl-kb/reference/trading-blocks/instrument-block.md) + [Field](../../adl-kb/reference/trading-blocks/field-block.md) blocks for book snapshots, [Time and Sales block](../../adl-kb/reference/trading-blocks/time-and-sales-block.md) for prints, and the [Market data, bars and indicators](../../adl-kb/guides/design-patterns.md#market-data-bars-and-indicators) recipe table in the ADL guide
