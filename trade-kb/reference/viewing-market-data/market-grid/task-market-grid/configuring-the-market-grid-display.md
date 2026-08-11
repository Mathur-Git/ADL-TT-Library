---
title: Configuring the Market Grid display
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/task-market-grid/configuring-the-market-grid-display/
---

# Configuring the Market Grid display

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/task-market-grid/configuring-the-market-grid-display/)

You can configure the display of instruments and market data in the Market Grid by doing the following:

* Changing and reordering columns
* Adding label rows
* Customizing the font and colors for rows
* Coloring rows by year
* Highlighting price updates
* Renaming instrument names
* Enabling Live Only mode

## Changing and reordering columns

You can configure the Market Grid display by changing and reordering columns within the grid. You can also set the bold font and text alignment for each column.

**Note:** If the widget level bold setting is enabled, the column-level bold option is not available.

To change and reorder columns:

1. Right-click in the Market Grid and click **Settings…** in the context menu.
2. In the **Settings: Market Grid** screen, click **Set Market Grid columns**.
3. Check/uncheck each column name to show/hide a column and click **OK**.If desired, click **Sort** to view the list of columns in alphabetical order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-columns.png)
4. To reorder the columns, click-and-hold a column title and move it to a different location in the list.**Tip**: You can also click-and-hold a column header and drag it to a new location directly in the Market Grid.
5. To set bold font for a column, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-bold-2.png) next to a column in the context menu. When bold is active for a column, the button will be highlighted (![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-bold-on-2.png)).
6. To set the text alignment for a column, click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-align-2.png) to the right of the column name to cycle through the left, centered, and right text alignment settings. You can also adjust the arrangement of your columns by clicking and dragging each column name.
7. Click **Save**.

## Adding label rows

You can add label rows to help you identify different sections of rows in the Market Grid similar to the following:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-intro.png)

To add a label row:

1. Right-click below the place you want to add the label row, and select **Insert label row…**.
2. Enter the desired label text and press <Return>.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-1.png)

   The label row is added.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-2.png)

**Note**: You can also add a label row by selecting a row in the grid and typing the apostrophe (‘) key.

To rename a label row:

1. Right-click on the label row text and select **Edit label**.
2. Enter the new label name and press **Enter**.

To remove a label row, right-click on the row and select **Remove row** from the context menu.

To change label row colors:

**Note**: Color changes to label rows or any other Market Grid option are applied to the entire widget, including all tabs on that widget.

1. Right-click in the Market Grid and select **Settings: Market Grid**.
2. Expand the **Colors** settings and scroll to **Label Row** to [customize the colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-color-label-row.png)
3. Click **Apply** and **Save**.

## Customizing the appearance of rows

You can customize the font size, row height and colors of each individual row in the Market Grid using the **Row appearance** context menu options.

To customize the font size for rows, right-click a row and select **Row appearance > Font size** to choose a font size.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-font.png)

To customize the row height, right-click a row and select **Row appearance > Row height** to choose a height.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-height.png)

To change the color of the text or background, right-click the row and select **Row appearance > Color(s) > Set text color…** or **Set background color…**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-colors.png)

**Note**: The column colors set in **Settings: Market Grid** | **Colors** will override the custom colors set for the row.

## Coloring rows by year

You can enable row coloring to show all contracts within rolling 12-month periods with different colors.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-color-rows.png)

To color contracts for successive years:

1. Right-click in the grid to display the context menu, and select **Settings**.
2. In the [Market Grid Settings](../reference-market-grid/market-grid-reference.md), enable the **Color rows by year** setting.
3. Click **Apply** and click **Save**.

## Highlighting price updates

To highlight a price cell every time it updates:

1. Right-click in the grid to display the context menu, and select **Settings**.
2. In the Market Grid Settings, enable the **Highlight price cells on update** setting.
3. Click **Apply** then click **Save**.

## Renaming an instrument in the Market Grid

Optionally, you can rename the instruments displayed in the Market Grid by right-clicking the instrument name in the **Contract** column and selecting **Rename Instruments…** in the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-rename-1.png)

In the **Rename Instrument** dialog box that opens, enter the new instrument name and click **Save**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-rename-2.png)

## Hiding instruments in the Market Grid

Instruments can be hidden from view by [applying a column filter](../../../overview/widgets/task-widgets/organizing-the-widgets-menu.md) to the **Contract**.
Hover over the right side of the **Contract** header and click the **caret**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-1.png)

From the popup, tick **All**, then deselect the intruments you would like to hide from view by unticking the **checkboxes** next to contract name.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-2.png)

The unticked contracts will be hidden from view and the header highlighted yellow to indicate that the filter has been applied.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-3.png)

To remove the filter and show all of the instruments, click the filter icon in the **Contract** header, then click **Clear Filter**.

## Enabling Live Only Mode

Market Grid supports a Live Only mode that allows you to hide instruments that are not currently being traded. When you enable Live Mode, the Market Grid displays only instruments that have an active bid, active offer, or last-traded price (LTP).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-enable-live-only-mode-1.png)

←[Previous PostSubscribing to Products in the Market Grid](subscribing-to-products-in-the-market-grid.md)

[Next PostOpening Widgets in the Market Grid](opening-widgets-in-the-market-grid.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-columns.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-bold-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-bold-on-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wgt-align-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-add-label-row-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-color-label-row.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-font.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-height.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-customize-row-colors.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-color-rows.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-rename-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-rename-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-hide-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-enable-live-only-mode-1.png
