---
title: Market Data in MD Trader
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/description-md-trader/market-data-in-md-trader/
---

# Market Data in MD Trader

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/md-trader/description-md-trader/market-data-in-md-trader/)

MD Trader is the industry-leading interface that provides single-click order entry for an instrument while displaying market depth against a static, vertical price axis. The static price display gives you a visual sense of market movement over a period of time or relative to other markets.111

In addition to the market data displayed for an instrument in the [MD Trader
header pane](md-trader-display.md), you can view your average price of open position, estimated position in queue (EPIQ), last traded quantity (LTQ), and volume-at-price (VAP) in the MD Trader columns.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-market-data1.png)

## Static Price Display

MD Trader displays bid and ask quantities and market depth along a static price display in the **Price** column. As the best bid and ask prices change, the price display remains static.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-static.png)

### Center Bar

To make it easier to identify the midpoint of the inside market, MD Trader places a black center bar across the width of its grid. The center bar appears between the best bid and ask prices in the static price display. As the best bid and ask prices move up or down, the center bar remains static until you [recenter the market](../task-md-trader/recentering-md-trader.md) to its midpoint.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-center-bar.png)

### Relative Price movement

In MD Trader, bid and ask quantities and market depth move up or down along the static **Price** column to indicate price movement. This allows you to view the price movement in one instrument relative to the price movement in other instruments. In the following example, the CL Dec16 contract is up two ticks from its previous midpoint, in relation to the CL Jan17 contract that is up one tick and the CL Feb17 contract that is down one tick from its midpoint.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-price-move2.png)

## Floating price display

Empty price levels can be hidden to show only available prices by enabling **Settings** | **Only show available prices** in the MD Trader widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-mdt-floating-price.png)

**Note**: This setting removes the static aspect of the ladder, which may result in orders being submitted at a price level different than the one you clicked on if the prices moved while in the process of clicking the mouse for order entry.

When “Only show available prices” is enabled, MD Trader briefly shows a blank cell where a price level is removed before it compresses and adjusts the price ladder. This allows you to to enter an order at the correct price before all the prices move, and helps to clearly show quick rallies or sell-offs in the market.

**Tip**: You can “freeze” prices on the ladder at any time by holding down the Shift key.

## LTQ Display

MD Trader displays the last trade quantity (LTQ) in the LTQ column at the best bid or ask price. The LTQ column is shown by default, but you can show/hide the column using the **Show Last Traded Quantity** option in the local **MD Trader: Settings**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-ltq.png)

The LTQ value is color-coded to indicate if the trade occurred at a price that was higher, lower, or the same as the last traded
price (LTP):

* Black text with white background ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-same.png) — Indicates a trade at the same price.
* White text with a green background ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-high1.png) — Indicates a trade at a higher price.
* White text with a red background ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-low1.png) — Indicates a trade at a lower price.

**Note**: The LTQ column shows the indicative quantity for indicative or theoretical open prices that are provided by the exchange during Pre-Open or Auction market states.

## LTP Display

Optionally, you can highlight the Last Traded Price (LTP) in the static price display by using the **Highlight Last Traded Price (LTP) on price column** option in the local **MD Trader: Settings**.

The highlighted LTP value is color-coded to indicate if the trade occurred at a price that was higher, lower, or the same as the previous LTP. MD Trader highlights the price column cell with the default LTP [color settings](../task-md-trader/configuring-md-trader.md#mdt-colors) or your customized settings:

* A trade at the same price uses the LTP Column “Stable” colors
* A trade at a higher price uses the LTP Column “Uptick” colors
* A trade at a lower price, uses the LTP Column “Downtick” colors.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-ltp-highlight2.png)

## Volume-at-price (VAP) data

From the [context menu](../reference-md-trader/md-trader-reference.md), you can also expose an additional **VAP** column in MD Trader to display the total trade volume at each price level as a gray bar. By default, showing VAP displays the combined volume for buy and sell orders. You can select options to split the volume bar into buy (blue) and sell (red) quantities, to display the total quantity as a number and to reset (and restore) the VAP counter to show only volume that occurs after the reset. You can also hide the bars and show only the numeric values.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-mkt-mdt-vap2.png)

**Tip**: When you hover on a bar or cell in the VAP column, the VAP value at that price is displayed in a tooltip.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-vap-hover.png)

By default, VAP displays the trade volume since the start of the session. If you want to start showing only recent volume, you can reset the VAP counter to display only trade volume that occurs from that moment on. At any time, you can switch back to the total session volume by restoring the VAP counter. To simplify resetting and restoring the VAP counter, MD Trader supports the following shortcuts in addition to the context menu items:

* Double-click anywhere in the VAP column.
* Press the **Shift+R** [hotkey](https://library.tradingtechnologies.com/trade/win-reference.html#widget).

## Direct Prices

The best bid and ask prices displayed for a product are based on the total bid and ask quantities, which include any implied bid and ask quantities. You can use the **Only show direct prices** setting for this widget to filter out the implied prices and quantities for each product added to the widget. Right-click to open the context menu and select **Settings…** to enable/disable **Only show direct prices**.

When the **Only show direct prices** setting is checked (enabled), implied prices are filtered out and only direct prices are shown, and implied bid and ask quantities are not included in the best bid and ask quantities. When unchecked (disabled), best bid and ask prices and quantities include both direct and implied values.

## Indicative Prices

MD Trader displays indicative or theoretical open prices that are provided by the exchange during Pre-Open or Auction market states. During these market states, the indicative price is used for calculating the net change displayed in MD Trader and your P/L displayed in the Positions widget. If you [recenter MD Trader](../task-md-trader/recentering-md-trader.md), the indicative open price is used as the reference price for recentering the market.

If an exchange provides an indicative open (matched) price, MD Trader highlights the price column cell with the default LTP Column [color settings](../task-md-trader/configuring-md-trader.md#mdt-colors) (or your customized settings):

* The initial indicative price uses the Last Trade Price “Stable” colors.
* If the indicative price is higher than the previous indicative price, MD Trader highlights the price using the Last Traded Price “Uptick” colors
* If the indicative price is lower than the previous indicative price, MD Trader highlights the price using the Last Traded Price “Downtick” colors.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-indicative-price2.png)

If the indicative Bid and Ask prices do not cross or match during the Pre-open or Auction states, a yellow border displays in the corresponding **Bids** and **Asks** columns:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-indicative-open1.png)

Upon receiving a new price update during an open trading market state, MD Trader restores any previously highlighted indicative price cells in the price column to the **Price Column** default colors defined in **Settings: MD Trader**.

## Theoretical Prices

For [Advanced Options](https://library.tradingtechnologies.com/trade/aop-overview.html) users, the theoretical value of an option or strategy instrument is displayed as a laser line in the Price column.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-theo-price.png)

## Detailed depth in MD Trader

Some exchanges provide detailed depth allowing you to see every order at a price level.

**Note**: TT supports detailed depth for the following exchanges: ASX, ATHEX, B3, CFE, CME, CME\_BrokerTec, EPEX, JPX, NASDAQ\_NED, NDAQ\_EU, Nord Pool, OSE, TFEX and SGX.

You can view detailed depth in MD Trader by checking the **Show detailed depth on hover** checkbox in [Settings: MD Trader](../task-md-trader/configuring-md-trader.md). When this option is enabled, you can see the quantity of each individual order at a price level for an instrument that supports detailed depth.

To display detailed depth, hover on the total number of bids in the **Bids** column or total number of asks in the **Asks** column at each level of depth in the price ladder. In the depth column that appears, the top row shows the quantity of the order that is best in queue at that price.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-detailed-float.png)

Up to ten levels of detailed depth are displayed at once. You can scroll through the column to view any additional levels that may be provided. To close the display, click away from the Bids or Asks column.

## Implied Quantities

MD Trader can display an asterisk in the Bids and Asks price levels to indicate that all or part of the displayed quantity at a price level includes implied quantities. To help visualize the implied quantities, you can enable the **Show implieds with an asterisk (\*)** widget [setting](../reference-md-trader/md-trader-reference.md), which will display an asterisk next to quantities that are partially or completely implied, as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-implied-quantites.png)

## Resting Market Orders

If provided by the exchange, quantities of resting Buy/Sell pre-open Market orders, as well as “On Auction” and “On Close” Market orders during Auction states are displayed in the top right of the header panel in MD Trader. The **B:** field displays the total quantity of resting Buy Market orders, and the **A:** field displays the total quantity of resting Sell Market orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-resting-quantity.png)

←[Previous PostMD Trader Display](md-trader-display.md)

[Next PostTrading with MD Trader](trading-with-md-trader.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-market-data1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-static.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-center-bar.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-price-move2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-mdt-floating-price.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-ltq.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-same.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-high1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-ltq-low1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-ltp-highlight2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-mkt-mdt-vap2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-vap-hover.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-indicative-price2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-indicative-open1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-theo-price.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/trade-mdt-detailed-float.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-implied-quantites.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mdt-resting-quantity.png
