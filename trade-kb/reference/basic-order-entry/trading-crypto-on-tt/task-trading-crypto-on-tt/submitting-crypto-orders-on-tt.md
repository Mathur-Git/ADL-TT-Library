---
title: Submitting crypto orders on TT
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/trading-crypto-on-tt/task-trading-crypto-on-tt/submitting-crypto-orders-on-tt/
---

# Submitting crypto orders on TT

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/trading-crypto-on-tt/task-trading-crypto-on-tt/submitting-crypto-orders-on-tt/)

Using MD Trader or the Order Ticket on the TT® platform, you can submit orders for all supported crypto instruments on the following exchanges:

* Coinbase
* Kraken

## MD Trader

When submitting orders for crypto instruments using MD Trader, consider the following:

* Fractional order quantities can be entered in the order quantity and default default order quantity fields. Fractional working order quantities are also displayed in the Bids and Asks columns, position, and cancel buttons in the order entry panel.
* The Net position field shows your total position (not your daily position).

  **Note**: Crypto exchange trading sessions are 24 hours. However, positions will reset at at 12:00 UTC (6PM CST), and an SOD record will be created for the next 24 hour trading period.
* Only working quantities and the amount bought or sold are shown in the **Work** column.
* Clicking the net open position seeds the full position as the order quantity and not the truncated version if **Quantity display decimal places** is enabled in **Preferences** | **Orders**.
* Market and Stop Market orders are submitted as quantities and not prices.

The following example shows submitting crypto orders with MD Trader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-mdt-orders-callouts.png)

## Order Ticket

When submitting orders for crypto instruments using the Order Ticket, consider the
following:

* Order quantity button toggles in 1.0 digit increments. You can also enter manual fractional quantities up to eight decimal digits.
* The inside market price with fractional quantities is displayed.
* Market and Stop Market orders are submitted as quantities and not prices.
* Native crypto exchange order types are supported.

The following example shows submitting crypto orders with the Order Ticket.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-ot-orders-callouts.png)

←[Previous PostViewing crypto market data on TT](viewing-crypto-market-data-on-tt.md)

[Next PostCreating a Coinbase API key](creating-a-coinbase-api-key.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-mdt-orders-callouts.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-ot-orders-callouts.png
