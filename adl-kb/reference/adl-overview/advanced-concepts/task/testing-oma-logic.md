---
title: Testing OMA Logic
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/testing-oma-logic/
---

# Testing OMA Logic

> Category: **ADL Overview, Concepts & Tutorials** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/task/testing-oma-logic/)

### Testing OMA Logic from the ADL Design Canvas

First thing is you build your normal OMA algo logic. This can include your management logic of the existing manual order, or your Hedge Logic for when that manual order gets filled. However and whatever it is that you build for your OMA. Now you need to test it right? But how do you test an OMA algo that needs a manual order to attach to?

The below screenshot uses a Funnel Block that allows you to add a basic “Test Order” type logic that you can turn on and off. When you turn it ON, and click the PLAY button on the canvas, the algo submits a “test order” allowing you to see how your OMA Hedge Logic works downstream from the Single Order Container Block.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-test-oma-logic.jpg)

←[Previous PostSummarize Volume](summarize-volume.md)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-test-oma-logic.jpg
