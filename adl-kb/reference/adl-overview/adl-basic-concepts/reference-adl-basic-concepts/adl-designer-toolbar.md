---
title: ADL Designer toolbar
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/reference-adl-basic-concepts/adl-designer-toolbar/
---

# ADL Designer toolbar

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/reference-adl-basic-concepts/adl-designer-toolbar/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § Algo settings (Information Panel → Settings)](../../../../guides/algo-types.md#algo-settings-information-panel-settings)

### ADL Designer toolbar

### Menus

| Menu | Item description |
| --- | --- |
| File | * **New**: Creates a new canvas. * **Open**: Opens an existing algo. * **Save**: Saves the current algo. * **Save As**: Saves the current algo with a different name. * **Deploy**: Uploads the current compiled algo to the Algo Server and makes it available in Trade widgets. * **Import**: Imports a JSON (.json) algo definition file and loads it on the canvas. * **Export**: Exports the current algo to a JSON algo definition (.json) file. * **Undeploy**: Removes a deployed algo from the Algo Server so it is no longer available in Trade widgets. * **Load Block Library**: Loads a library of Group blocks into ADL. * **Ver**: Date and time ADL was released. |
| Edit | * **Undo**: Undoes the previous action on the canvas. * **Redo**: Restores the previous action on the canvas. |
| View | * Zoom to Fit: Scales the ADL Designer to show the entire algo on the canvas. |

### Controls

| Control | Description |
| --- | --- |
|  | Allows you to navigate to the root algo or to the parent of a Group block currently open in the canvas. |
|  | Allows you to run, pause or stop a compiled algo, respectively, directly from the canvas. When you execute an algo from the canvas, the blocks will output dynamic values reflecting the execution of the algo. |
|  | Allows you to compile auto-generated code after every block addition, removal, variable adjustment, edge connection or an edge removal. Unchecking this option will activate the manual compile button, and the user may manually compile the generated code at will. |
|  | Allows you to compile the algo manually for testing (**Auto-Compile** is unchecked). |

### Algo settings

| Property | Description |
| --- | --- |
|  | Displays a drop-down menu of bookmarks created to save the view of the algo shown in the canvas. |
|  | Allows the user running the algo to choose between BUY or SELL when executing an algo. Some blocks in ADL have the capability to perform an alternate function depending on the user’s selection of this drop-down menu (see: [Flip For Sell Order Functionality](../../advanced-concepts/description/flip-for-sell-order-functionality.md) for more information). Use the **Order Side Selection** to design strategies which can alternate between buy and sell side routines. |
|  | Allows the algorithm to continue running even if one of the markets associated with an [Instrument](../../../trading-blocks/instrument-block.md) block contained in the algorithm closes. By default, the checkbox will be unchecked and the algorithm will pause when one of the markets reported by an [Instrument](../../../trading-blocks/instrument-block.md) block closes. You can enable this setting to design logic that can run outside of regular trading sessions (e.g., submitting orders during pre-open). |

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-navigation-controls.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-test-controls.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-auto-compile-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-manual-compile-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-bookmarks-menu.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-side-icon.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-ignore-market-state-icon.png
