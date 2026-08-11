---
title: Price block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/price-block/
---

# Price block

> Category: **Trading Blocks** · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/price-block/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § User-defined variables](../../guides/algo-types.md#user-defined-variables)

### Price block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block.png)

The Price block is a trading block that allows a user to specify a valid price for an instrument using the display format, such as 150’20. During algo execution, when the user specifies a price in this block, the Price block ensures that the price is a tradable price for that instrument. The block provides an alternative to using the [Number block](../basic-blocks/number-block.md) for specifying an order price.

**Example:** **The Price block determines the price display format for the connected [Instrument](instrument-block.md) block, allowing the user to specify the price using that display format. The output price is then sent to the [Order](order-block.md) block.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block-example.png)

When the algo is launched from the Algo Dashboard, the corresponding algo parameter also uses the price display format appropriate for the instrument. When a user right-clicks or left-clicks within the price field, the value decrements or increments only to the next valid prices. In this case, the contract’s price ticks in 1/32nds so decrementing the value automatically changes it to 154’31.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block-algo-param.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| BodyColor | Background color of the block |
| Variable Type | Method to use to specify the price   * **Static**. The price is set during development and does not change during execution. * **User Defined**. The price can be set or changed before starting an algorithm. This option allows you to design an algorithm template that can be used with different prices. * **Order Price**. Any algorithm containing an Order Instrument will be recognized as an Order Ticket Algorithm (OTA), which is executable directly from an MD Trader widget. The instrument automatically matches the price shown on the ladder. |
| Price | Default value for the price block  You can use the integrated price ladder to select a price or enter the price directly. |

←[Previous PostTime And Sales block](time-and-sales-block.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-price-block-algo-param.png
