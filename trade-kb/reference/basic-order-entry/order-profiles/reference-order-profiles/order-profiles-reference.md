---
title: Order Profiles Reference
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/reference-order-profiles/order-profiles-reference/
---

# Order Profiles Reference

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/reference-order-profiles/order-profiles-reference/)

## About the order profile upload file

When [uploading order profiles into TT](../task-order-profiles/uploading-order-profiles-to-tt.md), the **.csv** file must adhere to the following rules:

* Files must be saved as plain text format.
* The filename must use a **.csv** file extension.
* Data fields must be comma delimited.
* Spaces after commas (for readability) are allowed.

### Sample .csv file

```
FCM_Customer,FCM_IsActive,FCM_Product,FCM_Exchange,FCM_Group,FCM_ProductType,FCM_Account,FCM_ExchAccount,FCM_OrdQty,FCM_MaxQty,FCM_TIF,Clearing Acct,Staged Orders
Customer3,TRUE,6B,CME,*,FUT,SonnAB,456,4,100,Day,JS-1,
Customer3,TRUE,GE,CME,*,FUT,SonnAB,456,5,100,GTC,JS-2,
Customer3,TRUE,ES,CME,*,FUT,SonnAB,456,1,100,GTC,JS-3,
```

### File structure

The **.csv** file can contain a maximum of 1000 profile rows, as follows:

* Row 1 contains the header column fields as follows:
  * The row must contain columns for all fields used by any of the profiles.
  * The header column fields should match the header names in Order Profiles, including capitalization.
  * The field columns can be arranged in any order, but the data within a column must match the value expected by the column header.
* Rows 2-*n* (up to 1003) contain the values for a single profile per row.

## Order profile columns

To show the optional MiFID II columns in Order Profiles, right-click the rules panel of the widget and select the **Edit Columns…** option.

To filter column rows, click the right hand portion of a column header. Note: the **Profile** column cannot be filtered because the rule rows are already filtered based on the profile(s) selected in the Profiles panel.

When adding a rule or profile, you can set values in the following columns:

| Column | Description |
| --- | --- |
| Account | Sets the order routing account to use for the rule. Select an account from the drop-down list. |
| Account Type | Account type code that defines the trader’s relationship with a clearing house. The list of account types varies by exchange. |
| Algo Name | Name of a user created custom algo. |
| Algo Type | Type of user created custom algo, e.g. “OTA” or “OMA” |
| Agrsv Non-Match | An on/off checkbox, but applied to the Soft Price Non-Match value. |
| Agrsv Std | An on/off checkbox that behaves the same as the Aggressive only option described [here](https://library.tradingtechnologies.com/user-setup/rl-pre-trade-price-controls.html). |
| Alt Exch Acct | Shows the value of Tag 440 sent to ICE and ICE\_L exchanges. This field allows you to define the Tag 440 value and override the “Exchange Account” value configured in Setup for ICE and ICE\_L. |
| C.D.I. | Commodity Derivative Indicator. Indication of whether the order is for hedging purposes to reduce risk. Valid values:  * None (blank) * Yes * No |
| Clearing Acct | Shows the value sent to the exchange as the clearing account. |
| Clearing Firm | The clearing firm identifier. |
| Clearing Instruction | Indicates if the Euronext wholesale trade must be posted to a specific account in the clearing system. Valid values are:  * Automatic * Automatic and account authorization * Give-up to a single firm * Manual * Manual and account authorization  . |
| Client ID | Client ID. The customer’s legal entity identifier (LEI/Short Code). |
| Client Ref | Client identifier for Euronext wholesale trades. |
| CTI | Sets the type of user who is placing orders with this account. |
 D.E.A | Direct Electronic Access. Sets whether or not the order is sent from direct/sponsored access, or from another source. Valid values:  * None (blank) * Yes * No || Disp Qty | Sets a display quantity for disclosed-quantity orders (e.g., native Iceberg) for the rule. |
| Exch | Defines an exchange. The drop-down list in this cell shows exchanges assigned to your account(s). Select “Aggregator” or “Autospreader” to define an order entry rule for Aggregator or Autospreader orders. Default exchange preference is \* (any exchanges, including any Autospreader and Aggregator orders). Populated automatically based on the product. |
| ExecDec | Execution Decision ID. Indicates the user or firm that submitted the order. Enter a registered ID/Short Code. |
| Execution Instructions | Order execution instructions for a staged order. |
| Give-Up | Identifies the Give-up account or user. |
| Give-Up Type | Indicates if the Euronext wholesale trade is given up to a member trading firm or individual trader. |
| Group | Defines the exchange product group. The drop-down list in this cell shows product groups for exchanges assigned to your account(s). Default product preference is \* (all available product groups). |
| InvestDec | Investment Decision ID. Indicates the user or firm who made the trading decision. Enter a registered ID/Short Code. |
| LiqProv | Liquidity Provision. Indication of market making. Valid values:  * None (blank) * Yes * No |
| Max Qty | Sets the maximum order quantity for the rule.   **Note**: Largest value supported is 999,999,999. |
| MGT | Member-Group-Trader ID |
| MiFID ID | MiFID II profile ID for ICE only. Required for firms who register with ICE to use a single code instead of individual MiFID order tags 9700-9706. |
| O/C | Optional column which allows you to define default values for markets that support including **Open** and **Close** flags when submitting orders. |
| Offset Acct | Default account used for submitting an offsetting manual fill for a care order. Valid values:  * “Blank” — Sets the “Offset Account” field in the Order Ticket to the same account used for staging the order. * None — Sets “Offset Account” to “None”. * *<Account>* — List of accounts available to the user. The account selected appears in the “Offset Account” field. |
| Order Qty | Sets the order quantity for the rule. **Note**: As of version 15.11.4, the default order quantity was changed from 1 to 0 for all new rules. However, it did not changes the default quantity for existing rules; you must update existing rules if you want to set 0 for the default order quantity. |
| Order Ref | Trader or order reference identifier for Euronext wholesale trades. |
| Order Type | Sets the order type for the rule. Native order types vary by exchange. All TT order types are listed, as well as ADL algos and third party algos. |
| Prod | Defines a product. The Market Explorer opens in this cell to allow you to find and select a product. Multiple products can be selected using Ctrl+click or Ctrl+Shift+click. Default product preference is \* (all products). **Note**: The Exch and Type fields will be populated automatically based on the product selected. |
| Profile | Order profile name. |
| SL Payup | Sets the Stop-Limit order payup ticks quantity for the rule. |
| Soft Price Non-Match | Same as [Price reasonability](https://library.tradingtechnologies.com/user-setup/rl-pre-trade-price-controls.html) during non-matching states (e.g. pre-open), the value is interpreted as Ticks or Percent by the presence or lack of a “%” character, e.g. “10” is applied as 10 ticks, “10%” is applied as 10 percent. |
| Soft Price Std | Same as Price reasonability described [here](https://library.tradingtechnologies.com/user-setup/rl-pre-trade-price-controls.html). The value is interpreted as Ticks or Percent by the presence or lack of a “%” character, e.g. “10” is applied as 10 ticks, “10%” is applied as 10 percent. |
| Soft Qty | Same as Max Order Qty |
| Staged Order | Indicates whether the order is a staged order. When this field is checked, the **Stage** checkbox on the Order Ticket is checked. |
| Take-Up | Identifies who the Give-up order is allocated to. |
| Template | Sets a TT order type template to the order. |
| Text A | Free text field that can be [routed to the exchange](../../order-ticket/reference-order-ticket/order-ticket-reference.md). |
| Text B | Free text field that can be [routed to the exchange](../../order-ticket/reference-order-ticket/order-ticket-reference.md). |
| Text C | Free text field that is not routed to the exchange, but remains on the order in the TT system. |
| Text TT | Free text field that is not routed to the exchange, but remains on the order in the TT system. |
| TIF | Sets a time-in force (TIF) order restriction for the rule to apply to each order. Select a TIF from the drop-down list:  * DAY — Day orders (e.g., GTD) * GTC — Good Til Cancel * FOK — Fill Or Kill * IOC — Immediate Or Cancel   The default TIF is Day. |
| TrdgCap | Trading Capacity. Valid values:  * None (blank) * Deal — Indication of dealing on own account * Match — Indication of trading in a matched principal trading capacity * Other — Indication of trading in any other trading capacity * Wholesale — Indication of trading in a Wholesale Capacity * Employee — Indication of trading with a prescribed person |
| Type | Defines a product type. Populated automatically based on the product. If you select an exchange, only product types supported by that exchange are listed. The list of product types includes the following:  * FUT — Futures * SPRD — Spreads * OPT — Options * STRA — Strategies * CS — Common Stock * INDEX — Indexes * SPOT — Spot markets * TBOND — Treasury Bonds   Default product type is \* (all product types). |
| Use | Sets whether to use a rule for submitting orders. Check the **Use** column to make the rule available for order entry. If multiple rules are selected, rules will be selected based on the best match, where the more specific values override wildcard “\*” values. |
| User | The User ID to apply the rule to. |

