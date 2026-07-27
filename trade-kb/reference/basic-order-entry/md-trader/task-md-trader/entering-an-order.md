---
title: Entering an order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/task-md-trader/entering-an-order/
---

# Entering an order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/task-md-trader/entering-an-order/)

In MD Trader, you can easily configure an order, and quickly and safely enter the order for an instrument
with a single click.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-ovw1.png)

Before configuring and entering an order, configure the following parameters in MD Trader:

* [Maximum order quantity](../reference-md-trader/md-trader-reference.md#order-local)
* [Default order quantity](../description-md-trader/trading-with-md-trader.md#quantity)
* [Second default order quantity](../description-md-trader/trading-with-md-trader.md#quantity)

To enter an order in MD Trader:

1. Select an account, order type, and order restriction (TIF) in the Order Entry Panel or use the default settings
   for each. An account is *required* for submitting orders on TT.

   You can also use [custom action buttons](configuring-md-trader.md#buttons) to select a native
   order type, TIF, or [TT order type](#custom).
2. Enter an order quantity: Type in a value, use
   your default order quantity, or click one of the quantity buttons. A quantity is *required* for submitting
   orders on TT

   If needed, use the **CLR** button to clear the quantity field to enter a new quantity.
3. Click either the **Bids** or **Asks** column next to a price level to enter the order.

   If desired,
   right-click in the order placement columns to enter an order using your second default order quantity.

## Submitting new orders on hold

Optionally, you can submit new orders as held orders, then resubmit the orders from the Order Book at a later time.
To enable this functionality, right-click on the widget and check the **Show held-order toggle** setting. You can
also make this the default setting to submit all orders on hold. After you click **Save**, the **Hold** button
is shown on the widget.

New orders can be submitted as held orders for the following natively supported order types, which vary by exchange
and product:

* Limit
* Iceberg
* Market to Limit
* Stop Limit
* Stop Market

In addition, new orders for all TT Order Types can be submitted as held orders and resubmitted at a later time.

To submit an order as a held order, click the **Hold** button, then submit the order. The **Hold** button is
highlighted yellow when it’s active. When active, all newly submitted orders are sent to the exchange “on hold” and
appear in the Order Book widget with a status of “Hold” in the **Status** column.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-held-2.png)

## Submitting orders with custom TT order type buttons in MD Trader

When trading, left-click a custom TT order type button to quickly seed an order type with an assigned [template of predefined default order parameters](../../tt-order-types/description-tt-order-types/tt-order-types-overview.md#order-templates) without
displaying the order parameter flyout panel. The button remains active until you de-select it with a left or
right-click (for native order types and TIFs, not for synthetic order types), select a different order type, or have
**Reset order type to Limit after each order** enabled in the MD Trader settings.

**Note**: If the “Default” order parameters are used, meaning no specific template is assigned to the custom TT
order type button, then the order parameter flyout is displayed when you left-click the button.

When you right-click a custom TT order type button, it automatically sets the order type and displays the order
parameter flyout panel. The panel is only displayed when you select a TT order type from the main order type selector,
right-click a custom TT order type button, or click the **edit** button in the Order Entry Panel.

Note Right-click to deselect is not supported for synthetic TT Order Types.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-custom-action-buttons-1.png)

←[Previous PostAdding laser lines to MD Trader](adding-laser-lines-to-md-trader-2.md)

[Next PostManaging orders](managing-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-ovw1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-held-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-custom-action-buttons-1.png
