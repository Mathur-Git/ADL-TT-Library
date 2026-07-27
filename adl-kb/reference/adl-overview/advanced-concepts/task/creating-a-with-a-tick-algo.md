---
title: Creating a With A Tick Algo
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-with-a-tick-algo/
---

# Creating a With A Tick Algo

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-with-a-tick-algo/)

**Please note that all samples in the help library are intended for educational purpose to give insight into ways to approach building different pieces of logic in ADL. Any use of the samples in production is at your own risk.**

The following With A Tick algo is an Order Management Algo (OMA). This sample algo is designed to be attached to an existing order that is currently working on the best Bid/Ask. The origin of the existing order can be either manually or algo entered. The algo allows you to monitor the quantity available on the opposing side of the market one price increment away from your working order. You set a threshold which should the monitored quantity become less than the algo will ‘pay up’ one tick (minimum price increment).

Once created, you can launch this algo from the MD Trader, Order Book and, the Floating Order widget.

**Note**: The algo will only pay up once.
If you attach this algo to an order that is working in the depth or the opposing side of the market it more than one minimum price increment away the pay up tick will be actioned immediately.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-profit-or-scratch-algo.jpg)

In this example, the WAT Threshold variable represents the minimum available quantity you wish to be available at the monitored price before actioning the pay up tick.

←[Previous PostCreating a TT Time Sliced Order](creating-a-tt-time-sliced-order.md)

[Next PostSubmitting With A Tick Orders](submitting-with-a-tick-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-profit-or-scratch-algo.jpg
