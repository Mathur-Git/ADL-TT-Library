---
title: Algos & Autospreader Preferences
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/algos-autospreader-preferences/
---

# Algos & Autospreader Preferences

> Category: **Overview** · [Source](https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/algos-autospreader-preferences/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § From Algo Dashboard](../../../../guides/algo-ops.md#from-algo-dashboard) · [Platform & Workspace § Preferences](../../../../guides/platform-and-workspace.md#preferences) · [Platform & Workspace § Algos & Autospreader preferences (load-bearing for auto...](../../../../guides/platform-and-workspace.md#algos-autospreader-preferences-load-bearing-for-automated-strategies)

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-algos-auto.png)

| Preference | Description |
| --- | --- |
| Share newly created Aggregator/Autospreader configurations | Checks the **Share** checkbox by default in the configuration dialog box for all newly created synthetic spreads. When a synthetic spread is created after this preference is enabled, the spread will be shared with all users in your company. |
| Algo disconnect action | Select the default action to take when the client that launched the Algo loses its connection to TT:   * **Leave**: Algo orders to remain working. All algo child orders continue to be   managed by the Algo server. * **Pause**: Algo orders are paused. Child order behavior is dependent on the   configuration of each individual Order Block. * **Cancel**: Algo orders are canceled. Child order behavior is dependent on the   configuration of each individual Order Block.    **Note**: These settings apply only to the loss of connection between the client and TT. Child orders will be unaffected during connection problems with an exchange. |
| Autospreader disconnect action | Select the default action to take when the client that submitted the Autospreader order loses its connection to TT:  * **Leave**: Autospreader orders remain working. Quote and hedge orders continue   to be managed by the Autospreader server. * **Cancel**: Autospreader orders are canceled which in turn cancels quote   orders, but hedge orders remain working.    **Note**: These settings apply only to the loss of connection between the client and TT. Child orders will be unaffected during connection problems with an exchange. |
| Auto-launch OMA algos | Whether to launch [order-builder OMAs](../../../algo-trading/order-management-algos-omas/order-management-algos-oma-overview.md), such as the OCO 2 OMA, automatcally when the minimum number of required orders are added. This setting can be overridden on an individual basis by creating an OMA order template. |
| Per-market Account selection for ADL algos | Allows you to enter only one account for multi-leg algos and use that account for orders on all of the legs. |

←[Previous PostFills Preferences](fills-preferences.md)

[Next PostSounds Preferences](sounds-preferences.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-algos-auto.png
