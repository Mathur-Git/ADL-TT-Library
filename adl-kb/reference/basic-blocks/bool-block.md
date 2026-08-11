---
title: Bool block
category: basic-blocks
source: https://library.tradingtechnologies.com/adl/basic-blocks/bool-block/
---

# Bool block

> Category: **Basic Blocks** · [Source](https://library.tradingtechnologies.com/adl/basic-blocks/bool-block/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § OTA — Order Ticket Algo](../../guides/algo-types.md#ota-order-ticket-algo) · [Algo Types, Launching & Deployment § User-defined variables](../../guides/algo-types.md#user-defined-variables) · [Design Patterns & Recipe Index § Order entry](../../guides/design-patterns.md#order-entry)

### Bool block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-bool-block.png)

The Bool block outputs a TRUE or FALSE value. You can use the Bool block as an “on/off” switch to enable or disable other blocks.

The value of the block can be set as follows:

* Static value that does not change for the duration of the algorithm’s execution
* User-defined value that can be set by the user when starting the algorithm
* Order side value that gets its values from the price level a user clicks in the MD Trader widget when launching a OTA (order ticket algorithm)

The following illustrates different ways you can use Bool blocks with user-defined values to control an algorithm’s behavior.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-bool-block-example.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Value | Boolean value to output: True or False |
| Variable Type | Method to set the value:   * Static * UserDefined * OrderSide |

[Next PostNumber block](number-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-bool-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-bool-block-example.png
