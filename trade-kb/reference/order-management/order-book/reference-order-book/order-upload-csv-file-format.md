---
title: Order upload .csv file format
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/order-book/reference-order-book/order-upload-csv-file-format/
---

# Order upload .csv file format

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/order-book/reference-order-book/order-upload-csv-file-format/)

## About the order upload file

When [uploading orders into TT](../task-order-book/uploading-orders-to-tt.md), the **.csv** file must adhere to the following rules:

* Files must be saved as plain text format.
* The filename must use a **.csv** file extension.
* Data fields must be comma delimited.
* Spaces after commas (for readability) are allowed.
* You can upload orders from a .csv file using Bloomberg codes by including a “BBG” column in the file.

### Sample .csv files

  

#### Native Order Types

**Plain Text Format**

```
  B/S, OrdQty, Exch, Contract, Price, TIF, Type, TrigPrc, DispQty, Account, TriggerPriceType
  B, 10, CME, ESZ4, 2782.75, Day, Limit, , , 12345,
  S, 25, CME, ZBZ4, 141'24, GTC, Stop Limit, 142'16, , 12345,
  B, 100, CME, ESZ4, 2780.00, Day, Iceberg, , 3, 12345,
```

  
**Spreadsheet Format**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-native-order-types-csv.png)

  

#### TT Iceberg

**Plain Text Format**

```
  B/S, OrdQty, Exch, Contract, Price, Account, TIF, Type, End, DiscVal, Variance, TriggerType, TrigPrc, TriggerPriceType
  B, 10, CME, ESZ4, 5600, Acct_123, Day, TT Iceberg, Day, 1, , , ,
  B, 20, CME, ESZ4, 5601, Acct_123, Day, TT Iceberg, Day, 2, 50, , ,
  B, 50, CME, ESZ4, 5602, Acct_123, Day, TT Iceberg, Day, 10, , Stop, 5900, LTP
```

  
**Spreadsheet Format**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-tt-iceberg-csv.png)

  

#### TT Time Sliced

**Plain Text Format**

```
  B/S, OrdQty, Exch, Contract, Price, Account, TIF, Type, ChildOrderType, End, EndTime, DiscVal, Interval, LeftoverAction
  B, 10, CME, ESZ4, 5800.00, Acct_A, Day, TT Time Sliced, Limit, Day, , 1, 100000, Leave
  B, 10, CME, ESZ4, 5800.00, Acct_A, Day, TT Time Sliced, Limit, GTC, , 1, 40123, Leave
  B, 10, CME, ESZ4, 5800.00, Acct_A, Day, TT Time Sliced, Limit, Time, 14:00, 1, 59999, Leave
  B, 10, CME, ESZ4, 5800.00, Acct_A, Day, TT Time Sliced, Limit, Time, 14:30:00, 1, 59999, Leave
  B, 10, CME, ESZ4, 5800.00, Acct_A, Day, TT Time Sliced, Limit, Time, 28Dec24 14:35:00, 1, 59999, Leave
```

  
**Spreadsheet Format**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-tt-time-sliced-csv.png)

  

### File structure

The **.csv** file can contain a maximum of 1000 order rows, as follows:

* Row 1 must be the header fields, as follows:
  * The row must contain columns for all fields used by any of the orders.
  * The header column names must exactly match the field names, including capitalization.
  * The field columns can be arranged in any order, but the data within a column must match the value expected by the column header.
  * It must contain a field named “Type” which defines the order type for each row because the upload logic uses the order type to look up what parameters are available for the order type for each row. It is also a key piece of data and determines what parameters are available for that row, we do NOT allow the user to change the order type from the preview screen using the drop down menu.
    1i>
  * “ChildTIF” or ‘TIF-Child” field is not supported.
  * The Time-In-Force (TIF) for non-algo orders is the value normally visible in the main TIF control on the Order Ticket.
  * The Time-In-Force (TIF) for algo orders has two components:
    * the TIF for the algo child orders is the value normally visible in the main TIF control on the Order Ticket.
    * the TIF for the parent algo order is the value set in the “End” dropdown in the algo parameter flyout.
  * When an algo order is desired to complete at some other value than Day or GTC, the “End” field in the csv file should be set to “Time”, and an additional column named “EndTime” should define the desired date/time of the order. This string value can be a time in HH:MM format (e.g. 14:00), HH:MM:SS format (e.g. 14:05:30), or a full date and time string (e.g. 13Nov24 14:29:55).
  * To define the disclosed quantity of each slice of slicing order type (native Iceberg, as well as algos including TT Iceberg, TT Time Sliced and TT Time Duration):
    * use “DispQty” for native Iceberg orders
    * use “DiscVal” (and an optional “DiscValType” which can be Qty or Pct) for algo orders (including TT Iceberg, TT Time Sliced and TT Time Duration)
* Rows 2-*n* (up to 1001) contain the values for a single order per row.

**Note:** If the file contains both a TT instrumentID and a BBG code, then the instrumentID takes priority and ignores the BBG code.

## Supported field names for all orders

All uploaded orders can use the following fields.

| Field name | Required? | Description |
| --- | --- | --- |
| Account | Required | Account number associated with the transaction. |
| AcctType | Optional | Account type code that defines the trader’s relationship with a clearing house (e.g. A1, P1, etc.). |
| B/S | Required | Whether the transaction represents a Buy or Sell order |
| BBG | Optional | Bloomberg product symbol **Note:** Bloomberg symbology must be enabled for your company by TT.  **Note:** You must include the full Bloomberg code, including the “Comdty” string in the cell: e.g., “USU4 Comdty” as the BBG code for ZB Sep24. |
| C.D.I. | Optional | (MiFID) Commodity Derivative Indicator. Indication of whether the order is for hedging purposes to reduce risk. |
| ClearingAcct | Optional | Exchange Clearing Account. Account ID assigned the user by the exchange. |
| Client | Optional | (MiFID) Client. Identification of the customer (Short Code). |
| Compliance Text | Optional | Text field available to include additional values for compliance. |
| Contract | Required | The name and contract expiry for the instrument or strategy.   The contract name must use the short-form name, such as ESZ8.  **Note**: Optional if InstrumentID is present. |
| D.E.A. | Optional | (MiFID) Direct Electronic Access. Shows whether or not the order is sent from direct/sponsored access, or from another source. |
| DispQty | Optional | Amount of the total order quantity to disclose |
| Exch | Required | Name of the exchange.  **Note**: Optional if InstrumentID is present. |
| ExecDec | Optional | (MiFID) Execution Decision. A Short Code as an indication of who or what algo submitted the order. |
| ExecDecQ | Optional | (MiFID) Execution Decision. A Short Code as an indication of who or what algo submitted the order. |
| GiveUp | Optional | Give-up party identifier. |
| InstrumentID | Optional | Unique TT instrument identifier  If specified, the ID must be enclosed in single quotes (‘). Also, if the InstrumentID is specified, TT will use this value instead of the Exch and Contract fields to identify the instrument. Valid when the **Type** column contains “Limit”, “TT Iceberg”, “TT Timed”, “TT Time Sliced”, and “TT Time Duration”. **Note**: Required for Autospreader orders |
| InvestDec | Optional | (MiFID) Investment Decision. A Short Code as an indication of who made the trading decision. |
| InvestDecQ | Optional | (MiFID) Investment Decision Qualifier. The Order Tag Default qualifier for the InvestDec field as part of MiFID compliance. |
| LiqProv | Optional | (MiFID) Liquidity Provision. Indication of market making. |
| O/C | Optional | Type of position (open or close) you are establishing with the order. |
| OrdQty | Required | Total order quantity |
| Price | Required | Price of the order or fill. |
| Profile | Optional | Customer profile. |
| StageMsg | Optional | Additional execution instructions to include with staged order. |
| TextA | Optional | User-defined text string. |
| TextB | Optional | User-defined text string. |
| TextTT | Optional | User-defined text string. |
| TIF | Required | Time In Force for the order. For TT Order Types (TT Stop, TT Iceberg, etc.), the TIF must always be set to GTC. |
| TrdgCap | Optional | Trading Capacity. Indication of a user dealing on own account, trading in a matched principal trading capacity, or trading in any other trading capacity. |
| TrigPrc | Optional | Trigger price.  **Note**: Required for Stop orders |
| Type | Required | Type of order associated with this transaction (e.g. Limit, Market, etc.). |

## Supported field names to TT Order Types

In addition to the standard order fields, you can use all parameters when uploading orders for TT Order Types and TT Premium Order Types. For more information about the parameters you can use for the various TT Order Types, please see below.

Also refer to the [TT Order Types Overview](../../../basic-order-entry/tt-order-types/description-tt-order-types/tt-order-types-overview.md) and [TT Premium Order Types](../../../basic-order-entry/tt-premium-order-types/description-tt-premium-order-types/tt-premium-order-types-overview.md) help topic pages.

| **Field Name** | **Required By** | **Description** |
| --- | --- | --- |
| BracketOrderType | TT Bracket | Order type for the parent order |
| BracketSLOffset | TT Bracket | Number of ticks away from the Stop price to submit a Limit order |
| ChildOrderType | TT Stop  TT Time Sliced TT Time Duration TT Volume Duration | Order type sent when child order is triggered:  * Limit * Market |
| DiscVal | TT Iceberg  TT Time Sliced  TT Time Duration | Amount of the total order quantity to disclose |



**Note**: This can be used together with an optional field **DiscValType**.


| DiscValType | TT Iceberg  TT Time Sliced  TT Time Duration | Type of the total order quantity to disclose. It can be Qty (quantity) or Pct (percentage). |
| DispQty | TT Iceberg TT Time Sliced TT Time Duration | Amount of the total order quantity to disclose; includes the type of value (e.g. 100, 25%) |

**Note**: .csv file with **DispQty** field would still work, and it would require users manually mapping this field to **DiscVal** in the order upload preview grid. We therefore recommend users using the **DiscVal**field.


| Duration | TT Time Duration | The total length of time to submit each order slice. |
| DurationBaseUnit | TT Time Duration | Unit of time. Provide this value when **Duration** is populated. Valid values:  * **min** — Length of time in minutes. * **hr** — Length of time in hours. |
| DurationStartTime | TT Time Duration | When to start submitting orders. Enter a time in *hh:mm:ss* format. |
| DurationEndTime | TT Time Duration | When to stop submitting orders. Enter a time in *hh:mm:ss* format. |
| EndTime |  | Time to stop working the order (HH:MM:SS in the exchange timezone).  The EndTime field can include just a time by itself (HH:MM:SS) or can optionally include a date with the time (YYYY-MM-DD HH:MM:SS).  Instead of a date/time string, the “EndTime” field can also be set as “Day” or GTC”. If one of these restrictions is used, the order “TIF” field can be left blank and the parent order will use the setting in the “EndTime” field.  Note: If you omit a time, the order will work until the market closes (GTC). |
|
 EndTimeAction |  | Action to take for any unfilled balance when the End time is reached. Do not provide a value unless **EndTime** is also populated. Supported values:  * **Cancel** — Cancels all child orders and stops the order type. * **Market** — Cancels the resting Limit order and submits a Market order. If provided, a “MktLmtTicks” value can also be populated. || ExcludeImplieds |  | Whether or not to consider implieds when evaluating a price trigger  * Yes * No |
| Interval | TT Time Sliced | Length of each slice, in milliseconds |
| LeftoverAction | TT Time Sliced | How to handle any existing unfilled order quantities when it is time to send the next portion  * Payup * Leave |
| LeftoverTicks |  | Number of ticks to add (positive integer) or subtract (negative integer) from your Bid or Offer to determine the price of the limit order  **Note**: Required for TT Time Sliced orders if **LeftoverAction** is **Payup**. |
| LimitPrcType | TT Trailing Limit | Type of price to us as the base price to calculate a Payup price  * Bid * Ask * LTP * Trigger * Same Side * Opposite Side    **Note**: Also required for TT Bracket, TT OCO and TT Stop orders when StopOrderType = Limit. |
| LimitTicksAway | TT Trailing Limit  TT Timed | Number of ticks away from the specified limit price to submit the order (-999 to 999) |
| MktLmtTicks |  | Sets the number of ticks from LTP to submit a Limit order through the opposite inside market. Enter a positive integer from 0 – 100. This field can be populated when **EndTimeAction** is set to “Market”. |
| OcoStopTriggerPrice | TT OCO | Price at which to trigger the Stop Market or Stop Limit order |
| ProfitTarget | TT Bracket | Initial price for the profit order in the OCO pair:  * Price = Entry Order Fill Price + Profit target setting, if the TT Bracket order was a bid * Price = Entry Order Fill Price – Profit target setting, if the TT Bracket order was an offer |
| PayupTicks |  | Number of ticks away from the Stop price to submit a Limit order when a Stop Limit order is triggered; cannot be populated when the main “Price” field is also populated  **Note**: Also required for TT Bracket, TT OCO and TT Stop orders when StopOrderType = Limit. |
| ResetTrigger | TT Stop | Whether to reset the trade quantity counter back to zero, if the inside market backs away from the trigger price |
| RetryCount | TT Retry | Number of times to send a rejected order (0-32,000) |
| RetryInterval | TT Retry | Number of milliseconds between retry attempts (0-100,000) |
| StartTime |  | Time to start working the order. Enter a time (HH:MM:SS in the exchange timezone) or one of the following market states:  * Now * Pre-Open * Open   The StartTime field can include just a time by itself (HH:MM:SS) or can optionally include a date with the time (YYYY-MM-DD HH:MM:SS). |
| StopOrderType | TT Bracket  TT OCO  TT Stop | Order type sent when stop order is triggered  * Limit * Market |
| StopTarget | TT Bracket | Initial price for the stop loss order in the OCO pair:  * Price = Entry Order Fill Price + Stop loss setting, if the TT Bracket order was a bid * Price = Entry Order Fill Price – Stop loss setting, if the TT Bracket order was an offer |
| Trailing |  | Whether the trigger price trails the trigger price type by some number of ticks  * Yes * No |
| TriggerPriceType | TT If Touched  TT Stop | Type of price to trigger the order  * Bid * Ask * LTP * Trigger * Same Side * Opposite Side |
| TriggerQty | TT Stop | Quantity of the secondary trigger condition based on the executed quantity (if LTP) or the quantity on the Bid or the Ask. You can includes a comparison operator and the type of value, such as  **, **>=15%**.** |
| TriggerTicksAway |  | Number of ticks away from the specified price to submit the child order |
| TriggerType |  | How to handle the trigger price  * Stop * If Touched |
| Type | All | Name of the TT Order Type. Possible values (with capitalization and spaces) include:  * TT Bracket * TT Iceberg * TT If Touched * TT OCO * TT Retry * TT Stop * TT Time Sliced * TT Time Duration * TT Timed * TT Trailing Limit * TT With A Tick |
| Variance | TT Iceberg  TT Volume Sliced TT Volume Duration TT Time Sliced TT Time Duration | The percentage (0-100) by which to vary the child order quantity. For example, a variance of “50” allows each child order to have a random quantity within 50% above or below the disclosed quantity. |
| WATQty | TT With A Tick | WAT threshold quantity; if populated infers that WAT is applied to the child order; includes the type of value (actual or percent), such as 50, 50% |

←[Previous PostOrder Book Reference](order-book-reference.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-native-order-types-csv.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-tt-iceberg-csv.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ob-tt-time-sliced-csv.png
