---
title: Alerts Reference
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference/
---

# Alerts Reference

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/alert-manager-and-alert-viewer/reference-alert-manager-and-alert-viewer/alerts-reference/)
>
> **Interpreted in:** [Order Management & Risk § Alerts (real-time risk guard)](../../../../guides/order-management-and-risk.md#alerts-real-time-risk-guard)

## Order Condition

Field | Value || Account | A list of accounts assigned to a user. |
| Buy/Sell | The side of the trade. Valid values: Buy, Sell. |
| Contract | Opens the Market Explorer and Search to select an instrument. |
| CurrentUser | TT user name of the trader associated with the transaction or owns a staged order. |
| Exchange | The market being traded. |
| Exec Type | The reason for sending an order Execution Report, e.g., New, Canceled, Rejected, etc. |
| Fill Price | The price at which to fill the order. |
| Fill Qty | The quantity at which to fill the order. |
| Non-matching State | Indicates whether the market is in a matching or non-matching state, e.g., Open or Pre-Open. Valid values: True or False. The default is “False”. |
| Order Price | The price at which the order was entered. |
| Order Type | The natively supported exchange order type. |
 Originator | TT User ID of the person who submitted the order or staged order. || Price Deviation | Sets how far from the last traded price to submit an order. Set the number of ticks or a percentage. |
| Product Type | The asset class or type of instrument being traded. |
| Status | Order status information on an Execution Report, e.g., Working, Filled, Canceled, etc. |
| Synth Status | Order status information on an Execution Report for a parent synthetic order. |
| TIF | Natively supported exchange time-in-force restrictions. |
| Total Fill Quantity | Triggers the condition when the order is filled for the quantity entered. |
| Total Quantity | Triggers the condition when the order is completely filled. |
| Working Quantity | Triggers the condition based on the working order quantity. |

## Position Condition

Field | Value || Account | A list of accounts assigned to a user. Selected by default. |
| Contract | Opens the Market Explorer and Search to select an instrument. Either a contract or product is required if the field is set to “Position”. |
| P&L | The amount of P/L in a single account or for all accounts. |
| Position | The open position in a single account or all accounts. Sets a condition based on the quantity (Qty) or percentage (%) of the account position limit. The “%” operator provides the ability to display an alert when an account is approaching its limits (Max position product (net)). For percentage-based alerts, you must also provide one or more products or contracts. |
| Product | Opens the Market Explorer and Search to select a product. Either a contract or product is required if the field is set to “Position”. |

## Algo Condition

Field | Value || Account | A list of accounts assigned to a user. Selected by default. |
| Algo | A list of your available algos. |
| CurrentUser | TT user name of the trader associated with the transaction or owns a staged order. |
 Originator | TT User ID of the person who submitted the order or staged order. || Status | [Algo status](../../../algo-trading/algo-dashboard/reference-algo-dashboard/algo-dashboard-reference.md) information. |

## Price Condition

Field | Value || Specific Qty | The user-definied number of contacts or lots. |
| Bid Qty | The total quantity at the best bid price. |
| Bid Price | The current best bid price. |
| Ask Price | The current best ask price. |
| Ask Qty | The total quantity at the best ask price. |
| Last Price | The last traded price during the current trading session. |
| Last Qty | The total quantity at the last traded price. |
| Open | The price at market open. |
| High | The highest traded price during the current trading session. |
| Low | The lowest traded price during the current trading session. |
| Close | The price at market close. |
| Net Change | The net change in the contract price for the trading session. |
| Prev Last | The last traded price from the previous session. |
| Prev High | The highest traded price from the previous session. |
| Prev Low | The lowest traded price from the previous session. |
| Settle | The settlement price from the previous session. |
| Volume | The total traded volume for the contract. |

## Condition and Criteria Operators

Operator | Description || = | Equals |
|  | Less Than |
|  | Not equal |
|  | Less Than or Equal |
| >= | Greater Than or Equal |
| Contains | Contains value |
| Change | Price or quantity changes value |

