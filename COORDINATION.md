# COORDINATION.md — the campaign protocol

This file is the campaign protocol. Any swarm can run it, and any
sufficiently capable model can fill any role below. What is specific to one
swarm (its roster, seats, budget, machines, and standing directives) lives in
that swarm's `team/<name>/README.md`; the home swarm's is
`team/swarmHQ/README.md`. See `team/README.md` for the folder contract. Avenue inventory and
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

- `README.md` — project orientation and the contributor contract.
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
artifacts live beside the relevant cases. Rosters, machine inventory, and
compute policy are swarm-specific and live in `team/<name>/README.md`.

The root ledgers are written by swarmHQ's coordinator. Every other swarm keeps
its roster, journal, and `LIVE STATE` in `team/<name>/` and contributes results
through pull requests, as `README.md` describes.

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

- at most three child lanes and one unreviewed dependency generation per
  provisional claim;
- at most six active provisional roots campaign-wide;
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
proof/counterexample, a load-bearing review reversal, or a new result changing
the global ranking or critical-path hypotheses is critical and starts a full
round immediately, subject to the coalescing rule below. A new promoted entry
alone does not force a whole-portfolio rescan. Other events start a full round when they
materially change the global ranking; otherwise they receive a micro-round.

The September6 12:55Z48-hour trial ended September8 12:55Z. The September8
2220 synthesis continues its scoped-event rule: routine scoped lemmas and
instrument instantiations receive targeted review plus the theorem-interface
composition pass, not an automatic full scan solely because promotion is new.
Observed benefit includes15i's avoided identical echo scan; no controlled
throughput estimate or complete avoided-scan census is claimed. The missed
trial checkpoint and interruption/cadence debt remain recorded in notes.
This changes no hostile-review gate, critical scope-reversal response, or
12-hour completed-round backstop. Track avoided duplication, integration
time and review latency with existing records; revert if important cross-route
consequences are missed. Record the ranking/critical-path assessment for
each micro-round. Prepare invitations while root writes its blind, but do
not invite before root's seal or retroactively reset a frozen deadline.

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
   Every whole-portfolio model in the swarm's roster is invited automatically
   to every full round. Each receives the
   same sealed packet, submission contract, tool boundary, and deadline, and
   must submit before seeing any other lane's report.  Every submission
   receives equal post-deduplication consideration: model identity is neither
   a bonus nor a vote, and operational unavailability degrades but does not
   block the round.
3. **Required submission contract.** Each report gives:
   - a compact disposition vector over every numbered avenue: `unchanged`,
     `raise`, `lower`, or `reopen`, with reasons for every change;
   - a reranking of the principal proof and disproof bottlenecks;
   - one genuinely new mechanism, or an explicit `NO_NEW_MECHANISM` with
     evidence that the best use of capacity is an existing unresolved target;
   - at least one new connection between existing avenues;
   - the strongest proof attack and strongest counterexample/falsification
     attack;
   - one software acceleration or decisive experiment;
   - a short campaign-systems check, independent of the mathematical software
     proposal: either an `UPGRADE` card with the smallest useful test or
     implementation, or `NO_CHANGE` with evidence.  Rotate across state
     freshness, context and retrieval cost, claim/review propagation,
     duplication, model routing and utilization, adapter reliability, compute
     scheduling and cost, reproducibility, and operator/chat-summary quality;
   - no more than three detailed idea cards, each with explicit dependencies,
     cheapest discriminator, interpretation of each outcome, stop condition,
     and expected information gain;
   - a `continue / redesign / stop` recommendation for current major lanes.
4. **Deduplicate after collection.** Fingerprint ideas by target obstruction,
   mechanism, object, and decisive test. Merge operational duplicates while
   preserving independent origins, disagreements, and genuinely different proof
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

**External maximum-degree overlay (September6 12:42Z).** In addition to the
gcd theorem, GGHV arXiv:2204.14178v1 excludes characteristic-zero polynomial
Keller counterexamples with actual maximum total degree below108. Primary
applicability is recorded in AUDIT17(jjjjjjjjjjjj), with imported reduction
dependencies remaining externally trusted. Thus actual99/66 is closed despite
passing the gcd screen. Do not turn the paper's normalized sub125 pair list
into an arbitrary-representative filter, or apply this bound to partial-y
degrees with unbounded total degree or to Laurent/J=x^k charts. The installed
overlay has passed the scoped different-model Astra review of Sol's code
(xmodel/frontier-external108-root-gate-astra-20260906.md);
its legacy verdict remains gcd-only and overall_verdict combines both bounds.
The manual external check remains mandatory for actual source-degree
declarations and literature beyond the implemented bounds.
An inconclusive tool verdict never
certifies openness against unimplemented theorems. No frontier rerun of99
is authorized; a method control needs a named client and strict stop condition.

## Capacity allocation

Default portfolio targets, adjusted when evidence demands it:

- 45% strongest current critical paths;
- 25% new avenues and cross-avenue connections;
- 12% adversarial review and replication; the promotion gate is never queued
  behind frontier work;
- 10% software, instruments, and bounded campaign-system improvement;
- 4% external intelligence;
- 4% state integration.

These are the September 2 resolution-first defaults, superseding the older
35/20/20/15/5/5 allocation. Formalization remains non-blocking and outside the
separate repository's inspection boundary.

### Global-gap-first guard (September13, user-directed)

- Protect at least half of the strongest frontier-research time for
  all-degree proof mechanisms or genuinely new counterexample constructions,
  even when finite-family work is productive. Necessary FIRST review and
  bounded engineering are separate allocations, not excuses to consume this
  protected research time. Assess time, not report or lane counts.
- Before commissioning work, check the relevant canonical history. State
  the missing implication on an explicit route to a complete proof or genuine
  counterexample, its unresolved dependencies, and the cheapest decisive test.
  Prefer obtaining the missing actual-source hypothesis to extending an
  identity or conditional theorem whose closing gap is unchanged.
- Incremental work earns one bounded tranche, not an automatic successor.
  Renew it only when the result changes the next decisive test or removes a
  named dependency on that route. After two tranches leaving that bridge and
  test unchanged, pivot to an orthogonal mechanism even if new lemmas accrued.
  Count setup, retries and review against the same bottleneck's opportunity
  cost; new job tags, methods or preflight versions do not reset this rule.
  Delegate routine execution upkeep so it cannot silently replace the
  coordinator's protected global-gap research.
- Do not reverify accepted bounds or foundations, including the recorded
  degree>=125 result, without a specific doubt affecting a current
  load-bearing use. One different-model FIRST remains required for new claims.

Record these decisions in the existing LIVE STATE/claim queue; add no new
approval process or ledger. Already-live tasks retain their bounds; their
completion does not authorize more finite-family work.

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

1. `git fetch` the campaign repository and reconcile, then read the newest
   `LIVE STATE` and any events since it;
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
8. append findings, corrections, dead ends, costs, and decisions to the swarm's
   notes file (root `notes.md` for swarmHQ, `team/<name>/notes.md` otherwise),
   then append a fresh `LIVE STATE` block.

September6 resumption rule (1435 round's collection-delay micro-round):
check overdue terminal collection and exact process/cap obligations before
starting new exploratory work. A wall-clock target is not an assistant-wake
guarantee: keep detached job caps independent of coordinator presence, bank
the actual next collection owner, and report missed checks without resetting
clocks. Use the existing LIVE STATE queue; no second scheduler/ledger is implied.

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
- Exact mathematical integers/rationals cross orchestration as raw bytes or
  decimal strings, never through JavaScript native-number JSON roundtrips.
  Recheck retained values against exact computations, not just file hashes or
  no-float types; a rounded integer can also be wrong. This repairs the specific
  September6 B-witness export failure (AUDIT17(ppppppppppppp)), not a claim that
  all historical artifacts have been audited. Preserve erroneous frozen bytes
  with an explicit erratum and a separately pinned replacement.
- A claimed `python -O` or `-OO` verification is admissible only when every
  load-bearing check remains live in that mode. Freeze an AST scan showing no
  `Assert` nodes in the verification paths (or prove that any remaining
  asserts are non-gating diagnostics), and run a deliberate old-pass/new-fail
  mutation under every claimed interpreter mode. Byte-identical positive
  output alone is insufficient: stripped checks can print the same answer
  vacuously. Ordinary-only scripts may use `assert` only when the report labels
  that limitation and makes no optimized-mode evidence claim.
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
- Run heavy or uncertain-duration computation on a cloud machine, never on the
  machine that runs the coordinator. Where those machines are, how they are
  launched, capped, and stopped, and which launcher a lane uses are swarm
  policy, recorded in `team/<name>/README.md`. Every lane prompt carries the
  current `FALLACY-v2.md` guardrail, and a report that asserts a new exit price
  declares `charge_basis={...}` exactly as that file specifies.
- `jc2-lean` is a separately owned nested repository and is outside the
  campaign's inspection boundary. Campaign agents must not enter, enumerate,
  search, read, build, status, modify, or control it. Scope every parent Git
  query explicitly away from that path; never stage its gitlink. The parent
  `.ignore` excludes it from ripgrep-style broad searches. Concurrent local
  formalization may consume shared CPU/RAM, but campaign contention checks
  remain system-level and must not identify or inspect that nested workload.
- Third-party tools may mutate shared CLI configuration; adapters must isolate
  or sanitize it, and a new/updated adapter gets a smoke test before use.
- Lane launchers take prompt files, reject duplicate live tags, record their
  true exit status, and keep one task and deliverable path per tag.  Every
  model-review prompt names exactly one report path whose basename matches the
  lane tag, explicitly instructs the reviewer to write that file and no other,
  and is smoke-checked for that destination before launch.  Referee text left
  only in adapter stdout is a failed-delivery draft, not promotion evidence;
  preserve it and rerun through a fresh output-explicit prompt.
- A campaign win requires a global proof or an explicit characteristic-zero
  counterexample at its honest evidence tier. Failure of selected formal
  families to algebraize, or closure within one book/chart/degree range, is
  not by itself a resolution of JC2.

## Resolution-first directive (2026-09-02, DC, standing)

The campaign optimizes for **resolving JC2**, by proof or counterexample.
Verification exists to keep the probability of building on an unsound
foundation acceptably low — not to maximize assurance. Deep verification and
formalization are post-resolution work; resources for them will be ample if
we succeed. Concretely:

1. **Verification calibration.** One different-model hostile review still
   gates promotion (unchanged). Beyond that gate, additional hardening of
   already-promoted results (re-reviews, independent re-derivations,
   formal-adjacent replication) is DEFAULT-OFF unless the result is
   load-bearing for the current frontier AND a specific doubt is named.
   The N=4 foundation (repaired Domrina chain + the campaign's independent
   kill chain, all pair-reviewed) is assessed acceptable; do not spend
   frontier capacity re-hardening it.
2. **Speculative-parallelism caps loosened** (rationale: the caps were sized
   for a smaller fleet and maximal-assurance posture): at most **six** active
   provisional roots campaign-wide; at most **three** child lanes per
   provisional claim; the 25%-on-one-unreviewed-claim guard and the
   review-before-first-descendant rule are unchanged.
3. **Capacity allocation defaults** shift to: 45% strongest critical paths;
   25% new avenues and cross-avenue connections; 12% adversarial review and
   replication (floor: the promotion gate is never queued behind frontier
   work); 10% software/instruments; 4% external intelligence; 4% state
   integration. The review-debt slot reservation rule is unchanged.
4. **Ideation rounds keep hunting new paths.** Endorsement of named critical
   paths never narrows the round contract: every round still requires new
   avenues and cross-connections, weighed on merit against current paths in
   `APPROACHES.md`. Historical named flagships are not standing assignments.
5. **Formalization is non-blocking** in every direction: never wait on it,
   never gate a launch on it, and keep it outside the inspection boundary.
6. **Proactive surfacing.** The coordinator surfaces acceleration blockers
   (quota, seats, custody, instruments) to the human operator as they arise, in the next
   user-visible message — never batched behind a question from the operator.

## Bootstrap for a fresh coordinator

1. `git fetch` the campaign repository. Read this file, `README.md`, your
   swarm's `team/<name>/README.md` (for swarmHQ it carries the current handoff
   and entry points), the newest `PROGRESS.md` entry, the current reading guide
   and cited corrections in `AUDIT.md`, and all of `APPROACHES.md`. The
   historical 46-avenue catalog is linked from `APPROACHES.md`; old overlays
   and model scores are not current launch instructions.
2. Read `notes.md` from the bottom through the newest `LIVE STATE` and all
   later events. Historical `STRATEGY` and `STANDING QUEUE` blocks are
   provenance, not current policy.
3. Check the campaign repository's explicitly scoped status and basis commit,
   excluding `jc2-lean` without inspecting it. Sweep exact local lane tags and
   the machines listed in your team folder; harvest before relaunching anything.
4. Resolve overdue review, ideation, and web-sweep clocks. Continue the outer
   loop. Never silently promote, publish, spend beyond authority, or discard
   another lane's work.

## Lane report contract amendment: seal-at-completion (2026-08-31 17:35Z)

Two lanes returned sealed skeletons on 2026-08-31 (a provider ended its
turn after writing the skeleton; a 128K-output-cap kill mid-response),
because the previous template had lanes write the `<!-- BODY-END -->`
seal into the initial skeleton — making `report_state=BODY_SEALED`
unable to distinguish a finished report from a crashed one.

Binding contract for every future lane prompt:

1. The skeleton written as the lane's first action MUST NOT contain the
   `<!-- BODY-END -->` marker.
2. Sections are appended as separate bounded writes (target under
   ~1,500 words per write; never the whole report in one response).
3. The standalone `<!-- BODY-END -->` line is appended only after the
   final section is on disk, with nothing after it.
4. If the budget runs short: finish the current section, type every
   remaining section OPEN in one short paragraph each, then seal.

Under this contract, `PARTIAL_NO_MARKER` correctly identifies crashed
or under-delivered lanes, and the divert machinery banks their partial
content. Coordinator-side: a `BODY_SEALED` receipt no longer implies
substance; harvest still requires reading the report. Queued ops debt
(nonblocking): a divert heuristic flagging sealed reports whose
sections are empty.

## Authoring rule for raised OPENs (2026-09-02, coordinator, after the collision-check upgrade)

Every report that raises an `OPEN[...]` states, on the same line or the
next, the QUANTITY it asks to bound or decide (e.g. "bound U in terms of
e", "decide whether F^{-1}(c) is empty"). `ops/open_collision.py` (the
round-20260902T0741Z systems upgrade) fails closed on an OPEN without
such a description; run it on a report before sealing and keep its
COLLISIONS block. Collision hits are review candidates, never closures.
Realization jobs at N >= 6 launch only after `box/preflight.py` returns
exit 0 on their manifest (the encoding-faithfulness hard gate).

## Authoring rule amendment: cheapest test (2026-09-03, coordinator, round 20260903T1015Z systems upgrade)

Every raised `OPEN[...]` states, beside its bounded quantity, its CHEAPEST
TEST: the instrument, the gate, and a wall-clock estimate (one line). At
round freeze the coordinator attempts every live OPEN whose cheapest test is
under one lane-hour before setting the round's questions. Rationale: two
OPENs that were twenty minutes from resolution (PROP-5.6-SHADOW,
MAJOR-MULT) sat unattempted because the ledger could not tell them from
flagship-sized ones. `ops/open_collision.py` is not changed (older reports
stay valid); the field is checked by the coordinator at harvest.
