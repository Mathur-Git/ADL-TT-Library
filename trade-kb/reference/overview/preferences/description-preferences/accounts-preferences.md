---
title: Accounts Preferences
category: Overview
source: https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/accounts-preferences/
---

# Accounts Preferences

> Category: **Overview** · [Source](https://library.tradingtechnologies.com/trade/overview/preferences/description-preferences/accounts-preferences/)
>
> **Interpreted in:** [Platform & Workspace § Preferences](../../../../guides/platform-and-workspace.md#preferences)

![Account preferences dialog](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-accounts2.png)

### Display

| Preference | Description |
| --- | --- |
| Accounts assigned to me | Display only accounts assigned to the user in list boxes and dropdowns for widgets that display accounts. |
| All accounts visible to me | For users with administrator rights, display all accounts in the company in list boxes and dropdowns for widgets that display accounts. |

## Routable Accounts

Accounts are downloaded from the Setup database, and the account and exchange data displayed in Preferences is read-only. Accounts assigned to you are displayed in this section if they are configured as “Routable” in the Setup app. Any accounts configured as “Non-Routing” are not displayed.

Using radio buttons in the **Routable Accounts** section, you can select one of the following viewing options:

* **Account**
* **Exchange**
* **RFQ**

When the **Account** view is selected, a table is displayed with accounts in the first column, and exchange connections that each account is assigned to shown in the third column. User-defined account aliases are shown in the second column when viewing by account. The Account view is displayed by default.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-view2.png)

When the **Exchange** view is selected, a table is displayed with exchange connections assigned to accounts in the fist column, and a listing of each account assigned to the exchange connections in the second column. User-defined account aliases are shown in the third column when viewing by exchange. In both views, the column widths can be adjusted.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-exchange-view2.png)

Use the **Alias** column in both views to enter an alias name for identifying an account. When the account list is displayed in order entry widgets, the alias name is prepended to the actual
account name in parentheses. To add or modify an alias, double-click a cell in the **Alias** column and enter an alias name.

## RFQ Routing Accounts

Using the **RFQ** view, you can assign specific exchanges to accounts for submitting RFQs. When sending an RFQ for any instrument from a widget in TT, the RFQ is automatically routed to the exchange using the account set in your workspace preferences.

To assign an exchange to an RFQ routing account, enable the **RFQ** radio button, double-click in the **Exchanges** column for an account row and select one or more exchanges. When finished, click **OK** and save the changes.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-rfq.png)

When assigning an exchange to an RFQ routing account, consider the following:

* You can set one of the accounts as the “Default” account for routing all RFQs. When submitting an RFQ, accounts are selected in TT from specific (exchange name) to general (default). If no specific exchange is assigned to an account in your preferences, the “default” account is selected.
* Multiple exchanges can be assigned to the same account. After an exchange is assigned to an account, it cannot be assigned to other accounts.

An RFQ can be submitted from the following widgets in TT:

* Market Grid
* Watchlist
* Strategy Creation
* Blocktrader (exchange specific)
* Options Chain
* RFQ Viewer (resend)

**Note**: If you do not select an RFQ routing account prior to submitting the RFQ, you’ll receive the following widget error message:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-rfq-error2-3.png)

←[Previous PostGeneral Preferences](general-preferences.md)

[Next PostOrders Preferences](orders-preferences.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-accounts2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-view2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-exchange-view2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-rfq.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/wrk-preferences-account-rfq-error2-3.png
