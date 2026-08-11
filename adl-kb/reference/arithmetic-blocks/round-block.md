---
title: Round block
category: arithmetic-blocks
source: https://library.tradingtechnologies.com/adl/arithmetic-blocks/round-block/
---

# Round block

> Category: **Arithmetic Blocks** · [Source](https://library.tradingtechnologies.com/adl/arithmetic-blocks/round-block/)
>
> **Interpreted in:** [ADL Block Catalog § Arithmetic blocks](../../guides/block-catalog.md#arithmetic-blocks) · [Gotchas, Hard Limits & Platform Constraints § Pre-flight checklist](../../guides/gotchas-and-limits.md#pre-flight-checklist)

### Round block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-round-block.png)

The Round block is an arithmentic block that rounds a numeric input (**num**) based on the increment input (**inc**) and rounding method configured in the **Mode** block property; it then outputs the rounded value.

**Example:** Two Round blocks configured with **AlwaysDown** and **Normal** modes round the input number to the nearest tenth.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-round-block-example.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Mode | Rules to use for rounding the input value:   * **Normal**: Use standard rounding rules (n < 5, round down; n >= 5, round up) * **Always Down**: Round to the lower increment * **Always Up**: Round to the upper increment |

←[Previous PostMod block](mod-block.md)

[Next PostAverage block](average-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-round-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-round-block-example.png
