---
title: Recovery And Server Maintenance
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/recovery-and-server-maintenance/
---

# Recovery And Server Maintenance

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/recovery-and-server-maintenance/)
>
> **Interpreted in:** [Core Semantics § 11. Recovery and server maintenance](../../../../guides/core-semantics.md#11-recovery-and-server-maintenance)

TT has developed a new feature to automatically restart ADL algos following Algo Server maintenance restarts. Algo Servers in simulation are restarted Monday through Friday at 4:15PM Chicago time. Algo Servers in production may or may not restart on weekends if maintenance is required.

### Recovery Behavior

All ADL algos will be recovered back to the state in which they existed prior to the restart with the exception of those which contain one or more Order blocks configured to drive Autospreader / Aggregator orders. For these, recovery will fail.

In addition, it should be noted that the state of ADL algos that are designed to fire periodic non-exchange discrete events while the Algo Server is being restarted may be inaccurate or fail after being restarted. Algos designed in this manner should be stopped before weekend maintenance begins.

←[Previous PostADL and TT Mobile](adl-and-tt-mobile.md)
