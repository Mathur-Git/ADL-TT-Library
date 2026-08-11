---
title: Divide block
category: arithmetic-blocks
source: https://library.tradingtechnologies.com/adl/arithmetic-blocks/divide-block/
---

# Divide block

> Category: **Arithmetic Blocks** · [Source](https://library.tradingtechnologies.com/adl/arithmetic-blocks/divide-block/)
>
> **Interpreted in:** [ADL Block Catalog § Arithmetic blocks](../../guides/block-catalog.md#arithmetic-blocks) · [Core Semantics § 8. NaN is contagious and destructive](../../guides/core-semantics.md#8-nan-is-contagious-and-destructive)

### Divide block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-divide-block.png)

The Divide block divides the first input by the second input and outputs the quotient. The order of inputs affects the outcome.

**Example:** The Divide block divides the values of the Bid Quantity and Bid Order Count [Field](../trading-blocks/field-block.md) blocks and outputs the quotient representing the average bid order size.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-divide-block-example.png)

**Note:** Dividing a zero by another zero will output **-nan** (Not A Number). In a similar manner, dividing a non-zero number by a zero will output a positive or a negative infinity. Keep in mind that these values are invalid inputs in ADL.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostMultiply block](multiply-block.md)

[Next PostMod block](mod-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-divide-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-divide-block-example.png
