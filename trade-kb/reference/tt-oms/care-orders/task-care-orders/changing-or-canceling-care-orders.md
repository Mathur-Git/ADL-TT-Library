---
title: Changing or canceling care orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/changing-or-canceling-care-orders/
---

# Changing or canceling care orders

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/changing-or-canceling-care-orders/)

Based on their role in submitting or managing the order, users can make requests to [change a care
order](#changing) or [cancel a care order](#canceling). Requests can be made via the Order Book widget in TT
or a FIX trading application.

## Changing a care order

After the care order is claimed and has not been fully filled, the originator can request a change to the following:

* Price
* Quantity
* Exchange order type

To change a care order:

1. Select the order in the Order Book and change the price or quantity.
2. Click **Change**.  

   If you are the originator and not the owner, the **Status** column shows **Pending Change Approval**. ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-change.png)Both the originator and the owner will see **Pending Change Approval** in the **Status** column of their Order Books.

   **Note**: When a care order Originator submits a quantity reduction change on a locked care order, a warning will appear if the proposed order quantity is below the fill quantity of the unreleased fills. The Caretaker can then choose to reject the request, or approve the reduction and keep the extra fills for internal inventory. This feature requires enabling the “Alert on cancel/change of claimed staged orders” setting under **Preferences** > **Orders**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2026/05/co-qty-reduction-warning.png)

## Canceling a care order

The owner can cancel the care order before submitting any child orders.

If the originator attempts to cancel the care order after it is claimed by the owner, then the owner must approve the
cancel request. Both the originator and the owner will see **Pending Cancel Approval** in the **Status**
column of their Order Books, indicating that there is a care order cancel request pending approval by the owner.

**Note:** Canceling a parent care order will also cancel all working child orders of that care order, even if the child orders have not been selected in the Order Book.

To cancel a care order:

1. Select a care order in the Order Book.
2. Click the **Cancel** button in the tool bar.  

   If you are canceling orders with fills that have not been released, click **Release Fills and Cancel Order** in the **Cancel orders?** dialog box.![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-cancel-unrel.png)

     
   If you are the originator and not the owner, the care order **Status** changes to **Pending Cancel Approval**. Otherwise, “Pending Cancel” is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-cancel.png)

←[Previous PostCare order passing](care-order-passing.md)

[Next PostApproving or rejecting a request](approving-or-rejecting-a-request.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-change.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/05/co-qty-reduction-warning.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-cancel-unrel.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-cancel.png
