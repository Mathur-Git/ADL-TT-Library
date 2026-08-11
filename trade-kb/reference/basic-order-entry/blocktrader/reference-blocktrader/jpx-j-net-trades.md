---
title: JPX J-Net Trades
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/jpx-j-net-trades/
---

# JPX J-Net Trades

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/jpx-j-net-trades/)

The TT® platform supports [J-NET Trading on JPX](https://www.jpx.co.jp/english/derivatives/rules/j-net/index.html). Using the Blocktrader widget on TT, you can submit the following orders:

* J-Net One Sided: Orders that are only posted to the
  participant listed as the counterparty. J-Net One Sided
  orders are only executed after the counterparty submits a matching
  J-NET One Sided order.
* J-Net Cross: Orders where the bid-side participant and
  an ask-side participant are set within the same order message.
  Both sides of the order are then executed as a Cross order.

## Matching a J-Net One Sided trade

J-NET One Sided orders are only executed after both traders submit a matching J-NET
One Sided order. To match these trades, JPX requires the following:

* The orders must have the same trade type, instrument, price, and quantity.
* Both sides of the trade (Buy and Sell) must be set.
* Both participants must set each other as their counterparty.

## Blocktrader display for JPX

The Blocktrader widget consists of the following components needed for submitting J-Net trades on JPX.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-display.png)

The components are:

1. **Exchange selector** — Lists the exchanges with OTC trade reporting supported on TT.
2. **Trade Type selector** — Lists the OTC trade types supported for the selected exchange. For JPX, this value maps to *transaction\_type* in the exchange API.
3. **Account selector** — Sets the account used to route the trade to the exchange.
4. **Price** — Sets the price for One Sided or Cross trades. You can also use the up and down arrows to set the price.
5. **Quantity** — The total trade quantity.
6. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
7. **Use text for counterparty** — Allows counterpartys to be entered as text instead of selected from the dropdown list defined in Setup.
8. **Instrument Picker** — Allows you to search for and select the instrument being traded.
9. [JPX J-Net Trade fields](#ose_common1) — Allows you to complete the fields required by the exchange. Fields are displayed based on the selected trade type.
10. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking confirm will allow the user to check the details of the trade before clicking **Submit**.

## Common J-NET Trade fields for JPX

The following list shows the Blocktrader fields that are common when submitting J-Net trades on JPX.

* **Side** — Sets the Buyer or Seller. Click the Buyer or Seller cell to set each side of the trade.
* **Customer Profile** — A drop-down list of available Order Profiles. This is an optional field. Only customers with Order Profiles defined in Setup appear in the Customer Profile list.
* **Counterparty** — A drop-down list of counterparty participant codes in Setup and is mandatory for all J-Net trades. Maps to *ex\_customer\_s* in the exchange API. This is a required field.
* **TT Account** — Sets an optional account for the Buyer or Seller. This account will be used for the Buyer or Seller instead of the one set in the Account Selector. All accounts assigned to the user are listed in the drop-down menu. Maps to *client\_info\_s* in the exchange API. **Note**: The exchange does not allow the \* and % characters to be used as part of the account number.
* **Account Type**  — Sets the exchange account code for the trade. Maps to *exchange\_info\_s* in the exchange API as “0” = Client, “9” = House. Valid values are:
  * **Client (Agency)**
  * **House (Principal)**
  * **none**
* **Give Up** — Identifies which counterparty the Give-up order is allocated to. Enter the carrying participant code. Maps to *exchange\_info\_s* in the exchange API.
* **Trade Purpose** — Sets the intention of the J-NET One Sided trade. Refer to the exchange’s documentation for the requirements for reporting the trade purpose. This is a required field for one sided trades. Select one of the following:
  * **Arbitrage**
  * Combination
  * Cross Trade: Select “Cross Trade” to enter a J-NET One Sided Cross. This
    will require the counterparty to submit a matching trade. To enter a two sided J-NET Cross, select “J-NET Cross” in the Trade Type selector and enter credentials for both the Buy and Sell sides of the trade.
  * **Exchange for Physical* Position Consolidation
    * Rollover
    * Other**

## Submitting J-Net trades on JPX

**Note**: Prior
to submitting a J-NET trade, you should know the counterparty’s
participant code and the trade purpose (e.g., Arbitrage, Combination,
etc).

To submit a J-Net trade on JPX:

1. Open the Blocktrader widget and select **JPX** from the Exchange selector.
2. Select a trade type from the Trade Type selector:
   * **J-Net One Sided**
   * **J-Net Cross**
3. Find and select an instrument using the Instrument Picker at the top of the widget.
4. Set the quantity and price for the trade.
5. Select an account from the account selector.
6. Complete the [common and required fields](#ose_common1) in Blocktrader.

   Additional fields in Blocktrader vary depending on the type of J-Net trade you select:

   * [J-Net One Sided](#one)

     Enter the common fields, select a side, and enter the counterparty. You must verify that the counterparty
     enters a matching J-NET One Sided trade.
   * [J-Net Cross](#cross)

     Enter the common fields and counterparty participant codes, and submit both sides of the trade.
7. Click the **Submit** button.

   If **Confirm order** is checked, confirm the order before submitting it to the exchange.

## Example: JPX J-Net One Sided Trade

The following figure shows a J-Net One Sided trade in Blocktrader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-1sided.png)

## Example: JPX J-Net Cross

The following figure shows a J-Net Cross trade in Blocktrader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-cross.png)

←[Previous PostICE and ICE_L OTC Trades](ice-and-ice_l-otc-trades.md)

[Next PostLME Cross Orders](lme-cross-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-1sided.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-jpx-cross.png
