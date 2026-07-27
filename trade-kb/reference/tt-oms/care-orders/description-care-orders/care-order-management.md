---
title: Care Order Management
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-order-management/
---

# Care Order Management

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/description-care-orders/care-order-management/)

The Order Ticket, Order Book, Fills, and Order and Fills widgets support the following care order user functionality:

* [Submitting care orders](../task-care-orders/submitting-care-orders.md)
* [Claiming and unclaiming care order](../task-care-orders/claiming-and-unclaiming-care-orders.md)
* [Canceling or changing care orders](../task-care-orders/changing-or-canceling-care-orders.md)
* [Approving or rejecting a cancel or change request](../task-care-orders/approving-or-rejecting-a-request.md)
* [Assigning fills to a care order](../task-care-orders/assigning-fills-to-care-orders.md)
* [Submitting child orders for a care order](../task-care-orders/submitting-related-child-orders.md)

Before you begin, ensure you are [showing the following buttons and columns](../../../basic-order-entry/trading-crypto-on-tt/reference-trading-crypto-on-tt/crypto-reference.md) in the
Order Book or Order Book pane of the Order and Fills widget:

* **Claim** and **Unclaim** buttons
* **Status**, **Originator**, and **CurrentUser** columns

## Care order accounts and related child orders

After claiming a care order in the **Order Book**, the owner can submit child orders related to the parent care
order.
Child orders may be sent to the exchange in the same account as the parent order, or sent from different accounts.
Quantities of child orders may modified but their total sum cannot exceed the quantity of the parent order.
The different accounts can be the owner’s native accounts that are inaccessible to the originator, or can be child
accounts that are part of the same parent-child account hierarchy accessible to the originator.

Child orders can be sent in multiple accounts to fill the same staged order. If you use the account default or order
profiles functionality, those predefined rules will seed the execution accounts based on markets, product types, and
specific products.

## Care order fills

The care order owner and originator will both see the care order fills in their Fills widget or Fills pane in their
Order and Fills widget. The owner can fill the care order by submitting related child orders or assigning their own
fills,
including manual fills using their own account or the same account as the originator. Based on which account the
owner uses, the originator may also see the owner’s fills if they are associated with their care order.

### Fills from different accounts

If the owner fills all or part of the care order using a different account from the originator’s account, the owner
will see fills for both accounts. For example, the owner’s account “12345” and the originator’s account “ABCDEF”

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-fills-diff-account.png)

Because the owner used their own account to fill all or part of the care order, the originator sees just the fills
for their own account (e.g., ABCDEF).

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-originator-fills.png)

### Fills from the same account

When the owner fills all or part of the care order from the same account as the originator’s account, the owner will
see fills for both accounts. For example, account “ABCDEF” for the child order ID, and account “ABCDEF” for the care
order ID.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-fills-same-account.png)

Because the same account was used, the originator will also see both fills in their Fills pane.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-originator-fills-both.png)

## Care orders in the Audit Trail

When owners work a staged order at any point in time, they have access to a full Audit Trail of the order. The Audit
Trail includes information about when the order arrived and was claimed, as well as when the order was filled,
modified, and/or canceled and replaced, etc.

If the owner has MiFID II tags associated with their order profile when submitting child orders related to a parent
care order, those tags appear on the order and are sent to the exchange and appear in the Audit Trail.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-broker-a-mifid-tags.png)

←[Previous PostCare order account permissions and ownership](care-order-account-permissions-and-ownership.md)

[Next PostSupported/Unsupported Care Order Actions](supported-unsupported-care-order-actions.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-fills-diff-account.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-originator-fills.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-owner-fills-same-account.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-originator-fills-both.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-broker-a-mifid-tags.png
