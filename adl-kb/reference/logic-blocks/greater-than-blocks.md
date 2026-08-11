---
title: Greater Than blocks
category: logic-blocks
source: https://library.tradingtechnologies.com/adl/logic-blocks/greater-than-blocks/
---

# Greater Than blocks

> Category: **Logic Blocks** · [Source](https://library.tradingtechnologies.com/adl/logic-blocks/greater-than-blocks/)
>
> **Interpreted in:** [ADL Block Catalog § Logic blocks](../../guides/block-catalog.md#logic-blocks)

### Greater Than blocks

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-greater-than-blocks.png)

The Greater Than and Greater Than Equal blocks compare two number inputs. When the first input is greater than (or equal to) the second, the block outputs TRUE; otherwise it outputs FALSE.

**Example:** **The Greater Than block returns TRUE if the Ask Quantity [Field](../trading-blocks/field-block.md) block input is less than Bid Quantity [Field](../trading-blocks/field-block.md) block input; otherwise, it returns FALSE.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-greater-than-blocks-example.png)

### More about Flip for Sell Order

When the **Flip for Sell Order** option is enabled, the Greater Than block will use either a “Greater Than” or a “Less Than” comparison depending on the value of the **Order Side Variable** (see: [Flip For Sell Order Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information).

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Flip For Sell Order | Whether to enable a single algorithm to act either as buy or sell side routine as needed  See [Flip For Sell Order Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information. |

[Next PostLess Than blocks](less-than-blocks.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-greater-than-blocks.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-greater-than-blocks-example.png
