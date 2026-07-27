---
title: Continuous vs. discrete event messages
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages/
---

# Continuous vs. discrete event messages

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/continuous-vs-discrete-event-messages/)

A message is a piece of information that traverses the pathways established by the edges that connect ADL blocks. ADL supports two types of messages: continuous messages and discrete event messages.

### Continuous messages

Continuous messages represent information that is continuously disseminated by an exchange. For instance, the bid quantity available at a specific price level is considered to be a continuous message, as this information is essentially a continuous stream of data available at all times.

Continuous messages from an exchange are channeled into an algorithm through a few designated blocks such as the Instrument [Field](../../../trading-blocks/field-block.md) block. Other downstream blocks may use these channeled continuous messages to produce continuous outputs of their own. Such continuous outputs flow through an algorithm via Numeric, True/False, Instrument or Variable ports.

**Example:** The Instrument Field block channels a stream of continuous data from an exchange.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-continuous-msg-example.png)

### Discrete event messages

Discrete event messages represent information disseminated from or submitted to an exchange for occurrences of market events that happen at a single moment in time (denoted as Discrete Events). For instance, a Fill Confirmation message from an exchange server is considered to be a discrete event message, as this information is a pulse of data disseminated only at the moment of an order execution.

The following market events are considered to occur at a single moment in time:

* Fill Confirmation
* Order Add Request/Confirmation
* Order Modify Request/Confirmation
* Order Delete Request/Confirmation

Several designated blocks, such as the [Order](../../../trading-blocks/order-block.md) block, may exchange discrete event messages directly with an exchange. When a block submits or receives a discrete event message, it will distribute a copy of the message throughout the rest of the algorithm in the form a single pulse. A discrete event message may flow through an algorithm via discrete event message ports.

**Example:** The Order block is one of several designated blocks in ADL which can submit and receive discrete event messages from an exchange server.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-order-block.png)

Several blocks which do not interact directly with an exchange can also send a pulse of discrete event message throughout an algorithm at user-defined moments. However, as such discrete event messages are not associated with any real requests or confirmations, these messages are void of information and merely provide the function of triggering downstream blocks to perform an action at user-defined moments, such as resetting a block’s continuous output values.

←[Previous PostEdges](edges.md)

[Next PostMessage timing](message-timing.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-continuous-msg-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-order-block.png
