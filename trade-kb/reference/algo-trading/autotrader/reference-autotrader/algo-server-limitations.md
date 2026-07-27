---
title: Algo Server limitations
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/autotrader/reference-autotrader/algo-server-limitations/
---

# Algo Server limitations

> Category: **Algo Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/algo-trading/autotrader/reference-autotrader/algo-server-limitations/)

The number of algos you can run simultaneously is limited as follows:

* Aurora: at least 100 instances of ADL algos and 100 instances of TT order types but possibly as many as 400 instances of ADL algos and 400 instances of TT order types depending upon system load.
* Bangkok: 100 instances of ADL algos and 100 instances of TT order types.
* All other co-location facilities: at least 100 instances of ADL algos and 100 instances of TT order types but possibly as many as 200 instances of ADL algos and 200 instances of TT order types depending upon system load.

**Note**: In the simulation and user acceptance testing (UAT) environments, users may run up to 25 instances of ADL algos and 25 instances of TT order types per region simultaneously. This limit may be higher depending upon system load. These limits do not apply to Algo Servers deployed on TT Reserved instances.

If you have any questions or are interested in a dedicated Algo Server deployed on a TT Reserved instance, please contact your TT Customer Success representative.

←[Previous PostAutotrader reference](autotrader-reference.md)

