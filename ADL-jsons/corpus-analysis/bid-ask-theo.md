# Bid/Ask Theo

Quote a two-sided market around an operator-supplied theoretical bid and ask. 659 blocks, 21
subgraphs, three levels deep, 18 user variables.

**This doc carries the full analysis of the four-algo "theo family"** — `Bid/Ask Theo`,
[single-theo.md](single-theo.md), [reference-market.md](reference-market.md) and
[direct-entry.md](direct-entry.md). All four are the *same quoting engine* with a different
price source bolted on the front: fourteen named Groups, identical block-for-block across all
four, plus 7 `Note` blocks of TT's own commentary that between them explain the architecture
better than anything else in the corpus. The other three docs cover only their differences and
point here.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Bid_Ask Theo.adl.json` |
| Algo id | `9f5b06d1-1d2d-4907-b39e-84333888aec2` |
| Last modified | 2025-10-10 21:22:56 UTC |
| Size | 1,175,822 bytes |
| Flat blocks / true blocks | 115 / **659** |
| Subgraphs / max depth | 21 / **3** — joint-deepest in the corpus, with its three siblings |
| Edges | 586 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta` absent |

**[V]** All four family members were saved within nine minutes of each other on 2025-10-10, and
all four export the **same block GUID** for `Net Pos`
(`839a0771-c7a6-467d-b9b6-892e061124e2`). **[I]** They are branches of one canvas, not four
independent designs — which is exactly the cross-file GUID sharing the format spec warns about
(§3: 571 of 3,011 GUIDs appear in more than one file). **Never key anything by GUID across
these four.**

## The family

**[V]** Fourteen Groups appear in all four files with identical block counts:

| Group | Tier | Blocks | Purpose **[I]** |
|---|---|---:|---|
| `Orders` | RED | 476 (480 in Single Theo) | the virtualized quoting engine, one instance per side |
| `Order` | RED | 231 (233 in Single Theo) | one managed order with throttling and requote |
| `Alerts` | AMBER | 68 | the entire operator-messaging layer, no ports |
| `Group2` | AMBER | 64 | order-quantity calculation |
| `SafeToPlaceOrder` | RED | 56 | the master permission boolean |
| `CalculatedOrder` | AMBER | 37 | join-the-market price adjustment |
| `Mkt Price` | AMBER | 22 | the market excluding my own order |
| `PriceOrQtyChanged` | AMBER | 9 | change detector |
| `DOB` | RED | 8 | order placement |
| `Group4`, `Group0` (×2) | AMBER | 8, 8 | cover-order virtual blocks |
| `Group5`, `Group0` | GREEN | 6, 6 | **the virtual-boundary event bridge** |
| `DESIRED_QTY`, `InsideMarket`, + 3 more `Group0` | AMBER | 5 each | side selectors |

**[V]** Only `Orders` and `Order` differ between files, and only in
[single-theo.md](single-theo.md) (+4 and +2 blocks).

## What TT says about it

**[V]** Seven `Note` blocks, verbatim. Four of them are load-bearing:

> *"This logic creates two instances of the same core pricing algo, one for the buy-side and one
> for the sell-side."*

> *"Since this logic will be created for both buy and sell orders, these group blocks above
> internalize all of the `if buy` logic so that we can keep the other pricing logic clean
> elsewhere."*

> *"Because crossing a virtual block boundary with a discrete jump block will create **new
> instances** of the virtual block, and I needed to know whenever the user clicks either the
> Requote or Reset buttons, which generate discrete events, I use this mechanism to transmit the
> event to each virtual block instance."*

> *"Probably the most interesting part of this algo, this is the calculation of the order
> quantity to be fed into the `Order Block`. It takes into account (1) the requote-topper
> calculation which will be set if the user manually or automatically requotes, (2) the `reset
> memory` which will be calculated if the user ever `resets` the open position, and (3) the
> currently open net position. It will further compare the current calculated price and if it is
> through the market and the user has `dont cross market` enabled, it will set the order quantity
> to zero."*

The other three cover `User defined variables`, `Cover Orders`, and the join-market logic:

> *"This logic accomplishes two things: (1) if the order is outside of the best market and `join
> best` is set to true, it will set the price to equal the best price. (2) If the order is the
> only order at the best market (i.e. alone), it will move the price to whatever the next best
> price is in the market."*

## The three ideas worth stealing

### 1. Side polymorphism — the 5-block selector Group

**[V]** Five Groups share one shape: three inbound jumps (an ask value, a bid value, and
`Msg:isBuy`), no input ports, one output port of type **`generic`**:

| Group | Output port | Jumps in |
|---|---|---|
| `InsideMarket` | `Price` | `Market Ask`, `Market Bid`, `Msg:isBuy` |
| `DESIRED_QTY` | `qty` | `Ask Qty`, `Bid Qty`, `Msg:isBuy` |
| `Group0` | `Desired Price` | `Calculated Ask Prc`, `Calculated Bid Prc`, `Msg:isBuy` |
| `Group0` | `DepthMktPrice` | `Index Ask Price`, `Index Bid Price`, `Msg:isBuy` |
| `Group0` | `Market Qty` | `M Ask Qty`, `M Bid Qty`, `Msg:isBuy` |

**[I]** Each is an `IfThen` and its wiring, wrapped. Downstream logic asks for *"the price"* or
*"the quantity"* and gets whichever side this instance is running — so the whole 476-block
quoting engine is written once, side-agnostically, and instantiated twice. TT's `Note` says
exactly this: *internalize all of the `if buy` logic so that we can keep the other pricing logic
clean elsewhere.*

**[I] This is the single most copyable structural idea in the corpus for anyone building a
two-sided algo.** The alternative — `IfThen(isBuy, …)` scattered through the graph — is how a
two-sided algo becomes unmaintainable. Five blocks, one `generic` output, one name that says
what it means.

**[V] `generic` is a real Group port type** (format spec §3: 40 occurrences), alongside
`message`, `real`, `bool` and `string`. **[I]** It corresponds to ADL's yellow *variable* ports,
which take their type from the first thing connected
([block-catalog](../../adl-kb/guides/block-catalog.md)) — which is what lets one selector Group
serve prices and quantities alike.

### 2. Crossing a virtual boundary with an event

**[V]** Two GREEN Groups, 6 blocks each, with the same signature — **in `real`, out `message`**:

| Group | Output |
|---|---|
| `Group5` | `RequoteEvent` |
| `Group0` | `ResetPosEvent` |

**[V]** And TT's `Note` explaining why they exist: *crossing a virtual block boundary with a
discrete jump block will create new instances of the virtual block.*

**[I] This is a documented ADL behaviour that appears nowhere in adl-kb.** adl-kb states only
that `Jump` blocks *cannot* cross a virtual boundary
([block-catalog](../../adl-kb/guides/block-catalog.md)); TT's note describes the subtler failure
— attempting it **spawns instances**, because a discrete message arriving at a virtual Group is
precisely what spawning means. So a UI button press cannot simply be jumped into every running
instance.

**The bridge, and it is six blocks:**

1. outside, count the events into a `ValueAccumulator` — a **continuous** number;
2. `Jump` the *number* across the boundary (continuous values jump freely);
3. inside, detect the change and regenerate a discrete message from it.

**[I]** Convert event → level → event. Any time you need to notify every instance of a virtual
Group that something happened, this is the mechanism, and both instances of it here are
**GREEN** — one `real` in, one `message` out, nothing else:

```bash
python tools/patterns.py --extract "Group5" --from "Bid_Ask" -o event-bridge.json
```

### 3. The market excluding my own order

**[V]** `Mkt Price` (AMBER, 22 blocks, out `generic` port named **`Without Me`**), fed by
`Index Ask/Bid Price`, `M Ask/Bid Qty`, `InsideMarket:Price`, `Order:WorkPrc`, `Order:WrkQty`
and `Msg:isBuy`.

**[I]** It answers *"what would the best price be if my own order were not there?"* — using the
order's own working price and quantity to subtract itself out, falling back to the next depth
level when it is alone at the touch. TT's `Note` on `CalculatedOrder` describes the consumer:
if my quote is alone at the best, move to the next best price rather than quoting against
myself.

**[I] Every market-making design needs this and it is not obvious.** Leaning on a market that
consists of your own order is a feedback loop; the fix requires depth-by-index reads plus your
own working state, which is why the Group needs eight inbound jumps. **[V]** It appears
byte-identical in all four family files.

## The rest of the engine

**[V]** Composition, top down:

```
Orders (virtual, 476 blocks) - one instance per side
  Order (231 blocks)              one managed exchange order
    DOB (8)                       placement
    Group5 / Group0 (6 each)      the event bridges
  Group2 (64)                     order quantity: requote-topper + reset memory + net pos,
                                  zeroed if the price is through the market and
                                  "Dont Cross Market" is on
  SafeToPlaceOrder (56)           one boolean gating placement, 16 inbound jumps
  CalculatedOrder (37)            join-the-market price adjustment
    Mkt Price (22)                the market without me
      InsideMarket (5)            side selector
  PriceOrQtyChanged (9)           requote trigger
  Alerts (68)                     operator messaging, no ports at all
  Group0 / Group4 (8 each)        cover orders, virtual, one per fill
```

**[V] `Order` has 18 ports** — 8 in (`Instrument0` string, `IsBuy` bool, `PriceThrottle`, `TIF`,
`price`, `qty` real, `Use C/R`, `enabled` bool) and 10 out (`AddOK`, `ChgOK`, `ChgReq`, `DelOK`,
`Fills`, `Exit Delete`, `price requote` message; `CumQty`, `WorkPrc`, `WrkQty` real). **[I]**
That is a complete, explicit order-management interface — the shape to imitate if you ever wrap
your own order handling in a Group.

**[V] `Alerts` has no ports at all** — 11 inbound jumps, 2 outbound (`Pull Buy`, `Pull Sell`).
**[I]** The entire operator-messaging layer is a jump-addressed subsystem. Same shape as
`GTD Pause Logic` in [with-a-tick.md](with-a-tick.md), at ten times the size, and it means the
alerting layer can be developed without touching the trading graph.

## Stop gaps

**[V]** This is the corpus's most complete safety layer, and every name below is quoted from the
format spec §7 — this is where those names live.

| Guard | Detail |
|---|---|
| `Terminal` ×4 — **all `pause`** | `Net Pos Exceeds Max Pos` · `Max Pos = 0` · `Self Trade Prevention` · `Cover order setting violation` |
| `Alert` ×8 | `Cross Attmepted` (sic) · `Net Pos Exceeds Max Pos` · `Max Pos = 0` · `Unable to requote Buy` / `Sell` · `Order Prices Crossed` · `Cover order setting violation` · `"Order Cancelled - click Requote to resume quoting"` |
| `Stopwatch` ×4 | **`Min 25ms`** (an `IF` formula flooring the user's throttle) · `QuoteDelay` · `100` · `10` |
| `Exit` ×1 | in the cover-order virtual Group |
| Bounds | `Quote Throttle` `[100, 99999999]`, default 100 — the only bounded variable of the 18 |
| `IsNumber` | **[V]** none |
| `MarketState` | **[V]** none; `ignoreMarketState: false` |

**[V] Four `Terminal` blocks and every one of them pauses.** Same stance as
[market-base.md](market-base.md): an algo holding inventory should never disappear.

**[V] `Alert` and `Terminal` share names three times** — `Net Pos Exceeds Max Pos`,
`Max Pos = 0`, `Cover order setting violation`. **[I]** That is the §7 idiom read straight off
the file: one condition drives both, the `Alert` tells the human and the `Terminal` stops the
algo. The five Alert-only names are the softer tier — warnings that do not kill.

**[V] `Min 25ms`** is the ADL `Stopwatch` floor
([gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md)) enforced as a named block
inside production code, on top of the `minValue: 100` bound on the parameter. **[I]** Three
floors again, as in [market-base.md](market-base.md).

**[I] The gap: no `IsNumber`, with `Index Ask/Bid Price` depth reads feeding `Mkt Price`.**
adl-kb is explicit that an index beyond available depth returns **`NaN` for price fields**
([block-catalog](../../adl-kb/guides/block-catalog.md)), and those values flow into the price
calculation and thence to an order. [market-base.md](market-base.md) — the same quoting problem,
by the same authors — guards exactly these reads with `Bid Depth?` / `Ask Depth?` and reports
*"no existing market to lean on"*. **[I] The theo family does not.** Whether something upstream
makes the read safe is **[U]**; the guard costs two blocks and the corpus contains a worked
example of it. **If you transplant `Mkt Price`, add it.**

## Reuse

**[V]** 21 Groups. The tier spread is the lesson: **2 GREEN, 15 AMBER, 4 RED**, and the RED ones
are the big ones (`Orders` 476, `Order` 231, `SafeToPlaceOrder` 56, `DOB` 8).

```bash
python tools/patterns.py --show "Mkt Price"
python tools/patterns.py --extract "Group5"       --from "Bid_Ask" -o event-bridge.json
python tools/patterns.py --extract "InsideMarket" --from "Bid_Ask" -o side-selector.json
python tools/validate.py event-bridge.json
```

> **[V] `Alerts`, `Mkt Price`, `CalculatedOrder`, `PriceOrQtyChanged`, `DESIRED_QTY` and
> `InsideMarket` are byte-identical across all four family files** — the format spec's §10
> evidence that TT transplants its own Groups. Extract from any of the four; they are the same
> bytes. `patterns.py` deduplicates them, which is why its index reports "4 files".

**[I] The AMBER tier dominates here for one structural reason: this family routes almost
everything by jump.** `SafeToPlaceOrder` needs 16 inbound jumps, `Orders` needs 26. None of
those are hard — they are named values like `Max Pos` and `Bid Qty` — but there are a lot of
them, and `patterns.py --extract` will list every one in its manifest. Budget the wiring.

Worth taking, in ascending cost:

| Take | Tier | Blocks | Why |
|---|---|---:|---|
| **Virtual-boundary event bridge** | GREEN | 6 | the only way to notify running virtual instances of a UI event; TT's `Note` is its only documentation |
| **Side selector** | AMBER | 5 | write the engine once, run it twice; `generic` output |
| **`PriceOrQtyChanged`** | AMBER | 9 | requote-trigger change detector |
| **`Mkt Price` — "without me"** | AMBER | 22 | do not lean on your own order (add an `IsNumber`) |
| **`CalculatedOrder`** | AMBER | 37 | join-best and step-off-alone price adjustment |
| **`Alerts`** | AMBER | 68 | a complete portless messaging subsystem addressed entirely by jump name |
| **`Group2` — quantity calc** | AMBER | 64 | requote-topper + reset memory + net position, zeroed when crossing is forbidden |
| **`Order`** | RED | 231 | an 18-port managed-order interface — study the port list even if you do not transplant it |

## Jump inventory

**[V]** 95 jumps → 174 landings. The naming is the family's spine: `Msg:isBuy` reaches every
side selector, `Calculated Ask Prc` / `Calculated Bid Prc` reach every price consumer, and the
user variables (`Max Pos`, `Bid Qty`, `Ask Qty`, `Quote Throttle`, `TIF`,
`Dont Cross Market`, `Use Cancel/Replace`, `Manual Requote`, `Enable Cover Order?`) are jumped
into the Groups that need them rather than ported.

**[I] That last choice is what makes 15 of 21 Groups AMBER**, and it is a real trade-off: jumps
keep the canvas readable and the ports few, at the cost of making every Group depend on names
that are invisible in its signature. `patterns.py`'s AMBER tier exists precisely to price it.
For your own designs: **jump user variables if the Group is not meant to travel; port them if it
is.**

## The price source — what makes this one "Bid/Ask"

**[V]** Two `Price` blocks (`Theo Bid`, `Theo Ask`) plus `Bid Offset` / `Ask Offset` Numbers and
a second `Instrument2`. **[I]** The operator supplies both sides of a theoretical market
independently, each side is offset, and the result becomes `Calculated Bid Prc` /
`Calculated Ask Prc` — the two jumps the shared engine consumes.

Compare: [single-theo.md](single-theo.md) derives both from one price,
[reference-market.md](reference-market.md) derives both from another instrument's market, and
[direct-entry.md](direct-entry.md) takes both literally with no offsets at all.

## Related

[single-theo.md](single-theo.md) · [reference-market.md](reference-market.md) ·
[direct-entry.md](direct-entry.md) — the other three family members.
[market-base.md](market-base.md) is the same quoting problem written flat, with the `IsNumber`
depth guards this family omits.

**Cited from:** [single-theo.md](single-theo.md), [reference-market.md](reference-market.md) and
[direct-entry.md](direct-entry.md) — all three defer their shared-engine analysis here ·
[minvol.md](minvol.md) for the per-side throttles · [market-base.md](market-base.md) and
[with-a-tick.md](with-a-tick.md) for the depth-guard gap and the readiness gate.
