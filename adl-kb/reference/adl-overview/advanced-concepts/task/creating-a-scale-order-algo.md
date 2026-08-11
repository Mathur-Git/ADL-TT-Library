---
title: Creating a Scale Order Algo
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-scale-order-algo/
---

# Creating a Scale Order Algo

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-scale-order-algo/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry)

**Please note that all samples in the help library are intended for educational purpose to give insight into ways to approach building different pieces of logic in ADL. Any use of the samples in production is at your own risk.**

The following Scale Order algo is an Order Ticket Algo (OTA). This sample algo allows you to place multiple orders into the market with a single click. Starting from your order entry price the algo will place a user defined number of orders into the market, each order can be separated by a user defined number of ticks which is defined by the spacing value.

Once created, you can launch this algo from the MD Trader, Market Grid, Algo Dashboard and, Autotrader.

**Note**: Since this is an OTA algo with Flip for Sell functionality employed, if you launch it from the MD Trader the Instrument, Price, Order Qty and Buy / Sell direction will be picked up automatically based on where you click.

**Warning**: This algo has been designed to leave orders working in the market once the ago has been paused/ cancelled. This algo is designed purely as a submission tool.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-scale-order.jpg)

The Scale Orders algo uses the following process:

1. At the start of the algo a generator sends a message to the Loop Block which is configured to loop as many times as the number of orders you require. The Loop Block and its Index count are crucial for creating the scaling behavior we require.
2. You will see that we subtract 1 from the Index count. We do this so that we use a value of zero on the first loop, this ensures that the first order is entered at the start price.
3. The Index count is then multiplied by the minimum price increment of the instrument before the spacing value is applied. Once this has been calculated we subtract this value from the start price to give us the price for which we will be submitting the order.
4. Upon each loop the Discrete Order Block (DOB) will reference the blocks labelled ‘Submit Price’ and ‘Order Qty’. The Loop block will wait until the discrete message has reached the DOB before commencing the next loop, this ensures that each order is sent at a new price level.
5. Once the loop command has been completed the stopwatch is used to wait 1 second before and alert is produced and the algo paused. The reason the stopwatch is used as a throttle is to ensure that all orders have been sent prior to pausing the algo.

←[Previous PostSmartberg Algo](smartberg-algo.md)

[Next PostCreating a UTC Time Trigger and Time Counter](creating-a-utc-time-trigger-and-time-counter.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-scale-order.jpg
