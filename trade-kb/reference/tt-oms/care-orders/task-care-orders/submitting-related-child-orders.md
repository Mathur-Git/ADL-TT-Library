---
title: Submitting related child orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/submitting-related-child-orders/
---

# Submitting related child orders

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/submitting-related-child-orders/)

The owner who claimed the care order can enter related child orders to fill the parent order. Child orders are sent
to the exchange based on the total quantity, price and position of the parent care order, and can be submitted in
the same account or different accounts.

Child orders can be submitted simultaneously or at different times, allowing the staged
order to be worked based on market conditions. The owner can submit child orders using TT order types or algos in
addition to the natively supported order types and TIFs. Native order types and TIFs vary by exchange.

When submitting a child order for a claimed care order, the owner *cannot*:

* Reverse the Buy/Sell direction of the order.
* Exceed the parent order quantity. However, the related child order quantity can be increased as long as it
  doesn’t exceed the parent order quantity.
* Change the instrument specified in the order.

Child orders can be submitted using the following methods:

* [Submitting child orders using the Order Ticket or MD Trader](#otmd)
* [Submitting child orders using the Execute button](#execute)
* [Submitting child orders using the staged order alert](#staged)
* [Submitting child orders with a clearing account override](#clearing)
* [Submitting multiple child orders with the same algo](#algo)

## Submitting child orders using the Order Ticket or MD Trader

Left-clicking the **B/S** button on a parent care order in the Order Book launches either an Order
Ticket or MD Trader
based on the **Orders | Floating order entry style** setting in [Orders Preferences](../../../overview/preferences/description-preferences/orders-preferences.md).

Right-clicking the **B/S** button on a
parent care order in the Order Book launches an order entry widget of the opposite style defined in the Orders
Preferences. For
example, if **Order Ticket** is set as the preferred left-click order entry style, a right-click
will launch an MD Trader widget seeded with the staged order details.

### Submitting child orders using the Order Ticket

1. Select the care order in the Order Book.
2. Depending on the **Floating order entry style** setting in [Orders
   Preferences](../../../overview/preferences/description-preferences/orders-preferences.md),
   either left-click or right-click the **B (Buy)** or **S (Sell)** button in the
   **B/S** column for the care order.

   The Order Ticket opens seeded with the parent care order parameters and shows either the
   **Buy**
   or **Sell** button
   based on whether the parent order is a buy or a sell order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-submit-child.png)
3. Enter the [order
   parameters and account in the Order Ticket](../../../basic-order-entry/order-ticket/description-order-ticket/order-entry-from-order-ticket.md) as needed.

   If using an order profile, the account configured in the profile will be used to submit the order. This
   can
   be a different account or the same account as the originator.

   **Note**: If you select an order profile for the child order, the order tag values and account for
   that
   profile will be placed on the child order.

   All native order types and TT synthetic order types are supported when submitting a child order.
4. Click the single **BUY** or **SELL** button in the Order Ticket to submit the child order to the
   exchange.

   **Tip**: Click the expander (+) in the working care order row in the Order Book to show all working or
   filled child orders, as well as show fills assigned to the parent order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders.png)

### Submitting child orders using MD Trader

1. Select the care order in the Order Book.
2. Depending on the **Floating order entry style** setting in [Orders Preferences](../../../overview/preferences/description-preferences/orders-preferences.md),
   either left-click or right-click the **B (Buy)** or **S (Sell)** button in the
   **B/S** column for the care order.

MD Trader opens seeded with the parent care order parameters, but only one side is active depending on the
side
of the parent order.

3. [Change the
   quantity](../../../basic-order-entry/md-trader/task-md-trader/recentering-md-trader.md) as needed and click a price level to submit the order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-mdt.png)

## Submitting child orders using the Execute button

The optional “Execute” button gives you the ability to submit child orders for multiple care orders with a single
click. The child orders are submitted based on the order parameters of the care order.

To display the button, right-click the Order Book or orders pane in the Order and Fills widget and click
**Settings: Order Book** | **Set Order Toolbar buttons**.

To submit child orders using the “Execute” button, select one or more care orders in the Order Book or orders
pane
and click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-execute-1.png).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-execute1.png)

**Tip**: If the user or account setting “Manage staged orders without claiming” is enabled, you can also
claim
and submit child orders for multiple care orders by clicking “Execute”.

The child orders are submitted based on the care order parameters. The **Status** of the care orders changes
to “Working”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-execute-result1.png)

## Submitting child orders using the staged order alert

You can also claim and execute a care order from a pop-up alert. When the **Preferences** | **Orders** |
**Alert on new staged order** option is enabled in your workspace, the following pop-up alert is displayed
when a
new care order is available:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-alert-1.png)

When you click **Execute** in the pop-up, the care order is claimed and a child order is submitted based on
the
care order parameters. When you click **Buy**, the care order is claimed and an Order Ticket opens seeded
with
the care order parameters. The options to “Buy” or “Execute” are displayed when the “Manage staged orders
without
claiming” order permission is enabled for the account or user in Setup.

**Note**: To cancel the care order without claiming, click “Reject”. To simply ignore the alert, click “x” in
the
upper right corner of the pop-up alert.

## Submitting child orders with a clearing account override

Your administrator can create a clearing account in Setup that is sent to the exchange for the account or order
profile that you select when submitting child orders. If the “Client Can Override” setting is enabled for this
account, you can enter a different clearing account in the “Exchange Clearing Account” field in the Order Ticket
or
MD Trader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-override.png)

This field is optional and can be shown by enabling the **Show Exchange Clearing Account edit box** setting in
**Preferences** | **Orders**. The default value is the clearing account override name configured in Setup
for
the selected account or order profile. If “Client Can Override” is disabled for the clearing account, the edit
box
is grayed out.

## Submitting multiple child orders with the same algo

In the Order Book, you can select multiple parent care orders, apply the same algo or TT Order Type, and submit
the
related child orders using a single order action.

**Tip**: Apply OMS features with a single click without having to right click and navigate the context menu to use those features. In the right-click context menu, select **Settings: Order Book | Set Order Toolbar buttons**. Select **Same Order Type**, click OK then Save. When enabled on the toolbar, each button will enable, disable and function the same as their related right click menu item.

To submit multiple care orders with the same algo:

1. Select one or more parent care orders in the Order Book.
2. Right-click and select **Staging** | **Work with same order type** in the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-staging-menu.png)
3. Select an algo or TT Order Type in the Order Ticket.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-select.png)
4. Configure the algo or order type parameters and click **Submit**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-config.png)

   You can apply a percentage to the quantity of each selected order to work multiple different TT Order types.

   Note The percentage is entered as an integer value from 1 to 100.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-qty-percentage.png)
5. Review the orders and click **Confirm Submit**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-confirm.png)

   The child orders are submitted for each care order selected in the Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-working.png)

   ## Working with Same Order Type Across Staged Orders

   **The Work with same order type** feature is designed to manage staged orders efficiently:

   * **Mapping Order Parameters**: Order parameters &lbrack;including order type, account, and LTP (Last Traded Price)&rbrack; from each selected staged order are mapped to the resulting child orders.
   * **Handling Different Accounts and Order Types**: If the selected staged orders have different accounts or order types, the relevant drop-down controls will seed as empty (“”). If an account or order type is not manually selected, each child order will inherit the account and order type from its respective staged order.
   * **Applicable to All Order Types**: These behaviors apply to all native and algo order types, including both TT and third-party algo orders, when using this feature.

←[Previous PostFilling a care order with a manual fill](filling-a-care-order-with-a-manual-fill.md)

[Next PostExecuting care orders as wholesale trades](executing-care-orders-as-wholesale-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-submit-child.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-execute-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-execute1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-execute-result1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-alert-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-override.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-staging-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-child-orders-qty-percentage.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-confirm.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-same-working.png
