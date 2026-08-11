---
title: Time And Sales block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/time-and-sales-block/
---

# Time And Sales block

> Category: **Trading Blocks** · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/time-and-sales-block/)
>
> **Interpreted in:** [Core Semantics § 1. Two kinds of message](../../guides/core-semantics.md#1-two-kinds-of-message) · [Design Patterns & Recipe Index § Market data, bars and indicators](../../guides/design-patterns.md#market-data-bars-and-indicators) · [Formula Editor Reference § Message fields](../../guides/formula-reference.md#message-fields) · [Gotchas, Hard Limits & Platform Constraints § Environment restrictions](../../guides/gotchas-and-limits.md#environment-restrictions) · [Market Data & Depth § Time and Sales](../../../trade-kb/guides/market-data-and-depth.md#time-and-sales)

### Time And Sales block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block.png)

The Time And Sales block is a trading block that provides information for individual trades. Whenever a trade occurs for the specified instrument, the Time And Sales block outputs a discrete event message containing information regarding the last trade (trade price or quantity). The discrete event message can be sent to another discrete block, such as the [MsgInfo Extractor](../discrete-blocks/msginfoextractor-block.md) block, to extract trade data.

**Example:** **The Time and Sales block receives an update from the Instrument block each time a transaction occurs and sends the time & sales information to a [MsgInfo Extractor](../discrete-blocks/msginfoextractor-block.md) block to extract the price and quantity of the last trade.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block-example.png)

The Time And Sales block provides the following trade data:

* instrument
* tradeQuantity
* tradePrice
* tradeIsHit
* tradeIsTake
* tradeIsUnknown
* tradeIsOTC
* tradeIsImplied
* tradeIsLeg
* trade
* transaction time (year, month, day, hour, minute, second, milliseconds)

### Differences between Time And Sales block values and Field block values

The Time And Sales block and the [Field](field-block.md) block both allow you to access last-traded-price (LTP) and last-traded-quantity (LTQ) values; however, the values from these two block can differ due to how the blocks propagate changes in market data.

* Field blocks represent periodic snapshots of the market. For instruments with very active trading, a Field block might occasionally miss an LTP or LTQ that occurs between consecutive snapshots. For many trading purposes, market data snapshots are sufficient.
* Conversely, the Time And Sales block exposes every change in LTP or LTQ. Every time a trade occurs, the block fires a discrete event message containing the information regarding the trade, including the trade price and trade quantity.

**Example:** **Differences between Field blocks and Time And Sales blocks**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block-coalescing.png)

**Note:** **When developing an algo, you must start an algo to see time and sales data.**

### Blocks that can use time and sales data

The following blocks can extract and use the information generated from a Time And Sales block:

* [Branch block](../discrete-blocks/branch-block.md)
* [Discrete Max block](../discrete-blocks/discrete-min-max-blocks.md)
* [Discrete Min block](../discrete-blocks/discrete-min-max-blocks.md)
* [Discrete Order block](discrete-order-block.md)
* [MsgInfo Extractor block](../discrete-blocks/msginfoextractor-block.md)
* [Moving Average block](../discrete-blocks/moving-average-block.md)
* [State block](../discrete-blocks/state-block.md)
* [Value Accumulator block](../discrete-blocks/value-accumulator-block.md)
* [Value Bucket block](../discrete-blocks/value-bucket-block.md)
* [Value Extractor block](../discrete-blocks/value-extractor-block.md)

**Note:** **Certain logic propagated from a Time And Sales block discrete message could behave differently when running an algo in live and simulation modes, due to coalescing differences in the two environments.**

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostSingle Order Container block](single-order-container-block.md)

[Next PostPrice block](price-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-time-and-sales-block-coalescing.png
