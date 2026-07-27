---
title: Order Management Algos (OMA) overview
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/order-management-algos-omas/order-management-algos-oma-overview/
---

# Order Management Algos (OMA) overview

> Category: **Algo Trading** · [KB Home](../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/order-management-algos-omas/order-management-algos-oma-overview/)

An Order Management Algo (OMA) is an algo that can take control of and manage one or more orders. When an OMA takes control of an order, it can use its internal logic to manage the order in the market, such as updating the order’s price or quantity. An OMA can also modify one order it manages based on activity on another order it manages, such as canceling or reducing the quantity of one order as another order is filled.

You can use [Existing Order](../../../../adl-kb/reference/trading-blocks/existing-order-block.md) blocks in an [ADL](/adl) algo to create your own custom OMAs. Based on how you want to select the orders for an OMA to manage, you can create the following types of OMAs:

* [Order Book OMAs](#ob-omas), which can be launched for existing orders from the [Order Book](../../order-management/order-book/description-order-book/order-book-overview.md) and [Floating Order Book](../../order-management/floating-order-book/description-floating-order-book/floating-order-book-overview.md) widgets.
* [Order-builder OMAs](#mdt-omas), which can be launched directly from [MD Trader](../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) to create new orders or to take control of existing orders.

## Order Book OMAs

All OMAs can be launched from the [Order Book](../../order-management/order-book/task-order-book/launching-an-oma-in-the-order-book.md) widget. You can simply select the number of orders required by the algo and choose an OMA to manage them. Then you specify the algo’s parameters as desired and launch the OMA directly from the Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-ob-launch-params.png)

1. Selected OMA
2. Parameters defined for the OMA

When you launch the OMA for the selected orders, a new parent order is created and the selected orders are converted to child orders that are managed by the OMA parent order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-ob-parent-child-orders.png)

1. OMA parent order
2. Child orders managed by the OMA parent order

You can also launch an OMA for a single existing order, or multiple existing orders at the same price level, from the [Floating Order Book](../../order-management/floating-order-book/task-floating-order-book/launching-an-oma-in-the-floating-order-book.md) in MD Trader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-ob-algos.png)

1. Select an OMA to apply to the selected orders.
2. Select an OMA to apply to a single order.

The [OCO](https://library.tradingtechnologies.com/trade/oma-oco-public-algo.html) public OMA is an example of an Order Book OMA that can be launched from the Order Book and Floating Order Book widgets.

## MD Trader order-building OMAs

TT also supports OMAs that run in an “order building” mode that lets you dynamically build an OMA order in [MD Trader](../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md). Unlike Order Book OMAs, these OMAs also let you add both existing and new orders to the OMA order. From a single MD Trader widget, you can start the order-building OMA and then select working orders and submit new orders for the OMA to manage. You can also select or add orders across different instruments in different MD Trader instances.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-mdt-launch-overview.png)

When you select an OMA from the MD Trader Order Type dropdown, order-building mode is activated and:,

1. All MD Trader header panels are shaded yellow to indicate that building mode is active.
2. The order builder panel opens for the OMA that tracks the orders added to the OMA order. It also shows the current and maximum numbers of orders that the OMA can accept.
3. If you select an existing order, it is added to the panel, as shown.
4. If you place a new order while in order-builder mode, the new order will be added to the panel and submitted in a held state so it is not active in the market until the algo is launched.
5. After you have specified the minimum number of orders required by the algo, the **Launch algo** button is enabled so you can launch the OMA.

After you launch the OMA, any new orders you added to the OMA order are put into working state and become active in the market.

The [Conditional](https://library.tradingtechnologies.com/trade/oma-conditional-public-algo.html), [OCO 2](https://library.tradingtechnologies.com/trade/oma-oco2-public-algo.html) and [MinVol](https://library.tradingtechnologies.com/trade/oma-minvol-public-algo.html) TT public OMAs are examples of MD Trader order-building OMAs.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-ob-launch-params.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-ob-parent-child-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-launch-ob-algos.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oma-mdt-launch-overview.png
