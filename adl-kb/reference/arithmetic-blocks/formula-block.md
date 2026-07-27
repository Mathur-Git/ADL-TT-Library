---
title: Formula block
category: arithmetic-blocks
source: https://library.tradingtechnologies.com/adl/arithmetic-blocks/formula-block/
---

# Formula block

> Category: **Arithmetic Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/arithmetic-blocks/formula-block/)

### Formula block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block.png)

The Formula block evaluates a user-defined equation and outputs the result of the evaluation as a True/False, numeric, or an instrument type output. The block recalculates and outputs its value whenever any of the connectors referenced in its internal formula changes. Any connector used in the formula establishes an implicit connection to the Formula block

**Example:** The Formula block uses the **avg** outputs of the two [Moving Average](../discrete-blocks/moving-average-block.md) blocks to output **TRUE** when the difference between the 1-min and 5-min moving average exceeds the value of the **Diff Trigger** [Number](../basic-blocks/number-block.md) block. The Formula block outputs **FALSE**, otherwise.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block-example-new.png)

The formula for the block is specified as follows in the **Formula Editor**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block-example-formula-new.png)

In this example, the implicit connections from the two Moving Average block **avg** output ports cause the Formula block to recalculate when either of the **avg** output port values change.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formula | Equation used to calculate the value of the block  If not yet defined, the field displays a **Click to edit formula** link that opens the [Formula Builder](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostMath block](math-block.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block-example-new.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ab-formula-block-example-formula-new.png
