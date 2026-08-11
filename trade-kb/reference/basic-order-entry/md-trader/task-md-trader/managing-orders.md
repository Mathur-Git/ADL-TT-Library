---
title: Managing orders
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/task-md-trader/managing-orders/
---

# Managing orders

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/task-md-trader/managing-orders/)
>
> **Interpreted in:** [Order Types & Execution § MD Trader mechanics](../../../../guides/order-types-and-execution.md#md-trader-mechanics)

Working orders can be modified or canceled in MD Trader. You can modify a working order by moving it to a different
price level with an easy drag-and-drop action, or by clicking on it in the working orders column and launching a
Floating Order Book. Orders can be canceled by clicking on the orders in the working orders column or by using the
cancel buttons in the Order Pane.

## Modifying an order with drag and drop

To modify an order with drag and drop:

1. At a specific price level, click and hold the right mouse button in a cell in the **Work**
   column that corresponds to the price of the working orders.
2. Drag the orders to the desired price and release the right mouse button. This action will modify the price
   of all orders at that price level.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/orders-mdt-change.png)

## Launching a Floating Order Book in MD Trader

To launch a Floating Order Book in MD Trader:

1. Middle-click a working order cell in MD Trader.The Floating Order Book opens seeded with the order details.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-float1.png)
2. In the Floating Order Book, you can change the **WrkQty** (working quantity),
   **Price**, or **TrgPrc** (trigger price). You can also click the
   **Cxl** icon to cancel the order, or click the **Algo** icon to launch an algo to
   manage the order.

## Reducing the total quantity of multiple orders at a price level

If you have multiple orders working at the same price level, you can quickly reduce the total quantity of these
orders. TT will begin deleting newer orders, so you maintain the best position-in-queue, until the total
quantity of the remaining orders matches your desired lower total.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-intro.png)

For example, suppose you place three working orders at a price level of 10, 20 and 30, respectively, for a total
order quantity of 60 at that price level. You then decide you only want to work a total quantity of 30
contracts. TT would delete the 30-lot order (the most recent) to bring the total quantity to 30. Conversely, if
you placed the same orders in reverse (30, 20, 10), TT would delete the 10- and 20-lot orders, leaving the
single 30-lot order. If necessary, TT will change the quantity of the newest remaining order to acheive the
desired total quantity.

This feature is supported only for the following order types:

* Limit
* Stop limit
* Stop market
* TT Stop

To reduce the quantities of all orders at a price level:

1. Right-click on the working order cell on the price-level with one or more working orders.An entry box appears showing the current total working quantity of the orders at that price level.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-1.png)
2. Enter the desired new, lower total quantity, and click ![the check](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-checkbox.png). Note that you can only decrease the quantity; you cannot increase the quantity.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-2.png)

   Notice the total working quantity updates.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-3.png)
3. If desired, you can display the Floating Order Book to see the remaining working orders.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-4.png)

**Note**: You can also reduce the total order quantity using the [Floating
Order Book](../../../order-management/floating-order-book/task-floating-order-book/modifying-an-order-in-the-floating-order-book.md).

## Canceling orders in MD Trader

To cancel orders in MD Trader:

1. To cancel working orders at a specific price level, click the working orders in the cell in the
   **Work**
   column at the desired price. This action will cancel all orders at that price level.
2. To delete multiple orders, click one of the **CXL** buttons in the order pane of the MD Trader
   widget:

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/orders-mdt-cancel.png)

   * **CXL S** — Cancels all working Sell orders for the selected instrument.
   * **CXL All** — Cancels all working orders for the selected instrument.
   * **CXL B** — Cancels all working Buy orders for the selected instrument.**Note**: If you are filtering per account, only orders for that account
   will be canceled.

←[Previous PostEntering an order](entering-an-order.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/orders-mdt-change.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-float1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-checkbox.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-reduce-qty-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/orders-mdt-cancel.png
