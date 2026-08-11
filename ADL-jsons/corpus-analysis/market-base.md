# Market Base

A two-sided market maker: quote both sides, requote on fill, cover the resulting position, and
refuse to do any of it if the result would breach a position limit. 622 blocks — and unlike
every other large file in the corpus, **550 of them sit at the root level**, so it is legible
without descending through nested Groups.

**Read this file for its safety architecture, not its trading logic.** It carries 8 `Alert`
blocks, 14 `Stopwatch` throttles split by side and by action, 6 `IsNumber` guards, and two
`Terminal` blocks that both **pause** rather than stop. Every generalisation the format spec
makes in §7 about how TT builds risk controls is drawn largely from here. If you are copying
one file's defensive habits wholesale, copy this one's.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Market Base.adl.json` |
| Algo id | `1be544b8-bbf5-44d4-b50b-9474035a0208` |
| Last modified | 2021-11-21 15:36:19 UTC |
| Size | 842,970 bytes |
| Flat blocks / true blocks | **550** / 622 |
| Subgraphs / max depth | 2 / 1 |
| Edges | 585 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta` absent |

**[V]** No `ExistingOrder`; `Instrument` is a plain user variable, not `orderInstrument`. **[I]**
A **standard algo**, launched from the Algo Dashboard or Autotrader
([algo-types](../../adl-kb/guides/algo-types.md)) — the only large file in the corpus that is
neither an OMA nor OTA-shaped.

## Operator surface

**[V]** Thirteen variables, one export:

| Variable | Type | Default | Bounds |
|---|---|---:|---|
| `Instrument` | Instrument | — | — |
| `Bid Qty` / `Ask Qty` | Number | 0 / 0 | none |
| `Bid Offset` / `Ask Offset` | Number | 0 / 0 | none |
| `Max Pos` | Number | 0 | none |
| **`Quote Throttle`** | Number | 250 | **[100, 99999999]** |
| `Fill Throttle` | Number | 0 | none |
| `Cover Order Offset` | Number | 0 | none |
| `Enable Cover Order?` | Boolean | false | — |
| `Manual Requote` | Boolean | false | — |
| `Use Cancel/Replace` | Boolean | false | — |
| `Dont Cross Market` | Boolean | false | — |

**Export:** `Net Pos` (a `Subtract`) → a live Algo Dashboard column.

**[V] Four named toggles, every one of them gating a behaviour that can lose money**, which is
the format spec's §7 point about operator-visible switches made concrete. Note in particular
that `Dont Cross Market` — a protection — **defaults to false**. **[I]** The safe-by-default
choice would be the other way round; TT's choice suggests the block is meant to be configured
deliberately per deployment rather than relied on.

**[V] `Quote Throttle` is the format spec's §5 example of a throttle floor enforced at the
parameter** (`minValue: 100`). But the graph enforces a *different, stricter* floor:

```
Stopwatch "Quote Throttle (Bid)":  IF( @Quote Throttle > 250, @Quote Throttle, 250 )
Stopwatch "Quote Throttle (Ask)":  IF( @Quote Throttle > 250, @Quote Throttle, 250 )
```

**[I]** So there are three floors stacked: ADL's own 25 ms `Stopwatch` minimum, the parameter's
100 ms bound — which matches the `Generator` `TimeInterval` minimum in
[gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md) — and the algo's own 250 ms
policy in the formula. The parameter bound stops an absurd value; the formula encodes what this
*particular* algo considers responsible. **Both, not either.** An operator who sets 100 gets
250 anyway, silently — which is defensible for a throttle and would be a bug anywhere else.

## What it does

### Quoting

**[V]**

```
Instrument --> Market Bid / Market Ask (Field, bidPrice/askPrice, lookupType "best")
           --> M Bid Qty / M Ask Qty   (Field, quantities, "best")
           --> Bid OC / Ask OC         (Field, bidOrderCount/askOrderCount)
           --> MPI                     (Field, minPriceIncrement)
           --> Index Bid Price / Index Ask Price  (Field, lookupType "index")
           --> BQ D1 / AQ D1           (Field, quantities, lookupType "price")

Calc Bid Price / Calc Ask Price --> "Bid to Quote" / "Ask to Quote" (ValueExtractor snapshots)
   --> Buy Order / Sell Order   (Order, limit, day, onExtMod StopManaging,
                                 autoResubmit true, ignoreInputsAfterAdd false)
```

**[V] All three `Field` lookup types appear in this one file** — `best`, `index` and `price`
([block-catalog](../../adl-kb/guides/block-catalog.md)). Index reads appear in 5 corpus files —
3 here and 2 in each theo-family member — and this is the only one that guards them.

**[I]** The quote price is captured through a `ValueExtractor` rather than wired live into the
`Order`. That is the snapshot idiom: freeze the price at the moment the requote decision was
made, so the order is not chasing the market between the decision and the submission
([block-catalog](../../adl-kb/guides/block-catalog.md)).

**[V]** `Bid Ready` / `Ask Ready` are constant-`TRUE` `ValueExtractor` latches — the same
initialisation gate as [with-a-tick.md](with-a-tick.md).

### The throttle architecture

**[V]** Fourteen `Stopwatch` blocks. Six carry deliberate names:

| Name | Formula |
|---|---|
| `Quote Throttle (Bid)` / `(Ask)` | `IF(@Quote Throttle > 250, @Quote Throttle, 250)` |
| `Delete Throttle (Bid)` / `(Ask)` | `IF(...)` on the same parameter |
| `Cancel Replace requote throttle (BID)` / `(ASK)` | `50` |

plus unnamed ones at `@Fill Throttle`,
`IF(@Quote Throttle > 0 AND @Fill Throttle == 0, @Quote Throttle, @Fill Throttle)`, `100`, and
`1000`.

**[V] This is the evidence behind the format spec's §7 claim that TT splits throttles per side
and per action** — bid and ask are separately governed, and quoting, deleting and
cancel-replacing each have their own governor. There is no global rate limiter anywhere in the
file.

**[I] The reason the split matters is not politeness, it is correctness.** A single global
throttle couples the two sides: a burst of bid activity would delay an ask delete that has
nothing to do with it, and the delete is the side that reduces risk. Per-action separation says
the same thing more sharply — **a delete must never queue behind a quote**. Copy the split even
when one throttle looks sufficient.

**[V]** The fallback formula `IF(@Quote Throttle > 0 AND @Fill Throttle == 0, @Quote Throttle,
@Fill Throttle)` is worth reading twice: **[I]** if the operator configured a quote throttle but
no fill throttle, use the quote throttle for fills too. A parameter left at 0 does not become
"no delay"; it inherits a sibling's value. That is a small, transferable habit for any parameter
whose zero value would be unsafe.

**[V]** The `Order` blocks' `Connectors` property lists `["addOK","changeOK","deleteOK"]`, and
`autoResubmit: true` with `ignoreInputsAfterAdd: false` — **[I]** live input tracking on, so a
change to the computed price *modifies* the working order rather than replacing it
([block-catalog](../../adl-kb/guides/block-catalog.md)). The `Use Cancel/Replace` toggle exists
to force the other behaviour, with its own 50 ms throttle. Two requote mechanisms, operator's
choice, separately governed.

### Position limits — the reload guard

**[V]**

```
Net Pos = Subtract( Buy Fills, Sell Fills )    [exported]

Branch "OK to Requote?":  @Net Pos + @Bid Qty <= @Max Pos
Branch "OK to Requote?":  @ABS Sell (Next Clip Reload Check) <= @Max Pos
   --> Alert0 / Alert1  "Reload Prevented due to Potential Breach of Max Position -
                         Reset Max Pos to Continue"

Branch "BQ Filter" / "AQ Filter": the same tests, gating "BQ to work" / "AQ to Work"
Branch2 (@BQ exceeds MP) --> Alert3 "Bid qty exceeds Max Pos, algo paused" --> Terminal
Branch3 (@AQ Exceeds MP) --> Alert2 "Ask qty exceeds Max Pos, algo paused" --> Terminal
```

**[V] Two tiers, and the tier boundary is the design lesson.** The *predictive* test — would the
**next** clip breach `Max Pos`? — produces an `Alert` and **suppresses the requote**, leaving
the algo running. The *actual* breach — the configured quantity itself exceeds `Max Pos` — is
an `Alert` **and** a `Terminal`.

**[I]** So: a condition the algo can decline its way out of gets a soft response; a condition
that means the configuration is wrong gets a hard one. That is a more useful rule than "alert on
warnings, terminate on errors", because it is decidable from the graph: *can the algo continue
correctly by doing nothing?*

**[V] Position is tracked as `Buy Fills − Sell Fills` from two separate `ValueAccumulator`
blocks** — not one signed counter. Format spec §7 lists this as a house idiom; the file also
carries `Recent Buy Fills` / `Recent Sell Fills` / `Recent Buy Cover Fills` /
`Recent Sell Cover Fills`, i.e. four more accumulators tracking the same quantities over a
shorter window. **[I]** Separate counters per side and per purpose, netted only where the netted
number is what the logic needs.

### Cross protection

**[V]**

```
Branch5 (@Attempted Cross (Bid)) --> Alert9 "Bid price attempted to cross market,
                                             Orders deleted. Requote to continue quoting."
Branch5 (@Attempted Cross (Ask)) --> Alert8  (the ask twin)
Jump "Dont Cross Market" --> 4 landings
```

**[I]** When the computed quote would cross the market, delete the orders, tell the operator,
and **stop quoting until a human requotes**. Note the alert text says what happened, what the
algo did, and what the operator must do to resume — three things, one sentence. **[V]** All 8
alerts in the file follow that shape. It is a better standard than most production logging.

### Depth guards — the corpus's real NaN discipline

**[V]** Six `IsNumber` blocks, four of them named:

```
Bid Depth?  ·  Ask Depth?  ·  BidExists  ·  Ask Exists
Alert10  "Unable to quote Ask - no existing market to lean on"
Alert11  "Unable to quote Bid - no existing market to lean on"
```

**[I]** `Index Bid Price` / `Index Ask Price` are `lookupType: "index"` reads, and adl-kb is
explicit that an index beyond available depth returns **`NaN` for price fields** (0 only for
quantity fields) ([block-catalog](../../adl-kb/guides/block-catalog.md)). Those are precisely
the blocks guarded, and the failure is reported rather than swallowed — the algo tells the
operator it cannot quote instead of quietly producing a `NaN` that would delete working orders.

**[V] Market Base and [oco.md](oco.md) are the only two files in the corpus containing
`IsNumber` at all** — 6 here and 1 there, out of 7 total. **[I]** And it is the only file that
reads depth by index. The correlation is the point: TT guards where TT actually risks `NaN`.
The format spec's §6 warning applies to your design, not to this corpus's average.

### Cover orders

**[V]** Two virtual Groups, 36 blocks each, one per side:

```
Group0: in "Cover Sell?" (message), in "Instrument" (string), out "Fills" (message)
Group1: in "Cover Buy? "  — the mirror
Branch "Cover Sell?" / "Cover Buy? ":  @Enable Cover Order? AND @Net Pos != 0
inside each: an Order block (leaveOnPauseCancel ["Pause","Cancel"]) and an Exit block
```

**[V]** Both contain an `Exit` — 2 of the corpus's 7. **[I]** So Market Base and
[brackett.md](brackett.md) are the two files that virtualize *and* dispose. Each cover order
gets its own instance so a later fill cannot clobber an earlier cover, and the instance is
retired when done.

**[V]** `leaveOnPauseCancel: ["Pause","Cancel"]` on the cover orders and **not** on the quoting
orders. **[I]** Deliberate and worth copying: pausing the algo should pull the quotes and
**leave the hedges**. A pause that cancels your cover leaves you naked in exactly the moment you
decided something was wrong.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 — **both `pause`** | there is **no `stop`** anywhere in this algo |
| `Alert` | **[V]** **8** | max-pos ×4, cross ×2, no-market-to-lean-on ×2; all with operator instructions |
| `IsNumber` | **[V]** **6** | on the index price lookups and the best bid/ask |
| Throttles | **[V]** 14 `Stopwatch` | split per side and per action; floors at 25/100/250 ms |
| Bounds | **[V]** 1 of 10 numbers | only `Quote Throttle`; `Max Pos`, `Bid Qty`, `Ask Qty` are unbounded |
| Position cap | **[V]** yes | `Max Pos` with predictive and actual tiers |
| `Exit` in virtual Groups | **[V]** yes, both | correct lifecycle |
| `MarketState` | **[V]** none | `ignoreMarketState: false`, so the platform pauses out of session |
| `Pnl` / `PositionRisk` | **[V]** none | **[I]** neither block appears anywhere in the corpus (format spec §8) |

**[I] "Both Terminals pause, none stop" is a considered stance, not an omission.** A market
maker holding inventory should never disappear: stopping abandons a position that still needs
covering, while pausing keeps the algo attached and resumable by the human the `Alert` just
messaged. Compare [tt-sniper.md](tt-sniper.md), which stops on completion because it holds
nothing. **Decide pause-vs-stop by asking what the algo still owes when it ends.**

**[V] `Max Pos` defaults to 0 and is unbounded.** **[I]** With `Net Pos + Bid Qty <= Max Pos` as
the gate, a default of 0 means the algo declines to quote until the operator sets it — inert by
default, like `Min Qty` in [minvol.md](minvol.md). Safe, and easily mistaken for broken.

## Reuse

**[V]** Two Groups, both **RED**, both virtual:

| Group | Tier | Size | Ports | Cost |
|---|---|---:|---|---|
| `Group0` (cover sell) | RED | 36 | `Cover Sell?` msg in, `Instrument` string in, `Fills` msg out | + jump `Net Pos`, + 1 dangling formula (`ValueExtractor5`) |
| `Group1` (cover buy) | RED | 36 | the mirror | + jump `Net Pos`, + 1 dangling formula (`ValueExtractor2`) |

```bash
python tools/patterns.py --show "Group0" --from "Market Base"
```

**[I] These two are the corpus's best illustration of why RED is a real cost.** The leak is a
`ValueExtractor` inside the Group whose formula references a block outside it; after extraction
that reference dangles, and the format spec (§4) says explicitly **not** to hand-author or
hand-repair formulas — the `formulaNodes` AST must stay in sync with the string, and which one
the runtime evaluates is unresolved ([OPEN-QUESTIONS Q2](../../OPEN-QUESTIONS.md)). The clean
repair is to add a real input port to the Group and rewire in the Designer, not to edit JSON.

**The reusable material in this file is not its Groups.** It is flat, root-level structure —
which means copying it means copying *blocks*, with GUIDs reminted:

| Take | Blocks | Why |
|---|---|---|
| **Per-side, per-action throttles** | 6 named `Stopwatch` blocks | a delete must never queue behind a quote |
| **Layered throttle floor** | `minValue` on the Number + `IF(x > floor, x, floor)` in the Stopwatch | platform floor, parameter floor, policy floor |
| **Parameter inheritance** | `IF(@A > 0 AND @B == 0, @A, @B)` | a parameter left at 0 inherits rather than meaning "none" |
| **Two-tier limit response** | predictive test → `Alert` + suppress; actual test → `Alert` + `Terminal(pause)` | decide the tier by "can the algo continue correctly by doing nothing?" |
| **Depth guard + report** | `Field(index)` → `IsNumber` → `Alert` "no existing market to lean on" | the corpus's only guarded depth read — the theo family does the same lookups unguarded |
| **Alert text standard** | what happened · what the algo did · what you must do | all 8 alerts, one sentence each |
| **Pause-not-stop** | `Terminal(mode: pause)` | for any algo that still owes the market something |
| **`leaveOnPauseCancel` asymmetry** | on hedges, not on quotes | a pause should pull quotes and leave cover |
| **Fills per side and per window** | 8 `ValueAccumulator` blocks | net only where the netted number is what the logic needs |

## Jump inventory

**[V]** 112 jumps → 144 landings — the second-densest wormhole mesh in the corpus after
[tt-multi-level-bracket.md](tt-multi-level-bracket.md)'s 129. The high-fan-out names show the
algo's spine:

| Name | Landings |
|---|---:|
| `Reset Open Pos:messageOut` | 6 |
| `Requote:messageOut` | 5 |
| `Market Ask`, `Market Bid`, `Ask Qty`, `On Every Start:messageOut`, `Dont Cross Market`, `Instrument` | 4 each |
| `MPI`, `Bid Qty`, `Ask to Quote:val`, `Bid to Quote:val`, `Net Pos` | 3 each |

**[I]** `On Every Start:messageOut` with four landings is the resume-repair habit again —
[minvol.md](minvol.md) documents (via TT's own `Note`) why an `everyStart` `Generator` is
necessary after a pause, and here it re-primes four separate subsystems.

**[V] 28 `Note` blocks, 27 of them empty.** The one with text reads *"Waits for full fill or
price change"*. **[I]** Empty `Note` blocks are canvas furniture — coloured backing panels
behind block clusters — not documentation. Do not read `Note` count as a proxy for how
well-documented an algo is; [oco-2.md](oco-2.md) has five Notes and all five carry real
engineering rationale.

## Related

The theo family ([bid-ask-theo.md](bid-ask-theo.md),
[single-theo.md](single-theo.md), [reference-market.md](reference-market.md),
[direct-entry.md](direct-entry.md)) shares this file's throttle and alert vocabulary but
organises it into Groups. [brackett.md](brackett.md) is the other file that virtualizes with an
`Exit`. For the same `IsNumber` discipline applied to division rather than depth, see
[oco.md](oco.md).

**Cited from:** all four theo docs for the depth guards and the alert vocabulary ·
[brackett.md](brackett.md) and [tt-multi-level-bracket.md](tt-multi-level-bracket.md) for
pause-vs-stop, the `Order` block and `Exit` disposal · [oco.md](oco.md) for the `IsNumber`
discipline · [minvol.md](minvol.md), [with-a-tick.md](with-a-tick.md),
[conditional.md](conditional.md) and [tt-sniper.md](tt-sniper.md) for the throttle, readiness-gate
and alerting idioms the small files omit · [oco-2.md](oco-2.md) for the `Alert` layer it lacks.
