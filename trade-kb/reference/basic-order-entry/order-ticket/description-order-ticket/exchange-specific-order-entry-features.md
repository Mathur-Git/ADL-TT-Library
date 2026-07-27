---
title: Exchange-specific order entry features
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/description-order-ticket/exchange-specific-order-entry-features/
---

# Exchange-specific order entry features

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/description-order-ticket/exchange-specific-order-entry-features/)

An Order Ticket exposes some additional buttons to support exchange-specific order functionality.

## Exchanges using the Open/Close button in Order Ticket

The following exchanges allow you to indicate whether an order opens or closes a position on a per instrument basis:
CZCE, DCE, ICE, ICE\_L, INE, EEX, Eurex, Euronext, SHFE, and TFEX.

To support this functionality in TT, the Order Ticket displays an Open/Close selector per instrument as shown:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-open-close-button.png)

## TT support for China markets

TT provides access to the following China markets via a TT FIX Order Gateway:

* Shanghai International Energy Exchange (INE)
* Dalian Commodity Exchange (DCE)
* Zhengzhou Commodity Exchange (CZCE))
* Shanghai Futures Exchange (SHFE)
* China Financial Futures Exchange (CHFFE)

**Note**: Access to these markets requires a FIX Order Gateway connection to a third party system. Please contact your Customer Success Manager at TT for more details.

The **open/close** position selector in MD Trader and the Order Ticket provide FIFO controls that affect positions for China markets. In addition to selecting **open** or **close**, you can select the following order flags when trading on CZCE, DCE, and INE:

* **fifo** (CZCE) — Close the previous day first and then close today’s position.
* **close today** (INE) — Close today’s position only.
* **close fifo** (INE) — Close previous day only.
* **open – spread switch** (DCE, ZCE) — Open a position in the front leg and close a position in the back leg of an exchange spread.
* **close – spread switch** (DCE, ZCE) — Close a position in the front leg and open a position in the back leg of an exchange spread.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-open-close-china-1.png)

For China markets, you can also indicate the trading strategy for the order by using the **trading strategy** selector in MD Trader or Order Ticket. Click the selector to show the drop down menu and select one of the following:

* **directional**
* **hedge**
* **arbitrage**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-open-close-directional-1.png)

## MiFID II exchanges

For exchanges that need to comply with the MiFID II regulations, the **Show order entry compliance fields** setting in the **Orders** section of [Preferences](../../../overview/preferences/description-preferences/orders-preferences.md#cdi) can be enabled to add compliance fields to the Order Ticket.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cdi-dropdown.png)

The items added include:

* **CDI** (Commodity Derivative Indicator) dropdown that lets a user report whether a trade is reducing risk, also referred to as a hedging trade. The dropdown supports the following choices:
  * **<CDI>**: Use the value defined in Setup.
  * **CDI Yes**: This order is a hedging trade.
  * **CDI No**: This order is not a hedging trade.
* **Invest Decision** field for the short code identifying who made the trading decision.
* **Exec Decision** field for the short code identifying who or what algo is submitting the order.
* **Client ID** field for the short code identifying the customer.

If specified, these values override the default order profile settings defined in Setup.

## Support of block trades in the Order Ticket

Block trades are high volume trades in any outright or strategy product and arranged by two counterparties outside of the open market.

The Order Ticket supports submitting block trades at the following exchange: [EEX](http://www.eurexchange.com/exchange-en/products/eurex-trade-entry-services/block-trades).

## Support for CME SLEDS orders on TT

For most exchange-defined calendar spreads on CME, you can designate orders as [SLEDS (Single Line Entry Differential Spreads) orders](https://www.cmegroup.com/clearing/operations-and-deliveries/accepted-trade-types.html). For example, buyers and sellers can determine if they want these trades to be cleared by CME Clearing using the prior day settlement price instead of LTP for the front leg of their calendar spread.

Using the Order Ticket SLEDS selector, you can submit orders as designated for SLEDS pricing by CME Clearing. To show the selector, right-click the Order Ticket and select **Show/Hide** | **SLED** from the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-sleds-menu.png)

**Note**: Before submitting a SLEDS order, ensure the **Override exception for SLED orders** account setting is enabled in Setup. This setting *must be enabled* on the account used for submitting SLEDS orders even if **Client Can Override** is also enabled on the account.

To designate a spread order as eligible for SLEDS pricing, select a percent “%” or ampersand “&” character in the SLEDS selector in the Order Ticket.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-sleds.png)

## CME cabinet trades on TT

TT supports order entry at cabinet prices for outright options contracts on CME. A cabinet trade allows a user to mitigate risk by executing deep out-of-the-money options at the lowest price possible.

To submit an order at a cabinet price on TT, enter “0.00” as the price of the order in MD Trader or the Order Ticket. When “0.00” is entered as the price, TT submits the order to the exchange as a “cabinet” order.

**Note**: CME Globex only supports one cabinet price per instrument. Contact the exchange for the exact cabinet price and increment for the outright options instrument you are trading.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-cabinet.png)

←[Previous PostOrder entry from Order Ticket](order-entry-from-order-ticket.md)

[Next PostOrder Types](order-types.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-open-close-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-open-close-china-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-open-close-directional-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cdi-dropdown.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-sleds-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-sleds.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-cme-cabinet.png
