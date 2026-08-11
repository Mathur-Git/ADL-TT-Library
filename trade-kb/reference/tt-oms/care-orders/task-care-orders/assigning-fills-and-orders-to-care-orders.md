---
title: Assigning Fills and Orders to Care Orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/assigning-fills-and-orders-to-care-orders/
---

# Assigning Fills and Orders to Care Orders

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/assigning-fills-and-orders-to-care-orders/)
>
> **Interpreted in:** [Order Types & Execution § Care orders & the TT OMS lifecycle](../../../../guides/order-types-and-execution.md#care-orders-the-tt-oms-lifecycle)

## Assigning Orders to Care Orders

You can assign existing working orders to a care order in the Order Book and Orders and Fills widget (OFW) via the “Assign > Orders…” right-click menu item that appears on a staged order.

When assigning orders, consider the following:

* An owner can assign exchange orders that match the side and contract of the care order, are less than or equal to the care order quantity, and are at the same or better price.
* Orders can be assigned from a different account or the same account as the originator.

To assign orders to a care order:

1. [Claim the care order](claiming-and-unclaiming-care-orders.md) in the orders pane of
   the Order and Fills widget.
2. Right-click the care order and select **Assign Orders…** from the context menu.


   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-orders-filter.png)

   **Note**: If an exchange order exists that matches the side, contract, and is less than or equal
   to the care order quantity, the context menu shows the “Assign orders…” option.
3. In the Orders pane, select one or more orders to assign for the care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-orders-select-filter.png)

   **Tip**: Only orders that can be assigned to the care order are shown in the **Assignment** pane.

**Note**: When you select the “By Order” checkbox, fill records in the panel are “rolled up” and will be displayed grouped together under their same Order ID, similar to how the “By Order” display mode behaves in the Fills widget. In this “By order” mode, selecting a single parent fill order record and clicking the “Assign fills to order” button will assign all of that order’s individual fills to the care order, the same as if you had selected all of the partial fills themselves individually.

4. Click **Assign Orders to Order**.

The Orders are now nested below the Care Order in the **Assignment** pane.

## Assigning Fills to Care Orders

After claiming a care order, the owner can partially or fully fill the order by assigning fills from their inventory
using the Order and Fills widget. When the fills are assigned to the care order, both the owner and originator see
the fills and their impact on the remaining quantity of the care order in their Order and Fills widget.

**Note**: You must use the Order and Fills widget to assign fills.

When assigning fills, consider the following:

* An owner can assign manual or exchange fills that match the side and contract of the care order, are less than
  or equal to the care order quantity, and are at the same or better price.
* Fills can be assigned from a different account or the same account as the originator.

To assign fills to a care order:

1. [Claim the care order](claiming-and-unclaiming-care-orders.md) in the orders pane of
   the Order and Fills widget.
2. Right-click the care order and select **Assign Fills…** from the context menu.


   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-filter-1.png)

   **Note**: If a manual or exchange fill exists that matches the side, contract, and is less than or equal
   to the care order quantity, the context menu shows the “Assign fills…” option.
3. In the Fills pane, select one or more fills to assign for the care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-select-filter-1.png)

   **Tip**: Only fills that can be assigned to the care order are shown in the Fills pane.
4. Click **Assign Fills to Order**.

   The fill is added to the care order and appears in both the owner’s and originator’s Fills panes. The owner
   (e.g., Broker A) sees the fill from their own account (e.g., 12345) added to the care order account (e.g.,
   ABCDEF).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-owner-filter-1.png)

   The originator (e.g., Portfolio Mgr) sees only the fill assigned to their account (e.g., ABCDEF), and the
   **ExeQty**, **% Filled**, and **AvgPrc** columns are updated in the Order Book. The **NetPos**
   and **P/L** in the Positions pane are also updated based on the assigned **FillQty** (e.g., 5).



   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-orig-filter1-1.png)
5. To **unassign** fills to a care order:

   Right-click the care order and select **Unassign Fills…** from the context menu.

   **Notes**

   * Only current session fills can be assigned and/or unassigned to/from a care order.
   * Locked care order fills can be unassigned before the fills are released.
   * Unassigning fills on fully filled care orders makes that care order appear as a working order in the Order Book. The caretaker can then add new child orders and/or assign new fills to that order. The fills that have been unassigned in this process become available to be assigned to other care orders.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unassign-fills.png)

   In the Fills pane, select one or more fills to unassign for the care order.

   Click **Unassign Fills to order**.

←[Previous PostApproving or rejecting a request](approving-or-rejecting-a-request.md)

[Next PostFilling a care order with a manual fill](filling-a-care-order-with-a-manual-fill.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-orders-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-orders-select-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-filter-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-select-filter-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-owner-filter-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-orig-filter1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-unassign-fills.png
