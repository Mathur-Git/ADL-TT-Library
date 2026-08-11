---
title: Managing and resolving FIX care order rejections
category: TT® OMS
source: https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/managing-and-resolving-fix-care-order-rejections/
---

# Managing and resolving FIX care order rejections

> Category: **TT® OMS** · [Source](https://library.tradingtechnologies.com/trade/tt-oms/care-orders/task-care-orders/managing-and-resolving-fix-care-order-rejections/)

## Launching the Widget

* The Order Exceptions Widget is located under **Widgets** > **Order Management** > **Order Exceptions**.
* Only one instance can be open at a time; attempts to open another will bring the existing one forward.
* If OMS Advanced is not enabled, the menu item remains visible but disabled, with a tooltip: “Please contact your administrator to enable OMS Advanced features in Setup to access this widget.”

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-oms-advanced-disabled-1-scaled.png)

Note FIX care orders with exceptions are only displayed in the Order Exceptions widget — not in the regular Order Book or Orders and Fills (OFW) widgets.

## Included Exception Fields

Orders with exceptions in the following fields appear in this widget:

* Account
* Instrument
* Side (Buy/Sell)
* Quantity
* Price
* Order Type
* Time-in-Force (TIF)
* User Parameters (e.g., algo parameters)

Orders with other errors (e.g., invalid user) are hard rejected and will not appear in the Order Exception Widget.

## Exception Routing

Exception orders route on the normal TT account, unless the account itself is invalid. If an invalid account is detected, the order will route on the session’s assigned error account.

Note Firms should map these error accounts to the appropriate users handling exceptions.

## Exception Handling Actions

### Repair

The Repair action allows users to correct and resubmit orders that failed due to fixable errors.

* Enabled when at least one selected order has been modified to resolve errors.
* Submits corrected rows only; uncorrected rows remain in the widget.

### Reject

The Reject action rejects the order and sends a FIX cancellation to the originating client.

* Always enabled.
* Sends a cancel request which generates:

* A Reject message for FIX Drop Copy.
* A Cancel message for FIX Order Routing.

All Repair and Reject actions generate audit trail restatements for compliance tracking.

## Order Rows

* Only orders in Repair Mode appear.
* Rows automatically add or remove as status changes.
* Single-row Repair: Only one order can be repaired at a time.
* Multi-row Reject: Multiple rows can be rejected simultaneously.
* Corrected but not re-submitted rows display with a light green background to indicate readiness for re-submission.
* **Sorting** — The ability to sort rows per column is not supported.
* **Filtering** — Columns can be filtered similar to other grid based widgets.

## Column Behavior

### Error Cells

* Identified by a red border.
* Display intended FIX values or blank if missing.

### Contract Column

* Invalid instruments show as “Invalid Instrument.”
* Unknown markets display a question mark (?) in the Exch column.
* Clicking the “Magnifying Glass” icon ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-1.png) launches Market Explorer to select a valid instrument.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-select-instrument-1-scaled.png)

### Price Column

**Two invalid scenarios:**

1. Invalid Instrument — Price cell shows “?” (not editable) until a valid instrument is selected.
2. Invalid Price — Price cell shows “?” with red border and tooltip of raw FIX value. Editable via Repair Order Ticket launched by left click on the red pencil icon button.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-invalid-price-1-scaled.png)

### Edit Column

* Displays a pencil icon when editable.
* Clicking launches a floating Repair Order Ticket pre-populated with the order details.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-repair-order-ticket-1.png)

* The Repair Ticket:

* Displays a green **Repair** button.
* Highlights invalid fields.
* Hides **Stage** checkbox and **Reset** button.
* Allows multiple tickets open at once, but disables other edit buttons while one is active.

### Account Column

* Displays FIX account value.
* Invalid accounts can be corrected in the Repair Order Ticket.
* Adding new accounts in Setup requires a front-end refresh before appearing in the GUI.

### Message Column

* Displays FIX error text.
* Highlighted with a red border if the offending field isn’t one of the main exception fields.

### FIX Message Column

* Optional column showing full original FIX message text.
* Not queryable via Audit Trail or Audit Query.
* Not filterable; off by default.
* Hover tooltip displays full message content.

### Default Columns

Select, Edit, B/S, OrdQty, Exch, Contract, Price, Account, ProfileName, Type, TIF, Message, Originator, Time, TTOrderID

### Optional Columns

All standard Order Book fields are available for optional display and filtering

### Widget Settings

#### General

* Display widget for new exception (checkbox)

* Default: Off
* When enabled, the widget opens (or “shakes” to the front) when new exceptions arrive.

### Global Preferences

A new sound option under Preferences > Sounds > Orders:

* Exception order

* Default sound: “Notify”
* Default state: Off

←[Previous PostClaiming and unclaiming care orders](claiming-and-unclaiming-care-orders.md)

[Next PostUploading and staging orders](uploading-and-staging-orders.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-oms-advanced-disabled-1-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/btn-magnify-glass-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-select-instrument-1-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-invalid-price-1-scaled.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/co-order-exceptions-repair-order-ticket-1.png
