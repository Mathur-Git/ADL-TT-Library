---
title: State block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/state-block/
---

# State block

> Category: **Discrete Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/state-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block.png)

The State block receives an input discrete event message and routes the unchanged message to one of its output ports based on its internal formulas. For each output, you define a formula that evaluates to a Boolean result. When triggered by an incoming discrete event message, the State block begins evaluating its formulas until one of the evaluates to TRUE; then it routes the message through the corresponding output port. By default, the block exposes two discrete event message output ports, but you can add extra ports and define their formulas using the [Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md).

When a user-made True/False statement turns TRUE, the State block generates and outputs a discrete event message in the following manner:

* Directs the message to the **#1** output if the statement tied to it evaluates to TRUE
* Directs the message to the **#2** output if the statement tied to it evaluates to TRUE
* Directs the message each additional port added to the block and outputs if the statement tied to it evaluates to TRUE
* *When multiple True/False statements turn TRUE at once, a message outputs from the top-most port.*

After outputting its discrete event message, the State block will not re-evaluate its formulas until it receives another incoming discrete event message.

Note The State block will not “queue” up multiple incoming discrete event messages – even if multiple message enter the State block, the block can only output a single discrete event message.

ADL treats the act of sending request and receiving confirmation messages from the exchange server as discrete events, or events which occur at a single moment in time (see: [Continuous Vs. Discrete Event Messages](../adl-overview/adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages.md) for more information). In addition to these events, the user can define custom discrete events by using the [Formula Builder](../adl-overview/advanced-concepts/description/formula-editor.md) do define True/False statements for the **Formulas** field. When these True/False statements turn TRUE, ADL will consider it as an occurrence of a discrete event..

**Example:** **The State block uses its internal formulas to define three states. When triggered by the incoming discrete event message, the State block evaluates its formulas and passes the discrete event message through the appropriate port to be used by downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block-example.png)

The Formula Editor for this block defines formulas for each of the three outputs. The formula for the first port uses the > operator to compare the value of the Bid Price (from a Field) block with the value of the Snapshot Bid Price (from the Value Extractor block). The remaining formulas use the = and

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block-formula-new.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formulas | Equations used to calculate the value of the block’s output ports  The **edit** link opens the [Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostGenerator block](generator-block.md)

[Next PostBranch block](branch-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-state-block-formula-new.png
