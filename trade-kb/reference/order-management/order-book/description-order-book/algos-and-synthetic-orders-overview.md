---
title: Algos and synthetic orders overview
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/description-order-book/algos-and-synthetic-orders-overview/
---

# Algos and synthetic orders overview

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/description-order-book/algos-and-synthetic-orders-overview/)

An algo or synthetic order is an order managed within TT that submits orders to the exchanges. A synthetic order consists of a parent order and the child orders it submits to the exchanges. TT supports a variety of synthetic orders, including:

* ADL® algos
* Aggregator orders
* Autospreader orders
* Staged orders
* TT order types

The Order Book displays synthetic orders with child orders nested below the parent order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-overview.png)

1. ADL Algo parent synthetic order. ADL algo parent orders show **ALGO** in the **Exch** column and list the name of the algo (**Limit w Offset**) in the **Contract** and **Type** columns.

   In this example, you can see that the parent order manages one child limit order.
2. TT Order Type synthetic parent order. TT Order type parent orders show the exchange name followed by an asterisk (**CME\***) in the **Exch** column and the name of the TT Order type (**TT Time Sliced**) in the **Type** column.

   You can see that this parent order manages the three child limit orders shown in the rows below it.
3. Autospreader parent order. Autospreader parent orders show **ASE** in the **Exch** column and the name of the spread (**ZBZN**) in the **Contract column**

   Here, you can see that the parent order manages the two child limit orders below it.

1. One child limit order managed by the ADL algo parent order
2. Three child limit orders managed by the TT Time Sliced order type
3. Two child limit orders managed by the Autospreader ZBZN spread order

The Order Book allows you to hide child orders by collapsing their parent orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-collapsed.png)

The **TTOrderID**, **ParentID**, and **Child Orders** columns also provide information to identify parent synthetic orders and their associated child orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-columns.png)

1. All parent and child orders have a **TTOrderID**.
2. Child orders also show the order ID for their parent orders in the **ParentID** column.
3. The **Child Orders** column displays the number of child orders being managed by each parent synthetic order. Child orders always show **0** in this column.

←[Previous PostOrder Book overview](order-book-overview.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-overview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-collapsed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-parent-child-columns.png
