---
title: Adding laser lines to MD Trader
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/adding-laser-lines-to-md-trader/
---

# Adding laser lines to MD Trader

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/adding-laser-lines-to-md-trader/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Driving algo variables from Excel (linking)](../../../../guides/algo-ops.md#driving-algo-variables-from-excel-linking)

MD Trader lets you add laser lines to the price ladder that provide visual cues for prices you consider important. When you paste a link from an Excel spreadsheet into MD Trader, a laser line appears at the approximate value of the link in relation to the price level. For example, suppose you use an Excel spreadsheet to calculate a set of theoretical prices that you want to use in your trading strategy. By adding laser lines at those values, you can monitor when the market approaches your theoretical price.

**Tip**: If you paste links from Excel and save the workspace, the links will be preserved and then restored when you re-open the workspace.

To add laser lines to MD Trader:

1. In the Excel spreadsheet, right-click on the cell containing the price you want to use as a laser line and select **Copy link to TT**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-spreadsheet.png)
2. Open an MD Trader widget for the desired instrument, if it is not already open.
3. From the MD Trader context menu, select **Paste Link From Excel**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-mdt-menu.png)

   A red laser line appears in the price ladder proportionally within the price level associated with the value in the spreadsheet cell.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-result.png)
4. To verify the value is linked correctly, change the value in the linked cell in the spreadsheet, in this case to **2035.6**. The laser line automatically moves the to the new location in the price ladder.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-updated.png)

## Modifying laser lines in MD Trader

To modify the appearance of the laser lines added in MD Trader, right-click the line and select **Laser line appearance** in the context menu to choose the available options.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-appearance.png)

## Removing the Excel links

To remove Excel links from a widget:

1. In the widget field linked to Excel, right-click to display the context menu.
2. Select **Unlink from Excel**.

←[Previous PostConnecting TT to Excel spreadsheets](connecting-tt-to-excel-spreadsheets.md)

[Next PostLinking – Sharing data between Autotrader and Excel](linking-sharing-data-between-autotrader-and-excel.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-spreadsheet.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-mdt-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-result.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-updated.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-laser-line-appearance.png
