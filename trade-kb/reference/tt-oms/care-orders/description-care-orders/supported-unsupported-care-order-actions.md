---
title: Supported/Unsupported Care Order Actions
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/supported-unsupported-care-order-actions/
---

# Supported/Unsupported Care Order Actions

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/supported-unsupported-care-order-actions/)

The TT Platform will prevent a user from attempting to perform OMS actions that are not supported. The Order Book and OFW does not allow the following actions:

* “Unbulk” a bulked order with fills (the fills must be unassigned from the bulk before it can be unbulked).
* “Unstitch” a stitched order with fills (the fills must be unassigned from the stitch before it can be unstitched).
* Using the “Split” feature on: (a) Care orders with working child orders, (b) Bulked orders (an order must be removed from a bulk before it can be split), (c) Stitched orders, and (d) previously Split orders (a care order can only be split once).

←[Previous PostCare Order Management](care-order-management.md)

