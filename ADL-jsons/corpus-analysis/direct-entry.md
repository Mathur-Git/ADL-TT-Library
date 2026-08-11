# Direct Entry

Quote a two-sided market at two prices the operator types in directly. 646 blocks — the
**smallest** member of the theo family, and the one that shows what the shared quoting engine
costs with essentially no pricing logic in front of it.

The shared engine, its fourteen common Groups, its safety layer and the three architectural
ideas worth stealing are analysed once in **[bid-ask-theo.md](bid-ask-theo.md)** and not
repeated here. This doc covers the front end, which is almost nothing — and that absence is the
interesting part.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Direct Entry.adl.json` |
| Algo id | `bb2162c1-1b42-4032-a97f-3f925b529089` |
| Last modified | 2025-10-10 21:30:20 UTC |
| Size | 1,162,349 bytes |
| Flat blocks / true blocks | **102** / **646** — the family's smallest on both counts |
| Subgraphs / max depth | 21 / 3 |
| Edges | 576 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta` absent |

## The price source

**[V]** Two `Price` blocks — `Bid Prc` and `Ask Prc` — and **no offset variables at all**:

| | Bid/Ask Theo | Single Theo | Reference Market | **Direct Entry** |
|---|---|---|---|---|
| Price inputs | `Theo Bid`, `Theo Ask` | `Theo Price` | `Reference Instrument` + market | `Bid Prc`, `Ask Prc` |
| `Bid Offset` / `Ask Offset` | yes | yes | yes | **no** |
| Variables | 18 | 17 | 18 | **16** |

**[V]** The `Calculated Bid Prc` / `Calculated Ask Prc` jumps that every other family member
computes **do not exist in this file**. Their consumers are fed by `Bid Prc` / `Ask Prc` jumps
instead — the only place where the family's internal jump vocabulary changes.

**[V]** The arithmetic block census drops accordingly: 4 `Add` (family: 5), 4 `Subtract` (5),
**2 `Multiply`** (4–6), 28 `Number` (30–31), 93 `Jump` (95–98).

**[I]** So Direct Entry is the family with the pricing model removed. The operator is the model:
they type a bid and an ask, and everything else — throttling, requoting, joining the market,
position limits, cover orders, alerts — still runs.

## Why the empty front end is the useful observation

**[I] It puts a number on where the work actually is.** Take away the entire pricing layer and
646 of 659 blocks remain. Two prices in, and you still get:

- per-side, per-action throttling with a `Min 25ms` floor
- the "market without me" calculation so your quote does not lean on itself
- join-best and step-off-when-alone price adjustment
- order-quantity arithmetic reconciling requote-topper, reset memory and net position
- four `Terminal` pause conditions and eight `Alert` messages
- cover orders in virtualized Groups, one instance per fill
- external-modification handling, manual requote, cancel/replace as operator toggles

**[I] For anyone planning to build a quoting algo, that ratio is the estimate to carry:
the price model is ~2% of the block count. The other 98% is order management, and it is the
same 98% regardless of what you are quoting.** It is also the part the corpus already contains,
which is the whole argument for building on this family rather than beside it.

**[I]** A second reading: Direct Entry is the family's **test harness**. With the operator
supplying both prices by hand, every behaviour of the engine can be exercised deterministically
— push the bid through the market and watch `Dont Cross Market`; set it inside the best and
watch the join logic; set it wide and watch nothing happen. **[U]** Whether TT intended it that
way is not in the file, but it is how it is most useful before you trust a pricing model.

**[V]** One jump name is unique to this file: `Quote Fill Seq:output_1`. **[I]** A `Sequence`
output ordering the quote/fill path — present here and not in the siblings, which route the
same concern through the `Calculated *` chain that this file does not have.

## Everything else

**[V]** Identical to [bid-ask-theo.md](bid-ask-theo.md), which has the detail:

- the fourteen shared Groups, byte-identical, with tiers, ports and adoption costs — including
  the two **GREEN** virtual-boundary event bridges and the 5-block side selectors
- the same seven `Note` blocks, including TT's explanation of why a discrete jump cannot cross
  a virtual boundary
- 4 `Terminal` blocks (all **pause**), 8 `Alert` blocks, `Min 25ms`, `QuoteDelay`
- the `IsNumber` gap on the `Index Bid/Ask Price` depth reads
- `Quote Throttle` as the only bounded variable, `[100, 99999999]`
- the same exported `Net Pos` block GUID as all three siblings

```bash
python tools/patterns.py --show    "InsideMarket" --from "Direct Entry"
python tools/patterns.py --extract "Group5"       --from "Direct Entry" -o event-bridge.json
```

**[V]** `Orders` and `Order` here are the **pre-fix** versions (476 / 231 blocks). Take those
two from [single-theo.md](single-theo.md), which carries the fill-throttle repair.

**[I] But if you want the engine itself, start from this file rather than extracting Groups.**
`Orders` and `Order` are RED — 21 dangling formula references and 39 inbound jumps between them
— so transplanting them is not realistic (see [bid-ask-theo.md](bid-ask-theo.md)). The format
spec's §8 preference order says so directly: **transplant a Group first, modify an export
second, synthesize last.** For a quoting algo, "modify an export" means *this* export — the
family member with the least pricing logic to unpick before your own goes in.

## Related

[bid-ask-theo.md](bid-ask-theo.md) — the family analysis ·
[single-theo.md](single-theo.md) — the maintained head ·
[reference-market.md](reference-market.md) — the market-derived front end, and the better
starting point if your price comes from another instrument ·
[market-base.md](market-base.md) — the same quoting problem written flat, with the depth guards
this family omits.

**Cited from:** [bid-ask-theo.md](bid-ask-theo.md), [single-theo.md](single-theo.md) and
[reference-market.md](reference-market.md) as the family's minimal front end and the best base
for "modify an export".
