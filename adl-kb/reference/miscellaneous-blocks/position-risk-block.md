---
title: Position Risk block
category: miscellaneous-blocks
source: https://library.tradingtechnologies.com/adl/miscellaneous-blocks/position-risk-block/
---

# Position Risk block

> Category: **Miscellaneous Blocks** · [KB Home](../../README.md) · [Source](https://library.tradingtechnologies.com/adl/miscellaneous-blocks/position-risk-block/)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-block.png)

When a native order is placed by an ADL algo, it is routed to the TT risk system. If it passes the necessary risk checks, it is then routed to a TT component called the Order Connector which then routes it to the exchange. If it does not pass the risk checks done by the TT risk system, it is rejected and the algo is stopped.

ADL developers can use the Position Risk block to have an additional risk check done before the native order is sent to the TT risk system. This is generally done to ensure that an ADL algo instance is stopped if it attempts to go beyond certain limits. You would commonly set the values of limits to be checked by the Position Risk block to be less than a user’s actual risk limits. If you set the values of these limits to be above a user’s actual risk limits, the order will be rejected by the TT risk system.

**Example:** This algo uses two Position Risk blocks to set different maximum long and short limits for the attached instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-short-long.png)

If you enable the Flip for Sell Order property, the limit will apply to the side chosen by the user when the algo is launched.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-fill-for-sell.png)

The behavior of the risk check done by your ADL algo varies depending upon whether it has only a buy Position Risk block, only a sell Position Risk block, or both buy and sell Position Risk blocks for a given instrument / account. Specifically:

Buy Position Risk block only:

* For buy orders, the algo sums the worst-case-position of all buys (fills + working quantity) and checks against this limit. If the check fails, the algo is stopped. If the check succeeds, the order is routed to the TT risk system to be checked against the user’s TT risk limits before being sent to the exchange.
* Sell orders are routed to the TT risk system to be checked against the user’s TT risk limits before being sent to the exchange.

Sell Position Risk block only:

* For sell orders, the algo sums the worst-case-position of all sells (fills + working quantity) and checks against this limit. If the check fails, the algo is stopped. If the check succeeds, the order is routed to the TT risk system to be checked against the user’s TT risk limits before being sent to the exchange.
* Buy orders are routed to the TT risk system to be checked against the user’s TT risk limits before being sent to the exchange.

Both:

* The algo sums the worst-case-position of all buys and sells (fills + working quantity) and checks all buy/sell orders against this limit. If the check fails, the algo is stopped. If the check succeeds, the order is routed to the TT risk system to be checked against the user’s TT risk limits before being sent to the exchange.

### Position Reserve Orders

ADL developers can gain a significant performance boost by enabling the “Enable Position Reserve” option when using the Position Risk block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-block-enable-pr.png)

When enabled, the ADL algo, upon being launched, will send a separate Position Reserve order to the TT risk system for each Position Risk block to reserve a specified amount of position risk. Any subsequent native orders that are sent by the ADL algo will undergo a risk check by the Position Risk block to confirm that they do not exceed the limits specified. If this check succeeds, the native order is then routed directly to the TT Order Connector bypassing the TT risk system.

**Note:** Attempts to reserve risk from the TT risk system that is greater than a user’s available risk will be rejected and the algo will be stopped.

**Note:** Use of Position Reserve orders is restricted to dedicated Algo Servers. Their use is not available on gen-pool Algo Servers.

### Block properties

To customize the block, update the **Block Properties**.

| Property | Description |
| --- | --- |
| Name | Name to display beneath the block on the ADL canvas |
| Side | Whether the block represents a limit for a long or short position. |
| FlipForSell | Whether to use the same limit for buy and sell orders.  See [Flip For Sell Orders Functionality](../adl-overview/advanced-concepts/description/flip-for-sell-order-functionality.md) for more information. |

←[Previous PostPnl block](pnl-block.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-short-long.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-fill-for-sell.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/mb-position-risk-block-enable-pr.png
