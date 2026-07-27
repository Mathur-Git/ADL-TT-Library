---
title: SGX Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/sgx-trades/
---

# SGX Trades

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/sgx-trades/)

The TT® platform supports [SGX OTC Trades](https://www.sgx.com/).
Using the Blocktrader widget, you can submit the following orders:

* **One Sided Orders**

  Orders posted from one participant to another who is listed as the counterparty.
  Once the counterparty submits a matching half to a *Buy* or *Sell* order the trade is
  reported.
* **Two Sided Orders**

  Orders where the bid-side participant and the ask-side participant are set within the same order message.

### Blocktrader display for SGX

The Blocktrader widget consists of the following components for submitting OTC trades on SGX.

![Annotated SGX Blocktrader Widget](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-sgx-contract-displayed.png "One sided trade fields")

The components are:

1. **Exchange Selector** –
   Lists all exchanges with reporting supported on TT.
2. **Trade Type Selector** –
   Lists trade type supported for the exchange, in this case, **One Sided** and **Two
   Sided**.
3. **Price** –
   Sets the price for **One-Sided** or **Two Sided** trades.
   A price may be keyed-in or adjusted using the arrows.
4. **Quantity** –
   The total trade quantity
5. **Price per leg** —
   Unchecked by default, the **Price per leg** option is enabled when spread instruments are used.
6. **Use text for counterparty** –
   When checked, allows you to manually enter a value into the `Counterparty` field instead of
   selecting a preconfigured option from the dropdown.
7. **Instrument Picker**
   Allows you to search for an instrument and select it for trading.
8. [**SGX Trade Fields**](#sgx-trade-fields) –
   Allows you to modify fields required by the exchange.
   Fields are displayed base on the selected trade type.
9. **Confirm Order and Submit** –
   Submits the order with the selected options.

   When **Confirm Order** is checked, two clicks are required for submission.

   * The first **Confirm** click locks in the options for the trader to review.
   * The second **Submit** click sends the order.

### SGX Trade Fields

![SGX Trade Fields](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-sgx-fields.png "SGX Trade Fields")

1. **Side** –
   Sets the *Buyer* or *Seller*.
2. **Customer Profile** *(optional)* –
   A drop-down list of available **Order Profiles** as defined in **Setup** under the
   **Customer Profile** list.
3. **TT Account** –
   Sets the account for executing the trade.
   The accounts assigned to the user, as a *Buyer* or *Seller*, are listed in the dropdown.
4. **Counterparty** –
   A drop-down list of counterparty participant codes as defined in **Setup**.

   **Note:**
   This field can be manually overridden by ticking the box [Use text for
   counterparty](#counterparty).
5. **Clearing Acct** –
   Enter the Buyer’s or Seller’s exchange clearing account value.
6. **Text TT** *(optional)* –
   Adds a note that is **not** sent to the exchange but remains in on the order in the TT System.
7. **Report Type** –

   * **Negotiated Large Trade** *(NLT)* – Default
   * **Exchange For Physical** *(EFP)*
   * **Exchange For Swap** *(EFS)*
   * **OTC Swap** *(OTC)*

## Submitting Trades on SGX

To submit a trade on SGX:

1. Open the **Blocktrader** widget and select SGX from the [**Exchange
   Selector**](#display).
2. Select the trade type from the [**Trade Type Selector**](#display).

   * **One Sided**
   * **Two Sided**
3. Use the [**Instrument Picker**](#display) at the top of the widget to select the
   instrument.
4. Back under the **Trade Type Selector**, set the [**Quantity**](#display)
   and [**Price**](#display) for the trade.
5. Set the [**SGX Trade Fields**](#display) in the center of the widget:

   * Select the **Customer Profile**.
     If no profile is selected, the default profile is used.
   * Select the **TT Account** for executing the trade.
   * Select the **Counterparty**.
     Preconfigured members of the exchange are listed in the dropdown.
     Alternatively, click **Use text for counterparty** and manually type in a value
   * Enter the **Clearing Account**.
   * Make any notes regarding the transaction in **Text TT**.
   * Select the **Report Type**.

1. The fields will be locked for review.

   Click **Confirm**.

1. Review your selections for accuracy.

   Click **Submit**.

   Trades with two brokers are reported to the exchange once both parties submit matching halves of an order,
   both *Buy* and *Sell*.

## Matching One Sided Trades

Either **Buyer** or **Seller** can initiate the trade report for matched workflow.

1. If the **Seller** initiates the trade report:

   The buyer is notified via a **Trade Capture Report** *(TCR)* message and may choose to
   accept the trade report.
   If the buyer does not respond the notification and submits a trade report independently, the system tries to
   find the buyer’s corresponding trade report.
2. If the **Buyer** initiates the trade report:

   The seller is not notified via TCR.
   Instead, the seller must submit a trade report independently in the system, where it is matched to a
   corresponding *Buy* side.

←[Previous PostNZX Block Orders](nzx-block-orders.md)

[Next PostTFEX OTC Trades](tfex-otc-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-sgx-contract-displayed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-sgx-fields.png
