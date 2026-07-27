---
title: Yield Type Calculations
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/use-cases-trading-in-yield/yield-type-calculations/
---

# Yield Type Calculations

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/use-cases-trading-in-yield/yield-type-calculations/)

TT supports calculating the yield on futures and Treasury Bonds. For futures, you can change the type of yield calculation based on the configuration values.

## Forward Yield of Futures

This example shows calculating the yield of the cheapest-to-deliver (CTD) bond on the last delivery date using the current futures price of the ZF Mar21 contract. This is the yield to an investor who goes long on a futures contract at today’s price and takes delivery of the CTD bond on the last delivery date (i.e., Bloomberg “Forward Yield”, CME “Futures Yield”).

In this example, consider the following:

* The CTD price equals the current futures price multiplied by the conversion factor.
* The gross cash-futures Basis Value is zero.
* The settlement date is the last delivery date of the futures contract.

To calculate yield, open the **Edit Yield** dialog box from [the Yield widget, Autospreader, or MD Trader](../task-trading-in-yield/configuring-and-displaying-yield.md), and configure the following required fields:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-future-5.png)

For this configuration:

* Set the **Conversion Factor** to “ZF”.
* Enter the **Coupon Rate**, **Maturity Date**, and **Delivery Date** using the [cheapest to deliver](https://www.cmegroup.com/tools-information/quikstrike/treasury-analytics.html?redirect=/trading/interest-rates/invoice-spread-calculator.html) “5 yr” Treasury values.
* Set the **Settlement Date** equal to the **Delivery Date**.
* Set the **Contract Date**  to the first of the expiration month (e.g., ZF Mar21 = 3/1/21).
* In the **Basis Type** field select “Gross Basis”.
* Set **Basis Value** to “0”.

When this configuration is selected in MD Trader, the **Yield** column displays the instrument price in yield.



![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-futures-mdt-5.png)

## Yield of the CTD

The yield of the CTD bond is based on using the current futures price, the cash futures basis, and the next day settlement. This is the yield to an investor who buys the CTD bond at fair market value (i.e., Bloomberg “CTD Yield”). In this example,

* The CTD price is equal to the current futures price of the ZF Mar21 contract multiplied by the conversion factor less the cash-futures basis.
* The settlement date is next day business day.

To calculate yield for this example, open the **Edit Yield** dialog box from [the Yield widget, Autospreader, or MD Trader](../task-trading-in-yield/configuring-and-displaying-yield.md), and configure the following required fields:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-ctd-5.png)

For this configuration:

* Set the **Conversion Factor** to “ZF”.
* Enter the **Coupon Rate**, **Maturity Date**, and **Delivery Date** using the [cheapest to deliver](https://www.cmegroup.com/tools-information/quikstrike/treasury-analytics.html?redirect=/trading/interest-rates/invoice-spread-calculator.html) “5 yr” Treasury values.
* Set the **Settlement Date** equal to tomorrow (T + 1).
* Set the **Contract Date**  to the first of the expiration month (e.g., ZF Mar21 = 3/1/21).
* In the **Basis Type** field select “Target IRP”.
* Set **Basis Value** equal to the Target IRP value (e.g., .265)

When this configuration is selected in MD Trader, the **Yield** column displays the instrument price in yield.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-ctd-5-display.png)

## Yield of a Treasury Bond

The configuration of treasury bonds only requires the Coupon Rate, Maturity Date, and Settlement Date. Some exchanges provide this information on the instrument definition. This can be viewed by clicking Ctrl + Shift + X in MD Trader.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond-def.png)

For example, the “definition” field for CME\_BrokerTec 10 yr Bond contract includes the Symbol (UB10), Coupon (⅞ or 0.875), and Maturity (11/30 or Nov 2030) values.

To calculate yield for this example, open the **Edit Yield** dialog box from [the Yield widget, Autospreader, or MD Trader](../task-trading-in-yield/configuring-and-displaying-yield.md), and configure the following required fields:

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond.png)

For this configuration:

* Enter the **Coupon Rate** and **Maturity Date** from the instrument definition.
* Set the **Settlement Date** to tomorrow (T+1).

When this configuration is selected in MD Trader, the **Yield** column displays the instrument price in yield.

![](https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond-result.png)

### Images on page
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-future-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-futures-mdt-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-ctd-5.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-ctd-5-display.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond-def.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond.png
- https://library.tradingtechnologies.com/wp-content/uploads/2025/12/yield-use-bond-result.png
