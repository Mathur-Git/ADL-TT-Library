---
title: Modifying an order in the Order Book
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/modifying-an-order-in-the-order-book/
---

# Modifying an order in the Order Book

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/modifying-an-order-in-the-order-book/)

Using the Order Book widget, you can change the price, quantity, account, order type, or
time-in-force of a working order. Simply select an order, modify the order as desired, and click ![the Change button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-change.png).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order.png)

You can also raise or lower the price on an order by ticks by clicking the ![Tick Up](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-tick-up-2.png) and ![Tick Down](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-tick-down-2.png) buttons. When you use these buttons,
the changes happen immediately.

**Note**: When you select multiple orders, most buttons would grey out and only these are available for
modifying the selected multiple orders: Cancel, Hold/Submit, Tick Up and Tick Down buttons. If all of the selected
orders are of the same order type, you can also modify the following fields: Price (including Price Payup),
Time-In-Force (TIF) and TextTT.

If the modification requires that you cancel/replace the working order, the Change button displays as ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-cxl-replace.png) and indicates the order will lose its position in queue. The
**Cxl/Replace** button is displayed when you modify the following:

* account
* order type

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-cxl-replace.png)

When selecting a working parent order for a TT Order Type, you can make changes to the parameters for the selected
order type directly from the Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-tt.png)

**Modify Orders Using Multiple Floating Order tickets**
The Order Book provides an “Edit order…” right-click context menu on working order rows. This menu item launches a floating order ticket with a single green “Change” button.
This feature can be invoked on multiple orders, allowing you to queue up edits for several orders and then individually submit them when desired.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-mulitiple-tickets.png)

### FX Spot Quantity Button

When trading FX Spot instruments, the order quantity controls include a FX Spot Quantity button that allows you to quickly set the numeric quantity to equal the value in thousands (K), millions (M), or the numeric value (blank). Simply click the FX Spot Quantity button to cycle through the options.

## Modifying an order in a grouped Order Book

When an Order Book is part of a widget group, the ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-1.png) toggle button is
displayed in the “view” column for each order row. The button is used for “viewing” filled and partially filled
orders in a grouped widget. When the toggle button is displayed, the checkbox is used for “selecting” an order to
modify or cancel in the grouped Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-group.png)

## Changing the current user on an order

The **CurrentUser** column identifies who is monitoring an order while it’s working in the market. When
orders are entered by multiple users sharing the same account, this column identifies the user who “last touched” an
order.

When you select an order in the Order Book and click the “Current User” button in the Order Toolbar, your alias is
displayed in the **CurrentUser** column. The button is shown by selecting **Settings: Order Book** |
**Set Order Toolbar buttons** in the right-click context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-current-user.png)

## Modifying the clearing account for an order (ASX only)

In the Order Book or orders pane of the Order and Fills widget, you can change the clearing account for working
orders and partially or fully filled orders on ASX.

**Note**: To modify the clearing account, ensure that the **Show Exchange Clearing Account edit box** setting
is enabled in **Preferences** | **Orders**.

To modify the clearing account for an order:

1. Select the order in the Order Book or orders pane.
2. Click the Exchange Clearing Account edit box in the control panel and select an account in the drop down menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-modify-clearing-select.png)
3. Click **Change** to modify the clearing account on the order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-modify-clearing-change.png)

## Customizing order quantity buttons

To customize order quantity buttons:

1. While pressing the **Ctrl** key, right-click in the order quantity number pad buttons. The order quantity button interface opens.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-custom-ob-button1.png)
2. Change an order quantity in the interface. The value immediately changes on the corresponding number pad button.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-custom-ob-button2.png)
3. Click **Save**.

←[Previous PostMonitoring working orders in the Order Book](monitoring-working-orders-in-the-order-book.md)

[Next PostPlacing orders on hold](placing-orders-on-hold.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-change.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-tick-up-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-tick-down-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-cxl-replace.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-cxl-replace.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-tt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-mulitiple-tickets.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-change-order-group.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-current-user.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-modify-clearing-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-modify-clearing-change.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-custom-ob-button1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-custom-ob-button2.png
