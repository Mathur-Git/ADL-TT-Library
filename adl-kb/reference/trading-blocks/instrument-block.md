---
title: Instrument block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/instrument-block/
---

# Instrument block

> Category: **Trading Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/instrument-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-instrument-block.png)

The Instrument block is a trading block that identifies an exchange-traded or synthetic instrument to use in an algorithm. It allows your algo to access market data and activity associated with the instrument. You connect the output from the Instrument block to other trading blocks, such as [Order](order-block.md) and [Field](field-block.md) blocks, that need access to an instrument’s ID or market data.

The following example shows how an Instrument block can connect to an Order block to submit an order, a Field block to retrieve the bid price, and a Market State block to determine whether the market is open.

**Example:** **The Instrument block has an instrument identified in its properties and passes that instrument’s market data to upstream blocks.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-instrument-connections.png)

1. Order block to specify the instrument
2. Field block to extract market data for the instrument
3. Market State block to determine the current status of the market on which the instrument trades

To provide flexibility and reuse for algorithms, ADL allows you to specify instruments in three different ways:

* **Static**. The instrument is set during development and does not change during execution.
* **User-defined**. The instrument can be set or changed before starting an algorithm. This option allows you to design an algorithm template that can be used with different instruments.
* **Order instrument**. Any algorithm containing an Order Instrument will be recognized as an [Order Ticket Algorithm (OTA)](../adl-overview/advanced-concepts/description/order-ticket-algos-ota.md), which can be executed directly from an [MD Trader](../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md) widget. The instrument automatically matches the instrument shown on the ladder.**Note:** Additionally, you can enable the **Show algo order on ladder** setting in the [Information Panel](../adl-overview/adl-basic-concepts/description-adl-basic-concepts/adl-designer.md#information-panel) to display the OTA parent synthetic order, in addition to its child orders, in the MD Trader widget.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Instrument | Default instrument to attach to the block  You can begin typing to search for an instrument, or you can use the instrument explorer to identify the instrument. |
| Type | Method to use to specify the instrument   * **Static**. The instrument is set during development and does not change during execution. * **User Defined**. The instrument can be set or changed before starting an algorithm. * **Order Instrument**. The instrument automatically matches the instrument shown on the ladder in the MD Trader widget.   You can also use the right-click context menu to set or change the method. |
| Account | Account to use for accessing the market data and for routing orders |

←[Previous PostTrading blocks overview](trading-blocks-overview.md)

[Next PostField block](field-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-instrument-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-instrument-connections.png
