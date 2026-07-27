---
title: MX Committed 1-Sided Orders
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/mx-committed-1-sided-orders/
---

# MX Committed 1-Sided Orders

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/mx-committed-1-sided-orders/)

The Blocktrader widget supports entering committed (1-sided) orders using the [committed order functionality at MX](https://www.m-x.ca/f_avis_tech_en/11-022_en.pdf). A committed trade occurs when two exchange-approved parties pre-arrange a transaction and their committed orders are matched at an equal price and quantity on opposite sides of the trade.

## Blocktrader display for MX Committed 1-Sided Orders

The Blocktrader widget includes the following fields for submitting committed orders on MX.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-mx-committed-display.png)

The widget includes:

1. **Exchange selector** — Lists the exchanges with trade reporting supported on TT.
2. **Trade Type selector** — Lists the trade types supported for the selected exchange.
3. **Account selector** — Sets the account used to route the trade to the exchange.
4. **Price** — Sets the price for the transaction You can also use the up and down arrows to set the price.
5. **Quantity** — The total trade quantity. The exchange requires a [minimum quantity threshold](https://www.m-x.ca/f_avis_tech_en/11-022_en.pdf) based on product type.
6. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
7. **Instrument Picker** — Opens the Market Explorer to search for and select the instrument being traded.
8. [MX Trade fields](#mx_common) — Trade fields required by the exchange. Fields are displayed based on the selected trade type.
9. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking confirm will allow the user to check the details of the trade before clicking **Submit**.
10. **Message indicator** — Indicates whether the trade was successfully sent to the exchange. Also shows if the order needs to be confirmed before submitting.

## Submitting MX Committed 1-Sided Orders on TT

Before submitting a committed trade, consider the following:

* Exchange rules state that each side of a committed trade must contain a required minimum quantity and is priced inside the bid and ask posted at the time the order is submitted. **Note**: MX will reject any committed orders that do not meet these requirements.
* Both sides of the trade must have the same price and quantity.
* A committed order must contain the exchange-defined counterparty code.

To submit a MX committed 1-sided orders on TT:

1. Open the Blocktrader widget and select **MX** from the exchange selector.
2. Select “Committed 1-Sided” from the trade type selector:
3. Find and select an instrument using the Instrument Picker at the top of the widget.
4. Set the quantity and price for the trade.
5. Select an account for routing the order to the exchange.
6. Complete the [common and required fields](#mx_common) in Blocktrader.
7. Click the **Submit** button.

   If **Confirm order** is checked, confirm the order before submitting it to the exchange.

The following is an example of a committed order submitted on MX.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-mx-committed-overview.png)

## Blocktrader fields for MX Committed 1-Sided Trades

The following fields are common in Blocktrader when submitting committed orders on MX.

* **Side** — Sets the Buyer or Seller. Click the Buyer or Seller cell to set each side of the trade.
* **Customer Profile** — A drop-down list of available Order Profiles. This is an optional field. Only customers with Order Profiles defined in Setup appear in the Customer Profile list.
* **Counterparty** — Sets the exchange-provided counterparty participant code and is mandatory for MX committed orders. Maps to *ex\_customer\_s* in the exchange API. This is a required field.
* **Account Type**  — Sets the exchange account code for the trade. Maps to *Account Type* in the exchange API as one of the following valid values:
  * **Customer**: Account Type=1
  * **Customer Insider**: Account Type=I
  * **Customer Shareholder**: Account Type=H
  * **Pro**: Account Type=4
  * **Pro Insider**: Account Type=S
  * **Pro Shareholder**: Account Type=L
  * **House**: Account Type=2
  * **House Insider**: Account Type=N
  * **House Shareholder**: Account Type=O
  * **Non-Client**: Account Type=5
  * **Non-Client Insider**: Account Type=R
  * **Non-Client Shareholder**: Account Type=D
* **TT Account** — Sets an optional account to execute the trade for the Buyer or Seller. All accounts assigned to the Buyer or Seller are listed in the drop-down menu.
* **Open/Close** — Sets whether the order opens or closes a position.

←[Previous PostMEFF Cross Trades](meff-cross-trades.md)

[Next PostNDAQ_EU Wholesale Trades](ndaq_eu-wholesale-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-mx-committed-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-mx-committed-overview.png
