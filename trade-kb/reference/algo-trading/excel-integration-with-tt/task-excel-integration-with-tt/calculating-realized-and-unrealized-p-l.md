---
title: Calculating Realized and Unrealized P/L
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/calculating-realized-and-unrealized-p-l/
---

# Calculating Realized and Unrealized P/L

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/calculating-realized-and-unrealized-p-l/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Pulling live data into Excel (RTD)](../../../../guides/algo-ops.md#pulling-live-data-into-excel-rtd)

The following example formulas represent an optimal way to calculate both Realized and Unrealized Profit/Loss (P/L). However, you may need to adjust these values based on your own trading style.

To calculate realized and unrealized P/L, we populate the following cells in the spreadsheet (e.g., A1) with the corresponding RTD properties (e.g., Instrument LTP):

* A1 = Instrument LTP
* B1 = Instrument Point Value
* C1 = BuyQty
* D1 = AvgBuyPrice#
* E1 = SellQty
* F1 = AvgSellPrice#
* G1 = NetPos
* H1 = AvgOpenPrice#

Using these values, we calculate Unrealized P/L (in the contract’s currency) using:

**(Instrument LTP – AvgOpenPrice#) x NetPos x Instrument Point Value**

or

**(A1 – H1) x G1 x B1**

We also calculate Realized P/L (in the contract’s currency) using:

**(AvgSellPrice# – AvgBuyPrice#) x MIN(BuyQty, SellQty) x Instrument Point Value**

or

**(F1 – D1) x MIN(C1,E1) x B1**

For a complete list of available properties, refer to the [Excel RTD Properties](../reference/excel-rtd-properties.md) section.

←[Previous PostSetting Excel throttle limits](setting-excel-throttle-limits.md)

