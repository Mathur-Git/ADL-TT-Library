---
title: Managing a bulked order
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/bulking/task-bulking/managing-a-bulked-order/
---

# Managing a bulked order

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/bulking/task-bulking/managing-a-bulked-order/)

You can fill or modify the bulked order the same as other care orders using the Order Book or orders pane in the
Order and Fills widget.

## Modifying a bulked order

When an order is bulked, the care order originator still has the flexibility to cancel or change the quantity, price,
or order type of the original care orders. Any changes are then reflected in the parent bulked order.

For example, if you accept a request from the care order originator to change the quantity from “6” to “8”, the
bulked order quantity changes from “12 to “14”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-modify.png)

**Note**: You cannot change the parent bulk order directly. Only the original care orders can be modified.

To remove one or more original care orders from the bulked order, right-click the order and select **Order
staging** | **Remove from bulk**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-remove.png)

The selected care orders are removed, and the quantity of the bulked order reflects the quantity of the remaining
original care orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-remove-result.png)

**Note**: If you cancel the parent bulked order, all child care orders and related working child orders will also
be canceled.

## Filling a bulked order

You can fill a bulked order by submitting child orders or by assigning fills. To submit orders, click the order
action **B** (Buy) or **S** (Sell) button in the B/S column for the parent bulked order to open the Order
Ticket. You can select the same account or a different account, and can select different order types as needed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-submit-order1.png)

Working child orders are native exchange orders and nested as part of the bulked order in the orders pane or Order
Book. As these orders are filled, the quantity of the bulked order is reduced. Fills are reported to the customer
based on whether or not the bulked order is locked.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-submit-order-display1.png)

When [assigning
fills](../../care-orders/task-care-orders/assigning-fills-to-care-orders.md) to a bulked order, you can only assign fills to the parent bulked order and not to the child care
orders or working child orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-assign-fills.png)

←[Previous PostBulking Care Orders](bulking-care-orders.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-modify.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-remove.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-original-remove-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-submit-order1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-submit-order-display1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-bulk-assign-fills.png
