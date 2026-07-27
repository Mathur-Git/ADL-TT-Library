---
title: Number block
category: basic-blocks
source: https://library.tradingtechnologies.com/adl/basic-blocks/number-block/
---

# Number block

> Category: **Basic Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/basic-blocks/number-block/)

### Number block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-number-block.png)

The Number block outputs a constant numeric value. The value of the block can be set as follows:

* Static value that is set during algo creation and does not change for the duration of the algorithm’s execution either by entering a number for the value field in the Block Properties panel or by typing a number into block search to prepopulate the number block before adding it to the canvas
* User-defined value that can be set by the user when starting the algorithm
* Order price value that gets its values from the price level a user clicks in the MD Trader widget when launching a OTA (order ticket algorithm)
* Order quantity value that gets its value from the quantity specified in the MD Trader widget when launching a OTA (order ticket algorithm)
* User-defined value that sets the time-in-force for a [Discrete Order](../trading-blocks/discrete-order-block.md#formulas) block formula.
* User-defined value that sets the order type for a [Discrete Order](../trading-blocks/discrete-order-block.md#formulas) block formula.

**Example:** **The Number block outputs a number that is used by the Order block to set the order quantity.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-number-block-example.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Default Value | Default value to use when configuring an algo instance.  **Note**: This value pre-populates the value in the in the [Variables](../adl-overview/adl-basic-concepts/description-adl-basic-concepts/user-defined-variables.md) tab. Changing the value in the **Variables** tab while [testing user-defined variables](../adl-overview/building-your-first-algo/lessons/testing-the-entry-logic.md#testing-variables) only changes the block value for the algo currently running in the canvas; it does not affect the default value defined for the block. |
| Variable Type | Method to set the value:   * Static * User Defined * Order Quantity * Order Price * User Defined (TIF)  Can be used to specify the **timeInForce** variable in the [Discrete Order](../trading-blocks/discrete-order-block.md#formulas) block’s **Formulas** block property. The user must use one of the following values:   + 1: Day (GTD)   + 2: Good till cancel (GTC)   + 3: At the opening   + 4: Immediate or cancel (IOC)   + 5: Fill or kill (FOK)   + 6: Good till crossing   + 7: Good till date (GTDate)   + 8: At the close   + 9: Good through crossing   + 10: At crossing   + 13: Auction   + 14: Good in session   + 15: Day plus   + 16: Good till cancel plus   + 17: Good till date plus * User Defined (Order Type)  Can be used to specify the **orderType** variable in the [Discrete Order](../trading-blocks/discrete-order-block.md#formulas) block’s **Formulas** block property. The user must use one of the following values:   + 1: Market   + 2: Limit   + 3: Stop   + 4: Stop limit   + 5: Iceberg   + 20: Market with leftover as limit   + 21: Market limit market with leftover as limit   + 30: Stop market to limit   + 31: If-touched market   + 32: If-touched limit   + 33: If-touched market to limit   + 37: Limit post-only |

←[Previous PostBool block](bool-block.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-number-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bb-number-block-example.png
