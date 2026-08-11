---
title: Excel linking overview
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-linking-overview/
---

# Excel linking overview

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-linking-overview/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Excel / RTD linking](../../../../guides/algo-ops.md#excel-rtd-linking)

TT supports linking from Microsoft Excel spreadsheets to a variety of TT widgets so you can leverage spreadsheet data. If you use spreadsheets to drive your trading strategies, you can feed the results of your spreadsheet calculations into TT and the widgets will update automatically when your spreadsheet calculations change.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-linking-intro.png)

You can use Excel links in the following widgets:

* MD Trader®
* Autotrader

## Before you begin

To link from Excel spreadsheets, you first need to [set up TT workspaces and Microsoft Excel 2010 or higher](excel-integration-with-tt-overview.md).

## Alerts and messages displayed when the Excel and TT connection is disrupted

When you launch algos that use linked data from the Excel connection, TT requires the connection to be established during the life of the algo. As a safety precaution, TT automatically pauses all running algos with Excel links if the connection is broken while the workspace is open. If you close the workspace, however, the algos will not be paused and will continue to run.

### When you close Excel

If you exit the Excel application while an algo using links is running, TT displays an alert dialog.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-dialog.png)

### When you close widgets

The Autotrader or Algo Dashboard widgets keep track of algos that rely on Excel links, so the widget that launches an algo must remain open for the algo to continue running. If you try to close it while algos are running, TT displays the following dialog to confirm your choice.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-widget-dialog.png)

### When you close the workspace

If you try to close a workspace that contains running algos with Excel links, TT displays a dialog similar to the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-workspace-dialog.png)

Caution If you choose to **Leave this Page**, the workspace closes. However, the algos will not be paused and will continue to run. Also, the linked values will be converted to static values and will not change while the algos continue to run.

←[Previous PostExcel integration with TT overview](excel-integration-with-tt-overview.md)

[Next PostExcel and the TT RTD Server overview](excel-and-the-tt-rtd-server-overview.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-linking-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-widget-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-workspace-dialog.png
