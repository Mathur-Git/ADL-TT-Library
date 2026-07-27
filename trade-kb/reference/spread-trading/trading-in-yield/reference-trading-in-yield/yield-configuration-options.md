---
title: Yield configuration options
category: Spread Trading
source: https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/reference-trading-in-yield/yield-configuration-options/
---

# Yield configuration options

> Category: **Spread Trading** · [KB Home](../../../../README.md) · [Source](https://library.tradingtechnologies.com/trade/spread-trading/trading-in-yield/reference-trading-in-yield/yield-configuration-options/)

The following table shows the custom configuration options available when trading in yield on TT.

| Field | Description |
| --- | --- |
| Name | Use-defined name of the yield configuration |
| Contract | Opens the market explorer to search and find a fixed income instrument. |
| Yield Type | Shows required fields for the selected yield type. Valid values:  * FUT: Futures yield configuration * BOND: Bond yield configuration |
| Coupon Rate (%) | The annual coupon rate as a whole number (e.g, 8.5). |
| Conversion Factor | The product used for the Futures conversion factor calculation by the exchange.  **Note**: Currently, yield can only be configured for US Treasury Bonds products. |
| Maturity Date | The redemption date of the bond. This value must be less than the futures delivery date. |
| Settlement Type | The type of settlement date. Valid values: Absolute. |
| Settlement Date | The date when the security is traded to the buyer. This value must be less than delivery date. |
| Contract Date | The bond futures contract date. This value must be less than the maturity date. |
| Delivery Date | The date to deliver the contract/termination date. This value must be greater than the settlement date and less than the maturity date. |
| Optional Fields | |
| Basis Type | Select one of the following:   * Target IRP (Implied Repo Rate) * Gross Basis |
| Basis Value | The value of either the Target IRP or the Gross Basis as set by the Basis Type. This value must be a decimal between 0 and 1 (e.g., 0.0001). Calculated as follows:  * Target IRP: ((Sales Proceeds-Initial Investment)/Initial Investment)/Days Held\*360, where   * Initial Investment = Purchase Price of Bond (Including Accrued Interest)   * Sales Proceeds = Futures Price \* Conversion Factor + Accrued Interest of Bond on Futures Delivery Date + Coupon Income from Bond   * Days Held = Number of Days from Settlement Date to Futures Delivery Date * Gross Basis (Decimal): Price of CTD Bond – (Futures Price\*Conversion Factor)/32 |
|
| Coupon Frequency | The bond payment frequency. Set frequency equal to either Annual, SemiAnnual, Quarterly, or Monthly. |
| Day Count | Sets the number of days in the ‘year’ for the contract. This field provides the following values:   * 30/360 * 30/365 * 30E/360 * Actual/360 * Actual/365 * Actual/Actual |

