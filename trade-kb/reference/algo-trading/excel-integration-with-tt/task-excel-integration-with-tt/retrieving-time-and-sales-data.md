---
title: Retrieving time and sales data
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-time-and-sales-data/
---

# Retrieving time and sales data

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-time-and-sales-data/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Pulling live data into Excel (RTD)](../../../../guides/algo-ops.md#pulling-live-data-into-excel-rtd)

The TT RTD Server allows you to retrieve real-time [Time and Sales](../../../viewing-market-data/time-and-sales/description-time-and-sales/time-sales-overview.md) data for an instrument, providing details for each trade including side, time, price and quantity. It also indicates whether a trade is a block (OTC) trade and provides the counterparty IDs when provided by an exchange, such as B3.

The following illustration retrieves the 100 most recent updates for the CME ES Dec19 contract.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-ts-example.png)

Note: The TT RTD Server begins retrieving trade data only when the first trade occurs after the formula initializes. Historical time and sales data is not available through RTD.

The RTD formulas for extracing time and sales data using the following format:

> ```
> =RTD("tt.rtd",,"TS",instrument_id,num_of_rows,CELL("address",A1))
> ```

where:

* *instrument\_id* is the ID of the instrument returned by the [INST or Instr formula](rtd-retrieving-instrument-ids-and-properties.md).
* *num\_of\_rows* indicates the number of rows to return (100 max)

**Note**: The second parameter is the name of the external server running the RTD Server. As the TT RTD Server always runs locally, you must omit a value for the second parameter or supply an empty string (“”). However, you must account for the parameter in the formula.

←[Previous PostRTD – Retrieving instrument IDs and properties](rtd-retrieving-instrument-ids-and-properties.md)

[Next PostRetrieving order properties](retrieving-order-properties.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-ts-example.png
