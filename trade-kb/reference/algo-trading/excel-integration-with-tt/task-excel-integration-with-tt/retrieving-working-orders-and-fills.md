---
title: Retrieving working orders and fills
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-working-orders-and-fills/
---

# Retrieving working orders and fills

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/retrieving-working-orders-and-fills/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Pulling live data into Excel (RTD)](../../../../guides/algo-ops.md#pulling-live-data-into-excel-rtd)

The TT RTD Server allows you to retrieve information about working orders and fills, such as the columns available in the Order Book and Fills widgets, using various RTD formulas. You can:

* [Create order and fill sets](#os)
* [Retrieve working orders](#orders)
* [Retrieve order statistics](#order-stats)
* [Retrieve fills](#fills)
* [Retrieve fill statistics](#fill-stats)

## Working with order and fill sets

An RTD Server application accesses order and fill data through order sets and fill sets, respectively. These sets let you define a subset of orders or fills based on user-defined filtering criteria.

When you create an order set, for example, you create a set of selection rules, called an order selector ID that identifies which of the current orders you want to include in the set. For example, you might create one order set that contains all U.S. 30-Year Treasury Bond (ZB) orders and another order set that contains all buy orders. Also, individual orders can appear in multiple order sets.

The following illustration shows three order sets that provide different views into the whole order
book.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-os-filter-example.png)

Likewise, a fill set lets you use filters to create a subset of fills. For example, you could create one fill set that contains buy-side fills and another fill set that contains only full fills for a specific account.

The following RTD formulas return the selector IDs you can use to retreive information about working orders and fills, respectively.

> ```
> =RTD("tt.rtd",,"OS",filter-criteria)
> ```
>
> ```
> =RTD("tt.rtd",,"FS",filter-criteria)
> ```

where *filter-criteria* contains comma-separated strings of filters using the form:

> ```
> <column-name><operator><value>
> ```

where *column-name* is the name of an [Order Book column](../../../order-management/order-book/reference-order-book/order-book-reference.md) or [Fills column](../../../order-management/fills/reference-fills/fills-reference.md), as well as any input and output parameters of an algo order.

**Notes**:

* The second parameter is the name of the external server running the RTD Server. As the TT RTD Server always runs locally, you must omit a value for the second parameter or supply an empty string (“”). However, you must account for the parameter in the formula.
* The name and value of each property must match exactly, including capitals, spaces, and special characters.

For example, to create an order set that includes all orders for the ES product on the CME exchange using account ABCDEF, you would enter the following RTD formula:

> ```
> =RTD("tt.rtd",,"OS","Exch=CME","Product=ES","Account=ABCDEF")
> ```

## Retrieving working orders

You can use RTD to create custom order books in your spreadsheet. You can use an order set to focus on a particular set of orders and, for each order, include values for columns available in the [Order Book](../../../order-management/order-book/reference-order-book/order-book-reference.md).

The RTD formula for retrieving order information uses the following format:

> ```
> =RTD("tt.rtd",,"Orders",orderbook-columns,num-orders,orderset-id,cell-address)
> ```

where:

* *orderbook-columns* is a comma-separated list of one or more Order Book columns whose values you want to return. **Note**: Add Price# as an attribute for RTD orders and fills to retrieve the raw unformatted price.
* *num-orders* indicates the number of working orders to return. You can use the following methods to specify the number:
  * **“\*”** for all working orders matching the selected filter criteria.
  * **“last\**n*“** or **–*n*** for the *n* most recent working orders. By using this option, you don’t have to handle scrolling lists or to organize the orders, because your spreadsheet always displays the ten most recent orders.
  * **“first\**n*“** or ***n*** for the first *n* working orders.
  * **“*n*:*m*“** for the range of working orders between *n* and *m*, inclusively.
* *orderset-id* is an optional order set ID returned from the [OS formula](#os) to filter the orders. If you omit this parameter, you must account for it in the formula with a comma. Also, if you omit this parameter, the formula will return unfiltered orders.
* *cell-address* is the address of the internal, temporary spreadsheet that contains the array of values specified by the *orderbook-columns* parameter

For example, the following RTD formula retrieves values of six columns for the ten most recent orders within the order set referenced in cell B3. It returns the values in a 6×10 array starting in cell E1.

> ```
> =RTD("tt.rtd",,"Orders","Exch,Product,Contract,OrdQty,Price,Account","last*10",B3, CELL("Address", E1))
> ```

## Retrieving order statistics

You can use RTD to track changes in statistics related to working orders in an order set, such as the number of matching Buy orders.

The RTD formula for retrieving order information uses the following format:

> ```
> =RTD("tt.rtd",,"OrderStats",orderset-id,orderstat-column,cell-address)
> ```

where:

* *orderset-id* is an optional order set ID returned from the [OS formula](#os) to filter the orders. If you omit this parameter, you must account for it in the formula with a comma. Also, if you omit this parameter, the formula will return unfiltered orders.
* *orderstat-column* is one of the following [Order Book](../../../order-management/order-book/reference-order-book/order-book-reference.md) columns:
  * BuyCnt
  * SellCnt
  * NetCnt
  * BuyWrk
  * SellWrk
  * NetWrk
  * BuyPos
  * SellPos
  * NetPos

For example, the following RTD formula retrieves number of working Buy orders within the order set referenced in cell B3.

> ```
> =RTD("tt.rtd",,"OrderStats",B3,"BuyCnt")
> ```

## Retrieving fills

You can use RTD to monitor fills in your spreadsheet. You can use a fill set to focus on fills for a particular set of orders and, for each fill, include values for columns available in the [Fills](../../../order-management/fills/reference-fills/fills-reference.md) widget.

The RTD formula for retrieving fill information uses the following format:

> ```
> =RTD("tt.rtd",,"TTFills",fills-columns,num-fills,fillset-id,cell-address)
> ```

where:

* *fills-columns* is a comma-separated list of one or more Fills columns whose values you want to return. **Note**: Add Price# as an attribute for RTD orders and fills to retrieve the raw unformatted price.
* *num-fills* indicates the number of fills to return. You can use the following methods to specify the number:
  * **“\*”** for all fills for orders in the specified order set.
  * **“last\**n*“** or **–*n*** for the *n* most recent fills. By using this option, you don’t have to handle scrolling lists or to organize the fills, because your spreadsheet always displays the ten most recent fills.
  * **“first\**n*“** or ***n*** for the first *n* fills.
  * **“*n*:*m*“** for the range of fills between *n* and *m*, inclusively.
* *fillset-id* is an optional order set ID returned from the [TTFills formula](#os) to filter the fills. If you omit this parameter, you must account for it in the formula with a comma. Also, if you omit this parameter, the formula will return all fills.
* *cell-address* is the address of the internal, temporary spreadsheet that contains the array of values specified by the *fills-columns* parameter

For example, the following RTD formula retrieves values of seven columns for the ten most recent fills for the orders defined by the fill set referenced in cell B3. It returns the values in a 7×10 array starting in cell E1.

> ```
> =RTD("tt.rtd",,"TTFills","Time,Exch,Contract,Price,FillQty,Fill Type,Account","last*10",B3,CELL("Address", E1))
> ```

## Retrieving fill statistics

You can use RTD to track changes in statistics related to fills in a fill set, such as the net position for matching fills.

The RTD formula for retrieving order information uses the following format:

> ```
> =RTD("tt.rtd",,"FillStats",fillset-id,fillstat-column,cell-address)
> ```

where:

* *fillset-id* is an optional order set ID returned from the [TTFills formula](#os) to filter the fills. If you omit this parameter, you must account for it in the formula with a comma. Also, if you omit this parameter, the formula will return all fills.
* *fillstat-column* is one of the following [Fills](../../../order-management/fills/reference-fills/fills-reference.md) columns:
  * BuyFillCnt
  * SellFillCnt
  * NetFillCnt
  * BuyPos
  * SellPos
  * NetPos
  * AvgBuyPrice
  * AvgSellPrice
  * AvgOpenPrice

For example, the following RTD formula retrieves the net position of all fills within the fill set referenced in cell B3.

> ```
> =RTD("tt.rtd",, B3, "NetPos")
> ```

←[Previous PostRetrieving order properties](retrieving-order-properties.md)

[Next PostCombining multiple filters](combining-multiple-filters.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/xl-os-filter-example.png
