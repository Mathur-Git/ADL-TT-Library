---
title: Market State block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/market-state-block/
---

# Market State block

> Category: **Trading Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/market-state-block/)

### Market State block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-market-state-block.png)

The Market State block is a trading block that lets you check whether the market is currently in a particular state and outputs a Boolean value. For example, you can use the block to see if the market is open, close, or halted.

The following example uses the Market State block to enable an Order block only if the market is open.

**Example:** **A Market State block with properties set to check for a market state of ‘open’ recieves an instrument’s market data. The market state included in the instrument data matches ‘open’ so the Market State block outputs a Boolean value of ‘True’ to the Order block.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-market-state-block-example.png)

1. Disables the [Order](order-block.md) block if the market is closed

When using a Market State block, the **Ignore Market State** option for the algo should be enabled. This option is disabled by default, which causes the algorithm to pause automatically when any market reported by an [Instrument](instrument-block.md) block in the algorithm is not in a trading session. However, because the Market State block is typically used to execute logic outside of a regular trading sessions, the **Market State** block will be rendered ineffective when the **Ignore Market State** option is disabled.

### About market states

The State drop-down menu contains a complete list of all market states for all exchanges supported by TT. Consult information regarding a specific exchange to learn whether certain market states are supported by that exchange.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| State | Market state to check  The drop-down menu contains a complete list of all market states for all exchanges supported by TT. Consult information regarding a specific exchange to learn whether certain market states are supported by that exchange. |

←[Previous PostField block](field-block.md)

[Next PostOrder block](order-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-market-state-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-market-state-block-example.png
