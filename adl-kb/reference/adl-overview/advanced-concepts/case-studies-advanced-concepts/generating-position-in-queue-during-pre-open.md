---
title: Generating Position in Queue During Pre-open
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/case-studies-advanced-concepts/generating-position-in-queue-during-pre-open/
---

# Generating Position in Queue During Pre-open

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/case-studies-advanced-concepts/generating-position-in-queue-during-pre-open/)

### Case Study Overview

A large Texas-based energy commodities trading firm is looking to hedge their long exposure in Light Sweet Crude oil
with Futures contracts. In this case study example, the markets for Crude Oil are in a closed state. The
requirements are to sell CME WTI futures at the next Settlement, executing as close to or at the Settlement price.
In order to try and guarantee execution at the settlement price, rather than waiting for WTI settlement and manually
executing the sell orders at that time, they are looking to sell CME WTI TAS contracts as close to a price of 0.

Trading at Settlement (TAS) products, offered by multiple exchanges, allows users to execute at a spread to the
settlement price at any time during the trading session. You can enter a defined number of tick increments above or
below the settlement.

As CME Crude Oil TAS (product code: CLT) is a first-in-first-out (FIFO) market, it’s important to place the order at
the earliest possible time that the market can accept order placement. For CLT, this would be at the pre-open state.
The trader responsible for executing this is looking for viable options.

### Using the TT Timed Order Type

Within the TT platform, the user can utilize the [TT Timed](../../../../../trade-kb/reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-time-sliced-order.md) synthetic algo order type. It is possible to place this
algo order type during any market state to place a native order when the market is in an order accepting state. Per
the above scenario, the market for Crude Oil is in a closed state, so the user can set the start time to trigger
native order placement at the start of the pre-open. This is set within the “Start” dropdown within the Precondition
details section:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-generating-piq-tt-timed.png)

Once the TT Price Server receives the first pre-open market state confirmation from the CME exchange for the CLT
instrument, CLT Oct23 in this example, the TT Timed algo will immediately place the child order.

### Using the TT Retry Order Type

Another option would be to use the [TT Retry](../../../../../trade-kb/reference/basic-order-entry/tt-order-types/description-tt-order-types/tt-retry-order.md) synthetic order type. A TT Retry order is a synthetic order that repeatedly submits a child order until it is accepted by the exchange or until it is rejected a specified number of times, based on:

* The time to submit the first child order
* The maximum number of times to send a child order
* The time between retry attempts

The user can set a Start Time of 1 second before the CLT market opens at 17:00 CT and continue submitting a new order every 200 milliseconds until the order is either accepted or rejected 10 times:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-generating-piq-tt-retry.png)

### Using an ADL Order Ticket Algo (OTA)

TT allows users to also create custom logic by utilizing the [Algo Design Lab (ADL)](https://library.tradingtechnologies.com/adl/gs-adl-overview.html), where an [Order Ticket Algo (OTA)](../description/order-ticket-algos-ota.md) can be developed to submit a child order at the pre-open similar to a TT Timed synthetic algo. Within the ADL algo, it is possible to create additional conditional logic that is not present within the TT Timed or TT Retry synthetic algos.

Users may want to utilize the [Market State block](../../../trading-blocks/market-state-block.md) along with other logic conditions to drive child order placement. The [Generator block’s](../../../discrete-blocks/generator-block.md#modes) time interval function may also be used as part of implementation of a retry logic.

←[Previous PostAutomating a Fixed Income Futures Hedge Order](automating-a-fixed-income-futures-hedge-order.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-generating-piq-tt-timed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-generating-piq-tt-retry.png
