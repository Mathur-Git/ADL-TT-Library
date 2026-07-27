---
title: Market data in Market Grid
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid/
---

# Market data in Market Grid

> Category: **Viewing Market Data** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/description-market-grid/market-data-in-market-grid/)

The Market Grid displays market data for multiple instruments across multiple exchanges in a concise format. Users may add or hide columns to display various market data fields and can choose to expand the display of an instrument to display market depth.

## Market depth

The Market Grid can be expanded to display market depth for one or more instruments to the extent that an exchange disseminates the data. When a row is expanded, the aggregated bid or ask quantity is displayed for each price level.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-depth-intro.png)

## Detailed depth

Some exchanges disseminate detailed depth allowing you to see every order at a price level. When a row is expanded to display detailed depth, you can see the quantity of each individual order at a price level to the extent an exchange disseminates that data.

**Note**: TT supports detailed depth for the following exchanges: ASX, ATHEX, B3, CFE, CME, CME\_BrokerTec, EPEX, JPX, NASDAQ\_NED, NDAQ\_EU, Nord Pool, OSE, TFEX and SGX.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-detailed-depth-2.png)

When there are more levels of detailed depth available than can be displayed in Market Grid for a price level, the last row shows the remaining quantity in parenthesis.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-detailed-depth-summary2.png)

For markets that provide detailed depth, the Market Grid separates direct bid and ask quantities from implied bid and ask quantities at each price level. When viewing detailed depth for these markets and products, the implied quantities are listed below the direct quantities and marked with an asterisk (\*).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-separate-quantities2.png)

The display of summary rows and prices at each level of detailed depth is configurable in the [Market Grid local settings](../reference-market-grid/market-grid-reference.md#mg-settings).

## Floating Depth in Market Grid

The Floating Depth pop-up widget let’s you quickly trade from a contract’s market depth. The widget appears when you hover on a price or quantity in the Market Grid and Spread Matrix, or price or quantity edit control in the Order Book and Order Ticket.

To use the Floating Depth widget, enable the **Show floating depth widget on hover** option in the Order Ticket, Market Grid, Order Book, or Spread Matrix settings.

When shown, the Floating Depth widget displays up to three levels of depth for both bids and offers.
You can right-click a price or quantity in a level of depth to seed those values in the price and quantity controls of your floating order entry widget (e.g., Order Ticket).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-depth-seed-ot.png)

## Live Only mode

Market Grid supports a Live Only mode that allows you to hide instruments that are not currently being traded. When you enable Live Mode, the Market Grid displays only instruments that have an active bid, active offer, or last-traded price (LTP).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-enable-live-only-mode.png)

## Direct Prices

The best bid and ask prices displayed for a product are based on the total bid and ask quantities, which include any implied bid and ask quantities. You can use the **Only show direct prices** setting for this widget to filter out the implied prices and quantities for each product added to the widget. Right-click to open the context menu and select **Settings…** to enable/disable **Only show direct prices**.

When the **Only show direct prices** setting is checked (enabled), implied prices are filtered out and only direct prices are shown, and implied bid and ask quantities are not included in the best bid and ask quantities. When unchecked (disabled), best bid and ask prices and quantities include both direct and implied values.

## Implied prices

The Market Grid supports implied prices, which are tradable
prices that are synthetically generated from orders in outright contracts and spreads. There are two types of implied prices:

* Implied In — The spread market is based on orders in the market for the outrights. A bid or ask in the outrights implies a bid or ask in the spread for the two outrights. The difference of the outright prices goes into generating the spread price.
* Implied Out — The outright market is based on orders in the spread market. A bid or offer in an outright and a bid or offer in the spread implies a bid or offer in the other outright. The outright price is generated using the spread price and the price of the other outright.

The Market Grid displays the implied bid and ask order quantities for the spread and outright markets and displays the implied prices based on these orders. For example, a bid of 10 for the CL Dec16 contract and an offer of 5 for the CL Jan17 contract creates a quantity of 5 for the implied bid for the CL Dec16-Jan17 spread. The implied order quantity of 5 is displayed in the **ImpBidQty** column for the CL Dec16-Jan17 Calendar spread in the Market Grid.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-implied2.png)

## Indicative Prices and Quantities

The Market Grid displays indicative or theoretical open prices and quantities that are provided by the exchange. Indicative or theoretical open prices and quantities are typically provided during Pre-Open or Auction market states.

If an exchange provides a pre-open or auction price or quantity, the values are displayed in the optional **IndPrc** (indicative open price) and **IndQty** (indicative quantity) columns in the Market Grid. The indicative Bid and Ask prices for the instrument are displayed in the **Bid** and **Ask** columns during the Pre-Open or Auction market state.

An indicative settlement price published by an exchange is displayed in the **IndSettle** column. For example, if an exchange sends an intra-day settlement price, it will be displayed in this column.

To show/hide these columns in the Market Grid, right-click in the Market Grid, click **Set Market Grid columns** in the context menu and select **IndPrc**, **IndQty**, and **IndSettle**. For a description of the Market Grid columns, refer to [Market Grid Reference](../reference-market-grid/market-grid-reference.md#mg-col-desc).

### Resting Market Orders

If provided by the exchange, quantities of resting Buy/Sell pre-open orders, as well as “On Auction” and “On Close” orders during Auction states are displayed in the **BidMktQty** and **AskMktQty** columns in Market Grid. The Bid market quantity (BidMktQty) column
displays the total quantity of resting Buy Market orders, and the Ask
market quantity (AskMktQty) column displays the total quantity of resting Sell Market
orders.

## Options support in Market Grid

The Market Grid also provides market data specifically targeted for options contracts that you can expose by showing their columns in the grid.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-options-columns.png)

You can display the options values by showing the following [Market Grid columns](../reference-market-grid/market-grid-reference.md#mg-col-desc) through the [Market Grid settings](../reference-market-grid/market-grid-reference.md#mg-settings).

When you right-click a futures or spread contract in the Market Grid, you can select **Related Contracts…** from the context menu to list all options products in the Product Family for that instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-related-contracts.png)

Clicking an options product in the list opens an Options Chain widget seeded with the Market Explorer, which allows you to easily select a **Term** for the selected product.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-related-options-chain.png)

## New instruments in the Market Grid

If you are viewing market data at the product level in the Market Grid, new instruments added by the
exchange for that product will automatically appear in the widget. For example, if you are viewing market
data for ES strategies at CME, user-defined strategies newly created at the exchange for this product will
automatically appear in the Market Grid.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-pds.png)

←[Previous PostIntroduction to Market Grid](introduction-to-market-grid.md)

[Next PostTrading from Market Grid](trading-from-market-grid.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-depth-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-detailed-depth-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-detailed-depth-summary2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/market-grid-separate-quantities2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-depth-seed-ot.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-enable-live-only-mode.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-implied2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-options-columns.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-related-contracts.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-related-options-chain.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-pds.png
