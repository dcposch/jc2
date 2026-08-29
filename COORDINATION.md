# COORDINATION.md — the campaign protocol

This file owns the campaign's live operating policy. It is model-agnostic:
any sufficiently capable model can fill any role below. Avenue inventory and
ranking belong in `APPROACHES.md`; the detailed Keller-to-book / `G2-PSC` /
`G2-BD` dependency map belongs in `ladder/REDUCTION.md`; claim-level evidence
belongs in `AUDIT.md`. None is duplicated here.

## Mission and decision rule

Resolve the plane Jacobian conjecture, by proof or counterexample, as quickly
as sound research permits. Urgency changes scheduling, not standards. Review
gates promotion, publication, expensive commitment, and irreversible action;
it does not normally block cheap, reversible research based on a result that
has passed the provisional gate below.

The coordinator may take routine, reversible actions within the campaign.
External communication, publication, destructive operations, disclosure of a
private result, and newly expensive commitments remain human decisions unless
the human has granted standing authority for the exact action.

## Canonical files and write ownership

The six top-level Markdown files have disjoint jobs:

- `README.md` — short project orientation and public-progress pointer.
- `COORDINATION.md` — live process, roles, gates, clocks, and bootstrap.
- `APPROACHES.md` — canonical avenue inventory and comparative ranking:
  routes, gaps, promise, and tried/untried status.
- `AUDIT.md` — promoted-claim and trust-boundary ledger, including
  corrections. Promotion requires the review rule below.
- `PROGRESS.md` — one compact digest per calendar day, newest first.
- `notes.md` — append-oriented tick log and active-state journal.

The newest `LIVE STATE` block in `notes.md` is authoritative for lanes, holds,
provisional claims, review debt, clocks, and the immediate queue. `xmodel/`
holds immutable producer, reviewer, sweep, and round reports; code and replay
artifacts live beside the relevant cases. `ops/FLEET.md` owns machine inventory
and compute safety rules.

Do not maintain a second live queue, avenue map, or evidence ledger. Link to
the canonical entry instead of copying it. When a digest must repeat a fact,
label its date and evidence/lifecycle state; later corrections supersede but do
not erase the historical record.

## Roles

Exactly one coordinator is active. A handoff becomes effective only after the
outgoing coordinator banks an atomic `LIVE STATE` and the incoming coordinator
acknowledges its basis; research and review lanes may otherwise remain active.

- **Coordinator / integrator** — owns the scientific schedule and global
  synthesis. It freezes round inputs, keeps the claim and avenue dependencies
  legible, allocates capacity, adjudicates conflicting reports, attacks the
  hardest integrative gap, banks state, and surfaces human-only decisions. The
  strongest available reasoner should spend most of its time here or on the
  one problem for which global context has the highest marginal value, not on
  routine replay or documentation.
- **Research lane** — one bounded prove, disprove, compute, implement, or
  survey task. It names its input claims and permitted assumptions, owns its
  task end-to-end, and writes one `xmodel/<tag>.md` report plus replayable
  artifacts when applicable. It does not edit shared ledgers.
- **Adversarial reviewer** — independently tries to break one claim by source
  comparison, counterexample search, and direct replay. It reports a verdict
  for each exact claim: `CONFIRMED`, `REFUTED`, or `GAP`, with the attack and
  computation shown. It must not be the producer model.
- **External-intelligence lane** — searches broadly for new results, actors,
  artifacts, corrections, and priority changes; snapshots exact sources and
  maps actionable items into campaign claims and avenues.
- **Software / compute lane** — improves instruments or runs registered
  experiments. New tools carry an internal/unreviewed label until their gates
  and any claim they support are independently reviewed.

Persistent avenue owners preserve depth. At every ideation round, rotating
fresh-eyes lanes independently scan the whole campaign before receiving any
narrower lens.

## Two independent claim axes

Never conflate mathematical evidence with workflow maturity.

**Evidence tier** describes what the artifact proves, for example `EXACT`,
`PROVED`, `MOD-p`, `BOOK-RELATIVE`, `FORMAL`, `INTERNAL-UNREVIEWED`, or
`CONJECTURE`. Absence of a certificate means the lower tier. A computational
header or model verdict never upgrades the underlying artifact.

**Lifecycle state** describes scrutiny:

`DRAFT -> PRODUCER-CHECKED -> PROVISIONAL -> PROMOTED`

with exits to `QUARANTINED` or `REFUTED`. `PROVISIONAL` is not an evidence
tier and must never be presented as promoted truth.

A result may enter `PROVISIONAL` only when all of the following are recorded:

1. an exact statement and scope, with failed or excluded stronger readings;
   the ambient ring, quotient/localization/saturation order, and every
   specialization must be literal. A conclusion moved between rings must
   exhibit and audit the map; matching variable names are not a map;
2. explicit dependencies and provenance;
3. frozen source/artifact hashes and a replay command when computational;
4. producer-run attacks, sanity checks, and at least one meaningful negative
   control where the object admits one;
5. for a characteristic-`p`, Witt, or `p`-adic successor digit, the exact
   integer numerator, its divisibility on the charged predecessor scheme, and
   the reduced integer quotient are recorded before any reduction modulo `p`;
6. no known contradiction with the current ledgers.

## Promotion and adversarial review

1. **Different-model promotion.** No result enters `AUDIT.md` as promoted
   until a different model has performed hostile review. Self-review and two
   agents backed by the same producing model do not satisfy this rule.
2. **Recompute, do not defer.** Review the exact source statement, hypotheses,
   transcription, code, certificate, and conclusion as applicable. A second
   prose opinion is not a computational review.
   For a characteristic-`p`, Witt, or `p`-adic successor residual, independently
   reconstruct the integer quotient and compare its generated rows with the
   exact source identity on both a symbolic control and, where possible, an
   old-pass/new-fail negative control. A mod-`p` bracket calculation alone does
   not review a divided carry.
3. **Priority by exposure.** Review priority is proportional to
   `downstream fanout x centrality x fragility x rollback cost`. A claim that
   many active lanes consume outranks an isolated lemma of equal apparent
   importance.
4. **Latency targets.** Start review as soon as a claim becomes provisional.
   Aim to resolve high-fanout claims within six hours and ordinary claims by
   the next full ideation round. A miss is review debt, recorded in `LIVE
   STATE`; it is not silent permission to promote.
5. **Immutable review inputs.**  Give every background reviewer a frozen,
   hash-pinned claim packet (including the exact canonical excerpts it may
   need) and require it to review those bytes.  Do not make a long review
   depend on rereading mutable live ledgers, and do not freeze canonical
   promotion while that review runs.  Later ledger changes are queued for a
   delta review if they alter the charged claim; unrelated drift is not a
   custody failure.
6. **Fail closed.** `REFUTED` triggers immediate rollback. `GAP` preserves only
   the portion actually checked. Corrections are appended promptly to
   `notes.md`, the relevant canonical route/evidence file, and the current
   daily digest.

When the current reduction architecture is discussed, use the scoped names
`G2-PSC` (global packet/sheet transport and fidelity) and `G2-BD`
(post-residue-A bounded delay), never bare `G2`. The detailed dependency map
is `ladder/REDUCTION.md`; summaries elsewhere must preserve its arrow
directions and scope.

## Speculative parallelism and rollback

Review runs in the background. Once a claim is provisional, cheap and
reversible dependent exploration may begin under a visible speculative
budget:

- at most two child lanes and one unreviewed dependency generation per
  provisional claim;
- at most four active provisional roots campaign-wide;
- normally no more than 25% of active research capacity may depend on any one
  unreviewed claim;
- enqueue hostile review before launching the first dependent child; a missed
  review deadline freezes new descendants but not unrelated work;
- cap each speculative child at six hours unless the coordinator records a
  reasoned exception;
- publication, promotion, irreversible action, expensive fleet campaigns, and
  further fanout must not rely on an unreviewed claim;
- every dependent report labels the assumption `PROVISIONAL`, so descendants
  can be found and rolled back mechanically.

The coordinator maintains a lightweight claim DAG in the newest `LIVE STATE`
block: claim ID, exact scope, evidence tier, lifecycle, parents, owner,
reviewer, artifact hashes, descendants, and stop condition. If a premise is
refuted or narrowed, quarantine its descendants immediately, retain them as
conditional work when useful, and re-root any result whose proof did not
actually need the failed premise.

For each load-bearing bridge, prefer three concurrent attacks when useful and
affordable: prove it, falsify it on the cheapest honest model, and bypass it by
redesigning the route. A negative result closes only its registered scope.

## The continuous outer loop

Cadences below are maximum quiet intervals, never reasons to wait. Any event
may interrupt the current allocation; unrelated work continues.

### Event triggers and micro-rounds

Run an immediate strategy update when any of these occurs:

- a decisive lane confirms, refutes, gaps, caps, or times out;
- a new mathematical object, theorem, countermodel, certificate, or materially
  faster instrument is banked;
- review changes a claim's scope or lifecycle;
- an external result or actor changes correctness, route rank, priority,
  publication posture, available artifacts, or competitive status;
- the active portfolio is stalled, duplicated, or exposed to one fragile
  premise beyond the limits above;
- campaign machinery loses or delays state, duplicates work, misroutes a
  model or compute job, exposes mutable inputs, materially inflates context or
  cost, or reports fleet/lane state unreliably.  Treat this as a bounded
  systems micro-round unless it also changes the mathematical ranking.

A targeted response to a routine local event is a **micro-round**: triage the
delta, launch or stop bounded work, and bank it without forcing every ideator
to rescan all avenues. It does not reset the 12-hour clock. A credible external
proof/counterexample, a load-bearing review reversal, or any non-echo change to
the promoted ledger is critical and starts a full round immediately, subject
to the coalescing rule below. Other events start a full round when they
materially change the global ranking; otherwise they receive a micro-round.

Coalesce echo events to prevent review/round thrashing. If a sealed full-round
packet already states a provisional result's complete mathematical content and
the post-cutoff review merely confirms that same content and scope, harvest the
lifecycle promotion as a micro-round; it does not trigger an otherwise
identical full scan. A refutation or scope change of a **promoted or
load-bearing** claim, a new dependency on the critical path, or a materially
rank-changing review fact remains a critical trigger. An expected negative
first-gate result or correction to an unpromoted provisional formula may be
coalesced when the global ranking and trust perimeter are unchanged. Record
the coalescing decision explicitly in the next synthesis or `LIVE STATE`.

Every new provisional or promoted theorem also triggers a **theorem-interface
composition pass**.  Normalize it to object, hypotheses, field/ring, degree or
support bounds, and conclusion; search the claim DAG for results whose
conclusions discharge those hypotheses or whose hypotheses consume the new
conclusion; and test the cheapest exact pairings before treating the theorem
as an isolated endpoint.  Record a new bridge, a scope mismatch, or `NO HIT`.
This pass is bounded and does not interrupt unrelated work.  In particular,
compare proof-side degree/automorphy theorems with counterexample-side
integrality, specialization, compactness, and collision lemmas: their labels
may differ even when their theorem interfaces compose.

If a critical event arrives during an open full round and invalidates a
load-bearing snapshot assumption, mark that round `ABORTED` and reseal. If it
does not invalidate the packet, take any safe emergency action, finish the
sealed round, and start an immediate follow-on full round. Never mutate the
open snapshot in place.

### Full-spectrum ideation — at least every 12 hours

No more than 12 hours may pass between completed full rounds. A significant
event starts one sooner. Each round follows this protocol:

1. **Freeze a state packet.** Record UTC time, clean basis commit, newer local
   hashes if any, newest `LIVE STATE`, active/recent lane reports, review debt,
   current `APPROACHES.md`, load-bearing `AUDIT.md` corrections, and all new
   external evidence since the prior round.
2. **Blind independent scan.** Every active research agent is a core ideator by
   default and reads the whole avenue map, current gaps, and new evidence
   before seeing the other submissions. A noninterruptible compute or review
   worker may be omitted explicitly; mark the round degraded if this leaves
   inadequate coverage. A rotating specialist lens may be added only after
   the common scan. Model diversity is preferred; duplicate instances still
   think independently.
   **Every model marked as an equal-standing whole-portfolio researcher in the
   roster** is invited automatically to every full round.  Each receives the
   same sealed packet, submission contract, tool boundary, and deadline, and
   must submit before seeing any other lane's report.  Every submission
   receives equal post-deduplication consideration: model identity is neither
   a bonus nor a vote, and operational unavailability degrades but does not
   block the round.
3. **Required submission contract.** Each report gives:
   - a compact disposition vector over every numbered avenue: `unchanged`,
     `raise`, `lower`, or `reopen`, with reasons for every change;
   - a reranking of the principal proof and disproof bottlenecks;
   - at least one genuinely new avenue or mechanism;
   - at least one new connection between existing avenues;
   - the strongest proof attack and strongest counterexample/falsification
     attack;
   - one software acceleration or decisive experiment;
   - a short campaign-systems check, independent of the mathematical software
     proposal: either an `UPGRADE` card with the smallest useful test or
     implementation, or `NO_CHANGE` with evidence.  Rotate across state
     freshness, context and retrieval cost, claim/review propagation,
     duplication, model routing and utilization, adapter reliability, AWS
     scheduling and cost, reproducibility, and operator/chat-summary quality;
   - no more than three detailed idea cards, each with explicit dependencies,
     cheapest discriminator, interpretation of each outcome, stop condition,
     and expected information gain;
   - a `continue / redesign / stop` recommendation for current major lanes.
4. **Deduplicate after collection.** Fingerprint ideas by target obstruction,
   mechanism, object, and decisive test. Merge operational duplicates while
   preserving independent votes, disagreements, and genuinely different proof
   mechanisms. Shared wording is not independent support.
5. **Cross-pollinate adversarially.** Only after blind collection, ask lanes to
   combine compatible ideas, expose shared hidden assumptions, attack the
   strongest proposal, and design the cheapest experiment that separates the
   leading choices.
6. **Run the canonical history/priority checksum.** Before compute, search
   `AUDIT.md`, `APPROACHES.md`, `PROGRESS.md`, the newest `LIVE STATE`,
   `ladder/REDUCTION.md`, and repository reports for every surviving target,
   mechanism, and close synonym. Reconcile the master known-degree/closed-case
   ledgers, then check each load-bearing literature claim in primary text.
   Label every card `NEW`, `KNOWN`, `DUPLICATE`, or `SCOPE-CONFLICT` in the
   synthesis. Blind consensus never overrides a banked exact result or primary
   theorem; a shared stale packet premise is correlated error, not a vote.
7. **Synthesize and launch.** The coordinator writes a ranked synthesis,
   updates the avenue/claim graphs if needed, assigns owners and reviewers,
   launches reversible lanes immediately, and records why alternatives were
   deferred or stopped.  Deduplicate the systems checks, choose at most one
   highest-value bounded upgrade for immediate work, and track it only in the
   canonical `LIVE STATE` queue.  Trial at least one incremental machinery
   improvement in every rolling 48-hour window unless no candidate clears its
   measured benefit, regression-risk, and mathematical-opportunity-cost gate;
   record a reasoned `NO_UPGRADE` rather than changing machinery for its own
   sake.  Systems work runs beside, and normally does not block, live
   mathematical research.

Target 60 minutes for blind submissions, 30 for cross-pollination, and 30 for
synthesis. Close a round within two hours when possible; if an ideator misses
the close, mark the round `DEGRADED` instead of blocking ongoing research.
Events arriving after the snapshot are queued for the next micro/full round
and never silently mutate the sealed packet.

Round artifacts use
`xmodel/ideation-<YYYYMMDDTHHMMZ>-<lane>.md` and
`xmodel/ideation-<YYYYMMDDTHHMMZ>-synthesis.md`.

### External web sweep — at least every 24 hours

No more than 24 hours may pass between completed broad sweeps. Low-cost alerts
and known-actor watches run between sweeps when available. An external event
can trigger both immediate intake and a full ideation round.

The sweep covers broad phrase/concept searches as well as arXiv, repositories,
Zenodo, MathOverflow, Palomar and its public discussion channels, relevant
social feeds, citations, and the known-actor watchlist. Date-windowed searches
are supplemental, because old but newly discovered artifacts have already
escaped them.

Classify an item `ACTIONABLE` only if it can change correctness, route rank,
priority/publication posture, artifacts, or actor status. For each actionable
item: preserve URL and timestamp, snapshot or hash the artifact, extract the
exact claim without overreading it, replay the cheapest decisive check, map it
to the claim DAG and avenue graph, and assign follow-up. Bank a negative sweep
too; absence of a hit is weak evidence, not evidence of absence.

### Classical frontier admissibility gate

Before registering compute, every lane must state separately the actual total
degrees, partial-`y` degrees, weighted degrees, and whether any total/
coefficient-`x` cap is finite.  It must then reconcile that honest scope with
the classical closed-case ledger and primary sources.  In particular, the
Guccione--Guccione--Valqui/Heitmann theorem requires
`gcd(deg_total P,deg_total Q) >= 16` for a characteristic-zero
counterexample.  Thus every envelope with both total degrees at most `12`
and every explicitly registered fixed actual-total pair such as `(9,12)` or
`(8,12)` is counterexample-closed.  Historical `max12` and “maximum-12” tags
normally name a maximum actual partial-`y`-degree frontier; they never
establish a finite coefficient-`x` or total-degree cap.  Only an explicit
actual-total pair or total cap licenses `METHOD_CONTROL_ONLY`; an unbounded-
total partial-`y` lane remains `NOT_CLOSED_BY_THIS_GATE` unless another
theorem closes its exact scope.

For the mechanically covered cases, attach the deterministic output of
`ops/frontier_gate.py` to `REGISTRATION.md`.  A
`REFUSE_CLASSICALLY_CLOSED` verdict blocks frontier compute.  Such a lane may
run only after being relabelled `method-control`, with a named live client and
a strict cost/stop condition; its output cannot be advertised as advancing
the closed degree frontier.  `NOT_CLOSED_BY_THIS_GATE` means only that this
one theorem is inconclusive.  Unbounded-total partial-`y` work must say
`--total-unbounded` explicitly and still pass every other classical/history
check.  Any significant routing news reruns this gate across active lanes
before further capacity is allocated.

## Capacity allocation

Default portfolio targets, adjusted when evidence demands it:

- 35% strongest current critical path;
- 20% new avenues and cross-avenue connections;
- 20% adversarial review and replication;
- 15% mathematical software, formalization, decisive-experiment design, and
  bounded campaign-system improvement;
- 5% external intelligence;
- 5% state integration and publication readiness.

With four reasoning slots, the usual shape is: coordinator/integrator;
strongest current route; orthogonal new or disproof route; and
risk-prioritized review/rapid response. Use wider model fleets for blind idea
generation and independent review, and separate compute capacity from scarce
reasoning slots. Do not leave all slots exploring descendants of one premise.

Whenever provisional review debt exists, reserve at least one reasoning slot
or 25% of research capacity (whichever is practical) for review and
falsification. Two consecutive non-informative attempts on the same
representation force a redesign; a third requires written justification. Two
full rounds with unchanged leading gaps and no information gain trigger a
zero-base fresh-eyes reset for one cycle.

Choose work by expected information gain per unit time and cost, not by how
many agents or tokens it consumes. Track event-to-decisive-test time, review
latency/debt, central gaps resolved, provisional exposure and rollback cost,
new connections actually tested, and information gained per compute dollar.
For campaign machinery also track report-to-ingestion latency, stale or
missing state, context bytes per lane, duplicate work prevented, adapter and
job failure rates, model/fleet utilization, and time to a sealed replayable
certificate.  Retain an upgrade only when those measurements or mathematical
throughput improve without an offsetting reliability regression.

## Tick, banking, and live state

At each coordinator tick:

1. read the newest `LIVE STATE` and any events since it;
2. sweep local lanes and remote machines; verify exact process identities and
   stop idle paid capacity within standing authority;
3. rerun the classical frontier gate on new scopes or significant news;
4. harvest finished work, apply the provisional gate, and start hostile review
   immediately for promotable claims;
5. propagate review outcomes through the claim DAG without blocking unrelated
   work;
6. test the 12-hour ideation and 24-hour sweep deadlines and all event triggers;
7. rebalance the portfolio, launch the next bounded lanes, and assign a stop
   condition to each;
8. append findings, corrections, dead ends, costs, and decisions to `notes.md`,
   then append a fresh `LIVE STATE` block.

Before launch, check active tags, prior `xmodel/` reports, `AUDIT.md`, and
`APPROACHES.md`. One question/deliverable has one live owner unless a second
lane is explicitly registered as independent replication.

Use this compact block; append rather than editing an old one:

```text
## <UTC timestamp> LIVE STATE
- Basis: <commit and any explicitly dirty artifact hashes>
- Coordinator / ideators: <active coordinator; full-round research roster>
- Last full ideation: <UTC / round ID>; next deadline: <UTC>
- Last broad web sweep: <UTC / report>; next deadline: <UTC>
- Last system improvement/check: <UTC / result>; next 48-hour checkpoint: <UTC>
- Active lanes: <tag, owner, inputs, stop condition>
- Provisional claims: <ID, tier, parents, descendants, review>
- Review queue/debt: <priority and due time>
- Holds/human gates: <exact action and authority needed>
- Top gaps: <links into APPROACHES/REDUCTION/AUDIT>
- Immediate queue/triggers: <ranked bounded actions>
```

At the end of a calendar day, update that day's single `PROGRESS.md` entry.
Negative results and superseded plans remain in `notes.md`; they prevent the
campaign from paying twice for the same failed idea.

## Replayability and operational safety

- Computational claims ship engines, certificates, exact replay commands,
  versions, input hashes, seeds, host, UTC times, and meaningful negative
  controls. Mod-p work records every prime.
- A successor residual at digit `n` is typed only after an exact numerator `N`
  is proved divisible by `p^n` on the charged predecessor scheme and
  `N/p^n mod p` is derived with all lower-order divided carries retained. If
  the quotient is not integral on that scheme, or generated coefficient rows
  disagree with an exact determinant/source-identity reconstruction, the gate
  is `TYPE-FAIL` and must not be used downstream.
- msolve 0.10.1 characteristic-zero `-g` may return a first-machine-prime
  unit basis before rational reconstruction while printing a characteristic-0
  header. A char-0-header `[1]` is only first-prime trace evidence unless an
  independently checked exact rational certificate is present. See `AUDIT.md`.
- Run all heavy or uncertain-duration campaign computation on AWS, never on
  the local machine. This includes CAS/solver jobs, Lean builds, and long or
  potentially multi-GB exact-Python replays/enumerations. Reserve local
  execution for editing, orchestration, hashing, status checks, model-review
  adapters without compute tools, and genuinely short low-memory validation.
  Follow `ops/FLEET.md` for machine inventory, shipping, caps, telemetry, and
  kill safety.
- `jc2-lean` is a separately owned nested repository and is outside the
  campaign's inspection boundary. Campaign agents must not enter, enumerate,
  search, read, build, status, modify, or control it. Scope every parent Git
  query explicitly away from that path; never stage its gitlink. The parent
  `.ignore` excludes it from ripgrep-style broad searches. Concurrent local
  formalization may consume shared CPU/RAM, but campaign contention checks
  remain system-level and must not identify or inspect that nested workload.
- New heavy runners fail closed off AWS before importing a CAS or allocating
  large objects, require a registered AWS job tag, and record the remote
  hostname in custody.  New counterexample/frontier runners also record the
  classical admissibility verdict described above before launch.  A
  coordinator process-tree/swap-delta audit
  is part of each live-state checkpoint; allocated swap without new pageouts
  is historical occupancy, not by itself active thrashing.
- A process-group guard is valid only if its recorded group includes the
  actual CAS and every descendant whose RSS or lifetime it must control.
  Wrappers that create an unrecorded inner PGID (including GNU `timeout`
  without `--foreground`) are forbidden unless every inner group is itself
  recorded and validated.  Before a new or repaired heavy runner launches,
  a live no-CAS dummy regression must show that descendant RSS is included in
  telemetry and that namespace-validated TERM, then KILL if needed, leaves no
  nonzombie descendant or orphan; freeze that regression with the source.
- Third-party tools may mutate shared CLI configuration; adapters must isolate
  or sanitize it, and a new/updated adapter gets a smoke test before use.
- Lane launchers take prompt files, reject duplicate live tags, record their
  true exit status, and keep one task and deliverable path per tag.  Every
  model-review prompt names exactly one report path whose basename matches the
  lane tag, explicitly instructs the reviewer to write that file and no other,
  and is smoke-checked for that destination before launch.  Referee text left
  only in adapter stdout is a failed-delivery draft, not promotion evidence;
  preserve it and rerun through a fresh output-explicit prompt.
- `ops/lane.sh` appends the compact `FALLACY.md` reasoning guardrail exactly
  once from a hash-pinned private snapshot and records both the original and
  composed prompt hashes.  The appendix is semantic instruction, not a
  lexical proof checker.  Reports may declare an exact machine line
  `charge_basis={...}`; the validator checks its rational delta, branch,
  positive flag count, and citation.  Invalid declarations quarantine the
  lane, while an absent declaration is recorded as `ABSENT` and never
  interpreted as a mathematical pass.  Changes to the prompt, appendix,
  adapter, or validator during a run quarantine the result; focused launcher
  regression is required after any edit to this path.
- A campaign win requires a global proof or an explicit characteristic-zero
  counterexample at its honest evidence tier. Failure of selected formal
  families to algebraize, or closure within one book/chart/degree range, is
  not by itself a resolution of JC2.

## Bootstrap for a fresh coordinator

1. Read this file, then `README.md`, the newest `PROGRESS.md` entry, the
   canonical-correction/current-state sections of `AUDIT.md`, and all of
   `APPROACHES.md`.
2. Read `notes.md` from the bottom through the newest `LIVE STATE` and all
   later events. Historical `STRATEGY` and `STANDING QUEUE` blocks are
   provenance, not current policy.
3. Check the campaign repository's explicitly scoped status and basis commit,
   excluding `jc2-lean` without inspecting it. Sweep exact local lane tags and
   `ops/FLEET.md` machines; harvest before relaunching anything.
4. Resolve overdue review, ideation, and web-sweep clocks. Continue the outer
   loop. Never silently promote, publish, spend beyond authority, or discard
   another lane's work.

## Roster

This is the only operational adapter roster. Historical notes and artifact
provenance may name the producing or reviewing model.

| Model | Adapter | Notes |
|---|---|---|
| Fable 5 (Anthropic) | `ops/adapters/claude.sh` | exact-model pinned; permanent equal-standing whole-portfolio researcher; receives every sealed full-round packet independently; clean same-input ideation through `20260829T0820Z`; distinctive reviewed work includes theorem-interface/lifecycle auditing, compiler custody, K00 compression, the exact localized gate intertwiner, the uniform lower two-root endpoint theorem, the E0 exact-`p` linear-vacuity correction, the reviewed algebraic-primitive gate filter, the reviewed single-root endpoint-transport mechanism, the independent repair of the active-`c2` D8--D15 cascade, the normalization/localization repair of the q1/q3 composition, the clean 442-slot hostile review of raw origin coupling, the fixed origin-residue slice audit, the fixed-`Q=X` ideal-membership exclusion, and the literal active-`c2` D16--D22 audit; normal hostile review remains mandatory |
| Opus 5 (Anthropic) | `ops/adapters/opus.sh` | exact-model pinned; **permanently admitted as an equal-standing whole-portfolio researcher by the `20260827T2137Z` same-input evaluation**; clean same-input ideation through `20260829T0820Z`; distinctive reviewed work includes the etale-`mu4` torsor target-budget theorem, source-level `G2-PSC` same-edge/subsumption correction, all-row Lagrange and homogeneous `NU` laws, mod-8 row death, an exact rank-one nonlinear control, closed-form recurrence fixtures, the clean-room repair of unit-root endpoint transport, the repaired full-system q1/q3 deep-locus compression, the exact q5--q13/even-gate tail classification, the reviewed raw-origin/parity coupling with its exact `Q=X` mutation, the generic quadratic-Q fixed-face rank theorem, the promoted degree-432 `K0` field theorem, and the promoted asymptotic-complement covering mechanism; normal hostile review remains mandatory |
| GPT / "Sol" (OpenAI) | `ops/adapters/codex.sh` | coordinator and equal-standing whole-portfolio researcher; exact `gpt-5.6-sol` with `ultra` reasoning through the pinned adapter; clean same-input ideation through `20260829T0820Z` |
| Grok (xAI) | `ops/adapters/grok.sh` | equal-standing whole-portfolio researcher; via `grok --prompt-file`; clean same-input ideation through `20260829T0820Z`; its earlier `FACE-NC`/`FACE-CHAR` promotions failed hostile typing review; its 2259Z constant-bundle insight survived only after gauge repair and its Hessian formula proved visibility rather than an obstruction; it independently confirmed the row-30 nonlinear class slice, the promoted `K0` theorem, the ARITH-SPREAD correction, and the scoped asymptotic-complement theorems |

Temporary availability (2026-08-28 03:45Z): a fresh Fable5 launch returns
the provider's hard usage-limit response, with access advertised to resume
`2026-09-01 00:00Z`.  Preserve Fable's roster status, but route nonblocking
new reviews to another model until the adapter smoke test succeeds.  An
Opus5 task launched before the ceiling remains live; do not assume that this
licenses a fresh Anthropic launch.

Availability refresh (2026-08-28 06:30Z): a fresh exact-pinned Fable5 task
completed successfully through `ops/adapters/claude.sh`, including guarded
read-only shell metadata inspection.  The earlier hard ceiling has therefore
cleared in practice.  Restore Fable5 to normal equal-standing blind-round and
review launches; retain ordinary fallback if a later provider limit recurs.

Availability and allocation refresh (2026-08-28 23:20Z): one identical fresh
shell-capable smoke prompt passed through all four adapters: Fable 5, Opus 5,
exact `gpt-5.6-sol`, and Grok 4.6.  Evidence is
`xmodel/model-availability-smoke-20260828T2320Z.md`.  Earlier subscription
ceiling banners do not override a fresh successful adapter test; paid adapter
execution is currently usable.  In-product Codex collaboration subagents can
still hit a separate subscription window, so overflow is routed through the
working adapters rather than treated as model unavailability.

Sol coordinates and integrates but is not the default owner of all new
mathematics.  While at least two peer adapters are available, no more than
half of newly opened independent primary-research packets should default to
Sol; every significant-news/full ideation round continues to charge Fable,
Opus, and Grok independently, and between rounds each available peer receives
primary research as well as review work whenever the frontier decomposes.
Exceptions for a uniquely local context or an urgent serial dependency are
recorded in the live ledger.  Promotion still requires a different-model
hostile check; reviews run in the background and do not block provisional
descendants.

Availability and allocation refresh (2026-08-29 02:18Z): fresh paid-auth
Fable5 and Opus5 launches again reached their pinned models with shell tools,
and a fresh Grok 4.6 launch completed a hostile review before accepting a new
primary-research packet. Remaining provider quota is not exposed, so a later
limit banner is handled by rerouting, not by reducing permanent roster
standing. The live peer-majority allocation is Fable on LL-1, K0 R2 review,
and the Q+E5 two-pole repair; Opus on equal-join primary research and TRIPLE02 R2
review; Grok on an independent parametric Prop. 8.1(iv) solve. Sol coordinates,
integrates, and develops cross-lane deductions.

Allocation refresh (2026-08-29 02:47Z): peer models continue to own the
majority of active work. Fable independently reviews both parametric
Proposition 8.1 reports and repairs Q+E5, LL-1 R3, and TRIPLE02 R3; Opus
repairs K0 R3 and its completed equal-join report is under hostile review;
Grok independently reviews that semilinear report and attacks exact lambda.
Sol coordinates, replays, adjudicates, and maintains the cross-lane scope
firewall. The external pinned Fable/Opus/Grok adapters remain responsive;
only the separate in-product Codex collaboration pool is quota-blocked.

Availability and allocation refresh (2026-08-29 03:30Z): three fresh
paid-auth shell-capable calls succeeded with `ANTHROPIC_API_KEY` removed.
The default `claude` alias identified itself as `claude-fable-5`, the pinned
Fable call did likewise, and `--model opus` identified
`claude-opus-5`; all completed without quota or permission errors. Grok 4.6
also completed the clean rerun of the `20260829T0250Z` blind round and remains
live on primary and review work. The clean four-model synthesis is
`d2e34570...`/body `1bc47e35...`; the excluded first Grok submission remains
tainted and unused. Peer models own the mathematical frontier: Fable handles
Statement-3.9 coefficient transport, Grok handles U2, and Opus handles the
first-extra-jet/exact-lambda discriminator. Sol is coordinator/adjudicator.
Reviews and custody repairs run in the background and do not block provisional
descendants. Local model adapters showed no swap-in, swap-out, or pageout in
the sampled interval; all heavy or uncertain computation remains AWS-only.

Allocation refresh (2026-08-29 03:51Z): the fresh model checks have now been
converted into sustained peer ownership, not one-shot smoke tests. Fable runs
the td=8 Statement-3.9 transport primary, Q+E5 R3, U2 hostile review, Opus
exact-separation hostile review, and TRIPLE02 R4; Opus produced the td=8
exact-separation theorem and runs K0 R4, with further review work harvested as
lanes close; Grok produced the U2 reduction and now owns the distinct td=12 U1
trunk-consumer primary. Sol coordinates, verifies seals, integrates reviewed
residues, and assigns nonduplicate successors. New work continues on
reasonable provisional confidence while different-model reviews run in the
background. All current mathematical lanes are desk-scale; AWS remains
reserved for source-reviewed heavy jobs.

Allocation refresh (2026-08-29 07:24Z): the peer-majority wave has closed at
a quiescent checkpoint. Fable produced coefficient transport and reviewed U2,
exact separation, and the cv gate; Opus produced exact separation and reviewed
transport, U2 terminal finiteness, Q+E5 R3, and the td=12 trunk; Grok produced
U2, the td=12 trunk, the `(0,y)` initialization, and the cv primary. Sol
integrated those results and supplied two narrowly scoped U2/A-tower successor
lemmas rather than duplicating the peer primaries. After the checkpoint, use
Fable, Opus, and Grok first for the three independent hostile reviews and
route discriminators recorded only in the newest `LIVE STATE`; Sol retains
the integrative trunk/cross-lane problem. One Fable wrapper lost its final
bookkeeping because `ops/lane.sh` changed while it was waiting, although its
hash-pinned report was recovered. The launcher now parses its complete body
before execution, and recovered reports are a distinct dashboard state.

Allocation refresh (2026-08-29 08:15Z): the post-checkpoint wave remains
peer-heavy. Grok reviewed both the A-tower theorem and the rank-changing td8
trunk-arity kill; Fable reviewed U2 first-boundary finiteness and exact pole
purity and the td12 depth-24 successor; Opus independently reviewed both the
td8 zero-side initialization and trunk-arity correction.
Sol supplied the cross-lane trunk, td12, and direct-nested-U2 deductions and
integrates them rather than opening duplicate peer tasks. The reviewed td8
route kill is significant-news and therefore triggers a fresh whole-portfolio
ideation round after the next atomic checkpoint. All review lanes are now
quiescent. No current gate needs heavy
compute; AWS remains idle until a reviewed joint coefficient packet warrants
it. A parent `.ignore` and an explicit no-enumeration rule now enforce the
formalization-tree boundary for broad search tools.

Allocation and systems refresh (2026-08-29 09:35Z): significant-news round
`20260829T0820Z` closed with all four blind researchers and three independent
cross-pollination passes. Opus uniquely exposed both correlated central
errors—the false numerator branch in the proposed exit formula and the
prime-label/derivative misreading in U2—then independently passed the repaired
one-P0 family with one record-field correction. Fable supplied the broad
source/consumer synthesis and passed the full-exit carrier theorem with two
wording repairs. Grok supplied an independent exact td12 sibling T1 solve.
The Grok Q+E5 and Opus legacy-reprice reviews both failed closed when their
declared source bases changed during execution; neither is promotion evidence,
and both require fresh stable-basis review after the checkpoint. Sol
coordinates, integrates, and produced the cross-interface source audits.
Identity is not a vote; peer primary ownership resumes with the shared td12
child recurrence, U2 coverage/gluing, and Q+E5 after those relaunches.

The round's one selected machinery upgrade is live: `FALLACY.md` is a
hash-pinned semantic appendix on every new lane, and explicit
`charge_basis` declarations receive exact rational validation. This addresses
reasoning inputs and declared inference provenance; it does not claim semantic
prose lint. Focused regression passes 4/4 groups. The next quiet full-round
deadline is `2026-08-29T21:35Z`, the next broad web-sweep deadline remains
`2026-08-30T03:40Z`, and the next 48-hour systems checkpoint is
`2026-08-31T09:30Z`. All current work is desk-scale; AWS is idle and reserved
for a reviewed joint coefficient/CAS packet.

Adding a model requires one adapter in `ops/adapters/` and one roster row;
route documents do not assign permanent jobs by model name.
Admission requires a sealed same-input evaluation against a standing model.
At least one independently checked, nonduplicate contribution must change a
ranked launch, stop, merge, correction, or review decision; eloquence,
agreement, and duplicate ideas do not qualify.  Newly admitted models receive
the same blind-round standing and remain subject to normal history checksum,
scope audit, and different-model promotion rules.
