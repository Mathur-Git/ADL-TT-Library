---
title: Displaying Accumulated or Unaccumulated LTQ
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/displaying-accumulated-or-unaccumulated-ltq/
---

# Displaying Accumulated or Unaccumulated LTQ

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/displaying-accumulated-or-unaccumulated-ltq/)

Unaccumulated LTQ is simply the most recent LTQ. Accumulated LTQ is a summation of all LTQs that occur at a given LTP while the LTP remains unchanged.

For example, consider the following trades: LTP = 100, LTQ = 3LTP = 99, LTQ = 4LTP = 99, LTQ=7LTP = 99, LTQ=1
At this point, an unaccumulated LTQ would be displayed as 1 whereas an accumulated LTQ would display as 12 (4+7+1). In 7x, TT Price Servers could be configured to deliver LTQ as accumulated or unaccumulated. As such, the LTQ displayed in ADL would be accumulated or unaccumulated based on this setting. In TT, TTW displays an accumulated LTQ. However, TT ADL displays an unaccumulated LTQ. If desired, ADL designers can calculate the accumulated LTQ as follows

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-accumulated-unaccumulated-ltq.jpg)

For more information and LTP/LTQ in ADL, refer to the documentation on the [Field Block](../../../trading-blocks/field-block.md).

←[Previous PostAlgo sharing](algo-sharing.md)

[Next PostAdvanced Exit Block Functionality](advanced-exit-block-functionality.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-accumulated-unaccumulated-ltq.jpg
