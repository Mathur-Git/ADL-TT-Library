# Order Management & Risk

How TT tracks what you actually hold and what happened to your orders — Position Manager,
Positions, Fills, Order Book, and the alerting you'd wire up as a real-time risk guard around a
live algo.

[KB Home](../README.md) · [Full Index](../INDEX.md) · [Spread Trading & AutoSpreader](spread-trading-autospreader.md) · [Order Types & Execution](order-types-and-execution.md) · [Algo Ops](algo-ops.md) · [Order Management & Risk](order-management-and-risk.md) (this page) · [Platform & Workspace](platform-and-workspace.md)

---

## Why this page matters for a spread-tick algo

If you trade a calendar spread synthetically against its outright leg (long the spread ≈ short
the front month), TT's fill and position data **does distinguish the two** — but only if you know
which column to look at. The **FillType** field on every fill record tags it as an *outright*, a
*spread*, a *spread leg*, or a *synthetic* fill
([Fills Reference](../reference/order-management/fills/reference-fills/fills-reference.md),
[Fill and Audit Trail Service](../reference/order-management/fills/reference-fills/fill-and-audit-trail-service.md)).
Conflating spread fills with their constituent leg fills (or netting a spread position against
the outright position without accounting for the sign flip) is exactly the kind of error that
would misstate your real exposure — the Positions and Position Manager widgets below are the
tools for keeping that straight, and the Alert Manager is the tool for catching it in real time.

## Position tracking (Positions, Position Manager)

The **Positions** widget is the canonical net-position and P/L view: SOD + current-session fills
+ admin fills, rolled up per account
([Positions overview](../reference/order-management/positions/description-positions/positions-overview.md)).

| Goal | How | Reference |
|---|---|---|
| See net position across accounts | Positions widget, aggregate view (default) | [Positions overview](../reference/order-management/positions/description-positions/positions-overview.md) |
| Group by account / exchange / product / contract / risk group | Right-click → **Grouping** | [Displaying positions by group](../reference/order-management/positions/task-positions/displaying-positions-by-group.md) |
| Roll up related-but-distinct instruments (e.g. an outright and its calendar spread) into one exposure view | **Matrix** view mode, custom product group | [Positions matrix view](../reference/order-management/positions/description-positions/positions-matrix-view.md) · [Displaying positions by product group](../reference/order-management/positions/task-positions/displaying-positions-by-product-group.md) |
| Choose the P/L price source (Last, Midpoint, Settle, LTP Waterfall, …) | Positions widget settings → **P/L Calculation** | [How P/L is calculated](../reference/order-management/positions/description-positions/how-p-l-is-calculated.md) |
| Correct a position that doesn't reflect an off-system trade | [Position Manager](../reference/order-management/position-manager/description-position-manager/position-manager-overview.md) manual fill | [Creating a manual fill](../reference/order-management/position-manager/task-position-manager/creating-a-manual-fill.md) |
| Fix or seed a start-of-day position/price per contract | Position Manager, **Admin SOD** tab | [Creating and modifying an SOD](../reference/order-management/position-manager/task-position-manager/creating-and-modifying-an-sod.md) |
| Preview a manual fill/SOD before it hits your live position | Position Manager preview pane | [Previewing manual fill and SOD changes](../reference/order-management/position-manager/task-position-manager/previewing-manual-fill-and-sod-changes.md) |
| Bulk-load fills/SODs from a file | CSV upload, max 1000 rows, header names must match exactly | [CSV file format for uploading fills](../reference/order-management/position-manager/reference-position-manager/csv-file-format-for-uploading-fills.md) · [Uploading local manual fills to TT](../reference/order-management/position-manager/task-position-manager/uploading-local-manual-fills-to-tt.md) |

**The matrix view is the practical answer to "am I really flat."** In matrix mode you can build a
custom product group spanning multiple related contracts (TT's own example: CME CL futures + CME
CL TAS + ICE WBS in one "WTI" group) and see the aggregate net position per group alongside each
leg
([Positions matrix view](../reference/order-management/positions/description-positions/positions-matrix-view.md)).
For a VX outright + calendar-spread book, the same mechanism lets you see the outright leg
position and the spread's *implied* outright exposure side by side — but TT does **not**
automatically flip the sign for you; the P/L on a long spread position and a short front-month
position move in the same direction (both are "long spread P/L convention"), so grouping them
naively will **overstate**, not net, your real notional exposure if you intended them as an
offsetting pair. Verify sign convention per leg before trusting a rolled-up NetPos number.

**Local vs Admin manual fills matter for risk, not just bookkeeping.** Admin fills are visible to
everyone sharing the account and **are used in risk-limit calculations**; Local fills are visible
only to you, don't roll to the next session, and **do not affect any risk checks or limits**
([Position Manager overview](../reference/order-management/position-manager/description-position-manager/position-manager-overview.md)).
If you're using manual fills to true-up a position for your own risk monitoring, Local fills won't
protect you from an account-level credit/position breach — only Admin fills feed the actual limit
checks.

Key **Positions** columns for a P/L-sensitive strategy: `NetPos`, `AvgOpen`, `P/L Realized`,
`P/L Open`, `P/L PriceType` (which waterfall price was actually used), `WrkBuy`/`WrkSell`
(working exposure not yet filled) — full list in the
[Positions reference](../reference/order-management/positions/reference-positions/positions-reference.md).

For the migration-minded: the
[Position Management Transition Guide](../reference/order-management/position-manager/reference-position-manager/position-management-transition-guide.md)
maps old-Monitor position/order-book functionality onto the Positions / Order Book / Position
Manager / Audit Trail widgets described on this page, including Force Cancel for stale orders.

## Fills & Order Book

**Fills** is the fill-level ledger (current + prior 7 sessions); **Order Book** is the live working-order
blotter, including synthetic parent/child structure for algo, TT-order-type, and AutoSpreader orders.

| Goal | How | Reference |
|---|---|---|
| See all fills, most recent first | Fills widget (default view) | [Fills overview](../reference/order-management/fills/description-fills/fills-overview.md) |
| Distinguish outright / spread / spread-leg / synthetic fills | **FillType** column | [Fills Reference](../reference/order-management/fills/reference-fills/fills-reference.md) |
| See fills grouped by order, or just child fills of a synthetic parent | **By Order** / **By Order (Summary)** view | [Fills Views](../reference/order-management/fills/description-fills/fills-views.md) |
| Get notified the instant a fill lands | Fill Alerts widget + desktop notification setting | [Getting alerts for new fills](../reference/order-management/fills/task-fills/getting-alerts-for-new-fills.md) |
| Pull historical fills for a specific date | Right-click → **Go to date** | [Viewing historical fills](../reference/order-management/fills/task-fills/viewing-historical-fills.md) |
| Filter fills by contract/side/account | Column filter (hover column header) | [Filtering your fills](../reference/order-management/fills/task-fills/filtering-your-fills.md) |
| Seed a manual fill from an existing fill row | Right-click fill → **Create Manual Fill** | [Creating manual fills from the Fills widget](../reference/order-management/fills/task-fills/creating-manual-fills-from-the-fills-widget.md) |
| Automate compliance-grade fill/audit export | Fill and Audit Trail Service (EFT/SFTP, 15-min delivery) | [Fill and Audit Trail Service](../reference/order-management/fills/reference-fills/fill-and-audit-trail-service.md) |
| See all working orders | Order Book widget | [Order Book overview](../reference/order-management/order-book/description-order-book/order-book-overview.md) |
| Identify which parent type an order is | **Exch** column: `ALGO` = ADL algo, `ASE` = AutoSpreader, `CME*` = TT order type | [Algos and synthetic orders overview](../reference/order-management/order-book/description-order-book/algos-and-synthetic-orders-overview.md) |
| Filter to just working orders | Quick filter **Working** | [Monitoring working orders in the Order Book](../reference/order-management/order-book/task-order-book/monitoring-working-orders-in-the-order-book.md) |
| Find and diagnose rejected orders | Quick filter **Rejected**; **Message** column mirrors Audit Trail reject text | [Monitoring rejected orders in the Order Book](../reference/order-management/order-book/task-order-book/monitoring-rejected-orders-in-the-order-book.md) |
| Pull an order out of the market without deleting it | **Hold** button | [Placing orders on hold](../reference/order-management/order-book/task-order-book/placing-orders-on-hold.md) |
| Pause/resume a TT order type mid-flight | Add Pause/Resume toolbar buttons | [Placing orders on hold](../reference/order-management/order-book/task-order-book/placing-orders-on-hold.md) |
| Kill a stale order the exchange won't acknowledge | **Force Cancel** (admin permission) | [Deleting orders in the Order Book](../reference/order-management/order-book/task-order-book/deleting-orders-in-the-order-book.md) |
| Wire an OMA (e.g. OCO) onto a live order | Launch OMA button | [Launching an OMA in the Order Book](../reference/order-management/order-book/task-order-book/launching-an-oma-in-the-order-book.md) |
| See full order history/audit for one order | Order History button | [Displaying order details](../reference/order-management/order-book/task-order-book/displaying-order-details.md) |
| Fire a price alert straight off a working order | Right-click order → **Create price alert** | [Creating an Alert from the Order Book](../reference/order-management/order-book/task-order-book/creating-an-alert-from-the-order-book.md) |
| Batch-submit orders from a file | Order upload CSV | [Order upload CSV file format](../reference/order-management/order-book/reference-order-book/order-upload-csv-file-format.md) |
| Trade off the depth at a single price/instrument | Floating Order Book | [Floating Order Book overview](../reference/order-management/floating-order-book/description-floating-order-book/floating-order-book-overview.md) · [Viewing PIQ in the Floating Order Book](../reference/order-management/floating-order-book/task-floating-order-book/viewing-piq-in-the-floating-order-book.md) |
| One widget combining orders + fills + positions | Orders and Fills widget | [Orders and Fills overview](../reference/order-management/orders-and-fills/description-orders-and-fills/orders-and-fills-overview.md) |
| See only the positions implied by a specific subset of fills | "Watch"/eyeball column filters the Fills and Positions panes together | [Displaying positions for selected fills](../reference/order-management/orders-and-fills/task-orders-and-fills/displaying-positions-for-selected-fills.md) |
| Split a fill across multiple accounts after the fact | Allocation pane | [Allocating fills to different accounts](../reference/order-management/orders-and-fills/task-orders-and-fills/allocating-fills-to-different-accounts.md) |

**FillType is the load-bearing field for a spread strategy.** Every fill row (Fills widget, Order
Book, and the Fill/Audit CSV export) carries a `FillType` value indicating outright, spread,
spread leg, or synthetic
([Fills Reference](../reference/order-management/fills/reference-fills/fills-reference.md)).
Filter or group on this column rather than inferring leg vs. spread from contract name — it's the
one place TT tells you unambiguously which side of the outright/spread boundary a given fill sits
on. Also note `Term`, which for a strategy shows the front month when legs span multiple contract
months — useful for confirming which VX expiry a spread fill's exposure actually loads onto.

**Order Book parent/child structure mirrors your ADL algo's own order tree.** An ADL algo's parent
order shows `ALGO` in **Exch** and the algo name in **Contract**/**Type**; its child orders nest
underneath with the parent's `TTOrderID` in their `ParentID` column, and the **Child Orders**
column on the parent shows the live count
([Algos and synthetic orders overview](../reference/order-management/order-book/description-order-book/algos-and-synthetic-orders-overview.md)).
If your algo submits an AutoSpreader spread order as one of its actions, that leg shows up
separately with `ASE` in **Exch** — useful for confirming the algo is actually routing to the
synthetic spread and not silently falling back to outright legging.

## Alerts (real-time risk guard)

Alert Manager is the platform-level, algo-independent risk trip-wire: it watches order, position,
price, or algo-status conditions and can push a desktop or TT Mobile notification the moment a
threshold is crossed — independent of whatever your ADL algo itself is doing.

| Goal | Construction | Reference |
|---|---|---|
| Alert when P/L in an account drops below a threshold | **Position** condition → `P&L` field, operator, value | [Alerts Reference](../reference/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) |
| Alert as net position approaches a limit | **Position** condition → `Position` field, `%` operator against max position (net) | [Alerts Reference](../reference/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) |
| Alert on any fill / reject / cancel on an order | **Order** condition → `Exec Type`, `Status`, `Fill Qty` etc. | [Alerts Reference](../reference/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) |
| Alert if your algo stops or gets suspended | **Algo** condition → `Status` | [Alerts Reference](../reference/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) |
| Alert on a price level or spread-market move | **Price** condition → Bid/Ask/Last/Net Change etc. | [Alerts Reference](../reference/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) |
| Build and manage the alert | Alert Manager widget, **Alert Detail** screen | [Creating an alert](../reference/order-management/alert-manager-and-alert-viewer/task-alert-manager-and-alert-viewer/creating-an-alert.md) |
| Run/pause, edit, copy, delete alerts | Alert Manager toolbar | [Managing alerts](../reference/order-management/alert-manager-and-alert-viewer/task-alert-manager-and-alert-viewer/managing-alerts.md) |
| See triggered alerts live, or replay history | Alert Viewer widget | [Viewing alerts](../reference/order-management/alert-manager-and-alert-viewer/task-alert-manager-and-alert-viewer/viewing-alerts.md) |
| Overview of both widgets | — | [Alert Manager and Alert Viewer overview](../reference/order-management/alert-manager-and-alert-viewer/description-alert-manager-and-alert-viewer/alert-manager-and-alert-viewer-overview.md) |

A **Position** condition alert can be scoped to a single contract or product and set as a percent
of the account's max-position limit — the practical desktop equivalent of capping exposure per
side, without touching the algo. This is worth pairing with, not substituting for, an in-algo
guard: the ADL
[Position Risk block](../../adl-kb/reference/miscellaneous-blocks/position-risk-block.md) caps
position per side *inside* the algo (so the algo itself stops submitting), while an Alert Manager
Position condition is an outside-the-algo tripwire that fires even if the algo's own risk logic
has a bug or was launched without one — see the ADL guide's
[Risk recipe table](../../adl-kb/guides/design-patterns.md#risk) for the in-algo side (Pnl block
for max-loss, Position Risk block for max-position-per-side, Market State → Terminal for halting
on a market-state change). Both consume the same underlying fill/position stream described in the
sections above; the Alert Manager version is just watching it from outside the algo process.

## Accounts & balances

| Goal | How | Reference |
|---|---|---|
| Seed order-entry widgets and filter Order Book/Positions/Fills/Audit Trail by account | Account List widget selection | [Account List overview](../reference/order-management/account-list/description-account-list/account-list-overview.md) |
| Stop a specific widget from reacting to Account List selection | **Ignore global Account List broadcasts** setting | [Account List reference](../reference/order-management/account-list/reference-account-list/account-list-reference.md) |
| See real-time balance, margin, and P/L-driven cash impact | Balances widget (~10s refresh) | [Balances overview](../reference/order-management/balances/description-balances/balances-overview.md) |
| Understand Total Equity / Margin Excess / Initial vs Maintenance Margin fields | Balances field reference | [Balances Reference](../reference/order-management/balances/reference-balances/balances-reference.md) |
| Check what order actions an account/user is permitted (read-only) | Account & User Restrictions widget | [Account & User Restrictions overview](../reference/order-management/account-user-restrictions/description-account-user-restrictions/account-user-restrictions-overview.md) |

Balances' **Margin Excess** and **Total Equity** update off the same live P/L feed the Positions
widget uses, so a fast-moving VX session shows margin headroom shrinking in near-real-time — a
useful secondary confirmation that your Position Risk block's max-position-per-side cap and your
actual margin cushion agree with each other.

## Audit trail / query

Two widgets, same underlying data: **Audit Trail** streams live and lets you scroll back; **Audit
Query** runs an ad hoc, parameterized search against the same "forever" store — the tool for a
post-mortem on exactly what happened around a bad fill or an unexpected position change.

| Goal | How | Reference |
|---|---|---|
| See a live, scrollable stream of every order action, exchange announcement, and reject | Audit Trail widget | [Audit Trail overview](../reference/order-management/audit-trail/description-audit-trail/audit-trail-overview.md) |
| Filter by message type or execution type | Column filter — `ExecutionReport`, `CancelReject`, etc. | [Filtering the contents of the Audit Trail](../reference/order-management/audit-trail/task-audit-trail/filtering-the-contents-of-the-audit-trail.md) |
| Notice when a risk admin manually adjusted your position | Filter message type = `PositionModification` | [Filtering the contents of the Audit Trail](../reference/order-management/audit-trail/task-audit-trail/filtering-the-contents-of-the-audit-trail.md) |
| Pull a specific historical window | **Go to date** | [Viewing historical data](../reference/order-management/audit-trail/task-audit-trail/viewing-historical-data.md) |
| Run a saved, parameterized query across the whole audit history | Audit Query widget | [Audit Query overview](../reference/order-management/audit-query/description-audit-query/audit-query-overview.md) |
| Search, save, and re-run a query; export results | Add Query Parameter → Search → Export | [Searching the audit trail](../reference/order-management/audit-query/task-audit-query/searching-the-audit-trail.md) |

`PositionModification` messages are worth alerting on in their own right if multiple people or
admin tooling can touch your account — it's the audit-trail signature of exactly the kind of
manual fill/SOD change described in the Position Manager section above, and the fastest way to
confirm a Positions-widget discrepancy came from an admin correction rather than a bug in your
algo's own fill handling.

## See also (ADL side)

The Trade-platform widgets on this page are what you look at *outside* the algo process. Inside
an ADL algo, the equivalent risk surfaces are:

* [Pnl block](../../adl-kb/reference/miscellaneous-blocks/pnl-block.md) — cap loss per algo
  instance, consuming the same fill stream shown in the Fills widget above.
* [Position Risk block](../../adl-kb/reference/miscellaneous-blocks/position-risk-block.md) — cap
  position per side, one block per side, reading the same net position the Positions widget
  displays.
* [Design Patterns → Risk](../../adl-kb/guides/design-patterns.md#risk) — the recipe table
  tying Pnl, Position Risk, Market State, and Alert (Audit Trail action) blocks together for a
  worked risk-guard construction.
* [Capturing fills data](../../adl-kb/reference/adl-overview/building-your-first-algo/lessons/capturing-fills-data.md)
  — how an ADL algo reads its own fills via MsgInfoExtractor, the in-algo counterpart to reading
  FillType/AvgOpen off the Fills and Positions widgets by hand.
