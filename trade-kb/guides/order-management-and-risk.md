# Order Management & Risk

How TT tracks what you actually hold and what happened to your orders — Position Manager,
Positions, Fills, Order Book, and the alerting you'd wire up as a real-time risk guard around a
live algo.

[Trade KB Home](../Trade-KB-Home.md) · [Spread Trading & AutoSpreader](spread-trading-autospreader.md) · [Order Types & Execution](order-types-and-execution.md) · [Algo Ops](algo-ops.md) · [Order Management & Risk](order-management-and-risk.md) (this page) · [Platform & Workspace](platform-and-workspace.md)

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
| Make the notification say *what* filled, not just that something did | **Custom** alert text with `{orderN.field}` tokens | [Custom alert text](#custom-alert-text-interpolating-fill-fields) (below - not in the TT mirror) |
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

### Custom alert text: interpolating fill fields

> **Provenance: not from the TT documentation.** Every claim in this subsection comes from
> a working Alert Detail screen shared by a colleague of the user (observed 2026-08-11),
> not from `library.tradingtechnologies.com`. The mirrored pages
> ([Creating an alert](../reference/order-management/alert-manager-and-alert-viewer/task-alert-manager-and-alert-viewer/creating-an-alert.md),
> [Viewing alerts](../reference/order-management/alert-manager-and-alert-viewer/task-alert-manager-and-alert-viewer/viewing-alerts.md))
> mention a **Custom** alert-text checkbox but document **no** substitution mechanism at
> all, and `viewing-alerts.md` describes a notification as showing only "the color and
> message text defined for the alert". Taken alone, those pages imply alert text is
> static. **They are incomplete.** Do not re-derive that wrong conclusion from the mirror.

Ticking **Custom** under **Alert Text** lets the message interpolate fields from the event
that triggered it, using `{conditionName<N>.field_name}` tokens. This is what turns a fill
alert from "a fill happened" into a usable notification, and it is the only documented-anywhere
way to get fill detail onto TT Mobile - the desktop **Fill Alerts** widget (see
[Fills & Order Book](#fills-order-book)) has no mobile equivalent.

An observed-working fill alert, in full:

| Field | Value |
|---|---|
| Alert Name | `Sell Order Filled` |
| Send notifications to | Desktop (pop-up) **and** TT mobile, both ticked |
| Conditions | **ALL** of: `order` → `Exec Type` = `Trade`; `order` → `Product Type` = `Spread`; `order` → `Buy/Sell` = `Sell` |
| Alert Text | Custom: `{order1.instrument_id}, {order1.last_qty}, {order1.price}` |

**The token namespace is the Order-condition field list** `[V]` - confirmed 2026-08-11 by
reading the rule JSON while adding each condition (procedure below). Selecting `Contract`
writes `order.instrument_id` and `Fill Qty` writes `order.last_qty`, which are exactly the
two tokens already observed working in alert text. So **any field in the `Order` condition
dropdown is available as a token**, and its name is what the JSON panel shows.

Names harvested so far, with the UI label each maps to:

| Token | UI field | Renders as | |
|---|---|---|---|
| `{orderN.instrument_id}` | `Contract` | **the readable contract name** - `SR3 Dec26 3mo Butterfly`, *not* the stored integer | `[V]` |
| `{orderN.last_qty}` | `Fill Qty` | **this execution's** quantity, as a float - `1.0`, `3.0` | `[V]` |
| `{orderN.last_px}` | **`Fill Price`** | **the price actually filled at** | `[V]` name |
| `{orderN.price}` | **`Order Price`** | **the price the order was entered at - NOT the fill** | `[V]` name |
| `{orderN.side}` | `Buy/Sell` | **an uppercase label** - `SELL` | `[V]` |
| `{orderN.exec_type}` | `Exec Type` | - (`Trade` stores as code `14`) | `[V]` name |
| `{orderN.product_type}` | `Product Type` | - (`Spread` stores as code `43`) | `[V]` name |
| others | any dropdown entry | `Account`, `CurrentUser`, `Exchange`, `Order Type`, `Status`, `Synth Status`, `TIF`, `Total Filled Qty`, `Total Qty`, `Working Qty`, ... | names harvestable the same way |
| `{orderN.buy_sell}` | - | **does not exist.** The side field is `side`. | `[V]` |

**Interpolation resolves ids and enums to display values, not stored codes** `[V]` (observed
in delivered notifications 2026-08-11). This is the opposite of what the rule JSON suggests -
conditions store `instrument_id` as an opaque integer (`1694217178440827148`) and enums as
numeric codes (`side` = `1`) - so **do not infer render behaviour from the JSON panel.** The
practical consequence: a single alert covering both sides is fully viable, because
`{orderN.side}` delivers `BUY`/`SELL` on its own and the side does not have to be encoded in
the alert name via a mirrored per-side pair.

**An unrecognised token fails loudly, which makes the alert text self-checking** `[V]`. A bad
token renders as its own name with the braces stripped, and TT appends a diagnostic listing
the rejected names. From a live notification:

```
… | side=SELL | bs=order1.buy_sell, unknown fields=buy_sell
```

So `{order1.side}` resolved to `SELL` while `{order1.buy_sell}` echoed back bare, with
`unknown fields=buy_sell` appended to the message. Use this: probe several candidate tokens in
one alert text, take one fill, and the notification itself tells you which names are wrong.

**`price` vs `last_px` is a live trap, and the obvious-looking token is the wrong one.**
`order.price` is the *order* price. An alert built on `{orderN.price}` - as the
first observed working example was - reports the limit you entered, not the price you got.
It looks correct indefinitely, because a resting limit order that fills at its own limit
reports the same number for both. It diverges exactly when the fill is interesting: a
better-than-limit fill, or a spread filling at an implied price away from the order price.
**Use `last_px` for the fill price.**

**A live fill does not necessarily discriminate `price` from `last_px`.** In the observed
notifications both rendered `6.0`, because the order filled at its own limit - the exact
blind spot described above. The `Fill Price` -> `last_px` / `Order Price` -> `price` mapping
therefore rests on the rule-JSON harvest, not on the delivered message. To confirm it from a
fill you need one that prints through the limit.

**`orderN` is a handle to the matched order, not to the field that condition tests** `[V]`.
The first observed alert tests `exec_type` in condition `id: 1` yet reads
`{order1.instrument_id}`, `{order1.last_qty}` and `{order1.price}` off it. So any field of
the order is reachable through any condition's handle; `N` need only match an `id` that
exists.

**`Exec Type` = `Trade` is the house idiom for "any fill, including partials".** A Trade
execution report is emitted per fill event, partial or full, so this needs no quantity
comparison and no dependence on `Status` value names. It also verifies that `Trade` is a
selectable `Exec Type` value, which `alerts-reference.md:20` only hints at with "e.g., New,
Canceled, Rejected". Avoid `Total Quantity`, which the reference explicitly defines as
firing only "when the order is **completely** filled".

**The `N` in `orderN` keys off an explicit stored `id`, not display position** `[V]` - each
condition block in the rule JSON carries its own `"id"` (`"1"`, `"2"`, ...). The risk this
creates is sharper than mere renumbering: if ids are *assigned* rather than recomputed on
delete, removing condition 1 leaves condition 2 still holding `id: "2"` and every
`{order1.*}` token silently resolves to nothing. `[U]` - untested. **Re-read the rule JSON
after deleting any condition** (see below).

Collapsing the conditions into one condition plus **Add Criteria** would make the numbering
moot, but introduces a different unknown: `creating-an-alert.md:66` warns that the ALL/ANY
choice "applies to the condition only and **not** to the criteria within a condition", and
never says how criteria within a condition combine. **Prefer the separate-conditions form
above** - its AND semantics are explicit and it is the form observed working.

**No conflation.** Preferences → Fills and Preferences → Sounds each expose a
**Conflate partial fills (ms)** setting; Alert Manager exposes no equivalent. An order
worked in small clips therefore yields one notification per execution report.

#### The rule JSON panel - how to harvest token names without waiting for a fill

The Alert Detail screen has a **collapsed side panel** (the `>` arrow at its top right) that
exposes the alert's underlying rule tree as JSON, live as you edit `[V]` (observed
2026-08-11). Two `order` conditions render as:

```json
{ "condition": "AND",
  "rules": [
    { "condition": "AND", "type": "order", "id": "1",
      "rules": [ { "field": "order.exec_type",    "operator": "equal", "value": "14" } ] },
    { "condition": "AND", "type": "order", "id": "2",
      "rules": [ { "field": "order.product_type", "operator": "equal", "value": "43" } ] } ] }
```

Three things follow, and together they make this panel the cheapest tool in the Alert Manager:

- **Condition fields live in the same `order.<snake_case>` namespace as the alert-text
  tokens** `[I]`, strongly. `{order1.instrument_id}` / `{order1.last_qty}` are known-working
  tokens, and `Contract` / `Fill Qty` are condition fields - so if those two conditions write
  `order.instrument_id` and `order.last_qty`, the condition field list *is* the token
  vocabulary. **This makes the hypothesis self-verifying against two already-`[V]` tokens.**
- **The discovery procedure:** add a condition, read the field name the panel writes, delete
  the condition. Nothing has to fill. Use it to settle the side token (`Buy/Sell`) and the
  fill-vs-order price ambiguity (add `Fill Price` and `Order Price` and compare the two field
  names).
- **Three Order-condition labels in the mirror are stale** `[V]` (dropdown read 2026-08-11).
  The UI says **`Total Filled Qty`**, **`Total Qty`**, **`Working Qty`**; `alerts-reference.md`
  calls them `Total Fill Quantity`, `Total Quantity`, `Working Quantity`. The other 17 fields
  match, and the dropdown's placeholder row is `Choose a field`.
- **Values are TT-internal enum codes, not FIX** `[V]`. `Exec Type` = `Trade` encodes as
  `"14"`; `Product Type` = `Spread` as `"43"`. FIX ExecType for a trade is `F`, so these are
  TT's own numbering and cannot be predicted from FIX tables - harvest them the same way.
  Operators are word-form (`"equal"`), which is why the mirrored operator table
  (`alerts-reference.md:70-78`) came through with its comparison symbols mangled.

Still open, and cheap to settle with one live test:

- **Is Alert Manager evaluated server-side?** i.e. does TT Mobile push arrive with the
  desktop workspace closed. Nothing in the mirror says. That alerts can be run/paused from
  TT Mobile and the status syncs back to the desktop `Status` column
  (`managing-alerts.md:36-37`) hints the definitions live server-side, but that is `[I]`.
  This is the difference between "notifies me while I'm away from the desk" and "notifies me
  only while TT is running".
- **Whether `price` and `last_px` really differ on a fill that prints through the limit.**
  The field-name mapping is `[V]` from the rule JSON, but no observed notification has yet
  shown the two rendering different values. Everything else about the token vocabulary and
  its render behaviour is now closed.
- **The enum code tables.** Confirmed: `exec_type` `Trade` = `14`; `product_type` `Spread` =
  `43`; `side` `Buy` = `1` `[V]` (dropdown set to Buy, code read back from the JSON), so
  `Sell` = `2` on the FIX convention `[I]`. Remaining values are harvestable one dropdown
  selection at a time from the JSON panel; only needed if you *filter* on them, not to
  interpolate them.
  Also observed: `instrument_id` stores an opaque TT integer - `1694217178440827148` is
  SR3 Dec26 3-month butterfly - not a symbol.
  **Exchange-listed butterflies classify as `Product Type` = `Spread`** `[V]` (SR3 Dec26 3mo
  fly, confirmed 2026-08-11), so a `product_type = 43` condition does cover flies as well as
  outright calendar spreads - it does not silently drop them.

**A `Product Type` = `Spread` condition is load-bearing on a fill alert, not optional
scoping.** Every structure decomposes into outrights, so an alert that also admits outright
fills reports the *legs* - and a leg-level notification stream cannot tell you which
structure (spread / fly / double fly) actually filled. Constraining to `Spread` suppresses
*outright* leg noise, but it is **necessary, not sufficient**: when the legs are themselves
listed spreads it suppresses nothing, and an `Exchange` condition is needed as well (see
below). The corollary: **do not
"test" a spread fill alert by widening it to outrights.** Test it on a real listed-spread
fill, or you are exercising a different code path *and* recreating the noise the condition
exists to suppress.

**A `Spread`-scoped alert covers AutoSpreader fills - and fires once per leg as well as once
for the parent** `[V]`, observed 2026-08-11 on a synthetic VX 1:2 built from two listed CFE
calendars:

| Exchange | Contract | Fill Type | B/S | Qty | Price | TT Order ID | Parent Order ID |
|---|---|---|---|---|---|---|---|
| **ASE** | `Vx Aug26 1:2` | Spread | B | 1 | **-1.11** | `1310136f-…` | - |
| CFE | `VX Aug26-Sep26 Calendar` | Spread | B | 1 | 1.570 | `d455e5d4-…` | `1310136f-…` |
| CFE | `VX Sep26-Oct26 Calendar` | Spread | S | 2 | 1.340 | `1d48e329-…` | `1310136f-…` |

The synthetic parent and both legs all report `Fill Type` = **`Spread`**, so `product_type =
43` matches all three - coverage is fine, but **one structure fill yields N+1 notifications.**
The leg-noise problem the `Spread` condition exists to suppress therefore returns whenever the
legs are themselves *listed spreads*: filtering on product type cannot separate a parent from
its legs when both are spreads. In the Fills widget the only distinguishing columns are
**TT Order ID** and **Parent Order ID**, and neither is an Order condition field.

**Use `Exchange` as the parent/leg discriminator.** The synthetic parent books on **`ASE`**
(the AutoSpreader Server) while the legs book on their real exchange (`CFE` here), and
`Exchange` *is* in the Order condition dropdown. So:

| Goal | Conditions (**ALL**) |
|---|---|
| One notification per AutoSpreader structure fill | `Exec Type`=`Trade` · `Product Type`=`Spread` · `Exchange`=`ASE` |
| Listed spreads/flies traded directly | `Exec Type`=`Trade` · `Product Type`=`Spread` · `Exchange` `!=` `ASE` |

This needs **two alerts**, because the ALL/ANY choice is alert-wide (`creating-an-alert.md:43-44`)
and one alert cannot mix AND with OR. The split is semantically meaningful rather than
duplicated logic: "a structure I built filled" vs "a listed spread I traded filled". The
`ASE` alert is also the more informative one - it carries the **spread** price and **spread**
quantity (`-1.11`, `1`) instead of per-leg prices and ratio-scaled quantities.

`Synth Status` (Order condition field, status "for a parent synthetic order",
`alerts-reference.md:29`) is an untested alternative discriminator `[U]`; `Exchange` is
verified by the fill data above and is the simpler construction.

**Not adding the `Exchange` condition is a legitimate choice**, and was the one taken here.
The N+1 burst self-groups: three notifications within a second or two, for a structure you
launched, are evidently one parent plus its legs, and the parent is identifiable as the one
carrying the *spread* price. The heuristic degrades only when several structures fill
concurrently - or one fills in multiple clips - since then the bursts interleave and
timestamp proximity no longer attributes legs to parents. Worth revisiting if you ever run
more than one spread at a time; not worth the second alert otherwise.

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
