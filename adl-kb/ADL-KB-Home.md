# ADL Knowledge Base

A complete, offline, cross-referenced mirror of the Trading Technologies **ADL (Algo Design Lab)**
documentation — 128 pages — plus a hand-authored navigation layer built on top of it.

Purpose: answer ADL questions accurately from local files, without re-browsing the web.

Built from `https://library.tradingtechnologies.com/adl/` · captured **2026-07-23**

This KB is the sibling of **[trade-kb](../trade-kb/Trade-KB-Home.md)** — the Trade platform documentation
(order entry, market data, spread trading, algo operations, risk). ADL covers the block-programming
layer; Trade covers the platform surface an algo runs on top of. Pages that describe the same
concept from each side (MD Trader ↔ Instrument block, Order Book ↔ Order block, Care Orders ↔
Single Order Container, Algo Dashboard/Autotrader ↔ deploying an algo) are cross-linked directly.

---

## Start here

| Guide | Use it when |
|---|---|
| **[Core Semantics](guides/core-semantics.md)** | You need to know *how ADL actually executes* — continuous vs discrete, the freeze rule, propagation order, termination, virtualization, NaN. **Read this first; most ADL bugs live here.** |
| **[Block Catalog](guides/block-catalog.md)** | "Which block does X, what are its ports, what will bite me?" Every block, every category. |
| **[Design Patterns](guides/design-patterns.md)** | "How do I build X?" Recipes mapped to the TT worked examples. |
| **[Formula Reference](guides/formula-reference.md)** | Writing formulas: `#` message fields, `@` block connectors, operators, worked examples, TIF/order-type codes. |
| **[Gotchas & Limits](guides/gotchas-and-limits.md)** | Every hard limit and surprising behaviour, plus a pre-deploy checklist. |
| **[Algo Types](guides/algo-types.md)** | Standard vs OTA vs SOA vs OMA, user-defined variables, deployment, approval, sharing. |
| **[.adl.json Format](../ADL-jsons/ADL-JSON-Format-Spec.md)** ⎋ | You're reading or writing an exported algo **file** — schema, connector-GUID catalog, and the risk/throttle idioms observed in 13 TT production algos. *Different source: derived from the JSON corpus, not from TT's docs.* |

---

## Layout

```
adl-kb/
├── README.md                 this file
├── guides/                   hand-authored navigation layer
│   ├── core-semantics.md     the execution model
│   ├── block-catalog.md      every block + ports + pitfalls
│   ├── design-patterns.md    recipes → worked examples
│   ├── formula-reference.md  Formula Editor
│   ├── gotchas-and-limits.md limits + checklist
│   └── algo-types.md         OTA / SOA / OMA / deployment
└── reference/                verbatim mirror, URL structure preserved
    ├── adl-overview/         concepts, tutorials, advanced topics  (65)
    ├── trading-blocks/       (10)   discrete-blocks/     (14)
    ├── arithmetic-blocks/    (9)    miscellaneous-blocks/ (9)
    ├── logic-blocks/         (7)    group-blocks/        (3)
    ├── virtualized-blocks/   (3)    library-blocks/      (3)
    ├── jump-blocks/          (3)    basic-blocks/        (2)
```

Every `reference/` page carries YAML front matter (`title`, `category`, `source`) and links back to its
original URL. Inter-page links have been rewritten to local relative paths — **1,064 internal links
plus 93 into `trade-kb/`, all resolving**; there are no orphan pages and no dead anchors.

### Navigating: citations run both ways

The `guides/` layer cites the reference pages that support each claim. Every one of those citations
is also **inverted back onto the reference page**, as a line directly under its breadcrumb:

> **Interpreted in:** [Core Semantics § 2. The freeze rule](guides/core-semantics.md#2-the-freeze-rule) · …

So from any reference page you can jump straight to the guide section that interprets it. Where a
page is the section's own field/column reference or a near-sibling, an **Also in this section:** line
does the same job laterally.

**Reference pages deliberately do not link back to this page.** A "home" link on all 128 of them
would make this file a hub joined to everything by nothing more than being the index of it — which
is exactly what the deleted `INDEX.md` did, and it drowns the real structure in the graph view.
Navigate up through the guide that interprets the page instead; that path carries meaning.

---

## The ten rules that matter most

1. **Continuous vs discrete is the central distinction.** Continuous = live streaming values;
   discrete = a pulse at one instant. It decides which blocks you can use.
   → [Core Semantics §1](guides/core-semantics.md#1-two-kinds-of-message)
2. **While a discrete message propagates, all continuous data freezes.** That is what makes a
   fill-time market snapshot coherent. → [§2](guides/core-semantics.md#2-the-freeze-rule)
3. **Never fan out a discrete output.** Execution order is not deterministic — use a **Sequence** block.
   → [§4](guides/core-semantics.md#4-branching-a-discrete-output-is-non-deterministic)
4. **Messages terminate** at Single Order Container, State, Value Accumulator, Discrete Order, Stopwatch,
   Terminal, Alert, and any `reset` port. → [§3](guides/core-semantics.md#termination-blocks)
5. **Actor blocks cannot act inside a Loop.** Drive a **Discrete Order** block off the `loop` port to place
   one order per iteration. → [§6](guides/core-semantics.md#6-the-loop-block-suspends-actors)
6. **Virtualize when each event needs its own independent logic** (per-fill exits). It must have a discrete
   input, must have no continuous outputs, and **needs an Exit block** or instances pile up.
   → [§7](guides/core-semantics.md#7-virtualization)
7. **`NaN` deletes working orders.** Guard every division and depth lookup with **IsNumber**.
   → [§8](guides/core-semantics.md#8-nan-is-contagious-and-destructive)
8. **Order vs Discrete Order vs Single Order Container** is the key design choice: managed / one-shot /
   manage-someone-else's. → [§9](guides/core-semantics.md#9-order-block-vs-discrete-order-block-vs-single-order-container)
9. **`Ignore market state` is off by default** — and a Market State block is useless without it.
   → [§10](guides/core-semantics.md#10-what-pauses-or-cancels-an-algo)
10. **Never encode sequencing as a latency assumption.** TT optimises continuously; such designs break.
    → [§12](guides/core-semantics.md#12-do-not-design-around-assumed-latency)

---

## Quick lookup

**Getting market data** → [Instrument](reference/trading-blocks/instrument-block.md) +
[Field](reference/trading-blocks/field-block.md) (snapshots) or
[Time and Sales](reference/trading-blocks/time-and-sales-block.md) (every trade)

**Submitting orders** → [Order](reference/trading-blocks/order-block.md) (managed) ·
[Discrete Order](reference/trading-blocks/discrete-order-block.md) (one-shot) ·
[Single Order Container](reference/trading-blocks/single-order-container-block.md) (manage existing)

**Reacting to fills** → [MsgInfoExtractor](reference/discrete-blocks/msginfoextractor-block.md) ·
[Value Extractor](reference/discrete-blocks/value-extractor-block.md) (snapshot) ·
[Value Accumulator](reference/discrete-blocks/value-accumulator-block.md) (running total / counter)

**Timing** → [Generator](reference/discrete-blocks/generator-block.md) (clock/trigger) ·
[Stopwatch](reference/miscellaneous-blocks/stopwatch-block.md) (delay) ·
[Time and timers](reference/adl-overview/advanced-concepts/description/time-and-timers-in-tt-adl.md)

**Indicators** → [Analytics](reference/miscellaneous-blocks/analytics-block.md) (OHLCV + ATR, Bollinger,
MACD, SMA/EMA/DEMA/TEMA/WMA, RSI, StdDev, Stochastic — Production environments only)

**Risk** → [Pnl](reference/miscellaneous-blocks/pnl-block.md) ·
[Position Risk](reference/miscellaneous-blocks/position-risk-block.md) ·
[Terminal](reference/miscellaneous-blocks/terminal-block.md)

**Learning path** → [Building your first algo](reference/adl-overview/building-your-first-algo/introduction.md)
(a Scalper, built in four lessons)

---

## Provenance

Scraped from the official TT help library and converted to Markdown with content preserved verbatim —
including all property tables, field lists, notes and warnings. Images remain as links to TT's CDN
(460 referenced; the diagrams are illustrative, and the surrounding prose carries the substance).

The `guides/` layer is authored from that source material, not copied from it; every non-obvious claim
links to the reference page that supports it, and every such citation is mirrored back onto the cited
page as an **Interpreted in:** line.

**Video pages are excluded.** TT's video pages carried only a one-paragraph summary and the embedded
player — no property tables, no field lists — so the video does not survive a text mirror and the
summary duplicates the adjacent description page. 4 were removed here (44 more in `trade-kb`).
