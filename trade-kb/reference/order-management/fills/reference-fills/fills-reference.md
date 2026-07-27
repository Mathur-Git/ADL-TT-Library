---
title: Fills Reference
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/fills/reference-fills/fills-reference/
---

# Fills Reference

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/fills/reference-fills/fills-reference/)

## Context menu items

Right-click in the widget to open the context menu and select the following items:

* **Request download**: Sends a request for spreadsheet containing a range of fills.
* **Set as default alert view**: Saves the current view style as the default style.
* **Export Rows as…**: Exports data to a **.csv** or **.xlsx** file for the rows you select in the
  Fills widget. Use Shift-click to select multiple rows.
* **Print**: Prints fills based on the filtered content of the widget.
* **Clear all filters**: Turns off all filters you may have set for each column.
* **Go to date:** Displays historical fill data. Click [here](#date) for more details.
* **Zoom**: [Zooms](../../../overview/widgets/task-widgets/zooming-the-view-in-or-out.md) the view of the selected
  widget.
* **Fills settings**: Allows you to customize settings for the widget.

## Available settings

These settings affect only the selected Fills widget. To update the default settings with these values for
newly-opened Fills widgets, or to apply them to existing opened widgets, click **Defaults**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fls-settings.png)

#### General

| Setting | Description |
| --- | --- |
| Include trade capture reports | Displays trade capture report messages in addition to fills in the Fills widget screen. When this option is checked (enabled), trade capture report messages are also displayed in the Fills widget. This option is unchecked (disabled) by default and trade capture reports are not displayed. This setting must be enabled to receive OTC trades executed through Blocktrader to see their fills in the Fills widget and in the Fills panel of the Order and Fills widget. |

#### Display

| Setting | Description |
| --- | --- |
| Colors | Allows you to [customize or change the cell and column colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md#colors) available in the widget. There are separate settings for text and background colors. |
| Bold font | Sets the use of bold font for text. |
| Italic font for fills | Sets italic font on all fill rows. |
| Row numbers | Displays the row numbers column. |
| Ignore global Account List broadcasts | Configures the widget to ignore account selections made in an Account List. When checked (enabled), the widget ignores account selections broadcast by an Account List widget. |
| Show tabs | Displays the tab bar at the bottom of the widget. |
| Highlight new fills (seconds) | Highlights new fill rows. The highlight color displays for the set number of seconds. Setting the value to zero (0) seconds retains the highlight color until you select the right-click menu option **Mark all as seen**.    **Note:** Only new fills that come in after enabling the setting will be highlighted. Highlighted fills would go unhighlighted once they reach the end of the highliight time window. |
| Launch floating order entry on left click on price or quantity | Enables the floating order entry preference to be launched when clicking on price and quantity cells in the grid. |
| Include headers when copying or exporting rows | Configures the widget to include the headers when copying selected fills and pasting them into another application or exporting them to a .csv or .xlsx file. |

#### Fills column descriptions

| Setting | Description |
| --- | --- |
| Account | Account number associated with the transaction. |
| AcctType | Account type code that defines the trader’s relationship with a clearing house |
| AltExchAcct | Shows the value of Tag 440 sent to ICE and ICE\_L exchanges. |
 BBG | Displays the Bloomberg product symbol when this symbology is enabled in the workspace preferences. When the exchange’s symbology is enabled, this column is blank. **Note:** Bloomberg codes are for display only and are not included in downloads from the Fills widget. Filtering of historical data does not work on the BBG column. || Broker | The broker ID that is associated with the order. |
| B/S | Whether the transaction represents a Buy or Sell order |
| C.D.I. | Commodity Derivative Indicator. Indication of whether the order is for hedging purposes to reduce risk. |
| ClearingAcct | Shows the value sent to the exchange as the clearing account. |
| Client | Client. Identification of the customer (Short Code). |
| ClientSecondadry | Secondary customer identifier associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter the customer’s legal entity identifier (LEI/Short Code). |
| ClOrderID | Unique identifier for the order assigned by the client and sent to the exchange. |
| Compliance Text | Text field available to include additional values for compliance. |
| Confirmed | Contains the **Confirm** button used for confirming fills.  **Note**: Risk Administrator must enable permissions for you to confirm fills in the account. Users with view-only account permissions cannot confirm fills. See [User Account Permissions](https://library.tradingtechnologies.com/setup/company-administration/users/description-users/user-account-permissions/). If this option is not enabled, the **Confirm** button remains hidden. |
| ConnectionID | ID of the connection used to route the order or fill. |
| Contract | The name and contract expiry for the instrument or strategy. |
| Counterparty | Shows the Participant ID and account number of the counterparty that you submit the order on behalf of. |
| CurrentUser | TT user name of the trader associated with the transaction or owns a staged order. |
| CustOrderHandlingInstr | The “Customer Order Handling Instruction” value set on the account in Setup and sent to the exchange in Tag 1031, which identifies the execution method and source of derivatives trades. |
| Date | Date the transaction occurred or the message was sent.   * Order Book: Date the order was submitted. * Fills: Date the fill was received. * Audit Trail: Date the message was sent or received. * Blocktrader: The date that the block trade was submitted on TT. |
| D.E.A. | Direct Electronic Access. Shows whether or not the order is sent from direct/sponsored access, or from another source. |
| EchoDC\_1 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_2 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_3 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_4 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_5 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_6 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_7 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_8 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_9 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_10 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| End | Shows the end date and time parameter setting for TT Order Types or ADL algos. |
| ExecDec | Execution Decision ID. Indicates the user or firm that submitted the order. Enter a registered ID/Short Code. |
|
| ExecDecQ | Execution Decision Qualifier. The Order Tag Default qualifier for the ExecDec field as part of MiFID compliance. |
| ExecDecSecondary | Secondary user or firm associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter a registered ID/Short Code. |
| Exchange | Name of the exchange. **Note:** For parent TT order type orders, an asterisk “\*” is appended to the exchange name in this column (e.g., CME \*) to indicate the intended destination of the submitted parent order. No asterisk appears in the **Exch** column for the related child orders sent to the exchange. |
| ExchOrderID | ID of the order, supplied by the exchange. |
| ExchTransID | The transaction ID generated by and received from the Exchange. |
| ExchDate | The date the trading host received/sent the message. The date is displayed based on the timezone of the user’s workstation. |
| ExchTime | The time at which a fill is received by the exchange host or exchange gateway, depending on the practice of the exchange. The time is displayed based on the timezone of the user’s workstation. |
| ExecDec | Execution Decision. A Short Code as an indication of who or what algo submitted the order. |
| ExecDecQ | Execution Decision Qualifier. The Order Tag Default qualifier for the ExecDec field as part of MiFID compliance. |
| ExeNotional | The executed notional value of the order as it partially fills (e.g., submit an order for 1 CL contract: 1 contract traded \* $50/barrel \* 1,000 barrels/contract = executed notional value). |
| FillQty | The quantity filled in the order. |
| FillType | Indicates whether fill corresponds to an outright, a spread, a spread leg, or a synthetic fill. |
| Fixing Date | Allows users to query/filter by Fixing Date.  **Note:** This value will only be populated for FX Spot instruments. |
| GiveUp | Account of the give-up party |
| InvestDec | Investment Decision. A Short Code as an indication of who made the trading decision. |
| InvestDecQ | Investment Decision Qualifier. The Order Tag Default qualifier for the InvestDec field as part of MiFID compliance. |
| IΔ | The delta calculated with the auto-fit volatility curve values provided by TT. |
| IV | Implied volatility value. Implied volatilities are calculated using the midpoint of bid and ask prices. |
| LiqProv | Liquidity Provision. Indication of market making. |
| ManualFill | Whether the fill is a result of a:  * (blank): Normal fill * **Manual**: Manual fill * **Transfer**: AOTC position transfer fill |
| Modifier | The modifier applied to the order.  Example: Stop, If Touched, Trailing Stop, Trailing IT, Trailing Limit, Machine Gun |
| O/C | Type of position you are establishing with the order. |
| OrderQty | In “By Order” or “By Order (Summary)” mode, displays the sum of the filled quantity plus the remaining working quantity of the order. This column is hidden by default. |
|
| OrderQty | In “By Order” or “By Order (Summary)” mode, displays the sum of the filled quantity plus the remaining working quantity of the order. This column is hidden by default. |
| Organization | The value of the “Organization” custom field included on the order or configured for the user in Setup. Typically used for identifying traders that are managed by your firm but are not direct employees. |
 Originator | TT User ID of the person who submitted the order or staged order. || P/A | Whether a Brokertec order is passive (PA) or agressive (AA). |
| P/F | Fill indicator: P = partial fill, F = full fill. **Note:** Not all exchanges provide partial fill indicators. |
| ParentID | TT-generated ID that uniquely identifies a parent order. The ID is also associated with all of its child orders.  For example, if you submit a TT Iceberg order, the ParentID of each child order will contain the TTOrderID of the parent Iceberg order. |
| P/C | Indicates whether an options contract is a Put (P) or a Call (C). |
| Price | Price of the order or fill. |
| ProdType | Type of product (e.g. Futures, Options). |
| Product | Name of the product being traded. |
| ProfileName | Displays the applied order profile for the order or fill.  Only profiles that were configured in Setup will populate in this column. Locally created profiles will not appear.  **Note:** The “ProfileName” column in the Order Book displays the order profile ID (e.g., <109>) when the profile name is not available to the user. In Setup, Profile IDs for your company are listed in the data grid “ID” column on the **More** | **Profiles** tab. The column is hidden by default and can be shown using the “Grid Options”. |
| RiskGroup | Shows the name of the risk group. |
| Route | Indicates whether the fill was received from the exchange (Direct) or generated by internal matching due to position transfer (Indirect). |
| Source | Displays the name of the widget or application that originally placed an order. For child orders, this column displays the origin of the child order itself and not the parent. |
| Settle Date | The official settlement date for FX products. For some exchanges this value may differ from the **Trade Date** depending on the trading session which the contract settles. |
| Staged | Shows “Staged” to identify parent staged orders and fills. This column is blank on other orders and fills. |
| StagedOrderID | Shows the staged order identifier on the parent care order and all related child orders and fills. |
| Strike | Displays the strike price of the options contract. |
| TextA | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextA** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextB | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextB** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextC | Displays a read-only, customer-defined text value set by FIX client applications. The value is not sent to the exchange. |
| TextTT | Displays an optional, user-defined text value from the Setup app or entered in the **TextTT** free-form text field in the Order Ticket. The value displayed in this column remains on submitted orders for tracking purposes in the TT system, but is not routed to the exchange.  You can show or hide the Text TT text box for a selected working order in the Order Toolbar. You can add or modify the text that displays in the **TextTT** column for the selected order.  In the **Position Manager** widget, you can now edit the **TextTT** column for **Local Fills** and **Admin Fills**. However, this is not available for **Admin SODs**.  **Note:** For Autospreader orders submitted by an ADL algo, the value is populated with the order tag of the parent algo order. |
| Time | The time the order action occurred. This value is updated after each order action.   * Order Book: Time the order was submitted or modified. * Fills: Time the fill or partial fill was received. * Audit Trail: Time the message was sent or received. |
| Total Vega | The total amount of Vega filled per trade. **Note:** Does not display in Summary Mode. |
| TrdgCap | Trading Capacity. Indication of a user dealing on own account, trading in a matched principal trading capacity, or trading in any other trading capacity. |
| TotNotional | The total notional value of the order (e.g., submit an order for 1 CL contract: 1 contract traded \* $50/barrel \* 1,000 barrels/contract = total notional value). |
| Trade Date | The official trade date for FX products. For some exchanges, this value may differ from the **Settlement Date** depending on the trading session which the contract settles. |
| TTOrderID | TT-generated ID that uniquely identifies the order associated with the transaction. |
| TT SMP ID | Displays the value of the TT Self Match Prevention ID used to conduct a match within the TT Platform.  **Note:** This differs from the exchange self match prevention ID provided in the **SMP ID** field.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| TT SMP Instruction | Instruction provided to the TT platform as to whether to cancel the resting or incoming (aggressing) order in the event of a self-match.  **Note:** This field only applies to the TT Platform Self-Match Prevention (TT SMP) functionality. It does not contain information related to exchange-provided self-match prevention.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| Type | The type of instrument or options strategy. |
| Und Px | The price of the underlying instrument at the time of the fill. |
| UniqueExecID | TT-generated execution ID for fills. Sent in the form of a short-form GUID, no more than 22-characters in length. |
| TTOrderID | TT-generated ID that uniquely identifies the order associated with the transaction. |
| TT SMP ID | Displays the value of the TT Self Match Prevention ID used to conduct a match within the TT Platform.  **Note:** This differs from the exchange self match prevention ID provided in the **SMP ID** field.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| TT SMP Instruction | Instruction provided to the TT platform as to whether to cancel the resting or incoming (aggressing) order in the event of a self-match.  **Note:** This field only applies to the TT Platform Self-Match Prevention (TT SMP) functionality. It does not contain information related to exchange-provided self-match prevention.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| Type | The type of instrument or options strategy. |
| Und Px | The price of the underlying instrument at the time of the fill. |
| UniqueExecID | TT-generated execution ID for fills. Sent in the form of a short-form GUID, no more than 22-characters in length. |

### Filtering columns

If a column is filterable, a drop-down arrow appears when you hover on the column header.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter1-4.png)

To filter the column, click the arrow to select one or more values and click **OK**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter2-4.png)

When a column is filtered, the column header is highlighted and the filter icon is displayed. To clear a filter,
click the icon and select **Clear Filter**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter3-4.png)

When filtering the **Product** column, you have the option to use Search or Market Explorer to select products.
The product type is displayed in parentheses next to each product in the list.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter4-4.png)

When filtering the **Date** or **Time** column, you can specify a date or date range and a time or
time range. The changes you make set the filtering criteria for both columns. You can use the following modifiers
for more precise filtering:

* **Approx**: Filters based on a single date and for a number of minutes around a specified time.
* **Before**: Filters based on a single date before a specified time.
* **After**: Filters based on a single date after a specified time.
* **Between**: Filters based on a range from a specific date and time to a specific date and time.
* **Yesterday**: Sets the date to the previous day.
* **Today**: Sets the date to the current day.
* **Anytime**: Removes the time window limitation set by Approximate Time.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter5-4.png)

[Next PostFill and Audit Trail Service](fill-and-audit-trail-service.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/fls-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter1-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter2-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter3-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter4-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/filter5-4.png
