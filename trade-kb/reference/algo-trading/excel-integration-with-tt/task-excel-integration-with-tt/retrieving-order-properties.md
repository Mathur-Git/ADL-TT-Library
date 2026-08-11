---
title: Retrieving order properties
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-order-properties/
---

# Retrieving order properties

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-order-properties/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Pulling live data into Excel (RTD)](../../../../guides/algo-ops.md#pulling-live-data-into-excel-rtd)

The TT RTD Server allows you to retrieve information about individual orders, such as the order properties shown in an Order Book, using an RTD formula. In the following example, the formula retrieves the value of the **Price** order property for the order identified by a **TextTT** value of **ABC**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-order-properties-ob-column.png)

The RTD formula for extracting order information uses the following format.

> ```
> =RTD("tt.rtd",,"Order",order-property,filter)
> ```

**Note**: The second parameter is the name of the external server running the RTD Server. As the TT RTD Server always runs locally, you must omit a value for the second parameter or supply an empty string (“”). However, you must account for the parameter in the formula.

The *order-property* parameter can be any property available in the [Order Book columns](../../../order-management/order-book/reference-order-book/order-book-reference.md), as well as any input and output parameters of an algo order.

Note: The name of the property must match exactly, including capitals, spaces, and special characters.

The *filter* parameter must identify precisely one order, using either of the following formulas:

* **TTOrderID=*order-id***, where *order-id* is the TT Order ID for the order.
* **TextTT=*tag-value***, where *tag-value* is the value of TextTT field associated with the order.For ADL algos launched with an **Instance name** in [Algo Dashboard](../../algo-dashboard/task-algo-dashboard/launching-an-algo-from-the-algo-dashboard.md) that also set the **Order Tag** property of the [Order](../../../../../adl-kb/reference/trading-blocks/order-block.md) or [Discrete Order](../../../../../adl-kb/reference/trading-blocks/discrete-order-block.md) blocks, the TextTT field for child orders will be modified using the form, *instance-name***:***order-tag-value*.

**Note**: If the filter matches more than one order, the RTD formula returns an error.

For example, if you want to retrieve the **Contract** property of the order whose **TextTT** property is **bbb**, you need only enter the following formula in a cell.

> ```
> =RTD("tt.rtd",,"Order","Contract","TextTT=bbb")
> ```

After processing the formula, Excel displays the result in the cell, similar to the following. Note that the “$” in the cell references are Excel mixed reference notations, and the & symbol joins the values of the two cells to create the string, “TextTT=bbb”.

Note: Do not include the quotation marks around values in cells that you reference in a formula.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rtd-order-properties-spreadsheet.png)

## Retrieving ADL algo exported variables

You can also retrieve the values of exported variables from ADL algos. To identify a algo variable, you specify the *order-property* in the form, *block.connector*, where *block* is the name of the ADL block and *connector* is the name of its output port.

For an input block value, include only the block name. For example:

> ```
> =RTD("tt.rtd",,"Order","Instrument0","TextTT=myalgo")
> ```

For an output block value, use the name of the connector shown in the Exports tab for the variable. For example:

> ```
> =RTD("tt.rtd",,"Order","Entry Fill.fillPrice","TextTT=myalgo")
> ```

**Note**: The names of the block and connector must match exactly, include capitals, spaces, and special characters. For blocks with only one output port, such as an **Add** block, omit the connector.

Suppose you want to access some information from the following ADL algo, including the exported variables are shown in the Exports tab as well as the Instrument ID from the Instrument0 input block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-algo-variables.png)

To retrieve these values from the algo order, you would include RTD formulas similar to the following (notice the matching spaces and capitalization):

* For the **Instrument0** input block:
  > ```
  > =RTD("tt.rtd",,"Order","Instrument0","TextTT=myalgo")
  > ```
* For the output of the Add block named **Exit Price**:
  > ```
  > =RTD("tt.rtd",,"Order","Exit Price","TextTT=myalgo")
  > ```
* For the **fillQuantity** output of the Time and Sales block named **Entry Fill**:
  > ```
  > =RTD("tt.rtd",,"Order","Entry Fill.fillQuantity","TextTT=myalgo")
  > ```
* For the **fillPrice** output of the Time and Sales block named **Entry Fill**:
  > ```
  > =RTD("tt.rtd",,"Order","Entry Fill.fillPrice","TextTT=myalgo")
  > ```

←[Previous PostRetrieving time and sales data](retrieving-time-and-sales-data.md)

[Next PostRetrieving working orders and fills](retrieving-working-orders-and-fills.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-order-properties-ob-column.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rtd-order-properties-spreadsheet.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-export-algo-variables.png
