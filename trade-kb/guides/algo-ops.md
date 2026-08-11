# Algo Ops: Dashboard, Autotrader & Excel

Once an algo is built and deployed, it is launched, watched, and tuned through exactly two widgets —
Algo Dashboard and Autotrader — plus an optional Excel layer that drives their variable cells live. This
guide covers that operational surface: launching, monitoring, modifying live parameters, templates, and
built-in (non-ADL) algo types you'll encounter alongside your own.

[Trade KB Home](../Trade-KB-Home.md) · [Spread Trading Guide](spread-trading-autospreader.md) ·
[Order Types Guide](order-types-and-execution.md) · [Market Data Guide](market-data-and-depth.md) ·
**Algo Ops** (this guide) · [Order Management & Risk](order-management-and-risk.md) ·
[Platform & Workspace](platform-and-workspace.md)

---

## Algo Dashboard vs Autotrader

Both widgets deploy, launch, and manage algos built in ADL or TT Algo SDK, and both let you pick a
co-located data center nearest the exchange for execution. They overlap heavily but differ in shape:

| | Algo Dashboard | Autotrader |
|---|---|---|
| Launch style | One algo at a time, from a tree of My Algos / Shared with me | Multiple algos and multiple instances of each, in tabs |
| Layout | Three panes: Algo Explorer (left), Algo Orders grid (center), Algo Variables (right) | One grid per tab; every algo variable is a column |
| Best for | Picking parameters carefully before a single launch, watching P/L and order counts | Spinning up many instances fast (e.g. one per instrument) or bulk-editing via Excel paste |
| Excel-linking variables live | **No** — paste is static only | **Yes** — cells can be linked so they update from the spreadsheet in real time |
| Reference | [Algo Dashboard overview](../reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) · [panes](../reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-panes.md) | [Autotrader overview](../reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) · [overview 2](../reference/algo-trading/autotrader/description-autotrader/autotrader-overview-2.md) · [display](../reference/algo-trading/autotrader/description-autotrader/autotrader-display.md) |

Both widgets only list ADL algos and Order Ticket Algos (OTAs) you have permission to run — see
[algo sharing](../../adl-kb/reference/adl-overview/advanced-concepts/description/algo-sharing.md) for how
that permission is granted. Algo orders launched from either widget can also be managed from the
[Order Book](../reference/order-management/order-book/description-order-book/order-book-overview.md) widget, and
Autotrader can auto-create tabs for OTAs/OMAs that were started elsewhere so one widget shows everything running
→ [Managing algo instances](../reference/algo-trading/autotrader/task-autotrader/managing-algo-instances.md).

Every user-defined variable block in your ADL algo (Bool, Number, Instrument, Price) automatically becomes a
column/field in both widgets; exported block outputs appear too, colored differently (orange in Autotrader) from
input variables (green) → [User-defined variables](../../adl-kb/reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/user-defined-variables.md) ·
[Launching in Autotrader](../reference/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader-2.md).

---

## Launching an algo

### From Algo Dashboard

1. Select the algo in the Algo Explorer tree.
2. Configure parameters in the center pane; **Co-location** is seeded from the algo's default instrument's
   market (or shared market, if multiple instruments agree).
3. Optionally give the instance a custom **Instance name** (shows in the **TextTT** column) →
   [Algo instance names](../reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-instance-names.md).
4. Pick the **Client Disconnect** action (Leave / Pause / Cancel) — default is set in
   [Algos & Autospreader preferences](../reference/overview/preferences/description-preferences/algos-autospreader-preferences.md).
5. Click **Launch algo**. Status goes **Starting** → **Working**.

Full walkthrough, including multi-account routing for Autospreader/Aggregator instruments (submit legs to
different accounts/brokers) →
[Launching an algo from the Algo Dashboard](../reference/algo-trading/algo-dashboard/task-algo-dashboard/launching-an-algo-from-the-algo-dashboard.md).

### From Autotrader

1. **Pick Algo**, which opens a widget seeded with that algo's columns.
2. **Add row** (or the dropdown, for multiple) to create instance rows — a row is inert until launched.
3. Fill in each row's variables manually, by pasting from Excel (static), or by
   [linking from Excel](#excel--rtd-linking) (live).
4. Select rows and click the play icon to launch; **Status**/**SynthStatus** goes Starting → Working.

→ [Launching an algo in Autotrader](../reference/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader-2.md) ·
[step-by-step with Excel](../reference/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader.md)

Users running many simultaneous instances should check the co-location capacity table first:

| Facility | ADL algo instances | TT order type instances |
|---|---|---|
| Aurora | 100 (up to 400 under load) | 100 (up to 400 under load) |
| Bangkok | 100 | 100 |
| Other co-los | 100 (up to 200 under load) | 100 (up to 200 under load) |
| Simulation / UAT | 25 per region (higher under load) | 25 per region (higher under load) |

→ [Algo Server limitations](../reference/algo-trading/autotrader/reference-autotrader/algo-server-limitations.md).
These limits don't apply on a dedicated TT Reserved Algo Server instance.

---

## Monitoring a running algo

An algo parent order moves through the same status set in both widgets:

| Status | Meaning | Ends when |
|---|---|---|
| Starting | Initializing / risk checks | Initialization completes |
| Working | Running normally | Paused, canceled, or Algo Server status changes |
| Paused | Suspended | Resumed or canceled |
| Deleting | Cancel in progress | Algo Server finishes deleting child orders |
| Failed | Stopped abnormally | — (Algo Server may leave the parent Failed if it can't delete all children) |

→ [Algo Dashboard reference](../reference/algo-trading/algo-dashboard/reference-algo-dashboard/algo-dashboard-reference.md) ·
[Autotrader reference](../reference/algo-trading/autotrader/reference-autotrader/autotrader-reference.md)

Supported live actions on a parent order: **Cancel**, **Pause**, **Resume**, and — algo-dependent — **Modify
quantity** or **Modify price** via the Algo Variables pane (a Paused-state change takes effect on Resume).
Pausing/canceling respects the algo's **Leave Orders on Pause/Cancel** setting for child orders. In
Autotrader, **Pause** deletes children with Leave-on-Pause = False, **Stop** deletes children with
Leave-on-Cancel = False and (if unpinned) removes the row →
[Managing algo instances](../reference/algo-trading/autotrader/task-autotrader/managing-algo-instances.md).

The Algo Dashboard's right-hand **Algo Variables** pane has two tabs: **Variables** (algo-specific inputs
plus fixed standard ones like Co-location and Client Disconnect Action) and **Exports** (block
output values exported in ADL) →
[Algo dashboard panes](../reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-panes.md) ·
[Export block output values](../../adl-kb/reference/adl-overview/advanced-concepts/description/export-block-output-values.md).
Note the fields you **cannot** change on a working order in either widget: **Instrument**, **Co-location**,
**Disconnect Action**, **Ignore Market State** →
[Modifying algo variables in working orders](../reference/algo-trading/autotrader/task-autotrader/modifying-algo-variables-in-working-orders.md).

To edit several working child orders of the same type at once: select them in the Order Book, right-click →
**Open > Algo Dashboard**, edit the pre-filled Algo Parameters pane (blank = mixed values across the
selection), and **Submit** to bulk-apply →
[Modifying multiple algo parameters](../reference/algo-trading/algo-dashboard/task-algo-dashboard/modifying-multiple-algo-parameters-for-working-child-algo-orders.md).
In Autotrader, select adjacent cells in a column/row/region and change the last one to fan the value out to
the whole selection, then **Submit** (or **Discard**) →
[Modifying an algo variable in a working order](../reference/algo-trading/autotrader/task-autotrader/modifying-an-algo-variable-in-a-working-order.md).

Autotrader also supports **pinning** rows so they stay visible after the algo completes, filtering columns,
and auto-creating tabs for algos launched elsewhere →
[Managing algo instances](../reference/algo-trading/autotrader/task-autotrader/managing-algo-instances.md).

---

## Templates

A template saves a named set of variable values for one algo so you can launch it repeatedly without
re-entering parameters — the clip size, offset ticks, and on/off toggles for a strategy you run every day.
Templates are created and used identically in concept from three places:

| Widget | Create | Use | Set default | Notes |
|---|---|---|---|---|
| Algo Dashboard | **Templates** dropdown → **Add template** | Select from dropdown, adjust, **Launch** | Star icon in Templates dropdown | [Managing algo templates](../reference/algo-trading/algo-dashboard/task-algo-dashboard/managing-algo-templates-2.md) |
| Autotrader | **+ Add row** dropdown → **Manage templates** | Select template from **+ Add row** | Star icon in template flyout | [Managing algo templates](../reference/algo-trading/autotrader/task-autotrader/managing-algo-templates-3.md) |
| Template Manager (dedicated widget) | **+Add Template** button per algo in Algo Explorer | Launch pre-loaded, or bind to an [MD Trader custom button](../reference/basic-order-entry/md-trader/task-md-trader/configuring-md-trader.md) | Hover a template, click the star | [Template Manager overview](../reference/algo-trading/template-manager/description-template-manager/template-manager-overview.md) · [managing templates](../reference/algo-trading/template-manager/task-template-manager/managing-algo-templates-4.md) |

Templates created in any one of the three are visible and usable from the other two —
→ [Algo templates (Algo Dashboard)](../reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-templates.md) ·
[Algo templates (Autotrader)](../reference/algo-trading/autotrader/description-autotrader/algo-templates-2.md).

**All templates are private** — nobody else can see or use yours, though anyone sharing the same order book
can Pause/Run and adjust variables on an instance once you've started it. Cloning (Template Manager) lets
you fork a template into multiple presets fast, e.g. one per instrument for the same clip-size/offset logic.

---

## Excel / RTD linking

Two independent mechanisms connect TT to Excel, both requiring the TT Excel Add-in
(Windows, Excel 2010+, .NET 4.6, DNS access to `localhost-tradingtechnologies.com:8181`) →
[Excel integration with TT overview](../reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md) ·
[Installing the add-in](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/installing-and-enabling-the-excel-add-in.md) ·
[Connecting TT to Excel](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/connecting-tt-to-excel-spreadsheets.md).
Behind a corporate proxy, `localhost-tradingtechnologies.com` must be excluded from it →
[Integration with a web proxy](../reference/algo-trading/excel-integration-with-tt/reference/integration-with-a-web-proxy.md).

| Mechanism | Direction | Use for |
|---|---|---|
| **Excel linking** | Spreadsheet → TT widget (live) | Driving algo user-defined variables in Autotrader/MD Trader from spreadsheet calculations |
| **Excel RTD** | TT → Spreadsheet (live) | Pulling market data, positions, orders, fills into cells for your own calculations |

→ [Excel linking overview](../reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-linking-overview.md) ·
[Excel and the TT RTD Server overview](../reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-and-the-tt-rtd-server-overview.md)

### Driving algo variables from Excel (linking)

In Excel, select cells → right-click → **Copy link to TT**. In Autotrader, select the matching range of
**editable, numeric** user-defined-variable cells → right-click → **Paste Link From Excel** (Bool/toggle and
non-numeric variables can't be linked this way). The linked cells then update live
whenever the spreadsheet recalculates — e.g. change a quantity in Excel and every linked instance's clip
size updates immediately. This is the ADL side of the same feature the ADL guide documents as
[Linking Excel Data to the Algo Dashboard](../../adl-kb/reference/adl-overview/advanced-concepts/description/linking-excel-data-to-the-algo-dashboard.md) —
that page covers the ADL-variable side; this one covers the Trade-widget side.
→ [Linking – Sharing data between Autotrader and Excel](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel.md)

The reverse also works: right-click an exported block-output cell in Autotrader → **Copy link to Excel**,
paste into the spreadsheet, and it updates live as the algo runs (shows "Initializing" until the algo
starts). Requires the ADL algo to
[export block outputs](../../adl-kb/reference/adl-overview/advanced-concepts/task/exporting-block-outputs.md) first.

**Instrument and Account cannot be linked** — TT disallows changing these after launch, so only static
copy/paste works for them; use the instrument's short name (e.g. `ESU6`) to identify it, obtainable via
Shift+Ctrl+X on a Market Grid row →
[Linking – Using instruments and accounts in your spreadsheet](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-using-instruments-and-accounts-in-your-spreadsheet.md).

MD Trader also accepts a pasted Excel link as a **laser line** — a visual marker on the price ladder for a
theoretical price, which moves live as the linked cell changes →
[Adding laser lines to MD Trader](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/adding-laser-lines-to-md-trader.md).

**Safety behavior**: TT requires the Excel connection to stay alive for the life of any algo using linked
values. If the connection drops while the workspace stays open, running algos with links are **automatically
paused**; closing the workspace instead leaves them running but freezes the linked values as static. Closing
Excel, the launching widget, or the workspace each trigger a confirmation dialog →
[Alerts when the Excel/TT connection is disrupted](../reference/algo-trading/excel-integration-with-tt/reference/alerts-and-messages-displayed-when-the-excel-and-tt-connection-is-disrupted.md).

### Pulling live data into Excel (RTD)

RTD formulas follow `=RTD("tt.rtd",,Topic,...)`. Useful shapes for driving a strategy:

| Need | Formula shape | Reference |
|---|---|---|
| Instrument ID by short name | `=RTD("tt.rtd",,"Inst","CME","ESU6")` | [Retrieving instrument IDs and properties](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/rtd-retrieving-instrument-ids-and-properties.md) |
| Single field (bid/ask/last/etc.) | `=RTD("tt.rtd",,inst-id,"Bid")` | same, Type 1 properties |
| Market depth (N levels) | `=RTD("tt.rtd",,inst-id,"TTDepth",N,cell)` | same |
| Position stats, filtered | `=RTD("tt.rtd",,inst-id,"NetPos","Account=X")` | Type 2 properties, same page |
| Time & Sales feed | `=RTD("tt.rtd",,"TS",inst-id,rows,cell)` | [Retrieving time and sales data](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-time-and-sales-data.md) |
| One order's property | `=RTD("tt.rtd",,"Order",property,"TextTT=tag")` | [Retrieving order properties](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-order-properties.md) |
| ADL exported/input variable | `=RTD("tt.rtd",,"Order","Block.connector","TextTT=tag")` | same page — block name for inputs, `Block.connector` for outputs |
| Working orders / fills as a grid | `=RTD("tt.rtd",,"Orders"/"TTFills",columns,n,setid,cell)` | [Retrieving working orders and fills](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-working-orders-and-fills.md) |
| Realized/Unrealized P&L | `(LTP−AvgOpenPrice#)×NetPos×PointValue` etc. | [Calculating Realized and Unrealized P/L](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/calculating-realized-and-unrealized-p-l.md) |

Full property catalogue (market/instrument, order book, fills, position, options fields) →
[Excel RTD properties](../reference/algo-trading/excel-integration-with-tt/reference/excel-rtd-properties.md).
Filters combine as OR across repeated `=` and AND across `<>` or mixed conditions →
[Combining multiple filters](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/combining-multiple-filters.md).

**Latency note**: Excel throttles RTD refresh to 2000ms by default. For anything feeding a live strategy,
set `Application.RTD.ThrottleInterval = 0` (or the equivalent registry key) so cells update continuously
→ [Setting Excel throttle limits](../reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/setting-excel-throttle-limits.md).
Also note the hard ceiling: **100 columns × 5000 rows** for any Excel↔TT paste operation →
[Excel integration with TT overview](../reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md).

If setup breaks: check the [add-in troubleshooting](../reference/algo-trading/excel-integration-with-tt/reference/excel-integration-troubleshooting.md)
page for the known .NET 4.6 VSTO installer failure and its workaround, and verify your workstation clock is
synced — a clock more than a minute off will fail the connection.

---

## Built-in algos (not ADL)

Two families of TT-provided algo types appear in Algo Dashboard/Autotrader alongside your custom ADL algos.
Both are themselves built in ADL and shared publicly, so you can open, study, and fork them →
[Algo sharing](../../adl-kb/reference/adl-overview/advanced-concepts/description/algo-sharing.md).

### Market-making algos (MMAs)

Automated two-sided quoting strategies, launched and monitored exactly like a custom ADL algo (Autotrader or
Algo Dashboard; values manual, Excel-linked, or templated) →
[Market-making algos](../reference/algo-trading/market-making-algos/market-making-algos.md).

| Variant | Quote price source |
|---|---|
| Direct Entry | Fixed `Bid Prc` / `Ask Prc` you supply |
| Single Theo | Offset (ticks) from one `Theo Price` |
| Bid/Ask Theo | Offset from separate `Theo Bid` / `Theo Ask` |
| Market Base | Offset from the quoted instrument's own inside market |
| Reference Market | Offset from a *different* reference instrument's inside market, times an optional multiplier |

Shared parameters across all variants: `Bid/Ask Qty`, `Enable Cover Orders` + `Cover Order Offset` (auto
place an offsetting order on fill), `Quote Throttle` (min ms between requotes), `Fill Throttle` (pause
requoting after a fill), `Max Pos` (required — the algo pauses without one), `Manual Requote` (hold quoting
on the filled side until you click **Requote**), `If Quote Outside/Inside Join Mkt`, `Don't Cross Market`,
`Use Cancel/Replace`, and `Reset Open Pos`. TT warns against resuming a Paused MMA — it can briefly quote
stale prices — and any manual order intervention permanently hands that side of the market off the algo's
management. Full parameter table on the same reference page.

### Order Management Algos (OMAs)

An OMA attaches to and manages one or more **already-existing** orders rather than submitting its own
parent — the Trade-side counterpart to ADL's
[Existing Order block](../../adl-kb/reference/trading-blocks/existing-order-block.md) /
[OMA type](../../adl-kb/guides/algo-types.md). Two launch modes:

- **Order Book OMAs** — select existing orders in the [Order Book](../reference/order-management/order-book/description-order-book/order-book-overview.md)
  or Floating Order Book, choose an OMA, set its parameters, launch; the selected orders become children of
  a new OMA parent. TT's public **OCO** algo is an example.
- **Order-builder OMAs** (`Launchable OMA (as OTA)` enabled in ADL) — launched from the MD Trader Order Type
  dropdown in "order-builder" mode: headers shade yellow, an order-builder panel tracks orders added to the
  algo (existing orders you click, or new orders you place — held until launch), and **Launch algo** enables
  once the minimum order count is met. TT's **Conditional**, **OCO 2**, and **MinVol** public algos work this
  way.

→ [Order Management Algos (OMA) overview](../reference/algo-trading/order-management-algos-omas/order-management-algos-oma-overview.md)

---

## Quick troubleshooting

| Symptom | Cause / fix |
|---|---|
| Algo stuck in Starting | Still running initialization / risk checks — wait, or check Algo Server capacity limits |
| Can't change Instrument / Co-location / Disconnect Action / Ignore Market State on a running algo | Fixed for the life of the parent order — cancel and relaunch instead |
| Linked algo suddenly Paused | Excel connection dropped while the workspace stayed open — TT auto-pauses for safety |
| Excel cell shows "Initializing" | Algo instance hasn't started yet — the exported value has nothing to display until it runs |
| RTD values lag the market | Excel's default 2000ms throttle — set `ThrottleInterval = 0` |
| Copy/paste from Excel silently truncates | Over the 100-column × 5000-row TT paste limit |
| Approval-required algo vanished from Trade widgets | An admin turned on run-approval after deployment — see [Algo deployment and approvals](../../adl-kb/reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md) |
