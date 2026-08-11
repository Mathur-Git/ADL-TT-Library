---
title: TT OBV (Order by Volatility) order
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-obv-order-by-volatility-order/
---

# TT OBV (Order by Volatility) order

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-obv-order-by-volatility-order/)
>
> **Interpreted in:** [Order Types & Execution § Order type reference table](../../../../guides/order-types-and-execution.md#order-type-reference-table)

**Note**: To use this TT Order Type, your company administrator must provide you with access to the [Advanced Options Package](https://library.tradingtechnologies.com/trade/aop-overview.html) and set your account permissions in Setup.

The TT OBV (Order by Volatility) lets you enter an order for an options contract by entering a desired volatility. The TT OBV places the order at the price level that corresponds to the desired volatility. As moves in the underlying contract impact the volatility at each price level, the TT OBV will continuously reprice the order to maintain the desired volatility.

For example, suppose you want to buy a Call options contract, such as LO Dec17 C5150, at 23.6 vol. You would specify the following parameter value:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-obv-intro.png)

## TT OBV order parameters

The following parameter is required:

* **Volatility**: Specifies the desired volatility at which you would like to trade the contract.

For more information about using TT OBV orders, see [Entering a TT OBV order](tt-oco-order.md).

←[Previous PostTT Autohedger](tt-autohedger.md)

[Next PostTT Sniper (OTA)](tt-sniper-ota.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-tt-obv-intro.png
