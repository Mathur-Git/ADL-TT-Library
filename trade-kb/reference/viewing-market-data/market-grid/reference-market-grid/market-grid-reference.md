---
title: Market Grid Reference
category: Viewing Market Data
source: https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/reference-market-grid/market-grid-reference/
---

# Market Grid Reference

> Category: **Viewing Market Data** · [Source](https://library.tradingtechnologies.com/trade/viewing-market-data/market-grid/reference-market-grid/market-grid-reference/)
>
> **Interpreted in:** [Market Data & Depth § Market Grid / Product Grid](../../../../guides/market-data-and-depth.md#market-grid-product-grid)

## Available settings

These settings affect only the selected Market Grid widget. To update the default settings with these values for
newly-opened Market Grid widgets, or to apply them to existing opened widgets, click **Defaults**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-settings.png)

In the **Display** section, the following settings are available:

* **Grid font size**: Adjust the font size to suit your preferences and use bold text, if desired.
* **Colors**: Allows you to [customize or change the cell and column colors](../../../overview/widgets/task-widgets/customizing-widget-settings.md) available in the widget.
* **Depth increment**: Set the number of additional depth levels to show or hide when displaying market depth for an instrument.
* **Bold font**: Enable this setting to use bold text in the widget.
* **Color rows by years**: Enable this setting to highlight the contracts that expire within a year.
* **Price update highlight type**: Sets whether to change the text or background color of a price cell when the price increases or decreases.
  * **None**: Do not change the colors when a price changes.
  * **Highlight Text**: Change the price text color when the price changes.
  * **Highlight Background**: Change the price cell background color when the price changes.
* **Only show direct prices**: When this setting is checked (enabled), implied prices are filtered out and only direct prices are shown, and implied bid and ask quantities are not included in the best bid and ask quantities. When unchecked (disabled), best bid and ask prices and quantities include both direct and implied values.
* **View my orders only**: Sets whether or not to hide orders from other traders sharing an account.
  **Note:** This setting impacts working orders only and does not affect the net position value.
* **Include Undisclosed Qty in Working Qty** — Displays the sum of working and undisclosed order quantities in the **WrkBuys** and **WrkSells** columns. **Note:** When this setting is enabled, undisclosed quantity values continue to be displayed in the **UndBuys** and **UndSells** columns.
* **Show tabs**: Sets whether to show tabs at the bottom of the widget.
* **Auto sort rows on reload**:
  * **Unchecked** — User’s saved row positioning is maintained after refresh.
  * **Checked** —
    User row positioning is lost.
    Upon workspace open or refresh, Market Grid rows will display similar to when a new Market Grid is opened via Market Explorer.**Note:** This is a widget-level setting and applies to all tabs within a multi-tabbed Market Grid.
* **Set Market Grid columns**: Select the [columns](#mg-col-desc) you want shown in the Market Grid.

In the **Detailed Depth** section, the following settings are available:

* **Show Summary Rows** — Displays rows with the total Bid and Ask quantity at each price level of detailed depth.
* **Show prices for all rows** — Displays prices for all rows of detailed depth shown in the widget.

#### Market Grid column descriptions

| Column | Description |
| --- | --- |
| % Chg | The percentage of net change between the last traded price and the previous session’s **Settle** price.  **Note:** For instruments that support decimal quantities, e.g., GDAX, the net change is calculated as a continuous 24-hour net change based on the price from 24 hours ago. |
| ADelta | Delta calculated using the best Ask price. |
| AGamma | Gamma calculated using the best Ask price. |
| AIV | Implied volatility calculated using the best Ask price. |
| ARho | Rho calculated using the best Ask price. |
| ATheta | Theta calculated using the best Ask price. |
| AVega | Vega calculated using the best Ask price. |
| Ask | The best market ask price. |
| AskCnt | Shows the number of orders comprising the total ask quantity at a price level. |
| AskMktQty | Displays the total quantity of resting Sell Market orders. |
| AskQty | The total quantity working at the ask. |
| AskQtyAccum | The accumulated Ask quantity at each level of depth. The expanded depth rows in this column accumulate the quantities preceding them. |
 BBG | Displays the Bloomberg product symbol when this symbology is enabled in the workspace preferences. When the exchange’s symbology is enabled, this column is blank. **Note:** Bloomberg codes are for display only and are not included in downloads from the Fills widget. Filtering of historical data does not work on the BBG column. || BDelta | Delta calculated using the best Bid price. |
| BGamma | Gamma calculated using the best Bid price. |
| BIV | Implied volatility calculated using the best Bid price. |
| BRho | Rho calculated using the best Bid price. |
| BTheta | Theta calculated using the best Bid price. |
| BVega | Vega calculated using the best Bid price. |
| Bid | The best market bid price. |
| BidCnt | Shows the number of orders comprising the total bid quantity at a price level. |
| BidMktQty | Displays the total quantity of resting Buy Market orders. |
| BidQty | The total quantity working at the bid. |
| BidQtyAccum | The accumulated Bid quantity at each level of depth. The expanded depth rows in this column accumulate the quantities preceding them. |
| BT | Launches a Blocktrader widget populated with the selected contract. |
| CXL All | Cancel button for deleting all orders in the Market Grid. |
| CXL B | Cancel button for deleting Buy orders in the Market Grid. |
| CXL S | Cancel button for deleting Sell orders in the Market Grid. |
| Client | Client ID. The customer’s legal entity identifier (LEI/Short Code). |
| ClientSecondadry | Secondary customer identifier associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter the customer’s legal entity identifier (LEI/Short Code). |
| Close | The closing price for the session. |
| Contract | The name and contract expiry for the instrument or strategy. |
| CumQty | An accumulation of last traded quantities at the current price until it changes. |
| Delta | Call delta calculated using “user volatility” if it is provided by the user, or “fit volatility” if it is not. |
| Description | The full name of the product for each contract. |
| Exch | Name of the exchange. **Note:** For parent TT order type orders, an asterisk “\*” is appended to the exchange name in this column (e.g., CME \*) to indicate the intended destination of the submitted parent order. No asterisk appears in the **Exch** column for the related child orders sent to the exchange. |
| ExecDec | Execution Decision ID. Indicates the user or firm that submitted the order. Enter a registered ID/Short Code. |
| ExecDecSecondary | Secondary user or firm associated with the order. This field can be used for trading on behalf of clients and used for internal reporting purposes. Enter a registered ID/Short Code. |
| ExpDate | The contract expiration date. If an option to buy or sell the underlying is exercised, it must be exercised on the expiration date or anytime prior to the expiration date depending on the type of contract. |
| Gamma | Shows the change in delta per change in the underlying. |
| IV | Implied volatility value. Implied volatilities are calculated using the midpoint of bid and ask prices. |
| ImpAskQty | The implied ask quantity. |
| ImpBidQty | The implied bid quantity. For aggregated instruments, the implied bid quantity of each outright is displayed, and the sum of the implied bid quantities from each outright is displayed for the aggregated instrument. |
| IndPrc | Indicative price. Shows the indicative (open/close) price received from the exchange, as well as the equilibrium price during the Auction and Circuit Breaker states. |
| IndQty | Indicative quantity. If provided by an exchange, the indicative or theoretical quantity is displayed during Pre-Open, Auction, and Circuit Breaker market states. |
| IndSettle | Indicative settle representing the last settlement price received from the exchange |
| InstrumentId | A unique code generated by TT to identify the instrument in the TT system. |
| Last | The last traded price. |
| LastQty | Quantity of the last executed trade. |
| LastTrdDate | The last day the contract can trade. This may be different from the contract expiry date (ExpDate column). |
| Low | The low price for the session. |
| NetChg | The net change difference between the last traded price and the previous session’s **Settle** price.  **Note:** For instruments that support decimal quantities, e.g., GDAX, the net change is calculated as a continuous 24-hour net change based on the price from 24 hours ago. |
| Open | The opening price for the session. |
| OptAsk | Displays the best ask of the underlying option. |
| OptAskQty | Displays the best option ask quantity. |
| OptBid | Displays the best bid of the underlying option. |
| OptBidQty | Displays the best option bid quantity. |
| OptionStyle | * **American** — may be exercised on *any* business day until the expiration date. * **European** — may be exercised *only* on the expiration date. * **Asian** — may be exercised at the average price instead of the spot price. * **One Time** — is exercised *automatically* at a single reference price on the last trading day. |
| Pos | Net open position in an instrument. |
| Settle | The settlement price from the previous session. |
| Status | The current status of the exchange:   * PreTrading * Open * FastMarket * Auction * PostTrading * Closed * NonTradable * PreOpen * Freeze * Expired * OpeningAuction * ClosingAuction * Reserve * PriceDiscovery * Level * CircuitBreaker * SessionRoll * FeedDown * LateOpen * NonFinalClosed * NumStatus |
| Theta | Shows the change in options value per change in time. Also known as time decay. |
| Time | Shows the time of the last trade for the contract. Displayed as local time of the location where you are viewing and trading contracts in the Market Grid. |
| Type | The type of instrument or options strategy. |
| UndBuys | Shows the undisclosed Buy order quantity. |
| UndSells | Shows the undisclosed Sell order quantity. |
| Vega | Shows the change in options value per change in volatility. |
| Vol | The total traded quantity for the session. |
| VWAP | (Volume Weighted Average Price) — The intraday average traded price of an instrument based on both volume and price.  **Note:** Only available for instruments on the EPEX exchange. |
| WrkBuys | The total quantity of working buy orders for an instrument. If market depth is displayed, the working quantities are displayed for each price. Columns display the quantities of and floating order book access to working orders. If market depth is displayed, the working quantities are displayed for each price. |
| WrkSells | The total number of working orders at the ask price. At the best ask price, the total number of working sell orders for all levels of depth is also displayed. Columns display the quantities of and floating order book access to working orders. If market depth is displayed, the working quantities are displayed for each price. |

## Selective defaults

Market Grid lets you select individual customizations to save as default Market Grid settings and to update existing
Market Grid widgets, while applying other customizations to the current widget. Checking either of the **Save
as Market Grid defaults** or **Updating existing Market Grid widgets** settings enables the
**Selectively update properties** setting. You can choose the individual widget attributes you want
to save.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-settings-defaults.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-settings.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/icon-bt-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mg-settings-defaults.png
