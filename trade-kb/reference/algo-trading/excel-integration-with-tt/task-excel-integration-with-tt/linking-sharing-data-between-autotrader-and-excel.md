---
title: Linking – Sharing data between Autotrader and Excel
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel/
---

# Linking – Sharing data between Autotrader and Excel

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel/)

TT lets you easily share data between the [Autotrader](../../autotrader/description-autotrader/autotrader-overview.md) widget and your Excel spreadsheet. You can:

* [Access Excel data to populate user variables in the Autotrader widget](#from-excel)
* [Display Autotrader cell values containing an algo’s exported variables in Excel](#to-excel)

## Linking to user variables in Autotrader

Autotrader allows you to link Excel spreadsheets into any editable, numeric cell corresponding to algo user variables. In this manner, you can seed Autotrader with values from your own Excel spreadsheets.

**Tip**: If you paste links from Excel and save the workspace, the links will be preserved and then restored when you re-open the workspace.

To link Excel data to algo user variables in Autotrader:

1. In Excel, select the desired range of cells; then right-click in the cell range and select **Copy link to TT**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-spreadsheet-menu.png)
2. In the Autotrader widget, select the desired algo and click **New** to add the desired number of instances.
3. Select the user-defined variables to link. Ensure that the selected range matches the range of cells you selected in Excel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-select-range.png)
4. Right-click in the range, and select **Paste Link From Excel** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-paste-menu.png)

   The values update to match those linked from Excel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-result.png)
5. To verify the values linked correctly, change the values for the linked cells in the spreadsheet. In this case, the quantities were all incremented by 10. The changes are immediately reflected in Autotrader.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-updated.png)

## Exporting Autotrader cell values to Excel

Autotrader lets you export values from an algo to Excel, which allows your spreadsheet to monitor algo block outputs. This feature requires your ADL algo to [export ADL block outputs](../../../../../adl-kb/reference/adl-overview/advanced-concepts/task/exporting-block-outputs.md).

To export Autotrader cell values to Excel:

1. Verify that the ADL algo you are launching in Autotrader has exported the desired block outputs.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-1.png)

   You can reference the values for any of the exported **Block Name** outputs.
2. In Autotrader, launch the algo and add the desired number of rows; then configure the user-defined variables for each of the algo instances as desired.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-2.png)
3. Select the cells you want to export; then select **Copy link to Excel** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-3.png)
4. In the Excel spreadsheet, select the cells and paste the contents into the selected cells.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-4.png)

   **Note**: If the algos are not currently running, the cells in Excel will display **Initializing** as it waits for data from Autotrader.
5. In Autotrader, start the algo instances to populate the cells.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-5a.png)

   The values from the Autotrader cells dynamically update in the spreadsheet.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-5b.png)

## Removing the Excel links

To remove Excel links from a widget:

1. In the widget field linked to Excel, right-click to display the context menu.
2. Select **Unlink from Excel**.

To remove exported links from your spreadsheet:

1. In the Excel spreadsheet, select the cell or cells you want to clear.
2. From the right-click context menu, select **Clear Contents**.

←[Previous PostAdding laser lines to MD Trader](adding-laser-lines-to-md-trader.md)

[Next PostLinking – Using instruments and accounts in your spreadsheet](linking-using-instruments-and-accounts-in-your-spreadsheet.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-spreadsheet-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-select-range.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-paste-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-at-updated.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-5a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-at-5b.png
