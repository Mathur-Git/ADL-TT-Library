---
title: Value Extractor block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/value-extractor-block/
---

# Value Extractor block

> Category: **Discrete Blocks** · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/value-extractor-block/)
>
> **Interpreted in:** [Core Semantics § 2. The freeze rule](../../guides/core-semantics.md#2-the-freeze-rule) · [Core Semantics § 7. Virtualization](../../guides/core-semantics.md#7-virtualization) · [Design Patterns & Recipe Index § Control flow](../../guides/design-patterns.md#control-flow) · [Formula Editor Reference § Blocks that take formulas](../../guides/formula-reference.md#blocks-that-take-formulas) · [Formula Editor Reference § Message fields](../../guides/formula-reference.md#message-fields)

### Value Extractor block

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor.png)

The Value Extractor block receives a discrete message, extracts specified fields, and can access data from elsewhere in your algo to perform logic and calculations. The Value Extractor block can then output fields extracted from the discrete message, data from elsewhere in your algo, or specified numeric or Boolean values. The Value Extractor block is commonly used to take a snapshot of information that may be constantly changing in the market, such as the quantity at the best offer at the time of a fill for a given instrument. By taking a snapshot, the algo can capture the information at a single moment in time and use the “frozen” information later on even if the market continues to change. When a new discrete event message triggers the Value Extractor block, the block will replace the old snapshot with a new one.

The Value Extractor block works as follows:

1. A incoming discrete event message triggers the Value Extractor block.
2. When triggered, the Value Extractor block takes a “snapshot” of the desired information. You can choose to take a snapshot of information contained within the input message or of information from elsewhere in the algo.
3. After the taking the snapshot, the Value Extractor block passes the input message unchanged through its lower-right port and starts to output the snapshot through the upper-right port.As indicated by the default yellow output port, the value can be a Numeric, True/False or an Instrument type depending on the type of information captured by the snapshot.

**Example:** **The Value Extractor block is configured with a formula to extract the trade quantity from the incoming discrete event message.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-formula-qty.png)

**Example:** **The Value Extractor block receives a fill message from an entry order block. The Value Extractor block is configured with a formula to extract the fill quantity from the discrete event message and compare the fill quantity from the fill message to the best ask quantity in the market at the time of the fill. Based on the result, the block will either output the fill quantity or best ask quantity through its **val** port as the quantity for the exit order.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-example.png)

**Example:** **The Value Extractor block is configured as a “toggle” to indicate the occurrence of a specific event in the market. To do this, the user can instruct a Value Extractor block to take a snapshot of the numeric value “1” (in the internal logic canvas, type the value “1”) when triggered by a discrete event message. Before the discrete event message occurs, the Value Extractor block will output the default value of zero. However, when the discrete event message occurs, the Value Extractor block will output a value of 1, indicating that the discrete event has occurred.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-formula-count.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formula | Equation used to calculate the value of the block  The **edit** link opens the [Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostValue Injector block](value-injector-block.md)

[Next PostValue Bucket block](value-bucket-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-formula-qty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-extractor-block-formula-count.png
