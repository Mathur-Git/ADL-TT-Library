---
title: Linking Excel Data to the Algo Dashboard
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/linking-excel-data-to-the-algo-dashboard/
---

# Linking Excel Data to the Algo Dashboard

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/linking-excel-data-to-the-algo-dashboard/)

By leveraging the Autotrader Widget, users can populate user variables with RTD Excel data in the Algo Dashboard. There are two methods to populate values from Excel into ADL.

* Direct copy: Copying specific cells from Excel and pasting into ADL.
* RTD linking: Using the Autotrader widget to link the values from Excel.

**Note**: You must properly configure your environment prior to using TT with Excel. Refer to the articles in the [Excel Integration with TT](../../../../../trade-kb/reference/algo-trading/excel-integration-with-tt/description-excel-integration-with-tt/excel-integration-with-tt-overview.md) section in the Trade help.

#### Copying and Linking Values

To copy values from Excel to ADL:

1. Verify that you have the Excel application opened and it is highlighted in the ADL taskbar.
2. In Excel, right-click on the desired cell and select **Copy Link to TT**.
3. In the Autotrader widget, right-click the User-Defined Value (UDV) field and select **Paste Link From Excel**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-1.jpg)
  
![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-2.jpg)

For more information on this method, refer to the [Linking – Sharing Data Between Autotrader and Excel](../../../../../trade-kb/reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel.md) article in the Trade help section.

#### RTD Linking Values

If you have an algo with User Defined Variables (UDV), and want to RTD link values into these, you cannot use the UDV spaces in the Algo Dashboard. You should instead use the Autotrader Widget to utilize the RTD Linking functionality.

To RTD Link Values Between Excel to ADL:

1. In the Autotrader widget, select the algo from the **Choose an algo** dropdown menu.
2. Click the **Add row** button.
3. Right-click on the RTD link and select **Paste Link From Excel**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-3.jpg)
![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-4.jpg)

←[Previous PostFormula Editor](formula-editor.md)

[Next PostLeave orders on cancel or pause](leave-orders-on-cancel-or-pause.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-2.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-3.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-linking-excel-4.jpg
