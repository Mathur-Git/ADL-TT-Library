---
title: Entering orders in Spread Matrix
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/task-spread-matrix/entering-orders-in-spread-matrix/
---

# Entering orders in Spread Matrix

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/task-spread-matrix/entering-orders-in-spread-matrix/)
>
> **Interpreted in:** [Market Data & Depth § Spread Matrix (exchange-listed & inter-product spreads)](../../../../guides/market-data-and-depth.md#spread-matrix-exchange-listed-inter-product-spreads)

Using the Spread Matrix and a floating order entry screen, you can quickly enter orders for all outrights, calendar spreads, or inter-product spreads within a single window for active spread trading.

1. To trade the spread, left click on any of the four cells.

   Your floating order entry window appears.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-orders-condor1-1.png)

   **Note**: The cells containing spread contract names are highlighted to indicate which contracts you are spread trading.
2. Click on the offer to Buy or click on the bid to Sell.
3. Adjust the price as needed and enter your desired quantity.
4. Submit your order.

## Entering an order via the context menu

1. Right-click in the market data cells for a spread to view the context menu.
2. In the context menu, click **Open** to select **MD Trader** or **Order Ticket**.
3. Enter the order for the selected spread.

## Using the order entry panel in Spread Matrix

Spread Matrix supports single-click order entry using the order entry panel. To display the panel, right-click and select the Settings menu, check the **Enable single-click order entry** setting and click **Save**. The order entry panel appears on the left side of the Spread Matrix and works similar to the [order panel in MD Trader](../../../basic-order-entry/md-trader/description-md-trader/trading-with-md-trader.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-order-entry-panel.png)

**Tip**: You can also display the order entry panel by selecting **Show/hide** | **Show order entry panel** from the right-click context menu.

When single-click order entry is enabled, click a Spread Matrix price or quantity cell to submit an order at that price with the quantity set in the order entry panel.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-order-entry-panel-2.png)

When submitting orders using the order entry panel in Spread Matrix, consider the following:

* The Buy/Sell direction of the order adheres to the **Left click aggressive** setting on the
  **Preferences** | **Orders** page. For example, when “Left click aggressive” is checked, left clicks hit/lift the selected bid or offer price and right clicks join the price. When this setting is unchecked, left clicks join the selected price level and right clicks hit/lift the bid or offer.
* A left click on a position cell in the matrix does not submit an order, but seeds the quantity in the order entry panel to allow you to flatten your position on your next click in the Spread Matrix grid.
* You can launch a floating order entry widget (Order Ticket or MD Trader) by holding the Shift key while clicking a price or quantity cell in the matrix.

## Managing orders in Spread Matrix

After submitting an order in Spread Matrix, you can manage the order using the [Floating Order Book](../../../order-management/floating-order-book/description-floating-order-book/floating-order-book-overview.md). Based on your **Preferences** | **Orders** | **Launch floating order book using:** option, you can open the Floating Order Book by clicking the Bid Price or Ask Price for an outright or spread in the matrix.

Once opened, use the Floating Order Book to modify or cancel working orders that you submitted using Spread Matrix or other order entry widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-fob.png)

**Tip**: When the floating order book launch method is set to “left click” in Preferences, a “>” is shown at the right edge of the cell. Clicking the “>” will launch the floating order book.

←[Previous PostDisplaying market data in spread matrix](displaying-market-data-in-spread-matrix.md)

[Next PostCreating spreads in Spread Matrix](creating-spreads-in-spread-matrix.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/view-sm-orders-condor1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-order-entry-panel.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-order-entry-panel-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-fob.png
