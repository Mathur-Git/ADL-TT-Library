# Formula Editor Reference

Formulas are how ADL blocks compute values from message fields and other blocks' outputs. They appear in
block properties as a `Formula` / `Formulas` / `Qty Formula` / `Condition Formula` field.

→ [Formula Editor](../reference/adl-overview/advanced-concepts/description/formula-editor.md)

[ADL KB Home](../ADL-KB-Home.md) · [Block Catalog](block-catalog.md) · [Core Semantics](core-semantics.md) · [Patterns](design-patterns.md) · [Gotchas](gotchas-and-limits.md)

---

## Blocks that take formulas

| Category | Blocks |
|---|---|
| Trading | [Discrete Order](../reference/trading-blocks/discrete-order-block.md) (price, qty, condition, TIF, order type) |
| Discrete | [Branch](../reference/discrete-blocks/branch-block.md) · [State](../reference/discrete-blocks/state-block.md) · [Value Extractor](../reference/discrete-blocks/value-extractor-block.md) · [Value Injector](../reference/discrete-blocks/value-injector-block.md) · [Value Accumulator](../reference/discrete-blocks/value-accumulator-block.md) · [Value Bucket](../reference/discrete-blocks/value-bucket-block.md) · [Moving Average](../reference/discrete-blocks/moving-average-block.md) · [Discrete Min / Max](../reference/discrete-blocks/discrete-min-max-blocks.md) |
| Arithmetic | [Formula](../reference/arithmetic-blocks/formula-block.md) |
| Misc | [Alert](../reference/miscellaneous-blocks/alert-block.md) · [Stopwatch](../reference/miscellaneous-blocks/stopwatch-block.md) |

---

## Syntax

**Operators**

- Arithmetic: `+` `-` `*` `/` `%`
- Comparison: `<` `<=` `>` `>=` `==` `!=`
- Logical: `AND` `OR` `!` `IF`
- Grouping: `( )`

**Two reference sigils — this is the core of the editor:**

| Type | Sigil | Long form | Means |
|---|---|---|---|
| Message field | `#` | `{fieldName}` | a field of the **incoming discrete message** |
| Block connector | `@` | `[block.connector]` | a **continuous output port** of any block on the canvas |

Typing `#` lists available message fields; typing `@` lists blocks with continuous outputs.
Typing more characters filters the list. `@Analytics0-` drills into that block's ports.

> The editor displays at most **100** continuous output ports from any one block.

> In the [Formula](../reference/arithmetic-blocks/formula-block.md) block, referencing a connector
> creates an **implicit connection** — the block recalculates whenever that connector changes, with no
> visible edge on the canvas.

> The [Alert](../reference/miscellaneous-blocks/alert-block.md) block additionally accepts `"string"`
> literals joined with `+`, but **does not support the `IF` operator**.

---

## Message fields

Available via `#` / `{...}`, and as MsgInfoExtractor output connectors.

**Order fields**

| Field | Meaning |
|---|---|
| `limitPrice` | price of a new order |
| `orderQuantity` | total order quantity |
| `workingQuantity` | quantity still working |
| `fillPrice` | price of a fill |
| `fillQuantity` | quantity of a fill |
| `cumQuantity` | sum of fill quantities |
| `disclosedQuantity` | visible quantity of a disclosed order |
| `deletedQuantity` | cancelled quantity of a deleted order |
| `stopTrigger` | stop activation price |
| `orderType` | order type of the incoming order |
| `timeInForce` | TIF of the incoming order |
| `account` | account on the incoming order |
| `isSuspended` | order is in a Held state |

**Trade fields** (from [Time and Sales](../reference/trading-blocks/time-and-sales-block.md))

| Field | Meaning |
|---|---|
| `tradePrice` / `tradeQuantity` | last trade price / quantity |
| `tradeIsHit` | the trade hit the bid |
| `tradeIsTake` | the trade took the offer |
| `tradeIsUnknown` | exchange did not say which |
| `tradeIsOTC` | over-the-counter transaction |
| `tradeIsImplied` | occurred at an implied price |
| `tradeIsLeg` | matched a leg of an exchange-listed spread |

**Flags and metadata**

| Field | Meaning |
|---|---|
| `isBuy` | fill was a buy-side execution |
| `isTriggered` | order resulted from a trigger condition (stop triggered) |
| `isExternalEvent` | message originated outside the algo |
| `isQuotingOrder` | quote-leg message (Autospreader only) |
| `isHedgeOrder` | hedge-leg message (Autospreader only) |
| `instrument` | instrument on the message |
| `year` `month` `day` `hour` `minute` `second` `milliseconds` | timestamp parts (UTC) |
| `userField1..4` | four free slots, written by [Value Injector](../reference/discrete-blocks/value-injector-block.md), read by [Value Extractor](../reference/discrete-blocks/value-extractor-block.md) |

> Fields not relevant to the inbound message read as zero — a fill message has a real `fillPrice` but a
> zero `deletedQuantity`. Never assume a field is populated just because the port exists.

`userField1..4` are the **only** general-purpose way to carry a computed value out of a
[virtualized block](../reference/virtualized-blocks/rules-of-virtualization.md).

---

## Worked patterns

**Boolean constant** — output TRUE for downstream gating:
```
TRUE
```

**Counter** — in a [Value Accumulator](../reference/discrete-blocks/value-accumulator-block.md),
counts events rather than summing a field:
```
1
```

**Latch / toggle** — in a [Value Extractor](../reference/discrete-blocks/value-extractor-block.md),
outputs 0 before the first message and 1 after:
```
1
```

**Accumulate filled quantity:**
```
{fillQuantity}
```

**Exit price two ticks above the fill** (Value Extractor; `TickSize` is a
[Field](../reference/trading-blocks/field-block.md) block set to Min Price Increment):
```
{fillPrice} + 2 * [TickSize.out]
```

**Conditional** — is the opposite inside market at least two ticks above the fill?
```
IF( [BestAsk.out] >= {fillPrice} + 2 * [TickSize.out], TRUE, FALSE )
```

**Half the available bid quantity** (Discrete Order qty formula):
```
[BidQty.out] / 2
```

**Hedge-leg router** ([Branch](../reference/discrete-blocks/branch-block.md), Autospreader):
```
{isHedgeOrder}
```

**EPIQ trade-matching condition**
(from [Estimated Position In Queue](../reference/adl-overview/advanced-concepts/description/estimated-position-in-queue-epiq.md)) —
verbatim from the docs:
```
! tradeIsOTC AND tradePrice = MsgInfoExtractor0.limitPrice AND Order0 > 0
```

---

## Formula-driven order parameters

The [Discrete Order](../reference/trading-blocks/discrete-order-block.md) block takes its price, quantity
and enabling condition from formulas rather than ports. TIF and order type can be driven from
[Number](../reference/basic-blocks/number-block.md) blocks whose Variable Type is
`User Defined (TIF)` or `User Defined (Order Type)`, using these numeric codes:

**timeInForce** — 1 Day · 2 GTC · 3 At the opening · 4 IOC · 5 FOK · 6 Good till crossing · 7 GTDate ·
8 At the close · 9 Good through crossing · 10 At crossing · 13 Auction · 14 Good in session ·
15 Day plus · 16 GTC plus · 17 GTDate plus

**orderType** — 1 Market · 2 Limit · 3 Stop · 4 Stop limit · 5 Iceberg ·
20 Market with leftover as limit · 21 Market limit market with leftover as limit ·
30 Stop market to limit · 31 If-touched market · 32 If-touched limit · 33 If-touched market to limit ·
37 Limit post-only

---

## Guarding formulas

Formula output feeds real orders, so apply the [NaN rules](core-semantics.md#8-nan-is-contagious-and-destructive):

- Any division where the denominator can be zero needs a guard.
- Depth lookups beyond available levels return `NaN` for prices, `0` for quantities.
- A `NaN` price/qty at a trading block means **no order created** — or, for a working order,
  **the order is deleted**.

Guard either with [IsNumber](../reference/logic-blocks/isnumber-block.md) into the `on/off` port, or
inside the formula:
```
IF( [Denominator.out] != 0, [Numerator.out] / [Denominator.out], 0 )
```
