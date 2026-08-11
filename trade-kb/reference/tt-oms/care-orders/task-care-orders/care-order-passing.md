---
title: Care order passing
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/care-order-passing/
---

# Care order passing

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/care-order-passing/)

You can use order passing to pass staged orders. Once care orders are passed and accepted, the new caretaker can still perform the advanced OMS features on one or more passed care orders, such as bulking, splitting and stitching. Also, passed care orders can be bulked/stitched with other non-passed care orders.

**Restrictions**: When creating new child orders on staged order that are passed, the order entry widget will seed the account from the parent staged order and restrict the order types available based on that account. If the current caretaker would like to place a child order using a different order type, they must select an account for the child order that allows that order type..

## Passing a care order

The process of passing a care order is described below:

1. User 1 claims the staged order.
2. User 1 passes the order to the group with User 2:

* Click the **Order Passing** button and select a target user group.

* User 2 selects the order in the Order Book:

* Click the **Order Passing** button and select **Accept orders**.

* User 2 accepts the passed staged order:

* After accepting the passed order, your group name is displayed in the Caretaker column. The Original Group column shows the name of the user group that initially passed the order.

* User 2 clicks the **B** or **S** button to launch the Order Ticket to place a child order.

## Partial Fills for Passed Care Orders

When staged orders are passed to a different user group, the new caretaker will receive any previously partial fills when they choose to “watch” one or more of the partially filled care orders using the “eyeball” button. The status field on these orders will display “Retrieving fills…” while the partial fills are downloaded. Once the fills are downloaded, the status field will revert to normal behavior.

This status will display within an Order and Fills Widget (OFW), or in an Order Book that is grouped with a Fills widget and/or a Position widget.

←[Previous PostUploading and staging orders](uploading-and-staging-orders.md)

[Next PostChanging or canceling care orders](changing-or-canceling-care-orders.md)→

