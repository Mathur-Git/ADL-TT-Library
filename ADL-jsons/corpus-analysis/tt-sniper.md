# TT Sniper

Waits for the market to reach a target price, then takes exactly what is showing — no more —
and waits a configurable cooldown before taking again, until the total quantity is done.
62 blocks, three Groups, five user variables.

For anyone mining this corpus for parts it has the highest useful-idea density of any small
file: at 62 blocks it holds a virtualized Group, a `ValueInjector`, an in-graph parameter
validator with an `Alert`, a `Math(Min)` sizing rule and a cooldown latch. None of those is
unique to the file — the counts are given in place below — but nowhere else are they this
small and this readable at once. Three reuse lessons come out of it, one of them a warning.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `TT Sniper .adl.json` (**trailing space** in the filename) |
| Algo id | `1b6e4c78-a365-456c-9e96-1b127266eec9` |
| Last modified | 2020-12-13 10:15:48 UTC |
| Size | 86,372 bytes |
| Flat blocks / true blocks | 42 / **62** |
| Subgraphs / max depth | 3 / 1 |
| Edges | 53 |
| Algo flags | `orderSide: false`, **`ignoreMarketState: true`**, `isOmaOta: false` |

**[V]** No `ExistingOrder`, so not an OMA. Its `Instrument` block has `type: "orderInstrument"`
and its `TotalQty` Number has `type: "orderQty"` — which are two of the three ingredients of an
**SOA**, and the first alone makes it an **OTA**
([algo-types](../../adl-kb/guides/algo-types.md)). The third ingredient, the SOA algo setting,
is absent. **[I]** So: an **OTA**, launchable from the ladder, that could be promoted to an SOA
by flipping one setting.

**[I] `isOmaOta` is not "is this an OMA or an OTA".** This file *is* an OTA and has it `false`;
[with-a-tick.md](with-a-tick.md) *is* an OMA and has it `false`; [conditional.md](conditional.md)
and [minvol.md](minvol.md) are OMAs with ladder hooks and have it `true`. The pattern fits the
**`Launchable OMA (as OTA)`** algo setting ([algo-types](../../adl-kb/guides/algo-types.md)),
not the algo's type. Do not use the flag to classify a file — read the blocks.

## Operator surface

**[V]**

| Variable | Block | Type | Default | Bounds |
|---|---|---|---:|---|
| `Instrument` | Instrument | `orderInstrument` | (not selected) | — |
| `TargetPrice` | Price | `orderPrice` | 0 | — |
| `TotalQty` | Number | `orderQty` | 0 | none |
| `TIF` | Number | `tif` | 0 | none |
| `Aggressiveness (Sec)` | Number | `userDefined` | 1 | **none** |

No exports.

**[V]** 8 `Price` blocks exist across 6 corpus files; what is distinctive here is that the
variable set covers all four legal user-variable types
([algo-types](../../adl-kb/guides/algo-types.md) — Bool, Number, Instrument, Price). **[I]** If
you want a worked example of a complete launch-time parameter surface for a standard/OTA algo,
copy this one's shape.

**[V] `TIF` is a `Number` with `type: "tif"`, default 0** — and the TIF code table
([block-catalog](../../adl-kb/guides/block-catalog.md)) starts at 1 (Day). **[U]** What 0
means here is not answerable from the file; it may be an unset sentinel. Its value flows
straight into the `DiscreteOrder`'s `timeInForce` field formula, so it is not cosmetic.

## What it does

### The trigger

**[V]**

```
Instrument --> TargetPrice (Price)
           --> AskPrice (Field askPrice, lookupType "best", flipForSell)
           --> AskQty   (Field askQuantity, lookupType "best", flipForSell)

LessThanEqual0( TargetPrice, AskPrice )  --> And0
OrderEntryEnabled:OK to Enter (jump)     --> And0
And0 --> Generator0 (mode: boolTrue)
```

**[I]** "The offer has reached my target **and** I am allowed to enter" → fire one message. A
`Generator` in `boolTrue` mode turns a continuous boolean into the discrete pulse that
everything downstream needs ([block-catalog](../../adl-kb/guides/block-catalog.md)). Both
`Field` blocks carry `flipForSell: true`, so on a sell the same graph reads the bid.

### Sizing — take only what is showing

**[V]**

```
Subtract0     = SubmittedQty - DeletedQty            (net quantity that stuck)
AvailableQty  = TotalQty     - Subtract0             (still to do)
SubmitQty     = Math Min(x, y) of AvailableQty and AskQty
```

**[I]** `Min(remaining, quantity showing at the touch)` is the whole idea of the algo: never
send more than the level can absorb, so nothing rests and nothing signals. **[V]** `Min` is a
value of the `Math` block's `mathFunction` property, not a block of its own — the format spec
warns specifically against concluding `Min`/`Max` are missing from ADL (§8).

**[V]** Note how the accounting is done: `SubmittedQty` (accumulates `@SubmitQty` per
submission) minus `DeletedQty` (accumulates `{deletedQuantity}` from the virtual instances).
**[I]** Not "filled quantity" — *submitted minus cancelled*. That is deliberate: quantity
in flight is unavailable even before it is known to have filled, so the algo cannot double-send
while an order is live. `FillQty` is tracked separately and used only to decide when the job is
finished. **Sides tracked separately and netted downstream** is a corpus-wide TT idiom
(format spec §7); this is the in-flight-accounting version of it.

### Submission — the `ValueInjector`

**[V]**

```
Generator0 --> OrderQtyInject (ValueInjector: orderQuantity = @SubmitQty)
           --> SubmittedQty (ValueAccumulator, formula @SubmitQty)
           --> DiscreteOrder0
DiscreteOrder0 formulas: price = @TargetPrice
                         quantity = {orderQuantity}     <-- the injected field
                         timeInForce = @TIF
DiscreteOrder0: flipForSell true, cloneIncomingOrder false, onExtMod StopManaging
```

**[I]** The `Generator` manufactures an **empty** message
([block-catalog](../../adl-kb/guides/block-catalog.md)), so there is no `orderQuantity` field
to read. `ValueInjector` writes the computed size *into* the message, and the `DiscreteOrder`
then reads it back with `{orderQuantity}`. **[V]** 39 `ValueInjector` blocks exist across 10
corpus files — BrackeTT has the most (11), then [oco.md](oco.md) (5) and the theo family (4
each). This is the smallest and clearest instance.

**[I] Why bother, when the formula could reference `@SubmitQty` directly?** Because the
computed value is then frozen into the message and travels with it. adl-kb documents
`ValueInjector` as the way to carry data along a discrete pathway and, specifically, the way to
get values **out of a virtualized block** through `userField1..4`
([block-catalog](../../adl-kb/guides/block-catalog.md)). If you build anything virtualized,
this is the mechanism you will need; [oco-2.md](oco-2.md) shows the same block used to stamp an
instance's identity on the way *in*.

### `Group0` — the virtualized fire-and-forget order

**[V]** `virtual: true`, 6 blocks, three ports, all `message`:

```
in  message  DiscreteOrder0     <- the Add OK of the DiscreteOrder
out message  DelQty
out message  Fills

inside:  Connector "DiscreteOrder0" --> SingleOrderContainer0
         Boolean "DeleteImmediately" (static TRUE) --> SOC.del
         SOC msgs --> Demultiplexer0 --> out0 (delete) --> Connector "DelQty"
                                     --> out1 (fill)   --> Connector "Fills"
```

**[I]** Each snipe spawns its own instance, which immediately deletes the order it was handed
and reports back what filled and what got cancelled. Deleting instantly is how the algo gets
IOC-like behaviour out of a `day` order: whatever crosses in the same instant fills, the rest
is pulled.

**[V]** It satisfies the rules of virtualization exactly — a discrete input, and **no
continuous output ports**, only message ports
([block-catalog](../../adl-kb/guides/block-catalog.md)). That constraint is why `Fills` and
`DelQty` are messages that get accumulated *outside* rather than numbers computed inside.

> **[V] There is no `Exit` block inside this virtualized Group.** The corpus contains only 7
> `Exit` blocks and none of them are here.
> **[I]** adl-kb is unambiguous about the consequence: *"Without it, instances accumulate in
> memory and progressively slow the algo"*
> ([block-catalog](../../adl-kb/guides/block-catalog.md), rules of virtualization). A sniper
> working a large `TotalQty` in small clips spawns one instance per clip and disposes of none.
> **If you copy this Group — and it is otherwise the best small virtualization example
> available — add an `Exit` block driven from the delete pathway.** Whether TT considers this a
> defect or an accepted cost for a short-lived algo is **[U]**.

### Cooldown — `OrderEntryEnabled`

**[V]** 9 blocks; in `message`, out `bool`:

```
Connector "Sequence0" (the DiscreteOrder's Add OK) --> OrderBlockOn (ValueExtractor, TRUE)
OrderBlockOn msg --> Stopwatch0 (formula: @Aggressiveness (Sec) * 1000) --> OrderBlockOn.reset
OrderBlockOn val --> Not0 --\
GreaterThan0( AvailableQty, 0 ) --> And0 --> Connector "OK to Enter"
```

**[I]** Submitting an order latches `OrderBlockOn` TRUE, which blocks further entry; the
`Stopwatch` waits `Aggressiveness` seconds and resets the latch. Entry also requires quantity
still to do. So `Aggressiveness (Sec)` is really an *inter-snipe cooldown* — lower is more
aggressive.

**[I] This is a rate limiter built without a throttle block**, and it is a cleaner shape than
the counter-and-cap in [minvol.md](minvol.md): the guard is *in front of* the action rather
than counting it afterwards. The parts are a `ValueExtractor(TRUE)` latch, a `Stopwatch` on its
reset, and a `Not`. Copy that trio whenever you need "at most one of these every N seconds".

**[V] The `Stopwatch` formula is in milliseconds** (`seconds * 1000`) and the minimum ADL
accepts is 25 ms ([gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md)) — which is
exactly what the next Group defends.

### `MinAggressiveValueCheck` — the validator, and a model `Alert`

**[V]** 5 blocks, one `real` input port, no output:

```
input0 (<- Aggressiveness (Sec)) --> LessThan0 <-- MinAggressiveValue (static 0.25)
LessThan0 --> Alert0
LessThan0 --> Terminal0 (mode: pause)
```

**[V]** `Alert0`: formula `"Aggressive Value cannot be less than " + @MinAggressiveValue`,
`alertAction: ["Audit Trail"]`, `frequency: 5`, `alertSound: "none"`. It carries a formula
string and **no `formulaNodes` AST** — consistent with the format spec's §4 finding that the
two do not reliably come as a pair, and **[I]** making this one of the few formulas in the
corpus that is comparatively safe to hand-edit, since there is no AST to fall out of sync.

**[V] This is the `Alert` + `Terminal` pairing** the format spec describes as TT's core safety
idiom (§7): one condition drives both, telling the human *and* stopping the algo. 45 `Alert`
blocks exist across 8 corpus files — the theo family and [market-base.md](market-base.md) carry
8 each, [tt-multi-level-bracket.md](tt-multi-level-bracket.md) 3, this file and
[brackett.md](brackett.md) 1 each. **[V]** But of the five small files, only this one has any:
[conditional.md](conditional.md), [minvol.md](minvol.md), [with-a-tick.md](with-a-tick.md),
[oco.md](oco.md) and [oco-2.md](oco-2.md) all stop silently.

**[I] It is also an example of the "belt and braces" rule done with only one of the two.** The format spec (§5) notes TT bounds safety-relevant `Number` blocks *and*
validates in-graph, because bounds cannot express cross-parameter rules. Here the in-graph
check exists and `Aggressiveness (Sec)` still has `minValue: null`. Setting `minValue: 0.25`
on the block would be free and would stop the operator entering the bad value in the first
place, rather than pausing the algo after launch. **When you adopt this Group, set the bound
too.**

### Completion

**[V]** `Equal0( TotalQty, FillQty )` → `Terminal "Complete"` (`mode: stop`). **[I]** Exact
equality on a quantity is safe because both sides are integers; the corpus's `Epsilon`
parameter idiom (format spec §7) exists for *price* comparisons, not this.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 | `Complete` **stop** on done; `Terminal0` **pause** on bad parameter |
| `Alert` | **[V]** 1 | the parameter alert only — completion and errors elsewhere are silent |
| In-graph input validation | **[V]** 1 | `MinAggressiveValueCheck`; **[I]** the matching `minValue` bound is missing |
| `IsNumber` | **[V]** none | no division anywhere; **[U]** whether a `best` price lookup on an empty book yields `NaN` is not settled by the file — adl-kb documents `NaN` for *indexed* price lookups past depth |
| `MarketState` | **[V]** none | and **`ignoreMarketState: true`** |
| `Exit` in the virtual Group | **[V]** none | **[I]** instances accumulate — see above |
| Position / P&L cap | **[V]** none | bounded only by `TotalQty`, which is unbounded |

**[I] The `ignoreMarketState: true` setting deserves its own line.** Only this file and
[brackett.md](brackett.md) turn off the platform's automatic out-of-session pause, and unlike
[with-a-tick.md](with-a-tick.md) it contains **no `MarketState` block** to compensate. adl-kb
frames the setting as the prerequisite for pre-open logic and for `MarketState` to be useful
([algo-types](../../adl-kb/guides/algo-types.md)); used without either, it simply removes a
guard. A sniper resting on a target price through a settlement or a halt is a live exposure the
graph does not model.

**[V]** One dead jump: `FillQty:accVal` has no landing.

## Reuse

**[V]** Three Groups — the full tier range in one file:

| Group | Tier | Size | Ports | Cost |
|---|---|---:|---|---|
| `MinAggressiveValueCheck` | **GREEN** | 5 | `in real` | wire one number |
| `Group0` (virtual) | **GREEN** | 6 | `in message`, `out message` ×2 | wire three messages |
| `OrderEntryEnabled` | **RED** | 9 | `in message`, `out bool` | + jump `AvailableQty`, + one dangling formula |

```bash
python tools/patterns.py --show   "MinAggressiveValueCheck"
python tools/patterns.py --extract "MinAggressiveValueCheck" --from Sniper -o param-floor.json
python tools/patterns.py --extract "Group0"                  --from Sniper -o fire-and-forget.json
python tools/validate.py param-floor.json
```

**`MinAggressiveValueCheck` is the highest-value transplant in the entire corpus for a new
build.** It is GREEN, five blocks, one input, and it gives any algo the Alert+Terminal
parameter-floor idiom for the cost of one edge. Change the `MinAggressiveValue` Number and the
Alert's string — **[I]** and the Alert is one of the safest formulas to edit, having no AST.

`Group0` is the cheapest correct example of virtualization available: it obeys the
message-only-output rule, and it is small enough to read in one screen. **Add an `Exit` block
before using it.**

**[I] `OrderEntryEnabled` shows that RED is a severity range, not a verdict.** Its single
formula leak is `Stopwatch0`'s formula referencing `@Aggressiveness (Sec)`, a *user variable
sitting one level up*. Repointing it at your own Number after extraction is a one-token change
— far removed from a RED group whose formula reaches into another Group's internal state (see
[market-base.md](market-base.md)). Read the actual leak before writing a Group off; the format
spec's warning against hand-editing formulas (§4) still applies, so prefer adding a real input
port to the Group over editing the string.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Parameter floor validator** | `MinAggressiveValueCheck` | GREEN, drop-in, 5 blocks — the smallest Alert+Terminal pair in the corpus |
| **Fire-and-forget order** | `Group0` (+ an `Exit`) | correct virtualization in six blocks |
| **Cooldown latch** | `ValueExtractor(TRUE)` + `Stopwatch` on reset + `Not` | rate limiting *before* the action, not counting after it |
| **In-flight accounting** | `SubmittedQty − DeletedQty`, then `TotalQty −` that | prevents double-sending while an order is live; better than filled-quantity accounting |
| **Take-what-is-showing sizing** | `Math Min(x,y)` of remaining and touch quantity | one block; the core of any non-signalling execution algo (`Min(x,y)` also appears in the theo family and [tt-multi-level-bracket.md](tt-multi-level-bracket.md)) |
| **Injected quantity** | `Generator(boolTrue)` → `ValueInjector` → `DiscreteOrder{orderQuantity}` | the clearest worked example of getting a computed value into a manufactured message |

## Jump inventory

**[V]** 9 jumps → 10 landings; one dead.

| Name | Source | Consumers |
|---|---|---|
| `TotalQty` | `TotalQty` (Number) | `Equal0`, `AvailableQty` |
| `AvailableQty` | `AvailableQty` (Subtract) | `SubmitQty`, `GreaterThan0` *(inside `OrderEntryEnabled`)* |
| `AskPrice` / `AskQty` | the two `Field` blocks | `LessThanEqual0` / `SubmitQty` |
| `TargetPrice` | `TargetPrice` (Price) | `LessThanEqual0` |
| `Instrument` | `Instrument` | `DiscreteOrder0` |
| `OrderEntryEnabled:OK to Enter` | the Group's out port | `And0` |
| `DeletedQty:accVal` | `DeletedQty` (VA) | `Subtract0` |
| `FillQty:accVal` | `FillQty` (VA) | **no landing — dead** |

**[V]** Note `OrderEntryEnabled:OK to Enter` — a jump named `<group>:<portName>`, taking a
value that already left through a declared port and carrying it onward. **[I]** Ports and
jumps are used for different distances, not as alternatives: the port crosses the boundary, the
jump crosses the canvas.

## Related

[market-base.md](market-base.md) and the theo algos use the same Alert+Terminal idiom at scale.
For the opposite approach to rate limiting — count afterwards and cap — see
[minvol.md](minvol.md); for removing the need entirely, [with-a-tick.md](with-a-tick.md).

**Cited from:** [oco-2.md](oco-2.md) and [oco.md](oco.md) for the virtual Group with no `Exit`
and the `ValueInjector` ·  [brackett.md](brackett.md) for the parameter validator without its
bound · [minvol.md](minvol.md) and [with-a-tick.md](with-a-tick.md) for the three approaches to
rate limiting · [market-base.md](market-base.md) for pause-vs-stop ·
[conditional.md](conditional.md) and [tt-multi-level-bracket.md](tt-multi-level-bracket.md) for
the silent-shutdown contrast and `Math Min`.
