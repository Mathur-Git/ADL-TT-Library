---
title: Jump blocks overview
category: jump-blocks
source: https://library.tradingtechnologies.com/adl/jump-blocks/jump-blocks-overview/
---

# Jump blocks overview

> Category: **Jump Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/jump-blocks/jump-blocks-overview/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/jb-jump-blocks.png)

Jump blocks are representations of block inputs and outputs that the user can place at many locations throughout the algorithm in order to avoid cluttering up the canvas with edges. There are two components of a Jump block: the anchor Jump block (green arrow) which represents the output of a block, and one or more destination Jump blocks (pink arrow) which represent the input of another block. The pair can replace a direct edge between two blocks.

**Note:** **TT recommends that you use Jump blocks when creating an algo. They help to keep your algo organized and clean looking on the canvas, while also make it easier to follow the block logic pathways.**

### Common uses for Jump blocks

Jump blocks are commonly used for two purposes:

* To connect blocks on opposite sides of the algo so you don’t have edges running across large portions of an algo

  **Example:** **Using a Jump block to route a discrete event message to another block**

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-example.png)
* To make it easier to see the values that go into blocks without having to trace crossing edges

  **Example:** **Using Jump blocks to improve readability**

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/jb-min-max-before-after.png)

### Rules for using Jump blocks

The following rules govern the behavior of Jump blocks:

* Only the output of a block can be “jumped” to another block.
* The user can create multiple copies of the destination jump block (pink arrow) by copying or pasting the anchor Jump block (green arrow) or the destination block (pink arrow).
* Jump blocks can be applied to both continuous outputs and discrete event message outputs.
* Jump blocks cannot cross virtual block boundaries, only group block boundaries.
* Copy or paste the original variable AND the anchor Jump block together to create a new copy of both.

[Next PostAdding jump blocks](adding-jump-blocks.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/jb-jump-blocks.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/jb-min-max-before-after.png
