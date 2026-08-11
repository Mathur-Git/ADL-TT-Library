---
title: Introduction
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/introduction/
---

# Introduction

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/building-your-first-algo/introduction/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Exits and position management](../../../guides/design-patterns.md#exits-and-position-management) · [Design Patterns & Recipe Index § Testing](../../../guides/design-patterns.md#testing)

Welcome to the Building Your First Algo series. This series is designed to teach you the basics of ADL by demonstrating the construction of a basic Scalper algo.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-intro.png)

Over the course of this series you will create a Scalper algo designed to:

1. Submit an order to enter into a position.
2. Capture the fill price and fill quantity of your entry orders to calculate your average open price.
3. Submit an exit order a number of ticks above your average open price.

This series will also teach you how to use ADL and TT to test your algo logic in a simulated market.

The [Building the entry logic](lessons/building-the-entry-logic.md) section will demonstrate how to create the entry order and will cover:

* The different areas of the ADL interface.
* Adding blocks and setting their properties.
* Connecting block ports using edges.

The [Testing the entry logic](lessons/testing-the-entry-logic.md) section will cover testing the algo logic so far. You will:

* Use the titlebar’s Algo Controls to test and reset the algo.
* View the running algo simulation in both ADL and TT.
* Test the algos with different user inputs.

The [Capturing fills data](lessons/capturing-fills-data.md) section will show how to access information about your fills. This section will cover:

* The difference between continuous and discrete messages.
* ADL’s formula editor.
* Using math blocks to perform calculations.

The [Creating the exit order](lessons/creating-the-exit-order.md) section will define the exit order. You will:

* Use Jump blocks to more clearly see the algo.
* Test the completed algo in ADL and TT.

[Next PostBuilding the entry logic](lessons/building-the-entry-logic.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/bfa-scalper-algo-intro.png
