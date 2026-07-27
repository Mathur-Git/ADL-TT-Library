---
title: Trading from Market Grid
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/description-market-grid/trading-from-market-grid/
---

# Trading from Market Grid

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/description-market-grid/trading-from-market-grid/)

You can trade from the Market Grid by opening an Order Ticket or MD Trader widget for the instrument you wish to trade. You can open a widget for a specific contract as a Floating Order Entry widget, linked widget, or widget group. As you trade, your positions and working orders are displayed in the Market Grid.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-positions-orders.png)

You can also middle-click the value in the **Pos** column to display your positions by account.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-float-net.png)

## Floating order entry widget

When you click a cell in the following columns for an instrument, a floating order entry widget opens pre-populated with the selected value so you can quickly enter an order:

* Pos (open position)
* Last
* LastQty
* Bid
* BidQty
* Ask
* AskQty

Based on the [Preferences](../../../overview/preferences/description-preferences/orders-preferences.md), either an MD Trader or Order Ticket opens.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-foe.png)

## Linked widgets

From a Market Grid, you can quickly launch a linked MD Trader or Order Ticket. The linked widget can be identified by a yellow border. The linked widget remains open unless you close it, and you can quickly switch instruments in the linked widget by clicking on any instrument in the Market Grid. This allow you to trade one instrument and then quickly trade a different
instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-linked-widget-2-2.png)

## Widget Groups

You can create a widget group with the Market Grid and an order entry widget to trade with both as a single widget. As you submit orders for an instrument using the order entry widget, you can view the market in the Market Grid. As you change instruments in the Market Grid, they automatically appear in the order entry widget in the group.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-trade-group-widget.png)

## Floating Order Book

Users can cancel or modify working orders for any instrument in the Market Grid by opening a Floating Order Book. The Floating Order Book also allows you manage an order by attaching an Order Management Algo (OMA) to the order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-fob2.png)

## Number of Orders (Headcount)

The Market Grid provides optional columns that show the number of orders (i.e., headcount) that comprises the total bid and ask quantity at each price in the market. By viewing the number of orders, you can gain insight to the makeup of the bid or ask quantity displayed at that price level.

Some exchanges provide the number of orders in their market data feeds. If an exchange does not provide this data, TT calculates the number of orders based on the detailed depth provided by the exchange. If an exchange provides neither the number of orders or detailed depth, the optional columns for displaying the number of orders in the Market Grid will be blank.

### Number of orders display

The number of orders at a price level for bids and asks are displayed in the optional **BidCnt** and **AskCnt** columns. These columns are shown using the **Set Market Grid columns** option in the [Market Grid widget settings](../reference-market-grid/market-grid-reference.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-number-of-orders.png)

## Position in Queue in Market Grid

The Market Grid can show your actual or estimated position in queue (PIQ) after you submit an order in the optional **PIQ Buys** and **PIQ Sells** columns. To show these columns, right-click and select **Settings: Market Grid** and click **Set Market Grid columns**.

PIQ can be enabled either in [Preferences](../../../overview/preferences/description-preferences/orders-preferences.md) or by showing the **PIQ Buys** or **PIQ Sells** column  in the [Market Grid settings](../reference-market-grid/market-grid-reference.md).

When viewing position in queue, consider the following:

* Position in queue is only tracked and displayed when the order price is within the visibly displayed market depth.
* When your order is at the inside market, the PIQ number is white.
* When your order is the first in queue, the PIQ number is yellow.
* When multiple users share an account, PIQ is only displayed to the user who placed the order. Other users on that account will not see PIQ for that order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-position-in-queue.png)

## RFQ support

←[Previous PostMarket data in Market Grid](market-data-in-market-grid.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-positions-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-float-net.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-foe.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-linked-widget-2-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-trade-group-widget.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-fob2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-number-of-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-position-in-queue.png
