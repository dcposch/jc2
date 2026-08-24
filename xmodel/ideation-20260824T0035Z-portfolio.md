# Post-round portfolio — full-spectrum ideation `20260824T0035Z-2386780`

**Portfolio producer:** Nash / `/root/outerloop_critic`
**Frozen inputs:** `root` `9aa6e4c2…`, `bacon` `bfa0b026…`, `averroes` `46f5afee…`, `nash` `bebb4042…`, `grok2` `fa17f110…`
**Scope:** execution plan only; no claim is promoted here and no shared ledger is edited.

## Decision

Run four roots total, counting coordination. Only one root may consume an unreviewed mathematical claim, so provisional exposure is exactly one root out of four (25%). Three worker roots run beside the coordinator; the second proof experiment is a stage of the proof root, not a fifth root.

The five blind reports independently support the same ordering:

1. replay the strongest external certificates exactly;
2. discharge the overdue independent review of `D43-NF-FID`, then test a source-defined depth transition rather than increase the fixed depth;
3. run a cheap boundary-invariant control experiment before building a theorem programme;
4. preserve one orthogonal, genuinely new global proof mechanism—the trace-regularity criterion—as the proof root's second stage.

This is not a vote. The ordering is by information gained per hour, ability to kill a route cleanly, and reuse of exact tooling. The GGV/Sigray fingerprint, common-integral D43 compiler, cCa expansion, and all larger fixed-depth computations remain queued or held until one of these gates supplies the missing reason to run them.

## Four-root envelope

| Root | Role and launch state | Owner | Independent reviewer | Unreviewed premise exposure |
|---|---|---|---|---|
| **C — coordinate/harvest** | **NOW.** Dispatch, enforce gates, hash artifacts, maintain the dependency view, and trigger the next round. It produces no mathematical child. | Sol Ultra (`root`) | Mechanical hash check; human only for irreversible/public action | none |
| **E — exact external evidence** | **NOW.** Pin, replay, and crosswalk the Guo and SuperMind claims into a common certificate IR. | Bacon | Grok 2, after the D43 review; review is required before promotion | none: DRAFT claims are objects under test, not premises |
| **D — depth-transition discriminator** | **NOW.** First perform hostile review of `D43-NF-FID`; then, within this same root, test a source-defined `D25 -> D27` transition/symbol gate. | Grok 2 for review and transition experiment | Nash for any new Grok-produced transition claim | `D43-NF-FID` only: 1/4 roots = 25% |
| **P — global proof discriminator** | **NOW:** P1 boundary passport/control probe. **QUEUE in the same root:** P2 trace-regularity probe after P1 stops or finishes. | Averroes (P1), then Nash (P2) | Grok 2, only for a candidate claim that passes its producer gate | none: promoted exact boundary facts only |

At most these four root identifiers exist during this portfolio. A stage handoff changes the owner of an existing root; it does not open another root. No root has more than two children, and no chain may exceed one unreviewed dependency generation.

## Dependency DAG

```text
                         promoted D25 certificate
                                  |
D43-NF-FID [PROVISIONAL] --> D0 hostile review ----+
             (only D is exposed)                  |
                                                   v
                                          D1 D25->D27 source
                                          transition/symbol gate
                                                   |
                           CONFIRMED + typed map only
                                                   v
                                  [QUEUE] common-integral D43

Guo/SuperMind [DRAFT] --> E pin/replay/crosswalk --> review --> possible promotion
                         (no descendants this cycle)

PBJ + HENON + CLASSKILL [PROMOTED exact controls]
                         |
                         v
                P1 boundary passport probe
                         |
                  code/schema reuse only
                  (not a truth dependency)
                         v
                P2 trace-regularity probe

P1 schema --tool-only--> [QUEUE] PSC fingerprint
```

Dashed or “tool-only” reuse never licenses a mathematical inference. In particular, P2 may reuse parsers or compactification data from P1 but must restate and independently verify every mathematical premise. E's provisional findings may change priorities, but no proof or disproof branch may cite them before independent review.

## Parallel launch order

### T0: launch immediately

1. **C:** issue frozen prompts containing only the relevant packet, exact input hashes, output paths, timebox, and verdict vocabulary.
2. **E:** begin provenance pinning and the shortest upstream verifier for each external source.
3. **D0:** begin different-model hostile review of `D43-NF-FID`. This is the highest-priority review debt.
4. **P1:** begin the boundary control probe from promoted artifacts only.

This fills the coordinator plus three research/review slots. Work outside D continues while D0 is reviewed; nothing waits merely because review exists elsewhere.

### First completion or stop

- If **D0** finds no fatal mismatch in its rapid triage, D remains open and proceeds to D1 after the full verdict. D1's `D25 -> D27` part is independently grounded in promoted D25 and may be prepared without treating D43 as true. A common-integral D43 child may not launch until D0 is `CONFIRMED`.
- When **P1** finishes:
  - if it produces a non-tautological candidate obstruction/source lemma, P2 is held and the P root packages the candidate for Grok review;
  - if it returns `COSTUME`, `NEGATIVE`, or a reusable schema without a claim, hand the same P root to Nash and launch P2 immediately.
- When **E** finishes, freeze its artifacts and queue review. Do not occupy a live research slot merely waiting for that reviewer; C may already use the result as an event signal, not as a mathematical premise.

### Continuation discipline

An initial gate may receive one extension, at most six additional hours, only if it has already produced (i) an exact artifact, (ii) a sharply stated remaining question, and (iii) an estimated completion under the extension. C may authorize only one such extension at a time. Otherwise stop, record the discriminator, and recycle the slot.

## Root E — exact external evidence

### Question

Do the external claims reproduce from pinned public artifacts under their stated hypotheses, and are they genuinely independent certificates rather than differently named copies of one underlying computation?

### Six-hour gate

1. Pin URLs, commits/releases, manifests, environment versions, and hashes. Missing provenance is itself a `GAP`, not permission to reconstruct intent.
2. Run the shortest claimed upstream verifier before inspecting bulk output.
3. Recompute at least one representative exact identity from source data; do not accept screenshots, prose summaries, or success banners.
4. Encode claim, assumptions, polynomial normalization, certificate payload, and checker relation in one minimal IR.
5. Crosswalk each external statement to our claim IDs. Explicitly mark common files, common mathematical cores, and non-independent certificates.

### Verdicts and stops

- `PASS-EXACT`: pinned source plus an independently replayed exact identity and complete assumption map.
- `FAIL-IDENTITY`: a claimed exact identity fails; preserve the smallest counterexample and stop bulk replay.
- `GAP-PROVENANCE`: source, manifest, definition, or normalization is not recoverable within two hours; stop rather than guess.
- `DUPLICATE-CORE`: multiple public claims reduce to the same certificate lineage; count the evidence once.

Do not read or replay the full large corpus after a failed short verifier. Do not publish, contact an author, or change a public claim without human authorization.

### Exact outputs

- `cases/round1_external_cert/check_certificate_ir.py`
- `cases/round1_external_cert/lineage.json`
- `cases/round1_external_cert/replay_results.json`
- `xmodel/round1-external-certificate-20260824.md`

The report must contain exact commands, hashes, per-claim verdicts, and a minimal failing witness where applicable. A producer `PASS-EXACT` creates review debt; it is not promotion.

## Root D — review, then transition rather than depth

### D0: hostile review of `D43-NF-FID`

Grok 2 receives the frozen artifact, generator/source dictionary, and producer commands. It must attack the following separately:

1. type and source consistency of the variables and equations;
2. the definition of “non-origin” and the saturation/localization used to enforce it;
3. the rank/minor/Fitting criterion and its relation to the claimed nonvanishing locus;
4. reproducibility at a fresh admissible point and prime, not merely replay of stored output;
5. whether the conclusion is exactly the claimed one or a stronger extrapolation.

Return exactly one of `CONFIRMED`, `GAP`, or `REFUTED`, with the first irreducible defect if not confirmed. Rapid triage is due in 90 minutes; the frozen review is due in six hours.

**Output:** `xmodel/round1-d43-nf-fid-review-20260824.md`.

### D1: source-transition/symbol gate

After D0, test whether the source recurrence actually defines a typed relative map from the promoted D25 system to the next source-supported depth (nominally D27). Generate only the new equations/unknowns and compute the relative linearized symbol or Fitting data at at least two admissible non-origin samples and two good primes.

The gate asks a binary structural question before any larger solve:

- `FINITE-TYPE-SIGNAL`: the new symbol closes or stabilizes the free tail in a coordinate-stable way;
- `FREE-TAIL-SIGNAL`: a persistent positive-dimensional kernel survives and is not a gauge/coordinate artifact;
- `NO-TYPED-MAP`: the source does not supply a coherent transition; stop the tower interpretation;
- `INCONCLUSIVE`: sampling or implementation cannot distinguish these within the timebox.

Stop after two hours if the source projection/transition cannot be typed exactly. Stop after six hours even if more primes or depths look attractive. `FREE-TAIL-SIGNAL` is a successful route-killing result, not a request for D75.

### Exact outputs

- `cases/round1_dtransition/transition_symbol.py`
- `cases/round1_dtransition/samples.json`
- `xmodel/round1-dtransition-20260824.md`

Only `D0=CONFIRMED` plus a typed, informative D1 result may queue a common-integral D43 emission. Even then, the D43 integral/smooth witness is a new task with a new timebox; B=168 and D75 remain forbidden.

## Root P — two sequential global proof discriminators

### P1: boundary passport/control probe — NOW

Build the smallest exact representation that can simultaneously express the logarithmic coframe/primitive data and the first Fitting/Smith data of the pure-boundary cokernel. Evaluate it on a pre-registered control panel:

1. elementary and tame automorphisms;
2. the exact Hénon control;
3. the exact class-kill family;
4. one residue-A leading-pair specimen for which every required input is already certified.

One explicit blow-up chart is enough for this gate. The point is not to prove the boundary theorem; it is to learn whether the proposed invariant sees more than the determinant identity and whether it is stable under harmless coordinate/chart changes.

Verdicts:

- `CANDIDATE`: a nonzero, coordinate-stable invariant separates at least one control class for a mathematically explained reason;
- `COSTUME`: the output reduces to the known determinant/leading-form identity, changes under harmless presentation, or adds no information;
- `SCHEMA-ONLY`: the representation is correct and reusable but current certified data are insufficient;
- `INCONCLUSIVE`: exact implementation fails within six hours.

On `CANDIDATE`, stop theorem development and package the smallest claim for review. On `COSTUME`, do not add a new boundary avenue under another name.

**Exact outputs:**

- `cases/round1_boundary_probe/boundary_passport.py`
- `cases/round1_boundary_probe/control_results.json`
- `xmodel/round1-boundary-passport-20260824.md`

### P2: trace-regularity probe — QUEUED in P

If P1 does not create an urgent candidate review, hand P to Nash. First prove, with every algebraic hypothesis stated, the conditional reduction:

> regularity of the power traces needed by Newton identities forces `x` and `y` integral over `k[P,Q]`, after which the constant-Jacobian finite map is finite étale and hence an automorphism.

Then derive the principal-part condition for the first trace that can acquire a pole at infinity, and test it on the same exact automorphism controls plus at least one generically finite nonproper polynomial map. This is a discriminator for whether the current boundary data can force trace regularity, not an invitation to announce the conditional lemma as a proof.

Six-hour stops:

- `SEPARATING-IDENTITY`: an exact boundary identity cancels the automorphism poles and fails on the nonproper control;
- `INSUFFICIENT-DATA`: branch pairing or trace principal parts cannot be reconstructed from the promoted boundary package;
- `FORMAL-COUNTERMODEL`: a certified formal escape model satisfies every input used by the proposed argument while retaining a trace pole;
- `INCONCLUSIVE`.

`INSUFFICIENT-DATA` must name the smallest missing datum; it becomes a candidate target for PSC fingerprinting. `FORMAL-COUNTERMODEL` kills the proposed implication from those inputs.

**Exact outputs:**

- `cases/round1_trace_probe/trace_poles.py`
- `cases/round1_trace_probe/control_results.json`
- `xmodel/round1-trace-regularity-20260824.md`

P2 may reuse P1 code and schemas, but not an unreviewed P1 proposition. Thus it creates no second-generation speculative dependency.

## Review debt and promotion gates

| Priority | Candidate | Producer | Reviewer | Due / preemption rule | Descendants before review |
|---|---|---|---|---|---|
| 0 | existing `D43-NF-FID` | Sol Ultra | Grok 2 | T0 + 6h; already load-bearing | D root only, at 25% exposure; no common-integral child |
| 1 | D1 transition/symbol claim, if informative | Grok 2 | Nash | before the next full round or before any depth child | none |
| 2 | E exact external certificate, if `PASS-EXACT` | Bacon | Grok 2 | before promotion or public use; may preempt P review if externally consequential | none |
| 3 | P1 boundary candidate | Averroes | Grok 2 | before theorem development; P2 is held if P1 is a candidate | none |
| 4 | P2 separating trace identity | Nash | Grok 2 | before any proof child | none |

Only candidates that pass their producer gate enter review debt. Failed discriminators and schema-only tooling are checked for reproducibility but do not consume a hostile mathematical-review slot. At most one unreviewed load-bearing candidate may be pending per root. If Grok review debt exceeds two surviving candidates, halt new proof children and use the next Grok slot to retire the oldest/highest-exposure item.

No result from this portfolio is written to `AUDIT.md`, `PROGRESS.md`, or a promoted bank until the required independent review and exact artifact checks are complete.

## Queue and hold

### Queue, but do not launch now

1. **Common-integral D43 / smooth-witness compiler:** only after D0 confirmation and an informative typed D1 transition.
2. **PSC fingerprint / `G2-PSC`:** only if P1 or P2 identifies a precise valuation datum absent from the pure-boundary package. Treat GGV and Sigray as a fork until then, never as a hybrid source.
3. **Certificate-lineage generalization:** only after E's minimal IR replays at least one external and one internal certificate.
4. **Sparse cCa cofactor pilot:** only if E finds that an external result depends on a missing cofactor map that this pilot can supply.

### Hold for this cycle

- B=168, D75, and every larger fixed-depth solve;
- more DIR/KJN/A-SCALE case expansion or unification;
- full cCa6/F4 elimination, HC4 expansion, or an msolve upgrade campaign;
- new literature/book sweeps not tied to a named missing lemma;
- public claims, author contact, or external commitments without human authorization.

The hold list is released only by a gate above or a significant external event, not by idle capacity alone.

## Harvest contract and stop criteria

Every root report must include:

- exact input hashes and commands;
- one standardized verdict from its gate;
- mathematical dependencies separated from code/schema reuse;
- smallest witness or first failing check;
- wall-clock/compute cost and estimated cost of the next step;
- route-ranking effect: advance, hold, kill, or no change;
- any new review debt.

C stops a root when its pre-registered discriminator has answered the question, even if the answer is negative. It also stops a root for untyped source data, unrecoverable provenance, failure to produce an exact artifact by half-time, or a requested continuation that merely increases sample size/depth without changing the question.

The round is successful if it retires one ambiguity, kills one route, or produces one independently checkable new invariant. Number of files, equations, or agents is not a success metric.

## Next ideation and web triggers

### Full-spectrum ideation

- **Hard timer:** start the next blind full-spectrum round no later than `2026-08-24T12:35Z` (12 hours after this round's packet cutoff; if banking occurs later, use the stricter of that time and 12 hours after bank).
- **Start sooner** upon any of:
  - `D43-NF-FID` is `REFUTED` or its meaning materially narrows;
  - D1 returns a stable `FINITE-TYPE-SIGNAL` or `FREE-TAIL-SIGNAL`;
  - an external exact identity fails, duplicates another lineage, or verifies a claim that changes the route ranking;
  - P1 produces a coordinate-stable non-tautological invariant;
  - P2 produces a separating trace identity or a formal countermodel;
  - credible competitor news changes priority or apparent time-to-result.

A routine artifact that does not change assumptions or route ranking triggers a micro-review/harvest, not a fresh full round. Every researcher in the next full round again scans the entire avenue/gap/evidence landscape before applying a supplemental lens; packet summaries must not reveal other agents' rankings.

### Web/external intelligence

- **Broad sweep:** no later than `2026-08-24T21:25Z`, following the packet's last broad-sweep timestamp, and every 24 hours thereafter.
- **Targeted sweep immediately:** when E finds a new commit/release, a verifier fails, a cited source is missing, or a competitor announces a proof/disproof/certificate.
- Pin and hash before interpretation. External news may reprioritize work immediately, but mathematical dependence awaits exact replay and independent review.

## Capacity and contamination audit

- Four roots total: C, E, D, P.
- One of four roots consumes a provisional claim: 25% exposure, not more.
- Review is enqueued before any dependent child; independent roots never wait for it.
- P1 and P2 are sequential and mathematically independent; schema reuse is labeled.
- External claims are tested, never silently imported.
- A P1 candidate suppresses P2 to prevent branch explosion and review debt.
- D1 tests source transition before any larger depth, preventing compute momentum from masquerading as evidence.
- No same-model dual confirmation is counted as independent promotion; new Grok claims go to Nash, and OpenAI-produced claims go to Grok.

This portfolio should be rebalanced at the first decisive gate, not merely at the timer.
