---
title: Coinbase to TT Transition Guide
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/trading-crypto-on-tt/reference-trading-crypto-on-tt/coinbase-to-tt-transition-guide/
---

# Coinbase to TT Transition Guide

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/trading-crypto-on-tt/reference-trading-crypto-on-tt/coinbase-to-tt-transition-guide/)

Use this guide to map functionality in the Coinbase trading interface to the same functionality provided in your
TT® workspace.

For the items labeled in the following Coinbase trading interface…

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-gdax-gui-pro.png)

…the [widgets](../../../overview/widgets/description-widgets/widgets-overview.md) that provide the same trading functionality and more are
labeled in the following TT [workspace](https://library.tradingtechnologies.com/trade/win-workspaces-overview.html).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-tt-crypto-workspace-new-cb1.png)

The following widgets are labeled in the TT workspace above (equivalent Coinbase trading interface name is in
parenthesis):

1. [Market Grid (Coinbase Title bar)](#mg) — Displays market and pricing data for a user-defined
   list of currencies.
2. [Order Ticket (Order Form)](#ot) — Used for entering orders from the Market Grid widget.
3. [MD Trader® (Order Book)](#mdt) — Displays prices in a vertical price ladder and shows
   working quantities on both sides of the market at each price level. You can also [enter
   orders from MD Trader](#mdt-order).
4. [Charts (Price/Depth Chart)](#charts) — Displays the historical price data for an asset at
   specific time intervals.
5. [Time and Sales (Trade History)](#ts) — Shows the trade history of an asset. You can view the
   trade history of the cryoptocurrency you are trading, as well as add cryptocurrencies to the widget to view
   trade history for multiple instruments.
6. [Order Book (Open Orders)](#ob) — Shows your working orders. Click on a working order to change
   it’s price or quantity and resubmit it in the market. The Fills widget (Fills) shown below the Order Book shows
   your partially filled and fully filled orders.
7. [Assets widget (Wallet Balance)](#assets) — Shows the balance of each asset in your Coinbase
   wallet.

There are a few key differences between the Coinbase and TT workspaces:

* TT’s workspace allows you to add and arrange widgets into whatever configuration fits your trading style.
* TT displays market data and allows you to trade multiple currencies within the same workspace.
* You must still log in to Coinbase to move funds between your Coinbase wallet and your Coinbase account in order
  to make currencies available for trading on Coinbase using TT.

## Market Grid (Coinbase Title Bar)

The Market Grid widget displays volume and pricing information for a list of selected instruments similar to the
Coinbase Title Bar, which displays trading volume and price information for a selected product.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-market-grid-pro.png)

Similar to using the Coinbase Title Bar, you can use the Market Grid to:

* [View market data for your selected product.](../task-trading-crypto-on-tt/viewing-crypto-market-data-on-tt.md)
* [View the Last Traded Price, 24-hour price
  change, and the 24-hour volume.](../task-trading-crypto-on-tt/viewing-crypto-market-data-on-tt.md)

In addition, you can also use TT’s Market Grid to:

* [Launch the order ticket widget and quickly place orders for
  the selected currency.](../../../viewing-market-data/market-grid/task-market-grid/trading-from-the-market-grid.md)
* [Configure the display of your list of currencies and add
  label rows.](../../../viewing-market-data/market-grid/task-market-grid/configuring-the-market-grid-display.md)
* [Add columns for additional pieces of market data.](../../../viewing-market-data/market-grid/task-market-grid/configuring-the-market-grid-display.md)
* [Add additional tabs to your Market Grid to organize the display
  of different currencies.](../../../viewing-market-data/market-grid/task-market-grid/using-tabs-in-the-market-grid.md)

## Order Ticket (Order Form)

The [Order Ticket](../../order-ticket/description-order-ticket/order-ticket-overview.md) can be launched from the Market Grid widget. Select an
order type and Time-In-Force, then enter an order quantity and price and click “Buy” or “Sell” to submit the order.

**Note**: You must log into Coinbase to move funds between your Coinbase wallet and your Coinbase
account to make these funds available for trading in TT.



![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-order-ticket-new-order-pro.png)

Similar to using the Order Form, you can use the Order Ticket to:

* [Define the parameters of your order.](../../order-ticket/task-order-ticket/submitting-an-order.md)
* [Auto-populate the price parameter of your order by clicking a
  price in the market grid.](../../../viewing-market-data/market-grid/task-market-grid/trading-from-the-market-grid.md)

In addition, you can also use TT’s Order Ticket to:

* [Place orders using a wide variety of TT Order types.](../../tt-order-types/description-tt-order-types/tt-order-types-overview.md)
* [Create custom order type templates to pre-populate custom
  order parameters.](../../tt-order-types/task-tt-order-types/managing-tt-order-type-templates.md)
* [Launch a linked Order Ticket which will
  switch to whichever currency you have selected in the Market Grid.](../../order-ticket/task-order-ticket/launching-a-linked-order-ticket-from-a-contract-row.md)
* [Group the Order ticket with a Market Grid to create a widget
  group.](../../../viewing-market-data/market-grid/description-market-grid/trading-from-market-grid.md)

## MD Trader (Order Book)

The Coinbase Order Book provides users with “market size” or market depth and the “spread” or inside market between
the best Bid and Ask, as well as the volume at each price level. In TT, this information is provided in the [MD Trader](../../md-trader/description-md-trader/market-data-in-md-trader.md) widget.

Similar to using the Coinbase Order Book, you can use MD Trader to:

* [Only display price levels with working orders.](../task-trading-crypto-on-tt/viewing-crypto-market-data-on-tt.md)
* [Aggregate price levels using Price
  Consolidation.](../task-trading-crypto-on-tt/viewing-crypto-market-data-on-tt.md)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-md-trader-pro.png)

### MD Trader order entry on TT

With MD Trader you can [place an order with a single click](../../md-trader/task-md-trader/recentering-md-trader.md) directly
at each price level. You can also see any orders you have working in the market.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-md-trader-new-orders.png)

In addition to placing an order with a single click, you can use TT’s MD Trader to:

* [Place orders using a wide variety of TT Order types.](../../md-trader/description-md-trader/trading-with-md-trader.md)
* [Create custom order type buttons to quickly access commonly-used
  order types.](../../md-trader/task-md-trader/configuring-md-trader.md)
* [Create custom order quantity buttons.](../../md-trader/task-md-trader/recentering-md-trader.md)
* [Add a tab to your MD Trader to switch between different
  currencies.](../../../overview/widgets/description-widgets/widgets-overview.md)

## Charts (Price Chart)

TT’s [Charts](../../../analytics/charts/description-charts/chart-overview.md) widget also fully integrates charting and analytics into TT Cryto
by blending historical time series data with continuous real-time market data updates.

On Coinbase, the Price Chart shows historical price data at user-defined time intervals. In addition, you can also
view the Depth Chart, which graphically displays the market depth from the Coinbase Order Book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-charts-pro.png)

Similar to using the Coinbase Price Chart, you can use the Charts widget to:

* [Set your chart type to candle.](../../../analytics/charts/description-charts/chart-types.md)
* [Display the Volume technical indicator.](../../../analytics/charts/task-charts/using-technical-indicators.md)

Using TT’s Charts widget, you can also:

* [Create multiple Charts in your workspace.](../../../analytics/charts/task-charts/adding-an-instrument-to-a-chart.md)
* [Place orders directly on the Chart.](../../../analytics/charts/description-charts/chart-trading.md)
* [Select from a whole library of comparisons, overlays, studies and other
  technical indicators.](../../../analytics/charts/description-charts/technical-indicators.md)
* [Use drawing tools to annotate your charts.](../../../analytics/charts/description-charts/drawing-tools.md)
* [Add multiple tabs to your Chart to switch between different
  currencies.](../../../analytics/charts/task-charts/adding-an-instrument-to-a-chart.md)

## Order Book Widget (Open Orders)

Similar to the Coinbase **Open Orders** section, TT’s [Order
Book](../../../order-management/order-book/description-order-book/order-book-overview.md) widget shows your working (open) orders in the market and provides you with the ability to cancel each
working order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-order-book-pro.png)

With TT’s Order Book widget, you can also:

* [Modify existing orders](../../../order-management/order-book/task-order-book/modifying-an-order-in-the-order-book.md).
* [Place orders on hold](../../../order-management/order-book/task-order-book/placing-orders-on-hold.md).
* [Apply Order Management Algos (OMAs) to orders](../../../order-management/order-book/task-order-book/launching-an-oma-in-the-order-book.md).

## Fills Widget (Fills)

Similar to the Fills displayed in the Coinbase trading interface, the [Fills](../../../order-management/fills/description-fills/fills-overview.md) widget on
TT shows the time and price of all fully or partially filled orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-fills-pro.png)

With TT’s Fills widget, you can also:

* [Set your view of fills to a specific day and organize them in chronological or reverse
  chronological order.](../../../order-management/fills/description-fills/fills-views.md).
* [Filter the display of your fills by price or by partial fills that
  constitute an order](../../../order-management/fills/task-fills/filtering-your-fills.md).

## Time and Sales (Trade History)

The trades executed in the market for an individual currency are shown under
**Trade History** in the Coinbase trading interface. In TT, these are displayed using the [Time and Sales](../../../viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md) widget. Users can access historical Time and Sales
data by scrolling to the bottom of the widget screen. The Time and Sales widget on TT maintains and displays a
history of trade data from all of your sessions and not just for the current session.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-time-and-sales-pro.png)

Similar to Coinbase Trade History, the Time and Sales widget displays:

* Buys and sells in different colors.
* “Trade Size” in the “Qty” column.

With TT’s Time and Sales widget, you can also:

* [Highlight orders over a certain quantity.](../../../viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md)
* [Filter your view to display only fills over a particular quantity.](../../../viewing-market-data/time-and-sales/reference-time-and-sales/time-sales-reference.md)
* [View the fills of multiple currencies in the same
  widget.](../../../viewing-market-data/time-and-sales/task-time-and-sales/adding-instruments-to-time-sales.md)

## Assets Widget (Wallet Balance)

To see the funds currently available for trading in TT, you can use the
[Assets Widget](../description-trading-crypto-on-tt/assets-widget-on-tt-crypto.md).

**Note**: You cannot make deposits or withdrawals on TT. Your Coinbase account can only be funded from your
Coinbase wallet using the Order Form.

The **Wallet Balance** section of the Order Form also allows you to transfer funds between your Coinbase wallet
and your Coinbase Pro account and view the balance of each asset.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-assets-widget-pro.png)

## Additional TT Functionality

When trading Coinbase products on TT, you may also want to:

* [Run TT across multiple monitors using TT Desktop](../../../overview/tt-desktop/task-tt-desktop/managing-a-multi-monitor-workspace.md).
* [Customize the color-scheme of your workspace](https://library.tradingtechnologies.com/trade/win-reference.html).
* [Enable or disable order confirmations](../../md-trader/description-md-trader/trading-with-md-trader.md).
* [Define how many decimal points to display
  for currencies](../task-trading-crypto-on-tt/viewing-crypto-market-data-on-tt.md#quantity-display).

←[Previous PostCrypto Reference](crypto-reference.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-gdax-gui-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-tt-crypto-workspace-new-cb1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-market-grid-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-order-ticket-new-order-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-md-trader-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-md-trader-new-orders.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-charts-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-order-book-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-fills-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-time-and-sales-pro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gdx-assets-widget-pro.png
