---
title: Generator block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/generator-block/
---

# Generator block

> Category: **Discrete Blocks** · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/generator-block/)
>
> **Interpreted in:** [Core Semantics § 1. Two kinds of message](../../guides/core-semantics.md#1-two-kinds-of-message) · [Core Semantics § 5. Actor blocks act before generators fire](../../guides/core-semantics.md#5-actor-blocks-act-before-generators-fire) · [Gotchas, Hard Limits & Platform Constraints § Hard numeric limits](../../guides/gotchas-and-limits.md#hard-numeric-limits)

### Generator block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block.png)

The Generator block produces an empty discrete event message at the launch of the algorithm. As the message is empty, it contains no market information; however, an empty discrete message can be used to trigger other blocks that use discrete messages as inputs, such as a Pause block. The Generator block can be used to trigger other discrete blocks at precise moments in time.

**Example:** **The Generator block has its **Mode** property set to **Time Interval**. With its **enabled** and **repeat** properties set to ‘true,’ it uses the input from the [Number](../basic-blocks/number-block.md) block to generate an empty discrete event message every second (1000 milliseconds) to trigger downstream logic.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block-example.png)

### Generator modes

The Generator block provides different modes for specifying when the block generates a discrete event message:

* **TimeInterval**: Generates a discrete message at regular time intervals. This mode exposes the following input ports:

  + enabled: Whether to activate the block
  + repeating: Whether to continue sending messages at the specified interval
  + periodMs: Number of milliseconds between messages. The minimum interval is 100 milliseconds.
* **BoolChange**: Generates a discrete message when the value of its Boolean input changes, either from TRUE to FALSE or from FALSE to TRUE. This mode exposes a Boolean input port.
* **BoolTrue**: Generates a discrete message when its Boolean input becomes TRUE. This mode exposes a Boolean input port.
* **EveryStart**: Generates a discrete message when the algorithm initially launches, as well as every time the algorithm is paused and then resumed.
* **InitialStart**: Generates a discrete message once at the launch of the algorithm, then becomes inactive for the life of the algorithm.
* **At Start Time**: Generates a discrete message a specific time or specific date and time (timezone=UTC). This mode exposes the following ports:

  + hour, minute, second, millisecond: Time to generate the message.
  + month, day, year: Specific date to generate the message. These ports are shown only if you add a UTCDate connector in the Block Properties.

  **Note**: If you do not specify a date, the event will repeat daily at the specified time.
* **At Start Time-Combined**: Generates a discrete message at a user-specified date and time. This mode shows the **Date Time** block setting that allows you to select the date and time from a calendar. It also exposes a [Number](../basic-blocks/number-block.md) port that outputs the UTCDateTime as the number of milliseconds since UNIX epoch (Thursday, January 1, 1970). You can use this value for downstream time-related comparisons and calculations.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block-calendar.png)

  Unlike the **At Start Time** mode, this mode does not expose input ports for the start time; however, it is automatically declared as a user-defined parameter. A calendar widget will be displayed in [Algo Dashboard](../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) / [Autotrader](../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) to allow the user to specify a value.

  **Note**: This mode automatically displays a calendar widget for the algo parameter in the [Algo Dashboard](../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) and [Autotrader](../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) widgets.
* **UserTrigger**: Waits until a user triggers the block to generate a discrete message.

  When using this type of generator, a button is added to Autotrader. Clicking the button triggers the generator. The algo must be deployed to test this trigger.

### Timing considerations

When using the Generator block, it is important to know the exact timing at which the discrete event messages are generated.

When **InitialStart** or **EveryStart** is selected, the following sequence of events occurs when the algorithm is started:

1. All “actor” blocks (i.e., blocks that can take tangible actions such as placing an order) first perform their actions.
2. The Generator block generates and pushes a discrete event message downstream.

When **BoolChange** or **BoolTrue** is selected, a continuous update changes the value of the Boolean input on the Generator block and the following sequence of events occurs:

1. The Generator block does not generate a discrete event message immediately—it allows the continuous update to propagate completely throughout the algorithm.
2. All “actor” blocks (i.e., blocks that can take tangible actions such as placing an order) first take their actions.
3. The Generator block generates and pushes a discrete event message downstream.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Mode | When the block should [generate](#modes) its discrete event message |

←[Previous PostValue Bucket block](value-bucket-block.md)

[Next PostState block](state-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-generator-block-calendar.png
