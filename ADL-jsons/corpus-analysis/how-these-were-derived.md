# How the corpus-analysis docs were derived

One `.md` per file in [`../corpus/`](../corpus/), 13 in all. Each answers the same three
questions in the same order: **how the file is encoded**, **how the algo works**, and
**what of it you can lift into your own algo and at what cost**.

Read this once before trusting a number in any of them.

## Where the numbers come from

Every count, name, port, formula and edge in these docs is printed by one script:

```bash
cd ADL-jsons
python tools/profile_algo.py                 # one line per corpus file
python tools/profile_algo.py Conditional     # the full profile behind that file's doc
python tools/profile_algo.py Conditional --json
```

`profile_algo.py` recurses into `Group.internalAlgo.content` (a flat scan sees ~⅓ of a real
algo), resolves `Jump`/`JumpLanding` wormholes back to their real endpoints, resolves formula
GUID references to block labels, and reuses `patterns.py`'s GREEN/AMBER/RED tiering so a
reuse verdict here matches `patterns.py --show`. Nothing in these docs was read off the raw
JSON by eye. **If a doc disagrees with the script, the script is right and the doc is stale.**

Cross-check: the true-block counts agree with §2 of
[`../ADL-JSON-Format-Spec.md`](../ADL-JSON-Format-Spec.md) for all five files listed there
(682 / 669 / 659 / 622 / 43). The subgraph counts differ by one because the spec counts the
root graph and `profile_algo.py` does not.

## Confidence tags, kept honest

Same scheme as the format spec: **[V]** verified from the file, **[I]** inferred,
**[U]** unknown. In these docs the split falls out of the source almost mechanically:

- **[V]** — anything the file states: block types and counts, custom labels, property values,
  which block an edge joins to which, `variables`/`exports`, formula strings, Group ports.
- **[I]** — anything about *purpose*. "This Stopwatch is a settle-delay before the Terminal"
  is a reading of a wiring diagram, not a fact in the file. Behaviour claims are cited to a
  page under [`../../adl-kb/guides/`](../../adl-kb/guides/); where adl-kb is silent, the doc
  says so rather than filling the gap.
- **[U]** — three things recur and are called out wherever they matter:

  1. **Port index → meaning.** The file stores only connector GUIDs; ADL never writes a port
     label. `profile_algo.py` renders a port as its *position* in `block-catalog.json`'s
     connector list for that type (`in0`, `out2`). That position is an artefact of how the
     catalog was built — it is **not** documented operand order. So `Subtract in0 - in1` is
     an assumption, never a finding. Where operand order changes the meaning, the doc says
     which reading it took and why.
  2. **Firing order of a `Sequence`.** `out1` is not necessarily "#1". adl-kb documents that
     Sequence fires its outputs in order and waits for each pathway to finish
     ([block-catalog](../../adl-kb/guides/block-catalog.md)); the file does not record which
     GUID is which numbered output.
  3. **Whether any of this imports.** Nothing has been round-tripped through ADL — see
     [OPEN-QUESTIONS Q1](../../OPEN-QUESTIONS.md). Every transplant recommendation in these
     docs inherits that caveat and none of them repeat it.

## Two conventions the docs rely on, established from TT's own labels

Both are read off custom block names rather than out of any schema, and both are used
throughout without re-arguing them.

**`Branch` `out0` is FALSE/"no", `out1` is TRUE/"yes".** The catalog records two output
connector GUIDs for `Branch` and no indication of which is which. TT's jump names settle it:
in `MinVol.adl.json` the jump hanging off `out0` of the `IsSuspended?` Branch is named
**`IsSuspended?:no`**, the jump off `out0` of `External Delete?` is **`External Delete?:no`**,
and the jump off `out1` of `IsFirstRun` is **`IsFirstRun:yes`**. Three independent instances in
one file, all consistent. This is stronger than an inference but weaker than a schema, so it is
carried as **[V] for those blocks** and **[I] when applied to a Branch TT did not label**.

**Jump names follow `<producerBlock>:<outputName>`.** `Conditional:orderQuantity`,
`Order:instrument`, `SOC:workingQuantity`, `Group0:TooLittleVol`, `NewOrder:output_1`,
`Sequence0:output_3`, `SynthStop:Delete`. Groups stand in as producers, using their port name.
In a language where 41% of blocks are routing (format spec §6), the jump name **is** the wire
label — which is why every doc lists them, and why `profile_algo.py` resolves each one back to
its real source and consumers.

## How "dead jump" is counted

Each doc lists its file's jumps and flags the dead ones. **A jump is called dead here when its
`targetBlock` property resolves to no landing at all** — either the property is absent or it is
an empty list. By that definition 76 jumps are dead across the corpus, and only
`Conditional.adl.json` and `OCO 2.adl.json` have none.

The format spec's §1 `_invariants` figure of **6** counts something narrower — jumps where
`targetBlock` is *absent*, not those where it is present but empty. Both numbers are correct
about their own question; the docs use the wider one because a jump with an empty target list
is just as inert as one with no property. `python tools/extract_schema.py` prints the narrow
count; `python tools/profile_algo.py <file>` prints the wide one, per jump name.

## How to read the reuse sections

Groups are tiered exactly as `patterns.py` tiers them:

| Tier | Cost of adopting it |
|---|---|
| **GREEN** | wire its declared ports, done |
| **AMBER** | also feed every inbound `Jump` **by name** — jumps cross group boundaries, so the Group silently expects data that no port declares |
| **RED** | a formula inside points at a block outside; those references dangle the moment you extract it, and only formula surgery fixes them — which §4 of the format spec says not to attempt by hand |

Extract with `python tools/patterns.py --extract "<name>" -o part.json`, which remints every
instance GUID. Then `python tools/validate.py part.json`.

## Shared parts are analysed once

Six Groups are byte-identical across four algos each — `Alerts`, `Mkt Price`,
`CalculatedOrder`, `PriceOrQtyChanged`, `DESIRED_QTY`, `InsideMarket`. Each is analysed in
**one** doc and cross-linked from the other three, so the analysis cannot drift between
copies. The docs say which file owns each analysis.

## Filenames

Two corpus basenames carry stray whitespace — `TT Multi-Level Bracket  .adl.json` (double
space) and `TT Sniper .adl.json` (trailing space). The `.md` names are normalised; every doc
prints its exact source basename in the first line of its **Source** table, so the mapping
stays unambiguous in both directions.
