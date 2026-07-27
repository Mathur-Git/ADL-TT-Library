---
title: Algo deployment and approvals
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals/
---

# Algo deployment and approvals

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals/)

After you begin developing an algo in ADL, you can save it at any point. When an algo has been tested, you can deploy
the algo to make it available in Trade widgets, such as [Algo
Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md), [Autotrader](../../../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md), and [MD Trader](../../../../../trade-kb/reference/basic-order-entry/md-trader/description-md-trader/md-trader-overview.md). Once deployed, algos are available for execution until they are
undeployed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-illustration.png)

Selecting **Deploy** from the **File** menu, deploys an algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-algo-confirmation.png)

### Algos requiring approval

Some companies might require your algos to go through an approval process, such as to meet regulatory requirements,
before they can be used for trading in the Live environment. If a company administrator enables the **Requires
Permission to Run Own Algos** setting in [Setup](https://library.tradingtechnologies.com/user-setup/us-user-algo-management.html) for
you, any algos you deploy must be approved before they appear in Trade widgets. When you are configured as such,
selecting **Request Approval** in the **File** menu for an algo displays a dialog similar
to the following that requires you to request approval from each company that requires it.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-approval.png)

Clicking **Request Approval** will deploy the algo in the Simulation environment. To submit an algo for
approval in the Live environment, select the desired companies before clicking **Request Approval**.

Only after an algo is approved will the algo be available to use in the Live environment. If you already have an open
workspace, you need to refresh the algo list in the [Algo
Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) to make it visible.

**Note**: If your [Setup](https://library.tradingtechnologies.com/user-setup/us-adding-a-new-user.html) administrator requires
algo approval for your algos after your algos have been deployed, the algos will be removed from Trade widgets. In
such cases, you will need to submit a request for approval of each algo.

### Undeploying algos

Selecting **Undeploy** from the **File** menu removes the algo from all TT widgets. To use
the algo again, you must redeploy it.

←[Previous PostUser-defined variables](user-defined-variables.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-illustration.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-algo-confirmation.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deploy-approval.png
