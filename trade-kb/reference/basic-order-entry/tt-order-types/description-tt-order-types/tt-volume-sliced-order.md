---
title: TT Volume Sliced Order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-sliced-order/
---

# TT Volume Sliced Order

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-volume-sliced-order/)
>
> **Interpreted in:** [Order Types & Execution § Slicing family](../../../../guides/order-types-and-execution.md#slicing-family) · [Order Types & Execution § Order type reference table](../../../../guides/order-types-and-execution.md#order-type-reference-table)

A Volume Sliced order slices a large quantity order into smaller disclosed orders based on trading volume. The
resting portion may not be filled before there is enough trading volume to submit the next portion. The “Leftover”
parameter for a TT Volume Sliced order indicates how to handle the resting order when it is time to send the next
portion.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-volume-sliced-illustration.png)

## Behaviors

You can configure the following parent and child order behaviors for TT Volume Sliced orders:

* Defining the behavior of each child order slice:
  * [Setting the interval and quantity for each child order](#slice-details)
  * [Varying the quantities of child orders](#variable-qty)
* Specify when to submit child orders at a particular price:
  * [Set the type and price of each child order](#child-order-type)
  * [Set a leftover action for unfilled orders when a slice ends](#leftover-action)
  * [Aggressing the price of a working child based on market conditions](#wat)
* Set preconditions for the parent order:
  * [Triggering the parent order at a specific price level](#static-trigger)
  * [Using Stop and If-Touched trailing triggers to enter a TT Time Sliced parent order
    at a price level that trails the market](#trailing-trigger)
  * [Setting start and end times for a parent order](#times)

## Setting the interval and quantity of TT Volume Sliced child orders

To set the interval and quantity of child orders:

1. In the **Interval** field,set the volume of contracts that must be traded before disclosing a child
   order portion. The volume is defined by the exchange volume for the contract and may reflect more trades than
   indicated by summing the Last Traded Quantity (LTQ). This is because exchange volume sometimes includes volume
   from, for example, legs of calendar spread trades.
2. In the **Display** field, enter the amount of each child order to disclose, and select whether to
   disclose the portion as a set quantity (**Qty**) or percentage of the parent order quantity
   (**%**).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-child-slice-config.png)

   For example, if you enter a 500-lot order with these settings, the TT Volume Sliced parent order submits
   100-lot child orders each time 2000 contracts are traded until the 500-lot order is filled.

## Varying the quantities of the child order

Instead of submitting a fixed quantity for every child order you can use a variance to increase or reduce the
quantity of each child order by a random amount. This amount uses a percentage of the disclosed quantity as its
threshold.

To vary the disclosed quantity by a percentage of the order size:

1. Set the desired **Display** quantity. This quantity becomes the base quantity for calculating
   variance.
2. Set the **Variance** from the dropdown. This example sets the variance to 50%, so each child order
   could have an order quantity within 50% (+/- 5) of the base disclosed quantity.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config.png)
3. To see a proposed distribution of the child orders, click ![the magnifying glass button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-9.png). **Note**: You must specify the order quantity to see the
   distribution.A flyout shows the quantity of each child order that will be sent when you submit the parent order.

   ![TBD](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config-show-1.png)

   If you want to change the proposed distribution, you can continue to click ![the magnifying glass button](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-10.png) until you see a distribution you like.

   ![TBD](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config-2.png)

   **Note**: If you do not display the variance, or if you make any order change after displaying the
   variance distribution, the TT parent order will submit its child orders with random quantities within the
   specified variance until the total order quantity has been filled.
4. Submit the order at the desired side and price.If you entered a 100 lot order with these settings, the TT Volume Sliced parent order would submit an order for
   the first quantity (e.g., 11). Then, a new child order would be entered at each volume interval until all slices
   are submitted.

## Setting the type and price of the child order

For each set interval, the TT Volume Sliced parent order submits native child orders to the market at a specified
type and price. The following native order types are supported:

* Market order
* Limit order

  You can submit each child Limit order at the same price as the parent order or to use a price
  **Offset** based on the market at the time each child order is entered.

To configure the type and price of each child order:

1. In the **Order Type** dropdown, select the order type for the child orders.
2. If you select **Limit**, you can optionally set a relative price for the child order using an
   offset.

   In this example **Offset** is enabled with a value of “1”, so each child order is entered at a
   price level one tick away from the LTP at the time the slice is
   triggered.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-child-limit-offset-config.png)

## Setting a leftover action

The leftover action sets how to manage the resting child order when the next portion can be sent and the order is
not fully filled.

To set a leftover action, select one of the following:

* **Leave**: TT leaves the resting child order in the market when the next portion is submitted.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-action-config.png)
* **Payup**: Configures the resting child order to move a set number of ticks into the market. Set the
  number of ticks and select one of the following:
  * **At End**: Executes Payup ticks at the end of the **Interval** (default setting).
  * **At Half Life**: Executes Payup ticks after half of the **Interval**.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-payup-config.png)
* **Go to Market**: Cancels the resting Limit order and sends a Market order based on the following
  setting:
  * **At End**: Go to market at the end of the **Interval** (default setting).
  * **At Half Life**: Go to market after half of the **Interval**.
  * **Mkt Order Limit**: Sets the number of ticks from LTP to submit a Limit order through the
    opposite inside market. For example, “Go To Market” with “Mkt Order Limit” set to “1” will cancel the resting
    Limit order and submit a new Limit order at 1 tick through the market.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-goto-config.png)
* **Merge**: Merges unfilled child orders into a single order after each **Interval**.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-merge-config.png)

The following example shows using Payup ticks. If the child order is unfilled at the end of the interval, the order
will pay up two ticks to 3102.75.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-payup-mdt-1.png)

## Aggressing the price of a working child order based on market conditions

You can also apply [With A Tick](tt-with-a-tick-order.md) functionality to the child orders. This feature gives you the ability to work an order at one price and automatically pay up one tick when the quantity available at the opposite side drops below a user-defined threshold.

To configure With a Tick behavior:

1. Specify the desired quantity and price settings.
2. Enable **With a Tick** and set the quantity threshold.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-wat-qty-config.png)
3. Enter the order at the desired price level.If you entered a Buy order at the inside market, the TT Volume Sliced Order parent order will reprice its child order one tick when the quantity for the inside Ask falls below 20.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-wat-mdt-1.png)

   For this order:

   * **A** – When the quantity at this level falls below 20…
   * **B** – The TT Volume Sliced Order parent order will reprice its child order one tick higher.

TT gives users the option to set the **With a Tick** functionality with a percentage instead of a fixed quantity. For example, if you set **With a Tick** equal to 20%, instead of to a quantity, then:

* When the quantity on the opposite side of the market drops below 20% of your order’s quantity…
* Your order will aggress into the market by one tick.

## Triggering a TT Volume Sliced Order parent order at a specific price level

A TT Volume Sliced Order order type supports triggers that let you manage when to submit the parent order, which will then enter its child orders. You can set a trigger price, which puts the TT Volume Sliced Order parent order on hold until a trade occurs at a specific price level. When the market reaches that price level, the TT Volume Sliced Order parent order changes to Working state and submits its first child order. The TT Volume Sliced Order order type supports the following types of triggers:

* **If-Touched**: Triggers when a trade occurs at the specified price level or better
* **Stop**: Triggers when a trade occurs at the specified price level or worse.

After selecting the type of trigger, set a trigger price and trigger price type. The following trigger price types are supported:

* LTP: Any trade occurs at the specified price level.
* Bid/Ask: A trade on the selected side occurs at the specified price level.
* Same/Opposite Side: A trade occurs at the specified price on the specified side of the market relative to the TT Volume Sliced Order parent order.

To set a trigger for the TT Volume Sliced Order order to begin working when the market trades at a specific price on the same side as your Buy or Sell order, add a same-side If-Touched trigger as follows:

1. Enable **Trigger** to set a trigger for the order.
2. Select **If Touched** from the dropdown to trigger the TT Volume Sliced Order order when a trade occurs at the specified price or better.
3. For the **Trigger price**, enter the desired price at which to trigger the order.
4. Select **Same Side** from the drop-down to indicate the trade must occur at the inside market for the same side as the TT parent order. For example, if you enter the order as a Bid, the order will be triggered if a Buy order executes at the specified price.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-static-trigger-config.png)

If you clicked at any price level on the Buy side, the TT Volume Sliced Order parent order would resemble the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-static-trigger-mdt-1.png)

**Based on the specified parameters, the TT Volume Sliced Order parent order is entered into the market as follows:**

* The TT Volume Sliced Order parent order is placed at the specified trigger price of 178’12.
* The working quantity of the order you entered is 0 and will remain so until the order is triggered.
* When a Bid is filled at the 178’12 trigger price, the TT Volume Sliced Order parent order will begin working its child orders at that price level.

## Using Stop and If-Touched trailing triggers to enter a TT Volume Sliced Order parent order at a price level that trails the market

Instead of entering your TT Volume Sliced Order parent order at a specific price level, you can configure the TT Volume Sliced Order parent order to trail the market by setting the number of ticks away from the market to set your trigger.

* If the market moves away from your trigger, the trigger will reprice to remain the set number of ticks away
  from the market.
* If the market moves towards your trigger, the trigger will remain at its price level.

Adding a trailing component to a trigger causes it to behave as follows:

* **Trailing If-Touched triggers**
  * A Buy-side trigger is set a specified number of ticks below the market. When the market moves
    higher, the trigger follows the market and maintains its ticks away value; when the market moves
    lower, the trigger’s price does not move.
  * A Sell-side trigger is set a specified number of ticks above the market. When the market moves
    lower, the trigger follows the market and maintains its ticks away value; when the market moves
    higher, the trigger’s price does not move.
* **Trailing Stop triggers**
  * A Buy-side trigger is set a specified number of ticks above the market. When the market moves lower,
    the trigger follows the market and maintains its ticks away value; when the market moves higher, the
    trigger’s price does not move.
  * A Sell-side trigger is set a specified number of ticks below the market. When the market moves
    higher, the trigger follows the market and maintains its ticks away value; when the market moves
    lower, the trigger’s price does not move.

To set a trailing trigger for the TT Volume Sliced Order parent order:

1. Enable **Trigger** to set a trigger for the order.
2. From the dropdown, select the type of trailing trigger.
3. Enable the **Trail (ticks)** parameter to have the trigger trail the market.
4. Enter the desired number ticks away to trail the trigger price.
5. From the **Trigger price** drop-down, select the price type to trail.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-trailing-trigger-config.png)

If you clicked any price level on the Buy side, the TT Volume Sliced Order parent order would resemble the following.

![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-trailing-trigger-mdt-1.png)

**Based on the specified parameters, the TT Volume Sliced Order parent order is entered into the market as
follows:**

* The TT Volume Sliced Order parent order is placed at the trigger price of 3086.25.
* The working quantity of the order you entered is 0 and will remain so until the order is triggered.
* When a Bid is filled at the 3086.25 trigger price, the TT Volume Sliced Order parent order will begin working its
  child orders at that price level. If the market moves higher, the Stop trigger’s price will not move.

## Setting start and end times for a TT Volume Sliced Order parent order

By default, a TT Volume Sliced Order order begins working immediately after submission and continues to work until canceled. You can, however, customize when a TT Volume Sliced Order parent order begins working and when it stops.

To set start and stop times for a TT Volume Sliced Order parent order:

1. For the **Start** setting, click the dropdown arrow and select the desired [start time option](#start-options).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-8.png)

   In this example, you select **Time**.
2. Set a start date and time in the calendar selector, and click **Apply**.

   **Tip**: Use the “tab” key to navigate to the right between time edit boxes. Use “Shift + tab” to navigate left to an edit box.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-times-config.png)

   **Note**: If you specify a future start time, the Order Book will show the TT Volume Sliced Order parent order **Status** as **Working** and its **SynthStatus** as **Waiting**.
3. For the **End** setting, click the dropdown arrow and select one of the following:
   * **GTC**: Keeps the TT Volume Sliced Order parent order working until it is canceled.
   * **Time**: Sets a time and date for when the TT Volume Sliced Order parent order ends.
   * **Day**: Cancels the TT Volume Sliced Order parent order at the end of the trading session.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-8.png)

   **Note**: When creating or using an order template and using the **Time** option, the **Start** and **End** dates automatically adjust if originally set in the past.
4. Enter the order at the desired price level.If you placed the order with a future start time, the TT Volume Sliced Order parent order would appear in MD Trader and the Order Book similar to the following.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-times-mdt-ob.png)

   The Order Book shows the status of the future order.
   * **A** – The **Status** is **Working**, which indicates the TT Volume Sliced Order parent order is working on the Algo Server.
   * **B** – The **SynthStatus** is **Waiting**, which indicates the order has not yet started working in the market. When the start time is reached, the **SynthStatus** will also change to **Working**.

## TT Volume Sliced order parameters

Configuration parameters include: slice details, child order details, and precondition details.

### Slice details

* **Interval**:Sets the exchange volume needed to submit a child order portion.
* **Display**: Sets the displayed quantity, or the amount that is visible in the market.The displayed value can represent:
  * **Qty** for a specific number of contracts
  * **%** for a percentage of the total orderWhen the displayed quantity is specified as a percentage:
  * If the quantity is less than 1, the quantity rounds up to 1.
  * If the fractional portion is less than .5 (e.g. 3.2), the quantity rounds down.
  * If the fractional portion is greater than .5 (e.g. 3.7), the quantity rounds up.
  * If the fractional portion is exactly .5, the quantity rounds up.
* **Variance**: Sets the percentage (0-100) by which to vary the child order quantity.

### Child order details

* **Child order type**: Sets the type of exchange-native order to use for the order. Possible values include:
  * Limit
  * Market
* **Offset** — Sets the number of ticks away from the specified price to submit the order.
  This parameter is optional if the order type is “Limit”.The offset can be based on one of the following prices:
  * LTP
  * Ask
  * Bid
  * Same Side: Uses the inside market price in the Buy/Sell direction of the order:
    * Best Bid for Buys
    * Best Ask for Sells
  * Opposite Side: Uses the inside market price in the opposite Buy/Sell direction of the order:
    * Best Ask for Buys
    * Best Bid for Sells
* **With a Tick**: Sets the threshold for the [With A Tick](tt-with-a-tick-order.md) behavior that reprices the child order one tick toward the market when available quantity at the opposite inside market is at or below the specified quantity threshold.The quantity can be specified as:
  * **Qty** for an absolute number of contracts
  * **%** for a percentage of the initial quantity for this order
* **Leftover action** to specify how to handle any existing unfilled order quantities when it is time to send the next portion. Options include:
  * **Leave** to leave the resting child order portion in the market.
  * **Market** to cancel the resting child order portion and submit a market order for the remaining quantity.
  * **Payup** to change the price based upon the buy/sell direction of the order and the **Payup Ticks** value.
  * **Go to Market**: Cancels the resting Limit order and sends a Market order based on the following setting:
    * **At End**: Go to market at the end of the volume interval (default setting).
    * **At Half Life**: Go to market after half of the interval.
    * **Mkt Order Limit**: Sets the number of ticks from LTP to submit a Limit order through the opposite inside market.
  * **Merge**: Merges unfilled child orders into a single order after each interval.
* **Payup Ticks**: Sets the number of ticks to add or subtract from your Bid or Offer to determine the price of the Limit order. The Limit price is based on the Buy/Sell direction of the order. Optionally, select one of the following:
  * **At End**: Executes Payup ticks at the end of the volume interval (default setting).
  * **At Half Life**: Executes Payup ticks after half of the volume interval.
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

### Precondition details

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

**Note**: Using Same and Opposite sides instead of Bid and Ask lets you create a single order template that works when submitting either Buy or Sell orders instead of requiring separate templates for Buy and Sell orders.* **Trigger**: Sets the type of order trigger for the parent synthetic orderPossible types include:
  * Stop
  * If-Touched
* **Trail (ticks)**: Specifies the number of ticks away from the specified **Price Type** the order should trail the market.
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

←[Previous PostTT Volume Duration Order](tt-volume-duration-order.md)

[Next PostTT With A Tick order](tt-with-a-tick-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-volume-sliced-illustration.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-child-slice-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-9.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config-show-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-10.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-variable-qty-config-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-child-limit-offset-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-action-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-payup-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-goto-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-merge-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-leftover-payup-mdt-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-wat-qty-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-wat-mdt-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-static-trigger-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-static-trigger-mdt-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-trailing-trigger-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-trailing-trigger-mdt-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-times-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-8.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-volume-sliced-times-mdt-ob.png
