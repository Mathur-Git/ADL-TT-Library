---
title: Stitching and Splitting Care Orders
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/task-stitching-and-splitting/stitching-and-splitting-care-orders/
---

# Stitching and Splitting Care Orders

> Category: **TT® OMS** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/tt-oms/stitching-and-splitting/task-stitching-and-splitting/stitching-and-splitting-care-orders/)

Using the Order Book or orders pane of the Order and Fills widget, you can [stitch and split](../description-stitching-and-splitting/stitching-and-splitting-overview.md) care orders to create exchange-traded spreads. Care orders can be [stitched](#stitch) and [split](#split) using the context menu or [combining tool](#combine).

## Stitching care orders

To stitch a care order:

1. Select two claimed care orders for the same product with equal quantities and opposite sides.

   **Tip**: If the account or user has permission to “work orders without claiming” in Setup, you can stitch
   and claim care orders with a single stitching action.
2. Right-click one of the orders and select **Order staging** | **Stitch**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-context-menu-1.png)

   The orders are stitched into an exchange-traded calendar spread. The original care orders are nested below
   the stitched order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-result-2.png)

## Splitting and stitching care orders

For care orders with different quantities, you can split the orders and stitch them to care orders with equal
quantities to create exchange-traded instruments. After a care order is split, each portion can be split further or
combined with other care orders in the Order Book or orders pane. The [split quantities can also be modified](managing-stitched-and-split-care-orders.md) manually
without changing the quantity of the parent care order.

To split and stitch care orders:

1. Right-click a claimed care order and select **Order staging** | **Split** from the context menu.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-menu2-1.png)

   The order is split into two equal child care orders. The split orders are marked with two asterisks “\*\*”.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-result1-2.png)

   **Note**: To unsplit the order, right-click the original care order and select **Order staging** |
   **Unsplit**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-unsplit-1.png)
2. Select two claimed care orders for the same product with equal quantities and opposite sides.
3. Right-click one of the orders and select **Order staging** | **Stitch**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-split-1.png)

   The orders are stitched into an exchange-traded calendar spread. The remaining child care order is still
   associated with the original care order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-split-result-1.png)

## Stitching care orders using the combining tool

Care orders with equal or different quantities can also be stitched using the combining tool. If the quantities of
two orders
restrict stitching, you can split one order into two, stitch the quantities that match using the combining tool, and
work the remaining tails as a separate order.

**Tip**: Apply OMS features with a single click without having to right click and navigate the context menu to use those features. In the right-click context menu, select **Settings: Order Book | Set Order Toolbar buttons**. Select **Stitch** and **Split**, click OK then Save. When enabled on the toolbar, each button will enable, disable and function the same as their related right click menu item.

To stitch care orders using the combining tool:

1. Select two care orders of opposite sides and different contract months.
2. Right-click and select **Order Staging** | **Combine**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-hide-stitch-combine1-1.png)

   The combining tool opens in the Order Book or orders pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-hide-stitch-combine-tool-1.png)

   **Tip**: If you hover on the Stitch button, TT displays which care orders can be stitched.
3. Click the **Stitch** button.

   When **Stitch** is clicked, equal quantities of the selected orders are stitched into an exchange-traded
   spread.

## Stitching care orders for options contracts

Using the context menu, care orders for outright options contracts can be stitched into a parent care order for an
exchange listed strategy. Stitching options contracts does not require the use of the combining tool in the Order
Book or orders pane of the Order and Fills widget. When two or more staged outright options orders are stitched to
create an options strategy, TT submits the strategy creation request and RFQ directly to the exchange.

**Note**: For exchanges where an options strategy must fit a defined strategy type, contact the exchange for the
strategy requirements before stitching the care orders. If needed, the options care orders can be split first before
being stitched if the exchange does not accept strategy legs with different ratios.

To stitch care orders into an options strategy, select two or more staged orders for options contracts in the Order
Book or orders pane, then right-click and select **Order staging** | **Stitch** from the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-1.png)

When the care orders are stitched, a strategy creation request is submitted and resolved at the exchange. The
following status message is displayed in the upper right corner of the workspace.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-message-1.png)

After the strategy is created, it’s displayed in the Order Book or orders pane.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-created-1.png)

When the options strategy is traded, fills for the stitched care orders are [allocated](https://library.tradingtechnologies.com/trade/all-allocation-overview.html) the same way as stitched care orders for futures contracts.

## Unstitching a care order

To unstitch a care order, right-click the parent stitched order and select **Order staging** | **Unstitch**.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-unstitch-working-1.png)

If the unstitched order has a working child order, the working order is orphaned from the parent care orders but
remains working as a native exchange order.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-unstitch-result-1.png)

[Next PostManaging stitched and split Care Orders](managing-stitched-and-split-care-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-context-menu-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-result-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-menu2-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-result1-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-split-unsplit-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-split-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-split-result-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-hide-stitch-combine1-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-hide-stitch-combine-tool-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-message-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/stp-stitch-options-created-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-unstitch-working-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/oms-stitch-unstitch-result-1.png
