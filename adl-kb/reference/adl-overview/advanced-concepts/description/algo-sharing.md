---
title: Algo sharing
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/algo-sharing/
---

# Algo sharing

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/algo-sharing/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § Sharing](../../../../guides/algo-types.md#sharing) · [Algo Ops: Dashboard, Autotrader & Excel § Algo Dashboard vs Autotrader](../../../../../trade-kb/guides/algo-ops.md#algo-dashboard-vs-autotrader) · [Algo Ops: Dashboard, Autotrader & Excel § Built-in algos (not ADL)](../../../../../trade-kb/guides/algo-ops.md#built-in-algos-not-adl)

After developing and testing an algo, you might want to allow other users to use the algo for trading. ADL’s algo sharing feature allows you to grant permission to other users to execute your algo and open the algo in ADL. When you share an algo with other users for execution, the algo automatically appears in their list of available algos in [Algo Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md). If the algo is an [Order Ticket Algo (OTA)](order-ticket-algos-ota.md) or [Synthetic Order Algo (SOA)](synthetic-order-algos-soa.md), the algo also appears in the list of public algos in Trade widets, such as [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md).

### Algo sharing permissions

When you [share an algo](../task/managing-shared-algos.md), you can set one or both of the following permissions for those users:

* **View in ADL (but not edit)**: Allows the user to open the shared algo in ADL with read-only permissions.
* **Launch**: Allows the user to run the shared algo within TT. However, the user cannot open the algo in ADL.

**Note**: Users can send an approval request for an algo without needing to open the algo in the ADL canvas.

### Algo sharing restrictions

TT imposes the following restrictions for shared algos:

* You must know the email address of each user with whom you want to share an algo.
* If the same email address is shared over different companies, whether active or inactive, then this will default to the first company this was set up. You will need to speak with the other company’s administrator to delete the user from within TT Setup before sharing the ADL algo to the same email address under the new company.
* If a user with whom you share an algo requires approval to run algos in Setup, that user will need to [request approval](../../adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md) to run the algo. In this situation, you will need to enable Read permission for that user.

←[Previous PostExport block output values](export-block-output-values.md)

[Next PostDisplaying Accumulated or Unaccumulated LTQ](displaying-accumulated-or-unaccumulated-ltq.md)→
