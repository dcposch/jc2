# REDUCE4-REVIEW.md — Adversarial review of lib/reduce4.py + Phase 2c bank

Date: 2026-07-24. Reviewer: adversarial pass (no commits).

## Front 1: Gates 2a/2b vs paper propositions (re-derived)
- Tests: `python3 tests/test_reduce4.py` -> ALL PASS (9 test funcs).
- Paper /tmp/jcrefs/2204.14178.tex sec.4 (lines 457-1398) re-read:
  - Prop 4.1 (9,27): N(P)={(0,0),(1,1),(6,16),(6,18),(0,18)},
    N(Q)={(0,0),(1,0),(9,24),(9,27),(0,27)}, [P,Q]=x. Matches REG_9_27.
  - Prop 4.2 (9,24): 3 subcases, all match REG_9_24 constants verbatim.
  - Prop 4.3 (8,28): [P,Q]=x^2; paper subcase (1)=c) with (0,8)/(0,12),
    (2)=a)+b) merged. Both match OPEN_8_28; merge behavior matches paper.
  - Prop 4.4 (7,21): [P,Q]=x, N(P)={(0,0),2(2,0),2(3,1),2(0,7)}
    ={(0,0),(4,0),(6,2),(0,14)} -> matches REG_7_21.
  - Start polygons (0,c): paper c=9,6,4,7; CornerData c=v_{1-j,1}(A0)
    gives 9,6,4,7; engine re-derives via continuations (log checked).
  - rhs_exp=ceil(b0/a0)-2 -> 1,1,2,1 = paper x,x,x^2,x.
- Tests compare engine output (reduce_family runs live) to constants that
  I verified against the tex verbatim. No name-based special-casing found
  in the engine path.
- STATUS: CONFIRMED

## Front 2: Hand re-derivation of one Phase 2c family
- Target: (11,33)+(2,3) d132 (smallest banked). Data: A0=(11,33),
  A0'=(3,1), steps=((4,-1,3,11),), c=11, final=(19/4,8).
- Hand-checked every step against the design algorithm:
  q0=11 ((q_k): v_{4,-1}(A0)=11, gcd(3,11)=1); enR=(33,11)/11=(3,1) lattice ok;
  Alg1(3,1)={(1,0)} + case1 dup; (0,0)-ray killed by R6 pre-Laurent; c=11
  matches GGV5 table. StageA face (11,0)->(33,11)@(1,-2), zdeg 1, single
  shape [1] (312-case1: 33-22=11>0), e_2 collapse; B2 -> only (0,0)@(1,-3).
  Chain edge (1,3)->(33,11): K=4, zdeg=8=final.b -> single root; e_4 cut,
  y^3 prefactor tail to (33,11)-3(4,1)=(21,8). R9 at (21,8), inc (-1,4):
  k=1 only ((k+1)8<21); (eP,eQ)=((-1,0),(2,1)) cross 13 killed;
  ((2,1),(-1,0)) cross 0, fd=(-3,8) survives. Aligned: region
  {D>0, v_inc<11} forces b2<8 (rect covers); survivors (5,2),(13,5) die
  on fd==dW colinearity (same as paper 4.1 note). Finalize: j=3,
  psi_3(2*{(0,0),(33,11),(21,8)}+{(2,1)}) = {(0,0),(1,1),(0,22),(6,16)};
  3-fold+(-1,0) -> {(0,0),(1,0),(9,24),(0,33)}; rhs x^1.
- MATCHES banked entry exactly (polygons, RHS x, 1 subcase).
- Soundness caveats found while deriving -> see Front 4 (chain-edge
  single-root justification; R9 hypothesis provenance).
- STATUS: CONFIRMED (arithmetic); soundness deferred to Front 4

## Front 3: Invariant sweep over all Phase 2c outputs
- Re-ran engine on all 3 banked keys + every above-125 row (23 rows).
- Banked: bank == fresh engine output (sets equal). RHS rule
  ceil(b0/a0)-2: 11_33->1, 9_36->2, 8_40->3, all match cd.rhs_exp and
  banked rhs. Origin in NP,NQ; no negative coords; corner lists are their
  own hulls; apex corner (0, fold*a0) present in every case; proportional
  -part check: NP/NQ differ in at most one corner pair (the R9 ends) —
  for partials they are exactly (n/m)-proportional. NO FAILURES.
- Subcase exhaustiveness: banked counts = c-derivation branch counts
  (11_33: {11}->1; 9_36: {9,18}->2; 8_40: {8,16,24}->3); within each
  branch zdeg=1 forces a single B1 shape and a single B2 ray, checked by
  hand. 9_36/8_40 carry sound EXTRA subcases beyond GGV5's table c-value
  (engine re-derives (0,c) per design S2 and keeps all candidates).
- 9_36/8_40 are PARTIAL reductions (chain edge uncut, interference guard
  logged); provisional Laurent tails kept as real corners — verified the
  tail endpoint coefficient lam^d cannot cancel (off-edge terms sit at
  strictly lower v_{1,-K}), so hulls are exact.
- Latent (no banked impact): tail_resolve's aligned-candidate rectangle
  is provably complete only when v_incoming(V)>0 (holds: 11,4,1 in all
  uses) — the code never asserts it. Flagged for hardening.
- STATUS: CONFIRMED

## Front 4: Branch-kill rules — justification audit
Kill-rule ledger (rule -> source -> audit):
1. dir-strictly-decreasing + v>0 rejects (continuations): GGV1 Cor 7.4
   hyp/concl (v_{rho,sigma}(P)>0, Pred order) — statement re-read at tex
   1401.1784:4238. JUSTIFIED.
2. R6 axis-reachability kill: vdE 10.2.6 + Alg-1 recursion = paper 4.2's
   "(2,-5) -> Pred<=(1,-3) -> deg_x P(x,0)<=0" verbatim generalization;
   trichotomy completeness = Alg 1 (cases 2,3) + case1_singles (case 1,
   incl. v_{1,-2}(en)>0 addendum). Reproduced paper kills exactly.
   JUSTIFIED.
3. R4 shape kill (prop312_consistent): GGV2 Prop 3.12 (re-read, tex
   1605.09430:720): faithful trichotomy filter, applied at the R^q level
   exactly as the paper itself does (4.2 uses R^3 data st (12,3), N1=6,
   N2=3); drops t'<l*theta and dir-orientation => strictly conservative
   (under-kills only). JUSTIFIED (conservative).
4. R5 lambda_1!=0: not a check but a coverage argument — the lambda=0
   world is an enumerated sibling branch (verified: 9_24's (6,2) sibling
   killed by R6 = paper's own argument; (4,1)+[2] zero-root variant dies
   on axis check while its [(4,1),(0,0)] sibling merges into subcase 1).
   SOUND, but log wording "proven" overstates when the sibling survives
   (still sound: world covered by sibling). JUSTIFIED with nit.
5. _axis_ok kill + apply_cut "+x spread excluded": NO direct numbered
   citation. It formalizes the papers' silent hull claims (post-phi_2
   corner lists): Cor 7.4 powers at intermediate directions force
   lattice en(R)/st(R), killing unauthorized positive-axis corners.
   Design R1-note prescribes it. Main trust point of the engine; matches
   paper practice (paper is no more explicit). DESIGN-JUSTIFIED.
6. R9 non-parallel kill: Prop 8.2 st-proportionality (proof eq
   `proporcionalidad`) = paper 4.3's k=2 kill. JUSTIFIED.
7. R9 same-direction (colinearity) kill: paper 4.1's parenthetical
   ("different end for direction (-3,8)"). JUSTIFIED.
8. R9 direction-window ]incoming,(-1,1)[: Prop 8.2 proof line. JUSTIFIED.
9. R9 aligned diagonal kill: paper 4.1 + GGV2 st not in N(1,1). JUSTIFIED.
10. R9 divisibility kill D | (a-b)*gcd: derivation re-done (v_{-b,a} on
    the F-corner identity); reproduces paper 4.1's 13-gcd table verbatim;
    generalization to arbitrary V assumes the (1,1)-cornered F exists at
    the successor direction (Cor 7.4/Thm central hypotheses hold
    pre-final) — paper only instantiates (21,8),(24,7). DESIGN-JUSTIFIED,
    conservative for non-coprime V (need is g'-times weaker).
11. R8+R7 discard: GGV22 S2 (8,32) argument 1:1 (Thm 7.6(5) q1|d0
    confirmed in GGV1 tex; d0 bounds are pure lattice; PLLC via GGV5
    Alg 1, gate-A-tested). JUSTIFIED.
12. Interference guard (chain edge kept uncut when apex e_K respawn at
    x>0): engine-original, REFUSES rather than kills => conservative.
    SOUND.
- Prop 2.11(3) (design S8.2) is not implemented; the engine enumerates
  all partitions instead => superset of allowed shapes, conservative.
- Overall: every kill traceable to a cited result or to the design's
  R1-note re-derivation argument; no unsound overreach found, but rules
  5 and 10 rest on the design's generalization, not on a quotable
  numbered statement.
- STATUS: WEAKENED (soundly conservative; two rules design-level only)

## Front 5: `stuck` pathway integrity
- Real inputs (34-row sweep): 12 rows stuck, honest reasons, zero cases:
  "multi-root chain edge" (final.b != zdeg, e.g. (12,33)+(11/3,8): zdeg
  11 vs gamma 8) and "psi_j precondition fails: support point (8,0) with
  i>0" ((12,36) 3-chains, (10,40) rows). No fabrication; no
  reduced-with-0-cases wart observed.
- Synthetic probe: tampered 9_27 steps q0=9->7 => "first certificate:
  en(R) = (27,9)/7 not a lattice point (R1 lattice test fails)", status
  stuck, no cases. Engine refuses rather than guesses.
- Note: a Stuck raised while finalizing ONE branch aborts the whole
  family (valid sibling branches discarded) — lossy but safe.
- STATUS: CONFIRMED

## Verdict
- Tests: all reduce4 + families suites pass; gate constants verified
  against the paper tex independently (Front 1).
- The engine is a faithful, conservative mechanization of GGV22 S4: it
  reproduces the four propositions from Phase 1 data, its kills are
  cited or design-sanctioned-conservative, its stuck path is honest, and
  the banked above-125 outputs survived a full invariant sweep plus an
  independent hand re-derivation of (11,33).
- PROMOTION: YES — promote ABOVE125_UNVALIDATED to farm-ready as
  "engine-validated (G1-G3-class evidence), literature-unverified",
  with three riders: (a) run the design's G4 cross-check lane before any
  publication-grade claim; (b) assert v_incoming(V)>0 in tail_resolve;
  (c) keep 9_36/8_40 labeled partial (chain edge uncut) so the farm
  treats them as bigger-but-sound Generator-A inputs.
