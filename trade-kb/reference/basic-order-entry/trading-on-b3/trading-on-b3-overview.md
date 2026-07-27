---
title: Trading on B3 overview
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/trading-on-b3/trading-on-b3-overview/
---

# Trading on B3 overview

> Category: **Basic Order Entry** · [KB Home](../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/trading-on-b3/trading-on-b3-overview/)

The B3 exchange, formerly BVMF, was established in 2008 by a merger between the São Paulo Stock Exchange and Brazilian Mercantile & Futures Exchange. B3 is located in São Paulo, Brazil and offers you access to trading stocks, currencies, commodities, and futures on one exchange.

To support trading on B3, TT provides the following:

* [Detailed depth](#detailed) for B3 instruments in the Market Grid widget.
* [Counterparty information](#counterparty) is displayed for working orders in Market Grid and Depth widgets, and for completed trades in Time & Sales.
* For [Auction and Pre-Open](#auction) market states, Buy/Sell quantity imbalances, quantities for resting Buy/Sell Market orders, and accumulated quantities at the indicative price for Bids and Asks are displayed in Market Grid. The “On Auction” and “On Close” time-in-force order restrictions are available in the Order Ticket for equity products during these states.
* Settlement values as [Unit Prices for interest rate products](#settlepu) are displayed in the **SettlePU** column in Market Grid.
* P/L for the DI1 interest rate product is calculated in [Unit Prices (PU)](#pl).
* [Two-sided Cross](#cross2) orders are supported in the Order Ticket from Market Grid.
* Cross trades are [identified and filterable](#cross) in Time & Sales.
* [Hotkeys](#hotkeys) are available for launching an Order Ticket from Market Grid.

## Viewing B3 counterparty information

TT displays the counterparty code or name in the **AskMbr** and **BidMbr** columns in
the Market Grid, Depth, and Time & Sales widgets.

In Market Grid, the counterparty code or name is displayed for detailed depth only. No counterparty information is displayed for aggregate depth. To display detailed depth, expand the contract row and check the **Detail** checkbox.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-counterparty.png)

When you open or launch a linked Depth widget for a B3 instrument in Market Grid, counterparty information is displayed in the **BidMbr** and **AskMbr** columns.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-display.png)

In Time and Sales, the counterparty
code is displayed in the **AskMbr** and **BidMbr** columns for completed trades.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ts-counterparty.png)

## B3 Auction and Pre-Open support

Auctions are used in the B3 market for determining
the market price of a contract by accepting bids and offers for
a specified time period without matching. BVMF auction states are
either scheduled (e.g., Pre-Open market state) or triggered per
product or market condition during continuous trading (i.e., intra-day
auction).

### Viewing imbalance quantitiy

Buy/Sell quantity imbalances during Auction states are displayed in the **ImbQty** column in Market Grid. The imbalance quantity is the difference between the Bids and Asks at a given price in the
market, allowing you to determine if there are more buyers than sellers
or more sellers than buyers at each price for a given contract.

A positive value indicates more
quantity on the bid than the offer, and a negative value indicates
more quantity on the offer than the bid. Both quantities are highlighted
using the Net Change Up/Net Change Down color settings.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-imbalance.png)

### Resting Market Orders

Quantities of resting Buy/Sell “On Auction” and “On Close” orders during Auction states are displayed in the **BidMktQty** and **AskMktQty** columns in Market Grid. The Bid market quantity (BidMktQty) column
displays the total quantity of resting Buy Market orders, and the Ask
market quantity (AskMktQty) column displays the total quantity of resting Sell Market
orders.

### Viewing Indicative Price and Quantity

In Market Grid, accumulated quantities at the indicative price are displayed for Bid and Ask during Auction states. The quantities are displayed in the **BidQty** and **AskQty** columns, and the indicative price is displayed in the **IndPrc** column. Net change and P/L calculations are updated based on the indicative price when it’s available.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-indicative.png)

In MD Trader, the appropriate price column highlights the
indicative price during the Auction and Pre-Open periods.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mdt-indicative.png)

### Submitting Auction Orders

The “On Auction” and “On Close” time-in-force (TIF) order restrictions for Market orders are supported for equity products. You can submit Market On Auction and Market On Close orders using the Order Ticket from Market Grid.

Market On Auction orders can be submitted during Auction states only. Market On Close orders can be submitted during continuous trading, but do not work in the market until the Closing Auction begins. When an auction expires, the unfilled quantity of the order is deleted at the exchange.

## B3 Unit Price support

The Market Grid shows the settlement price unit in the **SettlePU** column, which is a converted form of the settlement price.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-settlepu1.png)

The DI instrument price is an annualized interest rate for interbank deposits. Each rate has a corresponding unitary price (PU), which is the final value discounted by the interest rate adjusted by the number of workdays to expire. At the end of each session, the exchange releases the settle denominated in interest rate and its corresponding settle in unitary price, which is displayed in the **SettlePU** column. P/L for the DI1 interest rate product is calculated using unitary prices.

## Submitting B3 two-sided Cross trades

To submit a two-sided Cross for a B3 instrument, open an Order Ticket in the Market Grid and select **Cross** from order type selector to open the **Cross** flyout panel. In the panel, select an account for both sides of the Cross trade, set the price and quantity, and click **Submit**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ot-cross1.png)

## Viewing Cross trades in Time & Sales

To filter the **Type** column for Cross trades in Time & Sales, click the drop-down arrow and select
**Cross**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ts-filter-cross.png)

## Hotkeys

Hotkeys are available to launch an Order Ticket from Market Grid as a Buy ticket (Alt+B) or a Sell ticket (Alt+S). When the Order Ticket is open, pressing the “Enter” key will submit the order and “Esc” will close the ticket.

The hotkey defaults can be customized in your workspace preferences. To edit the order entry hotkeys, click **Preferences** from the workspace menu bar, then click | **Hotkeys** | **Widgets** | **Market Grid**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ot-hotkeys.png)

## Exchange News

The Exchange News widget displays the news messages sent by the exchange on the B3 price feed. The widget subscribes to and displays news messages for all instruments traded at the exchange. To open the widget, click **Widgets** | **Market Views** from the workspace menu bar.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/news-overview.png)

**Note**: The widget displays news only for the B3 market. News from other exchanges is displayed in the Audit Trail.

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-counterparty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/depth-b3-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ts-counterparty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-imbalance.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-indicative.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mdt-indicative.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-mg-settlepu1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ot-cross1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ts-filter-cross.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/b3-ot-hotkeys.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/news-overview.png
