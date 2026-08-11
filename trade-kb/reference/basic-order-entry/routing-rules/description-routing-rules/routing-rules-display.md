---
title: Routing Rules Display
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/description-routing-rules/routing-rules-display/
---

# Routing Rules Display

> Category: **Basic Order Entry** · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/routing-rules/description-routing-rules/routing-rules-display/)

The Routing Rules widget consists of the following elements as shown.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-display.png)

The widget includes:

1. **Search** — Allows you to search and filter the list of rules by name.
2. **Routing rules** — Each available routing rule.
3. **Rules panel** — Displays routing rules available for trading.
4. **Order portions** — Each order portion for a routing rule consists of the following columns:
   * **Rule** — The name of the routing rule using the order portion.
   * **Use** — Indicates if the order portion is active.
   * **Profile** — The list of available customer order profiles.
   * **Account** — The list of available accounts. If an order profile is selected, the account assigned to a customer’s profile will be used to route the order portion.
   * **Portion** — The portion of the total order quantity to assign to a broker or account. At order entry, the portion is calculated as a ratio of the sum of all portion values for the rule. The portion value is not a percentage of the total order quantity, but you can enter values that look like percentages when creating a rule. Allocation percentages and portion sizes support up to ten (10) decimal digits of precision. This field must contain a positive number from 1 to 999.9999999999.
   * **Side** — The types of trades allowed in the account. Select one of the following: Buy, Sell, or Both (the account can be used for for both bids and offers).
5. **Order portions panel** — Displays portions for each routing rule.
6. **Edit button** — Allows you to add or remove a routing rule. Also allows you to add, change, or remove order portions for a rule selected in the rules panel. Refer to [Routing Rules Edit Mode](#edit-mode) for more details.
7. **Add portion button** — Adds a new order portion to the potions panel. Double-click the cell in each column to add a new value.
8. **Show/Hide button** — Shows/hides the Rules Panel.

## Routing Rules Edit Mode

When you click **Edit** or double-click a cell in the rules or order portions panel, the following additional buttons and checkboxes are displayed.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-display-edit.png)

Edit mode includes:

1. **Checkbox** — Allows you to select a routing rule. Multiple rules can be selected per edit.
2. **Add Rule** — Allows you to add and configure a routing rule. New rules are highlighted yellow until they are saved in the widget.
3. **Remove** — Allows you to delete a routing rule. The button is active when a rule is selected.
4. **Add Portion** — Allows you to add and configure an order portion for a routing rule. New portion are highlighted yellow until they are are saved in the widget.
5. **Remove** (portions panel) — Deletes a selected order portion. The button is active when a portion is selected.
6. **Import** —- Allows you to import a CSV file of routing rules.
7. **Cancel** — Quits editing mode without saving.
8. **Save Changes** — Quits editing mode and saves all changes.

←[Previous PostRouting Rules Overview](routing-rules-overview.md)

[Next PostRouting portion calculations](routing-portion-calculations.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-routing-rules-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/rr-display-edit.png
