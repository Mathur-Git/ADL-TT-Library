---
title: Estimated Position In Queue (EPIQ)
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq/
---

# Estimated Position In Queue (EPIQ)

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq/)

Estimated Position In Queue (EPIQ) is imperfect since you lack detailed order information. But a conservative estimate can be determined by starting with the quantity at the order’s price when it is entered. Then reduce it by any trades that occur at this price. Then adjust it further downward if the **BidQty** falls below this value.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-epiq-example.png)

The formula in the **Branch0** block is as follows.

`! tradeIsOTC AND tradePrice = MsgInfoExtractor0.limitPrice AND Order0 > 0`

←[Previous PostAdvanced Exit Block Functionality](advanced-exit-block-functionality.md)

[Next PostClip Size Reload Functionality](clip-size-reload-functionality.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-epiq-example.png
