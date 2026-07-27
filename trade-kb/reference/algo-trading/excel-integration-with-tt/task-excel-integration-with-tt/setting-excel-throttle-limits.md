---
title: Setting Excel throttle limits
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/setting-excel-throttle-limits/
---

# Setting Excel throttle limits

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/setting-excel-throttle-limits/)

Excel automatically limits the rate at which it checks for updates. By default, it sets the throttling rate to 2000
milliseconds (2 seconds). In a fast-paced trading environment, such an update might not be sufficient. TT recommends
that you disable the default Excel throttling rate by setting its value to 0. With this value, Excel continuously
checks for updates, ensuring that you have accurate and up-to-date values.

To set the throttle interval through the Excel object model:

1. In Excel, open the Visual Basic Editor.

   **Note**: If you need more information about opening the Visual Basic Editor, consult the Microsoft help for
   your version of Excel.
2. In the **Immediate** window (press **CTRL+G** or click **Immediate Window** on the **View** menu),
   type this code: `Application.RTD.ThrottleInterval = 0`, and then press **ENTER**.
3. To verify that it is set correctly, type this line of if code in the **Immediate** window:
   `? Application.RTD.ThrottleInterval` and press **ENTER**.
4. You can close the Visual Basic Editor, if desired.

Alternatively, you can set the throttle interval directly through the Windows registry (For information about
editing the registry, consult Microsoft help for your operating system). Set (or create, if missing) the following
registry key to 0 (It is a DWORD and the value is in milliseconds):

> ```
> HKEY_CURRENT_USERSoftwareMicrosoftOffice15.0ExcelOptionsRTDThrottleInterval
> ```

**Note**: This example uses the path for Excel 2013. If you use a later version, you will need to use the
appropriate version number in the path.

←[Previous PostCombining multiple filters](combining-multiple-filters.md)

[Next PostCalculating Realized and Unrealized P/L](calculating-realized-and-unrealized-p-l.md)→

