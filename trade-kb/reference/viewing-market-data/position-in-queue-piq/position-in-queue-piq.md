---
title: Position in Queue (PIQ) Overview
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/position-in-queue-piq/position-in-queue-piq/
---

# Position in Queue (PIQ) Overview

> Category: **Viewing Market Data** · [KB Home](../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/position-in-queue-piq/position-in-queue-piq/)

TT supports position in queue, which is your individual queue position per order at each price level for the products you are trading. Position in queue is either provided by the exchange on their price feed or provided by TT as an estimate of your queue position.

TT supports the following exchanges that provide actual queue position at each price level on their price feed:

* CME (Market by Order)
* ICE
* BIST

When provided by the exchange, the Trade application displays queue position in the **PIQ** column in the following widgets:

* [MD Trader](#piq)
* [Market Grid](#mg-piq)
* [Floating Order Book](#fob-piq)

PIQ is supported for all order flow on TT, which includes orders submitted via the Trade application, FIX applications, and other automated trading tools routing orders via the TT platform.

When multiple TT users share an account for order routing, PIQ is only displayed to the user who placed the order. Other users on that account will not see PIQ for
that order. However, if the **Enable (PIQ) for orders from other users** checkbox is checked in **Preferences** |
**Orders**, PIQ for an order is visible to all users sharing the account.

## Estimated Position in Queue

For products disseminated on price feeds that do not include individual queue position, TT provides an estimated queue position in the **PIQ** column to show how many contracts are in front of your order at any given price. Estimated PIQ is not sent from the exchanges, but is calculated by TT based on the quantity of trades occurring in front of the order, and is a conservative estimate of queue position.

For example, if your estimated PIQ is “25” and a 10-lot fill occurs at your price level, TT estimates that your PIQ improved and displays a new PIQ value of “15”. If an order is *canceled* at your price level, TT cannot tell if the order was in front or behind your PIQ, so your PIQ does not change and remains a conservative estimate of where you are in queue (your actual position may be better than what is shown). However, TT adjusts the estimated PIQ based on the reduced total quantity at that price to prevent your PIQ from being higher than the total volume at a price level.

Estimated PIQ is only maintained during the current logged in session and is cleared if you refresh or close your workspace, or log out. In this case, the estimated PIQ values on existing orders will be lost and no longer tracked on
those orders.

**Note**: In the Simulation environment, PIQ is estimated for *all* markets.

## Position in Queue in MD Trader

MD Trader can show your actual or estimated position in queue in the optional **PIQ** column. When multiple orders are submitted at a price level, PIQ is displayed for an order in MD Trader on a FIFO basis.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-show-epiq-piq-1.png)

### Enabling PIQ

PIQ can be enabled either in [Preferences](../../overview/preferences/description-preferences/orders-preferences.md) or by showing the PIQ column  in the [MD Trader settings](../../basic-order-entry/md-trader/reference-md-trader/md-trader-reference.md#columns). When this setting is enabled, the **PIQ** column displays the PIQ values
for visible orders.

### PIQ display

Your PIQ is only displayed and tracked when an order price is within the visible displayed market depth. When viewing PIQ, the PIQ number displayed in the column is black by default. If your order is the first in the queue, the background color turns black and the PIQ number “0” is white. If your order is at the inside market, the background color turns yellow.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-epiq3-piq-1.png)

## Position in Queue in Market Grid

The Market Grid can show your actual or estimated position in queue (PIQ) after you submit an order in the optional **PIQ Buys** and **PIQ Sells** columns. To show these columns, right-click and select **Settings: Market Grid** and click **Set Market Grid columns**.

PIQ can be enabled either in [Preferences](../../overview/preferences/description-preferences/orders-preferences.md) or by showing the **PIQ Buys** or **PIQ Sells** column  in the [Market Grid settings](../market-grid/reference-market-grid/market-grid-reference.md).

When viewing position in queue, consider the following:

* Position in queue is only tracked and displayed when the order price is within the visibly displayed market depth.
* When your order is at the inside market, the PIQ number is white.
* When your order is the first in queue, the PIQ number is yellow.
* When multiple users share an account, PIQ is only displayed to the user who placed the order. Other users on that account will not see PIQ for that order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-position-in-queue-1.png)

## Position in Queue in the Floating Order Book

The **PIQ** column in the Floating Order Book allows you to view your position in queue (PIQ) for each of your orders at a given price level.

To view PIQ in the Floating Order Book:

1. Check the **Edit** | **Preferences** | **Orders** | **Enable Position in Queue (PIQ)** checkbox in your workspace preferences.
2. Select the **PIQ** column in **Edit** | **Preferences** | **Orders** | **Set Floating Order Book columns**.

   **Tip**: You can move the column position using drag-and-drop in the column configuration dialog.
3. Launch the Floating Order Book from the **Work** column in MD Trader, or **WrkBuys** or **WrkSells** column in Market Grid.

   The position in queue for each order is displayed in the PIQ column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-piq.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-show-epiq-piq-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-epiq3-piq-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-position-in-queue-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fob-piq.png
