---
title: Sequence block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/sequence-block/
---

# Sequence block

> Category: **Discrete Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/sequence-block/)

### Sequence block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-sequene-block.png)

The Sequence block allows you to determine the precise order of propagation of the discrete event message, as follows:

1. A discrete event message enters the Sequence block.
2. The Sequence block channels the original message , unchanged, through the **#1** port. It waits until the message is processed completely downstream.
3. Afterwards, it generates and outputs another copy of the original message through the **#2** port. It waits until the message is processed completely downstream.
4. Afterwards, it generates and outputs another copy of the original message through the **#3** port.

**Example:** **When the Sequence block receives an Add OK message from the Discrete Order block, it first routes the message to an [Alert](../miscellaneous-blocks/alert-block.md) block to play a sound, then routes the message to a [Single Order Container](../trading-blocks/single-order-container-block.md) to manage the order.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-sequence-example.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostDiscrete Min/Max blocks](discrete-min-max-blocks.md)

[Next PostDemultiplexer block](demultiplexer-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-sequene-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-sequence-example.png
