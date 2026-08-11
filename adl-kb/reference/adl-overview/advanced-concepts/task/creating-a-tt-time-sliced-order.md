---
title: Creating a TT Time Sliced Order
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-tt-time-sliced-order/
---

# Creating a TT Time Sliced Order

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-tt-time-sliced-order/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry) · [Order Types & Execution § The ADL bridge](../../../../../trade-kb/guides/order-types-and-execution.md#the-adl-bridge)

### Creating a Basic TT Time Sliced Order

The basis of this algo is to submit a BUY Order from the Discrete Order Block at the Bid Price for an order qty of 10 ( Time Sliced Qty) up to a TOTAL of 100 (TOTAL QTY). These orders are to be placed every 5 seconds (Time Sliced Period).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tt-time-sliced-order-1.jpg)

This example leverages several user-defined variable to set the Instrument, Time Sliced Qty, Total Qty, and Time Sliced Period.

In addition, the Time Sliced Generator Block uses the Conditional output from comparing the “working Order Qty” to the Total Order QTY. This comparison gives us the “Total QTY Condition” input for the Enable / Disable condition (i.e., TRUE or FALSE). In this Time Sliced Generator Block, you also have the User Defined Variable for your Time Sliced period.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tt-time-sliced-order-2.jpg)

This includes a few EXPORT Value places for users to monitor internal algo values while the algo is running.

The individual child orders are virtualized since they could possibly have all different BID Prices if the market is moving quickly. Plus, inside that Virtualized Group Block (Order ADDS) is where you could put custom Child Order Management logic for the price, qty, or delete conditions.

From the FILLS or even the Working Order QTY accumulator blocks, you can carry on the downstream Hedge Logic part of your algo.

←[Previous PostCreating a UTC Time Trigger and Time Counter](creating-a-utc-time-trigger-and-time-counter.md)

[Next PostCreating a With A Tick Algo](creating-a-with-a-tick-algo.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tt-time-sliced-order-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tt-time-sliced-order-2.jpg
