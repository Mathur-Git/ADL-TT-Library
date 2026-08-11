# OCO 2

One-Cancels-Other for an arbitrary number of orders, built on a **virtualized Group** — one
instance per attached order — with a `ValueBucket` acting as shared memory between the
instances and a `Loop` scanning it. 131 blocks, five `Note` blocks of TT's own commentary,
three boolean toggles.

**This is the most technically ambitious file in the corpus**, and the one with the most to
steal. `Loop`, `ValueBucket` and `DiscreteMax` appear twice each corpus-wide — one instance
here and one in [oco.md](oco.md), its successor — so this pair of files is the only place any
of them can be studied, and this is the earlier, simpler of the two. It is also the file whose
own logic is closest to a live `NaN` hazard, which [oco.md](oco.md) later fixed.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `OCO 2.adl.json` |
| Algo id | `d2c5109d-10ac-48ca-b4f7-55b1c6afc7fc` |
| Last modified | 2019-04-03 21:57:34 UTC |
| Size | 188,597 bytes |
| Flat blocks / true blocks | 65 / **131** — half the algo is inside one Group |
| Subgraphs / max depth | 1 / 1 |
| Edges | 120 |
| Algo flags | `orderSide: true`, `ignoreMarketState` **absent**, `isOmaOta: true` |

**[V]** An **OMA**: two `ExistingOrder` blocks (`Order1`, `Order2`). **[I]** But the design is
written for *N* orders, not two — everything downstream is keyed by an order number and the
`Loop` iterates over however many exist. The two `ExistingOrder` blocks are the launch surface,
not a limit of the logic.

**[V]** `ignoreMarketState` has no key at all; the format spec treats missing as false (§1).

## Operator surface

**[V]** Three booleans, no numbers, no exports:

| Variable | Default | Meaning **[I]** |
|---|---|---|
| `Delete Orphan` | **true** | when one order finishes, delete the rest |
| `Enforce Mkt State` | **true** | stop the algo if the orders' instruments disagree about being open |
| `Proportional` | false | reduce the survivors in proportion to their size, rather than one-for-one |

**[V]** This matches the format spec's §7 observation exactly: *every risky behaviour is a
named, operator-visible switch, not a hardcoded branch*. All three switch off logic that could
delete a live order.

## What it does

### One virtual instance per order

**[V]**

```
Order1 / Order2 (ExistingOrder) --> Branch2 ({isSuspended}) --> [the suspended-order swap]
   --> Funnel1 --> OrderNum (ValueAccumulator, formula 1)      <-- the instance counter
   --> LargestOrder (DiscreteMax, formula {workingQuantity})
   --> ValueInjector0 (userField1 = @OrderNum)
   --> Group0  (virtual: true)  port "ValueAccumulator0" (message in)
```

**[I]** Each order that arrives is stamped with a serial number in `userField1` and handed to
the virtualized Group, which spawns an independent copy to manage exactly that order
([block-catalog](../../adl-kb/guides/block-catalog.md), rules of virtualization). Inside, the
first thing the instance does is read its own number back out:

```
Connector "ValueAccumulator0" --> OrderNumber (ValueExtractor, formula {userField1})
                              --> Order (MsgInfoExtractor) --> SingleOrderContainer1
```

**[V] This and [oco.md](oco.md) are the corpus's only demonstrations of identity inside a
virtualized block**, and the mechanism is one adl-kb points at without showing: ordinary continuous values inside a virtual
instance are unreachable from outside, and data crosses the boundary only inside a discrete
message — `userField1..4` being the general-purpose smuggling channel
([block-catalog](../../adl-kb/guides/block-catalog.md)). Here the channel is used *inbound*, to
give each instance a name.

**[V]** The suspended-order swap on the way in is the same shape as
[conditional.md](conditional.md) and [minvol.md](minvol.md): `Branch{isSuspended}` → `Sequence`
→ `DiscreteOrder(clone)` → an SOC with a static `TRUE` on its delete input. **[I]** Three
independent files, one idiom — treat it as the house way to normalise an attached order.

### Cross-instance state: `ValueBucket` as shared memory

TT's own `Note`, verbatim **[V]**:

> *"Any time the market state of an order's instrument changes, a message will come out of the
> Virtual Block. When this happens, we set its state in the ValueBucket block indexed at the
> block # in question. We then loop over *all* instruments, counting how many are open, and how
> many are not. As long as they are either all open or all closed, we don't do anything; but
> after a 250ms grace period if some are open and some are not, we delete all orders and stop
> the algo."*

**[V]** The wiring, inside the instance:

```
Order:instrument --> OrderInstIsOpen (MarketState, state "open") --> Not0
   --> Generator3 (mode: boolChange)   \
   --> Generator5 (mode: everyStart)   /--> Funnel0 --> ValueInjector0
        ValueInjector0 injects: isTriggered = @OrderInstIsOpen
                                userField1  = @OrderNumber
   --> Connector "MarketStateChanged"  (message out)
```

and outside:

```
Jump "Group0:MarketStateChanged" --> VBMktState (ValueBucket, mode "last",
                                        storeKey = {userField1}, storeVal = {userField2})
VBMktState --> Stopwatch2 (250) --> Sequence0
        out1 --> Jump "Sequence0:output_1" --> reset NumOpen, reset NumClosed
        out2 --> Loop0 (times = @OrderNum)
                 out1 currIndex --> Jump --> VBMktState lookup key
                 out2 loop      --> Branch1 (@VBMktState == 2) --> NumClosed / NumOpen
                 out0 exit      --> AnyStateMismatches (ValueExtractor,
                                       @NumClosed > 0 AND @NumOpen > 0)
```

**[I] This is the general solution to "virtual instances need to agree about something", and
nothing else in the corpus or in adl-kb shows it.** The pattern in full:

1. every instance publishes its own state outward as a **discrete message**, keyed by its
   instance number in `userField1` (a continuous port would be illegal — virtual Groups may not
   have continuous outputs);
2. a single `ValueBucket` *outside* the Groups stores `key → value`, `mode: "last"`, so each
   instance overwrites only its own slot;
3. a `Loop` whose `times` input is the instance counter walks every slot, resetting two
   `ValueAccumulator` counters first and tallying into them;
4. a `ValueExtractor` on the `Loop`'s exit port turns the tally into a single boolean.

**[V]** Note the ordering discipline: `Sequence0` resets the counters through output 1 and only
then starts the `Loop` through output 2 — a `Sequence` waits for each pathway to complete
before firing the next ([block-catalog](../../adl-kb/guides/block-catalog.md)). Reset-then-count
in one atomic sweep is the whole reason the tally is trustworthy.

**[V]** And the initialisation, from a second `Note`:

> *"Here, we immediately send a message out of the Mkt State port to initialize the outside VB
> block"*

— which is what `Generator5 (mode: everyStart)` is for. **[I]** A shared table is empty until
someone writes to it, and an empty slot in a `Loop` scan is indistinguishable from a closed
market. The `everyStart` generator publishes the initial value on launch *and on every resume*
— the same repair-on-resume habit that [minvol.md](minvol.md) documents from the other
direction.

**[V]** `Branch1`'s formula is `@VBMktState == 2`, so the market-state value is stored as a
small integer code. **[U]** What 2 means is not in the file and not in adl-kb's `MarketState`
page; it is `isTriggered` fed through `userField2` **[I]** and reconstructed on the far side.

### The 250 ms grace periods

**[V]** Two `Stopwatch` blocks, both `250`, and TT's `Note`:

> *"We add a 250ms grace period so that the various order blocks have a chance to delete the
> orders."*

**[I]** `Stopwatch2` sits between the `ValueBucket` write and the `Loop`, so the scan happens
after the burst of state changes has settled — a `Stopwatch` restarts on each new message
([block-catalog](../../adl-kb/guides/block-catalog.md)), making it a debounce over the whole
burst rather than a delay per message. `Stopwatch3` sits between the stop condition and
`Terminal0`, so the deletes get out before the algo dies.

**[I] 250 ms, not 25.** The other small algos use the 25 ms floor as "as short as legal". Here
the number is chosen for a real settling process — several orders being deleted across
several instances. If you copy a grace period, copy the reasoning, not the constant.

### Proportional quantity reduction — and `Epsilon`

TT's `Note` **[V]**:

> *"The current order qty formula takes into account (1) the global total fill count, (2) the
> number of fills received from this particular order (to offset my contribution to the global
> count) and (3) the fractional qty component of this order in relation to the others."*

**[V]** Inside the instance:

```
Fraction     = IfThen( Fractional, QtyFraction, 1 )
QtyFraction  = Divide( Order:workingQuantity , largestOrder )
QtyRaw       = Divide( <fill quantity from the demux> , Fraction )
Remainder    = ValueExtractor( QtyRaw - QtyFloor )
QtyFloor     = Math Floor( QtyRaw + Remainder + Epsilon )
ValueInjector1 injects fillQuantity = @QtyFloor  --> MyTotalFills (VA, {fillQuantity})

Subtract0 = TotalFilledQty - MyTotalFills          (everyone else's fills)
Multiply0 = Fraction * Subtract0
Math0     = Floor( Multiply0 + Epsilon )
OrderQty  = Order:orderQuantity - Math0            --> SingleOrderContainer1.qty
```

**[I]** Read: *this order's quantity is its original size, less its share of everybody else's
fills.* `Fraction` is its size relative to the largest order in the set, so a half-size order
gives up half as much. `MyTotalFills` is subtracted out so an instance never reduces itself for
its own fills.

**[V] `Epsilon` is a static `Number` with value `1e-10`, and it is added immediately before
each `Floor`.** Twice, in both quantity paths. It appears only here and in
[oco.md](oco.md).

**[I] That is a more specific idiom than the format spec's §7 summary suggests.** The spec
reads `Epsilon` as "float comparisons get an explicit tolerance, never `==`"; what TT actually
does here is **defend `Floor()` against binary representation error** — without it,
`Floor(3.0)` computed as `2.9999999996` silently loses a lot. Both uses are legitimate, but if
you are copying the idiom, copy this one: **any `Math Floor` fed by a division needs an epsilon
added first.** The corpus has no counter-example.

**[V]** Note also the `Remainder` `ValueExtractor`: it snapshots the fractional part left over
from the previous fill and adds it back into the next one. **[I]** Fractional quantity is
carried forward rather than discarded, so a sequence of small fills eventually releases the
whole unit instead of rounding each one to nothing. That is a genuinely subtle piece of
engineering and it is three blocks.

### Orphan deletion and shutdown

**[V]**

```
Group0 "OrderDeleted" (message out) --> DeletedOrderCount (VA, formula 1)
And0 = @Delete Orphan AND (DeletedOrderCount > 0)   --> Group0 port "AnyOrphans"
inside: Or1( Or0( OrderQtyZero, EnforceMktState AND SomeMarketsClosed ), AnyOrphans )
        --> SingleOrderContainer1.del

AllDeletedOrOrphans? (Branch): @Delete Orphan OR (@DeletedOrderCount == @OrderNum)
        --> Funnel0 --> Stopwatch3 (250) --> Terminal0 (mode: stop)
And1 = @Enforce Mkt State AND @AnyStateMismatches --> Generator0 (boolTrue) --> Funnel0
```

**[I]** Three independent reasons to delete an order from inside its instance — it finished
(`OrderQtyZero`, a `OnceTrue` latch on `workingQuantity == 0`), markets disagree, or a sibling
finished and orphan-deletion is on. Two reasons to stop the algo, both routed through the same
250 ms grace `Stopwatch`.

**[V]** `OrderQtyZero` is a `OnceTrue` — the same irreversibility trick as
[with-a-tick.md](with-a-tick.md), here ensuring a momentarily-zero working quantity latches the
order as done rather than flickering.

## Stop gaps

| Guard | Present? | Detail |
|---|---|---|
| `Terminal` | **[V]** 1 | `stop`, behind a 250 ms grace period; no pause tier |
| `Alert` | **[V]** **none** | five `Note` blocks explaining the design to *readers*, and not one message to the *operator* |
| `MarketState` | **[V]** 1 | `state: "open"`, per instance, aggregated by consensus |
| `ignoreMarketState` | **[V]** absent (= false) | **[I]** see below |
| `IsNumber` | **[V]** none | **two live divisions** — see below |
| `Epsilon` | **[V]** 1e-10 | before both `Floor`s |
| Bounds | **[V]** n/a | no `Number` user variables at all |
| `Exit` in the virtual Group | **[V]** none | instances are never disposed |

**[I] The NaN exposure here is the most concrete in the corpus.**
`QtyFraction = workingQuantity / largestOrder` divides by a `DiscreteMax` output, and
`QtyRaw = fillQuantity / Fraction` divides by that result. adl-kb: `0/0 → -nan`, `n/0 →
±infinity`, both invalid as ADL inputs, and **a `NaN` reaching a block that manages a working
order deletes that order** ([block-catalog](../../adl-kb/guides/block-catalog.md)). The result
of this chain lands on `SingleOrderContainer1`'s quantity input. `DiscreteMax` returns `NaN`
after a reset by design. There is no `IsNumber` anywhere in the file.

Whether the ordering can actually produce a zero or reset `largestOrder` while an instance is
live is **[U]** and not decidable from the file. But this is exactly the case the format spec
flags: *"TT's own algos guard sparingly because they rarely divide — if your design divides,
you need `IsNumber` more than this corpus suggests"* (§6). **If you transplant the proportional
quantity chain, put an `IsNumber` gate between it and the SOC.**

**[I] The `ignoreMarketState` problem is worse here than in
[with-a-tick.md](with-a-tick.md).** adl-kb says the algo auto-pauses whenever a market leaves
its session unless the setting is enabled, *"which is exactly the case you were testing for"*
([block-catalog](../../adl-kb/guides/block-catalog.md)). The entire consensus machine exists to
detect **partial** closure across instruments — which is precisely a state the platform may
pause the algo out of before the `Loop` ever runs. The setting is absent from the file. Either
TT relied on the pause being per-instrument in a way adl-kb does not document (**[U]**), or the
`Enforce Mkt State` path is defensive belt for a case the platform usually handles first.
Settle this before relying on it.

**[V] No `Exit` block inside the virtual Group** — the same accumulation issue as
[tt-sniper.md](tt-sniper.md), and here each instance is 66 blocks. **[I]** For a two-order OCO
that never matters; for a long-lived algo attaching orders repeatedly it does.

## Reuse

**[V]** One Group, and its tier is the headline:

| | |
|---|---|
| Name | `Group0` |
| Tier | **GREEN** — no inbound jumps, no formula leaks |
| Size | **66 blocks**, 59 edges, `virtual: true` |
| Ports | in: `AnyOrphans` bool, `EnforceMktState` bool, `Fractional` bool, `SomeMarketsClosed` bool, `TotalFilledQty` real, `largestOrder` real, `ValueAccumulator0` message · out: `FILL`, `MarketStateChanged`, `OrderDeleted` (all message) |

```bash
python tools/patterns.py --show "Group0" --from "OCO 2"
python tools/patterns.py --extract "Group0" --from "OCO 2" -o oco-worker.json
python tools/validate.py oco-worker.json
```

**[I] A 66-block GREEN Group is the best value in the corpus.** Everything it needs arrives
through ten declared, typed ports; nothing inside reaches out. That is not luck — it is forced
by virtualization, which bans continuous outputs and makes jumps illegal across the boundary
([block-catalog](../../adl-kb/guides/block-catalog.md)). **Virtualization is therefore also a
discipline that produces transplantable parts**, which is a reason to reach for it beyond the
per-instance behaviour it exists for.

What you get for wiring ten ports: an order manager that takes over one attached order, tracks
its own fills, reduces its quantity as siblings fill, deletes itself on three conditions, and
publishes its market state and death outward as messages.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **The whole worker** | `Group0` | GREEN, virtual, complete; the corpus's best single transplant |
| **Instance identity** | `ValueAccumulator(1)` + `ValueInjector(userField1)` + `ValueExtractor({userField1})` | how a virtual instance learns its own name; nothing else shows this |
| **Cross-instance consensus** | `ValueBucket(last)` + `Loop` + reset-then-count `Sequence` + `ValueExtractor` | shared memory between instances that cannot share continuous data |
| **Epsilon before Floor** | `Add(x, 1e-10)` → `Math Floor` | the corpus's only defended `Floor`; `Epsilon` appears here and in [oco.md](oco.md) only. Where floor semantics are not required, [tt-multi-level-bracket.md](tt-multi-level-bracket.md)'s `Round` is simpler |
| **Remainder carry-forward** | `ValueExtractor(raw − floored)` fed back into the next `Add` | fractional quantity accumulates instead of vanishing |
| **Settling grace period** | `Stopwatch(250)` before `Terminal` | let the deletes leave before the algo stops |
| **Suspended-order swap** | `Branch{isSuspended}` + `Sequence` + clone `DiscreteOrder` + delete-SOC | third independent occurrence; the house idiom |

Do not take the quantity chain without adding an `IsNumber`, and do not take the virtual Group
without adding an `Exit`.

## Jump inventory

**[V]** 18 jumps → 23 landings, **none dead**. Only this file and
[conditional.md](conditional.md) have a completely clean wormhole set; every other corpus file
carries at least one `Jump` with no landing (see the method note on how "dead" is counted).
Highlights:

| Name | Source | Consumers |
|---|---|---|
| `Group0:MarketStateChanged` | the Group's out port | `VBMktState` (the shared table) |
| `Loop0:currIndex` | `Loop0` | `VBMktState` lookup key |
| `Sequence0:output_1` | `Sequence0` | `NumOpen`, `NumClosed` (the resets) |
| `AnyStateMismatches:val` | `AnyStateMismatches` | `Group0`, `And1` |
| `Epsilon` | `Epsilon` (Number, 1e-10) | `Add2`, `Add3` |
| `Fraction:output` | `Fraction` (IfThen) | `QtyRaw`, `Multiply0` |
| `OrderQtyZero` | `OrderQtyZero` (OnceTrue) | `Or0` |
| `Order:instrument` / `:orderQuantity` / `:workingQuantity` / `:messageOut` | `Order` (MsgInfoExtractor) | inside the instance |

**[V]** Note that `Order:*` jumps live entirely *inside* the virtual Group — jumps may cross
Group boundaries but **not** virtual ones
([block-catalog](../../adl-kb/guides/block-catalog.md)), which is why every value entering or
leaving `Group0` uses a declared port instead.

## Related

[oco.md](oco.md) is the same problem solved without virtualization — read them as a pair; the
block counts (196 vs 131) and the tier verdicts diverge sharply.
[tt-sniper.md](tt-sniper.md) has the corpus's other virtual Group, six blocks instead of
sixty-six. For the `Alert` this file lacks, see [tt-sniper.md](tt-sniper.md) and
[market-base.md](market-base.md).

**Cited from:** [oco.md](oco.md) throughout — it is the successor and carries the diff ·
[conditional.md](conditional.md) and [minvol.md](minvol.md) for the suspended-order swap ·
[tt-sniper.md](tt-sniper.md) and [brackett.md](brackett.md) for virtualization without an `Exit`
and for the `ValueInjector` · [tt-multi-level-bracket.md](tt-multi-level-bracket.md) for the
`Floor`-plus-epsilon vs `Round` comparison · [with-a-tick.md](with-a-tick.md) for `OnceTrue`.
