---
title: Message timing
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/message-timing/
---

# Message timing

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/message-timing/)

A discrete event message occurs at a single point in time and can be used to capture market data at that precise moment.

Discrete event messages have a key characteristic: when a block outputs a pulse of discrete event message, an algorithm temporarily stops channeling continuous messages from the exchange servers. Continuous message channels will remain closed while the pulse of discrete event message propagates throughout the algorithm. In effect, this behavior will “freeze” the output of blocks such as the Instrument Field block which channels streaming market data. In this static state, the pulse of discrete event message will traverse the pathway designed by the user, updating the output values of the blocks which lie in its path, allowing the user to capture and use the market data existing precisely at the moment of a discrete event.

Once this propagation is complete, the algorithm will resume channeling continuous messages from all exchange servers.

The following is a simplified illustration of this mechanism in effect:

* The diagram below shows an example of an Instrument [Field block](../../../trading-blocks/field-block.md) (yellow block on the left) channeling a continuous numeric value into the [Order block](../../../trading-blocks/order-block.md) (blue block on the right). The Instrument Field block channels the best bid price of an instrument specified by the user, and the Order block uses this streaming data to quote buy orders at the best bid price for the specified instrument with the specified quantity (instrument and quantity inputs are not shown in the illustration).

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-1.png)
* When one or more of the quoted orders are executed, the Order block receives a Fill Confirmation message from the exchange server and outputs a discrete event message in the form of a single pulse. At this time, the algorithm stops channeling continuous messages from the exchange server. The pulse of discrete event message propagates through the algorithm, following the pathway designed by the user. It updates the output values of the blocks which lie in its path.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-2.png)
* Once the propagation is complete, the algorithm resumes channeling continuous messages from the exchange server.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-3.png)

←[Previous PostContinuous vs. discrete event messages](continuous-vs-discrete-event-messages.md)

[Next PostUser-defined variables](user-defined-variables.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/precision-timing-3.png
