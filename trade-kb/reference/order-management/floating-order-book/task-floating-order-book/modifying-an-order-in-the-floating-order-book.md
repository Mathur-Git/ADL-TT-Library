---
title: Modifying an order in the Floating Order Book
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/floating-order-book/task-floating-order-book/modifying-an-order-in-the-floating-order-book/
---

# Modifying an order in the Floating Order Book

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/floating-order-book/task-floating-order-book/modifying-an-order-in-the-floating-order-book/)

To make a change to an order using the Floating Order Book:

1. In the working order cell, click the middle mouse button to open the Floating Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-1a.png)
2. Click the values in the **Price**, **WrkQty**, and **TIF** columns as needed to change the values as
   follows:
   * Right-click or left-click to increase or decrease the price and quantity value, respectively.
   * Use the middle mouse button to scroll the price and quantity values up and down.
   * Use the up and down arrows keys to change the price and quantity values.
   * Enter specific price and quantity values.
   * If you click a **TIF** value, click the drop-down arrow and select a TIF restriction.
3. Click ![the check mark icon](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB.png) to accept the change.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-2a.png)
4. If you selected and modified multiple orders, click
   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB2.png) at the bottom of the Floating Order Book grid to accept the changes.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-3a.png)

## Reducing the total quantity of multiple orders at a price level

If you have multiple orders working at the same price level, you can reduce the total quantity of two or more of
the orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-intro-1.png)

For example, you submit three working orders of 10, 20, and 30 contracts respectively for a total order quantity of 60 at a price level, then decide to reduce the total quantity to 30 using the Floating Order Book.

TT would delete the 30-lot order (the most recent) to bring the total quantity to 30. Conversely, if you placed the same orders in reverse (30, 20, 10), TT would delete the 10- and 20-lot orders, leaving the single 30-lot order. If necessary, TT will change the quantity of the newest remaining order to achieve the desired total quantity.

To reduce the total quantity of multiple orders at a price level:

1. Open the Floating Order
   Book and select the orders whose total quantity you want to reduce.

   The total quantity of the selected orders is displayed in the **Update order qty:** field (e.g., 20).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-reduce-qty-2.png)
2. Click the **Update order qty:** checkbox and enter the new total quantity (e.g., 5).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-reduce-qty-3.png)

   The **WrkQty** column shows which selected orders will be canceled (red) or modified (green) to reflect the updated total quantity of the orders.
3. Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB3.png) to accept the order changes.

## Modifying child algo orders or TT Order Type orders

1. Select one or more child algo or TT Order Type orders in the Floating Order Book.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo1a.png)
2. Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-algo-fob.png) at the bottom of the Floating Order Book to open the Algo Parameters dialog box.

   The number of orders selected is displayed in the button (e.g., 2).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo2a.png)

   **Tip**: If only one order is selected, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-algo-fob-1.png) in the **Mod** column for the selected order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo2b.png)
3. Modify the algo or order type parameters and click **Submit**.

   Double-click each parameter to modify its value (e.g., Order Price).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo3.png)

←[Previous PostLaunching a Floating Order Book](launching-a-floating-order-book.md)

[Next PostDeleting orders in the Floating Order Book](deleting-orders-in-the-floating-order-book.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-1a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-2a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-modify-3a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-intro-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-reduce-qty-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-reduce-qty-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/Icon_CheckMarkFOB3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo1a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-algo-fob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo2a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-algo-fob-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo2b.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-algo3.png
