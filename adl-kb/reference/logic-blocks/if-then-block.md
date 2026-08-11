---
title: If Then block
category: logic-blocks
source: https://library.tradingtechnologies.com/adl/logic-blocks/if-then-block/
---

# If Then block

> Category: **Logic Blocks** · [Source](https://library.tradingtechnologies.com/adl/logic-blocks/if-then-block/)
>
> **Interpreted in:** [ADL Block Catalog § Logic blocks](../../guides/block-catalog.md#logic-blocks) · [Core Semantics § 8. NaN is contagious and destructive](../../guides/core-semantics.md#8-nan-is-contagious-and-destructive) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

### If Then block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block.png)

The If Then block outputs one of two values, based on the value of a Boolean input. When the input value is TRUE, the block outputs a value based on the block’s ThenValue condition. When the input value is false, the block outputs a value based on the block’s ElseValue condition.

**Example:** **The If Then block receives a Boolean value through its ‘if’ port, then outputs 5 if the value is TRUE or 10 if the value is FALSE.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-intro-example.png)

Like the [Equal block](equal-block.md), the If Then block uses yellow variable input ports, which allow you to specify different types of data (numeric, Boolean, or instrument). Because both inputs must be the same type of data, the block automatically sets the data type for the second input port as soon as you connect the other port. Also, the output port dynamically adjusts to match the data type of the input ports.

**Example:** **The following examples uses an If Then block to determine a quantity to use when submitting an order. The If Then block checks the current Bid quantity for the instrument. If the Bid quantity is greater than 50, the If Then block outputs 10 to the [Order](../trading-blocks/order-block.md) block’s **Quantity** port. Otherwise, it outputs 5.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-example.png)

You can link multiple If Then blocks together to define nested if-then statements as shown in the following example. To find the correct output of nested If Then blocks, always start with the right-most If Then block and trace the logical pathway to the left until arriving at an output.

**Example:** **Using nested If Then blocks**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-nested-new.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostAnd, Or, and Not blocks](and-or-and-not-blocks.md)

[Next PostOnce True block](once-true-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-intro-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-if-then-block-nested-new.png
