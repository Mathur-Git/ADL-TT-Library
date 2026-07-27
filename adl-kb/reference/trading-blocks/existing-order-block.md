---
title: Existing Order block
category: trading-blocks
source: https://library.tradingtechnologies.com/adl/trading-blocks/existing-order-block/
---

# Existing Order block

> Category: **Trading Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/trading-blocks/existing-order-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block.png)

The Existing Order block is a trading block that allows an Order Management Algorithm to take control of an existing order. An Existing Order block works in conjunction with a [Single Order Container](single-order-container-block.md) block to manage the order using the following process:

1. When an Existing Order block takes control of an order, it generates a discrete event message containing the respective order key.
2. The discrete event message enters the connected Single Order Container.
3. The container retrieves the order key from the discrete message and takes control of the identified order.

**Example 1:** **An Existing Order block recieves information about the order to which the algo has been applied. The Existing Order block generates a discrete message containing the order’s information which downstram blocks can use to control the order.**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-intro.png)

**Example 2:** **Using an Existing Order block to join the offer**

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-intro-1.png)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-example.png)

### Applying Order Management Algorithms

Applying the Existing Order block functionality to an existing order is referred to as creating an Order Management Algorithm (OMA). The following rules govern the behavior of OMAs:

* During the application process, the OMA will not disrupt the priority of the working order, but the OMA will have the authority to modify or delete the order after the application.
* An OMA can be applied to the child order of another OMA.

After saving and deploying an Order Management Algorithm to an Algo server, it can be applied to an existing order through the [Order Book](../../../trade-kb/reference/order-management/order-book/description-order-book/order-book-overview.md) widget.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |

←[Previous PostOrder block](order-block.md)

[Next PostDiscrete Order block](discrete-order-block.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-intro-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/tb-existing-order-block-example.png
