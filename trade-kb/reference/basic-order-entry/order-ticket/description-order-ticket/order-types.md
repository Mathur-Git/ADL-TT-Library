---
title: Order Types
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/description-order-ticket/order-types/
---

# Order Types

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/description-order-ticket/order-types/)

Order types allow you to specify how an order behaves when it enters the market. For example, you may want an
order to immediately fill at the current best price (market order) or to fill only at a particular price (limit
order).

Order Types differ from order restrictions which set how the order behaves during the session. For example, an
order may delete if not filled by the end of the session (Day) or may persist until filled or canceled (GTC).

Native order types refer to those types that are managed by an exchange. For example, the EEX exchange supports
OCO (one cancel other) orders natively, but CME does not. TT supports the following native order types, if
supported by an exchange:

* [Market](#market-type)
* [Limit](#limit-type)
* [Iceberg](#iceberg-type)
* [Stop Market](#stop-market-type)
* [Stop Limit](#stop-limit-type)
* [Cross](#cross-type)
* [Block](#block-type)
* [Book or Cancel (BOC)](#boc-type)
* [One Cancels Other (OCO)](#oco-type)
* [Minimum Volume](#minvol)
* [Limit If Touched](#lit)
* [Market If Touched](#mit)
* [Market On Open](#moo)
* [Market On Close](#moc)
* [Post Only (Limit)](#post)
* [FOK (Fill Or Kill)](#fok)
* [FAK (Fill And Kill)](#fak)
* [IOC (Immediate Or Cancel)](#ioc)
* [MLM (Market Limit Market)](#mlm)

Additionally, you can use [TT Order Types](../../tt-order-types/description-tt-order-types/tt-order-types-overview.md) that provide synthetic order
types to submit orders not supported natively at an exchange. For example, you could use a TT Timed algo to
submit an order automatically at a specific time.

## Market

A **Market** order is an order placed without a price with the intention of hitting the best Bid or taking the
best Offer currently available in the market. The order fills at the current best price.

Market orders may partially fill at multiple price levels.

For example, if you submit a 100-lot bid at $15.25 but there are only 10 ask orders at the price, you will
receive a partial fill at $15.25. The remaining quantity of your working order (90-lots) will attempt to fill at
each of the next best prices (e.g., 15.50, 15.75, etc) until the total order fills.

To place a market order, simply select Market in the order types drop-down, set the quantity in the MD
Trader® widget and select the direction you wish to trade.

## Limit

Limit orders allow you to submit an order at a specific limit price. Like market orders, limit orders allow for
partial fills however, the remaining quantity continues to work in the market at the original limit price.

To place a limit order, simply select Limit in the order types drop-down, set the quantity in the MD
Trader® widget and select the price level and direction you wish to trade.

Note: Limits differ from Stop Limit which allow you to select a range of prices (e.g., number of ticks aways
from) near the limit price.

## Iceberg

An Iceberg order executes a large quantity by breaking it into smaller disclosed orders or slices. When one
disclosed portion fills, the next portion is sent to the market. This process continues until the order is
filled.

To place an iceberg order, simply select Iceberg in the order types drop-down. The quantity field now allows for
two values:

* Qty: Sets the total order quantity for the iceberg order.
* Display: Sets the disclosed-quantity or the amount that displays in the market.

You may also enter Iceberg orders via the Order Ticket window by selecting iceberg from the order types
drop-down.

When managing an Iceberg order, you may view the following information in the Order Book and the Audit Trail:

* Qty: the total quantity of the order.
* WrkQty: the working quantity of the current slice working in the market.
* ExeQty: the current total filled quantity.
* UndQty: the remaining undisclosed quantity not displayed to the market. The undisclosed quantity equals the
  order’s total quantity minus the sum of the executed quantity and the working quantity (i.e., UndQty = Qty –
  (ExeQty + WrkQty).
* UndQty: Qty – (ExeQty + WrkQty)

## Stop Market

Stop Market orders allow you to select a trigger price which determines when the software submits a market order.
When the market reaches or passes the trigger price, a market order enters the market and fills at the best
market price.

The order may fill at a worse level than the trigger price and also may partially fill at multiple price levels.

## Stop Limit

Stop Limit orders allow you to select a trigger price which determines when the software submits a limit order.
When the market reaches or passes the trigger price, a limit order enters
the market and fills at the trigger price.

When you select Stop Limit, a Configure button displays. This allows you to set
a range of valid fill prices by selecting the number of ticks away from the trigger price.

If partially filled, the remaining volume continues to work in the market at either the trigger
price level or the configured number of ticks away.

## Cross

Cross orders are prearranged trades with either a party within the trading firm itself or with a
specified party outside the firm. This order type is available in the Trade application if the exchange you are
connected to supports cross trades. To submit a cross order, refer to [Submitting Cross Orders](../task-order-ticket/submitting-a-cross-trade.md).

## Block

Block orders are high-volume, prearranged OTC (over-the-counter) trades with either a party within the
trading firm itself or with a specified party outside the firm. This order type is available in the Trade
application if the exchange you are connected to supports block trades. To submit a block order, refer to [Submitting Block Orders](../../blocktrader/task-blocktrader/submitting-trades-in-blocktrader.md).

## Book or Cancel (BOC)

Book or Cancel (BOC) orders behave similar to limit orders except a Book or Cancel order deletes immediately if
entered at a price level that results in either a partial or full fill.

* Deletes immediately if entered at a price level that results in either a partial or full fill.
* Rests in the order book.

You must submit a Book or Cancel order with a limit price. You cannot submit a Book or Cancel market order.

## One Cancels Other (OCO)

An Order Cancels Order (OCO) order sets two orders of the same quantity for the same contract at different price
levels. When one order executes the other order cancels.

To enter an OCO, select OCO from the order types drop-down and enter the first bid or offer. The cursor now
displays SL Trigger and requires you to enter a second order on the same side of the market. When either order
fills, the other order is automatically cancelled.

## Minimum Volume

Minimum Volume orders require a minimum quantity to be executed immediately at the entered price. TT supports Minimum Volume orders on the following exchanges: B3, MX.

If the minimum quantity cannot be filled immediately at that price or better, then the order for the total quantity is rejected at the exchange. If the minimum quantity can be filled but the total quantity of the order is larger than what is immediately available, the balance of the order quantity will continue working in the market at that price.

## Limit If Touched

A Limit If Touched (LIT) order allows you to select a trigger price that determines when to submit a Limit order
at a set price. When the market reaches or passes the trigger price, a Limit order is submitted at the set Limit
price above or below the current market. Buy LIT orders are placed below
the last traded price, and Sell LIT orders are placed above the last traded price. For a list of exchanges that
support this order type and are traded on TT, refer to [Supported
Order Types and TIFs](https://library.tradingtechnologies.com/user-setup/otr-supported-native-order-types-and-tifs.html).

## Market If Touched

A Market If Touched (MIT) order allows you to select a trigger price that determines when to submit a Market
order. When the market reaches or passes the trigger price, a Market order is submitted above or below the
current market. Buy MIT orders are placed below the last traded price, and Sell MIT orders are placed above the
last traded price. For a list of exchanges that support this order type and are traded on TT, refer to [Supported
Order Types and TIFs](https://library.tradingtechnologies.com/user-setup/otr-supported-native-order-types-and-tifs.html).

## Market On Open

A Market On Open (MOO) order is a Market order submitted during a pre-open trading period and is intended for
execution at the opening market price. If these orders are partially filled at the market price on the open, any
unfilled quantity remains working in the market as a Limit Day order. For a list of exchanges that support this
order type and are traded on TT, refer to [Supported
Order Types and TIFs](https://library.tradingtechnologies.com/user-setup/otr-supported-native-order-types-and-tifs.html).

## Market On Close

A Market On Close (MOC) order is a Market order submitted during a pre-close or closing auction trading period and
is intended for execution at or near the closing market price for the trading session. For a list of exchanges
that support this order type and are traded on TT, refer to [Supported
Order Types and TIFs](https://library.tradingtechnologies.com/user-setup/otr-supported-native-order-types-and-tifs.html).

## Post Only (Limit)

The full Limit order works in the market and will not be charged “Taker Fees” for being filled immediately. If
any part of the order would take liquidity immediately due to its price, the entire order will be rejected by
the exchange.

## FOK (Fill Or Kill)

A Fill Or Kill (FOK) order is an order to buy or sell a contract that must be executed immediately in its
entirety; otherwise, the entire order will be canceled (i.e., no partial execution of the order is allowed).

## FAK (Fill And Kill)

A Fill And Kill (FAK) order is immediately executed against resting orders. If the order cannot be fully filled,
the remaining balance is canceled. A minimum quantity can be specified. If the specified minimum quantity cannot
be filled, the order is canceled.

## IOC (Immediate Or Cancel)

An Immediate Or Cancel (IOC) order is an order to buy or sell a contract that attempts to execute all or part of
the order quantity immediately and then cancels any unfilled portion of the order.

## MLM (Market Limit Market)

A Market Limit Market (MLM) order is executed at the best price available in the market. If the Market Limit
Market order can only be partially filled, the order becomes a Limit order and the remaining quantity remains on
the order book at the specified limit price.

←[Previous PostExchange-specific order entry features](exchange-specific-order-entry-features.md)

