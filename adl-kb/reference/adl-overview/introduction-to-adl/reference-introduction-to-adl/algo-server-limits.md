---
title: Algo Server limits
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/reference-introduction-to-adl/algo-server-limits/
---

# Algo Server limits

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/introduction-to-adl/reference-introduction-to-adl/algo-server-limits/)
>
> **Interpreted in:** [Gotchas, Hard Limits & Platform Constraints § Algo Server capacity](../../../../guides/gotchas-and-limits.md#algo-server-capacity) · [Platform & Workspace § Algos & Autospreader preferences (load-bearing for auto...](../../../../../trade-kb/guides/platform-and-workspace.md#algos-autospreader-preferences-load-bearing-for-automated-strategies) · [Platform & Workspace § Mock trading and UAT — the two pre-production environments](../../../../../trade-kb/guides/platform-and-workspace.md#mock-trading-and-uat-the-two-pre-production-environments)

### Algo Servers in Production

The number of algos you can run simultaneously is limited as follows:

* Aurora: at least 100 instances of ADL algos and 100 instances of TT order types but possibly as many as 400 instances of ADL algos and 400 instances of TT order types depending upon system load.
* Bangkok: 100 instances of ADL algos and 100 instances of TT order types.
* All other co-location facilities: at least 100 instances of ADL algos and 100 instances of TT order types but possibly as many as 200 instances of ADL algos and 200 instances of TT order types depending upon system load.

If you have any questions or are interested in a dedicated Algo Server deployed on a TT Reserved instance, please contact your TT Customer Success representative.

### Algo Servers in TT’s Test Environments

In an effort to ensure the equitable distribution of system resources, TT sets messaging limits for each instance of an ADL algo running in TT’s test environments. TT’s test environments include the [User Acceptance Testing (UAT)](https://uat.trade.tt/) and [simulation](https://trade.tt/sim) environments.

The messages that count towards this limit are any new order, change order, and cancel order messages sent by the ADL algo. If the cumulative number of these messages exceeds 200 in any given second, the algo will be stopped automatically by the Algo Server. An appropriate message will also be sent to the TT Audit Trail.

**Note**: In addition, users may run up to 25 instances of ADL algos and 25 instances of TT order types per region simultaneously. This limit may be higher depending upon system load.

These limits do not apply to Algo Servers deployed on TT Reserved instances. If you have any questions or are interested in a dedicated Algo Server deployed on a TT Reserved instance, please contact your TT Account Executive.
