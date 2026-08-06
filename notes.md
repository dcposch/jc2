# JC₂ campaign — high-level notes

(Working notes per DC's request: avenues, decisions, findings. Not a paper draft.)

## Where things stand (2026-07-28)
- (72,108) is the sole open Newton-polygon family below degree 125 (GGV 2022).
  We reduced both its subcases to small "cores" (30 and 73 vars) via:
  direct polygon transcription → torus normalization → gauge analysis
  (Q determined by P modulo explicit gauge) → bilinear b-elimination cascade.
- Pipeline validated on the solved (66,99) subcase: EMPTY [1] in 2.3s at p=65521
  (two machines, independent builds). Raw formulations of the same case need
  600-850 GB — explains why this sat unresolved since 2022.
- Line probe (validated on solved case): open subcase (2) has NO codim-1
  solution family at p ∈ {65521, 1048573, 2147483629}. Remaining outcomes:
  empty-with-deep-certificate, or small deep solution locus (= candidate
  counterexample towers).
- Verdict pending: msolve on the open cores (fleet: ultramem-1 + jc-b).
  Spot preemptions are the operational enemy; ~20h jobs lost twice.

## Avenue map (approved 2026-07-28)
1. **(72,108) resolution** — in flight. Either bound→125 (after char-0
   certificate + reduction audit) or first-ever live counterexample lead.
2. **Family farm** — approved. Automate GGV family enumeration → same pipeline
   per family → sweep all families to degree ~150-200 on a Spot fleet.
   Exclusion and search are the same computation. Prereq: validate Generator A
   on unreduced family data (§4 hand-reductions are the non-automated step).
3. **Algorithmic levers (my queue)**: left-kernel obstruction ideal (pure
   a-space, 18/24 vars); Cascade3 level-order fixes for (9,27)/(7,21) [G0
   completion]; plane probe (codim-2 test); engine diversity (Singular/M2/
   HC.jl) when quota allows.
4. **Proof-side threads (background)**: Conjecture E (Lee–Li remainder
   vanishing) — test low-degree instances computationally; Żołądek sheet-bound
   extension feasibility (chart case-analysis = agent-parallelizable);
   Zheglov DC₁ verification (would close the ¬DC₁ route).
5. **Not doing yet**: paper draft (per DC); Lean certificate formalization
   (post-verdict); GPU anything (no mature engine).

## Operational decisions log
- Spot-vs-on-demand: M3 quota = 96 vCPU global (ultramem-1:64 + jc-b:32 = at
  ceiling). On-demand M3 also capacity-blocked in us-central1-a. → QUOTA RAISE
  NEEDED for family farm (ask: M3 CPUs 96→512, or N2 equivalents).
- Preemption mitigations: redundant racing of the critical job on independent
  instances; @reboot resume; auto-restart guard; -v 2 progress files.
- All boxes self-poweroff when their queue drains (QUEUE_DONE marker).

## Open questions / risks
- Is the open-c2 core's grind "fat empty certificate" or "deep small variety"?
  (Line probe can't distinguish; msolve will.)
- Cascade3-over-ℚ soundness audit + G0 string identities still owed before any
  public claim (postverdict.md).
- Prop 4.3 (§4 reduction) is trusted from the unrefereed GGV chain; the direct
  raw-polygon runs (char-0 lane) provide partial independence.

## 2026-07-29 loop notes
- G0 sweep result: NO level direction (10 tried) completes Cascade3 on
  (9,27)/(7,21) — structural, not tuning. G0 stands at 3/5 solved families
  validated (both (9,24) forms + (8,28)-machinery); remaining 2 families
  emitted as partial-core fleet jobs instead (sound mid-cascade states).
- Open-case structure signal: complement chart (pivot-monomial = 0 branch) is
  HARD locally (>1h) where the regression analogue was instant — third
  qualitative difference between open and solved cases (after core hardness
  and fat memory).
- Plane probe (agent-built, gate-validated incl. planted-solution tests):
  open_8_28_c2 has NO codim-2 solution family at p=65521 (10 planes) and
  p=1048573 (2x5 planes); with the line probe, any solutions have codim >= 3
  in the 24-dim a-space. Empty-with-fat-certificate hypothesis strengthens.
- Farm prereq verdict: unreduced (48,64) family = 1314-var bilinear system;
  Cascade3 manages only 43/830 b-eliminations before swell (73 min). GGV's §4
  reductions are load-bearing. Farm routes: (a) automate §4 (edge-form
  factorization + corner-cutting automorphisms — the real prerequisite), or
  (b) raw unreduced systems directly on big-memory msolve — test queued on
  ultramem-1 (moh_48_64_raw, solved family = safe validation).
- 2026-07-30 (UTC) MILESTONE: open_8_28_c2 chartG (generic chart, 27 vars) =
  EMPTY [1] mod 65521 on jc-b, sub-second, verdict authenticated (proper F4
  header + full var order + basis length 1). Half of open subcase (2) decided
  at one prime. Remaining: complement = core + (a2=0 or a6=0) — split into
  two explicit sub-branch systems (cCa2, cCa6), racing locally + on jc-b's
  queue (unsplit). Then: other primes (queued), strict variant, subcase (1),
  char-0 for certificate grade.
- jc-b post-mortem: the "wedge" self-resolved via reset + one silently
  successful repoint attempt; giant-core jobs remain banned on 976GB boxes.
- Conjecture E (Lee-Li remainder vanishing): first computational verification
  of the 7 smallest instances ((a,b,m,n)=(2,3,2,4), delta=1): 6 HOLD with
  char-0 Groebner certificates + agreeing mod-p lane, 1 degenerate, 0 fail.
  Gate on commuting-pair fixture passed (automorphism pairs cannot realize
  these polygons by Abhyankar divisibility — commuting pairs are the right
  gate). lib/conjE.py, runs/conjE_results.txt. Evidence FOR the E=>...=>JC2
  program route. Next tier of instances is a scale-up when compute frees.
- 2026-07-30 AUDIT MILESTONE: the generic-chart emptiness of open subcase (2)
  is a SYMBOLIC theorem-fragment, not an F4 result: the cascade+chart
  substitution chain reduces original equation #3 (one explicit coefficient of
  [P,Q]-x^2) to the constant -1 on the chart locus. Independently audited at 6
  random exact-rational chart points (original equations + stored
  substitutions only; culprit = -1 at all points; 51/92 pivot equations
  vanish; no other constants). Valid over every field away from denominator
  primes. Regression contrast: the solved case's chartG has NO such collapse
  (needed real F4) — this shallowness is specific to (72,108) s2.
  TODO: extract which bracket position eq #3 is; write the substitution chain
  as a standalone lemma; attempt same for cCa2 (its char-0 [1] took real
  work; lift still running).
  Subcase (2) status: chartG EMPTY (symbolic+char-0+mod-p), cCa2 EMPTY
  (char-0+mod-p), cCa6 RUNNING (deg 12+, big box).
- 2026-07-31 MAJOR MILESTONE: open subcase (2) EMPTY at TWO primes across all
  three strata (chartG / cCa2 / cCa6 at p=65521 and p=1048573; cCa6 was the
  ~7h/48-thread nucleus each time). chartG+cCa2 also EMPTY over Q; chartG
  additionally by audited symbolic contradiction. Union of strata = full
  reduced variety of Prop 4.3 s2 => subcase (2) has NO solutions at either
  prime, pending: cCa6 char-0 (launching), strict variant (running),
  pipeline audit write-down. Subcase (1) = the remaining half of (72,108);
  chart decomposition being built now.
- 2026-08-01 MILESTONE: cCa6 EMPTY [1] over Q (17h43m, 761 GB peak, proper
  reduced-GB header). SUBCASE (2) OF (72,108) IS NOW EMPTY OVER Q IN FULL:
  chartG (symbolic + Q + 3 primes), cCa2 (Q + 3 primes), cCa6 (Q + 2 primes,
  3rd prime running on jc-b). GB=[1]/Q => empty over C. Conditional on:
  Generator-A transcription (regression-validated), Cascade3/two_chart/split
  soundness (numerically audited; formal write-down owed), msolve char-0
  correctness (+ multi-prime agreement), and GGV Prop 4.3.
  REMAINING for full (72,108) discard -> bound 125: subcase (1) (c1 core
  queued both boxes; chart decomposition blocked on two_chart swell guard),
  strict variant (1d1h in), audit paperwork + certificates.
- Strict-variant simplification: v6s (strict corner convention) died after
  ~1d2h, but is RETIRED as redundant: strict variety = nonorigin variety +
  extra origin-nonvanishing equations, i.e. a SUBSET — and the nonorigin
  subcase-(2) variety is proven empty over Q. Empty by inclusion; both polygon
  conventions settled for subcase (2) with zero further compute.
- AUDIT.md landed (410 lines): 8-claim soundness chain for "subcase (2) empty
  over char 0, conditional on GGV Prop 4.3", each claim with code citations +
  verification status; explicit trust boundary; remaining-obligations
  checklist (record pivot product from committed re-run; lemma write-downs;
  pin GGV arXiv versions; subcase (1) reserved for any bound-125 claim).
  Claim 2 torus algebra independently re-verified by hand.
- G0 deepened: solved case (9,24)-(3) EMPTY in 14/14 combinations swept by
  lane 1 (v6 core / chartG / chartC / strict x char-0 + three primes) —
  the pipeline reproduces known mathematics in every mode used for the
  open-case claims.
- 2026-08-02 LEMMA.md: the -1 collapse is a VERTEX-GAP OBSTRUCTION —
  vertex normalization a1*b3=1 vs gap-column death ((q0)_x=2) =>
  near-origin tower overdetermined by 1 => (unit)*a2^2*a6*b3 in I =>
  b3=0 contradiction. Chart-free: a2^2*a6 in I(core), DERIVING the
  cCa2/cCa6 split. Discriminator (q0)_x >= 2 sharply separates open vs
  solved family (verified symbolically both ways; eq3_chain.py committed).
  Valid char 0 + p outside {2,3,5,7,11,13}. Gaps: surplus condition not yet
  polygonal; c1's y-axis column breaks the mechanism (open there).
  FARM IMPLICATION: polygonal pre-filter candidate for family tables.
- SECTION4-AUTOMATION.md landed: §4 reductions ARE one algorithm, and it is
  COEFFICIENT-FREE (lattice arithmetic; RHS = x^(ceil(b/a)-2), matching all
  four props; subcase splits = root partitions + finite st-candidate lists).
  Agent-verified: reconstructed transforms reproduce all 7 emit.py polygon
  sets. Effort 2-3 weeks / 2-3 kLOC on lib/jc.py; regression gate = Props
  4.1-4.4 + the (8,32) discard. Farm now: quota + this implementation.
- LEMMA-REVIEW.md: 4/5 fronts CONFIRMED by independent recomputation
  (reproduction, geometry, chain soundness incl. fresh-point checks, prime
  hygiene {2,3,5,7,11,13} exact). Front 4 WEAKENED-and-improved: sharpness is
  side-symmetric (max((p0)_x,(q0)_x) >= 2); confound cell provably empty;
  swapped family also collapses; O(1) localization confirmed via toy family.
  Corrections appended to LEMMA.md. Mechanism STANDS.
- FACE-ISOLATION.md: Wilson GMC(2) port = partial-real (architecture matches
  slots JC2 already fills; disanalogy = infinite moment tower vs one bilinear
  identity). Transferable core = valuation-counting discipline; its TL1 is
  precisely our surplus-condition theorem (level filtration ~ p-adic
  valuation), verified on the c2 chain + a moment toy. Converges with the
  independent SURPLUS.md derivation in flight — cross-validate on landing.
- CROSSCHECK.md landed: THREE-WAY transcription agreement on Prop 4.3
  (Helali/Suzuki/ours; gauge-differences verified by hand). Both external
  artifacts cover BOTH subcases, both replays PASS (Helali 71s; Suzuki
  byte-identical 21.5s); our agent closed Helali's replay gap by proving his
  two untested identities. => bound-125 now rests on 2 external artifacts +
  our audited s2, with our c1 leaves as third replication (urgency reduced;
  a NONEMPTY leaf would contradict two artifacts = maximal alarm). Publication
  posture: cooperative (engage Helali, Suzuki, GGV; Leiden norms). c1-extract
  diff vs our core queued (crosscheck/c1_extracts/).
- SURPLUS.md v2: CONDITION (iii) PROVED from polygon data for the (k,d2)=(2,2)
  class (any strip lengths, char excl {2,3,5}) — includes (8,28). Props A/B
  (key/elimination counts) proved for ALL k,d2. Refinements: discriminator =
  leftover CONTENT not bare count (solved family counts 1 but leftover == 0);
  k>=3 breaks (iii) genuinely; wide strips: obstruction persists in non-
  surplus-1 form (4 leftovers, torus-empty numerically). Position rule:
  surplus key = w=1 stratum of Minkowski column k+2. Validation assertion-
  locked to the audited chain. Vertex-gap now fully polygon-theoretic in its
  regime. Next: adversarial review, TL1 cross-validation, then write-up.
- Ops: rev-order leaves deployed BOTH boxes (foreground file-based — the ssh
  failure law is now: complex inline commands flake, file-exec never has).
  Background gcloud-ssh loops retired permanently.
- SURPLUS-REVIEW.md: theorem CONFIRMED at variety level (scope map predicted
  4/4 fresh families; Props A/B independently re-derived; char {2,3,5} sharp;
  fix_ones-free). Errata applied: ideal-membership -> radical membership;
  content-discriminator marked observed-not-proved; TL1 scoped to (2,2) and
  superseded. VERDICT: SURPLUS+LEMMA ready for joint paper-grade write-up of
  the vertex-gap theorem in the (2,2) regime — awaiting DC's go-ahead per the
  standing no-paper-drafting instruction.
- ZHEGLOV-SCOPE.md: architecture mapped (GGV reduction -> head-chopping
  induction S4 -> string-equation transport S5 -> distinguished-coefficient
  contradiction S6). Top risk: S6 Steps 4-7 (rewritten in v4 AND v5) + the
  N-independence lemma. Machine audit lane ~45-75 agent-hours; expert lane
  3-5 weeks; paper under journal review (v5 thanks referees). Cheapest
  falsification (2-3h): random exact test of Lemma L:polynomials — launching.
- Zheglov T1 falsification test: Lemma L:polynomials PASSED 640/640 exact
  instances (4 regimes, 9 non-vacuous solvable cases matching deg H formula,
  48/48 solver controls). Kill-shot missed -> small confidence bump for S4;
  risk mass unchanged at S6 Steps 4-7 + N-independence. HOLDING at T1 (T2
  replay = 15-25 agent-hours, off critical path; escalate on anomaly or if
  DC(1) needed as citable). Artifacts: ZHEGLOV-LTEST.md, tests/ltest_*.py.
- SHEET6.md (P5): GO verdict — degree 6 ≈ 150-400 mechanizable exact-arith
  verifications (weeks-scale fan-out); wall (td 9 / bidegree (48,64)) is
  ABOVE 6. FOUND: Sigray 2008 thesis = independent degree-5 proof (RECON
  corrected). Caveats: both foundations unaudited; Żołądek gcd gap (GGV-
  documented). Pilot launched: machine-rederive Sigray Prop 9.1 + Stmt 9.6.
  USER ACTION WANTED: Żołądek PDF is CAPTCHA-walled — manual download needed.
- DC2-PROGRAM.md (P2): port-of-Zheglov blocked at step zero (centralizer
  rigidity collapses in A_2; prerequisite = 2D Schur-pair/Parshin theory,
  Zheglov's own open program; no Z^4 subrectangular reduction — vertex-gap
  slot). EXPERIMENT: DC(2) PROVED in Bernstein degree <= 2 (8s exact;
  deg-2 slice 0-dim of degree 90 = Lagrangian-cubic family over LGr(2,4) —
  geometry match; 5/5 operator-level certificates). Divergence at degree 3 =
  tier-1 next slice, queued. Full DC(2): unreachable at present.
- SHEET6-PILOT: Prop 9.1 exact PASS (11/11 rows, completeness certificates).
  Stmt 9.6 DISCREPANCY: thesis row (75,51) fails its own equation (p.52
  arithmetic slip, never-refereed source) — corrected statement drops the
  case, STRICTLY STRONGER; survivors {(21,15),(20,16)} verify. Degree-6 leaf
  table already emitted by the enumerator: 14 rows (< SHEET6's 20-30 est).
  Remaining for td=6: Props 9.3(e)-(m), lambda-budget, termination assembly.
- SURPLUS-EXT Phase C: surplus-4 variant THEOREM at (2,3) (dual proofs:
  resultant w/ constant lead + structural divisibility); torus-emptiness also
  proved at (2,4); rigidity certified (3,3),(4,3),(5,3). Pattern exact:
  leftovers = 2(w_P-1). DISCOVERY: log-residue functional R_{k,d2} =
  sum (-1)^j C(j,k+2) a2^(2d2-j) b_j survives per cell — PINS is its 1-term
  case; conjectured all k>=2,d2>=2; open (3,4),(4,4),(5,4),d2>=5. Erratum:
  scan's torus-solvable wide cells were numeric false positives (fixed in
  SURPLUS.md). Coverage: 0/34 current families in wide cells (theory
  completeness + beyond-150 relevance). P1 avenue now fully delivered:
  theorem grid (2,2),(2,3),(2,4) + k>=3 impossibility + coverage table.
- 2026-08-06 DECISION (DC): third replication of subcase (1) deprioritized —
  the deep cross-check (verified replays + closed gaps + 3-way transcription
  agreement) makes our own c1 Groebner runs evidentially marginal. Paper 2
  division: s2 ours end-to-end; s1 = external artifacts + our audit thereof.
  jc-b STOPPED. AWS Xeon Z-leaf + ultramem full-memory I-leaf continue as
  72h sunk-cost bonuses, then roll into sec4 Phase 2c / farm work.
- Xeon all-Z leaf FAILED at 940GB after 30h — every c1 leaf now exceeds 1TB.
  Xeon stopped (on-demand $, no viable leaf work); restarts for sec4 Phase 2c.
  Sole remaining bonus attempt: ultramem single-lane 1.7TB on I-leaves.
