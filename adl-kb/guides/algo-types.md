# Algo Types, Launching & Deployment

What kind of algo you are building determines how it is launched, whether it produces parent fills, and
which blocks are mandatory. Decide this first — it is not easily changed later.

[ADL KB Home](../ADL-KB-Home.md) · [Block Catalog](block-catalog.md) · [Core Semantics](core-semantics.md) · [Patterns](design-patterns.md) · [Gotchas](gotchas-and-limits.md)

---

## The four types

| Type | What makes it one | Launched from | Parent fills? |
|---|---|---|---|
| **Standard algo** | default | Algo Dashboard, Autotrader | n/a |
| **OTA** — Order Ticket Algo | [Instrument](../reference/trading-blocks/instrument-block.md) `Type = Order Instrument` | MD Trader, Order Ticket, Market Grid, Algo Dashboard, Autotrader | **no** — child orders only |
| **SOA** — Synthetic Order Algo | Instrument `Type = Order Instrument` **+** [Number](../reference/basic-blocks/number-block.md) `Variable Type = Order Quantity` **+** the SOA algo setting | MD Trader (like an order type) | **yes** — parent and children |
| **OMA** — Order Management Algo | contains an [Existing Order](../reference/trading-blocks/existing-order-block.md) block | Order Book, Floating Order Book, MD Trader (if *Launchable OMA* is set) | attaches to an existing order |

### Standard algo

Parameters come from user-defined variable blocks and appear automatically in the Algo Dashboard and
Autotrader. The algo runs as a parent order on the Algo Server, submitting child orders to the exchange.
→ [Using ADL algos](../reference/adl-overview/introduction-to-adl/description-introduction-to-adl/using-adl-algos.md)

### OTA — Order Ticket Algo
→ [Order Ticket Algos (OTA)](../reference/adl-overview/advanced-concepts/description/order-ticket-algos-ota.md)

For single-click execution straight off the ladder. Once deployed, the algo's name joins the list of
order types in MD Trader / Order Ticket.

- The instrument follows whatever the ladder is showing.
- Clicking the **bid** column sets Order Side = Buy; the **ask** column sets Sell (with
  [Flip for Sell](../reference/adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) enabled).
- A [Number](../reference/basic-blocks/number-block.md) block with Variable Type `Order Price` or
  `Order Quantity` picks up the clicked price and the ticket quantity. A
  [Bool](../reference/basic-blocks/bool-block.md) block with `OrderSide` picks up the side.
- By default **only child orders show on the ladder**. Enable **`Show algo order on ladder`** in the
  Information Panel → Settings to display the parent too; it appears with order qty and working qty **0**.
- **Fills are generated only for child orders.**

### SOA — Synthetic Order Algo
→ [Synthetic Order Algos (SOA)](../reference/adl-overview/advanced-concepts/description/synthetic-order-algos-soa.md)

Behaves like a genuine TT synthetic order type. Differs from an OTA in three ways:

1. The parent order **always** shows in MD Trader.
2. It **generates fills for the parent order** as well as the children.
3. It **terminates automatically** when the `Order Quantity` Number block reaches **0**.

Requirements: Instrument `Type = Order Instrument`, a Number block with `Variable Type = Order Quantity`,
and the **Synthetic Order Algo (SOA)** setting enabled — which force-enables `Show algo order on ladder`
and locks it on.

On the ladder the parent initially shows working qty `0` and `*` for undisclosed quantity. Child orders at
the parent's price level roll up into the parent's displayed working quantity; children at other levels do
not. Middle-click the order and use the Floating Order Book to see the parent's submitted quantity.

### OMA — Order Management Algo
→ [Existing Order block](../reference/trading-blocks/existing-order-block.md)

Attaches to an order that **already exists** — manual or algo-created.

Mechanism: the Existing Order block emits a discrete message carrying the order key → a
[Single Order Container](../reference/trading-blocks/single-order-container-block.md) reads the key and
takes control.

- **Attaching does not disturb queue priority**, but the OMA may then modify or delete the order.
- An OMA can be applied to another OMA's child order.
- Applied from the Order Book widget after deployment.
- Set **`Launchable OMA (as OTA)`** to allow launching from MD Trader in order-builder mode; the
  Discrete Order block's `Clone incoming order` property supports this.
- To test without a real manual order, use a [Funnel](../reference/discrete-blocks/funnel-block.md) plus a
  switchable "test order" branch into the SOC →
  [Testing OMA logic](../reference/adl-overview/advanced-concepts/task/testing-oma-logic.md).

---

## Algo settings (Information Panel → Settings)

→ [ADL Designer](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/adl-designer.md)

| Setting | Effect |
|---|---|
| **Show algo order on ladder** | display the OTA/SOA parent synthetic order in MD Trader |
| **Ignore market state** | keep running when a market leaves its trading session. **Off by default.** Required for pre-open logic and for [Market State](../reference/trading-blocks/market-state-block.md) blocks to be useful |
| **Synthetic Order Algo (SOA)** | mark the algo as an SOA |
| **Launchable OMA (as OTA)** | allow an OMA to launch from MD Trader in order-builder mode |

Toolbar also carries the **Order Side** selector (Buy/Sell) for Flip-for-Sell algos, the compile controls
(auto-compile on/off, manual compile), bookmarks, and run/pause/stop.
→ [ADL Designer toolbar](../reference/adl-overview/adl-basic-concepts/reference-adl-basic-concepts/adl-designer-toolbar.md)

---

## User-defined variables

→ [User-defined variables](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/user-defined-variables.md)

Only four block types can become user-defined variables:

- [Bool](../reference/basic-blocks/bool-block.md)
- [Number](../reference/basic-blocks/number-block.md)
- [Instrument](../reference/trading-blocks/instrument-block.md)
- [Price](../reference/trading-blocks/price-block.md)

They surface automatically as algo parameters in the Algo Dashboard and Autotrader, and can be RTD-linked
to Excel via Autotrader.
→ [Linking Excel data](../reference/adl-overview/advanced-concepts/description/linking-excel-data-to-the-algo-dashboard.md)

Notes:
- A user-defined **Instrument cannot be changed while the algo is running**.
- Editing values in the **Variables** tab during testing does **not** change the block's default.
- A **`Side`** variable appears automatically whenever any block has Flip for Sell enabled.
- Client-disconnect behaviour (continue / pause / cancel) appears automatically for every algo.

**Exported values** are different: right-click any numeric or Boolean **output port** → *Export value* to
show it as a live column in the Algo Dashboard. Not supported inside virtualized blocks.
→ [Export block output values](../reference/adl-overview/advanced-concepts/description/export-block-output-values.md) ·
→ [Exporting block outputs](../reference/adl-overview/advanced-concepts/task/exporting-block-outputs.md)

---

## Deployment and approval

→ [Algo deployment and approvals](../reference/adl-overview/adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md)

1. **Save** (File → Save / Save As) — algos are tied to your TT login and open from any machine.
2. **Deploy** (File → Deploy) — uploads the compiled algo to the Algo Server and makes it visible in
   Trade widgets. It stays available until undeployed.
3. **Approval**, if your firm enables *Requires Permission to Run Own Algos*: File → **Request Approval**,
   selecting each company that must approve. This deploys to **Simulation** immediately; Live use waits on
   approval. Refresh the Algo Dashboard algo list afterwards.
4. **Undeploy** removes it from all widgets.

> If an administrator turns on the approval requirement **after** you have deployed, your algos are
> **removed from Trade widgets** until each one is re-approved.

**Import/export** as JSON (File → Import / Export) for backup or hand-off. TT Public Algos (e.g. OCO) can
be opened read-only and **Save As**'d to create an editable copy.
→ [Accessing your algos](../reference/adl-overview/adl-basic-concepts/task-adl-basic-concepts/accessing-your-algos.md)

---

## Sharing

→ [Algo sharing](../reference/adl-overview/advanced-concepts/description/algo-sharing.md) ·
→ [Managing shared algos](../reference/adl-overview/advanced-concepts/task/managing-shared-algos.md)

Two independent permissions:

- **View in ADL (but not edit)** — read-only access to the canvas.
- **Launch** — run the algo in TT, without ADL access.

Shared algos appear in the recipient's Algo Dashboard automatically; OTAs and SOAs also appear in the
public algo list in MD Trader.

Restrictions: you need the recipient's **email address**; an email registered across multiple companies
resolves to the first one it was set up under (their admin must remove it from TT Setup first); and a
recipient who needs approval to run algos requires **Read** permission from you.

---

## After launch

The algo becomes a **parent order** on the Algo Server; its child orders go to the exchange. Monitor both
through the Order Book, Floating Order Book, Fills and Audit Trail widgets.

Use the [Order](../reference/trading-blocks/order-block.md) / [Discrete Order](../reference/trading-blocks/discrete-order-block.md)
**`Order Tag`** property to stamp child orders with text: the parent's `TextTT` is concatenated with the
tag, giving values like `MM 3x10:OT123` for filtering in the Fills widget. **`Order Color`** tints the
block's orders in MD Trader and Order Book.

Check the [Algo Server limits](gotchas-and-limits.md#algo-server-capacity) if you intend to run many
instances at once.
