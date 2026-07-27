---
title: TT Timed order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-timed-order/
---

# TT Timed order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-timed-order/)

Timed orders are used to manage a trading day (e.g., exit by market close). For instance, you might want to submit
an order as soon as the market opens, or exit a position just before the market closes. TT Timed order parameters
schedule an order’s start date and time and/or end date and time and may be included as part of all TT Order Type
orders.

The following describes the life cycle of a TT Timed order:

* An order submitted with a Start Date/Time is in the Waiting state.
* When the Start Date/Time is reached, the order goes into the Pending Trigger or Working state.
* When the End Date/Time is reached, the Algo Server deletes the parent order and associated child orders. If the
  trading session is closed when the End Date/Time is reached, the delete request will fail, leaving working GTC
  child orders on the exchange. It is the user’s responsibility to delete these orders when the exchange re‐opens.**Note**: Time in Force settings can override the End Date/Time. The Algo Server deletes timed orders when the
  exchange cancels the order. For example, when the exchange cancels GTD orders at the end of the trading session,
  the Algo Server deletes the order even if the End Date/Time has not been reached.

## Behaviors

The following examples illustrate how you can configure a TT Timed order with different behaviors for the child and
parent orders. Also, each example shows how the order will appear in MD Trader.

* Setting preconditions for the parent order
  * [Setting start and end times for a parent order](#times)
* Specifying the price at when child orders are entered
  * [Setting the type and price of the child order](#child-order-type)
  * [Aggressing the price of a working child based on market conditions](#wat)

## Setting start and end times for a TT Timed parent order

By default, a TT Timed order begins working immediately after submission and continues to work until canceled. You can, however, customize when a TT Timed parent order begins working and when it stops.

To set start and stop times for a TT Timed parent order:

1. For the **Start** setting, click the dropdown arrow and select the desired [start time option](#start-options).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-6.png)

   In this example, you select **Time**.
2. Set a start date and time in the calendar selector, and click **Apply**.

   **Tip**: Use the “tab” key to navigate to the right between time edit boxes. Use “Shift + tab” to navigate left to an edit box.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-times-config.png)

   **Note**: If you specify a future start time, the Order Book will show the TT Timed parent order **Status** as **Working** and its **SynthStatus** as **Waiting**.
3. For the **End** setting, click the dropdown arrow and select one of the following:
   * **GTC**: Keeps the TT Timed parent order working until it is canceled.
   * **Time**: Sets a time and date for when the TT Timed parent order ends.
   * **Day**: Cancels the TT Timed parent order at the end of the trading session.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-6.png)

   **Note**: When creating or using an order template and using the **Time** option, the **Start** and **End** dates automatically adjust if originally set in the past.
4. Enter the order at the desired price level.If you placed the order with a future start time, the TT Timed parent order would appear in MD Trader and the Order Book similar to the following.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-times-mdt-ob.png)

   The Order Book shows the status of the future order.
   * **A** – The **Status** is **Working**, which indicates the TT Timed parent order is working on the Algo Server.
   * **B** – The **SynthStatus** is **Waiting**, which indicates the order has not yet started working in the market. When the start time is reached, the **SynthStatus** will also change to **Working**.

## Setting the type and price of the child order

At the specified time, the TT Timed order will submit a single native child order to the market at a specific type
and price. You can choose the following types of native order types.

* Market order
* Limit orderYou can choose to use same price as the parent order for each child order or to use a price offset based on the
  market at the time each child order is entered.

To configure the type and price of the child order:

1. In the **Exch order Type** dropdown, select the desired order type for the child orders.If you select Limit, you can optionally enter a child order at a relative price using an offset.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-child-limit-config.png)

   With this setting, the child order will be entered at a price level two ticks away from the LTP at that time.

## Aggressing the price of a working child order based on market conditions

You can also apply [With A Tick](tt-with-a-tick-order.md) functionality to the child orders. This feature gives you the ability to work an order at one price and automatically pay up one tick when the quantity available at the opposite side drops below a user-defined threshold.

To configure With a Tick behavior:

1. Specify the desired quantity and price settings.
2. Enable **With a Tick** and set the quantity threshold.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-wat-config.png)
3. Enter the order at the desired price level.If you entered a Buy order at the inside market, the TT Timed parent order will reprice its child order one tick when the quantity for the inside Ask falls below 20.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-wat-mdt.png)

   For this order:

   * **A** – When the quantity at this level falls below 20…
   * **B** – The TT Timed parent order will reprice its child order one tick higher.

TT gives users the option to set the **With a Tick** functionality with a percentage instead of a fixed quantity. For example, if you set **With a Tick** equal to 20%, instead of to a quantity, then:

* When the quantity on the opposite side of the market drops below 20% of your order’s quantity…
* Your order will aggress into the market by one tick.

## TT Timed order parameters

The following parameters are required:

* **Exch order type**: Sets the type of exchange-native order to use for the order.Possible values include:
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
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.
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

←[Previous PostTT Time Sliced order](tt-time-sliced-order.md)

[Next PostTT Trailing Limit order](tt-trailing-limit-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-times-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-times-mdt-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-child-limit-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-wat-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-timed-wat-mdt.png
