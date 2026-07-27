---
title: TT With A Tick order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-with-a-tick-order/
---

# TT With A Tick order

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-with-a-tick-order/)

A With A Tick (WAT) order is a limit order that is automatically repriced one tick towards the market based on the price and quantity of the opposite inside market as follows:

* When best available price is more than one tick away from the limit price, the WAT order is repriced.
* If the best available price is one tick away and the available quantity drops below a specified threshold, the WAT order is repriced.

The WAT threshold is a parameter set by the user in one of two ways:

* **Qty**: The threshold is an absolute value. For example, you could place a buy order and join the best bid with a WAT threshold of 100. When the best ask quantity drops below 100, the buy order price will be repriced one tick higher.
* **%**: The threshold is a percentage of the WAT order quantity. For example, if the quantity on the opposite side of the market drops below 20% of your order’s quantity, then your order will aggress into the market by one tick.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-with-a-tick-config.png)

TT also allows you to add With A Tick behavior to all child orders of other TT Order Types, except for [TT Trailing Limit](tt-trailing-limit-order.md).

## TT With A Tick order parameters

* **With a Tick**: Sets the threshold to reprice the order.The quantity can be specified as:
  * **Qty** for an absolute number of contracts
  * **%** for a percentage of the initial quantity for this order
* **Exch order type**: The order type for the child order. (Currently, only Limit orders are supported.)
* **Offset**: The number of ticks away from the specified price to submit the order, based on the following price:
  * LTP
  * Ask
  * Bid
* **Auto-Resubmit Upon GTD Expiry**: Valid only when the child order TIF is **Day** (GTD). If any child orders are not completely filled by the session close, the exchange will expire the child orders; when the market reopens, the parent order will then resubmit the child orders with the same parameters as when they expired.

←[Previous PostTT Volume Sliced Order](tt-volume-sliced-order.md)

[Next PostTT Autohedger](tt-autohedger.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-with-a-tick-config.png
