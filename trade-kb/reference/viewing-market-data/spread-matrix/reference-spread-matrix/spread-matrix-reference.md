---
title: Spread Matrix reference
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/reference-spread-matrix/spread-matrix-reference/
---

# Spread Matrix reference

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/spread-matrix/reference-spread-matrix/spread-matrix-reference/)
>
> **Interpreted in:** [Market Data & Depth § Spread Matrix (exchange-listed & inter-product spreads)](../../../../guides/market-data-and-depth.md#spread-matrix-exchange-listed-inter-product-spreads)

## Context menu options

Right-click in the Spread Matrix to open the context menu. On this menu, you can select the following options:

* **Open** — Allows you to open an order entry or Time & Sales widget for a contract.
* **Submit RFQ** — Allows you to submit an RFQ for a contract.
* **Edit Spread** — Allows you to configure synthetic inter-product spreads or spreads created via the
  Custom tab in Spread Matrix. **Note**: This menu option is only available when viewing an inter-product spread
  matrix.
* **Choose legs** — Gives you the ability to check/uncheck each available contract month for the product.
  After checking specific contract months, right-click again and click **Save legs**.
* **Refresh instruments** — Re-downloads instrument defintions for all instruments in the grid.
  You typically need to use this option only if the instrument details, such as ticking size, changed since you
  started the Trade application.
* **Save legs** — Gives you the ability to display each contract month that you’ve selected (checked) for
  that product. When you click **Save legs**, the checkboxes disappear and the selected contracts remain in the
  matrix.
* **Show/hide** — Shows/hides the following:
  * The arrow pad used for navigating through the matrix. The pad is shown by default.
  * The panel containing the Butterfly, Vertical, and Cancel buttons. The button panel is shown by default.
  * The Cancel All, Cancel Spreads, and Cancel Outrights buttons. These order cancel buttons are
    shown by default.
  * An [MD Trader](../../../basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) inside the Spread Matrix. The ladder dynamically adjusts to show
    the market for the selected contract or spread. The MD Trader is hidden by default.
* **Switch to staircase/vertical layout** — Toggles between staircase and vertical orientations for viewing
  market data and positions for outrights and spreads in the matrix.
* **Open…** — When you right-click a contract month, you can open an MD Trader, Order Ticket, Chart, or
  Time and Sales widget.
* **Zoom…** — Opens a slider control that you can use to scale the size of the Spread Matrix display.
* **Settings: Spread Matrix** — Opens the local settings menu.

## Available settings

These settings affect only the selected Spread Matrix widget. To update the default settings with these value for
newly-opened Spread Matrix widgets, or to apply them to existing opened widgets, click **Defaults**.



![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-settings.png)

### Order Entry

**Enable single click order entry** — Displays the order entry panel in Spread Matrix and allows single click order entry.

### Layout

* **Show LTP/LTQ** — Displays a third column that shows the last traded price and quantity for each spread and outright.
* **Show outright LTP** — Toggles the display of the **Last** column in vertical mode to show the last traded price (LTP). Display as either “Price” or “Net Change”, which is the difference between the last traded price and the settlement price for the instrument.
* **Show outright prices across the top** — Displays outright cells at the top of matrix as either “Price” or “Net Change”, which is the difference between the last traded price and the settlement price for the instrument.
* **Show outright prices across the diagonal** — Displays outright cells diagonally below the spread prices. Outrights can be displayed as “Price” or “Net Change”, which is the difference between the last traded price and the settlement price for the instrument.
* **Show prices above quantities** — Displays the bid and ask prices above the bid and ask quantities for each spread and outright.
* **Show positions** — Displays a long or short net position in an outright instrument
* **Show direct and implied quantities on hover** — Displays implied and direct quantities on mouse hover over a particular quantity in an Outright or Spread cell. Cells showing implied and direct quantities are shaded based on the **Colors** settings.
* **Enable right-click on price cells to display context menu**— Allows you to right-click a price or quantity cell in the matrix to display the context menu.
* **Show quantity when hovering over price**— Displays the total Bid or Ask quantity when hovering over a price in the matrix. The quantity cells are hidden for each outright and spread when this setting is enabled.

### Market Data

* **Show spread prices as net change** — Displays spread prices as the difference between the last traded price and the settlement price for the instrument.
* **Only show direct prices** — When this setting is checked (enabled), implied prices are filtered out and only direct prices are shown, and implied bid and ask quantities are not included in the best bid and ask quantities. When unchecked (disabled), best bid and ask prices and quantities include both direct and implied values.
* **Show implieds with asterisk (\*)** — Display an asterisk next to quantities that are partially or completely implied. Valid only when the **Only show direct prices** setting is disabled.

### Display

* **Colors**: Allows you to [customize or change the cell and column colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md) available in the widget.
* **Bold font**: Enable this setting to use bold text in the widget.
* **Cell highlight type** — Sets whether to highlight **Net change** or **Implied prices/quantities** with colors selected in the **Colors** palette. The default setting is **None**.
* **Show tabs** — Check this option to enable tabs in the Spread Matrix or uncheck to hide the tabs
* **Highlight bid/ask price when instrument trades** — Highlights the Bid or Ask price cell for a
  spread or outright when it trades.

## Selective defaults

Spread Matrix lets you select individual customizations to save as default Spread Matrix settings and to update
existing Spread Matrix widgets, while applying other customizations to the current widget. Checking either of the
**Save as Spread Matrix defaults** or **Updating existing Spread Matrix widgets** settings
enables the **Selectively update properties** setting. You can choose the individual widget attributes to
you want to save.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-settings-defaults.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/sm-settings-defaults.png
