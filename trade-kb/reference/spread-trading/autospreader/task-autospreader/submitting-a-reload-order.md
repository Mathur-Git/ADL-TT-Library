---
title: Submitting a Reload Order
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-a-reload-order/
---

# Submitting a Reload Order

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-a-reload-order/)

When quoting in more than one leg and one of the leg orders is filled, the remaining quoting orders will continue to work in the market to keep your queue position for the next disclosed spread order quantity.

To submit a reload order:

1. Launch the desired spread in an MD Trader widget.
2. Specify the standard order parameters; then enable the **RLD** button and specify the total order and disclosed order quantities.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-1.png)
3. Enter the order at the desired side and price level.

   The following example shows a reload order with a quantity of 100 that is disclosed to the market 20 at a time.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-2.png)

You can also configure a reload order to enter the market at the same price as the previous spread order or a set number of ticks away from previously disclosed order price. For example:

* If the offset is 0, the next disclosed order is submitted at the same price as the previous order.
* If the offset is 1, the next disclosed order is submitted one tick away from the market from the previous order price.
* If the offset is -2, the next disclosed order is submitted two ticks toward the market from the previous order price.

The following example shows a reload order with an offset of 1.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-offset-example.png)

←[Previous PostSubmitting an Autospreader Order](submitting-an-autospreader-order.md)

[Next PostSubmitting a Sniper Order](submitting-a-sniper-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-reload-offset-example.png
