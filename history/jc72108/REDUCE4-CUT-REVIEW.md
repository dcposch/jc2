# REDUCE4-CUT-REVIEW.md — Adversarial review of the multi-root chain-edge cut
# (stuck-family closure, SECTION4-AUTOMATION.md 2026-08-11 + lib/reduce4.py)

Date: 2026-08-11. Reviewer: adversarial pass (no commits). Scope: the
multi-root e_K cut (`_chain_edge_data`/`_cut_chain`), the direct-emission
fallback (`_prepsi`/snapshot + no-progress guard), the 12_36_r1_c3
EMPTY-BY-CASCADE verdict, and the 22-row byte-identity claim.

## Front 1: The cited proposition (GGV5 Def 2.6 + `multiplicidad`(4))
- Source re-read: /tmp/jcrefs/1708.07936.tex. Proposition `multiplicidad`
  (tex 505) is Prop **2.5** in this tex's numbering, not 2.6; "2.6" is
  Remark `comentarios0` (simple roots for type-I corners). No Definition
  2.6 exists; the operative definitions are Γ = set of multiplicities
  (tex 623, = 2.8) and the A_(γ) display (tex 642–646, unnumbered).
  The same mislabel is in reduce4.py:755/768, tests/test_reduce4.py:253,
  and lib/families.py:208. CITATION WRONG AS WRITTEN.
- The mathematics: `multiplicidad`(3) gives only m_λ/m ≤ v01(A−A′)/gap,
  with EQUALITY only when the edge is simple; (4) gives only existence of
  SOME root with b′ < (ρa+σbl)/(l(ρ+σ)) ≤ m_λ/m. Neither pins
  "multiplicity exactly γ" as a theorem — and for these families the last
  edge is NOT simple (12_36_r0: gap=3, γ_max=11, family γ=8 < 11).
- Where exactness actually comes from: Remark `comentarios` (tex 594)
  defines γ := m_λ/m, and Remark `bala` (tex 743–767, items (4),(5)):
  A_(γ) = A₁ via GGV1 Prop 5.18(3), with b′ < γ ≤ γ_max. The enumeration
  BRANCHES over every γ ∈ Γ (GetGeneratedCorners); a family row FIXES γ =
  final.b. So "the cut root has multiplicity exactly γ" is a
  family-branch datum, exhaustive across catalog rows (all admissible
  chains ≤ deg 150 are swept), not a per-family theorem. The
  implementation USES it exactly that way (γ = cd.final.b, per-row), so
  the behavior is sound; the comment's "pin ... at multiplicity EXACTLY"
  overstates the citation, not the code.
- Hypothesis check: `multiplicidad` requires an (m,n)-pair in L^(l)
  (standard if l=1) and a regular corner — satisfied at the last chain
  edge (l=1 start triple, type II.b); the guard stE.y ≥ 1 and
  stE.y < γ < zdeg matches bala(4)'s b′ < γ in the flipped frame plus the
  multi-root condition. Table spot-check: F7 (6,15)→(7⁄3,4), γ=4 matches
  cd.final for 6_15mn27d147; 12_36 rows are engine-enumerated (beyond the
  paper's M=35 tables) with the same Γ rule.
- Mid-chain transforms: a second type-II.b step would make chain corners
  fractional; `_chain_edge_data` then refuses ("fractional corners") —
  the ρ=2 rows (12_36_r1/r2 etc.) hit exactly this and fall back. Sound.
- STATUS: WEAKENED (mathematical content CONFIRMED as branch-exhaustive
  enumeration data; the "Def 2.6 / multiplicidad(4) ⇒ exactly γ" citation
  is wrong-as-written and should be re-pointed to Prop 2.5(3),(4) + Γ/A_(γ)
  + Remark `bala`).

## Front 2: Support-exactness + partition-independence (re-derived)
- From scratch: e_K(α): y ↦ y + αx^{−K} preserves v_{1,−K} of every
  monomial (image of (i,j) spans (i−tK, j−t), all at v = i−Kj). Level
  form x^c y^d (z−α)^γ Π(z−β_i)^{t_i}, z = x^K y, rewrites exactly to
  x^{c−Kd}(z+α)^d z^γ Π(z−β′_i)^{t_i}, β′_i = β_i−α ≠ 0; support =
  {(c−Kd+Kj, j) : γ ≤ j ≤ d+zdeg}; endpoints j=γ ↦ V = stE+(γ−d)(K,1)
  with coefficient α^d·Π(−β′_i)^{t_i} ≠ 0 and j=d+zdeg ↦ enE with
  coefficient 1. Both exact for EVERY partition {t_i}; interior points can
  vanish (e.g. coefficient α−β₁−β₂ at j=γ+... for [1,1]) but are collinear,
  so the hull is partition-independent. Off-face images stay at strictly
  smaller v_{1,−K}, so nothing re-enters the face line: V is a genuine
  corner and [V,enE] a genuine face. Roots nonzero: p(0) ≠ 0 because the
  st corner (= (1/m)st(P) = A0′-exact) absorbs the full z-power.
- Adversarial example run: edge (1,1)→(9,5), K=2, zdeg=4. Engine
  `_cut_chain` γ=2 → hull {(0,0),(10,5),(9,5),(3,2)}, residual
  ((3,2),(−1,2)); γ=3 → (5,3); both equal my hand computation including
  the off-face tail (10,5)→(0,0). A naive apply_cut-style cut at the
  largest remaining root WOULD be partition-dependent (face start (5,3)
  for [2] vs (3,2) for [1,1]); the implementation takes no partition input
  at all and cuts the γ-root — correct.
- STATUS: CONFIRMED

## Front 3: Variety preservation + residual V arithmetic
- The correspondence chain per branch world: original pair —φ₁→ flipped
  (bracket sign) —e_K(α)→ Laurent pair (bracket invariant) —ψ_j→
  polynomial pair with [ψP,ψQ] = −c·x^{j−2}. All three transform laws
  verified NUMERICALLY mod 65521 on random polynomials (e_K bracket
  identity, ψ_j law matching finalize's logged formula, flip law). Torus
  normalization: fixing 2 corner coefficients + the rhs coefficient to 1
  is a 3×3 log-linear system whose determinant I re-derived =
  w(pP)+w(pQ), exactly `torus_fix`'s rule (manifest dets −120/120/15 ≠ 0);
  lossless for emptiness over the closure (finite cover).
- It is a COVERING (injection of true-pair worlds into emitted-system
  solutions), not a bijection: supports are over-approximated and only
  exactness-proven corners are saturated. That is the documented design
  stance (S5/S6, `_prepsi`/fix_ones docstrings) and is sufficient for
  EMPTY verdicts; it would NOT support a nonempty-witness claim. The doc's
  wording ("support-exact ... feeds the standard R9 step") does not
  overclaim equivalence.
- Residual V by hand, family 1 (12_36_r0): last edge flipped
  (0,1)→(33,12), K=3, zdeg=11, γ=8, d=1 ⇒ V=(0,1)+7(3,1)=(21,8) ✓;
  R9 at (21,8) inc (−1,3): k=1 only; ((2,1),(−1,0)) parallel
  (cross((−40,−15),(−64,−24))=0), fd=(−3,8) in ](−1,3),(−1,1)[ ✓,
  mirror order killed (cross 13) ✓, aligned (5,2),(13,5) die on
  colinearity ✓; ψ_3 of 2×{(0,0),(36,12),(33,12),(21,8)}+(2,1) =
  {(0,0),(1,1),(6,16),(6,24),(0,24)}, 3-fold+(−1,0) =
  {(0,0),(1,0),(9,24),(9,36),(0,36)}, rhs x — matches the emitted case
  and the banked pin exactly. Family 2 (6_15): (0,1)→(15,6), K=3, zdeg=5,
  γ=4 ⇒ V=(9,4) ✓; cross((−16,−7),(−64,−28))=0, fd=(−7,16) ✓; ψ_3 gives
  the {(0,0),(1,1),(6,8),(6,12)} / {(0,0),(1,0),(21,28),(21,42)} pair ✓
  (both engine cases reproduced live).
- STATUS: CONFIRMED (as a documented covering; adequate for EMPTY)

## Front 4: The first verdict — 12_36_r1_c3 EMPTY-BY-CASCADE (replayed)
- Rebuilt SystemA from the manifest polygons (NP {(0,0),(24,6),(24,24),
  (0,8)}, NQ {(0,0),(36,9),(36,36),(0,12)}, rhs x², fix (P,(24,24)),
  (Q,(36,36)), det −120) and ran Cascade3 fresh: **EMPTY at 0.0 s**, same
  core_eqs (1964) as the banked record.
- Kill isolated and hand-verified: the bracket coefficient at monomial
  (2,0) is IDENTICALLY zero on these supports — the only y=0 lattice
  point of either polygon is the origin, whose derivatives vanish, so
  every product contributes i₁j₂−j₁i₂ = 0 — and the equation
  coeff((2,0)) = 1 reads −1 = 0. This is precisely the coefficient-level
  mirror of vdE 10.2.6 (deg_x P(x,0) = 0) predicted by the conservatism
  note. Faithfulness: manifest cases c1–c4 match a fresh reduce_family
  run 1:1 (NP/NQ/rhs, label permutation recorded); transform identities
  verified mod p (Front 3); r2_c3 has identical polygons, so the transfer
  to 12_36_r2_c3 is legitimate.
- Caveat on WEIGHT, not validity: c3 is the origin-ray world that the
  engine over-emits ON PURPOSE (applying the vdE kill would retract
  banked 12_30 cases). The EMPTY verdict retires an engine-internal
  conservative world; it is not evidence about the family's main worlds
  (c1/c2/c4 are PARTIAL, still open).
- STATUS: CONFIRMED (verdict stands)

## Front 5: The 22-row byte-identity regression (rerun)
- PROVENANCE WART: commit 33021f4 touches ONLY SECTION4-AUTOMATION.md.
  The actual engine change (lib/reduce4.py +129, lib/farm.py +12 p-hygiene
  fallback, tests/test_reduce4.py +51, ops/stuck7_post.sh) is silently
  bundled inside 42377a6 ("housekeeping"). The commit message's claims are
  accurate but attached to the wrong commit; audit trails pointing at
  33021f4 for the code diff will come up empty.
- Rerun against the true pre-change engine (76ca37a:lib/reduce4.py),
  serializing status + full case data for all 34 catalog rows: exactly
  **22 IDENTICAL, 12 stuck→reduced**, case counts 1/4/4/3 (12_36 r0–r3),
  2 (6_15), 8/8 (10_40), 10 (12_33), 4 (8_28), 3/1/3 (the 5_20
  byproducts); rhs multisets match the inventory table verbatim
  (e.g. r1 [0,1,2,2], 10_40 [0,0,0,2,2,3,3,3]). r1/r2 case sets equal
  (twin-transfer premise verified). Full suite: ALL REDUCE4 TESTS PASS,
  including the new test_stuck150_closure pins.
- Spy-check reproduced: none of the 12 changed rows exercises
  apply_cut's shortened-face-with-prefactor path (the latent
  under-approximation from REDUCE4-REVIEW Front 3 stays unexercised).
- STATUS: CONFIRMED (numbers exact; commit provenance mislabeled)

## Front 6: The fallback path (ρ=2 direct emission) + guards
- Refusal mechanics verified live: 12_36_r1's chain edge refuses as
  "fractional corners" (mid-chain L^(4) corner (21/4,9)); the certified
  (4,1)@(2,−5) face has fdir[0]=2 ⇒ K=None, kept uncut. `_prepsi`
  polynomial leaves emit as-is (all ops bracket-constant ⇒ [P,Q] ∈ K^×,
  rhs x⁰); Laurent-mixed leaves emit the pre-stage-A polynomial snapshot
  (coords ≥ 0 asserted) — invertibility covering, strictly bigger, sound.
  Checked 12_36_r1_c2: NP = 2·S, NQ = 3·S for the same snapshot S
  {(0,0),(4,0),(16,4),(36,12),(0,3)} ✓ proportional as required.
- No-progress guard: fires on 10_40's (5,1)→(8,2)@(1,−3) face (q=5,
  dtail 5 ≥ face z-length 5 — the cut would exactly re-span the face);
  arithmetic checked. NOTE: the firing lines are swallowed from the
  merged family log by the flog-truncation in `_reduce` (visible only
  per-branch) — an observability wart, not a soundness one.
- SystemA conventions on the emitted system: header (varnames / char /
  ","-separated rows), a*/b*/t naming, corner saturation t·Πcorners = 1
  (nonorigin), fix_ones corners removed from the variable list, torus det
  ≠ 0. Guards re-run independently: ops/reduce_msp.py on r1_c4 →
  round-trip PASS (2 random points, independent parser), regenerated
  .RED.ms **byte-identical** to the banked twin; paren-free and token<p
  asserts present; p-hygiene path exercised on r1_c2 ("coeff vanished
  mod p" → char-0 emission recorded in the manifest, farm.py fallback
  code confirmed).
- Rider: saturation of snapshot corners relies on within-branch corner
  attainment (branch-world semantics, prior review Front 4 rules 2/5);
  inherited, not new risk.
- STATUS: CONFIRMED

## Verdict
- The multi-root cut is mathematically CORRECT: support-exact,
  partition-independent, level-preserving, with V = st+(γ−d)(K,1) exact —
  re-derived from first principles, hand-checked on 12_36_r0 and 6_15,
  and adversarially probed on synthetic polygons. The γ = final.b usage
  is sound as exhaustive branch data even though the quoted "Def 2.6 /
  multiplicidad(4) ⇒ exactly γ" citation is wrong-as-written (Front 1).
- 12_36_r1_c3 EMPTY-BY-CASCADE STANDS (replayed; kill = coefficient-level
  vdE 10.2.6 mirror; transfers to r2_c3), with the weight caveat that it
  retires a deliberately over-emitted world.
- PROMOTION: YES — promote the multi-root cut and the fallback emissions
  to the same evidence class as the reviewed single-root engine
  (farm-ready, engine-validated, literature-unverified), with riders:
  (a) fix the GGV5 citation in reduce4.py/SECTION4-AUTOMATION/tests to
  Prop 2.5(3),(4) [label `multiplicidad`] + the Γ/A_(γ) definitions +
  Remark `bala`, and rephrase "exactly γ" as a family-branch datum;
  (b) record in the ledger that the engine change physically lives in
  commit 42377a6, not 33021f4; (c) keep EMPTY-BY-CASCADE-on-ray-worlds
  labeled as conservative-world retirements, not family kills; (d) the
  no-progress-guard log truncation is worth a one-line fix before the
  next farm audit.

## Relaunch verification (2026-08-12, independent re-run; no commits)

The prior pass died at a spend ceiling after writing this file; every
front above was re-verified FROM SCRATCH (fresh source reads, fresh
scripts, fresh hand arithmetic) rather than trusted. All of it holds:

- F1: /tmp/jcrefs/1708.07936.tex re-read. Counter check (intro is
  \section*, notation shares the theorem counter, algorithm floats do
  not): `multiplicidad` = Prop 2.5 (env #5 of section 2), `comentarios0`
  = Remark 2.6, Γ-def = Def 2.8, `admisible` = Def 2.11, `bala` items
  (4)/(5) as quoted. Prop 2.5(3) is an inequality (equality iff simple);
  (4) is existence-only — "exactly γ" is indeed NOT a theorem there; the
  branch-datum reading via Remark `bala` + the Γ sweep (families.py:200
  matches Γ with b′ excluded per bala(4)) is the correct justification.
  POST-FIX STATE: commit 4d50e8b applied the F1 rider to lib/reduce4.py
  (both comment sites) and SECTION4-AUTOMATION.md. STILL STALE:
  tests/test_reduce4.py:253 ("GGV5 Def 2.6 + Prop `multiplicidad`(4)")
  and lib/families.py:209 ("Definition 2.6 admissible" — should be
  Definition 2.11 `admisible`). Rider (a) is therefore HALF-APPLIED.
- F2: re-derived independently; fresh exact-Laurent script (edge
  (1,1)→(9,5), K=2): endpoints V/enE exact with predicted extreme
  coefficients for γ=2 [2], γ=2 [1,1], γ=3 [1], plus a NEW adversarial
  interior-vanish instance (α=6, β=8,10 ⇒ the (7,4) support point
  vanishes; hull unchanged). Engine `_cut_chain` matches all cases;
  residual ((3,2)/(5,3), (−1,2)) confirmed.
- F3: e_K/φ₁/ψ_j bracket laws re-verified mod 65521 (5 fresh random
  trials each). 12_36_r0: V=(21,8), R9 k=1 cross 960−960=0, mirror kill
  13, fd=(−3,8), aligned (5,2)/(13,5) die in recursion, ψ₃ hand-applied
  reproduces the banked polygons exactly. 6_15: V=(9,4),
  cross((−16,−7),(−64,−28))=0, fd=(−7,16), both cases reproduced.
  Torus dets re-derived by the w-rule by hand: −105 (r0_c1), −120/120/
  −120/15 (r1_c1..c4) — all match manifests, all ≠ 0.
- F4: rebuilt SystemA from the r1 manifest and re-ran Cascade3: EMPTY at
  0.0 s, core_eqs 1964 = banked. Kill re-verified two ways: structurally
  (only y=0 lattice point of either polygon is (0,0) ⇒ coeff((2,0)) of
  [P,Q] ≡ 0 vs rhs x²) and numerically (3 random mod-p points). NEW:
  all 1960 SystemA bracket equations checked against an independent
  double-loop coefficient computation at a random mod-65521 point
  (+ saturation eq) — exact match. r1/r2 manifest case sets equal;
  r2_c3 banked EMPTY-BY-CASCADE; fresh reduce_family = r1 manifest 1:1.
- F5: tests/test_reduce4.py ALL PASS (0.7 s). Fresh 34-row diff vs
  76ca37a:lib/reduce4.py (families.py drift since 76ca37a: NONE):
  22 identical, 12 stuck→reduced, case counts/rhs multisets verbatim
  (3/1/3 for the 5_20 byproducts, whose manifests remain the 2026-08-07
  REDUCE4-STUCK stubs — "not re-emitted" confirmed). Spy-check re-run:
  0 hits on apply_cut's shortened-face-with-prefactor path across the
  12 changed rows.
- F6: fractional-corner refusal re-confirmed with the actual chain datum
  (last edge A = (21⁄4, 9), l=4). No-progress guard verified to FIRE by
  instrumented engine copy: 3 firings, all on face (5,1)→(8,2)@(1,−3)
  (arithmetic q=5, prefactor 5 ≥ z-length 5 re-checked). prepsi case
  NP = 2·S, NQ = 3·S confirmed from the manifest. p-hygiene record
  ("skipped: coeff vanished mod p" at p, char-0 emitted) matches the
  reduce2 write_msolve assert + farm._emit path. Round-trip re-run:
  ops/reduce_msp.py on r1_c4_partial.p65521.ms → guard PASS (1492 rows,
  2 random points), regenerated .RED.ms BYTE-IDENTICAL to the banked twin.

New findings (minor, none affecting soundness):
1. `_cut_chain` appends its "residual vertex ..." log line to blog AFTER
   mkstate has frozen the state's log tuple (both branches; same for the
   single-root path) — the line is invisible in every emitted log.
   Cosmetic observability wart, same class as the flog-truncation one.
2. Commit message "4 families now reduce fully" is imprecise: 12_36_r0,
   6_15 and 8_28mn34 emit all-ψ-normal cases; 12_33mn23d135 reduces with
   5 of 10 cases on the prepsi fallback. The doc text itself is accurate.
3. Rider (a) remains half-applied (see F1 post-fix state): fix
   tests/test_reduce4.py:253 and lib/families.py:209.

All six fronts REAFFIRMED at the statuses above; the promotion
recommendation and riders stand, with rider (a) narrowed to the two
remaining stale citation sites.
