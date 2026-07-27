---
title: Smartberg Algo
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/smartberg-algo/
---

# Smartberg Algo

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/smartberg-algo/)

**Please note that all samples in the help library are intended for
educational purpose to give insight into ways to approach building different
pieces of logic in ADL. Any use of the samples in production is at your own
risk.**

The following Smartberg algo is an Order Ticket Algo (OTA). This algo works in a similar fashion to a traditional Iceberg order with the exception of how it reacts when hitting/lifting. Where a traditional Iceberg would continuously reload at a price using an identical clip size each time the Smartberg takes the size available in addition to posting its instructed clip size in a single action. This is a more efficient way of executing as it reduces the amount of messaging, increases your chances of getting filled and is less obvious to the market that an iceberg is being worked.

Once created, you can launch this algo from the MD Trader, Market Grid, Algo
Dashboard and, Autotrader.

This algo includes the following user-defined variables: Instrument, Order Price, Total Qty and, Disclosed Qty.

**Note**: Since this is an OTA algo with Flip for Sell functionality employed, if you launch it from the MD Trader the Instrument, Price, Order Qty and Buy / Sell direction will be picked up automatically based on where you click.

**Warning**: The algo will never intentionally work an order larger than your defined clip size however there may be times where the algo sends an order to take advantage of resting size which is filled whilst the order is in flight leading to a momentary breach of your defined clip size. In this scenario the order will be pulled after 100ms and the appropriate size be reallocated to the order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-smartberg-algo.jpg)

The Smartberg algo uses the following process:

1. The algo starts by checking if there is any resting volume on the opposite side of the market. If there is then it will take the available volume adding the disclosed quantity assuming this is less than or equal to your ‘Total Quantity’.
2. A discrete message is generated at the start of the algo which hits a stopwatch block with a 50ms time delay. This is there to allow the above quantity calculation to take place, once elapsed the following two value extractors will capture the current fill count and calculated size of the first order.
3. The order will begin working, once the current clip has been filled a discrete message will be generated to repeat the process and calculate the next order quantity.
4. If the order price is manually modified whilst the algo is running this logic is used to check the new price and if any adjustments to the order quantity are required. Here you will also find a logic check to recalculate the order quantity should your working quantity exceed that of your clip size. Such situations could occur if the size wall pulled/filled whilst your order was in-flight.
5. When the total number of fills is equal to the total quantity the algo is complete and will enter a paused state.

←[Previous PostStacked Q Holder Example](stacked-q-holder-example.md)

[Next PostCreating a Scale Order Algo](creating-a-scale-order-algo.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-smartberg-algo.jpg
