---
title: Add block
category: arithmetic-blocks
source: https://library.tradingtechnologies.com/adl/arithmetic-blocks/add-block/
---

# Add block

> Category: **Arithmetic Blocks** · [Source](https://library.tradingtechnologies.com/adl/arithmetic-blocks/add-block/)
>
> **Interpreted in:** [ADL Block Catalog § Arithmetic blocks](../../guides/block-catalog.md#arithmetic-blocks) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

### Add block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block.png)

The Add block adds the first input number and the second input number and outputs the sum.

**Example:** The Add block adds 2 to the bid quantity.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block-bid-example.png)

### More about Flip for Sell Order

When the **Flip for Sell Order** option is enabled, the Add block will either perform an addition or a subtraction operation, depending on the value of the **Order Side Variable** (see: [Flip For Sell Order Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information).

**Note:** If you enable Flip for Sell Order, the order of the inputs matter because it subtracts the two inputs when flipped.

As an illustration, the previous example might produce undesired results if you enable Flip for Sell Order. In the Add block, the first input is 2 and the second input is the bid quantity. If flipped, the Add block would subtract the bid quantity from 2, which is probably not the intended behavior. If you plan to enable Flip for Sell Order, you likely want to configure the Add block as follows.

**Example:** Arrange inputs to work when flipped.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block-bid-example-flip.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Flip for Sell Order | Whether to enable a single algorithm to act either as buy or sell side routine as needed  See [Flip For Sell Order Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information. |

[Next PostSubtract block](subtract-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block-bid-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-add-block-bid-example-flip.png
