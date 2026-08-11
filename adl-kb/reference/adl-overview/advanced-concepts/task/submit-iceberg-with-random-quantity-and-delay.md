---
title: Submit Iceberg with Random Quantity and Delay
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/submit-iceberg-with-random-quantity-and-delay/
---

# Submit Iceberg with Random Quantity and Delay

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/submit-iceberg-with-random-quantity-and-delay/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry) · [Order Types & Execution § The ADL bridge](../../../../../trade-kb/guides/order-types-and-execution.md#the-adl-bridge)

An Iceberg order executes a large volume order by breaking it into smaller disclosed orders, publicly displaying only
the specified portion instead of the full order quantity.

The ADL Canvas below shows how the user can define the values for the child order quantities (i.e., 3-10) and the
delay values (i.e., 300-1500 milliseconds) to randomize these values. The algo leverages the [State block](../../../discrete-blocks/state-block.md) to determine the fill status.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-submit-iceberg-random-qty-delay.png)

←[Previous PostSubmit Orders Between Specific Start/Stop Times](submit-orders-between-specific-start-stop-times.md)

[Next PostCreating Uptick and Downtick Counters](creating-uptick-and-downtick-counters.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-submit-iceberg-random-qty-delay.png
