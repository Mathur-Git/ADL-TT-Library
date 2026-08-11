---
title: GFO-X Block Orders
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/gfo-x-block-orders/
---

# GFO-X Block Orders

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/blocktrader/reference-blocktrader/gfo-x-block-orders/)

The TT® platform supports [GFO-X](https://www.gfo-x.com/) block trades using the TT Blocktrader widget, you can submit the following orders:

* Block
* EFRP — Exchange for Related Position

## Blocktrader display for GFO-X

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-gfo-x-display-scaled.png)

The components are:

1. **Exchange** — Lists the exchanges with OTC trade reporting supported on TT.
2. **Trade Type** — Lists the OTC trade types supported for the selected exchange. For GFO-X, this can be either “Block” or “EFP — Exchange for Related Position”.
3. **Price** — Sets the price for Block or EFP trade. You can also use the up and down arrows to set the price.
4. **Quantity** — The total trade quantity.
5. **Price off tick** — When checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.
6. **Instrument** — Allows you to search for and select the instrument being traded. For GFO-X, this can be a futures instrument, options instrument or a spread instrument defined by the exchange.
7. [GFO-X block trade fields](#common-gfo-x-blocktrader-trade-fields) — Allows you to complete the fields required by the exchange. For GFO-X, the trade fields are same for both trade types: “Block” and “EFP”.
8. **Confirm Order and Submit** — Allows you to confirm the order before submitting. When **Confirm Order** is checked, clicking confirm will allow the user to check the details of the trade before clicking **Submit**.

## Common GFO-X Blocktrader Trade Fields

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-gfo-x-trade-fields.png)

The following list shows the Blocktrader fields that are common when submitting block trades on GFO-X.

1. **Side** — Sets the Buyer or Seller. Select “Buyer” or “Seller” to set each side of the trade.
2. **Customer Profile** — A drop-down list of available order profiles. This is an optional field. Only customers with order profiles defined in Setup appear in the **Customer Profile** list.
3. **TT Account** — Sets an optional account for the Buyer or Seller. This account will be used for the Buyer or Seller instead of the one set in the **Account** drop-down. All accounts assigned to the user are listed in the drop-down menu. Maps to **client\_info\_s** in the exchange API.

Note The exchange does not allow the \* and % characters to be used as part of the account number.

4. **Order Capacity** — Sets the type of user who is placing orders with this account. Value can be “Principal” or “Agency”.
5. **One Off Shared Key** — Free text string which is a shared key between the two sides of an order. Both the buy and sell side order should have the same string in this field for orders to be matched by the exchange.
6. **Text C** — An optional, user-defined text value that remains on submitted orders in the TT system and is sent to the exchange. Alpha-numeric and special characters are allowed.
7. **Text TT (optional)** — Adds a note that is not sent to the exchange but remains on the order in the TT system.

## Submitting Trades on GFO-X

To submit a trade on GFO-X :

1. Open the **Blocktrader** widget and select “GFO-X” from the **Exchange** drop-down.
2. Select the trade type from the **Trade Type** drop-down.

* Block
* EFRP — Exchange for Related Position

* Use the **Instrument** drop-down at the top of the widget to select the instrument.
* Under the **Trade Type** drop-down, set the **Price** and **Quantity** for the trade.
* Set the **Deal TIme**
* Set the [GFO-X block trade fields](#common-gfo-x-blocktrader-trade-fields) in the center of the widget:

* Set the **Side** as “Buyer” or “Seller”.
* Select the **Customer Profile**. If no profile is selected, the default profile is used.
* Select the **TT Account** for executing the trade.
* Select the **Order Capacity** as “Agency” or “Principal”.
* Set the **One off Shared Key**. This is a free text field; however, both the buy and sell sides of an order must have the same one off shared key in order to match.
* Define a value in **Text C** (sent to the exchange).
* Make any notes regarding the transaction in **Text TT**. (not sent to the exchange)

The fields will be locked for review.

* Click **Confirm**.
* Review your selections for accuracy.
* Click **Submit**.

## Matching Trades on GFO-X

For two opposite side trades to match on GFO-X, the following parameters must be identical on both orders:

* **One Off Shared Key**
* **Deal Time**
* **Price**
* **Quantity**
* **Instrument**

←[Previous PostCME R-Cross Trades](cme-r-cross-trades.md)

[Next PostEurex and EEX Wholesale Trades](eurex-and-eex-wholesale-trades.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-gfo-x-display-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/blk-gfo-x-trade-fields.png
