---
title: Creating and modifying an SOD
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/position-manager/task-position-manager/creating-and-modifying-an-sod/
---

# Creating and modifying an SOD

> Category: **Order Management** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/order-management/position-manager/task-position-manager/creating-and-modifying-an-sod/)

**Note**: As an administrator, the “Update positions” setting must be enabled in Setup for each account available to you in order to create or modify an SOD or that account. Also, only one SOD record can exist per account and contract.

## Creating an SOD

To create an SOD:

1. In the workspace menu bar, click **Widgets** | **Miscellaneous** | **Position Manager**.

   The Position Manager widget opens.
2. Select the **Admin SOD** tab.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-1.png)
3. Click **+ Add Row** to create a new SOD record.

   A new SOD row is displayed and highlighted yellow in the Position Manager.
4. Enable the following optional setting as needed:

   **Price off tick** — If checked, allows you to enter an off tick price per leg for instruments that support tick sizes smaller than what is displayed.

   **Note**: Off-tick prices cannot be entered for instruments that tick in fractions (displayed with an apostrophe). For example: ZB Sep18 with a price of 145’23.
5. In the SOD row, click each cell in the following columns to add or select a value:
   * **Contract** — Use the product search or market explorer to find and select a contract. The settlement price for the selected contract appears in the **Price** column.
**Account** — Select an account for the manual fill.

**Note:** An account is required to manually add an SOD record.

6. **SOD** — Add an SOD position. Positive values represent a long position, and negative values represent a short position.
7. **Use Settle** — Select whether to use the current settlement price for the contract.
8. **Price** — Enter a price for the SOD or use the default settlement price for the selected contract.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-2.png)

Before the SOD is published, the **Status** column displays a status of “Staged”.

9. To create additional SOD records, click **+ Add Row** and repeat the previous Step.
10. Review the SOD record and click **Publish**.

    The new SOD position is displayed in the Positions widget.

    ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-3-pos.png)

## Modifying an SOD

A Start of Day (SOD) record for an account can be modified manually on a per contract basis.

To modify an SOD:

1. In the SOD row, click the following fields to modify as needed:
   * **SOD** — Modify the SOD position.
   * **Use Settle** — Select whether to use the current settlement price for the contract.
   * **Price** — Enter a price for the SOD or use the default settlement price for the selected contract.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-modify-3.png)

   **Note**: You can also open Positions Manager by clicking
   **Modify SOD** from the context menu when selecting a contract in the
   Positions widget.

   **Tip**: Click ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-icon-reset.png) to clear the modifications without saving as needed.
2. Review the SOD record and click **Publish**.

   The new SOD position is displayed in the Positions widget.

←[Previous PostCreating a manual fill](creating-a-manual-fill.md)

[Next PostPreviewing manual fill and SOD changes](previewing-manual-fill-and-sod-changes.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-3-pos.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-sod-modify-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-icon-reset.png
