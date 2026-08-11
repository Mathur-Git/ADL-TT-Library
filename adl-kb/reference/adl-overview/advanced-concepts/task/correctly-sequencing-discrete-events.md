---
title: Correctly Sequencing Discrete Events
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/correctly-sequencing-discrete-events/
---

# Correctly Sequencing Discrete Events

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/correctly-sequencing-discrete-events/)
>
> **Interpreted in:** [ADL Block Catalog § Sequence →](../../../../guides/block-catalog.md#sequence-ref) · [Core Semantics § 4. Branching a discrete output is non-deterministic](../../../../guides/core-semantics.md#4-branching-a-discrete-output-is-non-deterministic)

Although it is possible to connect more than one edge to the discrete output port of a given block, it is not advisable. For example, consider the following ADL algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-event-sequencing-base-algo.png)

Upon the first fill, if the path to the **MsgInfoExtractor0** block is executed first followed by the path to the **MsgInfoExtractor1** block, the output of the **ValueExtractor0** block will equal the value of the output of the **MsgInfoExtractor0** block since the value of the **MsgInfoExtractor1** block will be zero.

However, upon the first fill, if the path to the **MsgInfoExtractor1** block is executed first followed by the path to the **MsgInfoExtractor0** block, the output of the **ValueExtractor0** block will equal the value of the output of the **MsgInfoExtractor0** block plus the value of the output of the **MsgInfoExtractor1** block. The actual path that is chosen first by the Algo Server execution logic is not always deterministic.

To force a deterministic path of execution, simply insert a **Sequence** block immediately downstream of the discrete output port and choose the sequence that makes sense for your algo. For example, consider this modified algo:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-event-sequencing-correct.png)

Notice now that the path to the **MsgInfoExtractor1** block will always be executed first followed by the path to the **MsgInfoExtractor0** block. As such, upon the first fill, the output of the **ValueExtractor0** block will equal the value of the output of the **MsgInfoExtractor0** block plus the value of the output of the **MsgInfoExtractor1** block, which is what was intended.

←[Previous PostHandling External Events](handling-external-events.md)

[Next PostSubmit Orders Between Specific Start/Stop Times](submit-orders-between-specific-start-stop-times.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-event-sequencing-base-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-event-sequencing-correct.png
