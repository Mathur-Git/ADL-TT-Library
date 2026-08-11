---
title: Claiming and unclaiming care orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/claiming-and-unclaiming-care-orders/
---

# Claiming and unclaiming care orders

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/claiming-and-unclaiming-care-orders/)
>
> **Interpreted in:** [Order Types & Execution § Care orders & the TT OMS lifecycle](../../../../guides/order-types-and-execution.md#care-orders-the-tt-oms-lifecycle)

Users with order permissions to manage care orders can [claim a care order](#claiming) using their Order
Book. After claiming the order, the user is considered the “owner” of the care order in the TT system.

After a care order has been claimed, the owner or originator can [unclaim the care
order](#unclaiming) to make it available again.

## Claiming a care order

**Note**: Ensure that the Order Book toolbar buttons **Claim** and **Unclaim** are shown. To show/hide these
buttons, right-click the toolbar, select **Settings**, and click
**Order Toolbar Buttons**. Scroll through the list that appears, check **Claim**
and **Unclaim**, and click **Ok**.

To claim a care order:

1. Open the Order Book widget or the Order and Fills widget.
2. Click the care order row to select it.

   **Note**: Care orders are displayed with a status of **Available** in the **Status** column. Make
   sure you are showing this column in the Order Book settings.

   **Tip**: In the Order Book and Order and Fills widgets, the **Available** status is displayed as an
   actionable button in the **Status** column, allowing you to claim the order with a single click.

   The order row checkbox is checked after selecting the care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-select.png)
3. Click the **Claim** button in the toolbar.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-claim1.png)

   When you claim the order, your alias appears in the **CurrentUser** column, indicating you are the owner
   of the care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-owned1.png)

   The **Unclaim** button is active and the **Claim** button is now grayed out. The Buy or Sell direction
   cell in the **B/S** column becomes an actionable button, and the owner can now click **B** (Buy) or
   **S** (Sell) to enter a child order.
4. Optionally, you can click the order details button ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-details.png) in the toolbar to open
   the **Order Details** screen and view any special order instructions in the **StageMsg** field.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-notes.png)

   **Tips**:

   * You can also view the care order message in the **StageMsg** column in the Order Book.
   * **StageMsg** will also appear for related Child orders.

## Claiming a care order using the staged order alert

You can also claim a care order from a pop-up alert. When the **Preferences** | **Orders** | **Alert on new
staged order** option is enabled in your workspace, the following pop-up alert is displayed when a new care
order is available:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-alert.png)

When you click **Claim** in the pop-up to claim the order, the **Status** column displays as “Claimed” and your
alias is displayed in the **CurrentUser** column. The options to “Buy” or “Execute” a care order using the pop-up
alert
are displayed when the “Manage staged orders without claiming” order permission is enabled for the account or user
in Setup.

**Note**: To cancel the care order without claiming, click “Reject”. To simply ignore the alert, click “x” in the
upper right corner of the pop-up alert.

## Unclaiming a care order

If you own a care order with a **Status** of **Owned**, **Working**, or **Partially Filled**, you can
relinquish ownership of the order using the **Unclaim** button on the toolbar.

**Tip**: When you select a care order, you may have the ability to force the claimed care order back into
“Available” status by using the **Unclaim** button. To use this functionality, your administrator must grant you
the
[Unclaim
Orders
Owned by Others](https://library.tradingtechnologies.com/user-setup/ac-assigning-a-user-to-an-account.html#owned) user permission.

To unclaim a care order:

1. Open the Order Book widget.
2. Click the care order row to select it.
3. Click **Unclaim** in the toolbar.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unclaim.png)

   When you unclaim the order, the **Status** of the order is “Available” and the **CurrentUser** column
   is blank until another user claims the care order. The **Claim** button is active and the **Unclaim**
   button is now grayed out. The “Available” status also becomes an actionable button in the **Status**
   column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unclaim2.png)

←[Previous PostSubmitting care orders](submitting-care-orders.md)

[Next PostManaging and resolving FIX care order rejections](managing-and-resolving-fix-care-order-rejections.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-claim1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-owned1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-details.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-stage-notes.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-alert.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unclaim.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unclaim2.png
