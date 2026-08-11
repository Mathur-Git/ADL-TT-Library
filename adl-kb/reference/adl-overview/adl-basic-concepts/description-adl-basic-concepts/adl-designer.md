---
title: ADL designer
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/adl-designer/
---

# ADL designer

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/description-adl-basic-concepts/adl-designer/)
>
> **Interpreted in:** [Algo Types, Launching & Deployment § Algo settings (Information Panel → Settings)](../../../../guides/algo-types.md#algo-settings-information-panel-settings)

### ADL Designer

The ADL Designer provides the tools you need to design and test your custom algorithms.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer.png)

Major areas of the ADL Designer include:

1. **Toolbar**: Menus and controls that provide access to algo and library management commands.
2. **Block Panel**: Collection of functional blocks to add to your algo.
3. **Canvas**: Work area for creating your algo.
4. **Block Properties**: Panel for specifying functionality and characteristics of the selected block.
5. **Information Panel**: Retractable area to provide access to view algo design issues, manage algo variables, and monitor algo alerts.

### Toolbar

The ADL Designer’s toolbar contains menus and controls to provide access to algo and library management commands.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer-toolbar.png)

In addition to menus, the ADL Designer’s toolbar contains:

1. **Algo Navigation**: Controls for moving between parent and child algos.
2. **Algo Controls**: Controls for compiling and running your algo.
3. **Bookmarks**: User-defined bookmarks for displaying specific sections of the algo.
4. **Complile options**: Options for compiling algos automatically or manually.
5. **Algo Settings**: Settings that indicate the side for orders submitted by the algo and control whether the algo responds to market state changes.

#### Bookmarks menu

The **Bookmarks** menu contains a collection of user-defined views of an algo. Bookmarked views are typically used for algos that are significantly larger than the visible canvas, as they allow you to save views of different portions of an algo in the visible canvas. Clicking a bookmark will zoom your canvas to the saved view.

The following example uses three user-defined bookmarks to display the entry order portion of the algo, the exit order portion, and the whole algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-bookmarks-intro.png)

The user-defined **Exit Order** bookmark displays a zoomed-in portion of the algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-bookmark-select.png)

For more information on using bookmarks, see [Managing views with bookmarks](../task-adl-basic-concepts/working-with-the-adl-designer-canvas.md).

### The Canvas

The canvas is the working area for designing an algo. You can add different types of blocks to the canvas and create connections between them. When the algo is compiled, ADL generates the necessary code that represents the algo inputs, logic, and outputs.

The canvas provides some basic functionality for designing your algo, including:

* Adding blocks
* Selecting multiple objects
* Moving blocks
* Copying and deleting blocks
* Connecting blocks

The canvas right-click context menu allows you to:

* Scale the canvas such that the entire algo is visible on the canvas
* Load a block library to make saved group blocks available
* Paste previously-copied objects onto the canvas

### Blocks Panel

The Block Panel contains the list of blocks, organized by function, that can be dragged and dropped onto your canvas to build your algo.

The top of the Block panel contains a Search field that filters the list of available blocks based on the search string. It can also be used to locate specific block or location within your algo.

* Show only blocks whose names contain the string.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-block.png)
* Show Field blocks with the field name already specified when you add it to the canvas.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-field.png)
* Show a Number block pre-populated with specified numeric value.

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-number.png)
* Scroll the canvas to display a named block (start with an “@”).

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-blockname.png)
* Scroll the canvas to a previously-saved bookmark (start with a period “.”).

  ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-bookmark.png)

### Block properties

Each ADL block has a collection of settings that determine its name and characteristics that impact the block’s functions. Selecting a block displays its specific settings in the **Block Properties** panel, similar to the following for a [Instrument](../../../trading-blocks/instrument-block.md) block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-block-properties-instrument.png)

### Information Panel

The Information Panel provides information about algo design issues, algo variables, and algo alerts.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer-information-panel.png)

The Information Panel provides information about your algo in the following tabs:

* **Problems** displays issues with the current algo design, such as missing required information or connections.
* **Exports** lists the values that will be displayed within the [Algo Dashboard](../../../../../trade-kb/reference/algo-trading/algo-dashboard/description-algo-dashboard/algo-dashboard-overview.md) and [Autotrader](../../../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md) widgets in the [Trade](https://library.tradingtechnologies.com/trade/index.html) application. The order in which values are displayed in these widgets can also be specified.
* **Variables** shows the blocks in the algo that are designated as user-defined variables whose values can be modified when testing and debugging an algo.
* **Alerts** displays the alerts triggered by any [Alert](../../../miscellaneous-blocks/alert-block.md) blocks in the algo.
* **Settings** displays the available settings for the algo.
  + **Show algo order on ladder**: Displays parent [OTA (Order Ticket Algo)](../../advanced-concepts/description/order-ticket-algos-ota.md) orders in an MD Trader widget
  + **Ignore market state**: Sets whether to ignore changes in the market state
  + **Synthetic Order Algo (SOA)**: Identifies the algo as a [Synthetic Order Algo (SOA)](../../advanced-concepts/description/synthetic-order-algos-soa.md) that can be launched from MD Trader.
  + **Launchable OMA (as OTA)**: Allows an OMA algo to be launched from MD Trader in order-builder mode. For information about launching OMAs, refer to [Order Management Algos (OMA) Overview](../../../../../trade-kb/reference/algo-trading/order-management-algos-omas/order-management-algos-oma-overview.md).

←[Previous PostAlgo design fundamentals overview](algo-design-fundamentals-overview.md)

[Next PostBlocks](blocks.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer-toolbar.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-bookmarks-intro.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-bookmark-select.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-block.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-field.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-number.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-blockname.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-search-bookmark.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-block-properties-instrument.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adl-designer-information-panel.png
