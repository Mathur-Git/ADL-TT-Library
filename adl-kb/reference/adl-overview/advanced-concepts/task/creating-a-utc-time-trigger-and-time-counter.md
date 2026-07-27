---
title: Creating a UTC Time Trigger and Time Counter
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-utc-time-trigger-and-time-counter/
---

# Creating a UTC Time Trigger and Time Counter

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/creating-a-utc-time-trigger-and-time-counter/)

### Creating a UTC Time Trigger and Time Counter

Below is a simple suggestion and possibility for how to create a Specific Date / Time trigger in a UTC ( Coordinated Universal Time) time. Then have that Time Trigger also have a secondary Counter Logic. You can also see how easy it is to add in UTC to CST (Central Standard Time) time conversion as well. The Trigger Value Extractor Block is simply using a counter formula of 1 inside the block. For the UTC to CST conversion logic…… you need to subtract the correct number of hours from UTC time to get CST. Hence the CST Hour Conversion.

For the counter you set the second input for 1000ms. This way you get a discrete message output each second which creates the counter.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-create-a-utc-time-trigger-and-time-counter.jpg)

←[Previous PostCreating a Scale Order Algo](creating-a-scale-order-algo.md)

[Next PostCreating a TT Time Sliced Order](creating-a-tt-time-sliced-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-create-a-utc-time-trigger-and-time-counter.jpg
