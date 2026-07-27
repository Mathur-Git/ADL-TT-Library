---
title: Value Accumulator block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/value-accumulator-block/
---

# Value Accumulator block

> Category: **Discrete Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/value-accumulator-block/)

### Value Accumulator block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block.png)

The Value Accumulator block accumulates a user-specified numeric value when it is triggered by a discrete event message. After calculating the accumulated value, the block outputs both the accumulated value and the original input discrete event message. You can also attach another discrete event message to the **reset** input port to reset the block value to 0.

**Example:** **Two ValueAccumulator blocks receive fill information. Each accumulates its value based on its internal formula and outputs the calculated value through its numeric output port. Each block can also forward its incoming message to downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-example.png)

You use the **Formula Editor** for the block to specify the value to accumulate. You can use the value of a field in the message or create a formula that generates a numeric value. For example, if you want accumulate the fill quantity for each fill message attached to the block, you could use the following formula.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-fill-qty.png)

In addition to accumulating selected information, such as fill quantity, the Value Accumulator block can also be used as a counter to count the occurrence of a user-defined market event. In the **Formula Editor**, type the value “1”. With this setup, the Value Accumulator will accumulate the numeric value “1” for each occurrence of the event, which results in counting the number of fills.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-fill-count.png)

**Example:** **Disable the Order block when the number of fills reaches three**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-example-1.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| BodyColor | Background color of the block |
| Formula | Equation used to calculate the value of the block  If not yet defined, the field displays an **edit** link that opens the [Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostMsgInfoExtractor block](msginfoextractor-block.md)

[Next PostValue Injector block](value-injector-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-fill-qty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-fill-count.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-accumulator-block-example-1.png
