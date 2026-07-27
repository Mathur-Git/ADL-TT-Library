---
title: TT Multi-Level Bracket (OTA)
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-multi-level-bracket-ota/
---

# TT Multi-Level Bracket (OTA)

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/tt-multi-level-bracket-ota/)

TT Multi-Level Bracket is an Order Ticket Algo (OTA) that allows you to take a position in an instrument and exit at
one or more prices.

**Note:** For an overview of Order Ticket Algos (OTA), refer to this article in the ADL help: [https://library.tradingtechnologies.com/adl/ac-order-ticket-algos.html](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/order-ticket-algos-ota.md)

The algo is submitted by placing a Limit order at a specific price level. When the Limit order is filled, TT
Multi-Level Bracket automatically places OCO orders up to four price levels from the fill price based on their
percentage allocation. You can set the distance from the fill price at each level, as well as the percentage of the
filled quantity to be allocated at each level. You also have the ability to only work a single side of the OCO as
needed.

You can launch a TT Multi-Level Bracket algo from the following widgets:

* [MD Trader](#submit)
* [Order Ticket](#submit)
* [Algo Dashboard](#launch)
* [Autotrader](#launch)

## Configuring a TT Multi-Level Bracket order

The algo is configured using the [TT Multi-Level Bracket order parameters](#tt-multi-bracket-params)
in the flyout.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-flyout.png)

For the OCO orders, configure the percentage of the filled quantity to be allocated at each level using fields “LV1-4
%”. The values entered must equal “100” otherwise the parent order will automatically pause. For example, if you
only execute OCO orders across two levels,
then **LV1 %** and **LV2 %** together need to equal “100”. The other levels can remain as zero.

After the levels are configured, set the number of ticks from the entry order fill price to submit the
Profit and Stop orders. You can configure up to four levels using the “Profit LV1-4” and “Stop LV-1” parameters in
the flyout.

## Submitting a TT Multi-Level Bracket order

Before you begin, select an instrument to trade and open it in MD Trader or the Order Ticket.

**Note:** You can also launch OTA algos from [Autotrader or the Algo Dashboard](#launch).

To submit a TT Multi-Level Bracket order:

1. Click the order types selector in MD Trader or the Order Ticket and select **TT Multi-Level
   Bracket**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-select.png)
2. Configure the [TT Multi-Level Bracket order parameters](#tt-multi-bracket-params) in the flyout.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-flyout-1.png)
3. Enter an order quantity and click the desired price level in MD Trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-mdt.png)

   If using the Order Ticket, enter a price and quantity and click **Buy** or
   **Sell**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-ot.png)

   The Order Book displays the TT Multi-Level Bracket and shows the working quantity and executed quantity in
   **WrkQty** and **ExeQty**, and shows the status of the parent order in
   **SynthStatus**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-mdt-ob.png)

When the Limit order fills, the OCO orders are submitted for the configured price levels.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-oco.png)

The working child orders are displayed in the Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-oco-ob.png)

When all OCO orders have been filled the algo will automatically pause.

## Launching TT Multi-Level Bracket from the Algo Dashboard or Autotrader

Select **TT Multi-Level Bracket**  from the Algo Explorer pane and configure the [TT Multi-Level Bracket order parameters](#tt-multi-bracket-params). In Algo Dashboard, you also need to
provide the contract, price, quantity, and side for the order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-dashboard.png)

In Autotrader, click **Choose an algo** and select “TT Multi-Level Bracket”. Click **Add
row** to configure the [TT Multi-Level Bracket order parameters](#tt-multi-bracket-params).
Then, click the cell in each corresponding column to provide the contract, price, quantity, and side or the TT
Multi-Level Bracket order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-autotrader.png)

## TT Multi-Level Bracket order parameters

The following parameters are available in the TT Multi-Level Bracket flyout:

* **LV1%**: Percentage of filled quantity to cover at level 1. The allocation at this level must be complete
  before subsequent levels receive allocation. Any residual quantity from the level allocations will be
  re-allocated to level 1.
* **LV2%**: Percentage of filled quantity to cover at level 2.
* **LV3%**: Percentage of filled quantity to cover at level 3.
* **LV4%**: Percentage of filled quantity to cover at level 4.
* **PROFIT**: Set to False if you do not wish to submit a Profit Order.
* **PROFIT LV1 (TICKS)**: Ticks from the fill price to submit Profit order 1.
* **PROFIT LV2 (TICKS)**: Ticks from the fill price to submit Profit order 2.
* **PROFIT LV3 (TICKS)**: Ticks from the fill price to submit Profit order 3.
* **PROFIT LV4 (TICKS)**: Ticks from the fill price to submit Profit order 4.
* **STOP**: Set to False if you do not wish to submit a Stop Order.
* **STOP LV1 (TICKS)**: Ticks from the fill price to submit Stop order 1.
* **STOP LV2 (TICKS)**: Ticks from the fill price to submit Stop order 2.
* **STOP LV3 (TICKS)**: Ticks from the fill price to submit Stop order 3.
* **STOP LV4 (TICKS)**: Ticks from the fill price to submit Stop order 4.
* **Stop Limit?**: True = Stop Limit; False = Stop Market.
* **Stop Limit (Ticks)**: Number of ticks from the Stop trigger price to submit the Limit order. Only applies
  to Stop Limit Orders.
* **Ignore Market State**: Sets whether to ignore changes in the market state.
* **Instance name**: Custom name to display in the **TextTT** field.
* **Disconnect action**: Sets which action to take if the client loses its connection to TT:
  * **Leave**: Allow the algo to continue running normally.
  * **Pause**: Suspend the algo until you manually restart it.
  * **Cancel**: Delete the algo.

←[Previous PostTT Sniper (OTA)](tt-sniper-ota.md)

[Next PostBrackeTT (OTA)](brackett-ota.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-flyout.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-flyout-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-ot.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-mdt-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-oco.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-oco-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-dashboard.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-multi-autotrader.png
