---
title: Care order account permissions and ownership
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-order-account-permissions-and-ownership/
---

# Care order account permissions and ownership

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-order-account-permissions-and-ownership/)

The risk administrator at your firm sets the [order permissions for submitting and managing care orders](https://library.tradingtechnologies.com/user-setup/ac-staged-order-permissions.html) per account or user. The risk administrator also configures risk settings for the execution accounts used for submitting child orders related to the parent care order.

**Note**:

* Staged orders themselves do not contribute to risk. Only child orders do.
* Position-based risk limits are on the account-level only, so limits on the routing user-level have no influence.
* Account user permission and max order quantity checks are based on the account/user. In the case of staged child orders, this will always be based on what are set on the claiming\_user\_id and routed child account, which are not necessarily always the same as the original user\_id and staged order account.

The account used for staging the order can be assigned to multiple users in the same company or shared with users in a different company. If a user will be staging an order into an account that needs visibility outside of your company, the account needs to be shared using using the Setup application in TT.

**Note**: You can stage orders or submit manual fills for these orders using accounts without active connections configured in Setup. These “stage only” accounts must also have order permissions set for submitting and/or managing staged (care) orders.

The following table shows the order actions allowed for users based on their care order and execution account ownership.

| User | Account | Actions | Comments |
| --- | --- | --- | --- |
| Originator | Care order account | * Submit/view care order * Cancel or change care order with approval from owner | Originator must have permission to submit care orders in this account.  When a care order is submitted, the originator’s risk limits are applied.  Both the originator and owner have visibility of the orders and fills in the care order account. Other users assigned to the account can view the care order and its current status. |
| Same execution account as owner | * View related child orders | Originators have visibility of execution accounts that are shared with them or are child accounts of the care order account, but cannot modify the child orders submitted by the owner. |
| Owner | Care order account | * Claim/unclaim care order * Cancel care order * Approve the cancel or change request of originator | Owner must have order permissions set for managing care orders in this account.  Both the originator and owner have visibility of the orders and fills of the care order account.  The owner can submit child orders using the care order account or other execution accounts they have access to. Native order permissions must be enabled on this account. It may be necessary to submit multiple child orders in the same account to fill a parent order.  Other users assigned to the account can view the care order and its current status, but cannot execute child orders on behalf of the care order while it is controlled by the owner. All non-care orders are also visible to users assigned to the account.  Owners can add a manual fill for all or part of a care order without sending a child order to the exchange.  Owners can assign fills from their own inventory for all or part of a care order. |
| Execution account | * Submit related child orders * Modify related child orders * Cancel related child orders | The owner who claims the care order can submit child orders in execution accounts, which are separate from the care order account. Native order permissions must be enabled on these accounts. It may be necessary to submit multiple child orders in different accounts to fill a parent order.  Owners often share an account with the originator for care orders and use their own accounts for order execution. These accounts can be sub-accounts of the care order account, or separate accounts independent of the care order account.  If the owner claiming the care order uses their own accounts to submit child orders, the originator will not have visibility of the owner’s accounts. However, fills from the execution accounts will be visible to the originator in the care order account. Child orders submitted using the owner’s execution accounts are tagged with an identifier that relates the child orders back to the parent care order.  The risk limits on the owner’s execution accounts, as well as any parent accounts of those execution accounts, are checked when the owner submits child orders in those accounts on behalf of a care order. |

←[Previous PostOrder Exceptions Widget](order-exceptions-widget.md)

[Next PostCare Order Management](care-order-management.md)→

