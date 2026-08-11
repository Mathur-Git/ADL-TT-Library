---
title: Uploading local manual fills to TT
category: Order Management
source: https://library.tradingtechnologies.com/trade/order-management/position-manager/task-position-manager/uploading-local-manual-fills-to-tt/
---

# Uploading local manual fills to TT

> Category: **Order Management** · [Source](https://library.tradingtechnologies.com/trade/order-management/position-manager/task-position-manager/uploading-local-manual-fills-to-tt/)
>
> **Interpreted in:** [Order Management & Risk § Position tracking (Positions, Position Manager)](../../../../guides/order-management-and-risk.md#position-tracking-positions-position-manager)

You can upload [local manual fills](../description-position-manager/position-manager-overview.md) into the TT system using the import functionality in Position Manager. For example, options users that do not use Expiration Manager can track their futures positions from exercised or expired options by uploading their underlying fills into Position Manager. Uploaded fills must be in the [CSV file format](../reference-position-manager/csv-file-format-for-uploading-fills.md).

**Note**: Uploading manual fills for Autospreader parent orders is not supported.

To upload local manual fills to TT:

1. Select the **Local Fills** tab and click the import button in Position Manager.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-button.png)
2. Drag and drop the CSV file into the import dialog box, or navigate to and select a file.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-dialog.png)

   The Position Manager import utility opens seeded with the uploaded CSV file.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-import.png)
3. Review the data in the **IMPORT PREVIEW** pane to verify that the imported columns are mapped to Position Manager columns.

   **Note**: Only the first ten (10) lines of the file are displayed in the **IMPORT PREVIEW** pane.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-preview.png)
4. If a column from the CSV file did not map to a Position Manager column, double-click the empty cell in **Imported Columns** to select one.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-select.png)

   **Tip**: You can also drag-and-drop columns from **Unused Columns** to **Imported Columns**.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-drag.png)
5. Click **Confirm**.

   The fills are imported to Position Manager in a “Staged” state.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-imported.png)
6. Click **Publish** in Position Manager to create the manual fills.

   When you add a local fill and click **Publish**, the fills are only visible to you and not visible to others who share your account. Local manual fills are stored on your machine:

   * They do not appear when the same workspace is opened on another machine during the same trading day.
   * They do not adhere to the Start Of Day (SOD) setting (which manages the exchange and admin fills), and therefore do not carry over.

   Local fills do not affect any risk checks or limits that are set on the account, and do not rollover to the next trading session. These fills appear in the Fills widget with a status of “Local” in the **ManualFill** column.

←[Previous PostPreviewing manual fill and SOD changes](previewing-manual-fill-and-sod-changes.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-button.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-import.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-preview.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-drag.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/pm-upload-fills-imported.png
