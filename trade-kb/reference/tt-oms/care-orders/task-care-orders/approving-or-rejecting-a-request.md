---
title: Approving or rejecting a request
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/approving-or-rejecting-a-request/
---

# Approving or rejecting a request

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/approving-or-rejecting-a-request/)

As an owner of a care order, you can use the Order Book to approve or reject a [cancel](#cancel) or [change](#change) request.

**Note:** This function is only for price and/or quantity changes, but not for order types.

Note Pending change requests on claimed care orders can be authorized and applied in one step via the **“Approve and apply changes to child orders”** option found in the right-click menu of **Pending Change Request(s)**. When the care order owner chooses this option, this will have the care order change request applied to current working child orders of that staged order when approved by the execution trader.

## Approving or rejecting a change request

If you are currently the owner of a care order and receive a change request from the originator, the order remains in the **Pending Change Approval** state until you approve or reject the request. No child orders can be entered for the parent care order in this state.

**Tip**: In the workspace “Preferences”, you can enable a sound alert that plays when a [change request is received](../../../overview/preferences/description-preferences/sounds-preferences.md#change).

To approve or reject a change request:

1. Right-click the care order with **Status** of **Pending Change Approval** flashing in the Order Book.
2. Click **Pending Change Request(s)** in the context menu and click **Details**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-details.png)
3. Click **Approve** or **Reject** to approve or reject the request, or click **Details** to review the request before approving or rejecting it.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-details2.png)

   If approved, the order price or quantity is changed in the originator’s and owner’s Order Book. If rejected, the **Status** column shows the previous status (e.g., Partially Filled).

   Note Pending change requests on claimed care orders can be authorized and applied in one step via the **“Approve and apply changes to child orders”** option found in the right-click menu of **Pending Change Request(s)**. When the care order owner chooses this option, this will have the care order change request applied to current working child orders of that staged order when approved by the execution trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-to-a-claimed-care-order.png)

## Approving or rejecting a cancel request

If you are currently the owner of a care order and you receive a cancel request, the order remains in the **Pending Cancel Approval** state until you approve or reject the request. No child orders can be entered for the parent care order in this state.

**Tip**: In the workspace “Preferences”, you can enable a sound alert that plays when a [cancellation request is received](../../../overview/preferences/description-preferences/sounds-preferences.md#cancel).

To approve or reject a cancel request:

1. Right-click the care order with **Status** of **Pending Cancel Approval** flashing in the Order Book.
2. Click **Pending Cancel Request(s)** in the context menu and click **Approve** or
   **Reject**.

   Note When you click **Approve** for a cancel, the care parent and child orders are canceled. When you click **Reject**, the care order status from the Order Book will return to Working.



   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-cancel-request.png)

## Approving or rejecting a request via staged order alert

You can also approve or reject a cancel or change request from a pop-up notification. When **Preferences** | **Orders** | **Alert on cancel/change of claimed staged order** is enabled in your workspace, the following pop-up alert is displayed for a cancel or change request:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-cancel-noty.png)

When you click **Accept** in the notification for an order change, the **Status** column returns to “Working”. When you “accept” a cancel request, the care order parent and child orders are canceled.

To reject the cancel or change, click **Reject**. To simply ignore the alert, click “x” in the upper right corner of the pop-up alert.

**Tip**: You can enable **Confirm action on Care Order Alerts** in **Preferences** | **Orders** to require confirmation before approving the requests.

←[Previous PostChanging or canceling care orders](changing-or-canceling-care-orders.md)

[Next PostAssigning Fills and Orders to Care Orders](assigning-fills-and-orders-to-care-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-details.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-details2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-to-a-claimed-care-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-cancel-request.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-approve-cancel-noty.png
