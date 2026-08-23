# MATHIEU-REVIEW.md — Adversarial review of MATHIEU.md (commit 7242f2c)

Reviewer: Claude (max-depth adversarial pass, 2026-08-12). Status: COMPLETE.
Scope: Theorem A (rigidity, all weights), Lemma B (block ⟺ ODE), the
Mathieu-frame bridge, composition with RESIDUE.md §4b, machine checks
M1–M5, consequence audit. Reviewer code: /tmp/mathieu_review/fresh_check.py
(written from scratch — own symbolic poly engine, own linear algebra, no
imports from the repo; run 2026-08-12, exit 0, ~5 s).

VERDICTS: 1 CONFIRMED, 2 CONFIRMED, 3 CONFIRMED, 4 CONFIRMED (with a
dependency-status note), 5 CONFIRMED (scope characterized), 6 CONFIRMED
(two scope sharpenings). Overall: **THEOREM A IS A REAL PROOF.** The
rigidity half of conj:R is closed at every cell k, d2 ≥ 2, and with
RESIDUE.md §4b (whose S1–S5 chain this review independently re-derives in
full generality) conj:R holds in full. No error found in any load-bearing
line. Nits: 3, all cosmetic, listed in §7.

## 1. Theorem A itself
Verdict: CONFIRMED — correct, complete, elementary, sharp.

Independent re-derivation (from scratch, before re-reading §5.1; my
derivation reproduced Steps 1–4 exactly):
- Step 1: A D′ − w A′ D = Σ_{i,j} A_i D_j (j − wi) y^{i+j−1}; the exponent
  δ+d−1 is reached ONLY by (i,j) = (δ,d) (i ≤ δ, j ≤ d, i+j = δ+d forces
  equality), coefficient (d − wδ)·lc(A)·lc(D); nothing higher. Char 0
  enters here and only here: d ≠ wδ (integers) ⟹ d − wδ ≠ 0 in F.
- Step 2: C = 0 gives LHS 0 ≠ c; deg C ≠ wδ gives exact LHS degree
  δ + deg C − 1 ≥ δ − 1 ≥ 1 > 0 = deg c (uses δ ≥ 2; this is where the
  d = 0 loophole of δ = 1 is closed — see scope remark below). So
  deg C = wδ.
- Step 3: L_A(A^w) = 0 — one line, any ring.
- Step 4: D := C − (lc(C)/lc(A)^w)A^w has deg D < wδ and L_A(D) = c by
  linearity; D = 0 gives c = 0, D ≠ 0 re-enters Step 2. Contradiction. ∎

Degree-configuration audit (the mission's (a)): deg C < deg A — killed by
Step 2, no relative-degree assumption anywhere; C or A with repeated
roots — irrelevant, the proof is pure leading-coefficient algebra;
A(0) = 0 or lc(A) pathological — the theorem nowhere uses A(0) = 1 (the
normalization lives in Lemma B, not here); w-coefficient edge — w ≥ 1
integer suffices, w enters only through d − wδ and A^w.

(b) char-0 usage: exactly "(d − wδ) ≠ 0 in F" (Steps 1/2/4). Nothing
else. §5.4's small-characteristic analysis is consistent (see §7 nit 1).

(c) the c ≠ 0 normalization: RIGHT, and it cannot degenerate on a
subvariety. In the unnormalized block gauge the ODE right side is
det(p0,q0)·a_{p0}·b_{q0} = a1·c1, and the vertex equation — itself a
block key — forces a1c1 = 1 on the whole variety. So after unit scaling
c = 1 identically; there is no locus where the constant vanishes. (c = 0
must be excluded: C = λA^w solves the homogeneous equation for every A.)

Counterexample sweep (fresh code, CHECK2): w = 1..6, deg A = 2..5,
adversarial A — random, perfect powers (1+uy)^δ, mixed multiplicity
(y−r)^{δ−1}(y−s), A(0) = 0 (y^m·squarefree), pure monomials y^δ, huge
coefficients (lc = (10^9+7)/3) — window deg C ≤ wδ + 12 (well past the
forced wδ): the system A C′ − w A′ C = 1 is INCONSISTENT in every
instance; δ ≤ 1 controls solvable; and the homogeneous kernel on the full
window is EXACTLY span{A^w} in every instance (independent confirmation
of Steps 3–4's structure, beyond M2's k ≤ 4, δ ≤ 4, window kδ+6). No
counterexample exists in the sweep; exhaustive small-degree non-existence
strengthens the theorem as requested.

Also verified: the ord_∞ remark's arithmetic (ord_∞(c·dy/A^{w+1}) =
(w+1)δ − 2 ⟹ t − t(∞) vanishes to order (w+1)δ − 1, vs the deg-based
order wδ − deg D ≤ wδ; (w+1)δ − 1 > wδ ⟺ δ ≥ 2 forces D = 0,
contradicting dt ≠ 0). The remark is a faithful reading of Steps 1–4.

Scope remark (not an error): at δ = 1 constant C also solve (with
c = −wa2C ≠ 0), so "any solution has deg C = wδ" is a δ ≥ 2 statement —
exactly the scope in which Bridge (d)'s parenthetical invokes it.

## 2. Lemma B (block ⟺ ODE) — the flagged weak point
Verdict: CONFIRMED. Every step re-derived; conventions match; no slip.

- Column identification, independently: fresh symbolic bracket
  computation (CHECK1, own poly engine): for fully symbolic A, B, C, E,
  [xA + x²B, x^kC + x^{k+1}E] has x^k column ≡ AC′ − kA′C, x^{k+1}
  column ≡ AE′ − (k+1)A′E + 2BC′ − kB′C, x^{k+2} column ≡ the depth-3
  column 2BE′ − (k+1)B′E, and nothing else — verified at (2,2), (3,4),
  (2,5). Post-gap-kill self-containedness of the depth-2 block is
  SURPLUS.md's Prop A/B territory (reviewed there); given it, the x^k
  and x^{k+1} coefficients are exactly the block equations.
- Bookkeeping, by hand: y^0 coefficient = 1·c_1 (vertex; det(p0,q0) =
  det((1,0),(k,1)) = 1, so a1c1 = 1 and c_1 = 1 in the scaled gauge);
  y^{(k+1)d2−1} coefficient = (kd2 − kd2)a_{(1,d2)}c_{kd2} = 0, and
  (i,j) = (d2, kd2) is the ONLY pair reaching that exponent — the w = 0
  stratum of Prop A, correctly matched; equations y^1..y^{kd2−1}
  triangular in c_2..c_{kd2} with pivots n+1 ∈ {2..kd2} ≠ 0 in char 0;
  extras = y^{kd2}..y^{(k+1)d2−2}, count d2 − 1 = Prop B's inner strata
  w ∈ [1, d2−1]. All checked against surplus_count/surplus_ext
  conventions (w0/W1 lattice cross-check re-run, exit 0) and against
  LEMMA.md's (2,2) instance (−a3²b3/a1 ↔ normalized −a3²).
- Converse/uniqueness: a witness C automatically has c_1 = 1 (the y^0
  coefficient of the ODE); two witnesses differ by K ∈ ker L_A = F·A^k
  (constants of (F(y), d/dy) = F in char 0 — standard, and the kernel
  claim was independently confirmed numerically in CHECK2) with
  K(0) = 0 ⟹ λ = 0 since A^k(0) = 1. Equivalently: triangularity alone
  forces witness = solved series. Both routes valid.
- Gauge/normalization matching: units a_{p0} = b_{q0} = 1 as in
  SURPLUS-EXT §0; the corner saturations enter only through the vertex
  equation, which supplies the nonzero constant (Front 1(c)); the
  stratum-w conventions match Prop A/B exactly. One symbol collision
  (Theorem A's weight w vs the stratum weight w = d2·i − j) — cosmetic,
  §7 nit 2.
- Numeric dichotomy at the previously OPEN cells, fresh path (CHECK3):
  inner system solvable ⟺ deg A ≤ 1 at (3,4), (4,4), (5,4), (2,5),
  (3,5), (2,6), (2,2), random/power/mixed A, every δ ≤ d2. All OK.

## 3. The bridge (Mathieu frame) and circularity
Verdict: CONFIRMED — implication direction correct; no circularity;
the Mathieu hypothesis is genuinely bypassed.

Bridge chain: M_A proper (a) + Mathieu ⟹ 1 ∉ M_A (c) ⟹ rigidity (d) —
each step's direction checked. (a)'s no-cross-cancellation argument is
sound: distinct source degrees d ≠ kδ give distinct exact image degrees
δ+d−1, the y^{kδ} part stays ≤ (k+1)δ−2, so degree (k+1)δ−1 is never
attained (fresh-verified as M2a's witness, and by hand). (b)'s residue
description: μ_i∘L_A = 0 is the exactness of (C/A^k)′dy; the
independence witness A^{k+1}/(y−r_i) is a polynomial with μ_j-value
δ_{ij}; codimension-δ bookkeeping checks (needs the splitting field for
the r_i — cosmetic). Circularity check: Theorem A's proof consumes ONLY
the lc-formula and L_A(A^w) = 0 — no Mathieu property, no rigidity, no
§4b, no M_A structure. §3(c)'s hypothesis (SC1) is never used
downstream; MATHIEU.md says so explicitly and truthfully (§4, §6). The
per-power Remark after the Bridge Theorem is also correct: Corollary E
gives every power, which Mathieu-ness alone could not.

## 4. Composition with RESIDUE.md §4b ⟹ conj:R in full
Verdict: CONFIRMED — and this review now supplies the missing general
hand-derivation of §4b's chain, upgrading Corollary D's dependency.

RESIDUE.md §4b (S1–S5) had "general derivation + 11-cell machine check"
status with no standalone review. Re-derived here in full generality:
- S1: deg G ≤ 2d2+k−1 < (k+1)d2 ⟺ (k−1)(d2−1) > 0 ✓ (k, d2 ≥ 2).
- S2: outer extras t ≥ 1 touch only e_n with n > (k+1)d2 (absent) and
  G_n = 0 ✓ identically zero.
- S3: extra_0 = ((k+1)d2 − (k+1))·a2·e_top = (k+1)(d2−1)a2·e_top ✓.
- S4: L(E_solved) + G = extra_0·y^{n0} exactly as polynomials; μ∘L = 0
  gives extra_0·μ(n0) = μ(G); μ(n0) = ±C(n0,k+1)a2^{−(n0+1)} ≠ 0 ✓.
- S5 (first full-generality hand check in the campaign): with z = 1+a2y,
  μ(G) = (1/a2)[z^{k+1}](2βz^{k−1} − β′z^k + β′) = (1/a2)(2β_2 − 2β_2 +
  (k+2)β_{k+2}) = (k+2)β_{k+2}/a2, and β_{k+2} = (−1)^k a2^{−2d2}R (M3's
  symbolic identity, itself a two-line binomial expansion). Sign:
  (−1)^{(k+1)d2−1} = (−1)^{k+(k+1)(d2−1)} ✓; a2-power (k−1)d2 ✓; unit
  (k+2)/C((k+1)d2,k+1) ✓ — the closed form is exact, all k, d2 ≥ 2.
- a2 = 0 branch: the closed form is a polynomial identity (extends from
  the dense chart), and solvability at a2 = 0 was fresh-verified
  directly (CHECK4d).
- Sum-start correction j = max(k+2,d2): automatic in R (C(j,k+2) = 0
  below k+2, b_j absent below d2); fresh-verified at (2,5).
- Empty-sum cells k+2 > 2d2: R ≡ 0, Corollary D degenerates to
  V(extras) = {A binomial} — fresh-verified at (5,3) (binomial A +
  ARBITRARY b: block solvable).

End-to-end (CHECK4, fresh linear algebra on the raw block, both columns,
unknowns (C,E)): at (3,4), (4,4), (5,4), (2,5), (5,3) — non-binomial A
⟹ inconsistent; binomial, a2 ≠ 0, R ≠ 0 ⟹ inconsistent; binomial with
R = 0 (or a2 = 0, or empty sum) ⟹ consistent. Exactly conj:R's
biconditional, at every previously open cell within reach. Corollary D
therefore stands; its honest dependency note is now discharged by this
review. Scope unchanged: k, d2 ≥ 2, strip hypotheses (i) + gap-kill +
full block columns, depth 2, char 0.

## 5. Machine checks M1–M5: theorem vs instances
Verdict: CONFIRMED as corroboration; scope correctly disclosed in §7.

What the code actually tests: M1, M2, M5(ii)(iii)(iv) are SAMPLED
instances (random/structured points, finite grids) — they corroborate,
they do not prove universally quantified statements. M3 and M4 are
symbolic identities, but on finite (k, δ, d) grids. M5(i) is a genuine
per-cell symbolic proof of the ⇐ direction (binomial ⟹ extras ≡ 0) at
9 cells. The universal content rests on the 15-line proof — whose entire
computational payload is exactly M4's two identities plus integer
inequalities, as §7 honestly states. Both suites re-run: `mathieu` exit
0 (0.3 s), default T0–T5 ALL OK, surplus_ext exit 0. Decisive additional
check, run in /tmp (nothing added to the repo): fresh_check.py CHECK1–4
as described above — independent implementation, wider windows,
pathological A, end-to-end open-cell block tests. All OK. Remaining
gold-standard step (recommended, not required): the planned Lean
formalization of Steps 1–4, and/or Groebner radical-membership
certificates a3,…,a_{d2+1} ∈ √(inner ideal) at (3,4),(4,4),(5,4) as a
third algebraic path (no sympy on this machine; the repo's resultant
certificates already cover the d2 = 3 grid and (2,4)).

## 6. Consequence audit
Verdict: CONFIRMED, with the boundary drawn precisely.

UPGRADES (if/now that Theorem A stands):
- paper1: conj:R (§functional) becomes a theorem for all k, d2 ≥ 2
  modulo absorbing §4b's write-up; thm:23/thm:24 rigidity halves,
  thm:23full/thm:24 outer parts, and thm:k3's certificates become
  corollaries of Lemma B + Theorem A + the §4b closed form; the
  "certified computation, not a structural proof" caveat and the "open
  at (3,4),(4,4),(5,4) and d2 ≥ 5" paragraph both die.
- Block-level: no depth-2 block point with all coordinates nonzero at
  any k, d2 ≥ 2 (a_{(1,2)} = 0 is forced); pinning form only at (2,2);
  no b-side obstruction for d2 ≥ 3; no residue condition for
  k > 2d2 − 2.
- GGV catalog (SURPLUS-EXT §3 / paper1 §coverage): the conditional
  "d2 ≥ 4 would be open" branch for the four k ≥ 3 rows closes — ANY
  hypothetical strip reduction of any admissible family now lands in a
  theorem-covered cell at depth 2; the scope map's cell table collapses
  to one uniform statement.
- Farm/SECTION4: the depth-2 rigidity + residue-hyperplane constraint is
  available uniformly as a pre-filter at every strip-shaped cell — one
  citation instead of a cell table; SURPLUS-EXT's per-cell resultant
  certificates become redundant (kept as independent corroboration).
- Depth ≥ 3 (attackable, NOT closed): Theorem A is weight-uniform
  (w = k+D−1), so the deeper inner columns' homogeneous rigidity engine
  exists; what is missing is the depth-D Lemma B (block layout,
  self-containedness, inhomogeneity structure) — RESIDUE §5's prediction
  remains a prediction.

DOES NOT FOLLOW: k = 1 (no-gap) families — no bridge there (and conj:R
excludes them); pentagon / y-axis-support shapes (subcase-1-type,
open_8_28_c1 regime — gap-kill fails); d1 ≥ 2 strips; strips shorter
than the block; deeper Minkowski columns (each adds one residue-type
condition, joint behavior open — "deeper Minkowski columns" stay open);
characteristic p ≤ (k+1)d2 (Mondello-consistent); SC1 (still open, still
unneeded). Theorem A closes the depth-2 rigidity question — it does not
by itself discard any GGV family whose reduction is not strip-shaped.

## 7. Nits (no load-bearing consequence; suggest absorbing)
1. §5.4: "pivots n+1 ≤ (k+1)d2 − 1" — true for the inner column
   (≤ kd2), but the OUTER column's triangular pivots reach (k+1)d2.
   The stated conservative bound p > (k+1)d2 still covers both columns
   (and Corollary C needs only the inner ones); no conclusion changes.
2. Symbol collision: Theorem A's weight w vs LEMMA/SURPLUS's stratum
   weight w = d2·i − j. Rename one in the paper write-up.
3. Bridge Theorem (b): the μ_i live over the splitting field of A;
   harmless (and (b) is not load-bearing for rigidity).
Also noted: §1.2–1.3's literature ledger is memory-sourced with honest
confidence labels; nothing in Corollaries C/D depends on it — Theorem A
is self-contained. DvdK is inspiration, not dependency.

## 8. Bottom line
Theorem A is a correct, complete, 15-line proof; Lemma B's block ⟺ ODE
bridge — the author's own flagged weak point — survives full re-derivation
and an independent bracket-level machine check; the composition with
RESIDUE.md §4b (S1–S5 now hand-derived in full generality here) yields
conj:R at EVERY cell k, d2 ≥ 2 in characteristic 0, including (3,4),
(4,4), (5,4) and all d2 ≥ 5, with the empty-sum and sum-start edge cases
verified. The rigidity half of conj:R is a theorem. Recommend: absorb
into paper1 (with nits 1–2), keep the resultant certificates as
redundancy, proceed with the Lean formalization of Steps 1–4, and open
the depth-≥3 front via the weight-w engine.

## Files
- MATHIEU-REVIEW.md (this file).
- /tmp/mathieu_review/fresh_check.py — reviewer's independent suite
  (CHECK1 symbolic bracket identity at (2,2),(3,4),(2,5); CHECK2
  Theorem A sweep w ≤ 6, δ ≤ 5, adversarial A, kernel = span{A^w};
  CHECK3 inner dichotomy at 7 cells; CHECK4 end-to-end conj:R block
  tests at (3,4),(4,4),(5,4),(2,5),(5,3)). Exit 0. Not added to the
  repo per review protocol; re-create from this description if needed.
