---
title: Installing and enabling the Excel add-in
category: Algo Trading
source: https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/installing-and-enabling-the-excel-add-in/
---

# Installing and enabling the Excel add-in

> Category: **Algo Trading** · [Source](https://library.tradingtechnologies.com/trade/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/installing-and-enabling-the-excel-add-in/)
>
> **Interpreted in:** [Algo Ops: Dashboard, Autotrader & Excel § Excel / RTD linking](../../../../guides/algo-ops.md#excel-rtd-linking)

To download and install the Excel add-in:

1. Log in to TT, and open a workspace.
2. From the **File** menu, open the **Excel** sub-menu and select **Download Excel Add-In**.

   **Note**: Based on your browser settings, the browser might automatically save the file to a pre-configured folder, ask you to save the file, or ask you to run the program. If you choose to run the program from your browser, skip the next step.
3. Launch the **TTExcelIntegrationSetup.exe** application.

   The following dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-security-dialog.png)
4. Click **Run**.

   If Microsoft .NET Framework 4.6 is not already installed on your system, the following dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-net-framework-dialog.png)

   Click **Accept** to install the framework.

   The **Microsoft Office Customization Installer** dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-office-installer-dialog.png)
5. Click **Install**.

   When the installation finishes, the following dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-office-confirm-dialog.png)
6. Click **Close**.

**Note**: In some instances, the installation of .Net 4.6 will fail with a **Visual Studio Tools for Office Solution Installer** error dialog. If you see this error dialog, try the steps described in [If the .NET installation fails](https://library.tradingtechnologies.com/trade/exc-reference.html).

### Enabling the Excel add-in

To enable the **TTExcelIntegrationSetup** add-in in Excel:

1. Start Excel.

   The following dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog1.png)

   **Note**: The dialog might be obscured by the Excel window, so you might need to collapse or move the Excel window to see the dialog.
2. Click **OK**.

   The following dialog is displayed.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog2.png)
3. Click **Yes** to install the security certificate.
4. If you use Windows Firewall, you might need to configure network access in the following dialog.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog3.png)

   Click **Allow access**.
5. Optionally, to verify the add-in installed successfully, open the **Excel Options**, select **Add-Ins**, and confirm the list includes **TTExcelIntegration**, similar to the following:

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-options-add-in.png)

### Uninstalling the TT Excel integration add-in

To uninstall the TT Excel integration add-in, open the Windows Programs control panel and remove **TT Excel Integration**.

[Next PostConnecting TT to Excel spreadsheets](connecting-tt-to-excel-spreadsheets.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-security-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-net-framework-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-office-installer-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-office-confirm-dialog.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-tt-plugin-dialog3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/excel-options-add-in.png
