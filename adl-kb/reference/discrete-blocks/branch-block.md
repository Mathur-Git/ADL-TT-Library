---
title: Branch block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/branch-block/
---

# Branch block

> Category: **Discrete Blocks** · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/branch-block/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Control flow](../../guides/design-patterns.md#control-flow) · [Formula Editor Reference § Blocks that take formulas](../../guides/formula-reference.md#blocks-that-take-formulas) · [Formula Editor Reference § Worked patterns](../../guides/formula-reference.md#worked-patterns)

### Branch block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block.png)

The Branch block routes messages to different parts of an algorithm based on the Boolean formula in the Branch block when triggered by an incoming discrete event message. If the formula evaluates to TRUE, the block routes the discrete event message to its **yes** output port; otherwise, it sends the message through its **no** output port.

**Example:** **The Branch block looks at the incoming discrete event message for an existing order and routes the message through the **yes** port if the message represents a hedge order; otherwise, send it through the **no** port.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block-example.png)

The Branch block uses the following formula:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block-formula.png)

**Note:** Though both the Branch block and the State block look alike, they are fundamentally different. While the State block waits until one of the internalized Boolean statements turns TRUE to output a message, the Branch block immediately directs the incoming message either through the **yes** or the **no** output port.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formula | Equations used to determine which branch (output port) to take  The **edit** link opens the [Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md).  **Note:** **The formula must evaluate to a Boolean value.** |

←[Previous PostState block](state-block.md)

[Next PostFunnel block](funnel-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-branch-block-formula.png
