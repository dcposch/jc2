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
- 2026-08-07: leaf program CLOSED (DC directive: novelty only). 8TB moonshot
  declined (~15% x replication value). Capacity reorganized: farm dispatch on
  review+driver gates; R residue-interpretation agent launched; sheet-6 build
  next slot; DC(2) deg-3 slice after. Lifts continue (paper obligation).

## 2026-08-07 (loop): residue theorem lands; farm gate-complete; leaf retired
- **RESIDUE.md committed (e67c50a)**: R_{k,d2} IS a Grothendieck residue — iterated residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary point {P=0}∩{x=0}. Three interpretations verified by exact arithmetic on 11 cells (48 checks): CT/contour form, Grothendieck form, Koszul moment functional spanning the reachable cokernel of ad_{xA}. Naive dP∧dQ/P^{k+2} refuted (exact form, residue ≡ 0). Uniform theorem all k,d2≥2: surviving outer extra = ±(k+2)/C((k+1)d2,k+1)·a2^{(k-1)d2}·R — explains every mystery unit (5,21,55,99,1001,364) as moments at top pivot; replaces per-cell certificates. conj:R now = its rigidity half only. Correction: sum starts j=max(k+2,d2).
- **Farm Phase 3 gate-complete**: driver agent hit the account credit ceiling (resets Aug 8 8pm PT) but deliverables were on disk; I ran gates locally — ALL FARM TESTS PASS incl GF6 (dry run reproduces S4 archives, 22 files byte-identical incl char 0, pivot product == AUDIT.md) and GF7 (dispatch covers 28 systems, balanced loads). deg≤150 sweep emission running locally under FLINT (13/~30 families done).
- **Ultramem I-leaf retired** (scp-script pattern beat the ssh-255 flake): lane4+msolve killed, cron removed. Rationale: replication, not novelty (user directive). cCa2/cCa6 Singular lifts untouched, still resident (~114 GB).
- **Blocked on credits until Aug 8 8pm PT**: sheet-6 case-bash build agent, DC(2) degree-3 slice agent. Local script work unaffected.

## 2026-08-07 (loop, later): deg<=150 sweep DONE; farm dispatch underway; credits restored
- Sweep final: 34 families, 62 .ms files (4.5 GB, largest 565 MB), 22 emitted-system cases + partials/cores. NOT COVERED (reduce4 STUCK, psi_j precondition / multi-root chain edge): 12_36mn23d144_r0-r2, 6_15mn27d147, 10_40mn32d150_r0-r1 — these stay open regardless of farm verdicts; candidates for a reduce4 extension later. PARTIAL/CORE emissions are valid (cascade steps are equivalences); they're just less reduced.
- Queues: --queues 2 -> box01 31 jobs/2.6GB, box02 31 jobs/2.2GB. Runner sorts smallest-first for early verdicts; NO guest poweroff (FARM_DONE marker + control-plane stop).
- Fleet: claude-x8i-3 restarted (new IP 54.175.21.169, 64c/991GB, msolve OK) <- box01 rsync in flight. jc-b restarted (32c/960GB, crontab wiped clean, msolve OK) <- box02 tgz in flight. ultramem-1 continues lifts only.
- Credits: user purchased more; probe confirmed live. Launched queued agents: sheet-6 case-bash build + DC(2) degree-3 slice (both in flight).
- Driver agent retired (its gates I re-ran locally: ALL FARM TESTS PASS, GF6 byte-identical vs S4 archives, GF7 dispatch cover).
- 2026-08-07: FARM LIVE — box01 (AWS Xeon 64c) + box02 (jc-b 32c), 62 jobs total, smallest-first; first EMPTY verdicts already in.
- SHEET6-CAMPAIGN.md: td=6 case-bash PHASE 1 COMPLETE. Built generic propagation
  engine (cases/sheet6_campaign.py; gate reproduces pilot exactly): ratio-eq
  Diophantine solver for all Prop 9.3 branches (I, IIa k>0/k=0, IIb, III) x mu|M,
  s-free reduction of parametric families w/ PIT certificates + s-shift, residue
  splitting, ceil-lambda budget BFS (Sigma lam <= td-2). Lambda<=7 table: 14 rows.
  VERDICTS (single-pole, conditional H1-H4+H3): td=6 rows 2,3 (both (2,3)-type)
  EXCLUDED; rows 6,8,9,11 reduce to ~14 case-III parametric s-tails (all s<=5
  instances die) + IV-terminals awaiting the root-kill H3. Two-pole 3+3 config
  OPEN (Prop 8.4 single-pole only). NEW THESIS ERRATA E2-E4: St 9.8/9.9/9.10
  "no solution"/"M_F=1" claims false (3nu=4m+1, 2nu=3m+1 families exist, lambda=0
  self-loops, M_F=2 via gcd(2nu,nu+1)). AUDIT FINDINGS: St 9.12's stated kills
  cannot close its own case-IV terminals (unstated root-kill = our H3, load-
  bearing G2); thesis silent on td<=5 rows 1,5,7,10 (rows 1,7 we closed
  mechanically; 5,10 have the same III-tails) => Sigray td>=6 proof INCOMPLETE
  as printed (JC td<=5 still safe via Orevkov/Domrina/Zoladek). Next: H3 audit
  (blocking, days), III-tail closure (~15 lemma-sized, 1-2h each, mechanizable),
  St 3.16/3.18 III-admissibility extraction (may kill all tails at once),
  two-pole analogue. Nothing farm-sized; all runs seconds-to-minutes exact.

## 2026-08-07 (loop, evening): P5+P2 build agents landed; reviews launched; farm grinding
- SHEET6 campaign (4835b13, UNREVIEWED): engine reproduces pilot; Lambda<=7 = 14 rows; td=6 rows 2,3 EXCLUDED; ~15 case-III s-tails + IV-terminals gated on H3 (root-kill). HEADLINE CLAIMS: 3 new thesis errata (E2-E4, lam=0 self-loop families the thesis says don't exist), G2 (St 9.12's kill set can't close its own IV-terminals — unstated H3 load-bearing), G3 (thesis silent on rows 1,5,7,10 => Sigray td>=6 INCOMPLETE AS PRINTED; td<=5 safe via Orevkov/Domrina/Zoladek). If review confirms: sheet-6 exclusion is genuinely open => our campaign = novel work, and RECON's "independent reproof" language needs qualification.
- DC2 degree-3 slice (1eb53b0, UNREVIEWED): 120 unknowns, 420 quantum/414 classical eqs; gate reproduces degree-2 exactly. HEADLINE: quantum corrections = 90 independent directions; at rational family points quantum corank 13 vs classical 14, rank exactly 1 on classical tangent => first measured DC/PC divergence (one scalar quantum obstruction kills one classical modulus). DC(2) consistent with HOLDS at D<=3. D=4 = 260 unknowns, big-box fibers.
- Adversarial reviews launched in parallel: SHEET6-REVIEW.md (vs sigray_full.pdf ground truth) + DC2-REVIEW.md (truncation-artifact attack prioritized).
- Farm: both boxes 4 verdicts each (all EMPTY so far), now grinding 4_12mn34d64_c2_core (35+ min in). 
- 2026-08-07 late: III-extraction landed (e5d42e7): E5 lambda-bound + N1 kill 10/13 td6 s-tails for ALL s; r6,r9 excluded mod H3+H5; G3 rows 5,10/M2 closed; 9 residual classes remain + IV-terminals (H3 agent still out). Combined H3+III adversarial review queued for when H3 lands.
- 2026-08-07 night: COMPOSITION LANDMARK (SHEET6-HIII-REVIEW.md): psi-budget CONFIRMED (G2 closed for real), E5/N1 CONFIRMED (+p.53 subscript-slip corroboration in thesis), composed engine gives td3:0 td4:0 td5:2 td6:13(AF3-superset)+1(SF1). Sanctioned td=6 table FULLY EXCLUDED mod {H1,H2,H4,AF2,AF3,H5a/b}+H3q — beyond what the thesis proves as printed. AF2-IIb pricing audit would kill both td5 residuals. Next: AF2-IIb audit + two-pole (3,3) config agents.
- 2026-08-07 latest: AF2-IIb DERIVED (no free reading); td<=5 sanctioned residual now 0, td6 down to 4 AF3-ext classes + two-pole (agent out). Errata count E1-E7. AF2 badge system retro-validated. Combined AF2+2POLE review queued when two-pole lands.
- 2026-08-07 night 2: TWO-POLE NOT EXCLUDED (284d847): exhibit survives with slack 1; 3 residue + 9 IV survivor classes; td=6 hinges on L1 (merged-pattern l>=1 inadmissibility). Launched combined AF2+2POLE adversarial review + dedicated L1 attack in parallel. THE FORK: L1 holds => td=6 theorem; L1 fails => counterexample template at the (3,3) merge.
- 2026-08-07 night 3: A2P review passed (8f3364f) — AF2 promoted as-is (E6 proven at proof level: thesis's own middle identity false + all p.53 usages compute the minus version); 2POLE promoted with fixes (derived-IIb default => book 2 residue + 6 IV; M_pole=gcd(P,P_g) pin kills residue B => TRUE survivor set = residue A + 2 boundary classes). In flight: L1 (fork-decider), AF3 sanction (last 4 single-pole classes).
- 2026-08-07 night 4: L1 PARTIAL (62335cc): merged pattern squeezed to 3 shapes via pin-propagation (mu=(1,1),k=0,lam=0); 2 of 3 proved empty; the third (IIa nu=3,l=1) is COEFFICIENT-CONSISTENT with explicit unique solution a1/a2=2+sqrt(3) — two-pole funnels to unique merged child (6,12,3,2,5)@lam0. Survivor book now: single-pole 4 r9/M2 (AF3, thesis-forced) + two-pole A + 4 IV classes on the rigid template. Closing needs global h1-branch accounting or Puiseux transport (beyond printed thesis). Combined AF3+L1 adversarial review launched. THE PICTURE: td=6 sheet-6 is one rigid coefficient template away from either a theorem or a counterexample search target.
- 2026-08-07 night 5 (905db83): A3L1 review — ALL FRONTS CONFIRMED, both promoted. CANONICAL BOOK: td<=5 CLOSED (0 survivors, independent of AF2); td=6 = 4 single-pole r9/M2 (thesis-forced entries) + two-pole residue A on the unique rigid template (merged child (6,12,3,2,5)@0, a1/a2=2+sqrt3). Endgame agents launched: (1) lam_root>=1 ledger attack (cuts 8->4), (2) coefficient-level template lift (genome -> edge consistency -> formal candidate or death edge; sizes farm computation if candidate). Errata E1-E9, five proof-level.
- 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so NO branch leaves the chain at the root; the psi-charge lives in the OTHER tree component (St 3.3) so no double-charge was ever possible, but no y-side root unit exists either). Full Prop 7.5 (22) Euler-ledger itemized and BALANCED at 0 root-lambda for all 8 survivors (engine cases/lroot_ledger.py, exact, asserts; gates untouched PASS). Book STAYS 8. Positive yield: (i) every carrier forced to a single x-side cv vertex, kappa_G=1, x-side one unsplit Puiseux cluster below height R>=3 (2 vertices or kappa>=2 blow the budget) — new pin for the template lift; (ii) the 4 slack-0 classes are TOTALLY rigid: x-mass exactly psi=R-1, orbit cv masses exactly the (24)-prices, delta_a = 0 on EVERY fiber of the pencil; (iii) L1's merge blind spot re-derived from the budget side (resonant q-orbit direction carries no punctures => empty ledger row). New erratum E10 (St 3.15 (i)/(iii) labels swapped; thesis usage consistent with the swap). Surviving attack surfaces, precise: delta-strictness at mult>=2 direction collisions (would kill all four slack-0 at once — Prop 7.3 equality question, not printed), x-side-pin vs template realizability, h1-branch budget.
- 2026-08-07 night 7: TEMPLATE LIFT decided (SHEET6-TEMPLATE.md, UNREVIEWED): FORMAL-CANDIDATE — the coefficient-level lift of the two-pole rigid template EXISTS; no edge dies. Genome fully explicit (kappa=42 ladder pi=0,2/7,16/21,37/42; all f/g/h1/h2 patterns at R,F_s,G_m,P_i; 2 punctures x 42 series + 42 B-side = k_f 126). Sweep highlights: (i) h1-branch count (St 3.11(i)+8.3(ii)) KILLS the naive tower reading m_{F_s}=1 (16<=7) and forces approximate-root tower (k0,l0)=(2,3),(k1,l1)=(3,4) UNIQUE (h1 ~ f^{4/3}); supplies the missing proof of St 9.6's silent i=deg(p_G)/M_G (erratum candidate E11); (ii) h2-collapse W(t)=t(t-b)^3-(t-a1)^2(t-a2)^2 must drop to deg 1 — forcing EXACTLY b=2sig/3, a1a2=sig^2/6: the L1c rigid coefficients RE-DERIVED from branch counting, independent of the 8.1(iv) ODE; (iii) three more kill chances pass by exact identity: pole-lead cancellation m_i^2=s0*lam_i^3 automatic, H^3=s1*S^4 transport closes via c_m^7=A, h2-lead pole identity 27a(a-b)^3=sig^3(a-3sig/4) exact over Q(sqrt3); (iv) all 12 (edge,h) count/d-ladder cells EXACT (leak-free); (v) minimal-tower branch forces FIRST-STEP merge (m-growth lock; 2POLE 7.3 restored). New pinned data: b2=(3/4)sig h2-direction, p_h1,P=eta^2-(4/3)w^2, w_i^4 formulas, h1-corner (168,56). Engine cases/template_lift.py: 46 checks 0 FAIL. Residuals R1-R6: cancellation depths (R1, decidable by staged linear system ~10^2-10^3 unknowns, hours-days on farm — the cheap decisive experiment), h-Newton budgets/x-side (R2, merge with LROOT pin), cv realizability (R3), root tower depth>=3 with (k2,l2)=(7,23) + M_R (R4), Jacobian closure (R5), deeper-tower window 4/3<l1/k1<3 (R6, same mechanism recursively). td=6 now rests on R1-R6; naive 17.6k-var msolve Ansatz ruled out, template-constrained staging sized and buildable on lib/jc.py.
- 2026-08-07 night 6 (3f06c21): TEMPLATE = FORMAL-CANDIDATE, no edge dies; L1c coefficients re-derived independently via h2-collapse (convergence of ODE + branch-counting routes). lam_root REFUTED (c8f8bc8, ledger balances at 0 for all 8). Final night review launched (LROOT+TEMPLATE + R1 GO/NO-GO gate). If R1 gates GO: build the staged linear system over Q(sqrt3) — the cheap decisive experiment on the counterexample template.
- 2026-08-07 night 7 (c4624ff): LT review promoted LROOT+TEMPLATE (E11 demoted: printed-tier derivable; 3 genuine kill chances). R1 gated REDESIGN-then-GO; R1 agent launched with the 4 mandated fixes (tower g^2-s0*f^3 gauge a=0, R6-first, co-staged (f,g)+x-side lead, pre-registered J-closure interpretation). Pre-registered: R6 empty + R1 UNSOLVABLE = two-pole td6 template DIES (theorem-grade); R1 SOLVABLE = formal candidate deepens toward R2-R5. This is the decisive experiment.
- 2026-08-08 ~02:15: FOUR worker-agent stalls in a row (R1 x3, R6 x1; probe agents fine — infra issue with long worker streams tonight). Took R1/R6 inline: R1 redesign spec distilled+banked into SHEET6-R1.md; R6 layer-1 ledger done (73504ad): 8/8 integral, (2,3)+(2,5) reproduce the E2-killed i=2 geometry, 6 cases pend layer-2 pattern counts (Prop 8.1(ii)/4.2 m=2 forms). Morning plan: retry R6-layer-2 agent, then R1 build. Farm grinding (box01 6 verdicts). Sleeping long.
- 2026-08-08 (456c634): R6 CLOSED — all 8 deeper-tower window cases DEAD (six at merge transport, two at h2 pole-edge count). m_Gm=1 minimal genome forced; R1 now decisive for the whole residue-A configuration. Agents recovered (R6 layer-2 ran clean, 17 min). Launched in parallel: R6 adversarial review + R1 staged-system build (pre-registered interpretation). Farm: next poll due.
- 2026-08-09 early (5df68d2): R6 print campaign CLOSED — 6/9 window cases dead; survivors {minimal (3,4), (1,2), (2,3)-chain(6,17), (2,5)-chain(6,23)} SURVIVE-IN-PRINT (nothing printable kills them). R1 must enumerate 4 branches ((1,2) delta-spec written: one extra staged resonance level at G_m). When R1-build lands: extend to 4-branch enumeration, then ONE review over echo-rung + R1 before interpreting. Bonus pin a2/a1 = 2±sqrt3.
- 2026-08-09 (f29eafd): R1 CAP-2 CORE EMPTY — GB=[1], char 0, 5s on ultramem (118 vars, 64 eqs, underdetermined-yet-infeasible = deep clash signature). IF faithful (review a9bb… in flight, incl. minimal-infeasible-subsystem extraction + hand re-derivation): minimal-tower genome DEAD; remaining branches (1,2), (2,3)-chain, (2,5)-chain need own cores; all four dead => residue-A EXCLUDED => td=6 = 4 single-pole classes only.
- 2026-08-09 (d434895): R1 EMPTY RETRACTED — spurious doubly (msolve 0.10.1 silently mis-parses parenthesized input; system a-priori satisfiable; 57/57 shipped rows were silent truncations, zero discriminating rows). AUDIT: 401-file paren sweep — ONLY the r1 core affected; all (72,108)/farm/dc2 verdicts stand (our emitters expand fully). Emission rules hardened in AUDIT.md. Rebuild agent launched (4 mandates: paren-free, sentinel fix + discriminating rows, guards, verdict discipline; sibling-branch cores if cheap). Echo-rung work CONFIRMED by same review — R6 4-branch state stands.
- 2026-08-09: R1 full-degree cores DISPATCHED to ultramem (sequential: w-free p-screen -> full p-screen -> char-0 decisive -> (1,2) sibling). All guards passed pre-flight; runner has verdict authentication. This queue IS the decisive experiment for 2 of 4 residue-A branches.
- 2026-08-10: user restarting local machine. All 3 remote workloads nohup'd (ultramem R1 queue+lifts w/ cron; box01 farm; jc-b farm — jc-b was ssh-255 at last poll, re-check on resume). On session resume: re-arm /loop, poll all three.
- 2026-08-10 (post-reboot resume): jc-b was TERMINATED (preemption) — restarted, farm resumed cleanly (9 banked outputs kept, re-running the killed core.q). Box01: 6 EMPTY / 6 FAILED (big char-0 cores OOM-class; triage tier owed after queue drains). Ultramem R1 w-free p-screen ~1 day in, 1.07TB resident, alive. No LIFT-CERT yet. Loop re-armed.
- 2026-08-10 (08fbbda): TD-UNIFORM entry theorem landed (UNREVIEWED, review launched): pinned M = b; PRIME td => all single-pole rows b=1 => excluded at entry, uniformly (scan verified td<=40; td=37: 8/8 dead). Composite residual grows (212 survivors at td=16); td=9 slack-6 chain shows budgets saturate; bottleneck = multi-pole 8.4 analogue. If review holds: JC2 geometric-degree ladder at prime td rests entirely on multi-pole configs. R1-acceleration agent still out.
- 2026-08-10: TDU fully settled — PRIME THEOREM promoted (single-pole dead at entry for every prime td, perimeter H1/AF3-tier); composite table authoritative (212 survivors at td=16, lower bound); bottleneck = multi-pole 8.4 analogue. My td=9 'discrepancy' was a display-truncation miscount, caught by reconciler.
- 2026-08-10 (c8f2cb0): R1 REDUCED queue live on ultramem (49 rows/63 vars, verdict-equivalent, soundness-proven). Old 128-var run killed per acceleration agent's recommendation. Sweep calibration: GB deep at every char (12 primes all timeout locally) — this is a real computation even reduced. Chain folds still grinding locally toward the (2,3)/(2,5) cores.
- 2026-08-10 (353ed0d): CHAIN CORES LANDED. (2,5)-chain core NONEMPTY at p AND char 0 (487-elt GB, origin excluded) — the branch DEEPENS; deep-dive agent launched (dimension, degeneracy split, deferred-row evaluation: real template data vs artifact — this decides the counterexample frontier). (2,3)-chain core queued on ultramem behind reduced minimal queue. Byte-identity gate passed on the fold/CRT pipeline.
- 2026-08-10 evening: (2,5) locus REAL (dim 27, nondegenerate, explicit point) but deferred rows refute sampled points at rung 10 — rung-extension decides. SECOND msolve hazard (unreduced mod-p coefficients => silent corruption): 110 shipped files affected, verdict-contamination audit agent running (expected clean: c1 leaves never yielded accepted verdicts; (72,108) rests on char-0 + external artifacts).
