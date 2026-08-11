---
title: Synthetic Order Algos (SOA)
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/synthetic-order-algos-soa/
---

# Synthetic Order Algos (SOA)

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/synthetic-order-algos-soa/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § SOA — Synthetic Order Algo](../../../../guides/algo-types.md#soa-synthetic-order-algo)

A Synthetic Order Algo (SOA) in ADL is similar to an [Order Ticket Algo (OTA)](order-ticket-algos-ota.md) in that it’s launched at order entry like a TT Order Type. However, an SOA differs from an OTA in three significant ways:

* A Synthetic Order Algo automatically shows the parent order in MD Trader.
* An SOA generates fills for the parent order in addition to the fills for the child orders.
* When an SOA is fully-filled (when the block with its type set to **Order Quantity** reaches 0), the algo is automatically terminated.

Like an OTA, a Synthetic Order Algo requires its [Instrument](../../../trading-blocks/instrument-block.md) block’s **Type** property to be set to **Order Instrument**. Additionally, its [Number](../../../basic-blocks/number-block.md) block’s **Variable Type** property must be set to **Order Quantity**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-order-instrument-number.png)

When the SOA is deployed, it also appears in the list of order type values, as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-widget-order-types.png)

Both the parent and child orders submitted by an SOA are displayed in the [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-display.md) widget. If the algo creator enables **Synthetic Algo Order (SOA)** setting in ADL, the **Show algo order on ladder** setting is automatically checked (and cannot be disabled).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-show-algo-setting.png)

### Viewing SOA orders in MD Trader

When a Synthetic Order Algo order is submitted, the order initially displays 0 for the working quantity of the parent order and \* for the undisclosed quantity. Child orders appear as normal working orders. If a child order is placed at the same price level as the parent SOA order, the working quantity reflects the total working quantity of all child order placed at that level. If the child orders are placed at a different price level, the parent order working quantity continues to display 0.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-widget-orders-in-mdt.png)

(1) SOA parent synthetic order with child exchange orders at the same price level
  
(2) SOA parent synthetic order
  
(3) SOA child exchange orders at a different price level

**Note**: To see the submitted quantity of the parent order, middle-click the order to display the [Floating Order Book](../../../../../trade-kb/reference/order-management/floating-order-book/description-floating-order-book/floating-order-book-overview.md).

**Note**: If an SOA delays submitting its first child order, the working quantity of the SOA parent order will remain 0 until the first child order is submitted.

←[Previous PostOrder Ticket Algos (OTA)](order-ticket-algos-ota.md)

[Next PostExport block output values](export-block-output-values.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-order-instrument-number.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-widget-order-types.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-show-algo-setting.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-soa-widget-orders-in-mdt.png
