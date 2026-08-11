---
title: Order Ticket Algos (OTA)
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-ticket-algos-ota/
---

# Order Ticket Algos (OTA)

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-ticket-algos-ota/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § OTA — Order Ticket Algo](../../../../guides/algo-types.md#ota-order-ticket-algo)

An algorithm in ADL can be designed as an Order Ticket Algo (OTA), which means that the algorithm can be launched directly from either [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-display.md) or [Order Ticket](../../../../../trade-kb/reference/basic-order-entry/order-ticket/description-order-ticket/order-ticket-overview.md) widget as you would any other type of order. The OTA functionality is especially useful for strategies that require a fast “single-click” style of execution.

Note: Fills are generated only for the OTA child orders, not for the OTA parent order.

An algo becomes an OTA when its [Instrument](../../../trading-blocks/instrument-block.md) block’s **Type** property is set to **Order Instrument**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-order-instrument.png)

When an OTA is created and deployed, the name of the algo is added to the list of order type values, as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adv-ota-widget-order-types.png)

### Viewing OTA orders in MD Trader

By default, only the child orders submitted by an OTA are displayed in the [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-display.md) widget. An OTA can optionally display the parent synthetic order in the MD Trader widget if the OTA algo creator enables the **Show algo order on ladder** setting.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-show-algo-setting.png)

The order quantity and working quantity are both set to **0** to indicate the order is an OTA parent synthetic order. Child orders appear as normal working orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-widget-orders-in-mdt.png)

(1) OTA parent synthetic order
  
(2) OTA child order

←[Previous PostLeave orders on cancel or pause](leave-orders-on-cancel-or-pause.md)

[Next PostSynthetic Order Algos (SOA)](synthetic-order-algos-soa.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-order-instrument.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adv-ota-widget-order-types.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-show-algo-setting.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-ota-widget-orders-in-mdt.png
