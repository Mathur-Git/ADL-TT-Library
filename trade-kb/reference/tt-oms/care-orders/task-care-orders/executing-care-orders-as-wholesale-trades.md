---
title: Executing care orders as wholesale trades
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/executing-care-orders-as-wholesale-trades/
---

# Executing care orders as wholesale trades

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/executing-care-orders-as-wholesale-trades/)
>
> **Interpreted in:** [Order Types & Execution § Care orders & the TT OMS lifecycle](../../../../guides/order-types-and-execution.md#care-orders-the-tt-oms-lifecycle)

Blocktrader supports executing staged care orders as two sides of a wholesale trade for HKEX and JPX markets. Select two single, bulked, or split care orders for the same instrument and order quantity with opposite Buy/Sell sides in the Order Book, then right-click and select **Order staging** | **Send to Blocktrader** in the context menu.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-send1.png)

**Note**: For HKEX, “Send to Blocktrader” also appears in the context menu when selecting a single staged order to be executed as a one-sided (T4) OTC trade.

The staged care orders are displayed in Blocktrader. When submitted as a wholesale order, TT displays the **Linked Order** numbers in Blocktrader. The resulting fills for the wholesale order will be associated with the care orders using the linked order identifiers.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-staged-linked.png)

The “linked order number” is also shown in the **TTOrderID** column in the Audit Trail.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-linked-audit.png)

←[Previous PostSubmitting related child orders](submitting-related-child-orders.md)

[Next PostAssigning fills to care orders](assigning-fills-to-care-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-send1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-staged-linked.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/hkex-block-linked-audit.png
