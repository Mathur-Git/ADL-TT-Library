# OCO

The same One-Cancels-Other problem as [oco-2.md](oco-2.md), rebuilt two years later. 196
blocks, two Groups, the same three toggles — and four substantive changes that are more
instructive than either algo taken alone, because they show what TT decided was wrong with the
first attempt.

**The headline: OCO adds the `IsNumber` guard on exactly the division that
[oco-2.md](oco-2.md) leaves unguarded.** Same formula, same block, same position in the graph,
two years apart. If you want evidence that the NaN discipline in
[gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md) matters in production rather
than in principle, this diff is it.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `OCO.adl.json` |
| Algo id | `b71e70a0-cde0-4e3c-ba30-050fc1fe6ff8` |
| Last modified | **2021-02-13** 13:08:18 UTC (OCO 2: 2019-04-03) |
| Size | 292,154 bytes |
| Flat blocks / true blocks | 60 / **196** (OCO 2: 131) |
| Subgraphs / max depth | 2 / 1 |
| Edges | 194 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta: **false**` |

**[V]** An OMA with **27** `ExistingOrder` blocks, against OCO 2's two.

> **[U] Every `ExistingOrder` block in the corpus has `required: true`** — all 27 here, both in
> OCO 2, both in [conditional.md](conditional.md), the single ones in
> [minvol.md](minvol.md) and [with-a-tick.md](with-a-tick.md). If the property meant "the
> operator must attach an order here", this algo would demand 27 orders before it could run,
> which cannot be the intent. So either it means something else, or ADL applies it differently
> when the blocks are optional siblings. Nothing in adl-kb's
> [Existing Order](../../adl-kb/guides/block-catalog.md) coverage settles it. **Do not copy the
> flag assuming you know what it does.**

## Operator surface

**[V]** Identical to [oco-2.md](oco-2.md) — `Proportional` (false), `Enforce Mkt State` (true),
`Delete Orphan` (true). No exports, no numeric variables. **[I]** Two years of rework and the
operator surface did not change by one control; all four changes below are internal.

## What changed from OCO 2, and why it matters

### 1. The NaN guard **[V]**

OCO 2, inside the virtual worker:

```
QtyFraction = Divide( Order:workingQuantity , largestOrder )   --> Fraction (IfThen)
```

OCO, same place:

```
Divide0  = Divide( OrderDetails:workingQuantity , LargestOrder )
IsNumber0( Divide0 )
IfThen1( IsNumber0, Divide0, Number0 = 0 )   --> Fraction (IfThen)
```

**[V]** One `IsNumber` block and one `IfThen`, inserted between the division and everything
downstream. **[I]** `LargestOrder` is a `DiscreteMax` output, which returns `NaN` after a reset
by design ([block-catalog](../../adl-kb/guides/block-catalog.md)); the quotient feeds a chain
that ends on the SOC's quantity input, and a `NaN` arriving there **deletes the working order**.
The guard substitutes 0 instead.

**[V]** This is one of only 7 `IsNumber` blocks in the entire corpus, across 2 files. **[I]**
The format spec's §6 note — *"TT's own algos guard sparingly because they rarely divide; if
your design divides, you need `IsNumber` more than this corpus suggests"* — reads differently
once you notice that the one algo which *does* divide grew a guard on its second iteration.
**The rule to take away: every `Divide` whose result can reach an order-managing block gets
`IsNumber` + `IfThen` immediately downstream.** Two blocks, always.

### 2. Twenty-seven orders, behind one port **[V]**

```
Group "ExistingOrders"  [GREEN, 41 blocks, one port: out message "Funnel14"]
   27x ExistingOrder --> 18x Funnel (a merge tree) --> Connector "Funnel14"
```

**[I]** `Funnel` merges discrete pathways because a discrete input accepts only one edge, and
it takes at most 3 inputs ([block-catalog](../../adl-kb/guides/block-catalog.md); the format
spec §3 records a maximum wired arity of 3). Twenty-seven sources therefore need a **tree** of
funnels — 18 of them — to become one stream. The whole tree is wrapped in a Group with a single
output port, so the rest of the algo sees one message source.

**[I] This is the cleanest structural idea in the file and it generalises immediately:** when
you need N of something discrete, build the fan-in as a funnel tree inside its own Group and
expose one port. The consumer never learns how many there were. Widening the algo from 27 to 40
orders is then a change inside one Group, and nothing downstream moves.

**[V]** It is also **GREEN** — no jumps in, no formula leaks — so it transplants for the cost of
one edge.

### 3. Rebroadcast and reset **[V]**

The virtual worker grew from 66 to 95 blocks, and from 10 ports to 13. The three new ones are
`Reset in progress` (bool, in), `Reset` (message, out) and `Rebroardcast` (message, out — TT's
own spelling).

```
Group0 "Rebroardcast" (out) --> Jump --> Funnel0 --> back into the worker's message input
Group0 (out) --> Rebroardcast in process (ValueExtractor, TRUE)
   --> Jump --> Group0 port "Reset in progress"
   --> Stopwatch2 (formula 50) --> resets itself
   --> Sequence2 --> [the re-entry sequence]

inside: ExternalQtyChange (Branch, {isExternalEvent}) --> Sequence0 --> Connector "Reset"
        Reset in progress --> Generator3 (boolTrue), Not1
        Freeze qty  (ValueExtractor, @SingleOrderContainer0 + @Fills)
        Fill Snapshot (ValueExtractor, @Fills)
        IfThen0( ValueExtractor1, Freeze qty, input qty + Fill Snapshot )
```

**[I]** Read: when a human externally changes an order's quantity, the affected instance
declares a **reset**; the algo latches "rebroadcast in progress", re-injects every order's state
through the worker again, and **freezes** each instance's quantity arithmetic at a snapshot
(`working + fills so far`) while the sweep runs — so the proportional reduction does not act on
half-updated numbers. `Stopwatch2 (50)` bounds the sweep.

**[I] The transferable idea is the freeze, not the plumbing.** Any design that computes each
participant's share from a global total has a window where the total has changed and the shares
have not. OCO 2 has no answer to it; OCO's answer is: a boolean saying "recalculation in
progress", a `ValueExtractor` snapshot of every input taken when it goes true, an `IfThen`
choosing snapshot-vs-live, and a short `Stopwatch` guaranteeing the window closes. **[V]** 50 ms
here, against the 250 ms used for order-deletion settling — the delays are sized to what they
wait for, not copied from each other.

### 4. Order-active gating **[V]**

```
OrderDetails msg --> OrderStatusCheck (Branch, @orderActive)
     out0 (no) --> Jump "OrderStatusCheck:no" --> orderActive (ValueExtractor, TRUE)
orderActive out1 (msg) --> SingleOrderContainer0
```

**[I]** An instance takes over its order only on the *first* message that finds `orderActive`
false, latching it true. It is a de-duplication guard: with a rebroadcast mechanism re-injecting
messages, an instance must not hand the same order to its SOC twice. **[V]** The
`orderActive:val` jump is dead — the latch is read by the `Branch`'s formula (`@orderActive`)
rather than through a wormhole, and the jump is a leftover.

## What did not change

**[V]** Everything else is recognisably the same design as [oco-2.md](oco-2.md), block for
block:

| Mechanism | Same? |
|---|---|
| One virtual instance per order, identified by `userField1` | yes |
| `ValueBucket` (`mode: last`, key `{userField1}`, value `{userField2}`) as cross-instance memory | yes |
| `Loop` over `@orderNum` with reset-then-count `Sequence`, tallying `NumOpen` / `NumClosed` | yes |
| `AnyStateMismatch` = `@NumClosed > 0 AND @NumOpen > 0` | yes |
| `Epsilon` = 1e-10 added before both `Floor`s | yes |
| `Remainder` carry-forward `ValueExtractor` | yes |
| 250 ms grace `Stopwatch` before `Terminal` and before the `Loop` | yes |
| `OnceTrue` latch on order-quantity-zero | yes |
| `Generator(everyStart)` initialising the shared table | yes |
| `AllDeletedOrOrphans?` = `@Delete Orphan OR (@DeletedOrderCount == @orderNum)` | yes |

**[I]** Read the mechanisms up in [oco-2.md](oco-2.md), which analyses each in full; this doc
does not repeat them.

**[V]** One difference worth noting in the intake: OCO has **no suspended-order swap**. There is
no `Branch{isSuspended}`, no clone `DiscreteOrder`, no delete-SOC — and no `DiscreteOrder` block
at all. **[U]** Whether the swap was found unnecessary or the 27-order intake made it
impractical is not answerable from the file.

## Stop gaps

| Guard | Present? | vs OCO 2 |
|---|---|---|
| `Terminal` | **[V]** 1, `stop`, behind a 250 ms grace | same |
| `Alert` | **[V]** **none** | same — still no operator message anywhere |
| `IsNumber` | **[V]** **1** | **added** |
| `MarketState` | **[V]** 1, `state: "open"`, per instance | same |
| `ignoreMarketState` | **[V]** `false` (explicit here, absent in OCO 2) | **[I]** same problem: the consensus machinery detects partial closure, a state the platform may pause the algo out of first ([block-catalog](../../adl-kb/guides/block-catalog.md)) |
| `Epsilon` | **[V]** 1e-10 before both `Floor`s | same |
| `Stopwatch` | **[V]** 3 — two at 250 ms, one at 50 ms | **one added** |
| Bounds | **[V]** n/a — no numeric variables | same |
| `Exit` in the virtual Group | **[V]** **none** | same — 95-block instances, never disposed |
| Dead jumps | **[V]** 1 (`orderActive:val`) | OCO 2 had none |

**[I]** So of the two clear defects in OCO 2 — the unguarded divisions and the missing `Exit` —
TT fixed one. The second `Divide` (`QtyRaw = fillQuantity / Fraction`) is **still unguarded**
in OCO; only the first was wrapped. `Fraction` is an `IfThen` that can select the guarded
quotient *or* the literal 1, so **[I]** it is plausibly never zero by construction — but that
is a reasoning step the graph does not make explicit, and it depends on `Number0 = 0` never
being selected while a fill arrives. **If you transplant the quantity chain, guard both.**

## Reuse

**[V]** Two Groups, both **GREEN**:

| Group | Tier | Size | Ports |
|---|---|---:|---|
| `Group0` (virtual) | GREEN | **95** | 8 in (`AnyOrphans`, `EnforceMktState`, `Fractional`, `LargestOrder`, `Reset in progress`, `SomeMarketsClosed`, `TotalFilledQty` real/bool + `ValueInjector0` message), 5 out (`FILL`, `MarketStateChanged`, `OrderDeleted`, `Rebroardcast`, `Reset`) |
| `ExistingOrders` | GREEN | 41 | 1 out: `Funnel14` (message) |

```bash
python tools/patterns.py --show    "ExistingOrders"
python tools/patterns.py --extract "ExistingOrders" --from "OCO.adl" -o order-fanin.json
python tools/patterns.py --extract "Group0" --from "OCO.adl" -o oco-worker-v2.json
python tools/validate.py order-fanin.json
```

**[V]** `ExistingOrders` is one of only three GREEN Groups in `patterns.py`'s named index (with
`SynthStop` and `MinAggressiveValueCheck`). **[I]** It is also the most mechanical: 27
`ExistingOrder` blocks and a funnel tree. Its value is the *shape*, and the shape is worth
copying even if you need 8 orders rather than 27 — delete the surplus, keep the tree.

**[I] `Group0` here supersedes OCO 2's.** It is 29 blocks larger, and every one of those blocks
is a fix: the NaN guard, the reset/rebroadcast protocol, the freeze snapshot, the active-order
latch. If you are taking the OCO worker, **take this one**, and read
[oco-2.md](oco-2.md) to understand the core it is built on.

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Guarded division** | `Divide` → `IsNumber` → `IfThen(ok, quotient, fallback)` | three blocks, and TT added them for a reason; make it reflexive |
| **N-source fan-in Group** | 18 `Funnel` + N sources + one `Connector` | one port hides arity; widening the algo touches one Group |
| **Freeze-during-recalculation** | bool + `ValueExtractor` snapshots + `IfThen` + bounding `Stopwatch` | the answer to "the global total moved while I was computing my share" |
| **Re-entry de-dup latch** | `Branch(@latch)` → `ValueExtractor(TRUE)` → the actor | stops a rebroadcast handing the same order over twice |
| **Delays sized to purpose** | 50 ms sweep, 250 ms delete-settle, 25 ms floor elsewhere | three different numbers in one design, each justified |

## Jump inventory

**[V]** 25 jumps → 30 landings, one dead (`orderActive:val`). The names follow the same
`<producer>:<output>` convention as every other file. Notable:

| Name | Source | Consumers |
|---|---|---|
| `Group0:MarketStateChanged` | the worker's out port | `VBMktState` |
| `Group0:Rebroardcast` | the worker's out port | `Funnel0` → back into the worker |
| `Rebroardcast in process:val` | `ValueExtractor` | the worker's `Reset in progress` port |
| `Loop0:currIndex` | `Loop0` | `VBMktState` lookup |
| `Sequence1:output_1` / `_2`, `Sequence2:output_1` / `_2`, `Sequence0:output_1` | the sequences | the reset/count/rebroadcast fan-outs |
| `Epsilon` | `Epsilon` (1e-10) | both `Add`s before the `Floor`s |
| `Fraction:output` | `Fraction` (IfThen) | `QtyRaw`, `Multiply0` |
| `orderActive:val` | `orderActive` | **no landing — dead** |

**[V]** Note `Group0:Rebroardcast` feeding a `Funnel` that re-enters `Group0`: a **jump from a
virtual Group's output port back to its own input**. Legal, because both ends are outside the
virtual boundary — the message left through a declared port before the jump picked it up. Jumps
themselves may not cross a virtual boundary
([block-catalog](../../adl-kb/guides/block-catalog.md)).

## Related

[oco-2.md](oco-2.md) is the earlier version and carries the full analysis of the shared
mechanisms — the `ValueBucket` consensus, the `Epsilon`-before-`Floor` idiom, the proportional
quantity chain, and TT's own `Note` blocks explaining them. [tt-sniper.md](tt-sniper.md) has
the corpus's other virtualized Group.

**Cited from:** [oco-2.md](oco-2.md) for the NaN fix and the shared mechanisms ·
[conditional.md](conditional.md) and [market-base.md](market-base.md) for the `IsNumber`
discipline · [tt-sniper.md](tt-sniper.md) for the `ValueInjector` count.
