---
title: Automating a Fixed Income Futures Hedge Order
category: adl-overview
source: https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/case-studies-advanced-concepts/automating-a-fixed-income-futures-hedge-order/
---

# Automating a Fixed Income Futures Hedge Order

> Category: **ADL Overview, Concepts & Tutorials** · [Source](https://library.tradingtechnologies.com/adl/adl-overview/advanced-concepts/case-studies-advanced-concepts/automating-a-fixed-income-futures-hedge-order/)
>
> **Interpreted in:** [Design Patterns & Recipe Index § Exits and position management](../../../../guides/design-patterns.md#exits-and-position-management)

### Case Study Overview

In this case study, a fund manager is looking to automatically hedge their notional cash exposure in Fixed Income
using the futures market to remain as delta neutral as possible. The fund manager executes bilaterally, a notional
value of EUR 10 million German 10-year Bunds, through a bank’s fixed income liquidity provider and is now long this
exposure. In order to offset the exposure, the fund manager creates a workflow to automatically execute, at market,
a futures position through the TT platform.

Within this case study, we will explain a simple method by which TT users with no programming ability can utilize [Excel](../../../../../trade-kb/reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel.md)
to drive a user defined value into an [ADL](https://www.tradingtechnologies.com/trading/algo-trading/adl/) algo via TT’s [Autotrader](../../../../../trade-kb/reference/algo-trading/autotrader/description-autotrader/autotrader-overview.md)
functionality in order to execute a trade by triggering a True condition.

### Creating the ADL Algo Logic

Within this example ADL algo, a sell side market order will get placed as soon as a quantity > 0 is defined.

A condition is also created whereby only a value greater than 0 will trigger a True boolean in order for a child
order to get placed. The IfThen0 block below states when 0 > 0, this will be True, otherwise False. So a value > 0
within the Number block named “qty” will trigger the condition for child order placement to be True. It is important
for this “qty” Number block to be user-defined, so a value can be driven into TT’s Autotrader as a user-defined
variable.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-submit-order.png)

We have further downstream logic from the Order Block to extract the fill quantity as an Export value, so the fund
manager can view his futures exposure back into Excel.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-extract-fill-qty.png)

Overall, the ADL algo logic looks like this:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-full-algo.png)

Note Within this example algo, hedge execution is only for the sell side. We
are assuming the Fund manager will only execute a positive notional value (long position) in the cash Bond.

Amendments to the example algo could be achieved in order to facilitate both buy and sell side executions.

### Excel Setup

Within Excel, the notional value of the trade will need to be pulled into a cell. Once this notional value is
present, the user can then use Excel to drive the underlying futures calculation that is required to attempt a delta
neutral hedge to the cash bond exposure. This can be achieved by simply dividing the notional cash exposure of the
bond by the notional value of one bond. Please note, for the purposes of this case study, we have not considered any
conversion factor values in the notional value calculation, i.e. Cheapest to Deliver (CTD) bond.

For example:

EUR 10,000,000 notional value of Bunds / EUR 100,000 notional value of 1 futures contract in the Bund = 100 lots

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-excel.png)

Using the above formula in cell F2, a conditional IF formula was required to output 0 if the notional quantity (cell
B2) was below the value of the underlying notional (cell C2). As cell F2 is used to drive the order quantity within
the ADL algo, as well as the True/False condition into the ADL algo’s Order Block, this conditional IF formula is
required to prevent an erroneous calculation. As a value of EUR 10,000,000 was placed in cell B2, this successfully
calculated the equivocal futures quantity required as 100 lots.

### Excel to Autotrader Setup

Once the ADL algo has been [deployed](../../adl-basic-concepts/description-adl-basic-concepts/algo-deployment-and-approvals.md), this will be accessible within the TT platform. Using TT’s Autotrader widget, we
select the algo then stage an instance by clicking on the “+ Add row” button.

We will need to define an account and futures contract within this algo instance on Autotrader, then using the [Copy
Link to TT](../../../../../trade-kb/reference/algo-trading/excel-integration-with-tt/task-excel-integration-with-tt/linking-sharing-data-between-autotrader-and-excel.md) function from Excel, copy the Equivocal Futures (lot) value (Cell F2) and paste into the user-defined
variable qty cell within Autotrader. You will see the cell turn green to indicate the dynamic linking of these two
cells:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-excel-formula.png)

### Launching the Algo

Once the above has been set up, the algo instance needs to be [launched](../../../../../trade-kb/reference/algo-trading/autotrader/task-autotrader/launching-an-algo-in-autotrader.md). This is done by highlighting the algo
instance row in Autotrader and pressing the play button. Once launched, you will see the Status of the algo instance
go into a “Running” state:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-autotrader.png)

### Hedge Execution

Within the Excel sheet, once there’s an update to Cell F2 (via notional value input into cell B2), this will trigger
True conditions within the algo to execute a child order, at market.

Per the above requirements from the Fund manager, he confirms a bilateral trade of long EUR 10m notional of the 10
year German Bund. This EUR 10m value is propagated into cell B2, which downstream executes an autohedge sell order,
at market, in the equivocal FGBL Sep23 futures contract:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-execution.png)

You can see the green qty cell in Autotrader update to a value of 100 based off the number in cell F2 within the
spreadsheet.

The fund manager’s position is now long EUR 10m of the German cash 10-year Bund and short 100 lots of the FGBL futures. Without factoring a notional conversion factor, the fund manager is now hedged.

### Alternative Setup Options

TT .NET SDK includes an Application Programming Interface (API) that provides developers with the ability to create high performance applications that communicate with the TT platform. Specifically, applications can subscribe for prices, route orders, and receive fills. A developer can therefore code a solution whereby once the cash bond is booked, this automatically submits a hedge order on TT.

Similarly, developers can utilize FIX order routing to automate a solution via an application to auto hedge exposure on TT.

[Next PostGenerating Position in Queue During Pre-open](generating-position-in-queue-during-pre-open.md)→

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-submit-order.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-extract-fill-qty.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-full-algo.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-excel.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-excel-formula.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-autotrader.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/ac-fixed-income-futures-hedge-execution.png
