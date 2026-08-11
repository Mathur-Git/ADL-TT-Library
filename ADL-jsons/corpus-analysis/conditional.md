# Conditional

The smallest algo in the corpus and the best one to read first: 43 blocks, one flat graph, no
Groups, no user variables. It is a complete, shipping **OMA** in 56 KB, and every idiom in the
big algos appears here in miniature — a state-machine release loop, a `Sequence` for ordering,
a `Jump` mesh instead of long edges, and a `Stopwatch` used as a settle-delay before shutdown.

Derivation and confidence conventions: [how-these-were-derived.md](how-these-were-derived.md).

## Source

| | |
|---|---|
| Exact basename | `Conditional.adl.json` |
| Algo id | `4a162ddd-6dec-4fde-a7f8-d6667d3b0a43` |
| Last modified | 2019-04-03 21:50:12 UTC |
| Size | 56,787 bytes |
| Flat blocks / true blocks | 43 / **43** — the only corpus file where they are equal |
| Subgraphs / max depth | 0 / 0 |
| Edges | 41 |
| Algo flags | `orderSide: true`, `ignoreMarketState: false`, `isOmaOta: true` |

**[V]** It is an **OMA** — it contains `ExistingOrder` blocks, which is the definition
([algo-types](../../adl-kb/guides/algo-types.md)). Two of them, *both* with `required: true`,
so the operator must attach it to **two** orders before it does anything.

## Operator surface

**[V] `variables` is empty and `exports` is empty.** Nothing is editable at launch and nothing
appears as a dashboard column. Every parameter is structural: the ratio comes from the two
attached orders' own quantities, so there is nothing left to tune. This is worth noticing
before you copy the file — it is the *only* corpus algo with a zero-width operator surface,
and it gets away with it because both of its inputs are orders, not numbers.

## What it does

**[I]** A **proportional release**: attach it to a large *Primary* order and a held-back
*Conditional* order, and it releases the conditional order in proportion to how much of the
primary has filled. Fill 30% of the primary, and 30% of the conditional becomes live.

The mechanism is two independent intake paths that meet at an arithmetic chain.

### Intake A — take over the Primary, and un-suspend it if needed

**[V]** wiring:

```
Primary (ExistingOrder, required)
  -> Primary (MsgInfoExtractor)          selects: instrument, orderQuantity
       out0 instrument ---------------> DiscreteOrder0~6529ffb1  (instrument in)
       out1 orderQuantity ------------> Jump "Primary:orderQuantity"
       out7 msg pass-through ---------> IsSuspended? (Branch)  formula: {isSuspended}
  IsSuspended?  out1 --> Sequence0 --> out1: DiscreteOrder0~6529ffb1
                                   \-> out2: SingleOrderContainer1  (del <- Boolean0 = TRUE)
  IsSuspended?  out0 --> Funnel1 in2
  DiscreteOrder0~6529ffb1 Add OK --> Funnel1 in1
  Funnel1 --> SingleOrderContainer0   (onExtMod: StopManaging)
```

**[I]** Read: *if the attached primary order is suspended, replace it.* `DiscreteOrder0~6529ffb1`
carries `cloneIncomingOrder: true` and **no field formulas at all** — every entry in its
`formula` property is an empty string — so it re-submits the incoming order verbatim as a live
one. `SingleOrderContainer1` then receives the original and has a static `Boolean0 = TRUE`
wired to it, which deletes it. If the order was *not* suspended, the `Branch`'s other output
routes the original message straight through `Funnel1` unchanged.

Either way `SingleOrderContainer0` ends up managing exactly one live primary order. The
`Funnel` is there because a discrete input accepts only one edge
([block-catalog](../../adl-kb/guides/block-catalog.md)) — the two mutually exclusive paths have
to be merged before the SOC.

**[I]** `Sequence0` matters here: the clone must be submitted *before* the original is deleted,
or there is a window with no order in the market. This is the canonical use of `Sequence` —
never fan a discrete output out to two consumers and hope
([core-semantics](../../adl-kb/guides/core-semantics.md)).

### Intake B — take over the Conditional, and hold it back

```
ConditionalOrder (ExistingOrder, required)
  -> Conditional (MsgInfoExtractor)   selects: instrument, orderQuantity
       out0 instrument --> Jump "Conditional:instrument"
       out1 orderQty    --> Jump "Conditional:orderQuantity"   (2 landings)
  -> Jump "ConditionalOrder"  (2 landings)
       landing 1 --> SingleOrderContainer2 in0   (onExtMod: Ignore)
       landing 2 --> Funnel0 in1                 (kicks the state machine on attach)
  SingleOrderContainer2  qty in3 <-- Jump "HeldQty"
  SingleOrderContainer2  msgs out1 --> Demultiplexer1 --> Funnel0 in0
```

**[V]** `SingleOrderContainer2`'s quantity input is driven continuously by `HeldQty`. That is
the holding mechanism: the conditional order's working quantity is *whatever the arithmetic
chain says has not been released yet*.

### The arithmetic chain

**[V]** Four blocks, all continuous:

```
Ratio        = Divide( Primary:orderQuantity , Conditional:orderQuantity )
CounterFills = Divide( PrimaryFills          , Ratio )
Rounded      = Math( Floor(x) )  of CounterFills
HeldQty      = Subtract( Rounded , Conditional:orderQuantity )
```

`PrimaryFills` is a `ValueAccumulator` with formula `{fillQuantity}` fed from the primary
SOC's demultiplexed message stream — a running total of primary fills.

**[I]** Substituting: `CounterFills = primaryFilled × condQty / primaryQty`, i.e. the share of
the conditional order that the primary's fills have earned. `Floor` snaps it to a whole
releasable quantity. `HeldQty` is that against the conditional order's total.

**[U] Operand order is not recoverable from the file.** `Subtract in0 - in1` is a positional
label from `block-catalog.json`, not documented operand order (see the method note). Taken
literally the edges give `Rounded − condQty`, which is negative; the block's own label says
`HeldQty`, which is positive. One of the two readings is inverted and **the file cannot settle
which**. If you lift this chain, verify the sign in the Designer before trusting it. That
ambiguity is the single most important thing to know before copying anything arithmetic out of
any corpus file.

### The release loop

```
Funnel0 --> State0
State0 formula, output "1":  Rounded > LastTotalFillCount
State0 formula, output "2":  (empty - the default, wired to nothing)

State0 out0 --> Sequence1
      out1 --> DiscreteOrder0~8e027201     quantity formula: Rounded - LastTotalFillCount
      out2 --> LastTotalFillCount (ValueExtractor)  formula: Rounded
      out0 --> Funnel0 in2                 (loops back into State0)
```

**[I]** A latch-and-drain loop. `LastTotalFillCount` is a `ValueExtractor` snapshotting
`Rounded` — "how much have we released so far". `State0` only fires while `Rounded` exceeds it,
`DiscreteOrder0~8e027201` submits exactly the newly-earned increment, the `ValueExtractor` then
advances the watermark, and the loop-back re-enters `State0` to check whether more is owed.
When the watermark catches up, `State0` falls to its empty default output, which is wired to
nothing — the pathway ends and nothing further happens until the next fill message.

**[I]** This is a genuinely reusable idiom and it is nowhere in
[design-patterns](../../adl-kb/guides/design-patterns.md): *a monotone target value, a
watermark holding what has been acted on, and a State-gated loop that drains the difference
one increment at a time.* It generalises to any "scale into a position as some signal
advances" design. It needs only `State`, `ValueExtractor`, `Sequence`, `Funnel` and a
`DiscreteOrder` — all common blocks, none of them Group-wrapped, so it is the cheapest thing
in the whole corpus to copy.

**[V]** Note the `Sequence1` ordering: the order goes out *before* the watermark advances. Get
that backwards and a slow order submission would release the same increment twice.

### Shutdown

```
PrimaryFills out1 (msg) --> IsFullyFilled? (Branch)  formula: {workingQuantity} == 0
                       out1 --> Stopwatch0  (formula: 25) --> Terminal0 (mode: stop)
```

**[I]** When the primary has no working quantity left, wait 25 ms, then stop the algo. The 25
is not a tuning choice — it is the documented **Stopwatch minimum**
([gotchas-and-limits](../../adl-kb/guides/gotchas-and-limits.md)), so this is "the shortest
delay ADL will accept", used to let the in-flight release pathway finish before the algo dies.
`Stopwatch` is a debounce, not a queue: each new message restarts the timer, so a burst of
final fills collapses into one shutdown.

## Order blocks and external interference

**[V]**

| Block | `onExtMod` | Notable |
|---|---|---|
| `SingleOrderContainer0` (primary) | **StopManaging** | |
| `SingleOrderContainer1` (deletes the suspended original) | Ignore | |
| `SingleOrderContainer2` (conditional) | Ignore | |
| `DiscreteOrder0~6529ffb1` (clone of primary) | StopManaging | `cloneIncomingOrder: true`, all field formulas empty, `TIF: day` |
| `DiscreteOrder0~8e027201` (release slice) | Ignore | `leaveOnPauseCancel: ["Pause","Cancel"]`, `TIF: day` |

**[I]** The stance is asymmetric and deliberate: touch the **primary** by hand and the algo
lets go of it (`StopManaging`); touch a **release slice** and the algo carries on. That is the
right way round — the primary is the thing whose fills drive everything, so a human
overriding it invalidates the algo's model of the world, while an individual released slice is
disposable. Copy the asymmetry, not just the settings.

**[V]** `leaveOnPauseCancel: ["Pause","Cancel"]` on the release order means released quantity
survives a pause. **[I]** Consistent with the rest: once quantity has been earned and released
it belongs to the market, not to the algo's control loop.

## Stop gaps — what is missing

This is the part to read before reusing anything here. **[V]**, by absence:

- **No `Alert` blocks at all.** The algo stops without telling the operator why. Every larger
  corpus algo pairs `Terminal` with `Alert` (format spec §7); this one does not. If you copy
  the shutdown path, add the Alert.
- **No `IsNumber` guard, and two `Divide` blocks.** `Ratio = primaryQty / condQty` divides by
  a quantity taken from an attached order; `CounterFills` then divides by `Ratio`.
  [block-catalog](../../adl-kb/guides/block-catalog.md) is explicit that `0/0 → -nan` and
  `n/0 → ±infinity`, and that **a NaN reaching a block managing a working order deletes that
  order**. `HeldQty` feeds `SingleOrderContainer2`'s quantity directly. **[I]** So a
  degenerate attach — a conditional order whose quantity reads 0 before it is populated —
  propagates NaN straight into the block managing the live conditional order. Whether ADL's
  attach sequence can actually produce that ordering is **[U]** and not answerable from the
  file. Treat it as the reason the format spec says *"if your design divides, you need
  IsNumber more than this corpus suggests"*.
- **No bounds.** No `Number` blocks exist at all, so there is nothing to bound — but equally
  no in-graph input validation of the kind `Market Base` and the theo algos carry.
- **No `MarketState`, no `Pnl`, no `PositionRisk`, no position cap.** Exposure is bounded only
  by the size of the order the operator attached. Acceptable for an OMA that can only ever
  release quantity already sitting in an order; **[I]** not acceptable as a template for
  anything that creates its own quantity.
- **`ignoreMarketState: false`** — the algo auto-pauses outside session
  ([algo-types](../../adl-kb/guides/algo-types.md)). Given the loop-back through `State0`,
  what a mid-loop pause does to the watermark is **[U]**.

## Reuse

**[V]** No `Group` blocks, so `patterns.py` offers nothing here and there is nothing to
`--extract`. Reuse is by **hand-copying blocks**, which for a file this small is realistic —
and reminting GUIDs is mandatory even so (571 of 3,011 corpus GUIDs are shared across files).

Worth taking:

| Take | Blocks | Why |
|---|---|---|
| **Watermark release loop** | `Funnel` + `State` + `Sequence` + `ValueExtractor` + `DiscreteOrder` | drains a monotone target one increment at a time; not documented in adl-kb; the most portable idea in the file |
| **Suspended-order replacement** | `Branch{isSuspended}` + `Sequence` + `DiscreteOrder(clone)` + SOC-with-static-TRUE-delete | the general "swap an order without a gap" move |
| **Settle-then-stop** | `Branch{workingQuantity}==0` + `Stopwatch(25)` + `Terminal` | shutdown that lets in-flight pathways finish; add an `Alert` |
| **Jump-per-value naming** | `Conditional:orderQuantity`, `Primary:orderQuantity` | `<source>:<field>` naming makes a jump mesh readable; the big algos use the same convention |

Not worth taking without rework: the arithmetic chain, until the `Subtract` operand order is
settled in the Designer; and the whole file as a starting point, since with no `variables` it
has no place to put your parameters.

## Jump inventory

**[V]** 7 jumps, 9 landings, no dead jumps. Every name is `<producer>:<field>` or a bare value
name:

| Name | Source | Consumers |
|---|---|---|
| `ConditionalOrder` | `ConditionalOrder` (ExistingOrder) | `SingleOrderContainer2`, `Funnel0` |
| `Conditional:orderQuantity` | `Conditional` (MsgInfoExtractor) | `Ratio`, `HeldQty` |
| `Conditional:instrument` | `Conditional` (MsgInfoExtractor) | `DiscreteOrder0~8e027201` |
| `Primary:orderQuantity` | `Primary` (MsgInfoExtractor) | `Ratio` |
| `HeldQty` | `HeldQty` (Subtract) | `SingleOrderContainer2` |
| `Ratio` | `Ratio` (Divide) | `CounterFills` |
| `Rounded:result1` | `Rounded` (Math) | `HeldQty` |

**[V]** Note that a `Jump` here also has a **real inbound edge** from its source block, *in
addition to* the `sourceBlock` property. Both encodings are present at once. A tool that reads
only edges still sees the producer side of every wormhole in this file; it is the *landing*
side that is invisible without reading properties (format spec §3a).

## Related

Compare with [oco.md](oco.md) and [oco-2.md](oco-2.md) — the other two small OMA-shaped algos,
which solve order-linking rather than order-release. For the same shutdown idiom at production
scale with the `Alert` this file omits, see [market-base.md](market-base.md).

**Cited from:** [minvol.md](minvol.md) and [oco-2.md](oco-2.md) for the suspended-order swap ·
[with-a-tick.md](with-a-tick.md) for the `onExtMod` surrender stance and the second
operand-order contradiction · [tt-sniper.md](tt-sniper.md) and
[tt-multi-level-bracket.md](tt-multi-level-bracket.md) for the silent-shutdown gap and the
per-role `onExtMod` rule.
