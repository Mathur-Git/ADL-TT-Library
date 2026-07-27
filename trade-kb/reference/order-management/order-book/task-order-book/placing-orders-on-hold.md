---
title: Placing orders on hold
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/placing-orders-on-hold/
---

# Placing orders on hold

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/task-order-book/placing-orders-on-hold/)

You can place an order on hold from the Order Book widget. When you place an order on hold, you can change it as you would any other order. A held order remains in the widget until it is resubmitted or deleted. To put on order on hold, click ![the Hold button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-hold-order-2.png).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-hold-order.png)

## Resubmitting held orders

When you click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-resubmit-order.png), the held order is resubmitted. If the **Confirm modifications to working orders from Order Book** setting is enabled in **Preferences** | **Orders**, a pop-up message will be displayed below the Order Toolbar that requires you to confirm the change before resubmitting the held order.

## Pausing and Resuming TT order type orders

In the Order Book widget, you can pause and resume [TT order types](../../../basic-order-entry/tt-order-types/description-tt-order-types/tt-order-types-overview.md). Before you can pause or resume a TT order type, you must first add the Pause and Resume buttons to the Order Book widget toolbar.

### Adding Pause and Resume buttons

To add the **Pause** and **Resume** buttons:

1. Right-click the Order Book or orders pane in the Order Book widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-hold.png)

2. Click **Settings: Order Book**.
3. Click **Set Order Toolbar buttons**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-toolbar-buttons.png)

4. Select **Pause** and **Resume**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-pause-resume.png)

5. Click **OK**.

### Pausing TT order types

Pausing a TT order puts all of the working child orders in the “Hold” state. Pausing a TT order type order is limited to orders with a status of **Waiting**, **Pending Trigger**, or **Working**.

To pause an algo order, select the parent order and click the **Pause** button ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-pause-algo-2.png) .

### Resuming paused TT order types

Upon selecting a paused order and choosing the **Resume** button ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-resume-algo-2.png) , the held child orders are resubmitted to the market. For slicer order types, if a slice was missed while the parent order was paused, the algorithm will resume by immediately placing the first slice after reactivation.

←[Previous PostModifying an order in the Order Book](modifying-an-order-in-the-order-book.md)

[Next PostDeleting orders in the Order Book](deleting-orders-in-the-order-book.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-hold-order-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-hold-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-resubmit-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-hold.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-toolbar-buttons.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-settings-pause-resume.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-pause-algo-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-resume-algo-2.png
