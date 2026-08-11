---
title: Using the Depth widget
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/depth/task-depth/using-the-depth-widget/
---

# Using the Depth widget

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/depth/task-depth/using-the-depth-widget/)
>
> **Interpreted in:** [Market Data & Depth § Depth widget & book imbalance](../../../../guides/market-data-and-depth.md#depth-widget-book-imbalance)

Use the Depth widget to:

* View [detailed depth](#detailed) if provided by the exchange, or all levels of available aggregate depth
* [Submit orders](#submit) at each level of depth
* View [counterparty data](#counterparty) if provided by the exchange
* View [market depth for orders](#orders) in the Order Book
* View [depth for multiple instruments](#tab) in a single widget.

## Viewing detailed and aggregate depth in the Depth widget

Detailed depth is displayed by default, but you can view aggregate depth for an instrument using the **Show/Hide Detailed Depth** context menu option.

To view detailed and aggregate depth:

1. Open a stand-alone or launch a linked Depth widget for an instrument.

   Detailed depth is displayed for the selected instrument.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-detailed1.png)

   **Tip**: Enable the [Show summary rows](../reference-depth/depth-reference.md) widget setting to display the total Bid and Ask quantities at each price level of detailed depth.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-detailed-summary.png)
2. To view aggregate depth, right-click in the widget and select **Hide Detailed Depth** in the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-hide-detailed.png)

   All levels of aggregate depth provided by the exchange for the instrument are displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-aggregate1.png)

## Submitting orders from the Depth widget

To submit orders:

1. Open a stand-alone or launch a linked Depth widget for an instrument.
2. Select a level of market depth and click a cell in the **BidQty**, **Bid**, **Ask**, or **AskQty** column to open your default order entry widget seeded with the selected market data.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-orders2.png)

   Optionally, right-click in the widget away from these columns and select **Open** | **Order Ticket** or **Open** | **MD Trader** from the context menu.

## Adjusting Orders with the Floating Order Book (FOB)

Launch the Floating Order Book (FOB) directly on the bid or ask cell to update or cancel a working order.

The FOB will launch based on the method defined in the global **Preferences | Orders** menu in the “Floating Order Book” section.

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/07/depth-orders3.png)

## Viewing counterparty data in the Depth widget

When detailed depth is displayed in the Depth widget, you can view counterparty codes or names at each level of depth if this data is provided by the exchange.

To view counterparty data:

1. Open a stand-alone or launch a linked Depth widget for an instrument.
2. Right-click in the column headers and click **Edit columns…** to select the **BidMbr** and **AskMbr** columns and click **OK**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-edit.png)

   The counterparty code or name is displayed in the **BidMbr** and **AskMbr** columns.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-display-1.png)

## Viewing market depth for orders in the Order Book

If you [create a widget group](../../../overview/widgets/task-widgets/working-with-widget-groups.md) that includes the Depth widget and the Order Book, selecting a working or filled order for an instrument in the Order Book shows the market depth for that instrument in the Depth widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-group.png)

## Viewing depth for multiple instruments

Using tabs, you can view market depth for multiple instruments in a single Depth widget. You can also change the instrument displayed in the widget.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-multiple-overview.png)

To add an instrument to the widget, click the **+** sign on the tab to open the Market Explorer and select an additional instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-multiple.png)

To change an instrument displayed in the widget, right-click the tab and select **Change instruments** from the
context menu to select a new instrument using Market Explorer.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-change-instruments.png)

**Note**: To use tabs, ensure the **Show tabs** option is enabled in the Depth widget settings. This option is enabled by default.

←[Previous PostLaunching Depth from Market Grid](launching-depth-from-market-grid.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-detailed1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-detailed-summary.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-hide-detailed.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-aggregate1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-orders2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/07/depth-orders3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-display-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-group.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-multiple-overview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-multiple.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-widget-change-instruments.png
