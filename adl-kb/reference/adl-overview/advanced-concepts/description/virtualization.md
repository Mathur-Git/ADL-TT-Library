---
title: Virtualization
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/virtualization/
---

# Virtualization

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/virtualization/)
>
> **Interpreted in:** [Core Semantics § 7. Virtualization](../../../../guides/core-semantics.md#7-virtualization) · [Design Patterns & Recipe Index § Exits and position management](../../../../guides/design-patterns.md#exits-and-position-management) · [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Cross-references](../../../../../trade-kb/guides/spread-trading-autospreader.md#cross-references)

### Virtualization

Virtualization is a property that can be applied to a designated portion of an algorithm to allow multiple “copies” of the designated portion to be created and executed simultaneously. While the concept may sound complex, the necessity of virtualization becomes clear when examined through an example.

1. Suppose that a user designs and runs a simple market making algorithm in E-Mini S&P 500 contract as shown in the following illustration.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex1.png)
2. Suppose that the current best bid price is 1313.75, and the entry logic of the algorithm quotes 10 entry side contracts at this price. Then 1 out of the 10 contracts is filled for 1313.75. In response, the exit logic of the algorithm offers 1 contract at 1314.25, two increments higher than the fill price.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex2.png)
3. Suppose that the market moves higher and the best bid price changes to 1314.00. The offset contract from Step 2 still rests at 1314.25 but the entry logic of the algorithm modifies the remaining 9 entry side contracts to 1314.00. Then 2 out of the 9 entry side contracts get filled for 1314.00. At this time, the algorithm’s total fill count is 3, including the first partial fill from Step 2. Since the algorithm’s exit side logic was designed to use the total fill count and only the most recent fill price, it offers 3 offset contracts at 1314.50, two increments higher than the most recent fill price. In addition, since the exit logic of the algorithm can only quote a single order at time, it deleted the offset contract resting at 1314.25 (from Step 2).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex3.png)

   To avoid this undesirable behavior, the user may virtualize the exit logic of this algorithm. With virtualization, a new copy of the exit logic is created every time an entry side fill occurs so that each offset order can operate with independent logic.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex4.png)

   By virtualizing a group of blocks, the user can arrange for a new copy of the group to be created every time a designated discrete event (e.g., fill) occurs. To be specific, the user must group a set of blocks, virtualize the group, and then link a discrete event message pathway into the virtualized group block. Whenever a discrete event message enters the virtualized block via this pathway, a fresh copy is created, with each copy operating independently of others. Each copy, while identical in the composition of blocks, can operate independently with unique inputs and outputs.

**Note:** **Because multiple copies of a virtualized block can exist at the same time, the Designer Canvas will not always display the correct dynamic output values of the blocks contained within a virtualized block.**

←[Previous PostOrder Stack Logic with Flip for Sell functionality](order-stack-logic-with-flip-for-sell-functionality.md)

[Next PostOrder of discrete event message propagation](order-of-discrete-event-message-propagation.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/concepts-virtualization-ex4.png
