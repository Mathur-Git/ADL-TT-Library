---
title: TT If-Touched order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-if-touched-order/
---

# TT If-Touched order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-if-touched-order/)

An If-Touched is an order that is triggered when the market has reached or traded through a specified price in the
market. If-Touched orders are similar to Stop orders except the trigger price behavior is inverted. An If-Touched
trigger price is typically set better than the current market.

Buy If-Touched orders are generally placed below the current last traded price while, Sell If-Touched orders are
generally placed above the current last traded price.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-if-touched-illustration.bmp)

The following is an example of a Trailing If-Touched order that triggers when a trade occurs and there is available
quantity at the selected last traded price. Once triggered, the TT If-Touched order submits a child order placed three
ticks into the market relative the LTP.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-if-touched-config.png)

## TT If-Touched order parameters

### Trigger details parameters

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

**Note**: Using Same and Opposite sides instead of Bid and Ask lets you create a single order template that works when submitting either Buy or Sell orders instead of requiring separate templates for Buy and Sell orders.**Tip**: A dropdown for this value is added to the [MD
Trader](../../md-trader/description-md-trader/trading-with-md-trader.md) Order Entry Panel to let you set the value without needing to reopen the flyout panel.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-if-touched-mdt-order.png)

**Note**: If you click a [custom action button](../../md-trader/task-md-trader/configuring-md-trader.md#buttons)
(or use a [hotkey](../../../overview/preferences/description-preferences/hotkeys-preferences.md)) for this TT Order Type that also specifies an order
template, these two fields will not be displayed, as the template already defines their desired values.
Right-clicking on the button displays these parameters. You can also click the **edit** button to
make changes, if desired.

* (Secondary Qty Trigger): Sets a secondary trigger condition based on:
  * Executed quantity when the Price Type parameter is **LTP**
  * Quantity of the best ask when the Price Type parameter is **Ask**
  * Quantity of the best bid when the Price Type parameter is **Bid**You can select a quantity or a percentage and select whether to use >= or
* **Reset on revert**: Resets the trade quantity counter back to zero, if the inside market
  backs away from the trigger price.**Note**: This property is for trigger orders waiting for a specific quantity to trade at a specific price level. If the product trades beyond the trigger price, the order is triggered regardless of the quantity traded.
* **Trail (ticks)**: Specifies the number of ticks away from the specified **Price Type** the order should trail the market.
* **Secondary Condition**: Optional condition to require before triggering the order. The order is triggered only when the initial and secondary conditions are both TRUE.**Note**: When specifying a second condition, exactly one of the conditions must use an LTP trigger.
  * **Trigger Price**: Sets the price at which to trigger the parent synthetic order.Possible values include:
    * LTP: Last Traded Price
    * Ask: Best Ask
    * Bid: Best Bid
    * Same Side: Evaluates the trigger using the inside market price in the Buy/Sell direction of the order:
      * Best Bid for Buys
      * Best Ask for Sells
    * Opposite Side: Evaluates the trigger using the inside market price in the opposite Buy/Sell direction of the order:
      * Best Ask for Buys
      * Best Bid for Sells**Note**: Using Same and Opposite sides instead of Bid and Ask lets you create a single order template that works when submitting either Buy or Sell orders instead of requiring separate templates for Buy and Sell orders.
* (Secondary Qty Trigger): Sets a secondary trigger condition based on:
  * Executed quantity when the Price Type parameter is **LTP**
  * Quantity of the best ask when the Price Type parameter is **Ask**
  * Quantity of the best bid when the Price Type parameter is **Bid**You can select a quantity or a percentage and select whether to use >= or
* **Trail (ticks)**: Specifies the number of ticks away from the specified **Price Type** the order should trail the market.
* **On trigger submit**: Sets the type of exchange-native order to submit when the order is triggered.Possible values include:
  * Limit order
  * Market order
* **Payup** – Sets the number of ticks from the specified price to submit the Limit order. Positive values indicate towards the market and negative values indicate away from the market.The offset is based on the following prices:
  * LTP: Last Traded Price
  * Ask: Best Ask
  * Bid: Best Bid
  * Trigger: Trigger price
  * Same Side: Evaluates the trigger using the inside market price in the Buy/Sell direction of the order:
    * Best Bid for Buys
    * Best Ask for Sells
  * Opposite Side: Evaluates the trigger using the inside market price in the opposite Buy/Sell direction of the order:
    * Best Ask for Buys
    * Best Bid for Sells**Tip**: An entry field for this value is added to the [MD Trader](https://mdt-trading-with-mdtrader.html) Order Entry Panel to let you set the value without needing to reopen the flyout panel.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-stop-mdt-order.png)

  **Note**: If you click a [custom action button](../../md-trader/task-md-trader/configuring-md-trader.md#buttons) (or use a [hotkey](../../../overview/preferences/description-preferences/hotkeys-preferences.md)) for this TT Order Type that also specifies an order template, these two fields will not be displayed, as the template already defines their desired values.Right-clicking on the button displays these parameters. You can also click the **edit** button to make changes if desired.
* **Limit price**: Sets the price for the child Limit order.
* **With a Tick**: Sets the threshold for the [With A Tick](tt-with-a-tick-order.md) behavior that reprices the child order one tick toward the market when available quantity at the opposite inside market is at or below the specified quantity threshold.The quantity can be specified as:
  * **Qty** for an absolute number of contracts
  * **%** for a percentage of the initial quantity for this order
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

### Timing parameters

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

←[Previous PostTT Iceberg order](tt-iceberg-order.md)

[Next PostTT OCO order](tt-oco-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-if-touched-illustration.bmp
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-if-touched-config.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-if-touched-mdt-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-stop-mdt-order.png
