# TT Multi-Level Bracket

One entry order, then **four** independently-sized exit levels, each with its own profit limit,
stop-market and stop-limit order — thirteen `Order` blocks in total. 682 blocks, the largest
algo in the corpus, and 599 of them live inside a single Group named `OCO`.

Two things make it worth study. Its operator surface is the most carefully bounded in the
corpus — nineteen variables, nine of them with `minValue`/`maxValue` — **and it still needs
in-graph validation**, which is the clearest possible demonstration of why the format spec's §5
"belt and braces" rule exists. And its 625-block `OCO` Group is the corpus's proof that
**size is not reusability**: the biggest Group in the corpus is also the least transplantable
one in it.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `TT Multi-Level Bracket  .adl.json` (**two spaces** before `.adl`) |
| Algo id | `73874d2b-d97a-4e63-a76b-cda61fdfa4ea` |
| Last modified | 2021-10-10 20:04:55 UTC — a minute after [with-a-tick.md](with-a-tick.md) |
| Size | 1,073,209 bytes |
| Flat blocks / true blocks | **57** / **682** — 92% of the algo is hidden one level down |
| Subgraphs / max depth | 2 / 2 |
| Edges | 682 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta: false` |

**[V]** `Instrument` is a plain user variable and there is no `ExistingOrder`; `Price` is an
`orderPrice` Price block. **[I]** A standard algo with a ladder-style price input.

**[V] The flat-vs-true block ratio is the format spec's §2 nesting trap at its most extreme.** A
tool that reads only top-level `content` sees 57 blocks and concludes this is a small algo.

## Operator surface

**[V]** Nineteen variables, no exports. Nine carry bounds — **more bounded parameters than the
rest of the corpus combined**:

| Variable | Default | Bounds |
|---|---:|---|
| `Instrument`, `Price` | — | — |
| `Order Qty` | 0 | none |
| `LV1 %` | 0 | **[0, 100]** |
| `LV2 %` | 0 | **[0, 99]** |
| `LV3 %` | 0 | **[0, 98]** |
| `LV4 %` | 0 | **[0, 97]** |
| `Profit` (Bool) | true | — |
| `Profit LV1..LV4 (Ticks)` | 0 | **[0, 999]** each |
| `Stop` (Bool) | true | — |
| `Stop LV1..LV4 (Ticks)` | 0 | **[0, 999]** each |
| `Stop Limit` (Bool) | true | — |
| `Stop Limit (Ticks)` | 0 | **[0, 99]** |

**[V] The level-percentage maxima descend: 100, 99, 98, 97.** **[I]** Not arbitrary. The four
must sum to exactly 100, so a later level can never legitimately take the whole allocation —
`LV4` capped at 97 leaves room for the three that must precede it to hold at least 1 each. It is
as much of the cross-parameter constraint as a per-block bound is *able* to express.

**[V] And it is not enough** — the real rule needs a formula:

```
Branch1:  @LV1 % + @LV2 % + @LV3 % + @LV4 % != 100  OR  (!@Profit AND !@Stop)
   --> Alert "Allocation Failure"  : "Level percent allocation does not total 100% - Algo Cancelled"
   --> Alert "No Cover Selected"   : "No Profit or Stop Selected - Algo Cancelled"
   --> Terminal "Incorrect Input values - Algo Stopped"   (mode: stop)
```

**[V] This is the exact block the format spec §7 names** — `Incorrect Input values - Algo
Stopped` — and this is where it lives. **[I] The lesson is the pairing, not either half.**
Bounds are cheap, catch the operator's typo at entry, and *cannot* express "these four must sum
to 100" or "at least one of these two booleans must be true". The graph check catches those but
only after launch. TT ships both, and this file is the reason the rule reads the way it does.
**Any parameter set with a cross-parameter invariant needs both layers.**

**[V]** Note the second alert's condition is folded into the same `Branch` (`OR (!@Profit AND
!@Stop)`) but gets its own message. **[I]** One kill switch, two diagnoses — the operator is
told which rule they broke, not merely that something was wrong.

## What it does

**[V]** Thirteen `Order` blocks:

| Role | Blocks | Type | `onExtMod` | `autoResubmit` |
|---|---|---|---|---|
| Entry | `Order0` | limit, buy | **StopManaging** | true |
| Profit, per level | `V4LV1..LV4 Order` | limit, sell | Ignore | true |
| Stop, per level | `Order1`, `3`, `5`, `9` | **stopMarket**, sell | Ignore | true |
| Stop-limit, per level | `Order10..13` | **stopLimit**, sell | Ignore | true |

**[V]** All thirteen have `ignoreInputsAfterAdd: false` and `submitInSuspendedState: false`.

**[I] The external-modification asymmetry is the same one [conditional.md](conditional.md)
uses, and for the same reason**: a human touching the **entry** invalidates the algo's model of
what it is bracketing, so the algo lets go (`StopManaging`); a human touching one **exit**
leaves the other twelve orders' logic intact, so the algo carries on (`Ignore`). **Set
`onExtMod` per block by asking what else depends on that order.**

**[V] `stopMarket` (4) and `stopLimit` (4) `Order` types appear only in this file** — the 12
`Order` blocks in [brackett.md](brackett.md) and [market-base.md](market-base.md) are all
`limit`. Everything else in
the corpus builds stops synthetically — [brackett.md](brackett.md) constructs one from
`TimeAndSales` + `OnceTrue` + a suspended order. **[I]** So the corpus contains both approaches:
a native exchange stop (here) and a synthetic one (there). The synthetic version exists because
a native stop leaks your trigger to the exchange; the native version exists because it survives
your algo dying. That choice is a design decision, and both implementations are available to
copy.

### Level allocation

**[V]** Four `Round` blocks (`mode: normal`) named `LV2 Qty`, `LV3 Qty`, `LV4 Qty` and
`Round0`, fed by `Multiply` and `Divide` chains off `Order Qty` and the `LV_ %` variables.

**[V]** All 4 `Round` blocks in the corpus are here — no other file uses one. **[I]** adl-kb frames `Round` as
"essential for snapping prices to tick" ([block-catalog](../../adl-kb/guides/block-catalog.md));
here it snaps *quantities* to whole lots after a percentage split. Percentage-of-quantity
allocation is the general case, and `Round(mode: normal)` is the whole answer to it — no
epsilon dance of the kind [oco-2.md](oco-2.md) needs, because `Round` does not truncate.

**[I]** Compare the two approaches directly: OCO 2 uses `Math Floor` and must add `1e-10` first
and carry the remainder forward in a `ValueExtractor`; this file uses `Round` and does neither.
**If you do not specifically need floor semantics, `Round` is three blocks cheaper and cannot
be got wrong.**

### Per-level tracking

**[V]** The `ValueExtractor` census tells the story — 59 of them, in an eight-block pattern
repeated per level:

```
LV_ Fills                    (ValueAccumulator, {fillQuantity})
LV_ New Price                (ValueExtractor, {limitPrice})
LV_ Manual Price update      (ValueExtractor, TRUE)          <- latch
LV_ Deleted                  (ValueExtractor, TRUE)          <- latch
LV_ New Stop Price           (ValueExtractor, {stopTrigger})
LV_ Manual Stop Price update (ValueExtractor, TRUE)          <- latch
LV_ Stop Deleted             (ValueExtractor, TRUE)          <- latch
LV_ Stop Activated           (ValueExtractor, TRUE)          <- latch
```

**[I]** Every level maintains, for both its profit order and its stop order: the current price,
whether a human changed it, whether it was deleted, and whether the stop fired. That is the
"ignore and cooperate" stance from [with-a-tick.md](with-a-tick.md), applied eight ways per
level and thirty-two times in total.

**[I] The uniformity is the transferable part.** A repeated per-instance state block —
*value · changed-latch · deleted-latch · activated-latch* — is what makes a 4-level algo
tractable to build and to read. Every level is the same eight blocks with a different index.
**Design the one level, then replicate; do not design four levels.**

**[V]** `Branch "No Entry Fills?"` reads `{userField4} == 1` — **[I]** a flag hand-carried on a
message through `userField4`, one of the four slots per message
([gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md)), the same smuggling channel
[oco-2.md](oco-2.md) uses for instance identity.

### The `MPI` jump

**[V]** One `Field(minPriceIncrement)` block, one `Jump` named `MPI`, **12 landings** — the
highest fan-out of any jump in the corpus (next is `Inst:val` at 9, also here; outside this
file the maximum is 6, in [market-base.md](market-base.md)).

**[I]** Every tick-denominated parameter (`Profit LV1..4`, `Stop LV1..4`, `Stop Limit`) has to
be multiplied by the increment to become a price, so a single tick size is consumed twelve
times across a canvas. This is the format spec's §6 point about routing blocks in its purest
form: one value, one producer, twelve consumers, and not one long edge on the canvas.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 2 | `Incorrect Input values - Algo Stopped` (**stop**), `Algo Paused` (**pause**) |
| `Alert` | **[V]** 3 | `Allocation Failure`, `No Cover Selected`, `Entry Deleted` — all with the "what happened / what the algo did" shape |
| Bounds | **[V]** **9 variables** | against 1 each in [market-base.md](market-base.md), [brackett.md](brackett.md) and each theo file — more than the rest of the corpus combined |
| In-graph cross-parameter validation | **[V]** yes | the `!= 100` and `!Profit AND !Stop` tests |
| Throttles | **[V]** 2 `Stopwatch` — `25` and `100` | **[I]** minimal, and no per-side split — this algo does not requote continuously |
| `IsNumber` | **[V]** **none** | but there are **4 `Divide` blocks** — see below |
| `MarketState` | **[V]** none | `ignoreMarketState: false` |
| Position cap | **[V]** none beyond `Order Qty` | the four levels allocate a fixed total |
| Virtualization / `Exit` | **[V]** none | 13 static `Order` blocks instead of N instances |

**[V] The pause tier is used well:** `Entry Deleted` → *"Entry manually deleted - no fills
received - ALGO PAUSED"* → `Terminal "Algo Paused"` (pause). **[I]** The algo has nothing to
bracket, so it stops working — but it pauses rather than stops, because the operator may simply
re-enter. The parameter failure, by contrast, **stops**: a bad configuration cannot be resumed
out of. **[I]** Same rule as [market-base.md](market-base.md) read from the other side: stop
when resuming would be wrong, pause when it would be fine.

**[I] Four `Divide` blocks and no `IsNumber` is the file's one soft spot.** The divisions are in
the percentage allocation, so the denominators are constants or `Order Qty` — an `Order Qty` of
0 gives `0/0 → -nan` ([block-catalog](../../adl-kb/guides/block-catalog.md)), and `Order Qty` is
one of the **unbounded** variables, defaulting to 0. Whether the allocation runs before the
validation `Terminal` fires is **[U]**. It costs two blocks to remove the question; see the
guarded-division pattern in [oco.md](oco.md).

## Reuse

**[V]** Two Groups, and they sit at opposite ends of the tier scale:

| Group | Tier | Size | Ports | Cost |
|---|---|---:|---|---|
| `OCO` | **RED** | **625** | `State0:3` msg in; `Deleted`, `Trade Complete` msg out | + 4 inbound jumps (`Order Qty`, `Price`, `Profit`, `Stop`) + **17 dangling formula references** |
| `Sum of working orders` | **AMBER** | 26 | `Active WRK Qty` real out | + **13** inbound jumps, one per `Order` |

```bash
python tools/patterns.py --show "OCO"
python tools/patterns.py --show "Sum of working orders"
python tools/patterns.py --extract "Sum of working orders" --from "Multi-Level" -o wrk-sum.json
```

**[I] `OCO` is the corpus's best argument that a big Group is not a big win.** 625 blocks behind
a three-port interface looks like the ideal transplant until you read the cost line: seventeen
formulas inside reference blocks outside — `Inst`, `LV1..LV4 % Snap`, `Limit Ticks`,
`OQ Snapshot LV4`, `Order Price Snap`. Every one dangles the moment the subgraph is lifted, and
the format spec (§4) says not to repair formulas by hand: the string and its `formulaNodes` AST
must stay consistent, and which the runtime evaluates is unresolved
([OPEN-QUESTIONS Q2](../../OPEN-QUESTIONS.md)). Seventeen Designer-side repairs is not a
transplant, it is a rebuild.

**[I]** The pattern behind those leaks is visible in the names: they are all **snapshots of user
variables** (`% Snap`, `Order Price Snap`, `OQ Snapshot`). The Group was carved out of a working
canvas without promoting those references to ports. **The general lesson for your own
designs: if you intend a Group to be reusable, every value it reads from outside must enter
through a declared port, even when a jump or a formula reference would work.** That single
discipline is the entire difference between GREEN and RED.

**[V] `Sum of working orders` is the opposite case.** Its AMBER cost is thirteen inbound jumps —
numerically the highest in the corpus — but every one is the same trivial thing: an `Order`
block's `workingQuantity`. **[I]** AMBER count and AMBER difficulty are different quantities.
Thirteen mechanical wirings is a smaller job than one formula repair.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Cross-parameter validation** | `Branch(sum != 100 OR ...)` → 2 `Alert` → `Terminal(stop)` | the rule bounds cannot express, with a distinct message per failure |
| **Descending bound design** | `[0,100] / [0,99] / [0,98] / [0,97]` | encode as much of a cross-parameter rule in per-block bounds as the format allows |
| **`Round` for quantity allocation** | `Multiply` + `Divide` + `Round(normal)` | no epsilon, no remainder carry — cheaper and safer than `Floor` |
| **Per-level state template** | 1 `ValueAccumulator` + 7 `ValueExtractor` latches | design one level and replicate; makes N levels readable |
| **Working-quantity summer** | `Sum of working orders` | AMBER but mechanical; useful in any multi-order algo |
| **`onExtMod` per role** | StopManaging on the entry, Ignore on the exits | decide per block by what depends on that order |
| **Native stop orders** | `Order` with `type: stopMarket` / `stopLimit` | the only corpus example; compare the synthetic stop in [brackett.md](brackett.md) |

## Jump inventory

**[V]** 129 jumps → 201 landings. Highest fan-out in the corpus:

| Name | Landings |
|---|---:|
| `MPI` | **12** |
| `Inst:val` | 9 |
| `Stop`, `Fill Price:val`, `Stop Limit Enabled?:val` | 8 each |
| `V4 Entry Fills:accVal` | 5 |

**[I]** Every one of the top six is a value consumed once per level, per order type — the fan-out
count is essentially `levels × order-types`. In an algo built by replication, jump fan-out is a
direct measure of how many copies of the template exist.

**[V]** 3 `Note` blocks, **all empty** — canvas furniture, as in
[market-base.md](market-base.md). For the corpus's algos that actually carry written rationale,
see [minvol.md](minvol.md) and [oco-2.md](oco-2.md).

## Related

[brackett.md](brackett.md) is the same bracket concept at one level, built with virtualization
and a synthetic stop instead of thirteen static `Order` blocks — read the pair to see the
static-vs-virtual trade-off. [market-base.md](market-base.md) shares the Alert/Terminal
vocabulary. For the `Floor`-plus-epsilon alternative to this file's `Round`, see
[oco-2.md](oco-2.md).

**Cited from:** [brackett.md](brackett.md) for the bracket concept at production scale and the
second both-layers-of-validation example · [oco-2.md](oco-2.md) for `Round` as the simpler
alternative to `Floor`-plus-epsilon · [market-base.md](market-base.md) for the jump-density and
`Order`-block comparisons · [tt-sniper.md](tt-sniper.md) for `Math Min` ·
[conditional.md](conditional.md) for the per-role `onExtMod` rule ·
[with-a-tick.md](with-a-tick.md) for the "ignore and cooperate" state template.
