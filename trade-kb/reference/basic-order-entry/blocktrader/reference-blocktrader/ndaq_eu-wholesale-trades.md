---
title: NDAQ_EU Wholesale Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/ndaq_eu-wholesale-trades/
---

# NDAQ_EU Wholesale Trades

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/ndaq_eu-wholesale-trades/)

Use the **Blocktrader** widget to submit wholesale trades for multiple accounts and counterparties at the NASDAQ Commodities and Derivatives Exchange (NDAQ\_EU). As an executing broker, you can select a counterparty and account for each side of the trade and submit both sides at once.

You can also create synthetic strategies to allocate multi-legged trades in the order ticket of the Blocktrader widget. All legs of the strategy are sent to the exchange as separate trades. Strategies can be saved as templates and used for submitting additional wholesale trades.

Once a trade is executed, you can view the fills and order status for each leg in the Blocktrader trade log, which is located in the bottom half of the widget. The orders and fills are also displayed in the **Fills** and **Audit Trail** widgets. Block trades can also be viewed in the **Time and Sales** widget.

For a list of wholesale trade types supported in Blocktrader for NDAQ\_EU, refer to [Blocktrader wholesale trade types on TT](../description-blocktrader/blocktrader-wholesale-trade-types-on-tt.md).

## Blocktrader display for NDAQ\_EU wholesale trades

Blocktrader consists of the following fields and selectors for submitting wholesale trades on NDAQ\_EU.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blocktrader-display.png)

The widget includes:

1. Exchange selector — Lists the exchanges with OTC trade reporting supported on TT®
2. Trade type selector — Lists the OTC trade types supported for the selected exchange.
3. Order Profile — Optional field for routing the transaction to the exchange. The account in the selected profile for this market will be used to route the order.
4. Deal Time — Used for setting the time of the transaction.
5. Price per leg — When checked, allows you to enter a price per leg instead of a single price for the entire transaction.
6. Price off tick — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
7. Counterparties per leg — Allows you to select a counterparty per leg in addition to one for each side.
8. Templates — Lists saved leg definitions that can be used as templates for defining and submitting additional trades. Click the icon to save the leg definition.
9. Leg definition grid — Consists of the following:
   * Instrument picker: Allows you to search for or manually select an exchange, product, and instrument in the **Contract** column.
   * Side column: Allows you to select the side of the trade for each leg. A single click in the **Side** column toggles a leg to the opposite buy/sell direction.
   * Qty column: Allows you to enter the buy or sell quantity for the leg.
   * Bid and Ask columns: Displays the best bid and ask prices for the contract.
   * Net sum values: Displays the net sum of the best bid and ask prices for each leg of the transaction.
   * Add/delete column: Allows you to delete all legs or add/delete individual instrument legs. Click “x” to delete a leg, and “+” to add a leg.
10. NDAQ\_EU wholesale trade fields:
    * **Side** — Allows you to set the counterparty’s side of the trade. A single click in the **Side** column toggles a leg to the opposite buy/sell direction.
    * **Counterparty** — Allows you to select an account and counterparty for each side of the trade. The counterparty selection shows your account, the counterparty’s alias (e.g., FCM name), and the counterparty’s Authorized Trader ID (ATID) or alias.
    * **Customer Profile** — A drop-down list of available Order Profiles. This is an optional field. Only customers with Order Profiles defined in Setup appear in the Customer Profile list.
    * **TT Account** — Sets an optional account to execute the trade for the Buyer or Seller. All accounts assigned to the Buyer or Seller are listed in the drop-down menu.
    * **Clearing Account** — Overrides the TT routing account value in Tag 1 in the exchange API on order actions sent to the exchange. Enter an exchange-provided account name of up to 10 characters in this optional field. By default, the TT routing account is sent in Tag 1.
    * **Text TT** — An optional, user-defined text value that remains on the submitted order for tracking purposes in TT, but is not routed to the exchange.
    * **TT Account for routing** — Sets the account used to route the trade to the exchange. Sent to the exchange in Tag 1.
11. Text TT — Allows you to add a text that is not sent to the exchange but remains on the order in the TT system.
12. TT Account for routing — Allows you to select an account that has been assigned to you and mapped to an active connection to the exchange.
13. Confirm Order and Submit — Displays the trade confirmation window when you click **Submit** to send the trade to the exchange. Order confirmations are enabled by default.

## Submitting NDAQ\_EU Wholesale Trades

Use the Blocktrader widget to submit over-the-counter (block, off-exchange, wholesale, etc.) transactions supported by the exchange and market that you are trading.

To submit an NDAQ\_EU wholesale trade:

1. Click **Widgets** in the workspace title bar and select **Miscellaneous** | **Blocktrader**.
2. In the open Blocktrader widget, click the exchange selector and select an exchange (e.g., NDAQ\_EU).
3. Click the trade type selector and select a transaction type (e.g., Block).
4. Select a contract for each leg of the transaction using the [instrument picker](#pick).
5. Enter a quantity and select a side for each leg.

   A single click in the **Side** column toggles a leg to the opposite buy/sell direction.
6. In the **Price** field, set a price for the transaction.

   If needed, you can click **Price per leg** to set the price for each leg of the trade.

   **Note**: For instruments that support tick sizes smaller than what is displayed, you can check **Price off tick** to enter an off tick price per leg.
7. Set the [transaction time](#deal) for the trade.
8. Configure the [NDAQ\_EU wholesale trade fields](#ndaq).

   In the **Counterparty** column, select a counterparty for each side of the trade.

   Use the drop-down arrows in the counterparty fields to select the appropriate buy and sell accounts. Enter a few characters in the search field to quickly find the entry you need.

   In the **Side** column, set whether the counterparty is the buyer or seller. A single click in the **Side** column toggles a leg to the opposite buy/sell direction.
9. Optionally, enter a value in the **Text TT** field.

   This field is not routed to the exchange, but the value remains on the order in the TT system.
10. Click the **TT account for routing** selector, and select an account.

    The accounts listed are assigned to you in the Setup application and have active connections to the exchange.
11. Click **Submit**.

    **Note**: Blocktrader prompts you to confirm orders by default. Uncheck **Confirm order** on the Blocktrader widget to disable order confirmations.
12. Confirm the order and click **Submit**.

←[Previous PostMX Committed 1-Sided Orders](mx-committed-1-sided-orders.md)

[Next PostNZX Block Orders](nzx-block-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blocktrader-display.png
