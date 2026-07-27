---
title: Managing stitched and split Care Orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/task-stitching-and-splitting/managing-stitched-and-split-care-orders/
---

# Managing stitched and split Care Orders

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/task-stitching-and-splitting/managing-stitched-and-split-care-orders/)

Stitched care orders can be filled the same way as other care orders by clicking the “B/S” (Buy/Sell) control button [to submit child orders to the exchange](../../care-orders/task-care-orders/submitting-related-child-orders.md). You can also [create manual fills](../../care-orders/task-care-orders/assigning-fills-to-care-orders.md#manual) or use the [Assign Fills](../../care-orders/task-care-orders/assigning-fills-to-care-orders.md) context menu option to fill the order.

**Note**: When assigning fills to a stitched exchange-traded instrument, you can only assign fills to the parent stitched order and not to the child care orders or working child orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-assign-fills1.png)

After splitting an order, the quantity of the original parent care order can be modified after it is split. Any changes to the quantity are rebalanced within the two split child care orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-modify.png)

The quantities of the split child orders can also be modified individually. Changes to these quantities are rebalanced between the two child care orders, but the parent care quantity does not change.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-modify-child.png)

**Note**: Split parent and child care orders cannot be canceled. A stitched order can be canceled unless it contains at least one split care order.

←[Previous PostStitching and Splitting Care Orders](stitching-and-splitting-care-orders.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-assign-fills1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-modify.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-modify-child.png
