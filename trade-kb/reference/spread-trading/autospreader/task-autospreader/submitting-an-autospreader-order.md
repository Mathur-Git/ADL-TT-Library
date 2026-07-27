---
title: Submitting an Autospreader Order
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-an-autospreader-order/
---

# Submitting an Autospreader Order

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/autospreader/task-autospreader/submitting-an-autospreader-order/)

You can submit synthetic spread orders the same way as you submit orders for exchange-traded instruments. For example, you can submit the spread order in MD Trader by specifying the order type, TIF and quantity and clicking a price level, as shown. In this example, the spread is configured to submit quoting orders for both legs.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-new-order.png)

## Submitting an Autospreader order using multiple accounts

The Autospreader MD Trader spread panel provides you with the ability to select separate accounts for routing the child orders of a parent spread order. For example, you can use separate accounts on different exchanges to submit orders for cross-exchange spreads, or split trading between separate accounts and different brokers.

When you launch a spread, the legs are seeded automatically based on any order default [account settings](https://library.tradingtechnologies.com/trade/win-reference.html#account-settings) you may have configured. The default accounts may also be different per leg.

To submit an Autospreader order using multiple accounts:

1. Click the account selector in the MD Trader spread panel and select **Multi…**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account1.png)
2. In the flyout panel that appears, click the account selector for each leg and select an account.

   Your default account displayed in **All Legs** is used for routing the leg orders.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account2.png)

   When you select a different account for each leg, then **Multi…** appears in **All Legs** and each separate account is displayed for **Leg 1** and **Leg 2**, etc.

   **Note:** Autospreader leg orders use the accounts from each leg when in Multi account mode.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account2a.png)
3. Configure and submit the spread order in the MD Trader spread pane.

   After submitting the order, the flyout panel closes and the spread, quoting, and hedge orders are submitted into the market. The leg orders are routed using the different accounts you selected.

   If you hover on the account selector in the MD Trader spread panel, a tooltip appears and displays your account selections for each leg.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account3a.png)

## Submitting an Autospreader order using multiple accounts per leg

When Autospreader is configured with an Aggregator as a leg instrument, TT supports sending multiple accounts per leg. TT sets the account of the Autospreader parent order using the **Leg 1 acct** field.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-multi-agg-leg.png)

When the first leg of the spread is an Aggregator with multiple accounts, then TT sets the account of the parent Autospreader order with Aggregator’s “Leg 1” account. For each Aggregator leg, you can then select **Multi** for **All Legs** and configure separate accounts per leg as needed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-multi-agg-leg2.png)

## Using the open/close functionality in Autospreader

For exchanges that allow you to indicate whether an order opens or closes a position, you can use the MD Trader Open/Close functionality in Autospreader.

The Open/Close setting can be applied per leg using the same account or multiple accounts. If one or more of the legs is an aggregated instrument, the setting can be applied to each instrument leg and account. When the Open/Close setting is applied to a parent order, the setting is also applied to all related child orders.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-as-agg.png)

## Changing the clearing account for each leg of an Autospreader order

Optionally, you can enter your own exchange clearing account value when submitting an order.

**Note**: Before entering your own value, ensure that your administrator has allowed you to override the exchange
clearing account value in Setup.

To enter your own clearing account value at order entry, check the **Show Exchange Clearing Account edit box**
setting in **Preferences** | **Orders**. When this setting is enabled, order entry widgets display an edit box
where you can enter the exchange clearing account. When you click the **Clearing Acct** edit box to enter a
value, it stores and displays a list of the most recent clearing account values you entered.

Prior to submitting the order, you can change the exchange clearing account “on-the-fly” for each leg of an Autospreader order by clicking **Multi…** in the account selector in the MD Trader spread panel. In the flyout panel that appears, enter a clearing account value in the *Exch Acct* edit box for each leg as needed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-account-change.png)

After submitting the order, the **ClearingAcct** column in the Order Book, Fills, or Audit Trail widget shows the value sent to the exchange as the clearing account. The **Account** column in these widgets shows the account you selected at order entry, but this account is not sent to the exchange if you enter your own exchange clearing account.

## Deleting parent spread orders

Using the Floating Order Book, you can delete a parent spread order and leave the child order(s) working in the market. For more details about how to abandon Autospreader child orders, refer to [Deleting parent orders in the Floating Order Book](../../../order-management/floating-order-book/task-floating-order-book/deleting-parent-orders-in-the-floating-order-book.md).

←[Previous PostLaunching a Synthetic Spread](launching-a-synthetic-spread.md)

[Next PostSubmitting a Reload Order](submitting-a-reload-order.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-new-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account2a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-multi-account3a.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-multi-agg-leg.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/as-multi-agg-leg2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oc-as-agg.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/autospreader-account-change.png
