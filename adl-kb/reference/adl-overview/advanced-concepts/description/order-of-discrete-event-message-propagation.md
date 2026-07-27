---
title: Order of discrete event message propagation
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-of-discrete-event-message-propagation/
---

# Order of discrete event message propagation

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/order-of-discrete-event-message-propagation/)

Understanding the granular order in which the variables are updated is one of the most crucial elements in mastering advanced programming techniques in ADL.

When a block outputs a pulse of discrete event message, an algorithm temporarily stops channeling continuous messages from the exchange servers. Continuous message channels will remain closed while the pulse of discrete event message propagates throughout the algorithm. In effect, this behavior will “freeze” the output of blocks such as the Instrument Field block which channels streaming market data. In this static state, the pulse of discrete event message will traverse the pathway designed by the user, updating the output values of the blocks which lie in its path. Once this propagation is complete, the algorithm will resume channeling continuous messages from all exchange servers.

**Note:** TT continuously makes system improvements to improve performance.
Therefore, TT strongly recommends that users avoid including time delays which assume specific system latencies when
designing sequence logic for their algos.

Note that such propagation takes place within microseconds and will not be perceivable in practice. With this mechanism, however, ADL allows the user to capture and use the market data existing precisely at the moment of a discrete event. The following ADL rules govern the exact order in which the blocks are updated as a discrete event message propagates.

### Pass-through blocks

During the propagation, when a discrete event message enters a Pass-Through block (i.e., any block which receives and passes on a discrete event message unchanged), actions occur in the following order:

1. The continuous output values of the pass-through block itself is updated first.
2. Any “downstream” block which uses the continuous output values of the pass-through block is updated.
3. The discrete event message exits the pass-through block.
4. The discrete event message continues to propagate through the designed pathway until it hits a termination point (see next bullet point).

**Example:** **Order of updates upon entering a “pass-through” block.** This example shows how the discrete event message will first update the blocks connected “downstream” from the pass-through block before exiting the pass-through block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-message-propagation-1.png)

1. The discrete event message enters the block.
2. The continuous output value propagates to the Add block input port.
3. The discrete event message output port exits the block and continues propagating through the pathway.

### Termination blocks

A discrete event message propagates along its path as far as possible and terminates upon entering any one of the following blocks:

* Termination block: [Single Order Container block](../../../trading-blocks/single-order-container-block.md), [State block](../../../discrete-blocks/state-block.md), [Value Accumulator block](../../../discrete-blocks/value-accumulator-block.md), [Discrete Order block](../../../trading-blocks/discrete-order-block.md), [Stopwatch block](../../../miscellaneous-blocks/stopwatch-block.md), [Terminal block](../../../miscellaneous-blocks/terminal-block.md), [Alert block](../../../miscellaneous-blocks/alert-block.md), and “Reset” input ports
* Pass-Through block with no discrete pathway extending beyond it

**Example:** **Termination point**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-message-propagation-2.png)

←[Previous PostVirtualization](virtualization.md)

[Next PostFormula Editor](formula-editor.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-message-propagation-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-message-propagation-2.png
