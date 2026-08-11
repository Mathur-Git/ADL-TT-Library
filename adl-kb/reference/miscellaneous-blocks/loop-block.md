---
title: Loop block
category: miscellaneous-blocks
source: https://library.tradingtechnologies.com/adl/miscellaneous-blocks/loop-block/
---

# Loop block

> Category: **Miscellaneous Blocks** · [Source](https://library.tradingtechnologies.com/adl/miscellaneous-blocks/loop-block/)
>
> **Interpreted in:** [Core Semantics § 1. Two kinds of message](../../guides/core-semantics.md#1-two-kinds-of-message) · [Core Semantics § 6. The Loop block suspends actors](../../guides/core-semantics.md#6-the-loop-block-suspends-actors) · [Design Patterns & Recipe Index § Order entry](../../guides/design-patterns.md#order-entry) · [Gotchas, Hard Limits & Platform Constraints § Execution model](../../guides/gotchas-and-limits.md#execution-model)

### Loop block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block.png)

The Loop block generates and outputs a user-specified number of empty discrete event messages, one after another, to facilitate designs that require loops.

**Example:** **The Loop block starts a three-interation loop (as specified through its times input port) when the Generator block sends a discrete event message through the Loop block’s enter port. For each iteration, the Loop block outputs the loop counter through its index port and sends an empty discrete event message through its loop output port. For the last interation, the Loop block also sends an empty discrete event message through its Exit output port.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-intro.png)

**Note:** **The Loop block outputs the counter through the index port before the discrete event message is generated and output.**

### Timing considerations

It is important to note that the Loop block does not allow any “actor” block (i.e., a block that can take tangible actions such as placing an order) to take an action while it is performing the loop.

**Example:** **Loop block fails to decrement an order price.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-timing.png)

In this example, the Loop block is designed to loop up to three times, and at each iteration it decrements the price input of the Order block by one price increment. At a glance, it might seem that the [Order](../trading-blocks/order-block.md) block will generate three change requests to incrementally move its child orders down the market. However, the Loop block does not allow the Order block to take any actions during the loop. It is only after the loop has completed that the Order block can take an action using the final resulting price input.

The following sequence of events occurs when this algorithm is started:

1. The Order block joins the best bid price with a 1-lot child order.
2. The Generator block generates and pushes a discrete event message downstream, triggering the Loop block.
3. The Loop block loops up to three times, and at each iteration it decrements the price input of the Order block by one price increment. However, the Order block cannot take any action during this step because the Loop did not output a discrete event message to pause itself until downstream action completed.
4. After the loop completes, the Order block changes its child order based on the final resulting price input.

One way you could solve the timing problem is to use a Discrete Order block instead of an Order block and send a discrete event message throught Loop block’s loop port to the msg input port of the Discrete Order block. Using the loop output allows the downstream action to send an order before starting the next loop iteration, shown in the following example.

Example **Use the Loop block to create a stack of Buy orders in the market**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-timing-fixed.png)

1. The Start Stack [Generator](../discrete-blocks/generator-block.md) block sends an empty discrete message to the Loop block’s enter port to trigger the Loop block.
2. For the first iteration, the Loop block will update its index output to “1”, which the algo uses to calculate the next price.
3. The Loop block will then output its first discrete event message, which will pause the Loop block and trigger the [Discrete Order](../trading-blocks/discrete-order-block.md) block to submit an order with the Bid price at the price level calculated from the Loop index.
4. The Loop block will increment its index by 1 and then generate its second discrete event message output. This step will repeat for the specified number of loop iterations.
5. After the last message is generated, the Loop block generates and outputs another discrete event message to indicate that the loop sequence has been completed.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostRandom Number block](random-number-block.md)

[Next PostAlert block](alert-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-timing.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-loop-block-timing-fixed.png
