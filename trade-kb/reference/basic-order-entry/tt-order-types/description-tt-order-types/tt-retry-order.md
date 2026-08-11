---
title: TT Retry order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-retry-order/
---

# TT Retry order

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-retry-order/)
>
> **Interpreted in:** [Order Types & Execution § Order type reference table](../../../../guides/order-types-and-execution.md#order-type-reference-table)

A TT Retry order is a synthetic order that repeatedly submits a child order until it is accepted by the exchange or until it is rejected a specified number of times, based on:

* The time to submit the first child order
* The maximum number of times to send a child order
* The time between retry attempts

A TT Retry order is commonly used to obtain a favorable position in the queue prior to the market open.

For example, the following TT Retry order submits an order 1 second before the market opens at 9:00 A.M. and continues submitting a new order every 200 milliseconds until the order is either accepted or rejected 10 times.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-retry-config.png)

If the exchange accepts the first submitted child order, the child order begins working in the market normally, and the TT Retry parent order terminates. If the first child order is rejected, the TT Retry parent order continues resubmitting a child order at the specified intervals, incrementing the retry counter each time. When the TT Retry parent order finishes, TT sends acknowledgments as follows:

* If a child order is accepted by the exchange before the specified number of retry attempts is reached, a single acknowledgment message containing the number of times the order was rejected and the average latency of each retry is sent by TT (Order Connector), followed by an acknowledgment for the child order. These messages are visible in the TT Audit Trail.
* If none of the child orders are accepted by the exchange before the specified number or retry attempts is reached, a single reject message is sent by TT (Order Connector) that contains the number of times the order was rejected and the average latency of each retry. This message is visible in the TT Audit Trail.

The TT Retry order is managed as follows:

* If exchange accepts the child order, the order works normally.
* Otherwise, the TT Retry order continues resubmitting a child order at the specified intervals, incrementing the retry counter each time. The TT Retry parent order sends acknowledgments as follows:
  * If a child order is accepted by the exchange before the specified number of retry attempts is reached, a single reject message containing the number of times the order was rejected is sent, followed by an acknowledgment for the child order.
  * If none of the child orders are accepted by the exchange before the specified number or retry attempts is reached, a single reject message is sent that contains the number of times the order was rejected.

## TT Retry order parameters

Required parameters:

* **Number of retries**: Sets the number of times (0-32,000) to resend a rejected order.
* **Retry interval**: Sets the number of milliseconds (0-100,000) between retry attempts.
* **Time and Date**: Sets the date and time to start executing the orderPossible values include:
  * **Start**, which sets the date and time to start executing the order
  * **End**, which sets the time to stop executing the logic of the order
* **Start**: Sets the date and time to start executing the order.

  Values include:

  * **Now** to start the order immediately
  * **Time** to display a date/time picker for you to indicate when to start the order
  * **Pre-open** to enter the order at the pre-open state defined by an exchange
  * **Open** to enter the order when the exchange opens its trading session

  **Note**: For TT Retry, the **Time** can be configured with microsecond granularity.
* **End**: Sets when to stop executing the logic of the synthetic order. Select one of the following:
  * **GTC** to leave the order working until canceled.
  * **Day** to leave the order working until the end of the trading session.

←[Previous PostTT OCO order](tt-oco-order.md)

[Next PostTT Stop order](tt-stop-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-retry-config.png
