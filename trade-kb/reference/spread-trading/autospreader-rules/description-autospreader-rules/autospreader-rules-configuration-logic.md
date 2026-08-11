---
title: Autospreader rules configuration Logic
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-logic/
---

# Autospreader rules configuration Logic

> Category: **Spread Trading** · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader-rules/description-autospreader-rules/autospreader-rules-configuration-logic/)
>
> **Interpreted in:** [Spread Trading: AutoSpreader, Aggregator, Hedge Manager § Rule anatomy](../../../../guides/spread-trading-autospreader.md#rule-anatomy)

The **Logic** tab contains fields to set conditions and conditional logic for the rule.

### Condition type

Before defining the conditions for applying the rule to each leg, select one of the following condition types in **If the following condition is true for:**

* **ThisLeg** — Only the leg being evaluated must pass the specified condition.
* **ANY legs** — Autospreader iterates over every leg in the spread until it finds one for which the specified condition is true.
* **ALL legs** — Autospreader iterates over every leg in your spread and requires that each leg passes the specified condition.
* **Always execute this rule** — Autospreader always executes the rule action(s) for the selected rule type.

### Condition logic

After selecting a condition type, define a condition using as many expressions as needed. Double-click in the condition text field to enter an expression, or right-click the text field to add a complex expression using AND/OR conditions. After adding AND/OR, right-click the AND or OR to add another AND/OR condition. Expressions can be moved within a condition by clicking the expression to select it and using drag-and-drop to move it.

The rule you create will be applied to a *single* leg of the spread. However, you can reference multiple legs in defining the condition.

**Note**: A rule is “evaluated” per leg, however, multiple legs may be “iterated” as part of evaluating the rule.

There are three leg identifier keywords you can enter in the text field that refer to the leg(s) involved in the expression(s):

* **ThisLeg**. The leg for which the rule is being **evaluated**.
* **Leg**. The leg being **iterated** over as part of the rule for ThisLeg.

  **Note**: Do not use the Leg identifier with the **When the condition is true for this leg** condition type, because this condition type has no implied iteration.
* **Leg#**. The nth leg of the spread regardless of iteration context.

  **Note**: There is currently no validation to prevent you from referencing a non-existent leg (e.g., Leg3 in a two-legged spread).

Enter a leg identifier followed by a “.” to select a leg attribute, such as:

* **CurrentQuoteOrderWorkingPrice** (information pertaining to the current quote / hedge order(s) of the respective leg)
* **BidPrice** (market data pertaining to the respective leg’s market)

When entering a leg identifier, the text field makes “intellisense” suggestions for which leg attribute to use. Refer to  [Leg Attributes](../../../order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference.md) for a description of the leg attributes available in the **Condition** and **Action** text fields.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-rule-typing.png)

To simplify rule construction, you only need to build a rule for the buy (bid) side of the trade. You can then choose to have it automatically reverse when it’s being evaluated from the sell (ask) side.

To automatically switch [Bid]- and [Ask]- attributes, Autospreader® Rules reverses arithmetic expressions ( “+” and “-” operations) and logical operators (<, >, ≤, ≥) as long as they are accompanied by operands and the condition is wrapped in curly brackets “{ }”. For example, the following condition: {ThisLeg.CalculatedQuoteOrderPrice < ThisLeg.BidPrice – ThisLeg.MinimumPriceIncrement}…is converted to the following when evaluated from the sell side: {ThisLeg.CalculatedQuoteOrderPrice > ThisLeg.AskPrice + ThisLeg.MinimumPriceIncrement}

The following arithmetic expressions and operators can be used when entering your condition logic:

* Arithmeric expressions: +, -, /, \*
* Operators: <, >, ≤, ≥

←[Previous PostAutospreader rules configuration](autospreader-rules-configuration.md)

[Next PostAutospreader rules configuration Actions](autospreader-rules-configuration-actions.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/auto-rule-typing.png
