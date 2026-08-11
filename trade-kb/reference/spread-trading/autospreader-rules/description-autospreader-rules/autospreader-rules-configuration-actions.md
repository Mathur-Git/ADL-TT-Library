---
title: Autospreader rules configuration Actions
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-actions/
---

# Autospreader rules configuration Actions

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-actions/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Rule anatomy](../../../../guides/spread-trading-autospreader.md#rule-anatomy)

To complete the rule, you must add an action that will be performed when your conditions are met. Click the
**THEN** add button to add additional actions. The list is based on the rule type you selected:

* If you selected **Quoting Order**, then you’ll see a list of [quote rule actions](#quote-act).
* If you selected **Pre-Hedge Order**, then you’ll see a list of [pre-hedge rule
  actions](#prehedge-act).
* If you selected **Post-Hedge Order**, then you’ll see a list of [post-hedge rule
  actions](#posthedge-act).

### Quote rule actions

If **Quoting Order** is selected as the rule type, **quote order** appears as the rule. After you
select **Set** in the first field, and you can select the following quote order actions in the second field:

* **price of this leg…** — Uses your action logic to override the quoting order price calculated by the
  Autospreader Server.
* **quantity of this leg…** — Uses your action logic
  to decrement the quoting order quantity calculated by the Autospreader Server.

### Pre-Hedge rule actions

Set up a pre-hedge rule for any hedge leg to be evaluated and trigger a rule before sending a hedge order into the
market after a quoting order fill.

If **Pre-Hedge Order** is selected as the rule type, **hedge order** appears as the rule. After you select
**Set** in the first field, and you can select the following hedge order actions in the second field:

* **price of this leg** — Uses your action logic to override the hedge order price calculated by
  Autospreader SE.
* **quantity of this leg** — Uses your action logic to override the hedge order quantity calculated by
  Autospreader SE.
* **type** — Click to select one of the following order types: Limit,
  Market, Post Only, FOK, FAK, IOC, MLM.

* [Limit](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [Market](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [Post Only (Limit)](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [FOK (Fill Or Kill)](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [FAK (Fill And Kill)](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [IOC (Immediate Or Cancel)](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)
* [MLM (Market Limit Market)](../../../basic-order-entry/order-ticket/description-order-ticket/order-types.md)

| **Note:** Autospreader rule order types override hedge order types. For example:  * If the hedge order type is Market and the rule type is Post Only (Limit), Autospreader SE submits the   hedge order   as a Post Only (Limit) order. * If the hedge order type is Post Only (Limit) and the rule type is Market, Autospreader SE submits the   hedge order as a   Market order. |
| --- |

When you select **Forfeit** in the first field and **consider it as** in the second field, the action allows
you to forfeit the respective hedge order, but you must select one of the following options to instruct the
Autospreader Server to update certain properties relating to hedge orders:

* **Submitted but legged**: Instructs the Autospreader® Server to increment [Total Hedges Sent] but not [Total
  Hedges Filled] of the respective hedge leg as if the hedge order was submitted but not filled.
* **Submitted and immediately filled**: Instructs the Autospreader Server to increment [Total Hedges Sent] and
  [Total Hedges Filled] of the respective hedge leg as if the hedge order was actually submitted and filled.

**Note:** If you wish to forfeit a hedge order but have the Autospreader Server “remember” and account for the
un-hedged portion at the next hedging opportunity, use the action **Set the hedge order quantity to…** and set
the hedge order quantity to zero. In this case, do not use the **Forfeit the hedge order and consider it as…**
action.

### Post-Hedge rule actions

Use a post-hedge rule to modify your order if the bid or ask you are leaning on starts to lose value. When
**Post-Hedge Order** is selected as the rule type, you can select the following actions:

* Select **Set** in the first field.
* Select one of the following in the second field:

* **price of this leg** Uses your action logic to override the hedge order price calculated by the
  Autospreader Server.
* **quantity of this leg** Uses your action logic to override the hedge order quantity calculated by the
  Autosprear Server.

### Action logic

After you select an action, enter the action logic using the same leg identifiers and attributes available for
conditions (the action text box also makes intellisense suggestions as you enter your logic). You can also use your
custom variables in your action logic.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rule-action-logic.png)

The logic you define for each action instructs the Autospreader Server to replace or modify its own calculated
price and quantity values. Refer to  [Leg Attributes](../../../order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) for a
description of the leg attributes available in the **Condition** and **Action** text fields.

The following arithmetic expressions and operators can be used when entering your action logic:

* Arithmeric expressions: +, -, /, \*
* Operators: <, >, ≤, ≥

←[Previous PostAutospreader rules configuration Logic](autospreader-rules-configuration-logic.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rule-action-logic.png
