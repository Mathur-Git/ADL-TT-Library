---
title: Algos in ADL
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/description-introduction-to-adl/algos-in-adl/
---

# Algos in ADL

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/description-introduction-to-adl/algos-in-adl/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry)

An algo in ADL represents programmatic logic visually as:

* A collection of functional [blocks](../../adl-basic-concepts/description-adl-basic-concepts/blocks.md) that get input values, perform calculations and produce outputs based on each block’s function.
* A set of [edges](../../adl-basic-concepts/description-adl-basic-concepts/edges.md) that specify how that data flows between the blocks.

To give you an idea of how the blocks and edges work together, take a look at the following algo that is designed to submit a buy order for all available quantity at the opposite inside market when the available quantity falls below a user-defined value.

![ADL Intro](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl.png)

To achieve its purpose, the algo uses the following blocks and connectors:

* Because the purpose of the algo is to submit an order to the market, it needs an [Order](../../../trading-blocks/order-block.md) block to submit the buy order to the exchange. An order minimally requires an instrument, order price, and order quantity, which are represented as inputs to the Order block.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-0.png)
* To identify the instrument for the Order block’s **inst** input, the algo uses the [Instrument](../../../trading-blocks/instrument-block.md) block. In this case, the Instrument block is configured to let the user select an instrument each time the algo starts.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-1.png)
* To specify the Order block’s **price** and **qty** inputs, the algo includes two [Field](../../../trading-blocks/field-block.md) blocks. These blocks are connected to the Instrument block so they can retrieve live market data for the best bid price and quantity from the user-defined instrument.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-2.png)
* The Order block also contains an **on/off** input that optionally can be used to enable the block only when certain conditions are met. In this case, the **on/off** input ensures the algo submits an order only when the available quantity at the best bid is less than a user-defined value. To calculate the value, the algo uses a [Number](../../../basic-blocks/number-block.md) block block to get the desired threshold quantity from the user (or use 20 by default). The [Less Than](../../../logic-blocks/less-than-blocks.md) block takes its inputs from the [Field](../../../trading-blocks/field-block.md) and [Number](../../../basic-blocks/number-block.md) blocks and outputs a Boolean value that is passed to the Order block’s **on/off** input connector. When the value is true, indicating that the available quantity at the best bid is less than a user-defined value, the algo enables the Order block so it can submit the order.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-3.png)

←[Previous PostADL (Algo Design Lab) overview](adl-algo-design-lab-overview.md)

[Next PostUsing ADL algos](using-adl-algos.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-0.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/gs-algos-in-adl-3.png
