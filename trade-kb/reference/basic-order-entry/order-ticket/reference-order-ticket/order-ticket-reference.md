---
title: Order Ticket Reference
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference/
---

# Order Ticket Reference

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-ticket/reference-order-ticket/order-ticket-reference/)

## Available settings

These settings affect only the selected Order Ticket widget. To update the default settings with these value for newly-opened Order Ticket widgets, or to apply them to existing opened widgets, click **Defaults**.

![Order Ticket settings](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-settings.png)

| Setting | Description |
| --- | --- |
| Enable broker mode | Displays an Order Ticket with a single Buy or Sell button based on whether you are entering a bid or ask. When enabled, you can also enable the **Left-click = aggressive** setting in **Edit** | **Preferences** from the workspace menu bar. When this setting is enabled, the Order Ticket is automatically seeded to lift the offer (Buy) or hit the bid (Sell). |
| Show floating depth widget on hover | When enabled, the Floating Depth widget displays up to three levels of depth for both bids and offers. You can click a price or quantity in a level of depth to seed that value in the price or quantity edit control in the Order Ticket. |
| Show held-order toggle | Sets whether to show/hide the “Hold” button on the Order Ticket. This button is used to submit new orders as held orders. |
| Ignore global Account List broadcasts | Configures the widget to ignore account selections made in an Account List. When checked (enabled), the widget ignores account selections broadcast by an Account List widget. |
| Retain Order Ticket fixed size (do not auto expand) | Retains the saved Order Ticket size as the default. To retain your Order Ticket dimensions, check this checkbox and also check **Defaults** | **Save as Defaults** in the Order Ticket settings. |
| Display Message on Staged Orders | Displays the staged order instructions on the Order Ticket. If the originator includes instructions or a message when staging an order, the message text is displayed on the Order Ticket when the owner clicks the “B” or “S” button to fill the claimed care order. This setting is enabled by default. |
| Display all algo parameters in confirmation mode | Shows the algo parameters flyout panel in expanded mode when confirming an order. This allows you to review and verify all algo parameters before submitting an algo order or TT Order Type. |
| Notional for futures contracts | To set the currency the notional value of the contract is displayed. |
| Price increment buttons | Order Ticket price increment buttons adjust the price values of a selected instrument either by (1) integer tick increments of the instrument, or (2) decimal precision multiples of the instrument’s point value.    **Note:** This feature is available for all instruments, but is most relevant with LME instruments. (Example – can set .25 increments for “carry” instruments.) |

## Free-form text fields

The following table provides descriptions of the free-form text fields on the Order Ticket when entering orders to exchanges supported by the TT platform.

| Text Field | Description | Exchange API Mapping |
| --- | --- | --- |
| Text A | Optional, user-defined text value that remains on the order in the TT system. This value may be routed to the exchange for clearing and back office purposes.  You can specify a value for the field. Alpha-numeric and special characters are allowed. If you do not specify a value, the value defined in the Setup application will be sent when the order is submitted. The following exchanges have a maximum character length for this field:   * ASX — 6 characters * B3 — 50 characters * DGCX — 128 characters * EEX — 12 characters * Eurex — 12 characters * HKEx — 15 characters * ICE — 12 characters * ICE\_L — 12 characters * Nodal — 12 characters * MEFF — 15 characters * MEXDER — 10 characters * MX — 25 characters * SGX — 32 characters | The value in Text A is routed to the following exchanges (Setup app user exchange field is in parentheses):   * ASX — Tag 58 (Text) * B3 — Tag 5149 (Memo) * CME (iLink 3) — Tag 5149 (Memo) * DGCX — Tag 58 (Text A) * EEX — Tag 25007 (Text 1) * Eris — Tag 58 (Text) * Eurex — Tag 25007 (Text 1) * HKEx — exchange\_info\_s (Text A) * ICE — Tag 9121 (Memo Field) * ICE\_L — Tag 9121 (Memo Field) * KCG — Tag 58 (Text) * MEFF — Tag 58 (Text 1) * MEXDER — Tag 58 (Text A) * MX — Memo (Text 1) * Nodal — Tag 25007 (Text 1) * OSE — exchange\_info\_s (byte 7-22 of 32) (Text A) * SGX — exchange\_info\_s (Text 2) * TFX — Tag 10001 (Text) |
| Text B | Optional, user-defined text value that remains on the order in the TT system. This value may be routed to the exchange for clearing and back office purposes.  You can specify a value for the field. Alpha-numeric and special characters are allowed. If you do not specify a value, the value defined in the Setup application will be sent when the order is submitted. The following exchanges have a maximum character length for this field:   * EEX — 12 characters * Eurex — 12 characters * HKEx — 15 characters * Nodal — 12 characters * SGX — 15 characters | The value in Text B is routed to the following exchanges (Setup app user exchange property is in parentheses):   * EEX — Tag 25009 (Text 3) * Eurex — Tag 25009 (Text 3) * HKEx — customer\_info\_s (Text B) * MEFF — Tag 1 (Instead of clearing account name) * Nodal — Tag 25008 (Text 3) * SGX — customer\_info\_s (Text 1) |
| Text C, Text TT | Optional, user-defined text values that remain on submitted orders for tracking purposes in the TT system, but are not routed to the exchange. | None. These values are not sent to the exchange, but remain on the order within the Order Book, Audit Trail, and Fills widgets. |

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ot-settings.png
