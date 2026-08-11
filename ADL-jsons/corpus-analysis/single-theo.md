# Single Theo

Quote a two-sided market around **one** operator-supplied theoretical price, offset on each
side. 663 blocks — the largest member of the theo family, and **the one carrying the newest
fixes**.

The shared quoting engine, its fourteen common Groups, its safety layer and the three
architectural ideas worth stealing are analysed once in
**[bid-ask-theo.md](bid-ask-theo.md)** and not repeated here. This doc covers what is different,
which is the price source and four extra `Note` blocks that document a bug and its repair.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Single Theo.adl.json` |
| Algo id | `d6093c8e-0964-4fc9-bd3c-545240e62f9b` |
| Last modified | **2025-10-10 21:30:57 UTC** — the newest of the four, by 19 seconds over [reference-market.md](reference-market.md) and 8 minutes over [bid-ask-theo.md](bid-ask-theo.md) |
| Size | 1,180,396 bytes |
| Flat blocks / true blocks | 115 / **663** — the family's largest |
| Subgraphs / max depth | 21 / 3 |
| Edges | 586 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta` absent |

## The price source

**[V]** One `Price` block (`Theo Price`), `Bid Offset` and `Ask Offset` Numbers, one
`Instrument1`. Seventeen variables in all, one fewer than
[bid-ask-theo.md](bid-ask-theo.md) — which needs two `Price` blocks.

**[I]** The operator gives one fair value; the algo quotes `theo − Bid Offset` and
`theo + Ask Offset`. That is the ordinary market-making parameterisation, and it enforces a
constraint [bid-ask-theo.md](bid-ask-theo.md) cannot: the two quotes stay symmetric about a
single point and cannot silently invert.

**[V]** Everything downstream is the same. The engine consumes `Calculated Bid Prc` and
`Calculated Ask Prc` as jumps, and does not know how they were produced.

**[I] That separation is the family's real design lesson, visible only by comparing all four:
the price source is a replaceable front end, and the boundary between it and the engine is two
jump names.** If you build a quoting algo, define that boundary deliberately — you will want to
swap the pricing model without touching the order management.

## What is different inside

**[V]** Single Theo is the only family member whose shared Groups differ:

| Group | Single Theo | The other three |
|---|---:|---:|
| `Orders` (RED, virtual) | **480** blocks | 476 |
| `Order` (RED) | **233** blocks | 231 |

**[V]** Plus one extra jump name that no sibling has — `fill throttled:accVal` — and **11
`Note` blocks** against the family's 7. The four extra notes, verbatim:

> *"Quote on resume avoids the need to press the manual requote button after resume to, for
> example, get a previously throttled quote order to go in."*

> *"Fill Throttled is used to prevent fill throttle being ignored when join market requote
> happens. Used in state block with group0."*

> *"Fill Throttled=0 was added to state block to prevent fill throttle being ignored when a
> join market event occurs."*

> *"v002 added -qty increase fill throttle- check"*

**[I] Read together, these describe a real bug and its fix.** The engine has two independent
reasons to requote: the fill throttle (wait N ms after a fill before quoting again) and the
join-market logic (if my quote is outside the best and *join* is enabled, move it to the best —
see `CalculatedOrder` in [bid-ask-theo.md](bid-ask-theo.md)). A join-market event was
**bypassing** the fill throttle, so a fill immediately followed by a market move produced an
unthrottled requote. The repair was to add a `fill throttled` accumulator to the `State` block's
condition so both paths respect the same governor.

**[V] `v002 added -qty increase fill throttle- check`** is the only version marker anywhere in
the corpus. **[I]** Combined with the two fill-throttle notes and the four extra blocks, it
makes Single Theo the family's maintained head: the other three are older siblings that did not
receive the fix.

**[I] Two things follow for anyone reusing this family.**

1. **Take `Orders` and `Order` from *this* file, not from its siblings.** They are the only
   versions with the throttle fix. Everywhere else the four are byte-identical, so it does not
   matter which you extract from.
2. **The bug class is worth remembering independently of ADL.** Two code paths reaching the same
   actor, one of them checking the governor and one not, is the most common way a rate limit
   fails. The structural fix — put the governor's state into the shared `State` block's
   condition rather than in front of each path — is the right one.

**[V]** `Quote on resume` is the same concern [minvol.md](minvol.md)'s TT `Note` documents from
the other direction: a pause loses in-flight throttled state, so something must re-establish it
on resume. Here it is a quote-on-resume path; there it was an `everyStart` `Generator` clearing
a mutex. **[I]** Two independent files, two repairs, one underlying fact: **ADL pause/resume is
not transparent to timing state, and any algo with a `Stopwatch` in a pathway needs an explicit
resume story.**

## Everything else

**[V]** Identical to [bid-ask-theo.md](bid-ask-theo.md), which has the detail:

- the fourteen shared Groups, tiers, ports and adoption costs
- the three ideas worth stealing — side-selector Groups, the virtual-boundary event bridge, and
  `Mkt Price`'s "market without me"
- 4 `Terminal` blocks (all **pause**), 8 `Alert` blocks, `Min 25ms`, `QuoteDelay`
- the `IsNumber` gap on the `Index Bid/Ask Price` depth reads
- `Quote Throttle` as the only bounded variable, `[100, 99999999]`
- the same exported `Net Pos` block GUID as all three siblings

```bash
python tools/patterns.py --show    "Orders" --from "Single Theo"
python tools/patterns.py --extract "Orders" --from "Single Theo" -o quoting-engine.json
python tools/patterns.py --extract "Order"  --from "Single Theo" -o managed-order.json
```

**[V]** Both are **RED** — `Orders` leaks 11 formula references and needs 26 inbound jumps;
`Order` leaks 10 and needs 13. **[I]** Neither is a realistic transplant; extract them to
*read*, and take the small GREEN and AMBER parts listed in
[bid-ask-theo.md](bid-ask-theo.md) instead.

## Related

[bid-ask-theo.md](bid-ask-theo.md) — the family analysis, and the two-sided-theo variant ·
[reference-market.md](reference-market.md) — theo derived from another instrument ·
[direct-entry.md](direct-entry.md) — no theo at all ·
[market-base.md](market-base.md) — the same quoting problem written flat, with depth guards ·
[minvol.md](minvol.md) — the other file whose `Note` blocks document a pause/resume defect.

**Cited from:** [bid-ask-theo.md](bid-ask-theo.md), [reference-market.md](reference-market.md)
and [direct-entry.md](direct-entry.md) — all three send you here for `Orders` and `Order`,
the only versions carrying the fill-throttle fix · [minvol.md](minvol.md) for the
pause/resume state problem.
