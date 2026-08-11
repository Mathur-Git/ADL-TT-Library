---
title: Handling External Events
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/handling-external-events/
---

# Handling External Events

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/handling-external-events/)
>
> **Interpreted in:** [Core Semantics § Losing control of an order](../../../../guides/core-semantics.md#losing-control-of-an-order)

The Order block, Discrete Order block, and Single Order Container block are used to manage orders in ADL. One of the properties of these blocks is named “When Ext Mod Occurs”. This property dictates a block’s behavior when the order that it is managing is externally modified. It has three possible values:

* Stop Managing
* Detach
* Ignore

#### Stop Managing

When the “Stop Managing” option is selected and an order is externally modified, the block will ignore any further changes to its input ports but continue to publish any updates to the order via the output ports. In other words, any changes to the inputs of this block will not be honored but discrete events will be propagated from the block when order and fill events occur. So the order is no longer being actively managed by the block.

#### Detach

When the “Detach” option is selected and an order is externally modified, the block will ignore any further changes to its input ports and no longer publish any updates to the order via the output ports. In other words, any changes to the inputs of this block will be not be honored and discrete events will not be propagated from the block when order and fill events occur. So the order is no longer being actively managed by the block as it is effectively dormant.

#### Ignore

When the “Ignore” option is selected and an order is externally modified, the block will override any changes to the child order using the values provided to its input ports as well as continue to propagate discrete events via the output ports when order and fill events occur. In other words, the order continues to be managed by the block and overrides any external attempts to modify it. You can, however, capture external changes and honor them. For an Order block, this can be accomplished as follows.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-handling-external-events-ignore.png)

In this snippet of an algo, the Generator0 block fires a discrete event at startup which is passed to the ValueInjector1 block. This block, in turn, injects the value of the InitialQty block (5) into the orderQuantity field of the discrete message. The MsgInfoExtractor0 block extracts the value of the orderQuantity field from the discrete message. This value is then fed into the Order block which then routes an exchange native 5-lot order @ 96.785 for the GE-Sep24 contract. The Order block is configured with “When Ext Mod Occurs” equal to “Ignore”.

When a user externally modifies the quantity of the exchange native order, the Order block fires a discrete message from its “Chg OK” port. The MsgInfoExtractor0 block then extracts the updated value of the orderQuantity field from the discrete message. This value is then fed back into the Order block. The Order block compares the current quantity of the exchange native order with the value of the “qty” input port. Since the two are equal, the Order block takes no further action. Hence, the user’s external change was honored.

Similarly, this can be accomplished as follows for an OMA.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-handling-external-events-ignore-2.png)

In this snippet of an algo, the ExistingOrder0 block fires a discrete message to the Sequence0 block when the OMA is launched. The Sequence0 block first forwards this message to the MsgInfoExtractor1 block which then extracts the value of the orderQuantity field. This value is then fed into the SingleOrderContainer0 block with the initial quantity of the adopted order. The Sequence0 block then forwards the message containing the order to be adopted to the SingleOrderContainer0 block which takes over management of the order.

When a user externally modifies the quantity of the order, the SingleOrderContainer0 block fires a discrete message. The MsgInfoExtractor1 block then extracts the new value of the orderQuantity field from the discrete message. This value is then fed back into the SingleOrderContainer0 block. The SingleOrderContainer0 block compares the current quantity of the order with the value of the “qty” input port. Since the two are equal, the Single Order Container block takes no further action. Hence, the user’s external change was honored.

←[Previous PostManaging shared algos](managing-shared-algos.md)

[Next PostCorrectly Sequencing Discrete Events](correctly-sequencing-discrete-events.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-handling-external-events-ignore.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-handling-external-events-ignore-2.png
