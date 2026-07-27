---
title: Tracking Recent Volume
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/tracking-recent-volume/
---

# Tracking Recent Volume

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/tracking-recent-volume/)

This example shows how to estimate how many contracts have traded within a certain number of seconds in the past. This functionality is achieved using the Stopwatch Block.

In general:

1. Multiply hour x3600 and minute x60 to calculate the number of seconds.
2. Use a Value Bucket to Sum up the Volume traded during each second (Hole=Current Second, Value=TradeQty)
3. Use a Value Accumulator to Sum all Trade Qty
4. Every second, subtract the volume from X seconds ago

The “Erased Volume” Value Accumulator’s formula is the Block Value for the Value Bucket marked “Volume to Erase”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tracking-recent-volume.jpg)

←[Previous PostCreating a Profit or Scratch Algo](creating-a-profit-or-scratch-algo.md)

[Next PostSummarize Volume](summarize-volume.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-tracking-recent-volume.jpg
