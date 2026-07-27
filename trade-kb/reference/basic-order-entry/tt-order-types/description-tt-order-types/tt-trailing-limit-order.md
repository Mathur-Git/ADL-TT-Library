---
title: TT Trailing Limit order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-trailing-limit-order/
---

# TT Trailing Limit order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-trailing-limit-order/)

A TT Trailing Limit order submits a native limit exchange order into the market then dynamically adjusts the price to stay within a specified distance of the market if it moves away. This means:

* A Buy Trailing Limit sets the price a fixed amount below the market price. The order moves higher if the market moves above the highest recent price. The order will not adjust if the market moves lower.
* A Sell Trailing Limit sets the price a fixed amount above the market price. The order moves lower if the market moves below the lowest recent price. The order does not adjust if the market moves up.

The following describes the life cycle of a TT Trailing Limit order:

* A TT Trailing Limit order submitted with a Start Date/Time is in the Waiting state.
* A TT Trailing Limit order goes into the Working state when the Start Time is reached or when the order is entered without a Start Date/Time. A single child order is placed in the market. The
  trailing parameters dynamically re‐price the child order as the market moves.

## Behaviors

The following examples illustrate how you can configure a TT Trailing Limit order order with different behaviors for the child and parent orders. Also, each example shows how the order will appear in MD Trader.

* Specifying the price at when child orders are entered
  * [Triggering a TT Trailing Limit parent order at a price level that trails the market](#trigger)
* Setting preconditions for the parent order
  * [Setting start and end times for a TT Trailing Limit order parent order](#times)

## Triggering a TT Trailing Limit parent order at a price level that trails the market

To enter a trailing limit order:

1. From the **Trail Price Type** dropdown, select the price off which you want to trigger.
2. For **Trail (ticks)**, enter the number of ticks to trail the selected price type.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-config.png)

   If you clicked somewhere on the Sell side, the TT Trailing Limit parent order would resemble the following.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-mdt.png)

## Setting start and end times for a TT Trailing Limit parent order

By default, a TT Trailing Limit order begins working immediately after submission and continues to work until canceled. You can, however, customize when a TT Trailing Limit parent order begins working and when it stops.

To set start and stop times for a TT Trailing Limit parent order:

1. For the **Start** setting, click the dropdown arrow and select the desired [start time option](#start-options).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-5.png)

   In this example, you select **Time**.
2. Set a start date and time in the calendar selector, and click **Apply**.

   **Tip**: Use the “tab” key to navigate to the right between time edit boxes. Use “Shift + tab” to navigate left to an edit box.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-times-config.png)

   **Note**: If you specify a future start time, the Order Book will show the TT Trailing Limit parent order **Status** as **Working** and its **SynthStatus** as **Waiting**.
3. For the **End** setting, click the dropdown arrow and select one of the following:
   * **GTC**: Keeps the TT Trailing Limit parent order working until it is canceled.
   * **Time**: Sets a time and date for when the TT Trailing Limit parent order ends.
   * **Day**: Cancels the TT Trailing Limit parent order at the end of the trading session.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-5.png)

   **Note**: When creating or using an order template and using the **Time** option, the **Start** and **End** dates automatically adjust if originally set in the past.
4. Enter the order at the desired price level.If you placed the order with a future start time, the TT Trailing Limit parent order would appear in MD Trader and the Order Book similar to the following.

   ![ADD PIC](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-times-mdt-ob.png)

   The Order Book shows the status of the future order.
   * **A** – The **Status** is **Working**, which indicates the TT Trailing Limit parent order is working on the Algo Server.
   * **B** – The **SynthStatus** is **Waiting**, which indicates the order has not yet started working in the market. When the start time is reached, the **SynthStatus** will also change to **Working**.
   * **C** – Because a TT Trailing Limit parent order cannot determine the initial price of a future order, it cannot be displayed in the ladder so displays the order as a callout. For more information, see [.](../../md-trader/description-md-trader/trading-with-md-trader.md#timed-order-display)

## TT Trailing Limit order parameters

### Trailing Limit details parameters

* **Trailing Price Type**: Sets the price used to calculate the trailing price relative to the marketYou can trigger the following prices:
  * LTP
  * Ask
  * Bid
* **Trail (ticks)**: Specifies the number of ticks away from the specified **Price Type** the order should trail the market.
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

### Precondition details parameters

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

←[Previous PostTT Timed order](tt-timed-order.md)

[Next PostTT Volume Duration Order](tt-volume-duration-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-start-time-dropdown-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-times-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-end-time-dropdown-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-trailing-limit-times-mdt-ob.png
