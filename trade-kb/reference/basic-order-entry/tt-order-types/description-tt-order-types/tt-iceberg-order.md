---
title: TT Iceberg order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-iceberg-order/
---

# TT Iceberg order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-iceberg-order/)

A TT Iceberg order executes a large volume order by breaking it into smaller disclosed orders, publicly displaying only the specified portion instead of the full order quantity. When one disclosed portion fills, the next portion is entered into the market. This process continues until the order is filled.

## Behaviors

The following examples illustrate how you can configure a TT Iceberg order with different behaviors for the child and parent orders. Also, each example shows how the order will appear in MD Trader.

* Determining the disclosed quantities of the child orders
  * [Submitting child orders with a fixed quantity](#static-qty)
  * [Varying the quantities of child orders](#variable-qty)
* Specifying the price at which child orders are entered and worked
  * [Varying the prices of child orders](#offset-price)
  * [Aggressing the price of a working child order based on market conditions (WAT)](#wat)
* Setting preconditions for the parent order
  * [Triggering a TT Iceberg parent order at a specific price level](#static-trigger)
  * [Using Stop and If-Touched trailing triggers to enter a TT Iceberg parent order at a price level that trails the market](#trailing-trigger)
  * [Setting start and end times for a parent order](#times)

## Submitting child orders with a fixed quantity

A basic Iceberg order slices a large-quantity order into smaller-sized orders of a fixed quantity, all at the same price. A TT Iceberg lets you specify either a fixed quantity for every child order or specify the static quantity as a percentage of the total parent order quantity.

To set the same fixed quantity for each child order:

1. Select TT Iceberg from the order type dropdown to display the flyout.

   ![Display 20 Qty](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-qty-config.png)
2. Set **Display** to the desired quantity and select **Qty** from the **Display** dropdown.If you wanted to submit a percentage of the total order quantity instead, you could enter the desired percentage and select **%** from the **Display** dropdown.
3. Submit the order at the desired side and price.If you submitted a 100-lot Buy order at 2927.50 with a disclosed quantity of 20, the TT Iceberg parent order would resemble the following:

   ![Add PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-qty-mdt.png)

   * The disclosed (D:20) and working (W:20) quantities are both 20.
   * The remaining undisclosed quantity (U:80) is 80.After each child order is fully filled, the TT Iceberg will submit the next 20-lot order at 2927.50 until the total order quantity has been filled.

## Varying the quantities of the child order

Instead of submitting a fixed quantity for every child order you can use a variance to increase or reduce the quantity of each child order by a random amount. This amount uses a percentage of the disclosed quantity as its threshold.

To vary the disclosed quantity by a percentage of the order size:

1. Set the desired **Display** quantity. This quantity becomes the base quantity for calculating variance.
2. Set the **Variance** equal to the desired percentage of variance. This example sets the variance to 50%, so each child order could have an order quantity within 50% (+/- 4 ) of the base disclosed quantity.
   ![Add PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config.png)
3. To see a proposed distribution of the child orders, click ![the magnifying glass button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-4.png). **Note**: You must specify the order quantity to see the distribution.A flyout shows the quantity of each child order that will be entered when you submit the parent order.

   ![TBD](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config-show-1.png)

   If you want to change the proposed distribution, you can continue to click the refresh button ![the refresh button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-refresh.png) in the distribution panel until you see a distribution you like.

   ![TBD](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config-show-2.png)

   **Note**: If you do not display the variance, or if you make any order change after displaying the variance distribution, the TT Iceberg parent order will submit its child orders with random quantities within the specified variance until the total order quantity has been filled.
4. Submit the order at the desired side and price.If you submitted a 100-lot order at 2970.50 with the above display and variance settings, the TT Iceberg parent order would submit a 7-lot child order.
   After each child order is fully filled, the TT Iceberg will submit each subsequent order at 2970.50 with the varied quantity shown in the distribution.

## Varying the prices of child orders

The default behavior for a TT Iceberg is to submit each child order at the same price. TT Iceberg orders also let you dynamically set the price of each child order based on different market prices or on the price of the previous order. You can configure the TT Iceberg to determine the price for its child orders by offsetting the price a number of ticks away from the:

* LTP, Ask or Bid price of the market at the time the child order is submitted.
* Price of the last child order (PrevSlice).

To enter a child order using a price offset:

1. Enable the **Offset** parameter.
2. Enter the desired number of ticks away from the selected price type. Use positive numbers to move the price away from the market or negative numbers to move the price toward the market.
3. Select a price type in the **Offset** dropdown. In this case, **PrevSlice** causes the TT Iceberg parent order to calculate the price of the new child order based on the price of the previous child order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-offset-config.png)
If you placed a Buy order at 131’035, the TT Iceberg parent order would resemble the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-offset-mdt.png)

When each child order is fully filled, the TT Iceberg will submit its next child order at a price level one tick away from the price of the previous child order.

## Aggressing the price of a working child order based on market conditions

You can also apply [With A Tick](tt-with-a-tick-order.md) functionality to the child orders. This feature gives you the ability to work an order at one price and automatically pay up one tick when the quantity available at the opposite side drops below a user-defined threshold.

To configure With a Tick behavior:

1. Specify the desired quantity and price settings.
2. Enable **With a Tick** and set the quantity threshold.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-wat-config.png)
3. Enter the order at the desired price level.If you entered a Buy order at the inside market, the TT Iceberg parent order will reprice its child order one tick when the quantity for the inside Ask falls below 20.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-wat-mdt.png)

   For this order:

   * **A** – When the quantity at this level falls below 20…
   * **B** – The TT Iceberg parent order will reprice its child order one tick higher.

TT gives users the option to set the **With a Tick** functionality with a percentage instead of a fixed quantity. For example, if you set **With a Tick** equal to 20%, instead of to a quantity, then:

* When the quantity on the opposite side of the market drops below 20% of your order’s quantity…
* Your order will aggress into the market by one tick.

## Triggering a TT Iceberg parent order at a specific price level

A TT Iceberg order type supports triggers that let you manage when to submit the parent order, which will then enter its child orders. You can set a trigger price, which puts the TT Iceberg parent order on hold until a trade occurs at a specific price level. When the market reaches that price level, the TT Iceberg parent order changes to Working state and submits its first child order. The TT Iceberg order type supports the following types of triggers:

* **If-Touched**: Triggers when a trade occurs at the specified price level or better
* **Stop**: Triggers when a trade occurs at the specified price level or worse.

After selecting the type of trigger, set a trigger price and trigger price type. The following trigger price types are supported:

* LTP: Any trade occurs at the specified price level.
* Bid/Ask: A trade on the selected side occurs at the specified price level.
* Same/Opposite Side: A trade occurs at the specified price on the specified side of the market relative to the TT Iceberg parent order.

To set a trigger for the TT Iceberg order to begin working when the market trades at a specific price on the same side as your Buy or Sell order, add a same-side If-Touched trigger as follows:

1. Enable **Trigger** to set a trigger for the order.
2. Select **If Touched** from the dropdown to trigger the TT Iceberg order when a trade occurs at the specified price or better.
3. For the **Trigger price**, enter the desired price at which to trigger the order.
4. Select **Same Side** from the drop-down to indicate the trade must occur at the inside market for the same side as the TT parent order. For example, if you enter the order as a Bid, the order will be triggered if a Buy order executes at the specified price.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-trigger-config.png)

If you clicked at any price level on the Buy side, the TT Iceberg parent order would resemble the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-trigger-mdt.png)

**Based on the specified parameters, the TT Iceberg parent order is entered into the market as follows:**

* The TT Iceberg parent order is placed at the specified trigger price of 2958.00.
* The working quantity of the order you entered is 0 and will remain so until the order is triggered.
* When a Bid is filled at the 2958.00 trigger price, the TT Iceberg parent order will begin working its child orders at that price level.

## Using Stop and If-Touched trailing triggers to enter a TT Iceberg parent order at a price level that trails the market

You can also use trailing price triggers to determine when to start working a TT Iceberg parent order. Instead of entering your TT Iceberg parent order at a specific-price level, you can have the TT Iceberg parent order trail the market. You specify the number of ticks away from the market to set your trigger.

* If the market moves away from your trigger, your trigger will reprice to remain the specified number of ticks away from the market.
* If the market moves towards your trigger, the trigger will remain at its price level.

Adding a trailing component to a trigger causes the trigger to behave as follows:

* **Trailing If-Touched triggers**
  * A buy-side trigger sets the trigger a specified number of ticks below the market. When the market moves higher, the trigger follows the market and maintains its ticks away value; when the market moves lower, the trigger’s price does not move.
  * A sell-side trigger sets the trigger a specified number of ticks above the market. When the market moves lower, the trigger follows the market and maintains its ticks away value; when the market moves higher, the trigger’s price does not move.
* **Trailing Stop triggers**
  * A buy-side trigger sets the trigger a specified number of ticks above the market. When the market moves lower, the trigger follows the market and maintains its ticks away value; when the market moves higher, the trigger’s price does not move.
  * A sell-side trigger the trigger a specified number of ticks below the market. When the market moves higher, the trigger follows the market and maintains its ticks away value; when the market moves lower, the trigger’s price does not move.

To set a trailing trigger for the TT Iceberg parent order:

1. Enable **Trigger** to set a trigger for the order.
2. From the dropdown, select the type of trailing trigger.
3. Enable the **Trail (ticks)** parameter to have the trigger trail the market.
4. Enter the desired number ticks away to trail the trigger price.
5. From the **Trigger price** drop-down, select which price to trail.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-trailing-config.png)

**If you clicked any price level on the Buy side, the TT Iceberg parent order would resemble the following.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-trailing-buy-stop-mdt.png)

**Based on the specified parameters, the TT Iceberg parent order is entered into the market as follows:**

* Because you set a Stop trigger three ticks away from the LTP, the TT Iceberg parent order is placed at 124’135.
* The working quantity of the order you entered is 0 and will remain so until the order is triggered.
* When the LTP reaches the trigger price, the TT Iceberg parent order will begin working its child orders at that price level.

## Setting start and end times for a TT Iceberg parent order

By default, a TT Iceberg order begins working immediately after submission and continues to work until canceled. You can, however, customize when a TT Iceberg parent order begins working and when it stops.

**Note**: If you specify both a trigger and a future start time, the start time takes precedence. When the specified start time is reached, the TT Iceberg parent order will begin working and evaluate the trigger condition at that time.

To set start and stop times for a TT Iceberg parent order:

1. For the **Start** setting, click the dropdown arrow and select the desired [start time option](#start-options).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-2.png)

   In this example, you select **Time**.
2. Set a start date and time in the calendar selector, and click **Apply**.

   **Tip**: Use the “tab” key to navigate to the right between time edit boxes. Use “Shift + tab” to navigate left to an edit box.

   **Note**: If you specify a future start time, the Order Book will show the TT Iceberg parent order **Status** as **Working** and its **SynthStatus** as **Waiting**.
3. For the **End** setting, click the dropdown arrow and select one of the following:
   * **GTC**: Keeps the TT Iceberg parent order working until it is canceled.
   * **Time**: Sets a time and date for when the TT Iceberg parent order ends.
   * **Day**: Cancels the TT Iceberg parent order at the end of the trading session.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-2.png)

   **Note**: When creating or using an order template and using the **Time** option, the **Start** and **End** dates automatically adjust if originally set in the past.
4. Enter the order at the desired price level.If you placed the order with a future start time, the TT Iceberg parent order would appear in MD Trader and the Order Book similar to the following.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-times-mdt-ob.png)

   The Order Book shows the status of the future order.
   * **A** – The **Status** is **Working**, which indicates the TT Iceberg parent order is working on the Algo Server.
   * **B** – The **SynthStatus** is **Waiting**, which indicates the order has not yet started working in the market. When the start time is reached, the **SynthStatus** will also change to **Working**.

## TT Iceberg order parameters

### Iceberg details parameters

The following parameters determine how the TT Iceberg parent order manages its child orders.

* **Display**: Sets the displayed quantity, or the amount that is visible in the market.The displayed value can represent:
  * **Qty** for a specific number of contracts
  * **%** for a percentage of the total orderWhen the displayed quantity is specified as a percentage:
  * If the quantity is less than 1, the quantity rounds up to 1.
  * If the fractional portion is less than .5 (e.g. 3.2), the quantity rounds down.
  * If the fractional portion is greater than .5 (e.g. 3.7), the quantity rounds up.
  * If the fractional portion is exactly .5, the quantity rounds up.
* **Variance**: Sets the percentage (0-100) by which to vary the child order quantity.
* **Offset** — Sets the number of ticks away from the specified price to submit the order.
  This parameter is optional if the order type is “Limit”.The offset is based on the following price:
  * LTP, which places the order the specified number ticks away from the last-traded price
  * Ask, which places the order the specified number ticks away from the Ask price
  * Bid, which places the order the specified number ticks away from the Bid price
  * PrevSlice, which places the order at the user-specified price and then calculates the offset for each subsequent
    order based on the price of the previous order slice
  * Same Side: which places the order at the inside market price in the Buy/Sell direction of the order:
    * Best Bid for Buys
    * Best Ask for Sells
  * Opposite Side: which places the order at the inside market price in the opposite Buy/Sell direction of the order:
    * Best Ask for Buys
    * Best Bid for Sells
* **With a Tick**: Sets the threshold for the [With A Tick](tt-with-a-tick-order.md) behavior that reprices the child order one tick toward the market when available quantity at the opposite inside market is at or below the specified quantity threshold.The quantity can be specified as:
  * **Qty** for an absolute number of contracts
  * **%** for a percentage of the initial quantity for this order
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

### Precondition settings parameters

The following trigger parameters specify the market conditions under which the TT Iceberg parent order will begin entering its child orders.

* **Trigger**: Sets the type of order trigger for the parent synthetic orderPossible types include:
  * Stop
  * If-Touched
* **Trigger Price**: Sets the price at which to trigger the parent synthetic order.Possible values include:
  * LTP: Last Traded Price
  * Ask: Best Ask
  * Bid: Best Bid
  * Same Side: Evaluates the trigger using the inside market price in the Buy/Sell direction of the order:
    * Best Bid for Buys
    * Best Ask for Sells
  * Opposite Side: Evaluates the trigger using the inside market price in the opposite Buy/Sell direction of the order:
    * Best Ask for Buys
    * Best Bid for Sells

**Note**: Using Same and Opposite sides instead of Bid and Ask lets you create a single order template that works when submitting either Buy or Sell orders instead of requiring separate templates for Buy and Sell orders.* **Trail (ticks)**: Specifies the number of ticks away from the specified **Price Type** the order should trail the market.
* **Start**: Sets the date and time to start executing the order.

  Values include:

  * **Now** to start the order immediately
  * **Time** to display a date/time picker for you to indicate when to start the order
  * **Pre-open** to enter the order at the pre-open state defined by an exchange
  * **Open** to enter the order when the exchange opens its trading session
* **End**: Sets the time to stop executing the logic of the orderPossible values include:
  * **GTC**, which leaves the order working until canceled
  * **Time**, which displays a date/time picker for you to indicate when to stop the order
  * **Day**, which leaves the order working until the market closes
  If End Time is selected and the End Time is reached, the order is deleted and the specified End Action is applied to its child orders. If the trading session is closed when the End Time is reached, the delete request will fail, leaving working GTC child orders on the exchange. It is your responsibility to delete these orders when the exchange re-opens.
* **At End Action**: Sets the action to take for any unfilled balance when the **End** time is reached. Visible only for a custom **End** time.

  Possible values include:

  * **Cancel** — Cancels all child orders and stops the order type.
  * **Go to Market** — Cancels the resting Limit order and submits a Market order. When selected, the “Mkt Order Lmt ticks” option is displayed.
  * **Mkt Order Lmt ticks** — Sets the number of ticks from LTP to submit a Limit order through the opposite inside market. If the checkbox is checked: all child orders are canceled, a Limit order is submitted for the unfilled quantity at a price that’s a set number of ticks from LTP, and the order type is stopped. If the checkbox is unchecked: all child orders are canceled, a Market order is submitted for the unfilled quantity, and the order type is stopped.

←[Previous PostTT Bracket order](tt-bracket-order.md)

[Next PostTT If-Touched order](tt-if-touched-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-qty-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-qty-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config-show-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-refresh.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-variable-qty-config-show-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-offset-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-offset-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-wat-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-wat-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-trigger-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-static-trigger-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-trailing-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-trailing-buy-stop-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-iceberg-times-mdt-ob.png
