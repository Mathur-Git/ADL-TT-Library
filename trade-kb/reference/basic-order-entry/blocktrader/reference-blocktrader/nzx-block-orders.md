---
title: NZX Block Orders
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/nzx-block-orders/
---

# NZX Block Orders

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/nzx-block-orders/)

The TT® platform supports [NZX Block Trades](https://assets.ctfassets.net/m5mydry9e35f/4tVvw8a4eZLJAPrGpwJv1u/50871a1f6ddb3458b5f3ce47a47cd94b/Derivatives_Procedures_July_2018.pdf). Using the Blocktrader widget on TT, you can submit the following orders:

* Block
* EFP – Exchange for Physical

Note

NZX supports both 1-sided and 2-sided block orders. TT supports only 1-sided block orders for NZX as described on this page. 2-sided NZX block orders are not supported by TT currently.

Note

NZX supports block orders for outrights only. Block orders for multi-leg orders are not supported by either NZX or TT.

## Blocktrader display for NZX

The Blocktrader widget consists of the following components needed for submitting NZX block trades.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-nzx-display-scaled.png)

The components are:

1. **Exchange** — Lists the exchanges with OTC trade reporting supported on TT.
2. **Trade Type** — Lists the OTC trade types supported for the selected exchange. For NZX, this can be either “Block” or “EFP – Exchange for Physical”.
3. **Price** — Sets the price for the Block or EFP trade. You can also use the up and down arrows to set the price.
4. **Quantity** — The total trade quantity.
5. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
6. **Instrument** — Allows you to search for and select the instrument being traded. For NZX, this can be a futures instrument or a spread instrument defined by the exchange.
7. [NZX block trade fields](#common-nzx-blocktrader-trade-fields) — Allows you to complete the fields required by the exchange. For NZX, the trade fields are the same for both trade types: Block and EFP.
8. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking **Confirm** will allow the user to check the details of the trade before clicking **Submit**.

## Common NZX Blocktrader Trade Fields

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-nzx-trade-fields.png)

The following list shows the Blocktrader fields that are common when submitting block trades on NZX.

1. **Side** — Select “Buyer” or “Seller” to set each side of the trade.
2. **Customer Profile (optional)** — A drop-down list of available order profiles. Only customers with order profiles defined in Setup appear in the **Customer Profile** list.
3. **TT Account (optional)** — Sets an account for the buyer or seller. This account will be used for the buyer or seller instead of the one set in the **Account** drop-down. All accounts assigned to the user are listed in the drop-down menu. It maps to **client\_info\_s** in the exchange API.

   Note

   The exchange does not allow the \* and % characters to be used as part of the account number.
4. **Account Type** — Sets the exchange account code for the trade. Valid values are:

   * Wholesale
   * Retail
   * Principal
   * Market Maker
   * Prescribed Person (Employee of participant trade)
   * none
5. **Open/Close** — Sets whether the trade opens or closes a position.
6. **Broker Reference (optional)** — Sets the Client ID for the broker, defined by tag 448 (PartyID) when tag 452 (PartyRole) = 3.
7. **Text TT (optional)** – Adds a note that is not sent to the exchange but remains on the order in the TT system.

## Submitting Trades on NZX

To submit a trade on NZX:

1. Open the Blocktrader widget and select “NZX” from the **Exchange** drop-down.
2. Select the trade type from the **Trade Type** drop-down.
   * Block
   * EFP
3. Use the **Instrument** drop-down at the top of the widget to select the instrument.
4. Under the **Trade Type** drop-down, set the **Price** and **Quantity** for the trade.
5. Set the [NZX block trade fields](#common-nzx-blocktrader-trade-fields) in the center of the widget: 
   * Select the **Customer Profile**. If no profile is selected, the default profile is used.
   * Select the **TT Account** for executing the trade.
   * Select the **Counterparty**. Preconfigured members of the exchange are listed in the drop-down. Alternatively, click **Use text for counterparty** and manually enter a value.
   * Set the **Account Type**.
   * Set the value of the position in **Open/Close**.
   * Set the **Broker Reference**.
   * Make any notes regarding the transaction in **Text TT**.

   The fields will be locked for review.
6. Click **Confirm**.
7. Review your selections for accuracy.
8. Click **Submit**.

## Block Order State Mapping

xml encoding="utf-8" ?

| NZX Block Order State (Tag 856) | NZX TradeReportTransType (Tag 487) | TT Block Order State (Status Column on Audit Trail) |
| --- | --- | --- |
| 0 = Submit | 0 = New | Pending New |
| 1 = Alleged | 0 = New | Working |
| 10 = Pended (trade awaiting approval) | 2 = Replace | Filled |
| 6 = Trade Report Cancel | 2 = Replace | Canceled |

←[Previous PostNDAQ_EU Wholesale Trades](ndaq_eu-wholesale-trades.md)

[Next PostSGX Trades](sgx-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-nzx-display-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-nzx-trade-fields.png
