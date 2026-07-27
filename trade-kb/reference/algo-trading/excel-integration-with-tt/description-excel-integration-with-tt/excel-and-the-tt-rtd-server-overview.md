---
title: Excel and the TT RTD Server overview
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-and-the-tt-rtd-server-overview/
---

# Excel and the TT RTD Server overview

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-and-the-tt-rtd-server-overview/)

The TT RTD Server allows traders to display live data from TT (market data, position, etc.) in an Excel spreadsheet. The TT RTD Server supports two types of properties you can retrieve from TT:

* [Type 1 properties](../reference/excel-rtd-properties.md#type1) return single values with no filtering support.
* [Type 2 properties](../reference/excel-rtd-properties.md#type2) also return single values but allow you apply filters for the results.

For example, the following spreadsheet uses the TT RTD Server to populate the cells with market data for three GE instruments (Jun16, Sep16, Dec16) from the CME exchange. As market data for any of the instruments change, the values update automatically in the spreadsheet.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rtd-intro.png)

**Note**: To use the TT RTD Server, you first need to install the TT Excel Add-In for Microsoft Excel 2010, or higher. For information, see [Excel Integration with TT: Overview](excel-integration-with-tt-overview.md).

TT provides a sample RTD spreadsheet that you can use as a template for creating your own spreadsheet. The sample spreadsheet shows how to define Excel formulas that retrieve instrument IDs, retrieve instrument property values and apply account filters.

The TT Excel Add-in installation downloads the **TT RTD Sample.xlsx** file to the **Desktop**. TT recommends that you copy the file to a different location and modify the copy as the original will be overwritten when newer versions are installed.

←[Previous PostExcel linking overview](excel-linking-overview.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rtd-intro.png
