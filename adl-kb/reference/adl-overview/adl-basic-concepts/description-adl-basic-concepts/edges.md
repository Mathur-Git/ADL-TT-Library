---
title: Edges
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/edges/
---

# Edges

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/edges/)
>
> **Interpreted in:** [ADL Block Catalog § Port type legend](../../../../guides/block-catalog.md#port-type-legend)

An edge is the line that [connects](../task-adl-basic-concepts/adding-connecting-and-arranging-blocks.md#connecting-blocks) an output port of one
block to the input port of another block. Edges define how information flows through an ADL algo by identifying the
pathways between ADL blocks. When a block’s output port sends a value, that value propagates to the connected blocks
which can then use the value to perform their corresponding block actions. You can connect one block’s output port
to another block’s input port, ultimately defining the overall logic of the algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-connections-example.png)

1. Edges that send information from an Instrument block output port to the **inst** input port of an
   Order block and the input port of a Field block.
2. An edge that sends the best bid price from the Field block output port to the price input for the Order block.
3. An edge that sends the quantity from the Number block output port to the qty input port of the Order block.

**Note:** An input port can receive only a single connection, while an output port can connect to multiple inputs.

#### Connecting ports of different data types

Edges can only provide connections between compatible port types. For example, a [Boolean](../../../basic-blocks/bool-block.md) block output port can connect to an input port of an [Or](../../../logic-blocks/and-or-and-not-blocks.md) block, but not to an input port of an [Add](../../../arithmetic-blocks/add-block.md) block. When attempting to connect “unlike” ports, ADL displays a visual warning
on the canvas to indicate that the connection is not allowed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bc-prevent-diff-port-types.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-connections-invalid.png)

#### Circular references

ADL does not allow a an output from a block to be fed back into its own input. When you attempt to create such a
circular connection, ADL displays a visual warning on the canvas to indicate that the connection is not allowed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-prevent-circular-ref.png)

←[Previous PostBlocks](blocks.md)

[Next PostContinuous vs. discrete event messages](continuous-vs-discrete-event-messages.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-connections-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bc-prevent-diff-port-types.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-connections-invalid.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-prevent-circular-ref.png
