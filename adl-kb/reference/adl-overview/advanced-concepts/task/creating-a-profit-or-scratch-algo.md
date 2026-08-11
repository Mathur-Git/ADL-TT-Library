---
title: Creating a Profit or Scratch Algo
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-profit-or-scratch-algo/
---

# Creating a Profit or Scratch Algo

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-profit-or-scratch-algo/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Exits and position management](../../../../guides/design-patterns.md#exits-and-position-management)

**Please note that all samples in the help library are intended for educational purpose to give insight into ways to approach building different pieces of logic in ADL. Any use of the samples in production is at your own risk.**

The following Profit or Scratch algo is an Order Ticket Algo (OTA). This sample algo is designed to work on the inside market. When you place your order the algo will monitor the quantity available at that price, should the quantity drop below the scratch threshold the order will be pulled.

In this example, the user sets the following parameters:

* Instrument
* Price
* Quantity
* Profit Ticks
* Scratch Threshold

The algo will automatically enter a profit taking order when any fills are achieved. The order will be entered a user defined number of ticks from the fill price (Profit Ticks).

Should the quantity at your entry price drop below the scratch threshold when you have a position the algo will attempt to scratch all unfilled profit taking orders.

Once created, you can launch this algo from the MD Trader, Market Grid and, the Algo
Dashboard.

**Note**: If the scratch threshold is triggered and the price is missed, the order will remain working at your entry price. The order can then be manipulated manually.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-profit-or-scratch-algo-1.jpg)

←[Previous PostSubmitting With A Tick Orders](submitting-with-a-tick-orders.md)

[Next PostTracking Recent Volume](tracking-recent-volume.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-profit-or-scratch-algo-1.jpg
