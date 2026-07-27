---
title: Passing and accepting orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/order-passing/task-order-passing/passing-and-accepting-orders/
---

# Passing and accepting orders

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/order-passing/task-order-passing/passing-and-accepting-orders/)

Using the Order Book widget or orders pane of the Order and Fills widget, you can pass partially filled, held,
modified, or unchanged working orders including the following:

* Synthetic parent orders (e.g., Autospreader) and TT Order Types.
* Working Cross orders or other OTC/Wholesale orders.
* Parent and child orders submitted by an ADL algo.

**Note**: Child orders cannot be passed separately from their parent. When a parent order is passed, it’s child
orders are passed with it.

## Passing an order

To pass an order:

1. Select a working order in the orders pane of the Order Book widget or Order and Fills widget.
2. Click the **Order Passing** button and select a target user group.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-chicago1.png)

   **Note**: You can select the **Send Home** option to pass the order directly to the user and group that
   originated the order as shown in the “Originator” and “Original Group” columns.

   After initiating the order pass, “Pending Out” is displayed in the **Pass State** column and the target
   group is shown in the **Dest Group** column. The row is highlighted in orange to indicate the order is
   being passed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-chicago2.png)

   Click **Undo Pass** if you want to cancel the pass and select a different “caretaker” group.

## Accepting a passed order

When an order is passed to you, the following is displayed in your Order Book widget:

* An orange highlighted order row in the orders pane with **Pending In** displayed in the **Pass State**
  column.
* The name of the user group passing the order to you displayed in the **Caretaker** column.

To accept a passed order:

1. Select the passed order in the Order Pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use6.png)
2. Click the **Order Passing** button and select **Accept orders**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use7.png)

   To reject the passed order, you can select **Reject orders**.

   After accepting the passed order, your group name is displayed in the **Caretaker** column. The
   **Original Group** column shows the name of the user group that initially passed the
   order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use8.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-chicago1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/op-chicago2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-op-use8.png
