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
- 2026-08-10 late: OPS SAGA RESOLVED — box01 root disk was 6.8GB (!), filled during box02-fold: EBS resized to 100GB (grown live, no downtime for the running job); truncated extracts purged; fold re-shipped; jc-b RETIRED after 3rd preemption (queue folded into box01 as lane 2, MEMGB=300/T=32, dual-lane). All 27 corrupt-class farm files replaced by round-trip-guarded reduced twins on box01; all previously banked box verdicts verified clean (W-class or char-0). (2,5) rung-extension decision runs still grinding locally.
- 2026-08-10 night: (2,5) rung-extension decision runs died locally (macOS mem-kill + 3000s timeout at 4 threads); shipped to ultramem as parallel runner (24 threads, 300GB cap, alongside the big reduced screen at 1.4TB+). Queue: ext_p105337 -> ext char-0. THE branch decider now runs on proper hardware.
- 2026-08-11 early: minimal-branch reduced wfree screen DIED at 1.5TB cap after 34h (no verdict); killed the auto-advanced (strictly bigger) full-p run; ultramem now dedicated to (2,5) ext decider (28h in). Minimal branch pivots to CHART DECOMPOSITION (agent launched: split reduced core into 4-16 guarded leaves w/ cover certificate, local calibration). The monolith era is over for this system class — decomposition always wins (campaign lesson, again).
- 2026-08-11: ULTRAMEM TERMINATION ROOT-CAUSED — not Spot preemption: the STALE jc_deadline poweroff cron (leaf-era) fired (deadline passed 25 min before death). Cron removed permanently. Cost: 28h of (2,5) ext compute. Recovery: ext decider MOVED to box01 (on-demand, 16 threads, 250GB cap, alongside farm lanes); (2,3) chain queue launched directly on ultramem (40 threads); lifts resumed. STANDING LESSON (2nd occurrence): guest lifecycle machinery must be inventoried and wiped on every box reuse — added to ops checklist.
- 2026-08-11 (e8839bb): minimal core decomposed (4 leaves, 1s each — monolith was foredoomed by relaxation artifact); UU chart NONEMPTY everywhere, core collapses to one conjugate-pair relation satisfied identically by template data. NO branch killed at core level yet — all discriminating content is in deferred bands. Minimal-branch ext build agent launched (mirrors (2,5) ext, in UU chart, with witness guard). Deciders running: (2,5) ext on box01, (2,3) chain on ultramem. (1,2) core to get the 4-leaf treatment after.
- 2026-08-11 ~05:00: minimal-ext DECIDED — branch survives entire in-window F_s band by explicit witness (all 323 eqs at 2 primes); next tier = depth-84 quotient (farm-scale, needs sizing). SURVIVOR PATTERN NOW UNIFORM: no two-pole branch dies at any accessible tier; discriminating content keeps receding deeper (depth-84 / R2-R5 / J-closure). Morning queue: depth-84 sizing, (1,2) 4-leaf, deciders.
- 2026-08-11 morning: Q0 PASSED — F_s ladder EXHAUSTED, minimal branch survives by explicit point (3913087). BUT the witness has s1F=0, and the tower tie H_F^3 = s1F*S_F^4 may force s1F != 0 — flagged as front 2 of the consolidated ladder review (sec 13-16, in flight). R2 build held pending that verdict. Deciders: (2,5) ext + (2,3) chain both ~23h in.
- 2026-08-11 (31f8309): LADDER REVIEW INVERTED THE VERDICT — survival was s1F=0 artifact; saturated Q0 = EMPTY both primes: minimal branch intended locus DIES at depth 84 (strong evidence, char-0 pending). Same artifact in (1,2). Saturated-rebuild agent launched (scale inventory + Rabinowitsch rows + E5/E6 tie emission + pattern-positive anchors; per-branch honest verdicts; char-0 upgrade attempt). If saturated kills hold at char 0 across minimal + (1,2), residue-A rests on (2,5)/(2,3) chains alone. The review protocol caught the ZZ-artifact pattern at a level where it had fooled four consecutive tier gates.
- 2026-08-11 (5a75ee3): G_m BRANCHES DEAD (verified+reproduced): minimal at depth-84 over Qbar (family object), (1,2) at terminal core char 0. Q2 full-locus screen + (1,2) E5-port review agent launched (the two riders). If Q2 empties and the port survives review: residue-A exclusion rests solely on the (2,3)/(2,5) chain deciders (grinding ~24h each). The kill side is winning.
- 2026-08-11: (2,5) ext p-screen DIED at 250GB/5h (monolith, pre-saturation object anyway); char-0 successor killed. (2,5) queued for saturated Q0-style gate after riders agent lands. Monolith count: 3 deaths, decomposed/witness gates: 100% decisive. The pattern is law now.
- 2026-08-11 midday: Q2 ladder closed (stratum-13 kill PROOF-TIER char 0; l12/l8/l4 shipped to box01 at 500GB/32t — GB cliff needs big iron; l1 build-gated). Saturated chain-gate agent launched for (2,3)/(2,5) — the last two open branches, built honest from birth. Residue-A endgame: minimal mostly dead (slots<13 strata pending), (1,2) owes ladder, chains at terminal gates.
- 2026-08-11 13:20: (2,3)sat screens live on ultramem (40t/1.4TB; stale unsaturated monolith killed). Fleet: box01 Q2-l12 + farm lanes; ultramem sat23 + lifts. Open ends: (2,5)sat NONEMPTY => next-tier build owed; (1,2) ladder owed; Q2 l1 build-gated.
- 2026-08-11 late: STUCK-FAMILY CLOSURE (33021f4): multi-root chain-edge cut implemented from GGV5's multiplicidad proposition — 4 of 7 stuck families now reduce fully (first verdict already: 12_36_r1_c3 EMPTY-BY-CASCADE, transfers to r2 twin); remaining 5 rho=2 families get guarded direct emission. The deg<=150 catalog now has NO family outside the pipeline. Emission driver detached (farm_stuck7.log, auto-finishes RED twins + queue + local msolve). Adversarial review owed on the cut transform before bound-150 claims.
- 2026-08-12: 5 monolith deaths diagnosed (vmem-cap silent kills) — requeued: q2l at 900GB (box01), sat23 at 1850GB (ultramem). Stuck-7 driver DONE (post-processing complete; one rc=124 timeout in tail). NEW AVENUE LAUNCHED: classical kill-test battery on the template (splice/Neumann, A-M semigroup, log-BMY, Jelonek) — four independent topology/combinatorics tests, any one can kill the two-pole configuration outright. Cut-transform review still out.
- 2026-08-12 (7242f2c): MATHIEU-ZHAO BREAKTHROUGH CLAIM — rigidity half of conj:R claimed PROVED (Theorem A, 15-line DvdK-mechanism ODE argument; M1-M5 machine checks pass incl perfect powers at all open cells). If review holds: conj:R closes at EVERY cell, strip theory uniform in (k,d2), paper1 conjecture becomes theorem. Max-depth adversarial review launched (fable) with small-degree counterexample sweeps + Lemma B bridge audit (agent's own flagged weak point). Workflows multipole-84 + sigray-audit grinding in parallel.
- 2026-08-12 (ad709ae): CLASSICAL BATTERY — the template SURVIVES topology: splice/Neumann PASS (all determinants/multiplicities positive), Jelonek PASS, A-M valuation PASS at poles with ZERO slack (ord f_y = -39 exact match), genus balance closes identically. One new kill (pi_G=4 branch dead). Sobering + significant: four independent classical tests, none contradicts the template — it is topologically a legitimate candidate. log-BMY still open pending B/x resolution tails (the one classical test left). All conclusions transfer to all surviving branch variants.
- 2026-08-12 (7179119): PAPER 1 v2 — the functional section is now THEOREMS (6.1 rigidity + 6.5 = former conj:R), 15pp, compiles clean. Ready for: (a) user's GGV follow-up note, (b) Zenodo artifact v2 (mathieu mode + MATHIEU docs added to bundle) when user wants. Still out: multipole-84 workflow, sigray-audit workflow, cut review, box01/ultramem screens.
- 2026-08-12 (0827409): THEOREM MP LANDS (multipole panel, 21 agents, 3.2M tokens): the td-ladder bottleneck is SETTLED at the structural level — verbatim m-pole 8.4 is FALSE, but the maximal kill + merge calculus reduces EVERY (m,td) multi-pole configuration to a finite book of resonant jump-vertex cells (2<=M<=r<=m, l>=1, full anatomy pinned). All 5 angles survived their refuters. Combined with prime-td + conj:R-now-theorem: the JC2 exclusion program is now finite-book at every level. NEXT: enumerate + bash the jump-vertex book (workflow-shaped); sigray-audit still running.
- 2026-08-12 (88186fd): SIGRAY FULL AUDIT (35 agents, 130 statements, 3.7M tokens): 10 NEW errata + 10 gaps found; every one triaged for campaign damage — NET RESULT: no promoted result damaged; multiple campaign readings PROVEN forced (H5a upgraded to printed-statement-forced via St 3.8; d_{f-a} reading mandatory via St 3.13/3.14). The thesis's section 2-6 foundations are now swept; the campaign's hypothesis perimeter is dramatically de-risked. Filing amendments owed (H3 quote, E-numbering of new errata) — doc-chore agent when slots free. MP integration review + cut review still out.
- 2026-08-12 (eb0abdf): MP promoted (MP0-MP8+O; MP9 corrected; finiteness rider demoted to per-frame). THE one open axis = chain-depth closure lemma — max-depth agent launched (stabilization orbit-map / Puiseux jump-count angles). If it lands: jump-vertex book FINITE per (m,td), and with prime-td + conj:R theorem + MP, the whole exclusion program becomes a finite enumeration at every level — the shape of a full JC2 proof modulo bashing the book.
- 2026-08-12 (depth): CHAIN-DEPTH CLOSURE LEMMA PROVED (SHEET6-DEPTH.md) — the M=1 chain step conserves w := (kap-rho)/nu on every l=0 step (the unbounded direction), resonant steps need Delta | num(w) and contract by <= 2/3, and the ENTIRE jump-cell menu factors through w (handshake kap_m - D/i = w; join forces equal w; nu determined per (kap_m,l)). Depth-invariance follows: menu constant beyond d0 = gen(W)+2. td=6: W={2}, menu == the promoted (2,3,1) cell exactly (explains 351/351). Bonuses: root merges need w<1 (one-line root kill); ZCH 0-edge is Prop 9.3 case (III) => needs w-ratio nu>=2 between chains (engine model corrected, no promoted conclusion touched); St 9.6(v) itself conserves w=3/2. 13/13 exact checks (cases/depth_closure_check.py). CONSEQUENCE: jump-vertex book FINITE per (m,td) — MP's demoted rider RESTORED (corrected book spec in SHEET6-DEPTH.md sec 8). The exclusion program is now a finite enumeration at every level, unconditionally at H1 tier.
- 2026-08-12 (2c81954): DEPTH CLOSURE LEMMA claimed (w-conservation; book finite per (m,td)) — max review launched (a case-branch drift or normalization mismatch would fake it; SIGRAY-AUDIT interaction checked). If it stands: launch the jump-book enumeration workflow with the reviewed spec — the program's final computational phase.
- 2026-08-12 (400b50b): DEPTH LEMMA PROMOTED — BOOK(m,td) enumeration is GO; enumerator agent launched (td 6-14, gate = td-6 record reproduction; mechanical kills inline; survivors banked for per-cell bash). The pipeline: prime-td theorem + Theorem MP + depth lemma + book bash = multi-pole exclusion per td; combined with conj:R theorem + degree farm = the full JC2 program, now finite at every level.
- 2026-08-12 (book): BOOK(m,td) ENUMERATED (cases/book_enum.py, BOOK-ENUM.md, systems/book/*.json): td=6..14, m=2..floor(td/3), reviewed spec E/T/C'/J'/R/S with the mechanical arsenal inline (MP7 l=0, gcd menu M>=2, kap-window integrality, corrected ZCH case-(III) w-ratio, root w<1, MP9 even-l, St 9.4 root budget). GATE PASS: td=6 m=2 == the promoted record cell-for-cell (unique residue-A IIa (2,3,1) M=2 child (5,3,1/2), R empty). RESULT: 421 cells, 346 killed, 75 survivors = only 22 distinct classes (31 IIa — ALL l=1, M=r, the Theorem-O escape pattern; 33 ZCH — only at w in {4,6} with an integer-ratio partner, first at td=9; 11 family-I — only r>=3, m>=3; 0 ROOT anywhere: every alphabet sits at w>=1, td-uniform root kill). Prime td 7/11/13 panels EMPTY (all entries off-axis b>=2 — the multi-pole shadow of the prime theorem). Largest class: residue-A in 10/18 panels; largest panel m=4 td=12 (21 cells). NEXT: per-cell bash — Prop 8.1(iv) rigid solve + coefficient-vs-ratio match (IIa l=1 family first), suffix engine from child data at budget td-2, r>=3 log-obstruction for family I, M>=2 chain engine for the 27 off-axis entry classes.
- 2026-08-12 (bd4baa2): BOOK BASH WORKFLOW launched (22 classes, full arsenal, adversarial votes per kill). If it drains the book: td 6-14 exclusion reduces to residue-A-type coefficient templates only — the program's endgame at every level. Prime td 7/11/13 already FULLY excluded.
- 2026-08-12 (5c6724b): BOOK BASH round 1 — 3 classes + 1 panel KILLED (frame-free T1 kills incl all 7 ZCH(2,2,3) panels); 6 survive to rigid one-scale templates; THE PICTURE SHARPENS: residue-A IIa(2,3,1) is in every nonempty panel and survives everywhere — the ladder's global bottleneck is ONE template family. Workflow resumed for the 13 unbashed ZCH/I classes (cache replay + live fill).
- 2026-08-12 (r2 interim): BOOK BASH ROUND 2 — 12 of 13 classes DEAD by first pass (only ZCH(2,3,2)M2@w6 survives); BUT the credit ceiling killed ~13 verify votes mid-run, so several 'confirmed' flags were VACUOUS (empty vote arrays). Credits restored; workflow resumed with cached bash results — live verifies + synthesis filling now. If kills hold: book = 7 surviving classes total, ALL of the rigid-template kind.
- 2026-08-12 (fbcd663): BOOK FULLY ADJUDICATED — 22 classes, 75 instances: 15 classes DEAD (closed-form kill criteria discovered: ZCH iff (nu+1)|l, family-I iff l/r or r/l in Z — these are little theorems in their own right), 7 SURVIVE, every survivor a rigid one-scale template. CREDIT CEILING hit again mid-verifies (resets Aug 15 8pm PT): 7 r2 kills carry engine-verification only, review votes OWED; cut-transform review agent presumed dead the same way. Agent work PAUSED until credits; local+fleet compute continues. Standing queue on credit restore: (1) r2 verify votes, (2) cut-transform review relaunch, (3) ZCH(2,2,3)@w4 r1 votes.
- 2026-08-12: cut transform PROMOTED (review passed; deg<=150 pipeline now fully load-bearing incl the stuck-7). Bound-150 blockers remaining: farm queue drain + big-core memory tier + two-machine replication decision + audit pass.
- 2026-08-12 (9fff9fc): BOOK FULLY CONFIRMED (all r2 kills 2-vote). TEMPLATE-FAMILY ATTACK workflow launched — 5 angles on the shared mechanism of the 7 survivors: GALOIS descent (new — the templates live in Q(sqrt d), conjugation swaps the poles; one non-symmetric pinned datum kills), the L1 sec-7.2 global h1-budget (the identified missing layer), panel budget squeeze (b>=2 entries may not reach mu=1 arrivals), classical battery on the 6 untested templates (zero-slack valuation test), and Weyl quantization (DC2 divergence as a weapon). This is the shot at closing td<=14 multi-pole outright.
- 2026-08-12 (33799c7): TEMPLATE ATTACK LANDS — book 27->23 (new law L6); three shield theorems prove Galois/budget/quantum have ZERO traction (templates conjugation-equivariant BY RIGIDITY — deep and slightly ominous); quantum divergence concentrates at the ONE resonant direction b. Everything now points at the same coordinates: L1 sec-7.2 coefficient tier at direction b.
- GROK 4.6 EVAL (xmodel/grok-eval-20260812.md): impressively deep repo read; P(JC2 true) ~0.72; 5 avenues incl. S_6 monodromy product test (covering-theoretic, Sigray-independent — GOOD and new), J-jet at G_m on the 7 dead-stretch coeffs (overlaps our R1 but sharper framing), Theorem-A-on-depth-3-column (cheap, connects our two lanes), mixed-merge completeness crack (checks our book's quarantine). Also flags the cheapest logged-but-unrun shot: IIa(3,5,1) W-residual deg-2-vs-<=1.
- 2026-08-12 (b9db83e): OFF-AXIS MAPPED — 23 entries, 2691 cells (700 mixed), prime-td NOT trivially restorable (td7 witness exists); DS2+MP8 break off-axis (the honest price of the externals' finding). Closure-lemma agent launched (R1-offaxis w-law -> td7 kill; R2 mixed-merge anatomy; recount). The book's soundness repair is the top thread; direction-b strike next slot after.
- 2026-08-12 (36505a6): OFF-AXIS CLOSED-ish — R1/R2 lemmas proved (unreviewed), td=7 restored, 2691->440 survivors (0 open). Review WITH the new cross-model protocol launched (Fable + Grok + GPT all referee R1/R2). Next after: direction-b strike, the 14 off-axis T1 targets, td11/td13 cells.
- 2026-08-12 (426e9c7): GROK MONODROMY — template passes covering theory too (169/169 passports realizable, genus-18 cross-check vs CLASSICAL). The candidate has now survived: printed combinatorics, coefficient tiers to depth 84, splice/A-M/Jelonek, Galois, quantum vertices, and S_6 monodromy. EVERYTHING funnels to the J-jet/algebraization layer — exactly where the direction-b strike (Fable) and the Hermite-Pade pilot (Sol) are both aimed RIGHT NOW. Convergence total.
- 2026-08-12 (Sol): PROP 5.8 EVERY-FIBER PROVED by GPT 5.6 Sol (its own avenue #1) — the mass identity td=Sigma Lambda now holds on every fiber via a relative pole-divisor + Chau's theorem argument; the generic-a rider on the entire book layer E is repaired. Needs our review pass (esp. the Chau citation and the defect identification), but the structure is exactly what the audit called for. Sol's first primary-research delivery: substantial.
- 2026-08-12 (1bee7f1): TRIPLE REVIEW converged (3 model families, identical cells found independently — the protocol works): off-axis R1.3-R1.5 refuted, td=7 re-retracted (2 live cells incl the (7,5) eps-cell); R1.0-R1.2+R2 solid. Lambda-budget repair agent launched (the M-jump escapes carry PRINTED St 9.6 lambda-costs — price them against St 9.4). Direction-b strike + Sol algebraization + 5.8 review still out.
- 2026-08-12 (e896cfa): SOL'S 5.8 PROMOTED — first fully-promoted primary-research result from an external model (Fable+Grok review; Chau full text verified; layer-E rider repaired). Three-model collaboration validated end to end: Sol authored, Fable+Grok refereed, one overclaim caught+demoted. In flight: algebraization/E5-factor review, budget repair, direction-b strike.
- 2026-08-12 (dc0918b): DIRECTION-B STRIKE CLAIMS THE BIG KILL — zero-tail residue-A DEAD char 0 (exact J-jet contradiction 0=-42 at the b-resonance slot; w_i^4 forced to 0; all 10 panels; every banked R1 witness). UNREVIEWED — full triple-model review launched with the wrong-object audit front (does the template force zero tails, or does the kill only close an artifact stratum? THE question). E5-factor interaction flagged. If this survives review, the residue-A frontier either closes outright or moves to the 83-var full-window object.
- 2026-08-12: Sol lands its SECOND promoted result (algebraization obstruction + a real E5 erratum in OUR promoted template — caught by an external model doing primary research; blast radius zero by unit-rescalability, adjudicated 90/90 exact + E6 anchor + Grok concurrence). Direction-b triple review + budget repair still out.
- 2026-08-12 (c0dfed0): DIRECTION-B THEOREM STANDS post-review (5 paths; the review itself caught+corrected the wrong-object corollary before promotion — culture holding). NET RESIDUE-A STATE: pure-dead-stretch sector dead everywhere (this theorem) + zero-window R1 witnesses dead (18.1) — the template lives ONLY on the forced-nonzero-tail locus; the 83-var window build (running) characterizes exactly that. The candidate keeps shrinking without dying: either the window build corners it into 0=contradiction (JC2 progress of the first order for td<=14) or produces the honest nonzero-tail template = the sharpest counterexample spec yet.
- 2026-08-12 night: FLEET RECOVERED. Root causes: GCP project transiently unavailable (user-side, restored; both instances TERMINATED but DISKS INTACT — 73 .out files preserved); box01 was never down — the local IP changed (149.22.81.205) and the SG allowlisted only the old IP; added new IP to sg-09ffa8932558f0a79. LOSSES: in-flight compute only — sat23 p105337 progress (relaunched), the old unsaturated 23chain runs (both FAILED pre-termination — superseded by sat23 anyway), and the cCa2/cCa6 lifts (weeks running, no LIFT-CERT, Singular restarted via cron: DECISION per novelty rule = let this one boot cycle run; if no cert by next check, kill permanently and note in AUDIT). NO banked verdicts lost (repo = source of truth). box01 kept farm lanes going throughout (+13 EMPTYs) though Q2 l8_p105337 FAILED (vmem again).
- 2026-08-13: BOX02 LIVE (x2idn.32xlarge, 2TB/128c, 54.166.236.69) — Q2 l8/l4 running at 1.9TB vcap/96t; box01 relieved of Q2 (farm lanes only now); ultramem sat23; fleet = 3 boxes optimally matched to workloads.
- 2026-08-13: Q2-l8 died on the 2TB box too (11h, 1.65TB RSS, vcap kill) — the GB cliff is structural; l8/l4 need leaf-decomposition, not iron. Box02 STOPPED (control plane, disk kept, ~$13/h saved) pending the window slot-20 verdict which may moot the whole Q2 ladder. Window agent resumed from transcript post-restart; bands banked, slot-20 in flight.
- 2026-08-13 ~12:15: WINDOW VERDICT (§6.V): NOT EMPTY-BY-KILL. Relaxation consistent
  (rank 57/77, -42 in column span) => no linear-algebra kill at depth 21; differential
  at zero-tail point INCONSISTENT rank 29 => zero-tail theorem sharp at first order;
  all closed-form strata dead. Survivor locus V = 47 band conditions + slot-20; residual
  = 32 low-data-dependent conditions on ~28 params. NONEMPTINESS NOT CERTIFIED.
  Actions: verdict committed; dual review launched (Grok one-shot + Fable internal);
  window agent re-tasked (emit residual-32 msolve system per AUDIT rules + relaunch
  depth-23 detached). Burden per §6.V moves to residual solve, rows 21+, and Q2 l8/l4
  (leaf decomposition needed — Box02 stays STOPPED until residual screen results).
  Sol lanes running: td7-law, thmB (now elevated: functional-level kill is the missing
  instrument), avenues2.
- 2026-08-13 ~13:05: PROMOTED generalized zero-chain law (Sol lane 1 + engine check
  62/62 + Grok audit SOUND): td-7 book 62 -> 6 live cells, 1636/1689 routes dead by
  theorem; 62-cell bash workflow CANCELLED, replaced by next-tier plan on 6 cells.
  Sol thmB = proved ceiling (no additive functional separator; escape = slot-10
  cusp tangent squared -> level-42 quadratic, matches window build independently).
  §6.V dual review SOUND-WITH-ERRATA both referees; repair 24-test verdict loop
  grinding. Residual-32: 2 timed-out prime lanes relaunched with 12h caps (5 msolve
  lanes now live). Depth-23 GB42 done, GB21 in progress. sol-avenues2 landed, unread.
- 2026-08-13 ~13:30: Grok re-audit of thmB vs §7 pins: SOUND-WITH-ERRATA. Decisive
  cross-cut: Sol's flexibility family REQUIRES level-42 tails => DEAD on pinned locus
  (no surviving constructive witness for residue-A survival); additive-separator
  ceiling still holds (pinned relaxation consistent 56/76 => no linear kill either).
  All rides on nolog screens + depth-23. Ultramem IP stale (re-resolve via gcloud).
- 2026-08-13 ~13:50: §6.V PROMOTED (dual review SOUND-WITH-ERRATA x2, errata applied,
  harness 17/17+27/27+24/24+6/6 all green). Lift last-chance executed (cCa2/cCa6
  retired; AUDIT note; remote pkill pending next ultramem window - gcloud ssh flaky).
  Ultramem: sat23 alive (r1_23sat_p105337, 2 lanes), IP now 136.65.11.117 via gcloud
  ssh only. 6 parallel nolog screens running orphan-safe. D23 analysis tasked to
  window agent (decisive: relaxation +rows21/22 +pins).
- 2026-08-13 ~14:45: Sol toric = NO-KILL-AT-TIER-1 (closure consistent; tier-2 = 7.8M
  binomials, parked — msolve screens subsume it; revisit on Box02 only if screens
  time out persistently). Sol sixcells: (9,15,7,3)@2 PROVEN next-step survival
  (transport+caseIV both completions; equality sharp-forcing proven for integerized
  summands; extra-unit kill CONJECTURE). Grok review queued. 3 background tasks
  got killed mid-flight (both Sol lanes' wrappers + stuck7) — deliverables were
  already written; nolog lanes (orphaned, PPID 1) unaffected. stuck7 script itself
  hangs >70s (remote polls?) — needs a look before next run.
- 2026-08-13 ~15:25: 11 msolve lanes local (6 nolog + 2 plain + 3 stuck7 farm cores
  relaunched orphan-safe: 12_33 c10 RED, 6_15 c1 RED, 6_15 c2.q). Grok sixcells
  review launched. Ultramem gcloud ssh now failing repeatedly (rc 255, also via IAP;
  worked at 13:47) — sshd possibly starved by sat23; lift-pkill deferred (cosmetic,
  retirement already recorded). GGV follow-up draft awaiting DC review.
- 2026-08-13 ~15:45: LOCAL MSOLVE BAN (DC directive after 32GB thrash — my stuck7
  big-core lanes were the offenders). All 13 lanes migrated to Box02 (restarted,
  new IP 54.89.92.223, 8 threads/lane, lanes.log self-recording). ops/FLEET.md
  written: fleet inventory + access + run conventions for ALL agents (Fable subs,
  Sol, Grok prompts must point at it for any solver job). Box02 stays up until
  its queue drains. Local-screen elapsed work forfeited (~2h; no msolve checkpoints).
- 2026-08-13 ~16:30: Grok sixcells review SOUND (all 6 attack lines clear; 1 citation
  nit) => (9,15,7,3)@2 transport-tier survival DUAL-CERTIFIED; BOOK-OFFAXIS §11
  addendum. td-7 endgame = coefficient-gluing tier on 6 cells (3-5d build, queued
  decision). Box02: 13 lanes, 468G/2T used, healthy grind. GGV follow-up draft
  awaiting DC review for Friday send.
- 2026-08-13 ~17:10: Box02 13 lanes grinding, mem 610G/2T (watch: if >1.5T next tick,
  kill the c2.q char-0 balloon first). Ultramem reachable again — stale lift runner
  bash (PID 9380) killed, lift retirement now fully executed. sat23 ~10h into
  p105337. No screen verdicts yet.
- 2026-08-13 ~18:10: §19.5a banked. QUEUE: l12 3-chart cover on Box02 AFTER current
  screen queue drains (350-500G fences). Preflight review still out.
- 2026-08-13 ~18:40: Preflight review = SOUND-WITH-ERRATA: 6->2 FALSE (2 of 4 "dead"
  cells E5-alive via unpriced arrivals; 37 completions saved by review). Deeper issue:
  book generated with kbar_BOOK pin, never re-enumerated under kbar_E5 => launched
  td7_census_e5 agent (both H5a readings, controls = 56 law-dead + 2 certified cells).
  3 doomed l8 leaf survivors killed on Box02 (frees ~450G for screens). Screens: no
  verdicts yet (~5h in at 8 threads).
- 2026-08-13 ~19:50: §11a PROMOTED (review SOUND; brute-force complete nu<=400).
  td-7 honest book: 17 cells (Q-value, printed record leans this way) / 2 (forced-nu).
  H5a theory lane launched (Sol): prove which reading is forced + decisive-experiment
  spec. Gluing design v2 (89KB): milestone plan = one complete (9,15) tower cert ->
  jet window -> Box02 solve -> only then expand to corrected census. Screens 13 lanes
  973G, ~6h in, no verdicts. Box02 mem eased post-cull.
- 2026-08-13 ~21:35: H5a PROMOTED as resolved (dual SOUND). 17-cell book unconditional;
  U_7C = open conjecture (no cheap discriminator). Launching gluing milestone 1 agent:
  (9,15) direct-route tower certificate per sol-gluing-design v2 build plan. Box02 mem
  plateaued 1226G (F4 possibly converging).
- 2026-08-13 ~22:20: Box02 triage — 3 stuck7 farm lanes were eating 975G (c2.q 423G,
  c1.RED 308G, c10.RED 244G) vs ~360G for ALL TEN res32 screens. Culled stuck7
  (farm riders, back to queue for post-drain/decomposition). Screens now have ~1.6T
  runway through their 03:43 PDT caps. Nice signal: nolog lanes (26G) < plain (38G)
  — the §7 pins genuinely shrink the F4.
- 2026-08-13 ~23:15: Tower adjudication mid-flight. Grok SOUND-WITH-ERRATA (kill stands
  + trunk likely dead too); trunk machine-checked DEAD (cell-level kill candidate);
  Sol BROKEN — but its critical finding = the already-repaired Case C (same 3 pairs).
  LIVE blockers: M_U=4 arrival + free-characteristic predecessor family unexamined
  (Sol f.3), schema reconciliation (f.2). Agent extending exhaustion; cell-kill
  promotion ON HOLD until Sol re-review. Screens: caps 03:43 PDT.
- 2026-08-14 ~01:05: FIRST CELL-LEVEL TOWER KILL PROMOTED — (9,15,7,3)@2 dead
  (triple-review convergence, Sol final CONFIRMED-KILL). td-7: 16 live cells.
  Rollout planner next. Screens: caps ~03:43.
- 2026-08-14 ~03:50: Screens R1 capped at 12h, no verdicts (F4 deep, 1.5T aggregate,
  progressing — banked per R6 §19.2: TIMEOUT, not evidence). R2 launched: 3 main-prime
  lanes @48h caps, -t 24 each + one -e 45 elimination probe (alternative instrument).
  ctl0 lanes dropped (calibration, not decisive). UNIFORM td-7 THEOREM proved pending
  dual review (Grok + Sol running). GGV follow-up: surface draft to DC this morning.
- 2026-08-14 ~05:00: TD-7 PANEL CLOSED — uniform tower theorem promoted (dual green,
  14 errata folded, 1559/1559). Second full panel after td<=5. Launching td-11/13
  refile+port scoping (Sol) overnight. Morning package for DC: GGV follow-up draft +
  td-7 news + paper-2 question.
- 2026-08-14 ~10:30: Normal-form review SOUND-WITH-ERRATA — Markov fat record proved,
  11-A kill stands, but fat-state enumeration is INFINITE (no emptiness cert) =>
  td-11 compiler GATED on NF-Z/P/M. Launching NF-Z attack (tower agent; N1-N4 is the
  precedent). Screens R2 ~7h in, 345G, no verdicts. No DC replies yet.
- 2026-08-14 ~12:30: AM audit = honest (c): char sequence forced + AM divisibility
  passes, but counterexample fibers are >=4-place (one-place => automorphism) so AM
  binds only via Jelonek components needing cross-fiber data (not template-pinned).
  Instrument parked with activation condition recorded. NF-Z repair in re-review;
  Sol lateral sweep cooking; screens ~9h into R2.
- 2026-08-14 ~13:05: NF-Z round 4 STILL-SHORT (3rd CE). Pattern: the free zone carries
  ordered arithmetic that resists finite invariants. PIVOT: reframe as NF-D — prove a
  depth cap on LIVE neutral words (dead-beyond-depth makes enumeration finite without
  quotient completeness; neutral-depth rigidity corollary + td-7 N-closure are the
  evidence). Witt lane: NEVER-VANISHES-PROVED on the registered stratum (clean
  rigidity; disproof lane closes there) — commit on marker.
- 2026-08-14 ~14:30: td-11 neutral depth OPEN (honest); REORDER: tower port before
  NF-P — an entry-level td-11 clash theorem kills deep words as a byproduct, breaking
  the depth/census circularity. Next object: 11-B/11-C entry clash windows under the
  corrected P/mu consumer (11-A intruder already dead — recheck its window too).
  Paper-2 core drafted (21pp). Screens ~14h. Witt review rerunning.
- 2026-08-14 ~17:45: Screen acceleration per DC ask: (a) ORDER PORTFOLIO — 2 reordered
  copies of nolog_p105337 (reversed + seeded shuffle) launched on Box02 spare cores
  (-t 12, 29h caps; GB order sensitivity = 10-100x lottery); (b) support-split leaf
  emission tasked to window agent (the §6.V strata evidence says zero-heavy leaves
  collapse); (c) held: more primes (correlated), HC (start-system explosion), Macaulay
  cert (unknown degree). Parallel: td-11 OPEN-residue (NF-Z-dagger) + td-13 13-2b recon.

## STRATEGY (standing, DC 2026-08-16 — loop/workflows read this)
WIN CONDITION: we win the JC2 proof race by using our full resources more
completely and more creatively than anyone else: all three frontier models
(Fable + GPT-5.6 Sol + Grok 4.6) across EVERY role — math ideation, primary
research, adversarial review, software engineering, software review — plus
AWS compute, under the adversarial-promotion culture (dual review, honest
retraction, evidence-graded claims).
RACE SPIRIT (DC 2026-08-16): the race is URGENCY, not adversarial posture.
Be generous with credit and with sharing partial results (precedents:
Helali priority citation, coordinated-note offers, public artifacts). Speed
matters because major results now drop direct-to-X with zero warning;
someone could post a JC2 proof tomorrow. Corollary: timestamp our partial
results early and often (Zenodo artifacts are cheap priority records).

DAILY DISCIPLINES (in order, at least once per day):
1. EXTERNAL SWEEP: public progress (arXiv/Zenodo/X/blogs), all sources on
   content; track the (72,108)/JC2 ecosystem actors.
2. AVENUE EXPANSION: fresh lateral/creative proof+disproof ideas,
   tri-model (Fable + Sol + Grok generating independently), cross-ranked.
3. SOFTWARE PASS: given 1+2 and the current bottlenecks, ask "would a
   software-engineering effort materially accelerate us?" (precedent: the
   FLINT tower-elimination engine replacing sympy = orders of magnitude).
   Software gets the same tri-model treatment: one model builds, another
   reviews the code.

## STANDING QUEUE (loop reads this; keep current)
- ACTIVE (live lanes; see ops/status.sh): box01 pilot (compressed p105337, cap ~13:40) + fc1_audit (445 states); Sol x2 (REDUCTION.md consolidation, residue-A algebraization kill)
- ON PILOT VERDICT: viable => Box02 restart (compressed campaign) + Box03 restart (char-0 certification wave for farm EMPTYs); fail => Sol instrument round 2
- NEXT THEORY: uniform-td track (FC1-R -> FC-batch review gauntlet; td-11 refile prep; td-13 new math: 13B-SAFE-SUFFIX + MAX/SIM-X); l12 eta0 certification (folded into algebraization lane route c)
- WRITING: paper-2 Part I (gated on residue-A verdict); A-prime note; paper-1 v3 HELD for GGV
- COMMS (DC decides): Horruitiner add-to-thread rec'd; Helali/Suzuki coordinated-note thread rec'd; drafts on request
- PERIODIC: accel+lateral scan w/ Sol ~6h; fleet cost sweep; GCP disks (300G) deletion = DC call
- GATED ON DC: anything external; msolve upstream report (HOLD)

- 2026-08-14 ~20:15: LEAF a3 CONFIRMED EMPTY AT TWO PRIMES (GB [1] at p105337 instant +
  p200257 confirm). Chamber map: 13 pre-dead (theorems) + a3 double-EMPTY; remaining =
  b1,b2,b3,a1,a2,a0 (6 lanes running, new-style). If all leaves empty at 2 primes =>
  partition => full nolog system EMPTY mod p => residue-A screening-tier death =>
  char-0 certification run => on-axis td=6 closes. Watch for a1/a2 next (similar
  size class to a3).
- 2026-08-14 ~20:25: OPS SLIP (mine): the broad-leaf cull pkill patterns also matched
  the NEW leaves2 process names — killed b1-b3/a1/a2 19min in (rc=143). Relaunched
  with L2GEN tags. LESSON banked: pkill patterns must include the generation
  discriminator (directory or tag), never bare leaf names.
- 2026-08-14 ~21:35: sat23 p105337 FAILED at 37h/1.6TB (ultramem vcap — same structural
  cliff class as l8); p105673 twin killed preemptively (identical death predicted);
  sat23-as-monolith RETIRED (decomposition only if the chamber map leaves it relevant).
  ULTRAMEM STOPPED (no active lanes; cost sweep). td-11 nested closure promoted.
- 2026-08-14 ~22:55: Box03: c1.RED died rc=137 (OOM, 21:48 — my earlier solo-pause
  pkill evidently failed silently; SECOND pkill-verification lesson today). One lane
  survives (identifying). Chamber lanes: 1003G, heavy b-chambers grinding, no new
  verdicts. NF-P banked; compiler top of queue.
- 2026-08-15 ~02:00: CHAMBER MAP partial failure — a1/a2/a0/b1 all died at the 120G
  fences (rc=139, UTC 10:37-14:52). Diagnostic: F4 hardness is NOT concentrated in
  one chamber; even 67-eq subchambers exceed 120G. Sol's caveat (input shrinkage !=
  F4 shrinkage) proved out. b2/b3 still running; R2 mains ~22h in (~26h to caps),
  Box02 at 1685G/2T — NO new load on Box02 (OOM risk); failed chambers re-queue
  post-drain with 300G fences ONLY if mains cap out empty-handed. Sol census review
  process died silently — relaunching. a3 remains the only computed chamber verdict
  (double-EMPTY).
- 2026-08-15 ~19:45: SESSION GAP ~17h (machine asleep). Catch-up: Sol census review
  BROKEN (M_G|sum(mu_e) misapplied outside epsilon=0=k scope — real quotient hole);
  Box03 both cores OOM at 495G -> STOPPED (big cores 3-for-3 beyond iron; sat23 1.6T,
  c1.RED 495G, c2.q 495G — decomposition-only, deprioritized); Box02 healthy: b2/b3 +
  R2 mains + portfolio grinding at 1736G, caps Aug16 ~03:50; a3 still the only chamber
  verdict. NEXT: census repair (the misapplied divisibility row), then re-review.
- 2026-08-15 ~22:45: FC ladder: 4 of 7 discharged in one evening (FC6,FC7,FC2,FC4);
  certificate now conditional on FC1 (beyond-core, days-scale computational route),
  FC5 (merged-emission w law — ONE new lemma), FC3 (refile — the wall). Next theory
  slots: FC1 computation, FC5 lemma attack. Screens ~5h to caps; big scan at expiry.
  After FC1+FC5: the td-11 panel rests on the refile alone — same shape as td-7's
  endgame before its census. Review gauntlet for the FC-discharge batch queued.
- 2026-08-15 ~23:50: FC5 = THE MERGED-EMISSION LAW (w'=kbar(d_q-1)/(nu d_q), M'=gcd)
  — the (c2) gap closed as a formula, trunk-certificate-verified. FC1 fleet lane:
  agent's box01 launch had NOT actually landed (verification caught it — ops lesson
  #3 this week: always verify remote launches by process count); shipped + launched
  properly, 1 proc confirmed. On clean FC1-R: certificate conditional on REFILE ALONE
  => FC-batch review gauntlet (all 6 discharge lemmas + FC5 law, dual review).
- 2026-08-16 ~00:15: FC1 lane launch saga (3 attempts: missing script, missing px2 dep,
  stale-snapshot race) — now VERIFIED running on box01 (import OK, proc confirmed,
  log streaming). Ops lesson compounding: remote lanes need dep-manifest + import
  smoke test in the launch script itself.
- 2026-08-16 00:05: Order-portfolio lanes BOTH capped out (29h, rc=124) — the ordering
  lottery LOST (neither reordering beat standard; GB hardness is order-robust here).
  FC1 audit healthy (300 pops/187 states/956s, growing BFS). 4 lanes to caps ~03:45.
- 2026-08-16 ~09:00: Interventions: (a) elim pivot curve steep (740/2483/9650s) —
  agent tasked with tau-transport shortcut (map tf1->tf2 images) or partial 11-pivot
  emission fallback; (b) FC1 NOT wedged (99.9% CPU, 60MB, 9.9h) — genuinely deep in
  one expensive state; let run (cheap on box01), revisit at 24h.
- 2026-08-16 ~11:40: PILOT LAUNCHED on box01 (compressed p105337, 2h cap, -t 4,
  process-verified; marked PROVISIONAL until the agent's formal guard report lands —
  emit log shows 0 FAIL). The 3x gate: R1 baseline = 12h timeout, so ANY verdict
  within the 2h cap clears the gate with margin; timeout at 2h = inconclusive
  (extend to 12h apples-to-apples before iron decision).
- 2026-08-16 ~13:30: DC directives executed: (1) GCP confirmed fully shut down (both
  instances TERMINATED; 2 disks remain ~300G — deletion = DC's call; AWS-ONLY policy
  in FLEET.md); (2) AWS spare capacity: Box02 restart DECISION GATED on pilot verdict
  (minutes away) — if compressed viable: full compressed campaign on Box02 + char-0
  certification wave for banked farm EMPTYs on Box03 (converts mod-p evidence toward
  claimable, uses idle capacity); (3) residue-A + reduction-chain lanes launched in
  parallel w/ uniform-td (Sol co-researcher x2: REDUCTION.md + algebraization kill);
  (4) Sol = equal co-researcher standing; loop directive simplified.
- 2026-08-16 ~13:40: Pilot 2h: TIMEOUT at 92.7GB (rc=124) — no quick win, but box01
  turns out to have 991G RAM (assumption corrected in FLEET next edit). PILOT12
  launched: 12h cap, -t 8, apples-to-apples vs the R1 12h baseline that timed out
  on the RAW system. Verdict inside 12h = compression helps; timeout = mod-p
  compression dead-end => Sol instrument round 2 (char-0-direct / structural /
  park). Box02/Box03 stay STOPPED (box01's 991G suffices for this).
- 2026-08-16 ~15:10: NEW STANDING DISCIPLINE (DC): daily external-progress sweep
  (X/arXiv/blogs) + fresh lateral-avenue generation, tri-model (Fable web + Sol +
  Grok). First run launching now.
- 2026-08-16 ~16:00: COMMS POLICY (DC + refinement): two-track. Math developments =
  track ALL sources on content. Citation = merit/priority only, NEVER credential-
  filtered (Helali keeps priority citation). Collaboration = two tiers: verification
  exchange open to all competent actors (Zenodo notes, artifact replay); endorsement-
  relevant outreach filtered to published authors. arXiv path = GGV/Horruitiner
  thread, fallback cold-credentialed (van den Essen circle / Orevkov line). Intel:
  Helali = non-mathematician (DC LinkedIn chat) — artifact more impressive, check
  his methods section for AI provenance before any joint note names methods.
- 2026-08-16 ~16:40: SOFTWARE PRIORITY (DC): FLINT tower-elimination engine build
  launched (window agent) — split-prime GF(p) band elimination = seconds/prime, no
  swell => TRUE ~36-var core per prime (PILOT12 grinds a HALF-compressed 68-var
  object with inherited swell). Gates: agreement with sympy 16-pivot ground truth
  mod p; tau; anchor/+42 survival. On core emission: multi-prime portfolio + (if
  core resists) triangular-decomposition diversity + tau-folding. Reusable for the
  3 OOM'd farm cores + Q2 strata. PILOT12 races on meanwhile (~3h to cap).
- 2026-08-16 ~23:15: FLINT engine DELIVERED: 25,000x (16 pivots in 0.2s vs days);
  TRUE CORES emitted (43v/67eq/21.9k terms/prime, guards 18/18) and 3 core lanes
  LAUNCHED on box01 (12h caps, process-verified: 5 msolve) racing PILOT12 (332GB,
  ~2.5h to cap). Any core verdict = the residue-A signal. Engine is reusable infra
  (farm big cores, Q2 strata next).
- 2026-08-17 ~00:25: box01 ssh outage = local IP drift again (.205 -> .202; SG rule
  added — ops pattern #3, consider a /24 or automation). PILOT12: TIMEOUT at 12h cap
  (rc=124) — the half-compressed object officially dead-ends; the 3x gate outcome is
  moot because the TRUE cores superseded it mid-race. 3 core lanes alive (~1h in).
- 2026-08-17 ~11:35: CORE LANES CAPPED (both rc=124 at 12h, 221G steady) — the TRUE
  43-var core is Groebner-hard at this budget: raw 48h fail + compressed 12h fail +
  core 12h fail + a3 double-EMPTY = the complete instrument dataset. Sol round 3
  launching. FC1 stalled-deep (595 states unchanged ~11h — kill+partial next tick
  if no movement). box01 down to farm only.
