---
title: Stitching and Splitting Overview
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/description-stitching-and-splitting/stitching-and-splitting-overview/
---

# Stitching and Splitting Overview

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/description-stitching-and-splitting/stitching-and-splitting-overview/)

The TT® OMS provides [stitching](#stitch) and [splitting](#split) tools that allow you to
combine and fill multiple care orders simultaneously.

## Stitching Care Orders

Stitching is a tool that allows you to combine staged orders for different instruments. As an execution specialist or
broker, you can stitch multiple orders together that comprise exchange-listed futures or options spreads.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-result.png)

By stitching orders together, you can fill multiple care orders simultaneously and often at
better prices due to more efficient spread markets. A newly stitched care order is seeded with a price calculated as
the net spread price of the child care order legs.
Stitching a spread order automatically creates a remainder “tail” order when the spread leg quantities do not exactly match.
Any excess quantity can be traded separately as an outright once the stitch is created.

You can [stitch care orders](../task-stitching-and-splitting/stitching-and-splitting-care-orders.md#stitch) using the Order Book
widget or orders pane of the Order and Fills widget. Orders stitched using the context menu in these widgets must
have the same product and quantity and opposite Buy/Sell direction. Bulked and split orders can also be stitched
using these widgets.

**Note**: The following orders cannot be stitched:

* Existing stitched parent orders with working child orders.
* Care orders with partially filled or fully filled allocated child orders.
* Fully filled bulked, stitched, or split orders.

## Splitting Care Orders

Splitting allows you to manage a claimed staged order by splitting it into into two equally sized orders that can be
executed separately. The split orders can then be stitched or bulked with other orders.

For example, if you cannot stitch the quantities of two orders together, you can split one of the orders into two,
stitch the
quantities that match, and work the remaining quantities as a separate order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-result1.png)

You can [split care orders](../task-stitching-and-splitting/stitching-and-splitting-care-orders.md#split) using the Order Book
widget or orders pane of the Order and Fills widget. Split actions are also allowed for partially and fully filled
unallocated split orders with no working child orders.

**Note**: The following orders cannot be split:

* Bulked orders (an order must be removed from a bulk before it can be split).
* Care orders with working child orders.
* Previously split orders (a care order can only be split once).
* Stitched orders.

## Split and Stitch From/To Behavior

When using care order features of Stitching and Splitting, the terms “From” and “To” refer to the various parent and child care orders that result from those actions.

**Note**: A “SplitFrom” order refers to the original care order that was split into smaller “SplitTo” constituent orders.

TT does not support executing a SplitFrom parent staged order; the smaller SplitTo orders must be executed instead. TT does not support executing StitchFrom care orders that have been stitched into StitchTo parent orders.

To prevent attempting unsupported actions in the Order Book, when one or more parent SplitFrom care orders and/or child StitchFrom care orders are selected, the **Execute** button is disabled.

When the **Execute** button is clicked on a selection of multiple care orders, any SplitFrom/StitchFrom orders in the selection will be ignored and not attempted to be executed.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-result1.png
