---
title: CSV file format for uploading fills
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/position-manager/reference-position-manager/csv-file-format-for-uploading-fills/
---

# CSV file format for uploading fills

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/position-manager/reference-position-manager/csv-file-format-for-uploading-fills/)

When [uploading fills to TT](https://library.tradingtechnologies.com/trade/pm-uploading-fills-to-tt.html), the CSV file must adhere to the following rules:

* Files must be saved as plain text format.
* The filename must use a **.csv** file extension.
* Data fields must be comma delimited.
* Spaces after commas (for readability) are allowed.

### Sample CSV file

```
Contract,B/S,FillQty,Price,Account,User
CL Mar20,B,2,57.94,AB Parent,Joe Trader
CL Mar20,B,2,57.94,AB Parent,Joe Trader
CL Mar20,B,2,57.39,AB Parent,Joe Trader
CL Mar20,B,10,57.39,AB Parent,Joe Trader
CL Mar20,S,5,57.37,AB Parent,Joe Trader
CL Mar20,S,1,57.29,AB Parent,Joe Trader
```

### File structure

The CSV file can contain a maximum of 1000 order rows, as follows:

* Row 1 contains the header fields, as follows:
  * The row must contain columns for all fields used by any of the fills.
  * The header column names must exactly match the field names, including capitalization.
  * The field columns can be arranged in any order, but the data within a column must match the value expected by the column header.
* Rows 2-*n* (up to 1003) contain the values for a single order per row.

## Supported field names for fills

All uploaded fills can use the following fields.

| Field name | Required or Optional | Description |
| --- | --- | --- |
| Exch | Required | The exchange name. Dependent on the contract selected. |
| Account | Required | Account number associated with the transaction. |
| B/S | Required | Whether the transaction represents a Buy or Sell order |
 Contract | Required | The name and contract expiry for the instrument or strategy.   The contract name must use the short-form name, such as ESZ8.  **Note**: Optional if InstrumentID is present. || OrdQty | Required | Total order quantity |
| Price | Required | Price of the order or fill. |
| TextTT | Optional | Displays an optional, user-defined text value from the Setup app or entered in the **TextTT** free-form text field in the Order Ticket. The value displayed in this column remains on submitted orders for tracking purposes in the TT system, but is not routed to the exchange.  You can show or hide the Text TT text box for a selected working order in the Order Toolbar. You can add or modify the text that displays in the **TextTT** column for the selected order.  In the **Position Manager** widget, you can now edit the **TextTT** column for **Local Fills** and **Admin Fills**. However, this is not available for **Admin SODs**.  **Note**: For Autospreader orders submitted by an ADL algo, the value is populated with the order tag of the parent algo order. |

←[Previous PostPosition Management Transition Guide](position-management-transition-guide.md)

