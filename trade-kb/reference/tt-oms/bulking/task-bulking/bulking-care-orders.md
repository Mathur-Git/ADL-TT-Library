---
title: Bulking Care Orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/bulking/task-bulking/bulking-care-orders/
---

# Bulking Care Orders

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/bulking/task-bulking/bulking-care-orders/)

Using the Order Book or orders pane in the Order and Fills widget, you can bulk care orders together by:

* Selecting the [“Bulk” option from the context menu](#context).
* Using the [combining tool](#combine).
* [Dragging and dropping](#drag-and-drop) a care order on another care order.

## Bulking care orders using the context menu

1. Select two or more claimed care orders in the Order Book or orders pane.

   **Tip**: If the account or user has permission to “work orders without claiming” in Setup, you can bulk
   and claim care orders with a single bulking action.
2. Right-click and select **Order Staging** | **Bulk** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-add2.png)

   The care orders are bulked into a single order. Additional care orders can be added to the bulked order
   using the context menu, drag-and-drop, or the combining tool.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-add2-result.png)

## Bulking care orders using the combining tool

1. Right-click a care order and select the **Order staging** | **Combine** option.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-combine.png)

   The combining tool appears in the left side of the Order Book or orders pane.
2. Select the care orders being combined and click the **Bulk** button.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-combine-tool.png)

   **Tip**: You can select the entire Order Book and hover on the **Bulk** button to see which orders are
   available for bulking.

## Bulking care orders using drag-and-drop

Left-click and drag-and-drop a care order unto another care order or bulked order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-drag-and-drop.png)

**Tip**: Apply OMS features with a single click without having to right click and navigate the context menu to use those features. In the right-click context menu, select **Settings: Order Book | Set Order Toolbar buttons**. Select **Bulk** and **Combine**, click OK then Save. When enabled on the toolbar, each button will enable, disable and function the same as their related right click menu item.

## Unbulking Care Orders

When you unbulk an order, consider the following:

* The child care orders return as claimed, individual care orders.
* Child orders continue working in the market, but are orphaned and no longer associated with any care order.
* Allocated fills remain with the child care orders to which they were allocated.
* If a care order is removed from a bulked order that is locked, the removed order remains locked. Refer to [Lock and Release Overview](../../lock-and-release/description-lock-and-release/lock-and-release-overview.md).

To unbulk a care order, right-click the parent bulked order in the Order Book and select **Order staging** |
**Unbulk** from the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unbulk1.png)

The working child orders and claimed care orders are returned to their “pre-bulked” state. The child orders continue
working in the market as native exchange orders, but are “orphaned” and no longer associated with a care order and
the parent
bulked order no longer exists.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unbulk1-result.png)

[Next PostManaging a bulked order](managing-a-bulked-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-add2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-add2-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-combine.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-combine-tool.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-drag-and-drop.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unbulk1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-unbulk1-result.png
