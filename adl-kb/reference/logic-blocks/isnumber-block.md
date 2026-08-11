---
title: IsNumber block
category: logic-blocks
source: https://library.tradingtechnologies.com/adl/logic-blocks/isnumber-block/
---

# IsNumber block

> Category: **Logic Blocks** · [Source](https://library.tradingtechnologies.com/adl/logic-blocks/isnumber-block/)
>
> **Interpreted in:** [ADL Block Catalog § Logic blocks](../../guides/block-catalog.md#logic-blocks) · [Core Semantics § 8. NaN is contagious and destructive](../../guides/core-semantics.md#8-nan-is-contagious-and-destructive) · [Formula Editor Reference § Guarding formulas](../../guides/formula-reference.md#guarding-formulas) · [Gotchas, Hard Limits & Platform Constraints § NaN](../../guides/gotchas-and-limits.md#nan)

### Is Number block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-is-number-block.png)

The Is Number block determines if a value is a valid number, as follows:

* Returns TRUE if the value on the input port is a valid number.
* Returns FALSE if the value on the input port is **NaN** (Not A Number). This value is considered an invalid value in ADL.

If you use a NaN value as an input to any smart trading block, such as an Order block, the block will not create a new order. If the block is instructed to modify an existing order to a price or a quantity of NaN, it will simply delete the order.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostOnce True block](once-true-block.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lb-is-number-block.png
