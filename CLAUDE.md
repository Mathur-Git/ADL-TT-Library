# CLAUDE.md

Operating manual for this repo. Read this first; it says where the truth lives and how
to work here.

## Start every session with one command

```bash
cd ADL-jsons && python tools/brief.py
```

That prints the repo shape, the active projects and their blockers, the open questions,
the corpus census, and a **routing table mapping each kind of question to the one file
that answers it** - in ~4 KB. Run it *before* any `ls`, `find`, `grep`, or `cat` of
`README.md` / `INDEX.md` / `OPEN-QUESTIONS.md` / `PROJECT.md`.

**Do not survey speculatively.** Re-deriving this repo's shape from the filesystem was
measured across 23 sessions at roughly a quarter of all shell output, spent rediscovering
facts that had not changed since the last session. There is no "let me get oriented
first" step beyond `brief.py`. Wait until you know the actual question, then open the
one artifact the routing table names.

## What this is

A workbench for designing **TT ADL** (Trading Technologies Algo Design Lab) algos and
turning them into importable `.adl.json` files. ADL is a block-and-wire visual language,
not a text one: you place blocks on a canvas, connect ports, and deploy to TT's Algo
Server.

It is **not a software project**. There is no app, no build, no dependency tree. It is
three things: two offline documentation mirrors, a corpus of real algo files with tools
that reverse-engineer them, and a workspace for the algos being built.

The user is a discretionary trader building their own systematic strategies. Treat their
market reasoning as domain expertise; treat ADL platform constraints as the thing they
are relying on this repo to get right.

## Ground rules

**Never answer an ADL question from model priors.** ADL is niche and pretrained
knowledge of it is unreliable and confabulation-prone. Every claim about a block, a
limit, or a behaviour comes from a file in this repo, and you cite the file. If it is
not in the KB and not in the corpus, say so rather than filling the gap.

**Source-of-truth precedence:**

| Question | Authority |
|---|---|
| How ADL *behaves* at runtime | `adl-kb/guides/` then `adl-kb/reference/` |
| How a `.adl.json` is *encoded* | `ADL-jsons/ADL-JSON-Format-Spec.md` + `block-catalog.json` |
| How the TT *platform* works (spreads, order types, depth, dashboards) | `trade-kb/` |
| What TT's own algos actually *do* in practice | the 13 corpus files, via the tools |

When behaviour docs and file-format findings disagree, **adl-kb wins on behaviour, the
corpus wins on encoding**. They describe different layers and are both right about their
own. The clearest example: `formula-reference.md` documents `@BlockName` / `#FieldName`,
which is correct for the *Formula Editor UI*; the *file on disk* stores
`[blockGuid.connectorGuid]` and `{fieldName}`.

**Carry the confidence tags.** The format spec tags every claim `[V]` verified /
`[I]` inferred / `[U]` unknown. Preserve that distinction when you repeat a claim.
Do not launder an `[I]` into a fact.

**Judge a block's existence by `defName`, never by a KB page title.** They differ - the
KB's "Bool block" is `defName: "Boolean"`. Check with `lookup.py` before concluding
anything is missing.

## Repo map

```
adl-kb/       ADL docs, 128 pages mirrored + 6 authored guides. START: guides/core-semantics.md
trade-kb/     TT platform docs, 594 pages mirrored + 7 authored guides
ADL-jsons/    the format spec + generated block-catalog.json
  corpus/       the 13 TT algo exports - pristine, never edit in place
  corpus-analysis/  one doc per corpus algo: how it works, its stop gaps, what to lift
  tools/        the reverse-engineering toolchain (run from ADL-jsons/)
projects/     one folder per algo being built; PROJECT.md is the durable record (gitignored)
OPEN-QUESTIONS.md   what is still unverified and how to settle it - check before promising anything
```

## The toolchain

Scripts in `ADL-jsons/tools/`, all sharing `adlkit.py` so the format quirks are
implemented once. They find the corpus and the catalog by their own location, so they
work from any cwd; the paths below assume you `cd ADL-jsons` first. Run them instead of
reading the JSON directly - the corpus is 8 MB and `block-catalog.json` alone is 375 KB.

```bash
python tools/brief.py                   # SESSION START: shape, projects, routing table
python tools/brief.py --routing         # just the question -> artifact table

python tools/q.py props MinVol Number Field   # block properties in one algo, cosmetics stripped
python tools/q.py props MinVol                # no types -> census, then pick
python tools/q.py grep throttle               # regex over names, formulas, notes, all 13
python tools/q.py notes Conditional           # TT's verbatim Note-block commentary
python tools/q.py block MinVol "Min Qty"      # one block + its edges and jump links

python tools/lookup.py                  # every block type, by frequency
python tools/lookup.py Stopwatch        # defId, connector GUIDs, observed properties
python tools/lookup.py --names Terminal # TT's own labels on that block = design intent
python tools/lookup.py --missing        # documented blocks the corpus cannot give you

python tools/patterns.py                # reusable Groups from TT's algos, by adoption cost
python tools/patterns.py --search throttle
python tools/patterns.py --show "Mkt Price"
python tools/patterns.py --show "Group0" --from MinVol        # TT reused 'Group0' 12 times
python tools/patterns.py --extract "SynthStop" --from BrackeTT -o part.json  # GUID-reminted

# --from <file substring> disambiguates; --extract REFUSES an ambiguous name rather than
# guessing. --guid <prefix> is the fallback when one file has several same-named Groups.

python tools/validate.py                # self-test against the 13 known-good algos
python tools/validate.py mine.adl.json  # check a file you built
python tools/validate.py --explain C7   # what a check means and why it matters

python tools/profile_algo.py            # one line per corpus file
python tools/profile_algo.py MinVol --brief   # reuse decision only, ~1 KB (PREFER THIS)
python tools/profile_algo.py MinVol     # full structural profile, ~15 KB
python tools/profile_algo.py MinVol --json

python tools/extract_schema.py          # rebuild the catalog after adding a new export
python tools/test_validate.py           # fault injection - proves the validator bites
```

`profile_algo.py` is the inverse of `lookup.py`: lookup asks "what does block type X look like
across the corpus", profile asks "what is inside THIS algo, and what can I lift". It prints
the operator surface, graph tree, per-file census, resolved edges and jump wormholes, order
properties, the safety layer and a per-Group reuse verdict. It is the script behind every
number in `ADL-jsons/corpus-analysis/` - one prose doc per corpus algo, explaining how each
one is built, what it does, where its stop gaps are, and which parts are worth copying. Start
there when you want a part rather than a fact.

**Before trusting any generated or edited file, run `validate.py` on it.** It enforces
14 structural invariants, self-tests clean on all 13 TT algos, and catches 18 injected
fault classes. It cannot tell you the design is correct, and it cannot promise ADL will
import the file.

### Reading discipline

Shell output is the dominant token cost in this repo - about 865 KB across 23 sessions,
nearly all of it re-derivation. Four rules, each aimed at a measured leak:

- **Never `cat` a KB or corpus-analysis file.** They run 100-400 lines; one `cat` of two
  guides cost 25 KB in a single call. Use `Read` with `offset`/`limit`, or `Grep` for the
  claim you actually need. `cat` is fine for something you already know is short.
- **Read `corpus-analysis/<algo>.md` before running `profile_algo.py`.** The prose doc was
  generated *from* the profiler and answers most questions about that algo. If you do need
  the profiler, start with `--brief` (~1 KB); the full profile is ~15 KB and mostly answers
  questions you did not ask.
- **Never hand-write a `python -c` script against `adlkit`.** 28 of them were written across
  23 sessions and 26 were the same query - that query is now `q.py props`. An inline script
  also tends to forget `walk_graphs`, and a flat scan silently misses two thirds of a real
  algo. If `q.py` genuinely cannot express the query, add a subcommand rather than inlining.
- **Say which file you are opening and why, before opening it.** If you cannot name the
  question, you are surveying, and the answer is `brief.py --routing` instead.

## Verified structural facts

These are `[V]`, re-checked on every `extract_schema.py` run (see `_invariants` in the
catalog - all must stay 0).

- `content` is **recursive**; Groups nest subgraphs up to 3 deep. A flat scan sees ~⅓ of
  a real algo. Always recurse.
- Block GUIDs are unique **within** a file but **not across** files - 571 of 3,011 are
  shared between TT algos. **Always remint GUIDs when copying anything.**
- Edges **never** cross a graph boundary (0 of 4,364). Cross-boundary data moves by
  `Connector` (through a Group port) or by `Jump`.
- `defId` and connector GUIDs are **globally stable per block type**. This is what makes
  generation feasible: connector GUIDs appear only inside edges, so the catalog is the
  only way to know how to wire a new block.
- **`Jump`/`JumpLanding` is a property-linked wormhole, not an edge** - and 41% of all
  blocks. `Jump.sourceBlock`/`.sourceConnector` name the real upstream,
  `Jump.targetBlock` is a **list** of landing GUIDs, each landing back-points via its own
  `sourceBlock`, and `generic` carries the port type as `{connectorGuid: type}`.
- A **Group port GUID must agree in three places**: the parent's `connectors` property,
  a `Connector` block inside whose own `guid` *is* that GUID, and that Connector's
  `definition` property. This is the most common way a hand-built Group breaks.
- Group port types are `message`, `real`, `bool`, `string`, `generic`.
- A property entry may have **no `value` key at all** (1,104 occurrences). Always `.get`.
- Formulas routinely reference blocks in **another graph**. Normal for TT; it is also
  exactly what makes a subgraph non-transplantable.

## Building an algo: the path

**1. Interrogate the idea.** Push back on the thesis before touching blocks. Cheapest
stage to kill a bad idea.

**2. Validate the signal - outside ADL.** ADL has **no backtester**. Analytics is capped
at 1-minute bars and does not run in UAT or Production-Delayed. If an edge needs proof,
it gets proven on tick data elsewhere. Do not let "we'll see in sim" stand in for this.

**3. Design the block architecture** against `adl-kb/guides/`, respecting the limits
below. Check `patterns.py` first - the problem may already be solved in a TT algo.

**4. Produce the file.** In strict order of preference:
   1. **Transplant** a Group via `patterns.py --extract`. Safest: every byte except the
      GUIDs was written by ADL, including `formulaNodes` ASTs you must not hand-author.
      TT reuses its own Groups this way across four of its algos.
   2. **Modify an export** - open the closest TT algo, change wired `Number` values, add
      plain blocks.
   3. **Synthesize from scratch** - most assumptions stacked, most risk.

**5. Validate, then round-trip.** `validate.py`, then actually import it into ADL and
read the values back. Then simulation. Never live off an untested file.

## Hard limits that bind designs

From `adl-kb/guides/gotchas-and-limits.md`, which has the full table and sources.

| Limit | Value |
|---|---|
| Stopwatch minimum timer | **25 ms** |
| Generator `TimeInterval` minimum | **100 ms** |
| Field block `Index` lookup depth | **20** |
| Analytics blocks per algo / bars / interval | **5** / 250 / 1–1440 min |
| Order messages/sec (test envs) | **200** - exceeding it **stops the algo** |
| `userField` slots per message | **4** |

Environment traps: **Analytics works only in Production-Live and Production-Simulation**
- not UAT, not Production-Delayed. Position Reserve needs a dedicated Algo Server.
Autospreader/Aggregator algos **fail to recover after a server restart**.

## Execution rules that cause the most bugs

Full list in `adl-kb/ADL-KB-Home.md`; these four cause the most damage:

1. **Continuous vs discrete** is the central distinction and decides which blocks are
   legal. While a discrete message propagates, **all continuous data freezes** - that is
   what makes a fill-time snapshot coherent.
2. **Never fan out a discrete output.** Order is non-deterministic; use a `Sequence`.
3. **`NaN` deletes working orders.** Guard every division and depth lookup with
   `IsNumber`. TT's own algos guard sparingly because they rarely divide - if your design
   divides or reads depth, you need it more than the corpus suggests.
4. **Never encode sequencing as a latency assumption.** TT re-optimises continuously.

## House idioms worth copying

Lifted from TT's own custom block names (`lookup.py --names <Block>`):

- **One condition drives both an `Alert` and a `Terminal`** - tell the human *and* stop
  the algo. Softer conditions get Alert only.
- **Throttles are split per side and per action** - `Quote Throttle (Bid)`,
  `Delete Throttle (Ask)` - never one global governor. A block literally named `Min 25ms`
  enforces the Stopwatch floor in production.
- **Buy and sell tracked separately, netted downstream** - not one signed counter.
- **External interference is first-class state** - `Buy ext deletes` counts what humans
  did, paired with `onExtMod` (`Ignore` vs `StopManaging`).
- **Every risky behaviour is a named operator-visible toggle**, not a hardcoded branch.
- **`Epsilon` as a real parameter** - float comparisons get an explicit tolerance, never
  `==`.
- **Bounds on safety-relevant parameters** (`minValue`/`maxValue` on `Number`), *and*
  in-graph validation, because bounds cannot express cross-parameter rules. Belt and
  braces.

## Conventions

- **`projects/<name>/PROJECT.md` is the durable record.** Chat memory is not. Update it
  when a decision is made, and keep `projects/INDEX.md` in step. Copy
  `projects/_TEMPLATE/PROJECT.md` to start.
- **`projects/` is gitignored - the whole directory, no exceptions** (since 2026-08-04;
  the `_TEMPLATE` carve-out was removed 2026-08-11 and the scaffold no longer survives a
  clone). **The GitHub remote is PUBLIC**, and `projects/` holds trading theses, strategy
  economics and desk knowledge - none of it belongs there. "Durable" therefore means
  *durable against losing chat context* - **not** version-controlled and not backed up off
  this machine. Back it up to a **private** remote or a synced folder instead. There is no
  history to recover a PROJECT.md from and no `git checkout` to undo a bad edit, so
  rewrite one in place with the same care as an untracked file. Anything that must
  outlive the machine needs its own backup.
- **Convert relative dates to absolute** in anything written to disk.
- Windows + PowerShell primary; a Bash tool is available for POSIX scripts. Script
  output goes through a cp1252 console - keep `print()` ASCII-only.
- Don't commit unless asked.
- The corpus files in `ADL-jsons/corpus/` are TT-published reference material.
  **Never edit them in place** - copy first. They are the ground truth the whole
  toolchain is derived from and the self-test depends on them being pristine.
