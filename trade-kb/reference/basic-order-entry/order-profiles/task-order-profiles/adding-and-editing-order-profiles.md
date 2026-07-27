---
title: Adding and editing order profiles
category: Basic Order Entry
source: https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/task-order-profiles/adding-and-editing-order-profiles/
---

# Adding and editing order profiles

> Category: **Basic Order Entry** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/basic-order-entry/order-profiles/task-order-profiles/adding-and-editing-order-profiles/)

To add an Order Profile:

1. In an open Order Profiles widget, click the show/hide button in the Profiles panel to show the rule panel and click **Edit**.
2. Click **Add Profile**.

   A new profile name and row in the rules panel are displayed and highlighted yellow.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-add-1.png)

   **Tip**: As an administrator, click the drop down arrow in the “Add Profile” button to create an admin-controlled profile.
3. Enter a new name the profile.

   Duplicate profile names are not
   allowed. The name also appears in the **Profile** column in the rules panel.
4. In the rule panel, double-click the cell in each column to enter a value.

   The default settings display asterisks for the Prod, Exch, Group, and Type cells and cannot be edited. Refer to [Order Profiles Reference](../../../viewing-market-data/depth/reference-depth/depth-reference.md) for a description of each column.

**Note**: **Max Qty** is a mandatory field for saving a new order profile or rule. It sets the maximum order quantity for the rule. The largest value supported is 999,999,999.

![](https://library.tradingtechnologies.com/wp-content/uploads/2026/05/order-profiles-max-qty.png)

5. To add a rule to the profile, click **Add Rule** and double-click a cell in [each column](../../../viewing-market-data/depth/reference-depth/depth-reference.md) to add values as needed.

**Note:** You cannot have the same combination of product, exchange, product group, and product type in multiple rules.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-add-2.png)

**Tip**: Repeat this step to create additional rules for the selected profile.

6. Optionally, right-click one or more variable rule fields to define how the fields are applied to an order.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-cell-behavior.png)

   **Tip**: Drag the mouse across multiple cells to define the same behavior for each one.

   Select one of the following:

   * **Clear existing value when profile is applied** — Allows the field value to be overwritten at order entry when a different profile is selected.
   * **Preserve existing value when profile is applied** — Keeps the existing field value at order entry when a different profile is selected. When this option is selected, the “pass-through” icon ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-icon.png) appears in the field.

   **Note**: By default, neither option is active and if a cell has a value, the field gets set to that value at order entry. If a cell is blank in the Order Profile selected at order entry, the previous value in that field is cleared unless that cell is configured with the **Preserve existing value when profile is applied** option.
7. Check the **Use** column to include the rule in finding a best match for order
   entry.
8. Click **Save Changes**.

## Editing an Order Profile

You can change or remove a profile, or change and remove rules to existing profiles in edit mode.

To edit an Order Profile:

1. In an open Order Profiles widget, click the show/hide button in the Profiles panel to show the rule panel.
2. Select a profile in the Profiles panel and click **Edit**.

   **Tip**: You can also double-click a cell in the rule panel to enter edit mode.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-select-profile.png)

   **Note**: Profiles created by your administrator are greyed-out and their fields cannot be edited. However, you can add your own rules to these profiles. Admin profiles created in Order Profiles are shaded green.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-admin-profile.png)
3. Double-click a cell in each column in the rules panel and change its value as needed.

   **Note**: The key fields for the default rule cannot be edited.

   **Tip**: Mouse drag up or down to select multiple cells.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-multiple-edit.png)
4. To add a rule to the profile you are editing, click **Add Rule** and edit each column cell as needed.

   **Tip**: If you select a product in the **Prod** column, the **Exch** and **Type** fields will be seeded automatically.

   Refer to [Order Profiles Reference](../../../viewing-market-data/depth/reference-depth/depth-reference.md) for a description of each
   column.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit-profile.png)

   To remove a rule from a profile, select the rule in edit mode and click **Remove**.

   For more details about your editing options, refer to [Edit Mode](../description-order-profiles/order-profiles-display.md#edit-mode).
5. Click **Publish Changes**.

   If you make changes to an uploaded profile or admin profile as an administrator, the changes are saved and broadcast to all users when you click “Publish”.

   Published changes are stored locally on each user’s machine and are loaded upon login. If they are currently logged in, users will see the profile changes in their open Order Profiles widgets.

## Removing an Order Profile

To remove an Order Profile:

1. Select the profile in edit mode and click **Remove**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-remove-profile.png)

   The button is active when a removable profile is selected.

   **Note**: The default profile and administrator profiles added in Setup cannot be removed.
2. Click **Save Changes**.

[Next PostSelecting an Order Profile for trading](selecting-an-order-profile-for-trading.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-add-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2026/05/order-profiles-max-qty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-add-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-cell-behavior.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-select-profile.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-admin-profile.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-multiple-edit.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-edit-profile.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/order-profiles-remove-profile.png
