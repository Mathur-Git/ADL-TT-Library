---
title: Alerts and messages displayed when the Excel and TT connection is disrupted
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/alerts-and-messages-displayed-when-the-excel-and-tt-connection-is-disrupted/
---

# Alerts and messages displayed when the Excel and TT connection is disrupted

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/alerts-and-messages-displayed-when-the-excel-and-tt-connection-is-disrupted/)

## Alerts and messages displayed when the Excel and TT connection is disrupted

When you launch algos that use linked data from the Excel connection, TT requires the connection to be established during the life of the algo. As a safety precaution, TT automatically pauses all running algos with Excel links if the connection is broken while the workspace is open. If you close the workspace, however, the algos will not be paused and will continue to run.

### When you close Excel

If you exit the Excel application while an algo using links is running, TT displays an alert dialog.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-dialog-1.png)

### When you close widgets

The Autotrader or Algo Dashboard widgets keep track of algos that rely on Excel links, so the widget that launches an algo must remain open for the algo to continue running. If you try to close it while algos are running, TT displays the following dialog to confirm your choice.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-widget-dialog-1.png)

### When you close the workspace

If you try to close a workspace that contains running algos with Excel links, TT displays a dialog similar to the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-workspace-dialog-1.png)

**Caution** If you choose to **Leave this Page**, the workspace closes. However, the algos will not be paused and will continue to run. Also, the linked values will be converted to static values and will not change while the algos continue to run.

←[Previous PostExcel integration troubleshooting](excel-integration-troubleshooting.md)

[Next PostExcel RTD properties](excel-rtd-properties.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-dialog-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-widget-dialog-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-close-workspace-dialog-1.png
