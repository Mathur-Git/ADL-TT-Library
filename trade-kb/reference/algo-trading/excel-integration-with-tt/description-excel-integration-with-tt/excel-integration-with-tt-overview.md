---
title: Excel integration with TT overview
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview/
---

# Excel integration with TT overview

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview/)

TT Excel integration establishes communications between the TT Trade application and Microsoft Excel spreadsheets, and consists of the following:

* [Excel linking](excel-linking-overview.md), which lets you use the results of your spreadsheet calculations in TT widgets.
* [Excel RTD](excel-and-the-tt-rtd-server-overview.md), which lets you display live data from TT (market data, position, etc.).

**Note**: TT supports a maximum size of 100 columns and 5000 rows (starting in cell A1) when copying or pasting cells from Excel into TT.

## Excel integration with TT requirements

Excel integration is currently supported on Windows systems with the following software:

* Microsoft Windows 10, or higher
* Microsoft Excel 2010, or higher, running locally
* Microsoft .NET 4.6 framework**Note**: Installing the TTExcelIntegration add-in will automatically install .NET 4.6, if necessary
* Browsers: Google Chrome, Firefox, or Microsoft Edge**Note**: As Microsoft has discontinued support for Internet Explorer, TT no longer supports Internet Explorer.

**Note**: Please ensure that your workstation host clock is syncing from a reliable time source. If the system is clock is off by more than a minute, the Excel integration will fail to connect.

## DNS requirements

In addition to the [network requirements of the TT platform](../../../overview/tt-platform/description-tt-platform/tt-accounts.md#network), TT’s Excel integration requires DNS access to **localhost-tradingtechnologies.com** on port **8181**.

**Note**: If your enterprise network implements a web proxy, you need to perform additional steps to support Excel intergration. For more information, see [Integration with a web proxy](../reference/integration-with-a-web-proxy.md).

[Next PostExcel linking overview](excel-linking-overview.md)→

