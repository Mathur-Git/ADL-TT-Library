---
title: Value Injector block
category: discrete-blocks
source: https://library.tradingtechnologies.com/adl/discrete-blocks/value-injector-block/
---

# Value Injector block

> Category: **Discrete Blocks** · [Source](https://library.tradingtechnologies.com/adl/discrete-blocks/value-injector-block/)
>
> **Interpreted in:** [Core Semantics § 7. Virtualization](../../guides/core-semantics.md#7-virtualization) · [Design Patterns & Recipe Index § Control flow](../../guides/design-patterns.md#control-flow) · [Formula Editor Reference § Blocks that take formulas](../../guides/formula-reference.md#blocks-that-take-formulas) · [Formula Editor Reference § Message fields](../../guides/formula-reference.md#message-fields)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block.png)

The Value Injector block receives a discrete event message and either adds new message fields or overwrites one or more of the existing message fields and sends the modified discrete message through its output port.

The Value Injector block operates in the following manner:

1. A discrete event message enters the Value Injector block.
2. The Value Injector block over-writes the specified fields of the incoming with user-specified values. The fields and the values must be specified in advance in the **Fields Formula Editor**.
3. After the over-write process, the Value Injector block passes on the modified message through its right-side output port.

**Example:** **When triggered by the empty discrete event message output from the [Loop](../miscellaneous-blocks/loop-block.md) block, the Value Injector block uses its internal formula to retrieve the price and quantity from their respective blocks and adds these values to the message before sending it to a [Value Bucket](value-bucket-block.md) block.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block-example.png)

When using the Value Injector block, it is important to recognize that every discrete event message is composed of multiple “fields,” with numeric or true/false values assigned to each. For instance, a discrete event message generated from a fill will contain a numeric value in the **fillPrice** and the **fillQuantity** fields. But it will contain zero’s for other irrelevant fields, such as **deletedQuantity**.

**Note:** **A single Value Injector block can over-write multiple fields of the incoming message.**

You can use the **Field Formula Editor** to define formulas for one or more values to inject into the output discrete event message.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block-formula.png)

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Formulas | Equations used to overwrite the values of different fields in the block  The **edit** link opens the [Fields Formula Editor](../adl-overview/advanced-concepts/description/formula-editor.md). |

←[Previous PostValue Accumulator block](value-accumulator-block.md)

[Next PostValue Extractor block](value-extractor-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/db-value-injector-block-formula.png
