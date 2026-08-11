---
title: Adding, Connecting and Arranging Blocks
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/task-adl-basic-concepts/adding-connecting-and-arranging-blocks/
---

# Adding, Connecting and Arranging Blocks

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/adl-basic-concepts/task-adl-basic-concepts/adding-connecting-and-arranging-blocks/)

To build an algo you will need to drag and drop blocks onto the canvas, define their properties and connect blocks together with edges to define the flow of data.

### Adding blocks on the canvas

To add a block to the canvas:

1. In the **Blocks** panel locate, or [search for](../description-adl-basic-concepts/adl-designer.md), the block you want to place on the canvas.
2. Drag the block to the desired location on the canvas.

   ![Add block](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adding-block-1.png)
3. In the **Block Properties** panel, specify the values for the desired properties.

   ![Specify block properties](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adding-block-2.png)

   Any changes to the properties are reflected immediately in the block.

### Connecting blocks

ADL provides two methods of making connections between blocks:

* Drawing edges between block ports
* Using the Edge Finder to highlight potential edges

#### Drawing edges

To connect blocks by drawing the edges:

1. Press and hold the left mouse button on the output port of the source block; then drag the line endpoint to the desired corresponding port of the destination block. Note that the ports are color-coded to indicate the type of data being passed.

   ![Connecting valid ports](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-connecting-ports-1.png)

   **Note**: If you drag the line endpoint to the wrong type of input port, the preventative design feature shows an invalid connection symbol.

   ![Connecting invalid ports](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-connecting-ports-2.png)
2. Release the mouse button.

#### Using the Edge Finder to highlight potential edges

To display and choose a potential edge between blocks:

1. Press and hold the **Shift** key to display dashed lines for all potential edges.

   ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-1.png)
2. Do either of the following to create edges:
   * Left-click a dashed line to convert it to an edge.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-2.png)
   * Right-click any of the dashed lines to convert all the dashed lines to edges.

     ![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-3.png)

### Disconnecting blocks

To delete a connection between two ports, right-click on the line connecting the desired ports, and select **Delete**.

![Delete Connection](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deleting-connection-1.png)

### Arranging blocks around the canvas

To arrange or move blocks:

1. Select a block or group of blocks you want to move.
2. Drag the selected blocks to the desired location. If edges are connected to the moved blocks, those edges update as well.

### Selecting multiple blocks

To select multiple blocks:

Press the left mouse button and drag the mouse to define the region containing the blocks you want to select; then release the mouse button.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-select-blocks.png)

Alternatively, you can click the first block to select, then use **Ctrl**-click (**Cmd**-click for Macs) to add other blocks to the selection.

←[Previous PostWorking with the ADL Designer Canvas](working-with-the-adl-designer-canvas.md)

[Next PostUsing variable blocks for user input](using-variable-blocks-for-user-input.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adding-block-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-adding-block-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-connecting-ports-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-connecting-ports-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-2.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-edge-finder-3.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/abc-deleting-connection-1.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/adf-select-blocks.png
