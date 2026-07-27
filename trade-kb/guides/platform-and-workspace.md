# Platform & Workspace

How the TT platform itself is put together — access methods, workspaces, widgets, and the global
preferences that govern them. This is the layer underneath everything else in this KB.

[KB Home](../README.md) · [Full Index](../INDEX.md) · [Spread Trading / Autospreader](spread-trading-autospreader.md) ·
[Order Types & Execution](order-types-and-execution.md) · [Market Data & Depth](market-data-and-depth.md) ·
[Algo Ops](algo-ops.md) · [Order Management & Risk](order-management-and-risk.md) ·
**Platform & Workspace** (self) · [Charts & Analytics](charts-and-analytics.md)

---

## TT Desktop vs browser access vs mobile

TT is a SaaS platform — there's no server-side install, and every front end (browser, TT Desktop,
mobile) hits the same back end, same login, same orders/fills/positions.
→ [TT Overview](../reference/overview/tt-platform/description-tt-platform/tt-overview.md)

| | Browser access | TT Desktop | TT Mobile |
|---|---|---|---|
| Install | None — go to `trade.tt` | One-time local install (`TTSetup.msi`) | App install |
| Multi-monitor | One browser window per workspace | Yes — parent + child windows across monitors | No |
| Performance | Standard | Highest — multi-processor design, faster price consumption | — |
| Typical use | Anywhere with a browser | Dedicated trading desks | View only |

- Browser: [Browser Access Overview](../reference/overview/browser-access/description-browser-access/browser-access-overview.md) ·
  [Platform requirements](../reference/overview/browser-access/description-browser-access/platform-requirements.md) —
  latest two versions of Chrome, Firefox, or Edge (IE no longer supported); 4GB RAM min; port 443 HTTPS
  egress to the TT domain (not an IP range); Excel integration additionally needs DNS access to
  `localhost-tradingtechnologies.com:8181`.
- TT Desktop: [TT Desktop overview](../reference/overview/tt-desktop/description-tt-desktop/tt-desktop-overview.md) ·
  [Platform requirements](../reference/overview/tt-desktop/description-tt-desktop/tt-desktop-platform-requirements.md) —
  Core i7 (7700-series+), 8GB RAM, dedicated GPU recommended; Windows + .NET 3.5+; same port-443
  network rule.
  [Downloading and installing](../reference/overview/tt-desktop/task-tt-desktop/downloading-and-installing-tt-desktop.md) —
  download from a logged-in browser session or `trade.tt/desktop/download`; a separate
  `TTUatSetup.msi` exists for the UAT environment.
  [FAQ](../reference/overview/tt-desktop/reference-tt-desktop/frequently-asked-questions-faq.md) —
  no static/offline version exists; the front-end code is re-downloaded into memory on every login
  and discarded on close; deployable via SCCM but without version control.
- Compare with [ADL's own platform requirements](../../adl-kb/reference/adl-overview/introduction-to-adl/description-introduction-to-adl/tt-platform-requirements.md)
  and [ADL and TT Mobile](../../adl-kb/reference/adl-overview/advanced-concepts/description/adl-and-tt-mobile.md)
  (TT Mobile can view running algo instances but cannot launch them).

Logging in: [Logging in to TT](../reference/overview/browser-access/task-browser-access/logging-in-to-tt.md) ·
[Logging in to TT Desktop](../reference/overview/tt-desktop/task-tt-desktop/logging-in-to-tt-desktop.md).
Both enforce an admin-configured idle timeout and a concurrent-session limit. If 2FA is enabled
company-wide it triggers on first browser login. → [Two-factor authentication](../reference/overview/tt-platform/task-tt-platform/configuring-two-factor-authentication.md)

### Session status

Every front end shows a session status indicator (green/connected, red/disconnected, yellow/degraded)
in the menu bar; clicking it opens a details screen (Authentication, Live Data Connection, Market Data,
IP restriction, Display, Software Version). Browser sessions should be refreshed periodically since the
latest code loads dynamically on refresh, whereas TT Desktop shows an explicit version number and flags
unsupported versions.
→ [Session Status (browser)](../reference/overview/browser-access/description-browser-access/session-status-2.md) ·
[Session Status (TT Desktop)](../reference/overview/tt-desktop/description-tt-desktop/session-status.md)

---

## Workspaces & multi-window layout

A **workspace** is one or more **windows**, each populated with **widgets**. Every workspace starts
with a single **Main** window; you can add more to dedicate windows to markets, product groups, or
accounts, or simply to extend usable screen space beyond one monitor.
→ [Workspaces (browser)](../reference/overview/browser-access/description-browser-access/workspaces.md) ·
[Workspaces in TT Desktop](../reference/overview/tt-desktop/description-tt-desktop/workspaces-in-tt-desktop.md) ·
[Workspace Windows Overview](../reference/overview/workspace-windows/description-workspace-windows/workspace-windows-overview.md)

- **Parent (main) window** — owns workspace-level actions (File/Edit menus, Windows selector, Message
  Center, Lock icon) and manages all child windows. Closing it exits the session.
- **Child windows** — created on demand, same titlebar minus the workspace-management controls.
- TT Desktop is purpose-built for spreading windows across physical monitors; browser workspaces switch
  windows within one browser tab via a drop-down or **Ctrl+*window-number***.

**Creating/opening/saving:**
[Creating and opening a workspace (browser)](../reference/overview/browser-access/task-browser-access/creating-and-opening-a-workspace.md) ·
[Creating and opening workspaces in TT Desktop](../reference/overview/tt-desktop/task-tt-desktop/creating-and-opening-workspaces-in-tt-desktop.md).
Browser workspaces are managed from the **Workspace Management** home page (**Launch Workspaces** +
admin-only **Manage Templates**); TT Desktop workspaces are managed from the parent window's **File**
menu (New/Open/Save/Save As/Rename/Delete).

**Multi-window management:**
[Managing multi-window workspaces (browser)](../reference/overview/browser-access/task-browser-access/managing-multi-window-workspaces.md) ·
[Managing a multi-monitor workspace (TT Desktop)](../reference/overview/tt-desktop/task-tt-desktop/managing-a-multi-monitor-workspace.md) —
add a window, set a default, rename/delete, send widgets between windows, drag windows to a different
monitor.

**Import/export:** workspaces export as a single `.tws` file for backup or sharing; importing requires
a browser refresh afterward, and unsupported widgets/features get silently filtered out on import.
→ [Importing/exporting (browser)](../reference/overview/browser-access/task-browser-access/importing-and-exporting-workspaces-2.md) ·
[Importing/exporting (TT Desktop)](../reference/overview/tt-desktop/task-tt-desktop/importing-and-exporting-workspaces.md)

**Templates** (admin-managed, browser only): share a workspace as a template so it appears under
**Manage Templates** for the whole company; admins can rename, delete, or copy a template to new users.
→ [Managing templates](../reference/overview/browser-access/task-browser-access/managing-templates.md)

**Locking a workspace:** "Lock all" freezes every action; "Lock order entry only" still allows
rearranging/opening widgets but blocks order submission. Unlock via the lock icon or **Ctrl+R**.
→ [Locking a workspace](../reference/overview/workspace-windows/task-workspace-windows/locking-a-workspace.md)

**Changing trading environment** (e.g. Simulation ↔ Live) is done from **Edit → Change Environment…**
on the workspace menu bar; unsaved changes prompt a save-first dialog.
→ [Changing trading environments](../reference/overview/workspace-windows/task-workspace-windows/changing-trading-environments.md)

### Finding instruments

- **Search box** in the title bar — free-text/contextual search (exchange, product, symbol, keyword);
  hover a result to see which widgets are launchable for it.
  → [Search overview](../reference/overview/workspace-windows/description-workspace-windows/search-overview.md) ·
  [Searching for an instrument](../reference/overview/workspace-windows/task-workspace-windows/searching-for-an-instrument.md)
- **Market Explorer** — structured Basic mode (Exchange/Type/Product/Instrument/Widget) or Advanced
  mode (adds Family/Term/Spread Type/Strike/Call-Put) for options, exchange-defined spreads, and
  strategies; supports drag-and-drop of found instruments straight onto open widgets. **Auto Roll**
  (Basic mode) automatically rolls an outright future or exchange-listed spread at expiry — not
  supported for exchange-listed strategies, non-monthly-expiry spreads, or LME_NTP products.
  → [Market Explorer overview](../reference/overview/workspace-windows/description-workspace-windows/market-explorer-overview.md) ·
  [Finding an instrument in Market Explorer](../reference/overview/workspace-windows/task-workspace-windows/finding-an-instrument-in-market-explorer.md)
- Selecting a new instrument can trigger a **Market Data Agreement** prompt the first time; accepting
  it records the agreement under **Setup → Users → Agreements**.

---

## Widgets

Widgets are the functional building blocks of a workspace — market data grids, order entry, fills,
charts, algo control, etc. Full catalog:
[Available Widgets](../reference/overview/widgets/description-widgets/available-widgets.md)
(Account List, Aggregator, Alert Manager, Algo Dashboard, Autospreader/Autotrader/Autospreader Rules,
Blocktrader, Chart, Depth, Fills, Hedge Manager, Market Grid, MD Trader, Options Chain/Risk/Trade
Monitor, Orders and Fills, Order Book, Positions, Position Manager, RFQ Viewer, Spread Matrix, Strategy
Creation, Template Manager, Time & Sales, Trader Analytics, Vol Curve Manager, Watchlist, and more).

Opening a widget: from the **Widgets** menu, from Search, from Market Explorer, or launched from
another (linked) widget. Widgets that accept an instrument at open time include MD Trader, Market
Grid, Chart, Blocktrader, Autospreader (Create Spread), and Spread Matrix.
→ [Widgets Overview](../reference/overview/widgets/description-widgets/widgets-overview.md) ·
[Opening a widget](../reference/overview/widgets/task-widgets/opening-a-widget.md)

**Widgets menu:** categorized (Market Views, Order Management, Automation, Options, Miscellaneous) plus
a **Favorites** section you curate — favorites also control which widget icons appear as quick-launch
options in search results, and in what order.
→ [Widgets menu](../reference/overview/widgets/description-widgets/widgets-menu.md) ·
[Organizing the Widgets menu](../reference/overview/widgets/task-widgets/organizing-the-widgets-menu.md)

**Tabs:** Market Grid, Order Book, Fills, and other widgets support tabs so one widget instance can show
several instruments/filters. Tabs can be reordered by drag, dragged out to spawn a new widget, colored,
renamed, copied, removed, or organized into extra rows.
→ [Managing tabs](../reference/overview/widgets/task-widgets/managing-tabs.md)

**Widget groups:** combine two or more widgets under one titlebar, managed as a single object. Within a
group, a "parent" widget (e.g. Market Grid) can drive the instrument shown in child widgets (MD Trader,
Time & Sales) — clicking a market-data cell updates the whole group. Frequently-used groups can be
saved as a reusable **custom widget**, which then appears in the Widgets menu and (optionally) in
search results; instruments are *not* saved with a custom widget, so it stays reusable.
→ [Widget Groups](../reference/overview/widgets/description-widgets/widget-groups.md) ·
[Working with widget groups](../reference/overview/widgets/task-widgets/working-with-widget-groups.md)

**Context menu** (right-click a widget titlebar): create/save group widget, clone, rename, always-on-top,
send to another window, contact support, zoom, and per-widget **Settings**.
→ [Widgets context menus](../reference/overview/widgets/description-widgets/widgets-context-menus.md)

**Customizing a widget:** **Settings** (from the context menu) exposes content/behavior/appearance
options; a **Defaults** section lets you push changes to all future widgets of that type or to every
currently-open widget of the same type. Several widgets (Chart, Depth, Fills, Market Grid, MD Trader,
Options widgets, Order Book, RFQ Viewer, Spread Matrix, Time and Sales, Trader Analytics) support custom
cell/column colors.
→ [Customizing widget settings](../reference/overview/widgets/task-widgets/customizing-widget-settings.md)

**Grid columns:** resize individually or "Fit all columns to content"; choose visible columns, bold,
and alignment via **Edit columns**; filter any filterable column (including custom filter values for
text/account/ID columns); Date/Time filters support Approx/Before/After/Between modifiers.
→ [Configuring widget columns](../reference/overview/widgets/task-widgets/configuring-widget-columns.md)

**Other widget mechanics:**
- Zoom a widget 50–150% (scales contents or resizes the widget depending on type).
  → [Zooming the view in or out](../reference/overview/widgets/task-widgets/zooming-the-view-in-or-out.md)
- Drag-and-drop instruments between grid-based widgets (Market Grid, Order Book, Fills, Audit Trail,
  Watch List, Options Trade Monitor, RFQ Viewer as sources; Market Grid, MD Trader, Chart, Watch List,
  Strategy Creation, Block Trader, Time and Sales, Autospreader/Aggregator Leg Builder as drop targets).
  → [Drag-and-drop instruments between widgets](../reference/overview/widgets/task-widgets/drag-and-drop-instruments-between-widgets.md)
- Copy an entire row (left-click) or a single cell (**Alt+left-click** then **Ctrl+C**, or
  **Alt+right-click → Copy**) out of grid widgets like Order Book, Orders and Fills, Fills, Audit Trail.
  → [Copying order data](../reference/overview/widgets/task-widgets/copying-order-data.md)
- Every widget has a titlebar **?** help icon opening context-specific help.
  → [Widget Help](../reference/overview/widgets/description-widgets/widget-help.md)
- **Feedback widget**: right-click a titlebar → **Contact support…**, or **? Support → Send Feedback**
  for a whole-workspace screenshot. Optionally attach a screenshot + metadata (account, username,
  environment), hide/highlight regions of it, or send feedback tied to selected Fills records.
  → [Feedback widget](../reference/overview/widgets/description-widgets/feedback-widget.md) ·
  [Reporting an incident or sending feedback](../reference/overview/widgets/task-widgets/reporting-an-incident-or-sending-feedback.md)

---

## Preferences

Global preferences apply to every widget/workspace under your login unless a widget's local Settings
override them. Open via **Edit → Preferences**.
→ [Preferences Overview](../reference/overview/preferences/description-preferences/preferences-overview.md)

| Tab | Covers |
|---|---|
| [General](../reference/overview/preferences/description-preferences/general-preferences.md) | Color theme, language, background, tooltips, product symbology (Exchange / Exchange(Bloomberg) / Bloomberg(Exchange)), spread-leg display, titlebar clock, scrollbars, high-res display support, price/quantity display (rounding, decimals, thousands separator, market depth level), energy quantity mode (Contracts vs Flow), local instrument-data caching |
| [Accounts](../reference/overview/preferences/description-preferences/accounts-preferences.md) | Which accounts you see (assigned-to-me vs all, admin only); Routable Accounts view by Account/Exchange/RFQ; account aliasing; RFQ routing-account assignment (one default + per-exchange overrides) |
| [Orders](../reference/overview/preferences/description-preferences/orders-preferences.md) | Default order-entry widget (MD Trader vs Order Ticket), account retention, PIQ, staged-order alerts, order confirmations (Cancel All, qty threshold, RFQ), Floating Order Book columns and launch method |
| [Positions](../reference/overview/preferences/description-preferences/positions-preferences.md) | Show/hide spread & strategy parent positions; show/hide synthetic Autospreader positions |
| [Options](../reference/overview/preferences/description-preferences/options-preferences.md) | Decimal precision for Greeks/options-risk columns; expiries shown on Options Chain launch |
| [Fills](../reference/overview/preferences/description-preferences/fills-preferences.md) | Fill Alerts widget, desktop notifications (full/partial), partial-fill conflation window, CurrentUser-only notification |
| [Algos & Autospreader](../reference/overview/preferences/description-preferences/algos-autospreader-preferences.md) | See below — **relevant to running the strategies documented elsewhere in this KB** |
| [Sounds](../reference/overview/preferences/description-preferences/sounds-preferences.md) | Sound alerts for connection state, orders (manual vs algo-submitted), fills, staged-order events, and **failed algo** |
| [Hotkeys](../reference/overview/preferences/description-preferences/hotkeys-preferences.md) | Global, order-type, and per-widget keyboard shortcuts (see below) |

### Algos & Autospreader preferences (load-bearing for automated strategies)

| Preference | Effect |
|---|---|
| Share newly created Aggregator/Autospreader configurations | Defaults new synthetic spreads to shared-with-company |
| **Algo disconnect action** | What happens to ADL/algo orders if the *client* (not the exchange) disconnects: **Leave** (keep working, Algo Server keeps managing), **Pause**, or **Cancel** (child behavior depends on each Order block's own config) |
| **Autospreader disconnect action** | Same, for Autospreader: **Leave** or **Cancel** (canceling cancels quote orders but leaves hedge orders working) |
| Auto-launch OMA algos | Whether order-builder OMAs (e.g. OCO 2) launch automatically once the minimum required orders are added; overridable per OMA template |
| Per-market Account selection for ADL algos | Lets a multi-leg algo use a single entered account across all legs |

→ [Algos & Autospreader Preferences](../reference/overview/preferences/description-preferences/algos-autospreader-preferences.md).
These disconnect-action settings only govern client-to-TT connectivity — exchange connection loss is
handled independently by each Order block. Cross-reference against
[ADL algo server limits](../../adl-kb/reference/adl-overview/introduction-to-adl/reference-introduction-to-adl/algo-server-limits.md)
for what a Stopwatch/State/recovery scenario looks like server-side.

### Hotkeys — high-value defaults

Hotkeys are user-level (apply across all workspaces), configured on the **Hotkeys** tab.
→ [Hotkeys Preferences](../reference/overview/preferences/description-preferences/hotkeys-preferences.md)

| Scope | Example | Default key |
|---|---|---|
| Global | Save workspace | Ctrl+S |
| Global | Focus Search box | `/` |
| Global | Switch window | Ctrl+1‑9 |
| Order type | Select Market / Limit / Iceberg | Ctrl+M / Ctrl+L / Ctrl+I |
| MD Trader | Join the Bid / Offer | F4 / F9 |
| MD Trader | Cancel working Buy / Sell orders | F5 / F8 |
| Order Book | Cancel selected order(s) | Delete |
| Order Book | Algo Dashboard | Alt+A |

Restrictions: single alpha/numeric keys can't be assigned as standalone hotkeys except in MD Trader
keyboard-trading mode; a fixed list of keys (Spacebar, Esc, Tab, Ctrl, Alt, F12, arrows, etc.) is
reserved and cannot be reassigned; hotkeys must be unique per widget, not globally.

---

## Accounts & platform basics (Pro, mock trading, UAT)

### TT accounts

Creating an account, joining a company, and account settings are the on-ramp to everything else in
this KB.
→ [TT Accounts](../reference/overview/tt-platform/description-tt-platform/tt-accounts.md) ·
[Creating a TT account](../reference/overview/tt-platform/task-tt-platform/creating-a-tt-account.md) ·
[Joining a company](../reference/overview/tt-platform/task-tt-platform/joining-a-company.md) ·
[Editing a TT account](../reference/overview/tt-platform/task-tt-platform/editing-a-tt-account.md)

- A directly-billed / trial account gets a trial period on ASX, B3, CFE, CME, Coinbase, and ICE.
- Trial/directly-billed users manage billing (Profile, Subscription, Agreements, Payment, Invoices) via
  **Setup** in the TT menu bar; all users manage Profile/Security/History via **Account Settings**
  (click your username in the title bar, or **File → About… → Account Settings**).
- **Joining a company** replaces trial/demo access with production access — accepting a company
  invitation gives up TT Demo environment access. Failed logins lock out after 5 attempts.
- Security: [Changing your password](../reference/overview/tt-platform/task-tt-platform/changing-your-password.md) ·
  [Configuring two-factor authentication](../reference/overview/tt-platform/task-tt-platform/configuring-two-factor-authentication.md) —
  2FA is **mandatory** for Production access (Google Authenticator/authenticator apps preferred, email
  next, SMS discouraged); without it, Production access is blocked entirely.
- Support: [Accessing Support](../reference/overview/tt-platform/task-tt-platform/accessing-support.md) —
  TT Service Portal for Incidents/Requests, case export (PDF/Excel/CSV), and filtering; also reachable
  from the Customer Portal [Home Page](../reference/overview/browser-access/description-browser-access/home-page.md),
  which is the landing page after login and links to Workspace Management, Trade, ADL, Monitor, Setup,
  Trade Surveillance, and Inbox.

### TT Pro vs TT Standard

Trade mode is set by a company admin and gates a large slice of TT's automation surface.
→ [TT Pro Advanced Features](../reference/overview/tt-platform/description-tt-platform/tt-pro-advanced-features.md)

| Capability | TT Pro | TT Standard |
|---|---|---|
| MD Trader, Market Grid, Chart, Time & Sales, Order Book, Fills, Positions, Audit Trail, Trader Analytics, Orders and Fills | Yes | Yes |
| Spread Matrix | Yes | Yes (no Autospreader/custom spread building) |
| **Autospreader, Autospreader Rules, Autotrader, Algo Dashboard, Aggregator, Hedge Manager, ADL** | **Yes** | **No** |
| Options widgets, Strategy Creation, RFQ Viewer, Account List, Blocktrader, Alert Manager/Viewer, Position Manager | Yes | Yes |

**This is the gate that matters for the strategies in this KB**: ADL, Autospreader, Autotrader, and the
Algo Dashboard all require TT Pro. TT Standard (View-only) additionally cannot route orders at all in
any environment. Going Pro changes your billing rate for the month it's enabled.

### Mock trading and UAT — the two pre-production environments

| | Mock trading | UAT (Certification) |
|---|---|---|
| URL | `mock.trade.tt` | `uat.trade.tt` |
| Purpose | Exchange-mandated testing of new products/features, outside production hours, on production connectivity | Pre-release TT functionality testing against exchange certification environments |
| Workspaces | Separate from Live/Simulation; import/export required to reuse | Separate from Live/Simulation; import/export required to reuse |
| Banner | "Mock Session" | "Certification Session" |
| Access | TTID login; admin grants access | Admin grants per-user via Setup **Environments** tab; also reachable via REST/.NET SDK/CORE SDK/FIX with app-key auth |

→ [Mock Trading Support](../reference/overview/tt-platform/description-tt-platform/mock-trading-support.md) ·
[User Acceptance Testing (UAT) Environment](../reference/overview/tt-platform/description-tt-platform/user-acceptance-testing-uat-environment.md)

**Unsupported in mock trading**: FIX Adapter, Autospreader, ADL and Algo Dashboard, Position Transfer,
Volume at Price (VAP), TT AOTC, Charts, Position Manager, SOD/manual-fill publishing, Staged Orders.
This makes mock trading unusable for testing ADL-based spread strategies directly — use **UAT** for
that instead, since UAT does support the full functional surface (it's exchange certification
environments, not a feature-stripped sandbox). Both environments filter out unsupported widgets/features
automatically when you import a Live/Simulation workspace.

Setup changes needed only for a mock session (e.g. DR-site IP/port) must be made in **Setup in Live**,
reached via **File → Open user setup** while logged in to `mock.trade.tt`; revert manually afterward if
not wanted permanently.

Compare against [ADL's Algo server limits](../../adl-kb/reference/adl-overview/introduction-to-adl/reference-introduction-to-adl/algo-server-limits.md)
for the 200-msg/sec and 25-instance caps that apply specifically to **UAT and Simulation** (not
production) — those limits live in the ADL guide, not here, but they bind on whichever
non-production environment you actually test in.

### Simulation vs Live

Distinct from Mock/UAT: **Simulation** connects to real exchange price feeds but routes orders to TT's
internal matching engine (never the exchange) — used for strategy testing, training, and API
certification. **Live** connects to the real exchange matching engine. Switch between them from
**Edit → Change Environment…** on the workspace menu bar (see Workspaces section above).
→ [Changing trading environments](../reference/overview/workspace-windows/task-workspace-windows/changing-trading-environments.md)
