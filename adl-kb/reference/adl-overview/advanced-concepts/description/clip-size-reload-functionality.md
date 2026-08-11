---
title: Clip Size Reload Functionality
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/clip-size-reload-functionality/
---

# Clip Size Reload Functionality

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/description/clip-size-reload-functionality/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Order entry](../../../../guides/design-patterns.md#order-entry)

This article discusses how to get algos to resubmit orders or to continually
submit orders without needing to launch new instances of algos. There are
several ways a user can create or utilize this “reload functionality”. Here
are a couple easy ways to build some reload functionality type Library
Blocks.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-1.jpg)

#### Reload Logic

A user creates a Library Block with 3 Connector Inputs (Fills, Clip Size Qty, and Total Order Qty). First you want to compare the inputted Fills value and divide that against the Clip Size Qty input value. You then have this calculated value and round this number down to the nearest whole number in order to make sure not to have possible decimal values. This resulting calculated value is then multiplied by the Clip Size Qty input value. This resulting calculated value is then added to the Clip Size Qty input value again. The resulting calculated value give the user a RELOAD Qty value which accounts for any previous fills since the order was launched or started. This RELOAD Qty then feeds into a Math Block that is set to output the MIN value which compares this reload qty to the total order qty. The resulting outputted MIN value will be the actual RELOAD Qty to be fed into the Orders Block. This Math Block set to output the MIN value is how the Reload logic function will shut off….. once the comparison shows the Total Order Qty input is the MIN value vs. the Reload Qty input. This value feeds into the Qty input of the Orders Block and results in the Orders Block not submitting any further orders that will result in more than the initial Total Order Qty.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-2-2.jpg)

Reload Button Example

#### Reload Button Example

The below example is how to create a User Defined Variable “RELOAD BUTTON”. This will allow the User to manually trigger the algo to submit new orders when desired. This is accomplished by simply switching between TRUE/FALSE outputs from the Boolean Block. This in turn will trigger the internal logic as you see below…..

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-3-2.jpg)

←[Previous PostEstimated Position In Queue (EPIQ)](estimated-position-in-queue-epiq.md)

[Next PostTime and Timers in TT ADL](time-and-timers-in-tt-adl.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-1.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-2-2.jpg
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-clip-size-reload-functionality-3-2.jpg
