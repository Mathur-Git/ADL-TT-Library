# Trade Knowledge Base

A complete, offline, cross-referenced mirror of the Trading Technologies **Trade** platform
documentation — 638 pages — plus a hand-authored navigation layer built on top of it.

Purpose: answer Trade-platform questions (order entry, market data, spread trading, algo
operations, risk) accurately from local files, without re-browsing the web.

Built from `https://library.tradingtechnologies.com/docs-category/trade/` · captured **2026-07-27**

**Scope note:** the **Options** subsection (Counterparty Manager, Electronic Eye, Expiration
Manager, Options Chain, Options Risk, RFQ Viewer, QuikStrike, Vol Curve Manager, etc. — 141
pages) is deliberately **excluded** from this mirror. Everything else in Trade is included.

This KB is the sibling of **[adl-kb](../adl-kb/README.md)** — the Algo Design Lab documentation.
Where a Trade-platform page and an ADL block/concept page cover the same ground (e.g. MD Trader
↔ the Instrument block, Order Book ↔ the Order block, Care Orders ↔ Single Order Container),
the two are cross-linked directly.

---

## Start here

Guides are organized around what you're actually trying to do, not around TT's own site
taxonomy (which groups by UI widget rather than by task).

| Guide | Use it when |
|---|---|
| **[Spread Trading & AutoSpreader](guides/spread-trading-autospreader.md)** | Synthetic spread definition, formulas, leg ratios/multipliers, tick sizing, quoting/hedging behavior, AutoSpreader Rules, Aggregator, Hedge Manager. |
| **[Order Types & Execution](guides/order-types-and-execution.md)** | The full order-type catalog (TWAP, Iceberg, With-a-Tick, Bracket, OCO, market-making variants…), MD Trader, Order Ticket, routing rules, and the TT OMS (care orders, bulking, stitching/splitting). |
| **[Market Data & Depth](guides/market-data-and-depth.md)** | Spread Matrix, Depth widget and book imbalance, Time and Sales, Position in Queue, Market/Product Grid. |
| **[Algo Ops](guides/algo-ops.md)** | Running and monitoring a deployed algo: Algo Dashboard vs Autotrader, user-defined variables, Excel/RTD linking, built-in OMA/market-making algos. |
| **[Order Management & Risk](guides/order-management-and-risk.md)** | Position Manager, Fills, Order Book, Alerts, accounts/balances, audit trail. |
| **[Platform & Workspace](guides/platform-and-workspace.md)** | TT Desktop vs browser access, workspaces and widget layout, preferences, platform basics. |
| **[Charts & Analytics](guides/charts-and-analytics.md)** | Chart types, settings, drawing tools, trading from a chart, and the full technical indicator catalog. |
| **[Full Index](INDEX.md)** | All 638 source pages, grouped by TT's own section/subsection structure. |

---

## Layout

```
trade-kb/
├── README.md                 this file
├── INDEX.md                  all 638 pages, grouped by TT's own taxonomy
├── guides/                    hand-authored navigation layer, grouped by workflow
│   ├── spread-trading-autospreader.md
│   ├── order-types-and-execution.md
│   ├── market-data-and-depth.md
│   ├── algo-ops.md
│   ├── order-management-and-risk.md
│   ├── platform-and-workspace.md
│   └── charts-and-analytics.md
└── reference/                 verbatim mirror, TT's own URL/folder structure preserved
    ├── spread-trading/        (67)   basic-order-entry/      (133)
    ├── viewing-market-data/   (54)   algo-trading/            (50)
    ├── order-management/      (84)  tt-oms/                  (38)
    ├── overview/               (70)   analytics/              (142)
```

Every `reference/` page carries YAML front matter (`title`, `category`, `source`) and links back
to its original URL. The `reference/` folder structure mirrors TT's own site taxonomy exactly
(preserving provenance and making re-sync straightforward); the `guides/` layer reorganizes that
same material around actual trading workflows.

---

## Why this KB exists

The [VIX spread tick-granularity project](../adl-kb/README.md) trades the gap between a CFE VX
outright (tick = 0.05) and its exchange-listed calendar spread (tick = 0.01). Reading that
setup in practice means watching **Spread Matrix** and **Depth** market data, understanding how
**AutoSpreader** computes and overrides synthetic tick size, and knowing the exact **order types**
and **routing** available — none of which lives in the ADL docs, which only cover the block
programming layer. This KB fills that gap.

---

## Provenance

Scraped from the official TT help library and converted to Markdown with content preserved
verbatim — including all property tables, field lists, notes and warnings. Images remain as
links to TT's CDN; the diagrams are illustrative, and the surrounding prose carries the
substance.

The `guides/` layer is authored from that source material, not copied from it; every non-obvious
claim links to the reference page that supports it. Cross-links into `adl-kb/` were verified to
resolve; a small number of legacy TT URLs referenced inside page bodies that could not be matched
with full confidence were left as absolute links to the live TT help site (they resolve there via
TT's own redirects).
