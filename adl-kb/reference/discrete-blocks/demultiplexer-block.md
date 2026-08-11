---
title: Demultiplexer block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/demultiplexer-block/
---

# Demultiplexer block

> Category: **Discrete Blocks** · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/demultiplexer-block/)
>
> **Interpreted in:** [Core Semantics § 9. Order block vs Discrete Order block vs Single Order...](../../guides/core-semantics.md#9-order-block-vs-discrete-order-block-vs-single-order-container) · [Design Patterns & Recipe Index § Control flow](../../guides/design-patterns.md#control-flow) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

### Demultiplexer block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-demultiplexer-block.png)

The Demultiplexer block takes in a discrete event message from the [Single Order Container](../trading-blocks/single-order-container-block.md) and evaluates whether the message is a fill, change or a delete confirmation. After the evaluation, the block directs the message, unchanged, through the appropriate output (e.g., for fill confirmations, the original message is output as the message through the fills output port).

**Example:** **The Demultiplexer block receives a discrete event message from the [Single Order Container](../trading-blocks/single-order-container-block.md) block, determines which type of message it received, and routes the unchanged message through the corresponding output port. If the discrete event message represents an Add OK or a Fill message, the block sends the message to downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-demultiplexer-block-soc.png)

**Note:** Only the Single Order Container can provide the required input discrete event message.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Connectors | Output message ports to expose:   * **Add Requested**:New order request sent to the exchange * **Added**: New order confirmations * **Change Requested**:Change order request sent to the exchange * **Changed**: Change order acknowledgments * **Delete Requested**:Delete order request sent to the exchange * **Deleted**: Delete order acknowledgments * **Filled**: Fill confirmations |

←[Previous PostSequence block](sequence-block.md)

[Next PostMoving Average block](moving-average-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-demultiplexer-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-demultiplexer-block-soc.png
