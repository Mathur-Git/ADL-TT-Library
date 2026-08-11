---
title: Creating a routing rule in TT
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/task-routing-rules/creating-a-routing-rule-in-tt/
---

# Creating a routing rule in TT

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/task-routing-rules/creating-a-routing-rule-in-tt/)
>
> **Interpreted in:** [Order Types & Execution § Routing rules](../../../../guides/order-types-and-execution.md#routing-rules)

Using the Routing Rules widget, you can define how orders are routed for your most common order routing scenarios. After a rule is created, validated, and enabled, you can [apply it at order entry](applying-a-routing-rule-in-tt.md).

**Note**: Either an order profile or account is required for each order portion defined for a routing rule. If an order profile is selected, all profile settings are applied to the order portion.

To create a routing rule in TT:

1. Open Routing Rules and click **Edit** at the bottom of the widget.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-step1.png)
2. Click **Add Rule** and select the rule in the panel.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-step2.png)

   You can double-click the rule name to change it as needed.
3. In the order portions panel, double-click in each column to configure the routing rule.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-columns.png)

   Available columns:

   * **Rule** — The name of the routing rule using the order portion.
   * **Use** — Indicates if the order portion is applied at order entry. Click the checkbox to enable/disable the order portion.
   * **Profile** — Customer order profiles available to the user.
   * **Account** — The list of available accounts.

     **Note**: When an order profile is selected, the account associated with the profile is used to route the order portion to the exchange and “Determined by Profile” is shown in the “Account” column.
   * **Portion** — The portion of the total order quantity to assign to a broker or account. At order entry, [the portion is calculated as a ratio of the sum of all portion values](../description-routing-rules/routing-portion-calculations.md) for the rule. This field must contain a positive integer from 1 to 999.

     **Tip**: The “Portion” field is not a percentage, but you can enter values that look like percentages to help understand how the order portions will be split between accounts.
   * **Side** — The types of trades allowed in the account. Select one of the following: Buy, Sell, or Both (the account can be used for for both bids and offers).
4. Click **Add Portion** to split the order routing rule among multiple brokers, customers, or accounts as needed.

   Enter a profile or account, portion, and side for the additional order portion(s).

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-portion.png)
5. Click **Save Changes**.

   The new rule is saved in the rules panel and can be applied at order entry.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-done.png)

[Next PostApplying a routing rule in TT](applying-a-routing-rule-in-tt.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-step1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-step2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-columns.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-portion.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-done.png
