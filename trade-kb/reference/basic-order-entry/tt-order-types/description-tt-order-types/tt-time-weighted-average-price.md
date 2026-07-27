---
title: TT Time Weighted Average Price
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-weighted-average-price/
---

# TT Time Weighted Average Price

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-weighted-average-price/)

TT Time Weighted Average Price (**TWAP**) may be used to fill large orders when a trader wants to keep the executed trade price as close as possible to the average market price without alerting other market participants to order volume.

**TWAP** avoids conspicuous trades by breaking up an order into smaller slices and submitting those to the market incrementally and systematically, according to a calculated plan, similarly to how the [TT Time Duration](tt-time-duration-order.md) order type does.
Plan behavior may be configured to suit the trader’s goals by setting parameters for
[fill duration](#setting-fill-duration),
[child order size per slice](#setting-childorder-size-per-slice),
[trading style](#selecting-trade-style),
[price triggers](#setting-would-if), and
[price limits](#setting-price-limits).

TT TWAP is available for use on all listed exchange products as well as on [Autospreader](../../../spread-trading/autospreader/description-autospreader/introduction-to-autospreader.md).

## Time Weighted Average Price Order Parameters

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-config.png)xml encoding="utf-8" ?

| # | Parameter Name | Required / Optional | Description |
| --- | --- | --- | --- |
| 1 | **Edit** | N/A | The **Edit** button shows the **TT TWAP Details** pane, where parameters for the trade can be entered or adjusted. |
| 2 | **Order Quantity** | Required | The **Order Quantity** field is used to specify the total number of orders for the trade. |
| 3 | **Duration Type** | Required | **Duration Type** defines the execution period for the parent trade.   Options:   * **Duration** *(Default)* — This option sets the total time, from now, to fill the total order quantity.  * **StartEnd** — This option causes a delayed start, setting begin and end times for the trade. The difference between the two time stamps determines the total duration for filling the orders.   **Note:** A defined STime/ETime in the future outside the existing trading session is not currently supported. |
| 4 | **Max Display %** | Required | **Max Display Percentage** specifies the maximum size of a child order lot in relation to the total parent order quantity.   Input:   * Integer between 1 and 100 *(default = 10)* |
| 5 | **Style** | Required | **Style** defines how the algorithm [lays out the slices and execution](#setting-style) options:  * **Aggressive** — Child orders are sent as market orders at the beginning of each slice. Child order quantities and time periods are uniform across each slice.  * **Passive** — A **Limit Order**  is placed at the **bid** *(for buys)* / **ask** *(for sells)* at the beginning of each slice and then continuously repriced to follow the market.  At the end of the slice, any unfilled **Limit Order** is cancelled, a **Market Order** is sent for any remaining quantity.  Time periods are uniform across slices but quantities vary with a 99% randomization around `(Total Qty x Max Disp %) / 2`.  * **Default** — Similar to the **Passive** style, a **Limit Order** is placed at the **bid** *(for buys)* / **ask** *(for sells)* at the beginning of each slice and then continuously repriced to follow the market. For every 10 lots traded, a quantity of 1 is decremented from the **Limit Order** and sent as a 1-lot **Market Order**. At the end of the slice, any unfilled **Limit Order** is cancelled and a **Market Order** is sent for any remaining quantity. Time periods are uniform across slices but quantities vary with a 99% randomization around `(Total Qty x Max Disp %) / 2`.   **Note:** If the exchange does not support market orders, a limit order of five ticks is submitted through the market. |
| 6 | **Would If Price** | Optional | **Would If Price** is a desired price threshold that will trigger TWAP to temporarily abandon its current slicing plan and aggressively fill as much quantity as possible as long as quantity is available on the opposite side of the market at the specified price, or lower *(for buys)*, or higher *(for sells)*. The algo then re-plans slices for any remaining quantity and resumes its execution.   Input:  * Price in Display format |
| 7 | **Limit Price** | Optional | **Limit Price** defines the highest price at which the user is willing to buy *(when buying)*, or the lowest to sell *(when selling)*.    Input:  * Price in Display format  **Note:** If this option is used, a portion of the order could go unfilled at the end of the set duration and remain working until filled or expired. |

## Behavior

### Setting the Fill Duration

From the TT TWAP **Details** pane:

1. Select **Duration** or **StartEnd** from the dropdown.
2. If selecting **Duration**, enter an integer or decimal in the text box and select the unit of time:
   * **hour** *(hr)*
   * **minute** *(min)*, or
   * **second** *(sec)*![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-enter-duration-length-4.png)
3. If selecting **StartEnd**, click on **End** to bring up the calendar widget, and select the target time for completing the trade.![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-select-trade-end-time-4.png)By default, **Now** is selected as the start time. You can delay the start time by clicking **Now** and selecting **Time** from the dropdown, which will bring up a calendar widget like before.  
     
   **Note**: **Start** time must be less than or equal to the **End** time. By default, **End** time is set to one hour from **Start**. Duration may be edited after TT TWAP is launched. However, changing the value cancels all pending child orders in the current plan, re-plans, and restarts the algo.

### Setting Child order Size per Slice

**Max Display %** sets a limit on child order size based on the total size of the order.

From the TWAP Details pane:

1. Set a maximum percentage, by entering an **integer** into the **Max Display %** textbox, or by incrementing or decrementing the count with the arrow buttons.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-max-display.png)  
      
   **Note:** Changing this parameter after the algo has begun cancels all pending child orders, re-plans the strategy, then restarts the algo.

When calculating child order quantities, TWAP may be limited by the instrument’s Round Lot Quantity (RLQ). When this occurs, TWAP dynamically merges the quantities to the lowest acceptable RLQ which may result in slices with a quantity of 0.

**Note:** An instrument’s Round Lot Quantity may result in child orders with quantities of 0.

For example, entering a 20 lot TWAP order and setting **Max Display %** equal to **10** normally results in slices with quantities up to 2 lots. However, if the instrument has a RLQ of 5, then a 2 lot slice would not be accepted by the exchange. In this case, TWAP calculates a slice schedule that includes both 0 and 5 lot quantities for the child orders. Depending on randomization of child slices, the first slice may equal a quantity of 0.

### Selecting a Trading Style

Selecting a **Style** sets the trade execution behavior for the child orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-select-trade-style.png)

From the TT TWAP **Details** pane, execution can be set to:
**Aggressive**,
**Default**, or
**Passive**.

### Setting a Price Trigger *(Would If Price)*

From the TT TWAP **Details** pane:

1. Select **Would If Price** by ticking the checkbox.
2. Specify a price in TT’s Price Display format.   
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-what-if-price.png)

### Setting a Price Limit

From the TT TWAP **Details** pane:

1. Select **Limit Price** by ticking the checkbox.
2. Specify a price in TT’s Price Display format.  
    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-limit-price.png)

←[Previous PostTT Time Duration order](tt-time-duration-order.md)

[Next PostTT Time Sliced order](tt-time-sliced-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-enter-duration-length-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-select-trade-end-time-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-max-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-select-trade-style.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-what-if-price.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-twap-limit-price.png
