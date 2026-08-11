---
title: Assigning fills to care orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/assigning-fills-to-care-orders/
---

# Assigning fills to care orders

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/assigning-fills-to-care-orders/)

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


   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-filter.png)

   **Note**: If a manual or exchange fill exists that matches the side, contract, and is less than or equal
   to the care order quantity, the context menu shows the “Assign fills…” option.
3. In the Fills pane, select one or more fills to assign for the care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-select-filter.png)

   **Tip**: Only fills that can be assigned to the care order are shown in the Fills pane.
4. Click **Assign Fills to Order**.

   The fill is added to the care order and appears in both the owner’s and originator’s Fills panes. The owner
   (e.g., Broker A) sees the fill from their own account (e.g., 12345) added to the care order account (e.g.,
   ABCDEF).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-owner-filter.png)

   The originator (e.g., Portfolio Mgr) sees only the fill assigned to their account (e.g., ABCDEF), and the
   **ExeQty**, **% Filled**, and **AvgPrc** columns are updated in the Order Book. The **NetPos**
   and **P/L** in the Positions pane are also updated based on the assigned **FillQty** (e.g., 5).



   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-orig-filter1.png)

←[Previous PostExecuting care orders as wholesale trades](executing-care-orders-as-wholesale-trades.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-select-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-owner-filter.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-assign-fills-orig-filter1.png
