---
title: Pnl block
category: miscellaneous-blocks
source: https://library.tradingtechnologies.com/adl/miscellaneous-blocks/pnl-block/
---

# Pnl block

> Category: **Miscellaneous Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/miscellaneous-blocks/pnl-block/)

### Pnl block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-pnl-block.png)

The Pnl block allow you to set P&L limits on per algo instance basis. You specify a positive P&L value that represents the maximum amount the trader can lose before pausing the algo. If the trader exceeds the specified loss threshold, the algo is automatically paused.

**Example:** **The PnL block receives the maximum-allowable loss through its input port. During trading, the PnL block monitors the trader’s P&L and will automatically pause the algo when the trader’s loss is 1000 or greater.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-pnl-block-example.png)

Every time the trader’s P&L updates, the block outputs a continuous message with new value through the **pnl** output port. It also outputs an empty discrete message through its discrete event output port for your convenience, should you choose to use the event to trigger another block.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostAlert block](alert-block.md)

[Next PostPosition Risk block](position-risk-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-pnl-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-pnl-block-example.png
