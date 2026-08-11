---
title: Excel integration troubleshooting
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/excel-integration-troubleshooting/
---

# Excel integration troubleshooting

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/excel-integration-troubleshooting/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Pulling live data into Excel (RTD)](../../../../guides/algo-ops.md#pulling-live-data-into-excel-rtd)

## If the .NET installation fails

**Note**: In some instances, the installation of .Net 4.6 will fail with a message similar to the following.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/visual-studio-error.png)

The cause of this issue is still under investigation by Microsoft. In the interim, customers that experience this issue can perform the following steps to work around this issue:

1. In Windows Explorer, navigate to the **VSTO 10.0** folder. The path indicated in the error message should be something similar to **C:Program Files (x86)Common FilesMicrosoft sharedVSTO10.0** or **C:Program FilesCommon FilesMicrosoft sharedVSTO10.0**.
2. In that folder, you should find a file named **VSTOInstaller.exe.config**. Rename it to **VSTOInstaller.exe.config.old**. (Ignore the warning from Windows about the file becoming unusable.)
3. Run the installation program again.
4. Undo the rename listed in step 2.

←[Previous PostIntegration with a web proxy](integration-with-a-web-proxy.md)

[Next PostAlerts and messages displayed when the Excel and TT connection is disrupted](alerts-and-messages-displayed-when-the-excel-and-tt-connection-is-disrupted.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/visual-studio-error.png
