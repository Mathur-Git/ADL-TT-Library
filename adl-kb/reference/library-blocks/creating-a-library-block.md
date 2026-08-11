---
title: Creating a library block
category: library-blocks
source: https://library.tradingtechnologies.com/adl/library-blocks/creating-a-library-block/
---

# Creating a library block

> Category: **Library Blocks** · [Source](https://library.tradingtechnologies.com/adl/library-blocks/creating-a-library-block/)
>
> **Interpreted in:** [ADL Block Catalog § Library →](../../guides/block-catalog.md#library-ref) · [Gotchas, Hard Limits & Platform Constraints § Blocks](../../guides/gotchas-and-limits.md#blocks)

Suppose you find yourself adding the same set of blocks to perform a particular task. If you create a [group block](../group-blocks/creating-a-group-block.md) with this functionality, you can easily add it your block library and then reuse it any time you want.

### Adding a group block to your library

You can save a portion of an existing algo by converting it to a group block and then saving it as a Library block. In this case, you create a Library block from the portion of the algo that calculates a price some number of ticks away from the market.

To create a group block and add it to your library:

1. Identify the blocks and connections you want to group.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-1.png)
2. Using the left-mouse button, select the desired blocks. You could also **Ctrl-click** (**Command-click**) to add blocks individually to the selection.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-2.png)
3. Right-click on any of the selected blocks and select **Group** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-3.png)

   The selected blocks are replaced with a group block.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-4.png)
4. Select the group block and change the **Name** so you can easily identify it from other blocks in your block library.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-5.png)

     
   **Note:** **If you do not rename the block, the default (e.g. **Group0**) name will be used when you add it to your library, and you will not be able to change its name later.**
5. Right-click on the group block, and select **Save As Library Block**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-6.png)
6. After the Library block is uploaded successfully, click **Close**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-7.png)

### Removing a block from your library

To remove a block from your library:

1. From the **File** menu, select **Load Library Block**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-load-library-block-1.png)
2. Click the delete icon (![](https://library.tradingtechnologies.com/wp-content/uploads/2026/01/icon-delete-algo.png)) and click **yes** to confirm.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-delete-library-block.png)

←[Previous PostLibrary blocks overview](library-blocks-overview.md)

[Next PostUsing library blocks in an algo](using-library-blocks-in-an-algo.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-4.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-6.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-create-7.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-load-library-block-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/01/icon-delete-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/lblk-delete-library-block.png
