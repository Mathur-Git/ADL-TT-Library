---
title: Submit Orders Between Specific Start/Stop Times
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/submit-orders-between-specific-start-stop-times/
---

# Submit Orders Between Specific Start/Stop Times

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/submit-orders-between-specific-start-stop-times/)

Users often need to turn on/off logic during specific time frames. There are multiple ways to do something in ADL, however the following focuses on using the [Generator block](../../../discrete-blocks/generator-block.md) to achieve this type of logic.

In the ADL canvas shown below, we have two Generator blocks set to **AtStartTime**. Only the **UTC Time** is selected, and the inputs to these blocks are user defined. You’ll notice that the **Trade?** [AND block](../../../logic-blocks/and-or-and-not-blocks.md) is currently false, preventing the algo from submitting orders.

When the time matches the **Start Time**, a discrete message will be output and will end up in the [Value Accumulator block](../../../discrete-blocks/value-accumulator-block.md) which is set to a # of 1 on the inside formula builder. When it gets this message, it outputs a 1 out of the continuous output port, and the following Boolean logic will turn that **Trade?** [AND block](../../../logic-blocks/and-or-and-not-blocks.md) to true, turning the [Order block](../../../trading-blocks/order-block.md) on.

When the **Stop Time** matches the stop time inputs you set, this generator fires another discrete message, which also goes into its own [Value Accumulator block](../../../discrete-blocks/value-accumulator-block.md). This action turns off the **Trade?** [AND block](../../../logic-blocks/and-or-and-not-blocks.md) as well as the [Order block](../../../trading-blocks/order-block.md).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-submit-order-start-stop-time.png)

←[Previous PostCorrectly Sequencing Discrete Events](correctly-sequencing-discrete-events.md)

[Next PostSubmit Iceberg with Random Quantity and Delay](submit-iceberg-with-random-quantity-and-delay.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-submit-order-start-stop-time.png
