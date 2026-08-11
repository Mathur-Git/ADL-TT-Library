---
title: TT Sniper (OTA)
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-sniper-ota/
---

# TT Sniper (OTA)

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-sniper-ota/)
>
> **Interpreted in:** [Order Types & Execution § Order type reference table](../../../../guides/order-types-and-execution.md#order-type-reference-table) · [Order Types & Execution § Order Ticket Algos (OTA) — TT Pro license](../../../../guides/order-types-and-execution.md#order-ticket-algos-ota-tt-pro-license)

TT Sniper is an Order Ticket Algo (OTA) that allows you to hide your intent to buy or sell at a given price until
there is quantity available at that price on the opposite side of the market.

**Note:** For an overview of Order Ticket Algos (OTA), refer to this article in the ADL help: [https://library.tradingtechnologies.com/adl/ac-order-ticket-algos.html](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/order-ticket-algos-ota.md)

When submitted, TT Sniper looks at the quantity available on the opposite side of the market at the specified order
price for the given contract. If there is at least one lot available at this price or better, a child Limit order
will be submitted at this price with a quantity equal to the available or remaining quantity to execute, whichever
is less.

If the full child order quantity is not immediately filled, TT Sniper will cancel the balance and add the unfilled
quantity back to the quantity remaining to be filled. It will repeat this until the total quantity is filled.

You can launch a TT Sniper algo from the following widgets:

* [MD Trader](#submit)
* [Order Ticket](#submit)
* [Algo Dashboard](#launch)
* [Autotrader](#launch)

**Note:** TT Sniper is not supported for use with Autospreader instruments.

## Submitting a TT Sniper order

To submit a TT Sniper order:

1. Click the order types selector in MD Trader or the Order Ticket and select **TT Sniper**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-select1.png)

   You can also launch OTA algos from Autotrader, the Algo Dashboard, or an Order Ticket launched from a
   supported widget (e.g., Market Grid).
2. Configure the [TT Sniper order parameters](#tt-sniper-params) in the flyout.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-flyout1.png)
3. Enter an order quantity and click the desired price level in MD Trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-mdt1.png)

   If using the Order Ticket, enter a price and quantity and click **Buy** or
   **Sell**.

   The Order Book displays “TT Sniper” in the **AlgoName** column.
   It shows the *working quantity* and *executed quantity* in **WrkQty** and
   **ExeQty**.
   The status of the parent order is shown as “Working” in **Status**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-ob.png)

   **Note:** If a value is specified in the flyout for “Instance Name,” it
   will show in **TextTT**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-instance-name.png)

   The Fills widget shows both parent order (\*) and child order fills. The child order fills are received
   directly from the exchange.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-fills.png)

## Launching TT Sniper from the Algo Dashboard or Autotrader

Select **TT Sniper** from the Algo Explorer pane and configure the [TT Sniper
order parameters](#tt-sniper-params). In Algo Dashboard, you also need to provide the contract, price, quantity, and side for
the TT Sniper order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-dashboard.png)

In Autotrader, click **Choose an algo** and select TT Sniper. Click **Add row** to
configure the [TT Sniper order parameters](#tt-sniper-params). You also need to provide the contract,
price, quantity, and side for the TT Sniper order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-autotrader.png)

## TT Sniper order parameters

The following parameters are available in the TT Sniper flyout:

* **Aggressiveness (sec)**: Sets the number of seconds to wait before submitting additional orders at
  the specified price or better. Minimum setting is 0.25 (250 milliseconds). The default setting is “1” second.
* **Ignore Market State**: Sets whether to ignore changes in the market state. If unchecked, the algo
  will pause when the market state of the instrument transitions to closed.
* **TIF**: *(Time in Force)* Specifies how long the order remains in effect.
  * **Day**: *(default when submitting through MD Trader)*   
    A **Day Order**
    expires at the end of the day and does not carry over to the next trade date.
  * **GTC**: A **Good Till Cancel** order remains active until it is executed, canceled, or
    when the instrument expires.
  * **IOC**: Any portion of an **Immediate or Cancel** order that is not filled immediately
    is cancelled.
  * **FOK**: An entire **Fill or Kill** order is filled immediately or the entire order is
    canceled.
  * **Day+**:
    A **Day Order Plus** is active during regular market hours plus the market’s extended hours *(if
    applicable)*.
  * **GTC+**:
    A **Good Till Cancel Plus** order is active during regular market hours plus the market’s extended
    hours *(if applicable)*.
* **Instance name**: Custom name to display in the **TextTT** field.
* **Disconnect action**: Sets which action to take if the client loses its connection to TT:
  * **Leave**: Allow the algo to continue running normally.
  * **Pause**: Suspend the algo until you manually restart it.
  * **Cancel**: Delete the algo.

←[Previous PostTT OBV (Order by Volatility) order](tt-obv-order-by-volatility-order.md)

[Next PostTT Multi-Level Bracket (OTA)](tt-multi-level-bracket-ota.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-select1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-flyout1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-mdt1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-instance-name.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-fills.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-dashboard.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-sniper-autotrader.png
