---
title: TT Bracket order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-bracket-order/
---

# TT Bracket order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-bracket-order/)

A TT Bracket order submits a Limit or Stop order accompanied by an OCO (one-cancels-other) order. When the original Limit or Stop order is filled, the child OCO order is automatically submitted. The OCO is set with a profit target offset and a stop loss offset from the price the trader places the original order. For each partial / full fill of the TT Bracket Limit order, a [TT OCO order](tt-oco-order.md) will be launched. The TT Bracket and TT OCO orders allow you to potentially lock in profits with a favorable move or prevent a downside loss without having to constantly monitor the position.

For example, a 10-lot TT Bracket order is submitted as a 10-lot Limit bid. If it gets partially filled for 7-lots, the TT Bracket order submits an OCO, which submits a child 7-lot Limit order at the specified profit target price and a 7-lot Stop Limit or Stop Market order at the protective stop-loss price. If the 7-lot OCO child Limit order is partially filled for 3-lots, then the OCO child Stop order is discounted by 3-lots. However, if the OCO Stop is triggered, the OCO Limit order will be canceled.

**Note**: If you change the quantity of one of the TT OCO child orders, it will not automatically change the quantity of the other order.

## TT Bracket example

In this example, a 50-lot bid is submitted as a TT Bracket order. The [Precondition details](#trigger-params) set the market conditions needed for the TT Bracket parent order to begin entering its OCO child orders. The TT Bracket order gets filled for 2 lots and submits a child OCO order for the 2-lot entry order fill. The OCO order then submits a child 2-lot Limit order at a profit target price, and a child 2-lot protective Stop order.

The 2-lot OCO orders continue to work in the market until either the OCO Limit order is filled or OCO Stop Limit order is triggered. A fill in the OCO Limit order discounts the quantity in the Stop
Limit order. However, if the 2-lot OCO Stop Limit order is triggered first, it submits another Limit order as a protective Stop and the 2-lot OCO Limit (profit) order is canceled.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-bracket-example5a.png)

## TT Bracket order parameters

### Order details

* **Order type**: Sets the order type for the parent TT Bracket entry order.Possible values include:
  * [Limit](../../order-ticket/description-order-ticket/order-types.md#limit-type)
  * [Stop Limit](../../order-ticket/description-order-ticket/order-types.md#stop-limit-type)
      
    **Payup**: Sets the number of ticks away from the Stop price to submit a Limit order.
  * [Stop Market](../../order-ticket/description-order-ticket/order-types.md#stop-market-type)
* **Profit target**: Sets the initial price for the profit order in the OCO pair:
  * Price = Entry Order Fill Price + Profit target setting, if the TT Bracket order was a bid.
  * Price = Entry Order Fill Price – Profit target setting, if the TT Bracket order was an offer.
* **Stop loss**: Sets the initial price for the stop loss order in the OCO pair:
  * Price = Entry Order Fill Price – Stop loss setting, if the TT Bracket order was a bid.
  * Price = Entry Order Fill Price + Stop loss setting, if the TT Bracket order was an offer.
* **Stop order type**: Sets the stop order type, market or limit, of the stop-loss order:
  * [Stop Limit](https://library.tradingtechnologies.com/trade/order-entry-order-types.html#stop-limit-type)
  * [Stop Market](https://library.tradingtechnologies.com/trade/order-entry-order-types.html#stop-market-type)
* **Stop order type**: Sets the stop order type, market or limit, of the stop-loss order:
  * [Stop Limit](../../order-ticket/description-order-ticket/order-types.md#stop-limit-type)
  * [Stop Market](../../order-ticket/description-order-ticket/order-types.md#stop-market-type)
  * [TT Stop](tt-oco-order.md#basic)For a TT Stop child order submitted as part of a TT OCO order, you can override/select the TIF of the native child order submitted by the TT Stop. The following TIFs can be selected if natively supported by the exchange:
  * Day
  * GTC
  * FOK
  * GTDate
  * IOC
* **Payup**: Sets the number of ticks away from the Stop price to submit a Limit
  order when the OCO Stop Limit order is triggered. Applies only if you set OCO stop order types as Stop Limit and it specifies the offset (in number of ticks) of the Limit order that will be placed if the Stop Limit is triggered.
* **With a Tick**: Sets the threshold for the [With A Tick](tt-with-a-tick-order.md) behavior that reprices the child order one tick toward the market when available quantity at the opposite inside market is at or below the specified quantity threshold.The quantity can be specified as:
  * **Qty** for an absolute number of contracts
  * **%** for a percentage of the initial quantity for this order
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

### Precondition details

The following trigger parameters specify the market conditions under which the parent order will begin entering its child orders.

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
* **At End Action** (shown only for custom **End Time**) — Sets the action to take for any unfilled balance when the **End Time** is reached:
  * **Cancel** — Cancels all child orders and stops the order type.

←[Previous PostTT Order Type Templates](tt-order-type-templates.md)

[Next PostTT Iceberg order](tt-iceberg-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-bracket-example5a.png
