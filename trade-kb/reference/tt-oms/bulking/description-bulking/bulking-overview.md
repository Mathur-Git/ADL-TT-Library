---
title: Bulking Overview
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/bulking/description-bulking/bulking-overview/
---

# Bulking Overview

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/bulking/description-bulking/bulking-overview/)

The Bulking functionality in TT® OMS allows you to combine multiple care orders with the same instrument and
Buy/Sell direction into a single care order for more efficient execution. You can submit orders for the individual
bulked order and then allocate the fills to the customer’s original care orders.

Care orders are bulked using the Order Book or orders pane in the Order and Fills widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-overview2.png)

Care orders can be bulked with working child orders or with partially or fully filled allocated child orders. When
orders with different prices are bulked, the parent bulked order shows the “best price” of the child orders (e.g.,
lowest price for Buys, highest price for Sells).

**Note**: Care orders that are a child of another care order cannot be bulked. Also, because bulking only applies
to care orders, the following types of orders cannot be bulked: native exchange orders, TT Order Types, ADL algo
orders, and third party bank algo orders.

## Bulking Display

Bulked orders are displayed in the Order Book or orders pane of the Orders and Fill widget as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-overview-display.png)

The display includes:

1. Buy/Sell button — Submits orders for the parent bulked order. Order actions for the bulked order can only
   be executed at the parent level.
2. Nested care orders — Indicates which care orders are part of the bulked order.
3. Parent bulked order — A combined group of customer care orders.
4. Child order — Order submitted for a parent care order or bulked order.
5. Child care order — The customer’s original care orders comprising the parent bulked order.

## Bulking From/To Behavior

When using care order features of Bulking, the terms “From” and “To” refer to the various parent and child care orders that result from those actions.

**Note**: A “BulkFrom” order is a care order that was bulked into a larger “BulkTo” parent order.

TT does not support executing BulkFrom care orders that have been bulked into BulkTo parent orders that can be executed.

To prevent attempting unsupported actions in the Order Book, when one or more child BulkFrom care orders are selected, the **Execute** button is disabled.

When the **Execute**is clicked on a selection of multiple care orders, any BulkFrom orders in the selection will be ignored and not attempted to be executed.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-overview2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-overview-display.png
