---
title: Eurex and EEX Wholesale Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/eurex-and-eex-wholesale-trades/
---

# Eurex and EEX Wholesale Trades

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/eurex-and-eex-wholesale-trades/)

Blocktrader supports submitting Eurex and EEX wholesale trade types.
**Note**: EEX only supports Block trades.

The following wholesale trades are supported:

* [Cross](https://www.eurex.com/ex-en/trade/order-book-trading/matching-principles) — A trade when a user buys and sells the same contract simultaneously. Cross trades are not processed as OTC trades at Eurex, but are submitted using Blocktrader.
* [Block](https://www.eurex.com/ex-en/trade/eurex-t7-entry-services/block-trades) — High volume trade in any outright or strategy product.
* [Exchange for Swap](https://www.eurex.com/ex-en/trade/eurex-t7-entry-services/exchange-for-swaps) — Strategy where a position in the underlying
  is traded for a futures position.
* [Volatility](https://www.eurex.com/ex-en/trade/eurex-t7-entry-services/vola-trades) — Eurex volatility trade, which requires you to submit and complete an options Block trade and hedge it with a futures trade. A Vola trade can only be submitted for previously completed block trade.
* [Exchange for Physical Fixed Income](https://www.eurex.com/ex-en/trade/eurex-t7-entry-services/exchange-for-physicals) — OTC trade that exchanges an OTC derivative
  product for an exchange-traded fixed income derivative.
* [Exchange for Physical Index](https://www.eurex.com/ex-en/trade/eurex-t7-entry-services/exchange-for-physicals) — OTC trade that exchanges an OTC derivative
  product for an exchange-traded index derivative.

## Blocktrader display for Eurex and EEX

Blocktrader consists of the components needed for submitting wholesale trades on Eurex.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-display2.png)

The image shows the following:

1. Exchange selector — Lists the exchanges with OTC trade reporting supported on TT®
2. Trade type selector — Lists the OTC trade types supported for the selected exchange.
3. Price — Used for entering a price for the transaction. You can also use the up and down arrows to adjust the price.
4. Quantity field — Used for entering the buy or sell quantity for the trade. You can also use the up and down arrows to adjust the quantity.
5. Deal time selector — Sets the time of the transaction. Click the arrow to set the time to the current time and date.
6. Price off tick — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
7. Instrument search — Allows you to search for and select the instrument being traded.
8. [Eurex Wholesale Trade fields](#eurex_common) — Allows you to complete the fields required by the exchange. Fields are displayed based on the trade type.
9. Delayed Publication —
   When checked, the trade is not published automatically,
   allowing the user to delay reporting of the trade to the exchange. The duration of the delay is set by the exchange.
10. Confirm Order and Submit — Allows you to confirm the order before submitting.
    When **Confirm Order** is checked, clicking confirm will allow the user to check the details of the trade before clicking **Submit**.
11. Message indicator — Indicates whether the trade was successfully sent to the exchange. Also shows if the order needs to be confirmed before submitting.
12. Order report panel — Displays the status and details of the trade after it’s submitted to the
    exchange. Wholesale trades sent to you are automatically inquired in Blocktrader and appear in the order report panel.

    The **Action** column displays either a “Cancel” button when submitting a trade, or an “Accept” button when accepting a trade. Actions pending exchange approval appear as “Pending” in this column.

    The **State** column shows the following states:

    * Approved: The trade has been submitted and accepted by the exchange. This state appears in the order report panel when you submit a Wholesale trade.
    * Received: The trade has been been auto-inquired and is awaiting acceptance by the counterparty.

## Submitting Wholesale Trades on Eurex

To submit a Wholesale Trade on Eurex:

1. Open the Blocktrader widget and select **Eurex** from the exchange selector.
2. Select a Wholesale trade type from the trade type selector.
3. Search for the instrument being traded.

   You can also use the Explorer to find an instrument.
4. Set the price and quantity for the trade.
5. Complete the [common fields](#eurex_common) in Blocktrader for both sides of the
   trade as needed.

   These fields are common for all supported Eurex wholesale trades unless otherwise noted.

   Complete the additional fields in Blocktrader based on the wholesale trade type selected:

   * [Block](#eurex_block)
   * [Exchange for Swap](#eurex_swap)
   * [EFP – Exchange for Physical Fixed Income](#eurex_income)
   * [EFP – Exchange for Physical Index Futures](#eurex_index)
   * [Volatility (Vola)](#eurex_vola)
   * [Cross](#eurex_cross)
6. Click the **Submit** button.

   If **Confirm order** is checked, confirm the order before submitting it to the exchange.

Submitted trades are automatically inquired and approved. In the order report panel, the **State** column displays “Approved” in the order report panel. If needed, you can click the **Cancel** button in the
**Action** column.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-send-status.png)

| Note | **Cross Trade Status** *(ITC)* |
|  | When submitting a [cross trade](#eurex_cross), ITC status is shown in the [Message Indicator](#message-indicator) prior to clicking **Submit**. |

  

In the Audit Trail, the **Message** column shows that the inquire was “Received” and “Approved”
automatically. When the counterparty accepts the trade, “Confirmed” and “Completed” are displayed in the **Message** column in the Audit Trail.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-send-audit1.png)

## Accepting Wholesale Trades on Eurex

**Note**: Trades sent to you are automatically inquired and displayed in the Blocktrader order report panel.

To accept a Wholesale Trade on Eurex:

1. Open the Blocktrader widget and select **Eurex** from the exchange selector.
2. In the Blocktrader order report panel, click the **Accept** button in the **Action** column.

   The **State** column in the order report panel shows a status of **Received**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-accept.png)

   After you click “Accept”, the trade is removed from the order report panel and the acceptance is sent to the exchange for approval.

   When the transaction is approved, the exchange sends both sides “Confirmed” and “Completed” messages that are displayed in the **Message** column in the Audit Trail.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-audit.png)

## Send Eurex/EEX care orders to Blocktrader

The Order Book and Orders and Fills widget (OFW) makes it easier to work large Eurex and EEX care orders in Blocktrader.

1. Select one care order (Buy or Sell), or two care orders (Buy and Sell) of the same quantity and same instrument
2. Right-click and select **Order Staging > Send to Blocktrader**.
3. A single care order can then be submitted from Blocktrader as you would like (typically as a Block) and the pair of buy and sell orders will be seeded in Blocktrader as a Cross.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-send-eurex-eex-care-orders-to-blocktrader.png)

## Common Wholesale Trade Fields for Eurex

The
table below lists the common fields for submitting wholesale trades
on Eurex.

|  |  |  |
| --- | --- | --- |
| **Wholesale Trades on Eurex** | | |
| **Blocktrader Field** | **Description** |
| Side | Click the field to select your side of the trade: Buyer or Seller |
| Customer Profile | A drop-down list of available Customer order defaults. Click the field and select a profile from the drop-down list. Only customers with Order Profiles defined in Setup appear in the Customer Profile list. If an account is provided in the selected profile, it will display in the TT Account field. |
| TT Account | Sets the customer account number/name for the Buyer or Seller. Select an account with an active connection to Eurex. The account number/name has a maximum limit of 11 characters. |
| Account Type | Supported account types:  * A1-A9 (Agent) * G1 (Pre-designated Give-Up) * G2 (Designated Giveup) * P1-P2 (Proprietary) * M1-M2 (Market Maker)   Sets the account type for submitting the trade.  If set to Giveup (e.g., G2), the you must populate the Giveup field with the take-up member ID. |
| Open/Close | Sets whether the trade opens or closes a position. |
| Giveup | Sets exchange member ID of the Giveup firm (e.g., TTGXV). This field is mandatory when Account Type is set to “G2”. |
| Counterparty MGT | Sets the exchange member ID of the counterparty receiving the trade. Eurex requires the entire 11 character ID in this field (e.g., TTGXVTRD001).   | Note | The default value for **Counterparty MGT** is populated with the **OTC Trading User ID** set by the accounts administrator for the exchange. The default can be overridden by selecting an **Order Profile** with a different ID for the counterparty or by entering a alternate member ID manually. | |
| Clearing Acct | Sets the account that is sent to the exchange on the order in Tag 25008 and used for clearing purposes. This value overrides the clearing account in the Customer Profile for the Buyer/Seller. |

## Block Trades

To submit Block trades, complete the [common fields](#eurex_common) for Eurex wholesale trades in Blocktrader. There are no additional fields required.

The following figure shows a Eurex Block trade using
the common wholesale trade Fields.

**Note**: Blocks can be entered from the Sell side by toggling the “Buyer” button.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-block2.png)

## Exchange for Swap (EFS) Trades

To submit Exchange for Swap trades, first complete the Blocktrader fields listed in
[Common Wholesale Trade Fields for Eurex](#eurex_common). In addition, complete
the fields provided in the following table.

|  |  |  |
| --- | --- | --- |
| **Additional Fields for Exchange for Swaps Trades** | | |
| **Blocktrader Field** | **Description** |
| Settlement Date | This field is mandatory for the buyer and display only for the seller. The settlement date of the swap trade must be entered. The value has to be greater than the current business date. |
| Nominal Amount | Sets the equivalent value of the futures leg to be traded. This value must be represented in units of one thousand. |
| Coupon | The interest rate of the fixed income instrument. |
| Coupon Frequency | This field is mandatory for the buyer and display only for the seller. The fixed leg coupon frequency of the swap has to be entered. Enter the number of interest payments per year by selecting one of the following: **Annually**, **Semi Annually**, **Quarterly**, **Monthly**. |
| Currency | The currency of the instrument being traded. |
|
| Customer 1 | The identification of the first customer involved in the EFS swap trade. This field is optional. Enter a user-defined value of up to 20 characters. |
|
| Customer 2 | The identification of the second customer involved in the EFS swap trade. This field is optional. Enter a user-defined value of up to 20 characters |
| Variable Rate Reference | This field is optional for the buyer and display only for the seller. The variable rate reference can be up to 12 characters. |
| Variable Rate Offset | This field is optional for the buyer and display only for the seller. Enter a numeric variable rate offset value greater than or equal to -99.9999 and less than or equal to 99.9999. |
| Start Date | This field is mandatory for the buyer and display only for the seller. The start date of the swap must be entered. Its value must be greater than or equal to the settlement date. |
| End Date | This field is mandatory for the buyer and display only for the seller. The end date of the swap must be entered. Its value must be greater than or equal to the start date. |

The following figures show an example of an EFS trade.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efs.png)

## Volatility (Vola) Trades

After a Block trade for an options contract is accepted and completed, you can initiate the Vola trade for the underlying futures contract.

**Note**: The **Exch OrderID** column in the Audit Trail shows the TT generated order ID value for the completed options Block trade. This value is now automatically available in the **Options Order ID** field drop down when using Blocktrader to submit the Vola trade for the underlying future contract.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-vola-audit2.png)

To
submit the Vola trade, you must first complete the Blocktrader fields listed in
[Common Wholesale Trade Fields for Eurex](#eurex_common). In addition, complete
the fields provided in the following table.

|  |  |  |
| --- | --- | --- |
| **Additional Fields for Vola Trades** | | |
| **Blocktrader Field** | **Description** |
| Options Order ID | The transaction number of the corresponding options trade. This number also appears in the **ExchOrderID** column in the Order Book, Order and Fills widget, and the Audit Trail for the completed options Block trade.  Note You can optionally right-click on a completed options block trade in the Order Book or the Order and Fills widget and select **Send to Blocktrader** to launch a Blocktrader widget pre-populated with the correct values for the Eurex Vola trade. |
| Options Product Name | The underlying Options product name (e.g., OESX). Entered with the Options Transaction ID. |
| Options Qty | The quantity of the corresponding options trade. |

The following is an example of a Eurex Vola trade:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-vola-submit.png)

## Exchange for Physical (EFP) Fixed Income Trades

You can use Blocktrader to submit either side of an EFP trade. When you are notified by the counterparty that they have submitted a wholesale EFP Fixed Income buy order, you can submit the corresponding sell order and accept the trade in Blocktrader. As part of submitting the sell side of an EFP order and accepting the trade, you must select the Settlement Institution (SI) responsible for clearing the transaction.

To submit Exchange for Physical Fixed
Income trades, first complete the Blocktrader fields listed in [Common Wholesale Trade Fields for Eurex](#eurex_common). In addition, complete the fields in the following table.

|  |  |  |
| --- | --- | --- |
| **Additional Fields for Exchange for Physical Fixed Income Trades** | | |
| **Blocktrader Field** | **Description** |
| Settlement Date | The date by which the buyer must pay for the securities delivered by the seller. |
| ISIN | Set the unique, 12 alphanumeric value used to identify the equity cash basket linked to the transaction.  Note: The first two characters of the Reference ID must be letters. |
| SI (optional) | Sets the settlement institution for the trade.  When used, this value must be provided for both the Buy and Sell sides of the trade. |
| Nominal Amount | Sets the equivalent value of the futures leg to be traded. This value must be represented in units of one thousand. |
| Coupon Frequency | The number of interest payments per year. Select one of the following: **Annually**, **Semi Annually**, **Quarterly**, **Monthly**. |
| Maturity | The date that the fixed income instrument matures. |
| Hedge Type | The hedging strategy for your side of the trade:  * Duration   Hedge * Nominal Hedge * Price Factor Hedge |
| Cash Price | The price of the fixed income instrument. |
|
| Issuer | The entity responsible for the obligation of the issue (optional field). Enter a value of up to 30 alphanumeric characters. |
 Currency | The currency of the instrument being traded (optional field). |

Note SI is an optional field.

The following is an example of a EFP Fixed Income trade:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efp-income.png)

## Exchange for Physical (EFP) Index Futures Trades

You can use Blocktrader to submit either side of an EFP trade. When you are notified by the counterparty that they have submitted a wholesale EFP Index Futures buy order, you can submit the corresponding sell order and accept the trade in Blocktrader. As part of submitting the sell side of an EFP order and accepting the trade, you must select the Settlement Institution (SI) responsible for clearing the transaction.

To submit Exchange for Physical (EFP) Index Futures
trades, you must first complete the fields listed in [Common Wholesale Trade Fields for Eurex](#eurex_common). In addition, complete
the fields provided in the following table.

|  |  |  |
| --- | --- | --- |
| **Additional Fields for Exchange for Physical Index Futures Trades** | | |
| **Blocktrader Field** | **Description** |
| SI (optional) | Sets the settlement institution for the trade.  When used, the selected value must be provided for both the Buy and Sell sides of the trade. |
| Nominal Amount | Sets the equivalent value of the futures leg to be traded. This value must be represented in units of one thousand. |
| Coupon | The interest rate of the fixed income instrument. |
| Reference ID | Set the unique, 12 alphanumeric character value used to identify the equity cash basket linked to the transaction.  Note: The first two characters of the Reference ID must be letters. |

Note SI is an optional field.

The following is an example of a EFP Index trade:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efp-index.png)

## Cross Trades

Eurex mandates that members send an “intention to cross” (ITC) message prior
to performing a cross trade. Using the **Auto ITC** option in Blocktrader, you can automatically send this message prior to the cross when you click **Submit** and confirm the trade. The “intention to cross” message is broadcast to all market
participants.

To submit a Cross trade, complete the Blocktrader fields listed in
[Common Wholesale Trade Fields for Eurex](#eurex_common) for both sides of the trade.

Before submitting the order, click the Intention to Cross **ITC button**. This submits your cross request to the market and activates the ITC timer. Eurex sets the time limit to wait before submitting the matching cross orders. The exchange also determines how long the cross request is active.

Optionally, check the **Auto ITC** checkbox to automatically submit the Cross after your user-defined time limit expires. When enabled, the Submit button displays “Abort” and counts down the timer. If needed, click this button again to cancel the cross request.

Once ITC is clicked, its status is shown in the [Message Indicator](#message-indicator) prior to submitting the trade.
ITC status is also viewable in the Audit Trail under the **Message Types**: `CrossRequestResponse` and `ExecutionReport`.

The following figure shows an example of a Cross trade in Blocktrader:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-cross.png)

←[Previous PostGFO-X Block Orders](gfo-x-block-orders.md)

[Next PostEuronext Wholesale Trades](euronext-wholesale-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-display2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-send-status.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-send-audit1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-accept.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-audit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-send-eurex-eex-care-orders-to-blocktrader.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-block2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efs.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-vola-audit2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-vola-submit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efp-income.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-efp-index.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-eurex-cross.png
