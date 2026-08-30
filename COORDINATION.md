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
7. **Completion handshake.** An author's hash or “ready” message is advisory
   while that author is still running. The packet is frozen only after the
   author is idle/completed and the coordinator independently verifies its
   seal, replay in every declared mode, and unchanged pre/post hashes. No
   reviewer, commit, or downstream consumer may charge preliminary bytes.
8. **Transactional local publication.** New reports authored by local agents
   or the coordinator use `ops/artifact_finalize.py` by default:
   `begin -> close -> finalize -> verify`. Authors write only the leased
   private partial; the tracked read-only manifest accompanies the final
   report. Root verifies after author completion and runs `verify --staged`
   on the explicitly staged report/manifest before commit. This supplements,
   rather than replaces, replay and hostile mathematical review. Existing
   external `ops/lane.sh` custody remains unchanged until a separate adapter
   migration is reviewed; do not retrofit the transaction into a live lane.

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
- Reviewed `ops/run_capped.py` is the opt-in `CAPRUN/v1` pilot for bounded
  argv-only process groups. Its exact-PGID scope, inherited per-process CPU
  limit, sampled RSS overshoot, and typed incomplete-cleanup outcome are
  binding limitations. No caller migration is implicit; each migration needs
  its own regression and review.
- Third-party tools may mutate shared CLI configuration; adapters must isolate
  or sanitize it, and a new/updated adapter gets a smoke test before use.
- Lane launchers take prompt files, reject duplicate live tags, record their
  true exit status, and keep one task and deliverable path per tag.  Every
  model-review prompt names exactly one report path whose basename matches the
  lane tag, explicitly instructs the reviewer to write that file and no other,
  and is smoke-checked for that destination before launch.  Referee text left
  only in adapter stdout is a failed-delivery draft, not promotion evidence;
  preserve it and rerun through a fresh output-explicit prompt.
- `ops/lane.sh` appends the compact current `FALLACY-v2.md` reasoning
  guardrail exactly once from a hash-pinned private snapshot and records both
  the original and composed prompt hashes.  The appendix is semantic
  instruction, not a lexical proof checker.  Reports may declare an exact machine line
  `charge_basis={...}`; the validator checks its rational delta, branch,
  positive flag count, and citation.  Invalid declarations quarantine the
  lane, while an absent declaration is recorded as `ABSENT` and never
  interpreted as a mathematical pass.  Changes to the prompt, appendix,
  adapter, or validator during a run quarantine the result; focused launcher
  regression is required after any edit to this path. Versioned predecessor
  `FALLACY.md` remains immutable for packet replay.
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
| Fable 5 (Anthropic) | `ops/adapters/claude.sh` | exact-model pinned; permanent equal-standing whole-portfolio researcher; receives every sealed full-round packet independently; clean same-input ideation through `20260829T2254Z`; distinctive reviewed work includes theorem-interface/lifecycle auditing, compiler custody, K00 compression, the exact localized gate intertwiner, the uniform lower two-root endpoint theorem, the E0 exact-`p` linear-vacuity correction, the reviewed algebraic-primitive gate filter, the reviewed single-root endpoint-transport mechanism, the independent repair of the active-`c2` D8--D15 cascade, the normalization/localization repair of the q1/q3 composition, the clean 442-slot hostile review of raw origin coupling, the fixed origin-residue slice audit, the fixed-`Q=X` ideal-membership exclusion, and the literal active-`c2` D16--D22 audit; normal hostile review remains mandatory |
| Opus 5 (Anthropic) | `ops/adapters/opus.sh` | exact-model pinned; **permanently admitted as an equal-standing whole-portfolio researcher by the `20260827T2137Z` same-input evaluation**; clean same-input ideation through `20260829T2254Z`; distinctive reviewed work includes the etale-`mu4` torsor target-budget theorem, source-level `G2-PSC` same-edge/subsumption correction, all-row Lagrange and homogeneous `NU` laws, mod-8 row death, an exact rank-one nonlinear control, closed-form recurrence fixtures, the clean-room repair of unit-root endpoint transport, the repaired full-system q1/q3 deep-locus compression, the exact q5--q13/even-gate tail classification, the reviewed raw-origin/parity coupling with its exact `Q=X` mutation, the generic quadratic-Q fixed-face rank theorem, the promoted degree-432 `K0` field theorem, and the promoted asymptotic-complement covering mechanism; normal hostile review remains mandatory |
| GPT / "Sol" (OpenAI) | `ops/adapters/codex.sh` | coordinator and equal-standing whole-portfolio researcher; exact `gpt-5.6-sol` with `ultra` reasoning through the pinned adapter; clean same-input ideation through `20260829T2254Z` |
| Grok (xAI) | `ops/adapters/grok.sh` | equal-standing whole-portfolio researcher; via `grok --prompt-file`; clean same-input ideation through `20260829T1517Z`; the `20260829T2254Z` call returned HTTP 402 before model work and is `UNAVAILABLE_NO_MODEL_WORK`, not a mathematical response; its earlier `FACE-NC`/`FACE-CHAR` promotions failed hostile typing review; its 2259Z constant-bundle insight survived only after gauge repair and its Hessian formula proved visibility rather than an obstruction; it independently confirmed the row-30 nonlinear class slice, the promoted `K0` theorem, the ARITH-SPREAD correction, and the scoped asymptotic-complement theorems |

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
before execution, and recovered reports have a distinct state in the
authoritative `LIVE STATE` and operator-facing chat summary.

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

Allocation and systems refresh (2026-08-29 10:44Z): the stable-basis review
wave again has peer-majority ownership. Grok independently passed the Q+E5
fixed-index pattern consumer with interface repairs; Opus verified the LL-1
reprice arithmetic but correctly refused promotion at the missing two-pole
full-flag carrier bridge; Fable found the edgewise-`V_{2,a}` defect in Sol's
provisional U2 source-mass proof and proved the weaker family floor `td>=12`.
Sol coordinates, independently replays the corrected bound, and integrates
the weakest dispositions. The next primary goes to the shared td12 child
recurrence; the U2 td12 equality landing, row-to-actual-edge coverage, and
two-pole attachment theorem proceed independently as slots free. Reviews stay
background/nonblocking. The lane guardrail now also forbids merge-free-to-St
8.5 inference without edgewise V2 typing and fixed-target/incoming-index
conflation. All listed work is desk-scale; AWS remains idle until a reviewed
heavy packet exists.

Allocation and systems refresh (2026-08-29 11:55Z): Grok independently
returns `PASS_WITH_REPAIR` on Sol's labelled one-P0 U2 td12 budget kill. The
route is promoted only at actual-landing, `REPRESENTATIVE` selected-exit
scope: `5+5+1>10`; other U2/one-P0 routes and all-td12 remain open. Stop
source/gluing/index work on that dead label and recycle it as a regression
fixture. In parallel, Sol and blind Opus independently converged on the
strong two-pole actual-first-separation attachment theorem; clean Grok review
now passes it with a nomenclature-only repair. The full-carrier bridge closes
the former LL-1 typing defect and licenses the exact `13 -> 7` replay. The shared td12
recurrence audit is fail-closed at source: B and sibling routes need separate
realized pair/completion packets, while the two sibling evaluations share one
parent jet family without an automatic Galois-conjugacy claim. Fable's
primary plus Sol hostile disposition
now promote the exact symbolic recurrence and own-order absorption identity,
while correcting `r=3i/2` on each actual type-`(2,3)` route and quarantining
the claimed one-dimensional cascade count. No vector or recurrence engine is
licensed; a typed desk-scale cascade-rank precursor may run independently.
This reviewed route kill is significant news, so after the next atomic
checkpoint launch a blind whole-portfolio ideation round across all proof,
disproof, and machinery avenues; descendants and reviews continue without
blocking it. Current work is desk-scale and AWS remains reserved for a
reviewed heavy coefficient/CAS packet.

Allocation and systems refresh (2026-08-29 12:20Z): two desk-scale
descendants are locally complete without blocking the significant-news
round. `TD12-FORMAL-CASCADE-RANK/v1` is provisional: the reduced operator is
injective with nominal cokernel two for B and three for sibling, while the
integral type-`(2,3)` binomial response (`r=3i/2 in Z`) absorbs all formal
rows through `s<=i`; no depth-window obstruction follows under
`i>=depth`. The route-separated exact-pair/completion/source-cap packets are
therefore the next source deliverables. LL1-R4 deterministically implements
the promoted full-actual carrier and exact `13 -> 7` replay, with an
independent validator and 166/166 acceptance checks, but remains provisional
software pending different-model review. Both reviews are background debt;
neither serializes the checkpoint or whole-portfolio ideation. No heavy
local process was used, and AWS remains idle until a reviewed heavy packet
exists.

Allocation and systems refresh (2026-08-29 13:15Z): round
`20260829T1224Z` closed with four clean blind reports and three clean
cross-pollination reports on basis `ccb6cd52...`; no numbered avenue reranks.
Fable's different-model LL1-R4 review promotes the narrowly typed software
consumer, while Opus's different-model cascade review strengthens the
formal transparency range and stops all homogeneous-window descendants.
Peer-equal primary ownership resumes with a route-separated
`TD12-GLOBAL-SOURCE-BRIDGE/v1`, an actual finite-pole scope review, a short
`TWIN-ORDER` derive-or-`OPEN` lane, and protected K00 counterexample
continuation. The LL1 equality profiles are banked until a typed client
exists: five terminal states encode six scalar-consistent routes. Sol owns
cross-lane integration. New provisionally credible work may spawn descendants
immediately; hostile
review stays in the background and gates promotion, not exploration.

The sole selected machinery trial is `ROUNDVIEW/v1`: a deterministic,
non-authoritative, hash-bound compiler for the newest strategy overlay, the
exact 46-row avenue inventory, and a historical heading index. It must fail
closed on missing or duplicate anchors, source mutation, or nondeterminism;
its output is a prompt slice only and can never become a second authority,
queue, or dashboard. Current lanes now use versioned `FALLACY-v2.md`, whose
small repair requires `charge_basis` only for a new exit-price assertion and
a direct mathematical-source citation. Pinned `FALLACY.md` v1 remains
immutable for historical packet replay. No wrong result depended on the prior
provenance loop. All current tasks remain desk-scale, AWS is idle, and heavy or uncertain CAS
is AWS-only. The next broad web sweep is due `2026-08-30T03:40Z`; the next
systems checkpoint is due `2026-08-31T09:30Z`; absent significant news, the
next full ideation round is no earlier than twelve hours after this closure.

Allocation and systems refresh (2026-08-29 14:30Z): two independently
reviewed results are now canonical. The finite-s full-actual attachment
theorem is banked at one-fibre/one-component, complete-carrier,
lower-floor-only scope; no current `s>=3` object is a typed consumer, so it
spawns no reprice or compute. The K00 grade-three radical obstruction closes
every rank-exact-two full-`P6` chart; stop those engines immediately without
relabeling the historical capped selected chart. K00 rank five and rank at
most one continue provisionally under one combined Fable hostile review.
Fable's td12 B source bridge is under Grok hostile review, while Opus's
sibling bridge is under internal audit. Sol's sealed RESROW correction stops
the proposed `j=17` descendant provisionally; `j=42` is only an outside-B24
frontier marker pending review, not a launch. Producer confidence may still
fan out nonconflicting work, but promotion remains review-gated. No new heavy
job is licensed; all heavy or uncertain CAS remains AWS-only.

Allocation and systems refresh (2026-08-29 14:40Z): Grok's different-model
review now promotes only the Fable B bridge C1--C3 core and repaired C4
operator/first primitive at named-actual-occurrence scope. The distant
inhomogeneous row passes uniquely on the reviewed T1 ratio; there is no
B-route kill, uniform scheme/cap, serialized `PairRef`, or source-value
packet. Sol's `j=17` vacuity and `j=42` frontier remain provisional. The
Opus S bridge has completed internal mathematical audit with material
repairs, but its producer body seal fails and different-model review remains
mandatory; the generic-source-translation `FLOOR-COORD` simplification is
provisional. Opus also owns the active conditional K00 grade-four
rank-zero-plane desk lane. These lanes remain asynchronous and nonblocking;
no new heavy launch is licensed, and heavy or uncertain CAS remains
AWS-only.

Systems maintenance refresh (2026-08-29 14:54Z): four hung ad hoc desk
Singular invocations--three Opus scratch probes and Fable's
`Singular --version` query--exposed the same lifecycle defect, not a
mathematical or resource incident. All four printed their expected stdout
but did not close cleanly because the
stdin/termination contract was incomplete; a wall watchdog using
`while kill -0 "$pid"; do ...; done; wait` could continue on an unreaped
completed child. The coordinator terminated only each validated exact
process group; no orphan remained. The stalls occurred after the expected
output and revise no report verdict or mathematical replay. A read-only audit
found nine bare loops of this form: one signal-cleanup loop in `ops/lane.sh`
and eight case supervisor/worker telemetry loops. Bounded D43
heartbeat/deadline polling and one-shot status checks are lower-priority
audit targets, not equivalent findings.

The next systems-maintenance target is one repo-owned capped-process helper
or supervisor contract. It must close stdin unless input is deliberately
streamed, terminate Singular scripts with explicit `quit;`, make `wait`/the
reaped child status authoritative, and enforce wall, CPU, and RSS caps while
recording process-group telemetry. Cancellation must validate PID, PGID, and
available start identity; send TERM to the exact PGID; allow a bounded grace
period; then KILL only that exact PGID and reap once. Broad name matching,
unscoped `pgrep`/`pkill`, and indefinite `kill -0` polling are forbidden.
The helper and call-site migration require their own reviewed software
packet; no code changes or active-lane mutation belong in this checkpoint.

Allocation refresh (2026-08-29 15:07Z): Fable's combined K00 review and the
binding coordinator integration promote the rank-five and rank-at-most-one
cores with repairs. Together with the prior rank-two obstruction, the full
grade-three compatible geometric incidence over `V(B)` is exactly the
reduced plane `(2s,t/8,s,t,s,2t)` times free `u`, over an algebraic closure.
Stop all rank-three through rank-five Fitting/localizer jobs and every
selected grade-three rank-one `I2(E3)` chart; preserve historical cap labels.
The repaired containment is `B subset P6`, hence
`V(P6) subset V(B)`. Fable's new minimal-prime decomposition and exact
minimal-power refinements stay provisional, and its prompt-induced generic
`charge_basis` ledger is only input metadata; the validated exit status is
`charge_basis=ABSENT`.

Opus's grade-four rank-zero-plane primary is now DONE and provisionally finds
a proper 13-dimensional nonreduced survivor with prime reduced locus
`A^12 x G_m`; `d*_3` and `k10_0` vanish at grade four but return at grade
five. It awaits different-model review. `K00-G5-RANK0-PLANE` is registered in
both radical-input and scheme-input variants but must not launch before this
canonical checkpoint is sealed. No other K00 computation is licensed by this
delta; heavy or uncertain CAS remains AWS-only.

Allocation and systems refresh (2026-08-29 16:35Z): significant-news round
`20260829T1517Z` closes with four blind whole-portfolio researchers and three
adversarial cross-pollination passes. Opus discovered the grade-five leading-
plane collapse; Fable and Grok independently reconstructed it; Fable's
separate two-input primary supplied a richer unpromoted scheme census; Sol
integrated the maximum reviewed source-compatible theorem. The normalized
valuation-one K00 seed is closed at grade five, so no grade-six descendant or
scheme-primary AWS job remains live. Avenue 36 stays open but must be re-seeded
from an honest higher-valuation or different-support source normalization.

On the proof side, Fable's fresh review promotes the repaired S map-level
bridge, Opus review promotes B first-resonance vacuity, and Sol's interface
audit confirms that completion machinery is present while actual
td12/U1/B25/S17 occurrence is absent. Put the strongest proof slot on that
global occurrence/coverage arrow; source-value serialization follows only
after a named vertex. Local residue, Ward, proportionality, and Hermite jobs
remain stopped or interface-blocked. Reviews continue in the background.

The internally hostile-reviewed opt-in `CAPRUN/v1` pilot passes 17 ordinary and 17
optimized fixtures, but no caller is migrated in this checkpoint. A separate
Fable primary launched four uncertain local Singular subjobs that reached
their 60-second caps; those results are typed `RESOURCE_CAP_NO_VERDICT` and
unused, but the launch violated policy. External lanes must fail closed before
uncertain local CAS; 60 seconds is a desk ceiling, not permission to discover
cost. No campaign-owned heavy AWS mathematics is active or presently
justified. Heavy or uncertain work remains AWS-only; the 512-vCPU quota is a
ceiling, and separately owned capacity remains outside campaign inspection.
The next web, quiet-round, and systems deadlines are respectively
`2026-08-30T03:40Z`, `2026-08-30T04:35Z`, and
`2026-08-31T16:35Z`.

Allocation and systems refresh (2026-08-30 00:35Z): significant-news round
`20260829T2254Z` closed with four completed blind contexts (two Sol, Fable,
Opus), two independent cross-pollinations, and one Grok 402 receipt typed
`UNAVAILABLE_NO_MODEL_WORK`. Fable independently found the decisive empty-
Proj correction and then sharpened the unloaded filtration to
`J^5 subset I subset J^2`; a clean AWS V2/replay-B route independently
confirms all 56 fifth-degree generators and an explicit fourth-power
noncontainment. Opus independently promotes the complete `e=3,m=1` G9 fan.
The `e=2,m=2` G10 producer is genuinely new scope and remains review-gated.
Sol coordinates the cross-interface corrections and exact source partition.

Proof-side allocation is asynchronous: pair-square QCS gets one definition/
invariance gate; the minimal-degree block surface gets a separate codimension-
one hostile proof review; the actual-map occurrence/coverage arrow and
primitive-monodromy horn stay live. The scalar ACV inequality without a
Keller partner and the literal regular monomial chart are stopped clients,
not stopped broad avenues. K00 next work reviews e2m2 while independently
opening e3m2 and the source-completeness partition. Reasonably credible
producer descendants need not wait for reviewers, but canonical promotion
does.

The round's one systems trial is independent section assembly. Opus found two
mandatory and seven secondary contract defects; all are repaired, 9/9 focused
tests pass under ordinary/`-O`/`-OO`, and 47/47 full operations tests pass
ordinary/optimized. The repaired bytes remain `TRIAL_NOT_ENABLED` until a
stable-basis hostile re-review. A Fable quartic review nevertheless ran an
86-second local Singular refinement and an abandoned 300-second decomposition;
this is a policy incident. Future external prompts must explicitly prohibit
uncertain local CAS and route it to AWS. Mathematical verdicts are not revised,
but detailed counts are not machine dependencies until portable replay exists.

AWS r6b is released running/idle/unclaimed with zero CAS process or session;
the clean sharp-exponent packet is frozen. Box02/Box03 R4 diagnostics were
previously stopped after their promotion-independent role ended. Heavy or
uncertain computation remains AWS-only. No campaign action inspected, built,
modified, or controlled the separately owned formalization. The next broad
web sweep remains due no earlier than `2026-08-30T03:40Z`; the next quiet full
round is due within twelve hours of this closure unless significant news fires
sooner; the 48-hour systems-improvement clock resets at this repair.

Adding a model requires one adapter in `ops/adapters/` and one roster row;
route documents do not assign permanent jobs by model name.
Admission requires a sealed same-input evaluation against a standing model.
At least one independently checked, nonduplicate contribution must change a
ranked launch, stop, merge, correction, or review decision; eloquence,
agreement, and duplicate ideas do not qualify.  Newly admitted models receive
the same blind-round standing and remain subject to normal history checksum,
scope audit, and different-model promotion rules.

Allocation refresh (2026-08-30 00:47Z): Fable's block-descent hostile review
closes the last live lane from round `20260829T2254Z`. The binding theorem
retypes every nontrivial intermediate block as an étale sandwich through a
forced non-`A^2` normal surface whose nonempty branch divisor is missed by
the first map and maps into `A(F)`. Stop the codimension-one-image and
intermediate-`A^2` minimality descendants; they are ruled out by theorem,
not merely review-blocked. Primitive monodromy stays open. Its cheapest new
block client is the provisional `BD-D2` obstruction, independent of the
pair-square QCS gate and of K00 source partitioning. A CRT/minimal-polynomial
repair promotes the discriminant-fibre deficit without a flatness assumption;
only the polynomial-parametrization decoration remains unpromoted review
debt. No lane is active at this atomic checkpoint; commit
and push precede the next research wave. AWS remains idle/unclaimed, and
heavy or uncertain computation remains AWS-only.

Allocation and systems refresh (2026-08-30 02:28Z): the proof-side block
lane has advanced twice. Different-model review promotes `BD-GAL`, excluding
every proper Galois intermediate quotient and hence every two-block system.
Separate Opus review promotes the exact log-plurigenus of a two-section
complement and rules out a dominant `A^2` first leg whenever at least two
collision fibres occur. At that timestamp Fable's `AL3-REDUCE` review was
live; confirmation would close the affine-linear Miranda cubic subfamily
without waiting on any K00 lane. A sealed review-gated rational-forest
producer now makes the nonlinear successor finite: generic quadratic-
coefficient infinity already has genus two, while smooth coefficient degree
at least three has positive geometric genus. Review the residue formula, then
classify only degenerate quadratic infinity forests; no nonlinear family is
yet promoted closed.

K00 now has four different-model-confirmed generic cells
`(e,m)=(2,1),(3,1),(2,2),(3,2)`. The positive-order K10 boundary is not
closed: on `(2,2),h10=1`, G11 nonemptiness is different-model confirmed;
the provisional G12 extraction kills the old rank-one branch but retains
fresh rank-one and rank-two points through G12, making G13 the next literal
gate after review. The general 569-tail calendar was
independently reconstructed by Opus and is promoted at exact possible-arrival
scope, with tangentiality and non-attainment qualifications. It refutes
cone/rank-only and ratio-only recurrence but does not establish that no finite
transition quotient exists.

The pair-square curve layer is reviewed and shows why abstract augmentation
or local inertia cannot prove QCS. The surface successor is narrowed to one
scheme-theoretically marked conductor stalk and its equivariant generic-to-
special cone. Its graph, dimension match, and marked-connectivity claims are
unconstructed; a same-model correction also distinguishes affine Kummer
ramification from the physical pole and withholds promotion.

One workflow defect is banked for the next systems micro-round: two completed
external reports observed an excluded nested-worktree status despite the
no-inspection instruction; those observations are quarantined and carry no
mathematics. The calendar receipt is clean—the human prompt and composed model
prompt are different artifacts, and each original/post-run pair matches.
After that external lane closes and this checkpoint is pushed, harden
the Fable/Opus adapters with an OS-level deny rule for the excluded path and a
read-only frozen prompt snapshot, then regression-test both positive review
delivery and forbidden-path failure. Do not edit adapters under live lanes.

All current mathematics is desk-scale. AWS is idle/unclaimed and no heavy
campaign job is licensed; heavy or uncertain CAS remains AWS-only. The next
broad web sweep is no earlier than `2026-08-30T03:40Z`; the quiet full-round
deadline remains `2026-08-30T12:35Z` unless significant news triggers one
sooner. At this timestamp the next coherent commit/push awaited closure of the
remaining mutating Fable cubic-review log. Holds/human gates: none.

Allocation refresh (2026-08-30 03:00Z): the remaining Fable cubic-review lane
has closed with exit code one and no report because its generated response
exceeded the 64,000-token output cap. Its immutable prompt and adapter hashes
match their post-run values, so this is an operational failure and no
mathematical verdict. Keep `AL3-REDUCE` and every affine-linear Miranda cubic
consequence provisional; after this atomic checkpoint, issue a shorter,
explicitly bounded different-model review. No mutating external lane or heavy
campaign job is active. The checkpoint is therefore unblocked. Adapter
path-deny hardening remains the first systems task after the push, before the
next external lane. AWS is idle/unclaimed; heavy or uncertain CAS remains
AWS-only. Grok remains unavailable: both the affine-linear cubic review and
the first `e=3,m=2` review launch returned HTTP 402 before model work because
the Grok Build balance was exhausted; record both as
`UNAVAILABLE_NO_MODEL_WORK`. Web and quiet-round clocks remain
`2026-08-30T03:40Z` and `2026-08-30T12:35Z`. Holds/human gates: none.

Systems refresh (2026-08-30 03:12Z): the queued adapter boundary is complete.
`ops/lane.sh` now requires macOS Seatbelt and launches every external adapter
and descendant beneath a profile that denies direct and symlink-resolved
reads/writes of the excluded nested workspace. It separately denies writes to
the private prompt-custody directory, whose snapshots and composed prompt are
mode `0400`, and denies the model any write to its `.run.v2` receipt. Receipts
pin pre/post launcher and generated-profile hashes. The full operations suite
passes 50/50 in ordinary, `-O`, and `-OO` modes; all adapter shell syntax
checks pass. Receipt schema stays v2.
Commit and push this systems atom before launching the compact AL3 review, so
the review basis itself contains the enforcement. No heavy job is active;
AWS remains idle/unclaimed and heavy or uncertain CAS stays AWS-only.

Allocation refresh (2026-08-30 03:46Z): both first hardened mathematical
lanes closed cleanly. Fable's compact hostile review promotes `AL3-CLOSED`:
no proper cubic intermediate block has affine-linear Miranda coefficients in
any fixed global trace-zero basis. Opus independently promotes the broader
rational-forest first-leg theorem and the generic quadratic infinity
exclusion. A Sol sublane has a sealed finite classification of the reduced
`(2,3)` forest locus (seven viable factor types, two impossible); it is
provisional until a fresh different-model review on the next committed basis.
Keep nonlinear/basis-minimal cubic closure, nonreduced infinity, projective
basepoints, singular closure, and degree-drop strata open.

Pair-square now has an exact but review-gated finite-set consumer: a genuine
special-to-generic ancestry surjection would canonically produce the local
augmentation cone of length `w-b`. Standard specialization has the opposite
direction, so the scheme-level `ANCESTRY-STALK` construction remains the
gate. Do not start the event graph or infer QCS from dimensions.

The K00 G13 sublane reports an exact provisional kill of every fresh `n=5`
G12 survivor via a new row-six quartic and a second cokernel combination. It
is writing a sealed packet with an old-pass/new-fail control for the following
checkpoint; do not rush it into this one and do not promote before independent
carry/source review. Even confirmation closes only the declared
`e=2,m=2,h10=1` finite child, not occurrence, arcs, or the source atlas.

The scheduled web sweep reset the backstop to `2026-08-31T03:40Z`. It found
no external plane resolution and only one missed August-25 F2 interface note;
crosswalk its `q18`/`B5Q` values during ideation without launching broad CAS.
The combined affine-linear closure, nonlinear finite classification, and G13
provisional kill are significant news. Immediately after this atomic
commit/push, launch the classification review and begin a fresh whole-
portfolio ideation wave; background review must not block independent new
work. No heavy campaign job is currently licensed, AWS is idle/unclaimed,
and all heavy or uncertain CAS remains AWS-only. Holds/human gates: none.

Allocation refresh (2026-08-30 03:59Z): checkpoint
`201b848b4422225f9514145c9c9655b635564404` is pushed and matches remote
`master`. The reduced `(2,3)` classification is now under a bounded Fable
hostile review on that frozen basis; a Sol whole-portfolio significant-news
ideation lane runs independently and does not wait for the verdict.

The K00 G13 packet is now frozen as producer `b352e26e...`/body
`82c277ca...` with replay `a508b985...`. It provisionally kills both fresh
`n=5` rank-one signs and every rank-two G12 survivor by two independent G13
terminals. Commit it as a small second atom, then start different-model
carry/source review. The full `h10=1` cell remains conditional on the
provisional old-`n=4` G12 parent, and neither result bears on occurrence,
arcs, attainment, or source completeness.

One author announced hashes before finishing a strengthening edit. Root's
pre-commit replay caught the drift; no committed or reviewed artifact was
affected. The completion handshake above is now binding: messages from a
running author are not frozen custody, and root must verify final bytes after
the lane becomes idle/completed. AWS remains idle/unclaimed; no heavy job is
licensed. Holds/human gates: none.

Allocation refresh (2026-08-30 04:12Z): Fable's bounded classification review
closed cleanly with `CONFIRM_WITH_CORRECTIONS` and no mathematical error.
Binding integration `e3dc96f0...` promotes the exact nine-type reduced
`(2,3)` rational-tree classification. The correction firewall distinguishes
empty factorization types `F8,F9` from refinements and records that affine
coefficient common zeros are invisible to infinity. The classification lane
is closed; Opus remains live on the independent G12--G13 carry/source review.

Proceed provisionally on two nonblocking nonlinear clients. First, sealed
attachment packet `f3129c34...` reduces the smooth projectively finite,
irreducible-ramification branch to `F5`; reducible ramification remains within
that stratum, while basepoint types are outside its finiteness hypothesis.
Queue a different-model review after the current reviews free a slot. Second,
whole-portfolio ideation `b5119d76...` proposes
`DISC8-CONDUCTOR`: the full cubic discriminant divisor is basis-invariant and
has degree at most eight for a quadratic presentation. Keep its
order/normalization conductor typing provisional until checked on actual
local controls.

Allocation for the next tranche is 25% full discriminant/conductor/full-
boundary work; 20% reviews; 20% K00 lift-image plus occurrence; 15% one-stalk
nearby/vanishing-cycle ancestry; and 20% `A(F)` source audit, bounded Strinz
crosswalk, and uniform-complexity characteristic-`p` falsification. A systems
sublane is implementing the bounded `ARTIFACT-FINALIZE/v1` transaction and
tests without touching live adapters. AWS remains idle until a source-reviewed
heavy packet exists; local heavy CAS remains prohibited. Holds/human gates:
none.

Allocation refresh (2026-08-30 04:16Z): Opus independently reconstructed the
G12--G13 chain and closed with exit zero. Binding integration `5d66761f...`
promotes the exact field-point emptiness of the normalized
`e=2,m=2,h10=1` cell by G13. The G13 rank-two terminal is independent of the
G12 survival equations, reducing rollback exposure. Corrections to raw term-
count labels, one fixture description, and rank-one kernel dimension do not
alter the theorem.

Do not continue to another grade on `h10=1`. The cheapest literal cell is
`h10=2`, but run it only as a bounded secondary lane after a source/occurrence
or truncation-image client is specified. The promoted cell remains neither a
scheme-level emptiness result nor a source atlas, arc theorem, or map claim.
Both external review lanes are now closed; the next different-model review
slot goes to the provisional ramification-attachment dichotomy. The
`ARTIFACT-FINALIZE/v1` systems lane may finish independently. AWS remains
idle pending a source-reviewed heavy packet; holds/human gates: none.

Allocation refresh (2026-08-30 04:36Z): Opus's discriminant/index review
closed cleanly with `CONFIRM_WITH_CORRECTIONS`. Binding integration
`410de2f5...` promotes `DISC8-INDEX`: the full trace-discriminant divisor is
basis-independent, quadratic coefficients force degree at most eight, and a
reduced order has a global normalization inclusion over `C[u,v]` with
`Delta_B=(det M)^2 Delta_Btilde` and index degree at most four. Replace every
informal “conductor index” label by “normalization index (Fitting/length)
divisor.” Keep source ramification, different, target discriminant, and
reduced branch separate. No curve-delta translation is licensed without a
Tor-free slice/normalization comparison and the applicable Gorenstein input.

The two strict-henselian controls in the integration are now mandatory before
any heavy `DISC8` computation. After they pass, the high-information client is
the joint divisor/component lattice on the promoted `F1`--`F7` types, not a
blind discriminant image sweep. The Fable attachment review and
`ARTIFACT-FINALIZE/v1` systems lane continue asynchronously. K00 occurrence/
truncation images and one actual ancestry stalk remain independent. AWS is
idle pending a source-reviewed heavy packet; holds/human gates: none.

Allocation refresh (2026-08-30 04:42Z): Fable's attachment review closes
cleanly with `CONFIRM_WITH_CORRECTIONS`. Binding integration `255bd0ba...`
promotes the exact boundary-critical set and nonempty reduced ramification,
then narrows the smooth reduced projectively finite quadratic block stratum
to the fork “reducible ramification or `F5`.” Irreducible ramification forces
`F5` and concentrates all eight `H.R_pi` units at the unique triple point.

Retire the proposed raw `Cl(Y)` rank-at-most-one gate. The same review
independently derives `rho(X)=11` and `rank Cl(Y)>=8`, agreeing with supporting
packet `7ee2a8e3...`; the component injection remains exact, but only the
actual effective component lattice can now help. Allocate the next quadratic
work first to the one-chart `F5` local different, and second to effective
decompositions of `2A+B` with attachment and `DISC8-INDEX` constraints. The
systems finalizer has reported completion but remains outside this math atom
until root independently inspects and reruns it. AWS stays idle until a
source-reviewed heavy packet exists; holds/human gates: none.

Systems refresh (2026-08-30 04:48Z): `ARTIFACT-FINALIZE/v1` is accepted for
new locally authored reports. Root read the complete 1,691-line
implementation/test pair, matched hashes `c62f35f1...`/`5256a36d...`, and
reran the full operations suite 65/65 in ordinary, `-O`, and `-OO` modes.
Self-hosted acceptance report `1c474b02...`/body `f6aae71f...` and manifest
`dc96281b...` exercise lease, close, canonical seal, no-overwrite hard-link
publication, immutable crash-recovery record, residue checks, and optional
stage-zero Git binding. The tool is cooperative integrity/custody machinery,
not hostile same-user security or mathematical evidence. External adapter
migration remains deferred and requires its own regression packet. No heavy
job is licensed; AWS remains idle; holds/human gates: none.

Allocation refresh (2026-08-30 04:52Z): completed sealed producer
`8a1c3c50...` gives the exact F5 local different. Its tangent cone
`(z-v)(3z-v)` has two smooth branches and the eight boundary-intersection
units split rigidly as `5+3`. Provisional composition with the promoted
attachment-cycle theorem forces reduced ramification to be reducible on
every survivor in the current smooth, reduced, projectively finite quadratic
scope. Commit this frozen producer, then send it to a different model for a
bounded hostile review while the effective component-lattice lane continues
without blocking. Do not launch coefficient elimination before that finite
lattice gate. AWS remains idle; holds/human gates: none.

Allocation refresh (2026-08-30 05:06Z): Opus closes the F5 local review with
`CONFIRM_WITH_CORRECTIONS`. Transactional binding integration `8fcd071f...`
promotes the exact two analytic different branches and `5+3` boundary split;
the tangent-line notation and no-common-branch check are repaired. Every
survivor in the smooth, irreducible, reduced-infinity, projectively finite
quadratic first-leg scope now has at least two ramification components.

Continue the already active rank-11 component-lattice lane provisionally.
Its task is now eliminative, not merely classificatory: carry the exact
`(5,3)` boundary vectors, Cartier multiplicities, contracted `A`-null curves,
effectivity, and forest graph. If a finite lattice no-go freezes, commit it
and launch a different-model review immediately; do not wait for coefficient
elimination. AWS remains idle; holds/human gates: none.

Allocation refresh (2026-08-30 05:32Z): different-model GPT-5.5 xhigh review
closes the global ramification packet with `CONFIRM_WITH_CORRECTIONS` and no
mathematical gap. Binding integration `c9871c92...` promotes emptiness of the
smooth, projectively finite, reduced-squarefree fixed-basis quadratic stratum
under the dominant-`A2` rational-forest/unit hypotheses. Stop all coefficient
realization and lattice work inside that closed cell. Move the quadratic owner
to basepoint/nonfinite, singular-incidence, degree-drop, and basis-minimization
strata while the independent whole-portfolio ideation lane continues.

Fable 5 and Opus 5 currently reach their pinned adapters but are refused at an
account-wide Claude monthly spend ceiling; Grok reaches its adapter but has an
exhausted Build balance. All three failures occurred before model work and are
quarantined availability receipts, not reviews. GPT-5.5 xhigh completed the
different-model gate. Retry the peer adapters after billing capacity changes,
without blocking reversible research. No heavy local computation is active;
AWS is idle/unclaimed and remains the only venue for a future reviewed heavy
packet. Web backstop remains `2026-08-31T03:40Z`; holds/human gates: none.

Allocation refresh (2026-08-30 06:04Z): two GPT-5.5 xhigh reviews close the
smooth quadratic frontier with corrections and no mathematical gap. Binding
integration `1b30c798...` absorbs nonreduced infinity and both projective and
affine coefficient basepoints whenever the exact quadratic incidence is
smooth; together with `AL3-CLOSED` it excludes every smooth fixed trace-zero
presentation of coefficient maximum at most two in the promoted proper
cubic-block first-leg scope. Stop all further work inside that cell.

The independent one-attachment theorem is now an exact structural client:
one physical attachment forces three infinity sections `(b,a,a)`, pure-power
boundary discriminant of degree `4d`, exact affine discriminant degree `4d`,
fixed-algebra trace-zero basis minimality, and boundary order index `2d`.
Do not treat it as an existence result, surface conductor statement, or a
singular theorem. Continue the already active normal-singular/ADE lane and
the orthogonal nonnormal/basis-coverage lane without waiting on one another.
Their first task is theorem/no-go reduction, not computation. No heavy local
job is licensed; AWS remains idle but is the required venue for any later
source-reviewed heavy packet. Peer billing limits are unchanged; GPT-5.5
xhigh remains available. Web backstop remains `2026-08-31T03:40Z`;
holds/human gates: none.

Allocation refresh (2026-08-30 06:20Z): GPT-5.5 xhigh confirms the normal-
singular quadratic reduction with corrections and no mathematical gap.
Binding integration `17f41e70...` turns the lane into a finite effective
problem: Du Val exceptional trees embed as possibly nonprimitive root
sublattices of the exact geometric `D9(-1)` complement; `E8` is gone; and
ramification through each tree obeys `n=C_ADE*m` with positive exceptional
multiplicities and nonzero strict attachment vector. Continue the active
ADE-decorated lane on effectivity, total infinity/different multiplicities,
typed boundary vertices, carriers, and physical attachment points. Do not
infer a cycle from `n!=0` alone and do not enumerate abstract root embeddings
as if they occurred geometrically.

The nonnormal moving-double-section review and its normalization/conductor
successor continue independently. No heavy computation is licensed; use AWS
only if a reviewed finite enumeration later exceeds desk scale. The external
GPT-5.5 reviewer remains available; peer billing limits are unchanged. Web
backstop remains `2026-08-31T03:40Z`; holds/human gates: none.

Allocation refresh (2026-08-30 06:23Z): GPT-5.5 xhigh confirms the nonnormal
quadratic content-cone dichotomy with corrections and no mathematical gap.
Binding integration `45685cce...` proves the affine incidence normal and
reduces every projective nonnormal quadratic presentation to the sole form
`Phi^h=Q^2L+TQS+T^2R`, with moving double `(1,1)` infinity and intrinsic
`deg Delta<=6`. Stop broad nonnormal factor searches. Continue the active
normalization/conductor lane on the blowup `(T,Q)`, the actual finite
normalization, conductor preimage, and square/split/connected degenerations of
the quartic `S_C^2-4L_C R_C`. A genus-one candidate counts only after it is
proved to be a component of the resolved first-leg boundary.

The normal-singular ADE-decorated lane remains independent and active. The
quadratic portfolio now has two sharply typed geometric frontiers rather than
an open smooth/nonnormal census: ADE-decorated normal singularity, and the one
moving-double-section conductor form. Basis-orbit coverage across quadratic
presentations remains separate. No heavy computation is licensed; use AWS
only for a later reviewed finite enumeration that exceeds desk scale. Web
backstop remains `2026-08-31T03:40Z`; holds/human gates: none.

Allocation refresh (2026-08-30 06:58Z): GPT-5.5 xhigh confirms the
moving-double-section normalization/conductor theorem with corrections and no
mathematical gap. Binding integration `01e77dba...` closes the entire
nonnormal fixed-quadratic-presentation stratum: affine normality forces a
smooth elliptic conductor, its normalization quotient `O_C(-2)` gives
`h1=1`, and both irregularity and rational-forest arguments contradict the
dominant `A2` first leg. Stop all work inside the nonnormal quadratic cell.

Binding ADE integration `3846f7e2...` simultaneously promotes the exact
connected `A/D` Cartan semigroups and conditional caps, while recording that
no connected type is killed. Continue the active desk-scale local enumerator,
but label it as one-component local data only. Its successor must add
disconnected simultaneous `D9` embedding orbits, global cap allocation,
paired infinity data, physical carrier graphs, and ruled-marking effectivity;
split common-carrier/nonfinite cases before using any cap. Review remains a
background gate, never a research barrier.

The independent basis lane should retain the newly found distinction between
quadratic-to-quadratic basis changes and existence of a quadratic basis. A
nonconstant shear can preserve degree two without fixed-root/content
degeneracy; extract only the stronger theorem licensed by proper-block
nonmonogenicity. No heavy local computation is licensed; AWS is idle and is
the required venue if the reviewed global embedding enumeration outgrows
desk scale. Peer billing limits are unchanged; GPT-5.5 xhigh remains
available. Web backstop remains `2026-08-31T03:40Z`; holds/human gates: none.

Allocation refresh (2026-08-30 07:05Z): the exact one-connected-component
Cartan enumerator is sealed and independently replayed locally. Commit its
script, deterministic data, report, and manifest, then run a bounded GPT-5.5
xhigh hostile review in the background. Treat `16,360/12,238` (cap eight)
and `772/646` (conditional cap four) only as local labelled/diagram-orbit
counts. The conditional one-carrier cut leaves `718/563` and `198/163`, but
is unavailable until actual resolved carrier connectivity is proved.

Do not spend another lane optimizing the local table. Advance immediately to
disconnected simultaneous `D9` embeddings and paired infinity/carrier data;
distinguish per-point target-line caps from genuinely shared infinity or
fibre budgets. If that global enumeration becomes materially heavier than
the one-second ordinary replay, package it for AWS rather than running it
locally. The basis-change lane remains independent and active; holds/human
gates: none.

Allocation refresh (2026-08-30 07:20Z): different-model review promotes the
one-component Cartan table through binding integration `ecb5d18b...`; no
script or data repair was needed. Retire local-table optimization. The active
global lane now owns disconnected `D9` root-subsystem orbits, actual vertical
conic-fibre blowup configurations, paired infinity vectors, correctly shared
slice budgets, carrier labels, and effectivity. Target-line cap eight is per
chosen singular image; never pool it across unrelated points. Any new
`A.H=3` or `B.H=2` boundary cap remains provisional until its own exact
total-transform/properness proof is sealed and reviewed.

Binding basis integration `30c8ae05...` promotes the leading image/kernel
section theorem and constant-only affine-linear changes in the integral
nonmonogenic proper-block scope. The nonmonogenicity charge is `f9720718...`,
not merely the block sandwich. Continue entry-degree-at-least-two orbit work
only when a slot is free; it is secondary to the normal-singular global
effectivity gate and cannot prove quadratic-basis existence. The normal
monogenic counterexample permanently retires the broad fixed-full-root,
content, or nonfiniteness heuristic. AWS remains required for any materially
heavy global enumeration; web and peer-capacity backstops are unchanged;
holds/human gates: none.

Allocation refresh (2026-08-30 08:07Z): two GPT-5.5 xhigh reviews close with
`CONFIRM_WITH_CORRECTIONS` and no mathematical gap. Binding integration
`8b1404cc...` promotes the 115 unmarked reflection-closed `D9` signed-support
signatures as abstract weighted `B_s/U_s` fibre forests, with the separate
75-signature saturated diagnostic and exact shared-cap ownership. Binding
integration `f385387d...` independently forces every reduced, finite-near-
infinity normal-singular quadratic survivor to the unique `F5` boundary and
concentrates all `H.R=8` units at its one triple/tangency point. Affine ADE
trees remain live, and neither theorem asserts marked effectivity or
occurrence.

Continue the already active carrier/effectivity lane without waiting on any
new review. It must decorate the 115 skeletons with target-image partitions,
actual beta-weighted fibre budgets, paired Cartier vectors, smooth-versus-
singular F5 carrier data, physical contacts, and common-carrier flags before
testing ruled classes. Do not optimize or Cartesian-expand the local 12,238-
orbit table. In parallel, source-audit two new global filters from the whole-
portfolio ideation round: reduced-support adjunction energies and the exact
Miyanishi--Sugie/Fujita `A1`-ruling hypotheses for
`X minus Supp(H+R)`. The latter must retain the possible complete-base branch
until excluded. No heavy local computation is licensed; AWS remains idle and
is mandatory only if a reviewed decorated enumeration exceeds desk scale.
Web backstop remains `2026-08-31T03:40Z`; holds/human gates: none.

Allocation refresh (2026-08-30 08:33Z): GPT-5.5 xhigh closes the
Miyanishi--Sugie/Euler audit with `CONFIRM_WITH_CORRECTIONS` and no
mathematical gap. Binding integration `f092a715...` promotes a direct
`A1`-fibration on `U=X minus Supp(H+R_X)`, base `A1` or `P1`, the exact
completion-invariant identity `e(U)=12-r-c`, and the F5 support budget
`r+k<=8`. Remove every singular-F5 `A8` row now. Retain `A7` only as the
extremal `r_aff=0,k=1`, affine-base cell with all second-ruling fibres
irreducible in reduced support.

Charge `r_aff+k<=8-r_0` to the active carrier/effectivity producer as soon as
it freezes, but do not make its hostile review a research barrier. Keep
original conic fibres and the new `A1`-ruling fibres typed separately. The
parallel successor tests whether the actual etale first-leg degree `d1>=2`
excludes the complete-base branch or admits a degree-at-least-two control.
Do not enumerate ruling classes on the raw `D9` marking without a boundary-
adaptation theorem. No heavy computation is licensed; AWS remains idle and
mandatory for any later reviewed enumeration that exceeds desk scale. Web
backstop remains `2026-08-31T03:40Z`; holds/human gates: none.
