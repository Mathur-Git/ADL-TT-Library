---
title: Market data for exchange-listed spreads
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads/
---

# Market data for exchange-listed spreads

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/description-spread-matrix/market-data-for-exchange-listed-spreads/)
>
> **Interpreted in:** [Market Data & Depth § Spread Matrix (exchange-listed & inter-product spreads)](../../../../guides/market-data-and-depth.md#spread-matrix-exchange-listed-inter-product-spreads) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § What AutoSpreader is](../../../../guides/spread-trading-autospreader.md#what-autospreader-is) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Cross-references](../../../../guides/spread-trading-autospreader.md#cross-references)

Using the **Exchange Listed** tab when opening the Spread Matrix, you can display market data for an exchange-listed calendar
spread.

Right-click in the market data cells for a spread to view the context menu for the calendar spread. You can also right-click a single contract to open the context menu for the contract. In the context menu, select **Open…** to open an MD Trader, Order Ticket, Chart, or Time and Sales widget that displays the market data for the selected spread or outright contract.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-context-condor.png)

## Market data display in Spread Matrix

Spread Matrix displays four pieces of market data for each outright contract or spread. The information is displayed in one of four cells that make up a larger grouping: Ask Price, Ask Quantity, Bid Price, and Bid Quantity.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-data.png)

The prices and quantities can be direct, implied, or a combination of both. To highlight the different prices and quantities, the widget provides default colors for Bid and Ask cells that you can customize using the **Colors** options in [Settings: Spread Matrix](../../../order-management/fills/reference-fills/fills-reference.md). To help visualize implied quantities, you can enable the **Show implieds with an asterisk (\*)** widget setting, which displays an asterisk next to quantities that are partially or completely implied.

To display prices above quantities for each outright or spread, check the **Show prices above quantities** option in **Settings: Spread Matrix.**

To display a third column that shows the last traded price and quantity for each spread and outright, enable (check) the **LTP/LTQ** option in **Settings: Spread Matrix**.

## Direct Prices

The best bid and ask prices displayed for a product are based on the total bid and ask quantities, which include any implied bid and ask quantities. You can use the **Only show direct prices** setting for this widget to filter out the implied prices and quantities for each product added to the widget. Right-click to open the context menu and select **Settings…** to enable/disable **Only show direct prices**.

When the **Only show direct prices** setting is checked (enabled), implied prices are filtered out and only direct prices are shown, and implied bid and ask quantities are not included in the best bid and ask quantities. When unchecked (disabled), best bid and ask prices and quantities include both direct and implied values.

## Butterfly and Condor spread market views

Using the Butterfly/Calendar toggle button on the tool bar, you can view exchange-listed Butterfly and Condor spread contracts in the Spread Matrix. When you click **Butterfly** to enable this mode, Spread Matrix displays the Butterfly and Condor market data for the applicable contract months.

For Butterfly spreads, prices are based on the corresponding three consecutive expires (e.g., GE Sep18, GE Dec18, GE Mar19):

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-butterfly-view.png)

For Condor spreads, prices are based on the corresponding four consecutive expiries (e.g., GE Mar18, GE Jun18, GE Sep18, GE Dec18):

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-condor-view.png)

Butterfly and Condor spread prices can be displayed in both the “vertical” and “staircase” orientations. By default, prices are shown using the “vertical” display when you enable Butterfly mode.

←[Previous PostOrder entry for exchange-listed spreads](order-entry-for-exchange-listed-spreads.md)

[Next PostOrder entry for inter-product spreads](order-entry-for-inter-product-spreads.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-context-condor.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-data.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-butterfly-view.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-condor-view.png
