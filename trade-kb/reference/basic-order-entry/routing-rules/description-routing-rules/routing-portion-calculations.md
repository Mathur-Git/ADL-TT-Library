---
title: Routing portion calculations
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/description-routing-rules/routing-portion-calculations/
---

# Routing portion calculations

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/description-routing-rules/routing-portion-calculations/)
>
> **Interpreted in:** [Order Types & Execution § Routing rules](../../../../guides/order-types-and-execution.md#routing-rules)

When a routing rule is applied to an order, the total order quantity is divided based on the Buy/Sell portions assigned in the selected routing rule.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example.png)

When calculating order portions, the routing rule logic does the following:

* For a Buy order, all order portions with a **Side** of “Sell” are excluded from the order
  portion calculations on the order.
* For a Sell order, all order portions with a **Side** of “Buy” are excluded from the portion calculations.
* All portions with a **Side** of “Both” are included in the portion calculations.
* The ratio for each order portion is calculated as a percentage of the sum of the rule’s
  total order portions.




* The order quantities are rounded to best achieve the target ratios.
* Any remaining order portions are randomly sorted prior to applying the ratio calculations to ensure that leftover quantities are assigned with equal fairness.

## Portion ratios for disclosed quantities

If a parent TT Order Type slicer (e.g., TT Time Sliced, TT Volume sliced) order is submitted using a routing rule that splits it across multiple accounts and customers, the order portion ratios are applied to both the total order quantity and the child order disclosed quantities with the following restrictions:

* After calculating the total order quantity for each slicer portion, the disclosed quantity of slicer must be at least 1. For example, if a 10 lot slicer set to disclose “1” at a time is split equally across two accounts, then the rule produces two 5 lot slicers that each disclose “1” at a time.
* The disclosed quantity cannot exceed the total quantity for each slicer.

## Routing Rule Example

In this example, a broker creates “New Rule 2” to split orders among three user accounts.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example-rule.png)

The broker submits a Buy order for 10 lots, so the “Sell” side portion of 10 is ignored in routing rule “New Rule 2”.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example-buy.png)

The rule logic splits the order based on the remaining order portions as follows:

* A.111 account: Portion/sum of all portions = 30/40 = 75% of total order quantity = .75(10)
* 12345 account: Portion/sum of all portions = 10/40 = 25% of total order quantity = .25(10)

The remaining order portion is sorted randomly and assigned to account “12345”. The total order quantity of “10” is split into quantities of “8” and “2” based on the routing rule.

←[Previous PostRouting Rules Display](routing-rules-display.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example-rule.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-example-buy.png
