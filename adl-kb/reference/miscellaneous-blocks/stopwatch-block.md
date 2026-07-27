---
title: Stopwatch block
category: miscellaneous-blocks
source: https://library.tradingtechnologies.com/adl/miscellaneous-blocks/stopwatch-block/
---

# Stopwatch block

> Category: **Miscellaneous Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/miscellaneous-blocks/stopwatch-block/)

### Stopwatch block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-stopwatch-block.png)

When a discrete event message enters its discrete input port, the Stopwatch block evaluates its StopTime formula (using the [Formula Builder](../adl-overview/advanced-concepts/description/formula-editor.md)) to determine the stop time in milliseconds. After the specified stop time, the block sends a discrete event message through its output port.

**Example:** **The Stopwatch block is triggered when it receives a discrete event message from a fill. The Stopwatch block formula is set to 1000, which causes the block to wait one second before forwarding the discrete event message to the [DiscreteOrder](../trading-blocks/discrete-order-block.md) block to submit the exit order.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-stopwatch-block-example.png)

**Note:** If the value calculated within the Stopwatch block is negative, the discrete message propagates through the Stopwatch block as if a value of **0** has been defined.

Each time the block receives an input, it resets and restarts the timer. For example, suppose a Stopwatch block with a 5000ms timer is triggered by an incoming message. After five seconds, it sends out a discrete event message. However, if a second input message enters the block after only three seconds (3000ms), the Stopwatch block restarts its internal timer. In this case, the Stopwatch block will it send its first output message after eight seconds.

**Note:** TT continuously makes system improvements to improve performance.
Therefore, TT strongly recommends that users avoid including time delays which assume specific system latencies when
designing sequence logic for their algos.

**Note:** During periods of algo server recovery, in particular over the weekend, if a Stopwatch timer has elapsed at the start of recovery, the algo will get into a Failed state.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formula | [Formula](../adl-overview/advanced-concepts/description/formula-editor.md) to calculate the timer value.  The minimum timer value for the Stopwatch block is 25ms. |

←[Previous PostAnalytics block](analytics-block.md)

[Next PostNote block](note-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-stopwatch-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-stopwatch-block-example.png
