---
title: BrackeTT (OTA)
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/brackett-ota/
---

# BrackeTT (OTA)

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/tt-order-types/description-tt-order-types/brackett-ota/)
>
> **Interpreted in:** [Order Types & Execution § Order Ticket Algos (OTA) — TT Pro license](../../../../guides/order-types-and-execution.md#order-ticket-algos-ota-tt-pro-license)

BrackeTT is an Order Ticket Algo (OTA) that is a simplified version of the TT Bracket order type. When launched, BrackeTT submits a Limit order which, upon being filled, submits additional orders that synthesize the logic of an OCO (one-cancels-other) order. These additional orders allow you to potentially lock in profits with a favorable move or prevent a downside loss without having to constantly monitor the position, and can be beneficial to users executing trades with tighter risk limits.

**Note:** For an overview of Order Ticket Algos (OTA), refer to this article in the ADL help: [https://library.tradingtechnologies.com/adl/ac-order-ticket-algos.html](../../../../../adl-kb/reference/adl-overview/advanced-concepts/description/order-ticket-algos-ota.md)

For each partial fill of the Limit order, BrackeTT automatically submits a Limit order and a Stop Limit order in the opposite Buy/Sell direction. If the additional Limit order (profit order) is filled, the algo cancels the protective Stop Limit order. If the Stop is triggered, the algo cancels the profit order and submits a Limit order at the trigger price.

BrackeTT can be launched from the following widgets:

* [MD Trader](#submit)
* [Order Ticket](#submit)
* [Algo Dashboard](#launch)
* [Autotrader](#launch)

## Configuring a BrackeTT order

The algo is configured using the [BrackeTT order parameters](#brackett-params)
in the flyout.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-flyout.png)

For the OCO order, you can configure how many **Price Increments** from the Limit order fill price to submit the “Profit Order”, and how many **Loss Trigger Increments** from this price to submit the Stop Limit order. You can also configure the **On Trigger, Payup Increments** parameter to set how many ticks from the protective Stop price to submit the Limit order when the Stop is triggered.

## Submitting a BrackeTT order

Before you begin, select an instrument to trade in MD Trader or the Order Ticket, and select an account.

**Note:** You can also launch OTA algos from [Autotrader or the Algo Dashboard](#launch).

To submit a BrackeTT order:

1. Click the order types selector in MD Trader or the Order Ticket and select **BrackeTT**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-select.png)
2. Configure the [BrackeTT order parameters](#brackett-params) in the flyout.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-flyout-step2.png)
3. Enter an order quantity and click the desired price level in MD Trader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-mdt.png)

   If using the Order Ticket, enter a price and quantity and click **Buy** or **Sell**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-ot.png)

   The Order Book displays the BrackeTT order and shows the working quantity in the **WrkQty** column, and shows the status of the parent order in **SynthStatus**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-mdt-ob.png)

When the Limit order fills, the profit and stop loss OCO orders are submitted at the configured price levels.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-oco.png)

The working OCO child orders are displayed in the Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-oco-ob.png)

When the OCO orders are filled, the algo automatically pauses.

## Launching BrackeTT from the Algo Dashboard or Autotrader

Select **BrackeTT** from the Algo Explorer pane and configure the [BrackeTT order parameters](#brackett-params). You also need to set the following in the Algo Dashboard:

* **Order Instrument**: The instrument being traded. Select an instrument from the Market Explorer.
* **Account**: The account used for submitting the order. Select an account from the account selector.
* **Order Price**: The price of the order.
* **Order Side**: Sets the side of the order. Select either “Bid” or “Ask”.

After configuring the OTA, click **Launch Algo**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-dashboard.png)

In Autotrader, click **Choose an algo** and select “BrackeTT”. Click **Add row** to configure the [BrackeTT order parameters](#brackett-params). Then, click the cell in each corresponding column to provide the contract, price, quantity, and side for the BrackeTT order. After configuring the OTA, click the “Play/Resume” button.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-autotrader.png)

## BrackeTT order parameters

The following parameters are available in the BrackeTT flyout:

* **Profit Increments**: Sets how many ticks from the filled order price to submit the OCO Limit order (ProfitOrder).
* **Loss Trigger Increment**: Sets how many ticks from the filled order price to submit the Stop Limit order.
* **On Trigger, Payup Increment**: Sets how many ticks from the Stop price to submit the Limit order when the Stop is triggered. You can enter positive or negative payup increments to determine the Buy/Sell direction of the Limit order.
* **Ignore Market State**: Sets whether to ignore changes in the market state.
* **Instance name**: Custom name to display in the **TextTT** field.
* **Disconnect action**: Sets which action to take if the client loses its connection to TT:
  * **Leave**: Allow the algo to continue running normally.
  * **Pause**: Suspend the algo until you manually restart it.
  * **Cancel**: Delete the algo.

←[Previous PostTT Multi-Level Bracket (OTA)](tt-multi-level-bracket-ota.md)

[Next PostOCO OMA](oco-oma.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-flyout.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-flyout-step2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-mdt.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-ot.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-mdt-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-oco.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-oco-ob.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-dashboard.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tto-brackett-autotrader.png
