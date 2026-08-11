---
title: Creating a Group block
category: group-blocks
source: https://library.tradingtechnologies.com/adl/group-blocks/creating-a-group-block/
---

# Creating a Group block

> Category: **Group Blocks** · [Source](https://library.tradingtechnologies.com/adl/group-blocks/creating-a-group-block/)
>
> **Interpreted in:** [ADL Block Catalog § Group →](../../guides/block-catalog.md#group-ref)

### Creating a Group block

To create a Group block:

1. Select the blocks you want to add to the group.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-1.png)
2. Right-click on any of the selected blocks and select **Group** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-2.png)

   The selected blocks are consolidated into a single block with ports for each of the connected inputs.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-3.png)

From the Group block context menu, you can access the following options:

* **Ungroup** to restore the internal algo blocks to the parent algo.
* **Virtualize** to allow new copies of the Group block to be created every time a discrete event message enters the virtualized group block. See [Rules of Virtualization](../virtualized-blocks/rules-of-virtualization.md) for more information.
* **Add Input Connector**, **Add Output Connector** to attach extra ports providing additional input values to and output values from the Group block for the following data types:

  + Boolean
  + Numeric
  + Instrument
  + Discrete message

### Opening a Group block

To open a Group block, double-click the Group block.

The ADL canvas replaces the parent algo with the contents of the Group block, as shown:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-open-grouped-block.png)

Use the ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adv-group-block-icons.png) icons located at the top portion of the Designer canvas to navigate back to the root or parent algo.

### Ungrouping a Group block

To ungroup a Group block:

1. Right-click the block you want to ungroup to display the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-ungroup-block-1.png)
2. From the context menu, select **Ungroup**.

   The Group block is replaced with the internal contents of the Group block.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-ungroup-block-2.png)

### Deleting a Group block

To delete a Group block, right-click the group block and select **Delete**.

←[Previous PostGroup blocks overview](group-blocks-overview.md)

[Next PostAdding inputs and outputs to a Group block](adding-inputs-and-outputs-to-a-group-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-create-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-open-grouped-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adv-group-block-icons.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-ungroup-block-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gb-ungroup-block-2.png
