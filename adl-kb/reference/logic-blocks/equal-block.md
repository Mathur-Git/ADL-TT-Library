---
title: Equal block
category: logic-blocks
source: https://library.tradingtechnologies.com/adl/logic-blocks/equal-block/
---

# Equal block

> Category: **Logic Blocks** · [Source](https://library.tradingtechnologies.com/adl/logic-blocks/equal-block/)
>
> **Interpreted in:** [ADL Block Catalog § Logic blocks](../../guides/block-catalog.md#logic-blocks) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

### Equal blocks

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block.png)

The Equal block compares two inputs of the same data type, returning TRUE when the inputs are equal and FALSE otherwise. When you add an Equal block to the canvas, both input ports are yellow, indicating they are variable type ports. You can connect numeric, Boolean, or instrument values to variable inputs.

**Example:** **The Equal block receives inputs from two [Market State](../trading-blocks/market-state-block.md) blocks and outputs TRUE if both states are Open; otherwise, it outputs FALSE.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block-example.png)

To ensure that both variable input ports contain the same type of data, the Equal block automatically changes the port type to match the type of the first input connected to it.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block-ports.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostLess Than blocks](less-than-blocks.md)

[Next PostAnd, Or, and Not blocks](and-or-and-not-blocks.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-equal-block-ports.png
