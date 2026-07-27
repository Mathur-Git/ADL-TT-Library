---
title: Excel RTD properties
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/excel-rtd-properties/
---

# Excel RTD properties

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/reference/excel-rtd-properties/)

The RTD server can retrieve the following fields from TT:

* [Market data and instrument](#market)
* [Order Book](#orders)
* [Fills](#fills)
* [Positions](#positions)
* [Options](#options)

Two types of properties can be retrieved:

* [Type 1 properties](#type1) return single values with no filtering support.
* [Type 2 properties](#type2) also return single values but allow you apply filters for the results.



## Market Data and Instrument Fields

**Note:** TT RTD Server supports the following type 1 properties. If you specify the name of the
property in the formula, you must enclose it in quotes.

| Property | Description |
| --- | --- |
| Ask / Ask# | The best market ask price in TT display format / points |
| AskCnt | Number of orders that make up the AskQty. |
| AskMktDepth | Total quantity of resting Sell Market orders |
| AskMktQty | The total quantity of resting Sell Market orders |
| AskQty | The total quantity at the best ask |
| Bid / Bid# | The best market bid price in TT display format / points |
| BidCnt | Number of orders that make up the BidQty |
| BidMktDepth | Total quantity of resting Buy Market orders |
| BidMktQty | The total quantity of resting Buy Market orders |
| BidQty | The total quantity at the best bid |
| Change / Change# | The net change in the contract price for the trading session in TT display format / points |
| Close / Close# | The closing price for the session in TT display format / points |
| Contract | The name of the contract as it appears in the Trade application |
| CTQ | The cumulative traded quantity that occurred at the last price since its value changed |
| Currency | ISO currency code associated with the instrument |
| CurrencyId | The ID of the currency code |
| DAsk / DAsk# | The best direct ask price in TT display format / points |
| DAskQty | The portion of the DAsk that is direct |
| DBid / DBid# | The best direct bid price in TT display format / points |
| DBidQty | The portion of the DBid that is direct |
| ExpirationDate | Instrument expiration date in the form, MM/DD/YY. For contracts that have no expiration date, this property returns NULL. |
| High / High# | The high price for the session in TT display format / points |
| IAskQty | The portion of the AskQty that is implied |
| IBidQty | The portion of the BidQty that is implied |
| IndPrice / IndPrice# | Indicative price. Shows the indicative (open/close) price received from the exchange, as well as the equilibrium price during the Auction and Circuit Breaker states |
| ImbQty | Buy/Sell quantity imbalances during Auction states |
| IndOpen / IndOpen# | Indicative opening price indicating the settlement price for the session, as an integer |
| IndQty / IndQty# | Indicative quantity as an integer / decimal value. If provided by an exchange, the indicative or theoretical quantity is displayed during Pre-Open, Auction, and Circuit Breaker market states. |
| IndSettle / IndSettle# | The last settlement price received from the exchange in TT display format / points |
| Last& | To retrieve prices in ticks |
| Last / Last# | The last traded price in TT display format / points |
| LastQty | Quantity of the most-recent trade |
| LastSide | The side that crossed the market |
| LastTrdDate | The last day the contract can trade. This may be different from the contract expiry date (ExpDate column). |
| Low / Low# | The low price for the session in TT display format / points |
| MaturityDate | Maturity date for the specified instrument, in the form DDMmmYY |
| MinPriceIncrement | Minimum trade-able increment for the specified instrument |
| Name | The name of the instrument published by the exchange |
| Open / Open# | The opening price for the session in TT display format / points |
| PointValue | The value of one price point |
| RIC | The value of the RIC code |
| Settle / Settle# | The settlement price from the previous session in TT display format / points |
| Status / Status$ / Status& | Status of the instrument on the exchange, such as Trading, Pre-trade, etc. as a string (Status, Status$) or an integer (Status&). |
| TTDepth | Market depth (merged direct and implied) for a specified number of levels |
| TTDetailedDepth | Detailed depth (merged direct and implied) for a specified number of levels  **Note:** If a price level included implied quantities, the last array element for the price level aggregates the implied quantities and appends it with an asterisk (**\***), such as **8\***. |
| TTQ | The total traded quantity for the session |
| WrkBuys | The total quantity of working buy orders for an instrument |
| WrkSells | The total quantity of working sell orders for an instrument |

## Order Book Fields

**Note:** To retrieve working orders into RTD, the name of the RTD fields must match the following Order Book
widget or orders pane of the Order and Fills widget column names.

#### Order Book column descriptions

| Column      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|             | The Watch column. Used for selecting orders in an Order Book grouped with other widgets (e.g., Fills, Positions) and viewing the orders in those widgets. **Note:** This column is only available when the Order Book is grouped with another widget. To show/hide this column in a widget group, right-click in the Order Book pane and select **Show/Hide Watch column**. For more details, refer to [Displaying Positions for Selected Fills](http://library.tradingtechnologies.com/trade/of-displaying-positions-for-selected-fills.html). |
| Account     | Account number associated with the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| AcctType    | Account type code that defines the trader’s relationship with a clearing house                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Algo        | Shows a symbol to launch an OMA algo for an order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| AlgoName    | For TT synthetic and algorithm orders, the name of the algorithm controlling the order.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Alloc %     | The exchange-provided id for the instrument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Allocated   | Shows whether the selected fill has been allocated to a different account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AllocQty    | Shows the quantity of the total fill that was allocated in this account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| AltExchAcct | Shows the value of Tag 440 sent to ICE and ICE\_L exchanges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AskPrc      | The best market ask price.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AvgPrc      | Average fill price.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| BBG | Displays the Bloomberg product symbol when this symbology is enabled in the workspace preferences. When the exchange’s symbology is enabled, this column is blank. **Note:** Bloomberg codes are for display only and are not included in downloads from the Fills widget. Filtering of historical data does not work on the BBG column. || BidPrc | The best market bid price. |
| B/S | Whether the transaction represents a Buy or Sell order |
| Broker | The broker ID that is associated with the order. |
| Caretaker | Identifies the user group monitoring an order. If no order was passed, this column is blank. For the caretaker’s group, this column shows the group that passed the order to them. Their group name is highlighted until the order is accepted. After accepting a passed order, the Caretaker column displays the name of the current group that is managing the order. The value in this column is visible to both the group passing the order and the group accepting the order. |
| C.D.I. | Commodity Derivative Indicator. Indication of whether the order is for hedging purposes to reduce risk. |
| CXL | Cancel button for this order |
| Child Orders | Number of child orders currently working for a parent order |
| ChildTIF | Shows the time-in-force applied to the child order. |
| ClearingAcct | Shows the value sent to the exchange as the clearing account. |
| Client | Client. Identification of the customer (Short Code). |
| ClientSecondary | Secondary customer identifier associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter the customer’s legal entity identifier (LEI/Short Code). |
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
| Description | The full name of the product for each contract. |
| Dest Group | Identifies the target order passing group that you are passing the order to. When shown, this column is blank until an order is passed. |
| EchoDC\_1 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_2 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_3 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_4 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_5 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_6 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_7 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_8 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_9 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. |
| EchoDC\_10 | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records. Also displays “MTL” to indicate Market-to-Limit orders submitted on TT and natively supported on OM Gateways for HKEX, OSE, SGX and TOCOM. |
| End | Shows the end date and time parameter setting for TT Order Types or ADL algos. |
| Exch | Name of the exchange. **Note:** For parent TT order type orders, an asterisk “\*” is appended to the exchange name in this column (e.g., CME \*) to indicate the intended destination of the submitted parent order. No asterisk appears in the **Exch** column for the related child orders sent to the exchange. |
| ExchDate | The date the trading host received/sent the message. The date is displayed based on the timezone of the user’s workstation. |
| ExchOrderID | ID of the order, supplied by the exchange. |
| ExchTime | The time at which a fill is received by the exchange host or exchange gateway, depending on the practice of the exchange. The time is displayed based on the timezone of the user’s workstation. |
| ExcludeImplieds | Indicates if the price shown does not include implied prices. |
| ExecDec | Execution Decision. A Short Code as an indication of who or what algo submitted the order. |
| ExecDecQ | Execution Decision Qualifier. The Order Tag Default qualifier for the ExecDec field as part of MiFID compliance. |
| ExeNotional | The executed notional value of the order as it partially fills (e.g., submit an order for 1 CL contract: 1 contract traded \* $50/barrel \* 1,000 barrels/contract = executed notional value). |
| ExeQty | Executed quantity (sum of fills) of an order |
| Expander | Button to expand or collapse parent orders |
| FillQty | The quantity filled in the order. This column tracks and displays fill quantities for the current session and onward if you do not refresh the Trade application. Upon refresh or start up, this column only shows fill quantities for the current session. |
| Fixing Date | Allows users to query/filter by Fixing Date.  **Note:** This value will only be populated for FX Spot instruments. |
| GiveUp | Account of the give-up party |
| InstrumentID | A unique code generated by TT to identify the instrument in the TT system. |
| InvestDec | Investment Decision. A Short Code as an indication of who made the trading decision. |
| InvestDecQ | Investment Decision Qualifier. The Order Tag Default qualifier for the InvestDec field as part of MiFID compliance. |
| LimitPrcType | The type of limit price to be used for a native child order (e.g., Ask, Bid, Last Traded Price [LTP], etc.) |
| LiqProv | Liquidity Provision. Indication of market making. |
| LTP | The last traded price. |
| Message | Message received from the exchange, if sent |
| Modifier | The modifier applied to the order.  Example: Stop, If Touched, Trailing Stop, Trailing IT, Trailing Limit, Machine Gun |
| MDT | Button to launch the contract in the MD Trader widget. |
| O/C | Type of position you are establishing with the order. |
| OMAOrderID | ID that uniquely identifies the OMA (Order Management Algo) order associated with the transaction. |
| OptBid | Displays the best bid of the underlying option. |
| OptBidQty | Displays the best option bid quantity. |
| OptAsk | Displays the best ask of the underlying option. |
| OptAskQty | Displays the best option ask quantity. |
| OrdQty | Total order quantity |
| Organization | The value of the “Organization” custom field included on the order or configured for the user in Setup. Typically used for identifying traders that are managed by your firm but are not direct employees. |
| OrigDate | Date the order was originally submitted. |
| Original Group | Identifies the order passing group that initiated the order pass. When shown, this column is blank until an order is passed. |
| Originator | TT User ID of the person who submitted the order or staged order. |
| OrigTime | Time the order was originally submitted. |
| ParentID | TT-generated ID that uniquely identifies a parent order. The ID is also associated with all of its child orders.  For example, if you submit a TT Iceberg order, the ParentID of each child order will contain the TTOrderID of the parent Iceberg order. |
| Pass State | Shows the state of a passed order. Two states are possible:   * Pending Out: Indicates that you passed an order to a user group, but the order hasn’t been accepted yet. The column goes blank after you undo an order pass. * Pending In: Indicates another user group passed an order to you and is pending your acceptance. The column goes blank after you accept or reject an order pass. |
| P/C | Indicates whether an options contract is a Put (P) or a Call (C). |
| Pct from LTP | Shows the percentage that each limit order’s price is relative to the last traded price (LTP). A positive value for this specified percentage would mean away from the market and a negative value for this specified percentage would mean into the market.  **Note:** This column supports a maximum of two (2) decimal places of precision. In addition, negative values appear in parentheses. For example, **(18.45)** equals -18.45. |
| PIQ | Shows your position in queue (PIQ) for each of your orders at a given price level. The column is hidden by default. The PIQ value is displayed when you enable PIQ in your workspace preferences. |
| PayupTicks | The number of ticks that the child order was submitted away from the parent order’s price. |
| Price | Price of the order or fill. |
| Previous Group | Shows the name of the user group that previously accepted, rejected, or worked the order and passed it to another group. When shown, this column is blank until an order is passed. |
| Prod Type | Type of product (e.g. Futures, Options). |
| Product | Name of the product being traded. |
| ProfileName | Displays the applied order profile for the order or fill.  Only profiles that were configured in Setup will populate in this column. Locally created profiles will not appear.  **Note:** The “ProfileName” column in the Order Book displays the order profile ID (e.g., <109>) when the profile name is not available to the user. In Setup, Profile IDs for your company are listed in the data grid “ID” column on the **More** | **Profiles** tab. The column is hidden by default and can be shown using the “Grid Options”. |
| Release | Shows if the allocated fills were released into the TT trading system. |
| RemAlloc | Shows the amount of fills remaining to allocate. |
| Reprice Hgd Ord | To select a TT Uncovered order that has a “legged” hedge order and reprice it to the inside futures market. |
| RemQty | Shows the total remaining unfilled quantity of an order (OrdQty – ExeQty = RemQty). |
| Route | Routing destination for the order, such as TT SIM or Algo SE. |
| Source | Displays the name of the widget or application that originally placed an order. For child orders, this column displays the origin of the child order itself and not the parent. |
| Settlement Date | The official settlement date for FX products. For some exchanges this value may differ from the **Trade Date** depending on the trading session which the contract settles. |
| Staged | Shows “Staged” to identify parent staged orders and fills. This column is blank on other orders and fills. |
| StagedOrderID | Shows the staged order identifier on the parent care order and all related child orders and fills. |
| StageMsg | Text message, typically execution instructions, included with the staged order. |
| Start | Shows the start date and time parameter setting for TT Order Types or ADL algos. || Status | The current status of the exchange:   * PreTrading * Open * FastMarket * Auction * PostTrading * Closed * NonTradable * PreOpen * Freeze * Expired * OpeningAuction * ClosingAuction * Reserve * PriceDiscovery * Level * CircuitBreaker * SessionRoll * FeedDown * LateOpen * NonFinalClosed * NumStatus |
| SynthStatus | The status of the parent synthetic order. |
| Strike | Displays the strike price of the options contract. |
| Term | Shows the contract month for a strategy. If all contracts in a strategy are in the same month, that month is listed in the Term column. If not, then just the front month of the strategy is listed. |
| TextA | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextA** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextB | Displays an optional, user-defined text value from the Setup app, Order Profiles, or entered in the **TextB** free-form text field in the Order Ticket. This value remains on the order in the TT system. If accepted or required by an exchange, the value in this column [may be routed to the exchange](../../../basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference.md#fft-table) for clearing and back office purposes. |
| TextC | Displays a read-only, customer-defined text value set by FIX client applications. The value is not sent to the exchange. |
| TextTT | Displays an optional, user-defined text value from the Setup app or entered in the **TextTT** free-form text field in the Order Ticket. The value displayed in this column remains on submitted orders for tracking purposes in the TT system, but is not routed to the exchange.  You can show or hide the Text TT text box for a selected working order in the Order Toolbar. You can add or modify the text that displays in the **TextTT** column for the selected order.  In the **Position Manager** widget, you can now edit the **TextTT** column for **Local Fills** and **Admin Fills**. However, this is not available for **Admin SODs**.  **Note:** For Autospreader orders submitted by an ADL algo, the value is populated with the order tag of the parent algo order. |
| Ticks From Inside | The number of ticks between the price of the order and the inside market. For example, a Buy order working one tick below the best bid price will display “1”, or a Sell order working at the best ask price will display “0”. |
| Ticks Away | Number of ticks the order is currently away from the inside market. |
| TIF | Time In Force for the order. |
| TotNotional | The total notional value of the order (e.g., submit an order for 1 CL contract: 1 contract traded \* $50/barrel \* 1,000 barrels/contract = total notional value). |
| TrdgCap | Trading Capacity. Indication of a user dealing on own account, trading in a matched principal trading capacity, or trading in any other trading capacity. |
| TTOrderID | TT-generated ID that uniquely identifies the order associated with the transaction. |
| Time | The time the order action occurred. This value is updated after each order action.   * Order Book: Time the order was submitted or modified. * Fills: Time the fill or partial fill was received. * Audit Trail: Time the message was sent or received. |
| Trade Date | The official trade date for FX products. For some exchanges, this value may differ from the **Settlement Date** depending on the trading session which the contract settles. |
| TrdgCap | Trading Capacity. Indication of a user dealing on own account, trading in a matched principal trading capacity, or trading in any other trading capacity. |
| TrigPrc | Price at which to enter an order (Shown only when an order has an associated Trigger price, such as a TT Stop or TT If-Touched order) |
| TriggerQty | The trigger quantity of the algo or TT order type (TT Stop or TT If Touched). |
| TriggerPrcType | Shows the trigger price type: LTP, Bid, Ask, Same Side, Opposite Side. |
| TT SMP ID | Displays the value of the TT Self Match Prevention ID used to conduct a match within the TT Platform.  **Note:** This differs from the exchange self match prevention ID provided in the **SMP ID** field.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| TT SMP Instruction | Instruction provided to the TT platform as to whether to cancel the resting or incoming (aggressing) order in the event of a self-match.  **Note:** This field only applies to the TT Platform Self-Match Prevention (TT SMP) functionality. It does not contain information related to exchange-provided self-match prevention.  For an overview of TT’s support for self match prevention and the Avoid Orders That Cross (AOTC) functionality, refer to the [Order Cross Prevention](https://library.tradingtechnologies.com/user-setup/ocp-order-cross-prevention-and-position-transfer.html) section of the Setup help. |
| Type | Type of order associated with the transaction (e.g. Limit or Market). |
| UndQty | Undisclosed quantity of a disclosed quantity order (e.g. Iceberg. TT Iceberg, Time Sliced) |
| UnHgdQty | The fill quantity of futures allocations minus the fill quantity of the hedging orders. |
| UniqueExecID | TT-generated execution ID for fills. Sent in the form of a short-form GUID, no more than 22-characters in length. |
| WrkQty | Working quantity of the order |

## Fills Data Fields

**Note:** To retrieve fills data into RTD, the name of the RTD fields must match the following Fills widget column
names.

#### Fills column descriptions

| Setting                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |     |        |                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | ------ | ------------------------------------------------ |
| Account                | Account number associated with the transaction.                                                                                                                                                                                                                                                                                                                                                                                                        |     |        |                                                  |
| AcctType               | Account type code that defines the trader’s relationship with a clearing house                                                                                                                                                                                                                                                                                                                                                                         |     |        |                                                  |
| AltExchAcct            | Shows the value of Tag 440 sent to ICE and ICE\_L exchanges.                                                                                                                                                                                                                                                                                                                                                                                           |     |        |                                                  |
| BBG                    | Displays the Bloomberg product symbol when this symbology is enabled in the workspace preferences. When the exchange’s symbology is enabled, this column is blank. **Note:** Bloomberg codes are for display only and are not included in downloads from the Fills widget. Filtering of historical data does not work on the BBG column.                                                                                                               |     | Broker | The broker ID that is associated with the order. |
| B/S                    | Whether the transaction represents a Buy or Sell order                                                                                                                                                                                                                                                                                                                                                                                                 |     |        |                                                  |
| C.D.I.                 | Commodity Derivative Indicator. Indication of whether the order is for hedging purposes to reduce risk.                                                                                                                                                                                                                                                                                                                                                |     |        |                                                  |
| ClearingAcct           | Shows the value sent to the exchange as the clearing account.                                                                                                                                                                                                                                                                                                                                                                                          |     |        |                                                  |
| Client                 | Client. Identification of the customer (Short Code).                                                                                                                                                                                                                                                                                                                                                                                                   |     |        |                                                  |
| ClientSecondadry       | Secondary customer identifier associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter the customer’s legal entity identifier (LEI/Short Code).                                                                                                                                                                                                                              |     |        |                                                  |
| ClOrderID              | Unique identifier for the order assigned by the client and sent to the exchange.                                                                                                                                                                                                                                                                                                                                                                       |     |        |                                                  |
| Compliance Text        | Text field available to include additional values for compliance.                                                                                                                                                                                                                                                                                                                                                                                      |     |        |                                                  |
| Confirmed              | Contains the **Confirm** button used for confirming fills.  **Note**: Risk Administrator must enable permissions for you to confirm fills in the account. Users with view-only account permissions cannot confirm fills. See [User Account Permissions](https://library.tradingtechnologies.com/setup/company-administration/users/description-users/user-account-permissions/). If this option is not enabled, the **Confirm** button remains hidden. |     |        |                                                  |
| ConnectionID           | ID of the connection used to route the order or fill.                                                                                                                                                                                                                                                                                                                                                                                                  |     |        |                                                  |
| Contract               | The name and contract expiry for the instrument or strategy.                                                                                                                                                                                                                                                                                                                                                                                           |     |        |                                                  |
| Counterparty           | Shows the Participant ID and account number of the counterparty that you submit the order on behalf of.                                                                                                                                                                                                                                                                                                                                                |     |        |                                                  |
| CurrentUser            | TT user name of the trader associated with the transaction or owns a staged order.                                                                                                                                                                                                                                                                                                                                                                     |     |        |                                                  |
| CustOrderHandlingInstr | The “Customer Order Handling Instruction” value set on the account in Setup and sent to the exchange in Tag 1031, which identifies the execution method and source of derivatives trades.                                                                                                                                                                                                                                                              |     |        |                                                  |
| Date                   | Date the transaction occurred or the message was sent.   * Order Book: Date the order was submitted. * Fills: Date the fill was received. * Audit Trail: Date the message was sent or received. * Blocktrader: The date that the block trade was submitted on TT.                                                                                                                                                                                      |     |        |                                                  |
| D.E.A.                 | Direct Electronic Access. Shows whether or not the order is sent from direct/sponsored access, or from another source.                                                                                                                                                                                                                                                                                                                                 |     |        |                                                  |
| EchoDC\_1              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_2              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_3              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_4              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_5              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_6              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_7              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_8              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_9              | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| EchoDC\_10             | Customer-defined text field that can be populated by FIX client applications. The value is not sent to the exchange, but is visible in the Order Book, Fills, and Audit Trail widgets and on FIX Drop Copy records.                                                                                                                                                                                                                                    |     |        |                                                  |
| End                    | Shows the end date and time parameter setting for TT Order Types or ADL algos.                                                                                                                                                                                                                                                                                                                                                                         |     |        |                                                  |
| ExecDec                | Execution Decision ID. Indicates the user or firm that submitted the order. Enter a registered ID/Short Code.                                                                                                                                                                                                                                                                                                                                          |     |        |                                                  |

## Position Fields

**Note:** TT RTD Server supports the following type 2 properties.

| Property | Description |
| --- | --- |
| Account | The account identifier |
| NetPos | Current net position (**BuyQty** – **SellQty**) |
| AvgBuyPrice / AvgBuyPrice# | Average price of all buys in points  You must specify at least one **Account** filter. |
| AvgSellPrice / AvgSellPrice# | Average price of all sells in points  You must specify at least one **Account** filter. |
| AvgOpenPrice / AvgOpenPrice# | Average price of open position in points  You must specify at least one **Account** filter. |
| SodQty | Quantity of a start-of-day record |
| BuyQty | Total number of contracts bought |
| SellQty | Total number of contract sold |
| SodPrice / SodPrice# | Price of a start-of-day record in points |
| WrkBuys | Quantity of working Buy orders |
| WrkSells | Quantity of working Sell orders |

## Options Fields

**Note:** TT RTD Server supports the following type 1 properties. If you specify the name of the property in the formula, you must enclose it in quotes.

| Property                         | Description                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------- |
| AskImpliedDelta                  | Option Delta from the ask implied volatility                                             |
| AskImpliedGamma                  | Option Gamma from the ask implied volatility                                             |
| AskImpliedRho                    | Option Rho from the ask implied volatility                                               |
| AskImpliedTheo / AskImpliedTheo# | Option theoretical value implied from the market ask in TT display format / unformatted  |
| AskImpliedTheta                  | Option Theta from the ask implied volatility                                             |
| AskImpliedVega                   | Option Vega from the ask implied volatility                                              |
| AskImpliedVolatility             | Option implied volatility from the market ask                                            |
| AutofitDelta                     | Option Delta from the autofit curve                                                      |
| AutofitGamma                     | Option Gamma from the autofit curve                                                      |
| AutofitRho                       | Option Rho from the auofit curve                                                         |
| AutofitTheo / AutofitTheo#       | Option theoretical value from the autofit curve                                          |
| AutofitTheta                     | Option Theta from the autofit curve                                                      |
| AutofitVega                      | Option Vega from the autofit curve                                                       |
| AutofitVolatility                | Option volatility from the autofit curve                                                 |
| BidImpliedDelta                  | Option Delta from the bid implied volatility                                             |
| BidImpliedGamma                  | Option Gamma from the bid implied volatility                                             |
| BidImpliedRho                    | Option Rho from the bid implied volatility                                               |
| BidImpliedTheo / BidImpliedTheo# | Option theoretical value implied from the market bid in TT display format / unformatted  |
| BidImpliedTheta                  | Option Theta from the bid implied volatility                                             |
| BidImpliedVega                   | Option Vega from the bid implied volatility                                              |
| BidImpliedVolatility             | Option implied volatility from the market bid                                            |
| MidImpliedDelta                  | Option Delta from the mid implied volatility                                             |
| MidImpliedGamma                  | Option Gamma from the mid implied volatility                                             |
| MidImpliedRho                    | Option Rho from the mid implied volatility                                               |
| MidImpliedTheo / MidImpliedTheo# | Option theoretical value implied from the mid market in TT display format / unformatted  |
| MidImpliedTheta                  | Option Theta from the mid implied volatility                                             |
| MidImpliedVega                   | Option Vega from the mid implied volatility                                              |
| MidImpliedVolatility             | Option implied volatility from the mid market                                            |
| OptionType                       | Call/Put                                                                                 |
| SettlementDelta                  | Option Delta from the settlement curve                                                   |
| SettlementGamma                  | Option Gamma from the settlement curve                                                   |
| SettlementRho                    | Option Rho from the settlement curve                                                     |
| SettlementTheo / SettlementTheo# | Option theoretical value from the settlement curve in TT display format / unformatted    |
| SettlementTheta                  | Option Theta from the settlement curve                                                   |
| SettlementVega                   | Option Vega from the settlement curve                                                    |
| SettlementVolatility             | Option volatility from the settlement curve                                              |
| Status / Status$ / Status&       | Trading status of the instrument as an string (Status, Status$) or an integer (Status&). |
| Strike                           | Option strike price                                                                      |
| UserCurveDelta                   | Option Delta from the user curve                                                         |
| UserCurveGamma                   | Option Gamma from the user curve                                                         |
| UserCurveRho                     | Option Rho from the user curve                                                           |
| UserCurveTheo / UserCurveTheo#   | Option theoretical value from the user curve in TT display format / unformatted          |
| UserCurveTheta                   | Option Theta from the user curve                                                         |
| UserCurveVega                    | Option Vega from the user curve                                                          |
| UserCurveVolatility              | Option volatility from the user curve                                                    |

←[Previous PostAlerts and messages displayed when the Excel and TT connection is disrupted](alerts-and-messages-displayed-when-the-excel-and-tt-connection-is-disrupted.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/of-view-button-2.png
