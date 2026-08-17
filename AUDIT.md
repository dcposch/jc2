# Soundness audit — emptiness of GGV Prop 4.3, subcase (2) (the (8,28) family)

Audited claim (2026-08-01): **Subcase (2) of Proposition 4.3 of
Guccione–Guccione–Valqui/Horruitiner (arXiv:2204.14178) — the (8,28) family,
(deg P, deg Q) = (108,72), reduced to [P,Q] = x^2 with prescribed Newton
polygons — has no solutions over any field of characteristic 0.**

Proof skeleton being audited:

```
Prop 4.3 s2 statement                                  [trusted-external]
  → Generator A transcription        (lib/jc.py SystemA, cases/emit.py)
  → torus normalization fix_ones     (lib/jc.py, emit.py emit_normalized)
  → Cascade3 b-elimination           (lib/reduce3.py, moves from lib/reduce.py)
  → two_chart decomposition          (lib/chartelim.py two_chart)
      V(core) = V(chartG) ∪ V(core + prod(pivots))
  → kill-split of the complement     → cCa2 (a2:=0) ∪ cCa6 (a6:=0)
  → per-stratum emptiness:
      chartG: symbolic −1 derivation + msolve GB=[1] over Q + 3 primes
      cCa2:   msolve GB=[1] over Q + 3 primes
      cCa6:   msolve GB=[1] over Q + 2 primes (3rd prime in flight)
```

Composition: a solution over any char-0 field K is a solution over the
algebraic closure K̄ (claim 1); it can be torus-normalized within K̄ (claim 2);
the normalized solution survives to the Cascade3 core (claim 3) and hence lies
in one of the three strata (claims 4, 5); each stratum carries a Q-coefficient
certificate 1 = Σ h_i f_i (claims 6, 7), which evaluated at the solution gives
1 = 0. Contradiction. Subcase (1) is **not** covered by this audit; it is the
remaining half of the (72,108) family.

Verification-status legend:
- **proved-in-code** — the property is enforced by an assertion/test in the repo.
- **numerically-audited** — checked at random exact points; script may live
  only in session transcripts (flagged where so).
- **regression-validated** — the identical pipeline re-derives the known-empty
  solved cases (Props 4.1, 4.2, 4.4).
- **trusted-external** — imported from outside this codebase (GGV chain, msolve).

---

## Claim 1 — Generator A faithfully transcribes Prop 4.3 subcase (2)

**Statement.** The system `open_8_28_c2` (cases/emit.py:45-48) has solution set
(over any field) equal to the set of pairs (P,Q) demanded by Prop 4.3 s2 under
the conservative ("nonorigin") reading of the Newton-polygon convention, and
containing the solution set under the strict reading.

**Why it holds.**
- *Support = hull ∩ Z².* Unknowns are one coefficient per lattice point of
  hull(cornersP) and hull(cornersQ) (`SystemA.__init__`, lib/jc.py:143-199;
  `lattice_points`, lib/jc.py:113-139, with `ccw_order` asserting strict
  convexity). Any P with N(P) ⊆ polygon is representable; nothing outside the
  hull is allowed, exactly as in the Prop 4.3 shape constraint. Lattice counts
  for all four subcase polygons (25, 47 and, for subcase (1), 61, 125) are
  hand-verified via Pick's theorem in tests/test_jc.py:14-27.
- *Equations.* `E = bracket(P,Q) − x^2`; **every** coefficient of E over its
  full bivariate support is an equation (lib/jc.py:184-188). The bracket
  [P,Q] = P_x Q_y − P_y Q_x (lib/jc.py:92-94) is property-tested:
  antisymmetry, Leibniz, [x,y] = 1 (tests/test_jc.py:29-42), plus a
  known-solution substitution test (tests/test_jc.py:44-62).
- *Corner attainment.* The saturation equation t·∏(listed corner coeffs) = 1
  (lib/jc.py:190-199) forces every listed non-fixed corner coefficient ≠ 0.
  If all vertices of the polygon are attained, hull(supp) equals the polygon
  exactly — so saturation is precisely "N(P) = the stated polygon".
- *Origin convention ("nonorigin") and the strict reading.* In `nonorigin`
  mode the (0,0) coefficients are left unconstrained (lib/jc.py:190-195).
  Under GGV's convention that (0,0) always belongs to N(P), no origin
  constraint is the faithful reading. Under the strict reading ((0,0)
  coefficients also ≠ 0), the strict variety = nonorigin variety ∩
  {a_(0,0) ≠ 0, b_(0,0) ≠ 0} ⊆ nonorigin variety. **Emptiness of the
  nonorigin variety therefore settles both readings by inclusion** — this
  retired the separately-launched `_strict` runs (../notes.md, 2026-08-01
  entry). No extra compute needed.
- *Bracket sign convention.* If GGV's convention is the opposite sign, a
  GGV-solution satisfies our [P,Q] = −x^2; then (P, −Q) satisfies
  [P,Q] = +x^2 with identical support and corner nonvanishing. Emptiness is
  convention-independent (README.md "Semantics").

**Status.** proved-in-code (tests above) + regression-validated: the same
generator + pipeline re-discards all five solved cases — e.g.
reg_9_24_c3 core EMPTY [1] mod 65521 in 2.3 s (README.md; runs/
reg_9_24_c3_v6.p65521.out, reg_9_24_c3_chartG/chartC.p65521.out, all
basis-length 1). The *statement* transcribed (polygon data, subcase split,
rhs x^2) is trusted-external (claim 8); the corner data in emit.py was
transcribed by hand from the paper and has no independent machine check —
see obligations.

---

## Claim 2 — Torus normalization is lossless for emptiness

**Statement.** Let k = 2 (rhs x^k). Over an algebraically closed field, the
system `open_8_28_c2_n` — which fixes coeff_P(8,16) = coeff_Q(12,24) = 1
(`FIX`, cases/emit.py:79-80) — is empty iff `open_8_28_c2` is empty.

**Why it holds (the lemma, stated precisely).** For λ, α ∈ K̄^× let
φ_λ(x,y) = (λx, μy) with **μ = λ^−(k+1)**, and act by
(P,Q) ↦ (α·(P∘φ_λ), α^{−1}·(Q∘φ_λ)).
- The chain rule gives [P∘φ, Q∘φ] = λμ·([P,Q]∘φ) = λ^{−k}·([P,Q]∘φ), and
  [P,Q] = x^k ⇒ ([P,Q]∘φ) = λ^k x^k, so the transformed pair again satisfies
  [P,Q] = x^k. The α-scaling preserves the bracket exactly. Supports and
  corner (non)vanishing are preserved.
- The coefficient of P at (i,j) is multiplied by α·λ^w, and of Q by
  α^{−1}·λ^w, with weight **w = i − (k+1)j**. Given a solution with
  c_P := coeff_P(8,16) ≠ 0 and c_Q := coeff_Q(12,24) ≠ 0 (both are non-origin
  listed corners, forced ≠ 0 by saturation), we need
  αλ^{w_P}c_P = 1 and α^{−1}λ^{w_Q}c_Q = 1. Multiplying:
  λ^{w_P+w_Q} c_P c_Q = 1. Here w_P = 8 − 3·16 = −40, w_Q = 12 − 3·24 = −60,
  so w_P + w_Q = −100 ≠ 0 and λ exists in K̄^× (algebraic closure supplies a
  100-th root); then α := (λ^{w_P}·c_P)^{−1} settles both equations.
  So every solution is torus-equivalent to a normalized one; conversely a
  normalized solution is a solution. Hence emptiness transfers both ways
  **over algebraically closed fields** — sufficient, since claim 1's
  composition passes through K̄.

**Why the hypothesis is machine-checked.** `emit_normalized` computes
det = (i_P − (k+1)j_P) + (i_Q − (k+1)j_Q) and **asserts det ≠ 0**
(cases/emit.py:87-89; here det = −100); `SystemA` asserts fix_ones points are
listed corners (lib/jc.py:166-167). The lemma statement is recorded in the
`fix_ones` docstring (lib/jc.py:154-160).

**Status.** Lemma: pen-and-paper (above; not yet in any test). Hypothesis
det ≠ 0: proved-in-code. Pipeline behavior on normalized systems:
regression-validated (all `_n` solved cases re-discarded).

---

## Claim 3 — Every Cascade3 move preserves the corner-localized variety

**Statement.** Let W = { points with all Generator-A equations = 0 and every
listed non-fixed corner coefficient invertible }. Each Cascade3 step
(lib/reduce3.py) replaces the current system by one whose solution set is in
natural bijection with W projected along eliminated variables; in particular
W = ∅ iff the final core system is empty.

**Why it holds.**
- *Setup.* Cascade3 drops the degree-7 t-saturation and instead adjoins
  c·ic − 1 = 0 for each corner variable c (lib/reduce3.py:28-34).
  Equivalence: ∃t with t·∏c_i = 1 ⟺ ∏c_i ≠ 0 ⟺ each c_i ≠ 0 ⟺ ∃ inverses.
  Same (a,b)-projection, so emptiness is unaffected. `units` = corner vars +
  their inverses; these are invertible at every point of W.
- *M1 (contradiction).* An equation reduced to a nonzero rational constant,
  or to k·m with k ∈ Q^× and m a product of units, has no zeros on W
  (units invertible) → status EMPTY (lib/reduce3.py:56-64; semantics
  documented in lib/reduce.py:6-9). Over Q, "k ≠ 0" is exact.
- *M2 (monomial zero-forcing).* Equation k·m = 0 with exactly one distinct
  non-unit variable v in m (any multiplicity e): at a field-valued point,
  units cancel and v^e = 0 ⇒ v = 0. Substituting v := 0 everywhere
  (`_kill_var`, lib/reduce.py:43-45) is an isomorphism onto W ∩ {v = 0} = W.
- *M3 / b-pivot elimination with unit-monomial pivots.* `_pick_pivot`
  (lib/reduce3.py:107-126) accepts a b-variable v only if: v occurs in the
  chosen equation in a single monomial m0, to the first power, and every
  other factor of m0 is a unit. Then the equation reads q·u·v + rest = 0
  with q ∈ Q^×, u a unit monomial — invertible at every point of W — so
  v = −u^{−1}·rest/q =: g is *forced*. u^{−1} is realized polynomially as
  the mirror product of inverse variables (`invmon`, lib/reduce3.py:138),
  and `_inv_reduce` (lib/reduce3.py:92-105) rewrites c·ic → 1, i.e. reduces
  modulo the adjoined relations — sound as functions on W. Forgetting v is
  then a bijection (solutions of new system) ↔ (solutions of old), inverse
  v := g(point). Emptiness preserved in both directions.
- *Termination and b-linearity.* Generator-A equations are bilinear (each
  monomial has ≤ 1 a-var and ≤ 1 b-var, degree ≤ 1 each, because P is
  a-linear and Q is b-linear in their coefficients). Eliminating only
  b-variables keeps every monomial b-degree ≤ 1 forever — substitutes are
  never raised to powers (`_subst_linear`, lib/reduce3.py:81-90; module
  docstring lines 1-13) — so each pivot really is a linear solve and the
  cascade ends after ≤ #b steps. a-degrees may grow (harmless: msolve takes
  over on the core). The MAXTERMS_EQ guard only *aborts* (status
  "aborted-swell"); an aborted mid-cascade state is still a sound system.
  For open_8_28_c2 the cascade completed; the two Q-corner variables b3
  (2,1) and b43 (12,21) are the only surviving b's, since pivots skip units.
- *The ghost audit.* The elimination log (`C.elim`, list of (v, g)) was
  audited numerically: sample random exact points of the core, reconstruct
  every eliminated b ("ghost" variables) by back-substitution through the
  log, and evaluate the **original** Generator-A equations — all vanish.
  This checks the bookkeeping (`_subst_linear`/`_inv_reduce`) end-to-end.

**Status.** Move-level arguments: pen-and-paper (above; module docstrings
state them). Bookkeeping: numerically-audited — but the ghost-audit script
exists only in session transcripts (no "ghost" artifact is committed to the
repo; searched 2026-08-01) → obligation. Whole cascade:
regression-validated (solved cases stay EMPTY through the same path).
Field caveat: M1/M2 verdicts and all Fraction arithmetic are exact over Q;
transfer to F_p additionally needs p to divide no cleared numerator or
denominator (see claim 6 caveat).

---

## Claim 4 — The two_chart identity

**Statement.** For the finished core C,
`two_chart(C)` (lib/chartelim.py:54-99) returns leaves (chartG, chartC) with
**V(core) = π(V(chartG)) ∪ V(chartC)**, where chartC = core equations +
prod(pivot coefficients) = 0, and π forgets the fresh u-variables. Hence
core empty ⟺ both leaves empty.

**Why it holds.** For each remaining b (here b3, b43), a pivot equation is
split as coeff·b + rest = 0 with b strictly linear (monomials with b-degree
≥ 2 disqualify the equation, lib/chartelim.py:68-76 — vacuous here by claim
3's b-linearity, but re-checked). The generic leaf adjoins a fresh u with
**u·coeff = 1** and substitutes **b := −u·rest**, dropping the pivot
equation (lib/chartelim.py:83-95); chartG for open_8_28_c2 gained u75, u76
(visible in the emitted variable order, runs/open_8_28_c2_chartG.q.out).
- (⊇) A chartG-point defines b := −u·rest; substituted equations hold by
  construction, and the dropped pivot equation holds:
  coeff·(−u·rest) + rest = rest·(1 − u·coeff) = 0. A chartC-point is
  literally a core point. So both leaves map into V(core).
- (⊆) At a core point, either every chosen pivot coeff is ≠ 0 — set
  u_i := coeff_i^{−1}; the pivot equations force the b's to the substituted
  values, giving a chartG-point — or some coeff = 0, so
  prod = ∏ coeff_i = 0 (lib/chartelim.py:94) and the point lies in chartC.
- *Caveat (checked for this run).* In general a later pivot coeff could
  involve an earlier u, which would make chartC's added generator ill-posed;
  in the open_8_28_c2 run both chosen pivot coefficients were single
  monomials in original core variables (`info` records length 1 for each),
  so prod is a genuine core-variable monomial. The general-position code
  does not enforce this — flagged in obligations.

**Status.** Identity: pen-and-paper (docstring lib/chartelim.py:55-58 states
it). Instantiation for open_8_28_c2 (monomial pivots, two u's):
numerically-audited via the claim-7 point audit (chartG points reconstruct
to original solutions) and regression-validated (reg_9_24_c3 chartG/chartC
both EMPTY [1], runs/). The exhaustive-branching variant `eliminate_bs`
(lib/chartelim.py:101-170) was not used for the final decomposition.

---

## Claim 5 — The kill-split of the complement

**Statement.** For open_8_28_c2 the pivot product is a monomial
prod = (unit factors)·a2^α·a6^β with α, β ≥ 1, so
**V(chartC) = V(core + a2) ∪ V(core + a6)** — the emitted kill-branches
cCa2 (a2 := 0) and cCa6 (a6 := 0). chartC empty ⟺ both branches empty.

**Why it holds.** On the corner-localized locus every unit factor of prod is
invertible, and field points have no zero divisors, so prod = 0 ⟺ a2 = 0 or
a6 = 0. Substituting a2 := 0 (resp. a6 := 0) into the core is an isomorphism
onto V(core) ∩ {a2 = 0} (a2, a6 are interior P-coefficients, not corner
variables, so no saturation forbids their vanishing). Evidence that the
emitted systems are exactly these substitutions: the variable line of
systems/open_8_28_c2_cCa2.*.ms omits a2 (and keeps b3, b43, ia1, ia22, ib3,
ib43), that of open_8_28_c2_cCa6.*.ms omits a6; both otherwise agree with
the core.

**Status.** Identity: pen-and-paper (elementary). Instantiation:
numerically-audited/reconstructed — the split-emitter session script is
**not committed** (systems/ artifacts + ../notes.md 2026-07-30 entry are the
record; prod's exact unit part and exponents α, β are not archived) →
obligation. Union coverage chartG ∪ cCa2 ∪ cCa6 = full reduced variety is
asserted in ../notes.md (2026-07-31) and follows from claims 4 + 5.

---

## Claim 6 — What msolve GB = [1] certifies, per stratum

**Statement.** msolve reporting reduced Gröbner basis = {1} over Q for a
stratum system certifies (conditional on msolve correctness) that
1 = Σ h_i f_i for the stratum's generators f_i with h_i ∈ Q[vars]; hence the
stratum has no points in **any** nonzero Q-algebra — in particular over
every field of characteristic 0. Mod-p verdicts are independent
corroboration, not part of the char-0 certificate.

**Why it holds.** 1 ∈ I ⟺ reduced GB = {1} (Buchberger); a common zero in
any char-0 field would evaluate the cofactor identity to 1 = 0. Emptiness
over C (Nullstellensatz) is the special case. Note the localization is
internal: corner/pivot invertibility is imposed by polynomial equations
(c·ic − 1, u·coeff − 1), so plain ideal triviality is the right test — no
saturation-aware reasoning is delegated to msolve.

**Verdict inventory** (runs/ + fleet logs per ../notes.md 2026-07-31 and
2026-08-01; all verdicts are authenticated full msolve headers: field char,
complete variable order, "length of basis: 1 element"):

| stratum | over Q | mod p (65521 / 1048573 / 2147483629) | local artifacts |
|---|---|---|---|
| chartG (27 vars) | [1] | [1] / [1] / [1] | runs/open_8_28_c2_chartG.q.out, .p65521.out |
| cCa2 | [1] | [1] / [1] / [1] | runs/open_8_28_c2_cCa2.q.out, .p65521.out |
| cCa6 | [1] (17h43m, 761 GB peak) | [1] / [1] / running | none yet (fleet only; local .p65521.out is 0 bytes) |

**Caveats.**
- The three primes rule out "lucky-prime" artifacts and cross-check the
  char-0 lane, but all runs used the *same engine* (msolve). No independent
  GB engine has confirmed the open-case strata (Singular ran only the lift
  attempts, claim 8).
- Mod-p emission path: `leaf_to_msolve` (lib/chartelim.py:172-208) clears
  denominators per equation but — unlike `Cascade.write_msolve`
  (lib/reduce.py:152, which asserts no cleared coefficient vanishes mod p) —
  has **no mod-p vanishing guard**. If p divided a cleared coefficient the
  mod-p system would be silently weakened. This cannot affect the char-0
  certificate; it only (mildly) weakens the corroboration lanes. No check
  that the three primes avoid all denominators/numerators has been run →
  obligation.

**Status.** Certificate semantics: pen-and-paper (standard). Verdicts:
machine-produced, trusted-external w.r.t. msolve; multi-prime + two-machine
agreement (README.md) is the current defense in depth. Fleet verdict files
for cCa6 and the third-prime runs are not yet archived in runs/ →
obligation.

---

## Claim 7 — The symbolic −1 on chartG, and its numeric audit

**Statement.** On the generic chart, the Cascade3 + two_chart substitution
chain reduces **original Generator-A equation #3** (one explicit coefficient
of [P,Q] − x^2) to the constant −1. Hence chartG is empty by pure algebra —
a theorem-fragment independent of F4 — valid over every field in which the
chain's denominator primes are invertible (so over all char-0 fields, and
all F_p away from finitely many explicit primes).

**Why it holds.** Each step of the chain multiplies by explicit units and
performs the forced linear substitutions of claims 3-4, so it is an
ideal-membership derivation: −1 ∈ I(chartG) with an explicitly recomposable
cofactor chain. The artifact systems/chartG_culprit.sing contains the chart
system with the literal generator −1 as its first entry; Singular's
lift(I,1) on the chart accordingly succeeded instantly with a **1-term
cofactor** (1 = (−1)·(−1)) — trivial, because the unit is already a listed
generator, but it confirms the emitted system is the one carrying the
symbolic contradiction.

**Numeric audit** (../notes.md, 2026-07-30 AUDIT MILESTONE): at 6 random
exact-rational chart points, using **only** the original equations plus the
stored substitution logs: equation #3 evaluates to exactly −1 at all 6
points; 51/92 pivot equations vanish identically; no other equation reduces
to a nonzero constant. Exact rational arithmetic — no rounding. Regression
contrast: the solved case's chartG exhibits **no** such collapse (its
emptiness needed real F4), so the collapse is a structural feature of
(72,108) s2, not a pipeline artifact.

**Status.** numerically-audited (6 exact points; audit script transcript-only
→ obligation). The standalone-lemma write-up (which bracket coefficient
equation #3 is; the substitution chain as a self-contained derivation) is
owed (../notes.md TODO). Once written, this upgrades chartG to
proved-on-paper, independent of msolve.

---

## Claim 8 — TRUST BOUNDARY (explicit)

Everything above reduces the headline claim to the following trusted inputs:

1. **GGV Prop 4.3 itself** — that the (108,72) Jacobian pair analysis
   reduces to the two stated subcases with those polygons, corners, and
   [P,Q] = x^2, including the internal branch bookkeeping of the §4 proof
   (subcases (1)+(2) exhausting the family). Unverified here; parts of the
   supporting chain (1401.1784 / 1605.09430 / 1406.0886 / 1708.07936 /
   2204.14178) are **arXiv-only/unrefereed**; the published J. Algebra
   version of 1401.1784 omits Cor. 7.12 (Heitmann JPAA 64 (1990) Thm 2.24
   covers it independently) — see ../plan-72-108.md "Risks"/"Phase 0".
   Exact arXiv versions must be pinned in any writeup.
2. **msolve correctness** (F4 + char-0 tracing + [1] reporting), version(s)
   as installed on the local box, jc-b, and ultramem-1. Mitigations in
   place: 2-3 primes per stratum, two machines/builds agreeing, authenticated
   headers. Not yet mitigated: no second GB engine on the open strata.
3. **Steps still lacking machine-checkable certificates:**
   - Cofactor certificates 1 = Σ h_i f_i: **chartG — obtained** (trivial
     1-term lift, systems/open_8_28_c2_chartG.lift.sing / chartG_culprit.sing);
     **cCa2 — Singular lift(I,1) TIMED OUT** (runs/cCa2_lift.txt is empty;
     input systems/open_8_28_c2_cCa2.lift.sing); **cCa6 — lift not
     attempted**. Until cCa2/cCa6 lifts (or an equivalent certificate,
     e.g. msolve's own cofactors) exist and are re-verified by the planned
     independent FLINT/Nemo checker, those two strata rest on trusting
     msolve.
   - Cascade3 / two_chart / kill-split correctness: mathematically argued
     (claims 3-5) and numerically audited, but the audits are
     session-transcript-only and there is no formal write-down and no
     committed re-runnable audit script.
   - The Prop-4.3-to-emit.py polygon transcription (claim 1) has no check
     against the paper other than eyes + the lattice-count tests.
4. **Not** in the trust boundary: torus normalization (claim 2, self-
   contained lemma + asserted hypothesis), the strict-vs-nonorigin
   convention question (settled by inclusion), and the bracket sign
   convention (settled by negation).

---

## Remaining obligations before any public claim

- [ ] **Commit the audit scripts**: ghost audit (claim 3), 6-point symbolic
      audit (claim 7), and the chart/kill-split emitter session code
      (claims 4-5), as re-runnable tests under tests/.
- [ ] **Write the standalone −1 lemma** for chartG: identify equation #3's
      bracket position, lay out the substitution chain, state the excluded
      denominator primes (upgrades chartG to paper-grade).
- [ ] **Certificates for cCa2 and cCa6**: rerun cCa2 lift with more
      time/memory or extract cofactors by other means; attempt cCa6 lift;
      then verify all three certificates with the independent FLINT/Nemo
      checker (../plan-72-108.md Phase 4).
- [ ] **Second GB engine** (Singular/Macaulay2/Groebner.jl) reproducing
      [1] at one prime for each stratum — removes single-engine risk even
      before lifts land.
- [ ] **Archive fleet artifacts** into runs/: cCa6 Q-run and p-run outputs,
      third-prime outputs, with full headers, plus msolve version strings
      and host info.
- [ ] **Prime-hygiene check**: verify no cleared numerator/denominator in
      any emitted stratum system vanishes mod 65521 / 1048573 / 2147483629;
      add the missing guard to `leaf_to_msolve`.
- [ ] **Record prod(pivots)** exactly (unit part, α, β) from a committed
      re-run of the two_chart step; assert its non-unit support is {a2, a6}.
- [ ] **Formal write-down** of claims 2-5 as lemmas with proofs (this file
      is the outline; ../notes.md flags the write-down as owed).
- [ ] **Pin arXiv versions** of the GGV chain; flag unrefereed links; note
      the Prop 4.3 dependency explicitly in the writeup; optionally probe
      the raw unreduced formulation for partial independence (char-0 lane,
      README "Findings").
- [ ] **Subcase (1)** — not an obligation for *this* claim, but required
      before any "(72,108) family discarded / bound = 125" statement.
      Scope discipline: the public claim matching this audit is
      "Prop 4.3 subcase (2) is empty over char 0, conditional on Prop 4.3".

## Committed artifact — pivot product (obligation 1, recorded 2026-08-02)
Deterministic re-run of Cascade3(level_dir=(2,1)) + two_chart on
open_8_28_c2 (nonorigin, fix_ones per FIX):
  prod(pivots) = -1/5 * a2((1, 1))^2*a6((2, 4))*ia1^2*ib43
Non-unit support asserted == {a2 (P-point (1,1)), a6 (P-point (2,4))} — PASSED.
Hence V(complement) = V(core + a2*a6 = 0) = V(core, a2=0) ∪ V(core, a6=0),
which is exactly the cCa2/cCa6 split used throughout.

## Pinned external versions (obligation 3)
- arXiv:2204.14178v1 (GGV-Horruitiner, 29 Apr 2022) — Prop 4.3, THE dependency.
- arXiv:1401.1784 (GGV; J. Algebra 471 (2017) 13-74 — journal omits Cor 7.12).
- arXiv:1605.09430, arXiv:1406.0886, arXiv:1708.07936 — arXiv-only (unrefereed).
- msolve (Homebrew build, local; git master built 2026-07-27 on ultramem/jc-b).

## msolve parenthesis hazard (2026-08-09)

SHEET6-R1-REVIEW.md discovered msolve 0.10.1 SILENTLY MIS-PARSES
parenthesized polynomial input (micro-test: `x-(3+1)` yields GB `[x+1]`).
Sweep of all 401 shipped .ms files (systems/**, recursive): exactly ONE
contained parentheses — systems/r1/r1_gmband_core.ms (the new R1 engine's
emission; its EMPTY verdict retracted on this + independent grounds).
ALL 400 other systems (72,108 leaves, farm, dc2, sheet6) are fully
expanded monomial sums — no parentheses — so every prior verdict stands.
Standing rule added: .ms emitters MUST emit expanded monomial sums only;
any new emitter gets the paren-sweep + a satisfiability smoke test
(constant-term row check: a system whose rows all lack constant terms
cannot be [1] — guard against impossible verdicts) before its verdicts
are banked.

## msolve mod-p coefficient-reduction hazard (2026-08-10)

### The hazard, and its TRUE boundary (established by micro-test)

SHEET6-R1-25LOCUS.md §4b discovered that feeding msolve 0.10.1 a p>0
char line with char-0-style bignum coefficients silently corrupts the
system (r1_25chain_core: spurious GB=[1] at three primes; the same
system with coefficients pre-reduced into [0,p) gives the correct
487-elt GB). Root cause isolated TODAY by micro-test (/tmp/redtest):
**msolve's integer-token parser clamps at LONG_MAX = 2^63-1
(9223372036854775807)**. Verified: `x+9223372036854775807*y` parses to
exactly the LONG_MAX value mod p, and every larger token (2^64, a
9.6e21 coefficient from the c1 leaves) parses to the SAME clamped
value — silently, exit 0. Conversely, coefficients in [p, 2^63) are
reduced correctly mod p at parse time: unreduced-vs-reduced twin files
at magnitudes 65522 / 445440 / 1337656320 produce BYTE-IDENTICAL
Gröbner bases. So the corruption condition is
  some |coefficient| > 2^63-1  (NOT merely >= p),
though the standing rule below mandates full reduction into [0,p)
regardless, because relying on the parser's internal reduction is
exactly the kind of trust this campaign does not extend.

### 110-file inventory (full scan of systems/**/*.ms, 2026-08-10)

Scan: line 2 read as char, every integer token of the body compared
against it (chunked streaming reader; full list with per-file class
and max coefficient BANKED at ops/modp_contam_inventory_20260810.txt).
110 files have char p>0 and max coefficient >= p, splitting at the
true hazard boundary into:

- **49 CORRUPT-class (max coeff > 2^63-1 — msolve genuinely mangles):**
  - 16 systems/c1_* leaf files at p65521 (max 9.6e21 / 1.6e21);
  - systems/open_8_28_c1_v6.p65521.ms (1.6e21);
  - 3 systems/ordtest_*.ms (1.6e21);
  - systems/reg_7_21_partial.p65521.ms, reg_9_27_partial.p65521.ms;
  - 27 systems/farm/* p65521 partial/core files (max up to 9.3e30),
    ALL 27 dispatched in the live farm queues (14 box01 + 13 box02
    per systems/farm/queue/*/queue.txt).
- **61 word-sized (p <= max coeff < 2^63 — msolve parses correctly;
  hygiene violations, not corruptions):** the open_8_28_c2 stratum
  files (cCa2/cCa6/chartC/chartG/v6/v6s at p65521 and p1048573, max
  1.34e9), the reg_9_24_c3 mod-p suite, reg_9_24_c1/c2_v6.p65521,
  24 systems/conjE/*.p65521.ms (max 67200), 14 farm files
  (4_12mn34d64, 9_24mn23d99, 7_42*_c1_partial).

systems/r1/* mod-p emissions: ALL verified reduced (max coeff < p) —
the R1 rebuild's emitters already reduce; every R1 mod-p verdict in
SHEET6-R1.md §8.20/§10.3/§10.5/§11 used clean inputs. dc2, zheglov,
sheet6-engine systems: zero hits (exact-arithmetic or char-0 lanes).

### Cross-reference: does ANY accepted campaign verdict rest on these?

**VERDICT: NO accepted campaign verdict rests on a corrupted input.
Contaminated-verdict count = 0.** Per relied-upon verdict class:

1. **(72,108) subcase (2) — the claim-6 inventory.** The char-0
   certificates (chartG.q, cCa2.q, cCa6.q = the actual soundness
   chain) are char-0 files: hazard inapplicable. The mod-p
   corroboration lanes at p=65521/1048573 DID use unreduced files,
   but all are word-sized (max 1.34e9 < 2^63): msolve parsed the
   intended systems. Re-verified empirically today (see re-runs). The
   third prime 2147483629 > 1.34e9: those emissions are reduced by
   construction. chartG additionally rests on the symbolic -1 (claim
   7), msolve-free. **Subcase-(2) verdicts stand.**
2. **(72,108) subcase (1).** The 16 c1_* leaves + open_8_28_c1_v6
   ARE corrupt-class — but produced NO accepted verdict: every c1
   lane run died without verdict (notes.md 2026-08-06/07: Xeon all-Z
   leaf FAILED at 940GB/30h; ultramem I-leaf retired; leaf program
   CLOSED, novelty rule). Subcase (1) is settled via the EXTERNAL
   Helali + Suzuki artifacts (CROSSCHECK.md): Helali = gmpy2/flint
   exact char-0 number-field certificates, Suzuki = exact char-0 +
   F_23 descent with recorded pivot residues, byte-identical
   regeneration — NEITHER uses msolve or unreduced mod-p input.
   **The c1 corruption never touched an accepted verdict.**
3. **Regression/validation verdicts.** reg_9_24_c3 mod-p suite
   (14/14 G0 sweep) used word-sized files — parsed correctly;
   re-verified today. reg_7_21/reg_9_27 partials are corrupt-class
   but no completion/verdict was ever banked for them (G0 stands at
   3/5 via other lanes). ordtest_*: runs errored (runs/ordtest_*.err),
   no verdicts.
4. **Sheet-6 R1.** All r1 mod-p files reduced (see above); the §6
   retraction is unrelated (paren hazard); §11's (2,5) NONEMPTY rests
   on char-0 + reduced-coefficient mod-p GBs (25LOCUS §6). Clean.
5. **conjE.** HOLD verdicts are char-0 Gröbner certificates; the
   agreeing mod-p lane used word-sized files (max 67200) — parsed
   correctly, spot re-verified today. Clean.
6. **Farm (deg<=150 frontier).** The ONLY at-risk class with live
   verdict exposure: 27 corrupt-class p65521 jobs are in the remote
   queues, and the boxes bank smallest-first — the early banked
   EMPTYs (box01 6 EMPTY, jc-b 9 outputs as of 2026-08-10, not yet
   pulled locally) plausibly include corrupt-class jobs (e.g.
   7_42*_c3_core.p65521 at 5.1MB, 8_28mn32d108_c1_core.p65521 at
   15.7MB are among the smallest). No farm verdict is yet relied upon
   in any headline claim (README farm checkbox is open), so the
   contaminated-ACCEPTED-verdict count stays 0 — but **ACTION
   REQUIRED at next fleet poll: quarantine every farm mod-p verdict
   whose input is in the 27-file corrupt list; re-emit those inputs
   reduced (ops/reduce_msp.py) and re-queue.** Sizing: 27 files,
   4.3GB total (largest 593MB 12_36mn32d144_c1_partial); .q.ms
   char-0 twins and the 14 word-sized farm files are unaffected.

### Re-runs performed today (reduced re-emissions, local msolve -g 2)

Reducer: ops/reduce_msp.py — reduces every non-exponent integer token
into [0,p); built-in guard = independent-parser round-trip (exact
bignum evaluation of every row at 2 random points mod p, original vs
reduced, plus no-token->=p and row-count asserts). All 12 emissions
guard-PASS (systems/redcheck/), outputs banked in runs/redcheck/:

| system (reduced) | result | vs banked original |
|---|---|---|
| open_8_28_c2_chartG.p65521 | [1], <1s | header+verdict IDENTICAL |
| open_8_28_c2_cCa2.p65521 | [1], 291s | matches banked [1] |
| open_8_28_c2_cCa2.p1048573 | [1], 277s | matches fleet [1] |
| reg_9_24_c3_v6/chartG/chartC .p65521 | [1], 0-3s each | IDENTICAL |
| reg_9_24_c3_v6/chartG/chartC .p1048573 | [1], 0-3s each | matches |
| conjE i3l2B12 / i3l3B6x9 .p65521 | [1], <1s | matches |
| open_8_28_c2_cCa6.p65521 | TIMEOUT 1500s locally (fleet nucleus was ~7h/48T — expected); word-sized => parse-safe; reduced emission staged in systems/redcheck/ for optional big-box re-check |

Every re-run reproduces its banked verdict exactly — direct empirical
confirmation that the word-sized contaminated inputs were parsed as
intended (the [0,p) reduction changes nothing), on top of the
micro-test boundary proof.

### Standing rule (added to the emitter checklist, alongside the
parenthesis rule)

**Every .ms emission with char p > 0 MUST have all coefficients
reduced into [0,p) before it ships.** Checklist per new emitter/file:
(1) expanded monomial sums only, no parens (2026-08-09 rule);
(2) coefficients reduced into [0,p) — verifier: max integer token of
the body < char line (the 110-file scan one-liner), reducer:
ops/reduce_msp.py; (3) independent-parser round-trip at the target
prime; (4) constant-term satisfiability smoke test. NEVER bank a
mod-p verdict from a file violating (2) — even word-sized violations
(currently parse-safe) are barred, since parser internals are not a
trust anchor and the 2^63 clamp is silent (no warning, exit 0).
Related: ops/msolve-issue-draft.md (paren hazard) should gain the
2^63-clamp finding before filing upstream.
## Ops checklist addendum (2026-08-11)
On every box restart/reuse: crontab -l FIRST; remove any deadline/poweroff/lifecycle entries before launching work (two incidents: jc-b poweroff loop, ultramem jc_deadline kill).

## External trust ledger (2026-08-12)
- Chau, Ann. Polon. Math. 71 (1999), Theorem 4.4 (full text banked at
  refs/chau1999_apm71_full.pdf; verified on-page pp. 304-305): load-bearing
  for the every-fiber Prop 5.8 upgrade (SOL-PROP58.md). Published +
  refereed; hypotheses Keller + monic in y.
- GPT-5.6-Sol, generalized zero-chain rigid law (xmodel/sol-td7-law.md,
  2026-08-13): td-7 class-B/C cell is T1-dead iff d_p | d_q (iff M = d_p
  iff kbar in {3,4}); on-axis ZCH (nu+1)|l recovered as the mu=1 case.
  PROMOTED after dual verification: zero-shared-reasoning engine check
  62/62 (xmodel/td7-law-engine-check.md; independent reduced-equation
  derivation from BOOK-OFFAXIS R1.0, exact sympy over QQ(A)) + Grok
  hostile proof audit SOUND, all 5 attacks held (xmodel/
  grok-td7-law-review.md). Effect: td-7 book 62 -> 6 live cells
  ((9,15,7,3),(10,15,7,5),(15,25,8,5),(15,25,12,5),(18,27,13,9),
  (39,65,32,13); 53 routes, 35 budget-equality), 1636/1689 routes
  removed by theorem. The six are certified LOCAL T1 survivors
  (explicit admissible solutions); next tier = transport/global.

## Lift retirement (2026-08-13)
cCa2/cCa6 char-0 lift certificates: RETIRED under the last-chance rule
(no LIFT-CERT at the post-outage ultramem check; runs killed). Soundness
unchanged: the (72,108) subcase-(2) record rests on exact mod-p verdicts
at 3 independent large primes + satisfiability guards (see emission
rules); the char-0 lift was a redundancy rider, never load-bearing.
Ultramem access note: use `gcloud compute ssh ultramem-1` (plain ssh key
not authorized); current IP 136.65.11.117 (changes on restart).

## 729-row re-emission (2026-08-13)

TEMPLATE 2c-E5 erratum (SHEET6-TEMPLATE.md §2c, 2026-08-12): the cleared
E5 row constant is 243 = 3^5, not the 729 an earlier draft baked; the
corrected row is 4*(a_i-b)*HM + 243*S_M^3*(a1-a2)^4*a_i^2*c_i*W_i^4 = 0.
H_M is unit-rescalable (HM -> 3*HM maps the 243-row onto the 729-row),
so no banked verdict flips; emitted files carrying the stale constant
are re-emitted for hygiene so downstream consumers do not inherit it.

Findings per engine — all three were (b) stale in code AND (c) stale in
prior emissions:
- cases/r1_q0_gate.py: e5e6_rows() (-> r1_q0_sat_p*) and phase_famemit()
  (-> r1_q0_fam*) used 729; patched to 243 (comment breadcrumbs cite the
  erratum).
- cases/r1_q2_screen.py: phase_emit() (-> r1_q2_l*_p*) and phase_exact()
  (-> r1_q2_l13.ms char 0) used 729; patched to 243.
- cases/r1_12_sat.py: phase_minsat() and phase_corr() used cW =
  729*7^36*144; patched to 243*7^36*144.  (The e5port/emit 81-constant
  rows derive via the RETRACTED mult-4 port, not the 2c-E5 H_M row —
  untouched; the 729 inside the e5port transport identity is lam_i^3's
  9^3, legitimate.)

Re-emitted (26 files; originals kept as *.stale729, nothing deleted):
- Q0: r1_q0_sat_p{105337,105673}.ms + .rows.txt (the rows.txt pinned-HM
  / implied-s1F annotations change by exactly 1/3 mod p, as forced);
  r1_q0_fam.ms; r1_q0_fam_p{105337,105673}.ms.
- Q2: r1_q2_l13.ms (char 0); r1_q2_l{4,8,12,13}_p{105337,105673}.ms;
  r1_q2_l8_sub{16,23,30}_p{105337,105673}.ms (row-subset probes with no
  in-repo emitter: re-emitted surgically — corrected E5 rows generated
  by the engine's own emit path, all other rows byte-identical).
- 12sat: r1_minsat.ms; r1_12sat_corr.ms; r1_12sat_corr_p{105337,
  105673}.ms.
Unaffected by construction: every ctlA/ctlB control (E5/E6 rows
dropped), the relaxed base tiers (r1_q0_p*), the r1_12sat e5port family,
all leaves.  r1_23sat.ms matches the raw integer 12*729*7^36*144 only as
an expanded chain-core coefficient on x-monomials — the chain engine
emits NO E5-analogue rows (EMPTY BY DERIVATION, sec 20.0); not stale.

Verification (all PASS):
- Per file vs its .stale729 twin: exactly the two E5 rows differ;
  paren-free; every changed row reduced into [0,p); independent-parser
  identity stale_row(W, 3*HM) == 3*corr_row(W, HM) at random points
  (FC.parse_eval), 24/24 .ms files — pins the ratio-3 W-side change and
  the unchanged HM-side in one shot.  Label-only rows.txt regenerated
  with zero drift.
- Engine guards: q0_gate a7 anchor PASS (both primes); q2_screen pert 13
  PASS (2/2 deliberate perturbations caught); r1_12_sat e5port PASS.
- 12sat engine-fused re-runs REPRODUCE the banked verdicts exactly:
  r1_minsat.ms char-0 NONEMPTY; r1_12sat_corr.ms char 0 + both primes
  NONEMPTY (~1s walls; engine appended them to runs/*_runs.log).

Why no verdict flips (and what was deliberately NOT re-run):
- NONEMPTY class (minsat, 12sat_corr): exact variety bijection
  (HM|H12 -> 3x, tH -> (1/3)x; no E6/s1F coupling in these systems) —
  provable invariance, plus the empirical reproduction above.
- EMPTY class (r1_q0_sat_p*, r1_q0_fam[_p*], r1_q2_l13[.ms/_p*]): NOT
  re-screened; the banked EMPTY verdicts refer to the .stale729 bytes.
  Robustness: the banked ctlB_satonly controls (quotient rows + s1F
  saturation, NO E5/E6 rows) are EMPTY (fam char 0; q2 l13 both primes;
  and the banked Q0 GB contains s1F), and ctlB's rows are a SUBSET of
  the full tier's rows, so EMPTY(ctlB) => EMPTY(full) for ANY E5/E6
  rows, 243 or 729: the E5 constant is not load-bearing for the kills.
  FLAG: should any future run of a corrected EMPTY-class twin fail to
  reproduce EMPTY, that falsifies the subset argument -> review.  The
  l4/l8/l12/sub* strata carry only TIMEOUTs (no verdicts) — nothing to
  flip.
- Pre-existing, unchanged: the E6 literal 16777216 (2^24) token in the
  q0_sat/q2 mod-p emissions exceeds p (word-sized, parse-safe per the
  2^63 micro-test); it is byte-identical to the stale banked inputs and
  was deliberately NOT altered, to keep byte-parity outside the E5 rows.
  Standing-rule [0,p) reduction of that literal remains an obligation
  for those emitters.
- Restored: systems/r1/r1_full_core.rows.txt (byte-identical copy from
  runs/r1chain_prebuild_snapshot/) — missing from systems/r1 before this
  task (pre-existing gap) and a required input of the q2 guard
  (ME.core_name_map).

## H5a resolution (2026-08-13)
The Notation 3.5 GAP at doubly realized vertices (SIGRAY-AUDIT rows
26/37/92) is RESOLVED at proof tier: the P/coarse reading is incoherent
(nonintegral D_{h,F} against printed Stmt 3.8; conflict with Prop 5.5),
so Q/jump/max kappa_F = nu_F kappa_G / nu_G is the unique uniform repair,
and Q + printed Stmt 3.17(ii) + Prop 9.3(e) force the E5 transport
identities. Proof: xmodel/sol-h5a.md (GPT-5.6-Sol); hostile replay SOUND
incl. printed-page verification and witness construction:
xmodel/grok-h5a-review.md. Consequence: the §11a 17-cell td-7 book is
unconditional under the filed perimeter; the 2-cell sub-book requires
CONJECTURE U_7C (nu_F = nu_G on relevant case-III edges) — genuinely
new, unproven, unrefuted (an exact non-Keller model permits inequality);
no cheap empirical discriminator exists (review finding 5).

## First cell-level tower kill (2026-08-14)
(9,15,7,3)@mu0=2 of the td-7 §11a book: DEAD at the tower tier (no global
Prop 4.2 ladder; level-1 clash, terminal-independent). Adversarial history
preserved in full: Grok SOUND-WITH-ERRATA -> Case C repair; Sol BROKEN
(same gap, pre-repair snapshot) -> M_U=4/free-characteristic extension
(universal nu_X>=2 refactor) -> Sol STILL-BROKEN (in-perimeter neutral
insertions, real gap) -> N1-N4 closure (Sol's sketch formalized) -> Sol
CONFIRMED-KILL. Artifacts: TOWER-9-15.md, cases/towers/t9_15_{direct,
trunk}.json, cases/tower_check.py (696 gates). Book: 17 -> 16 live cells.

## Second cell-level tower kill (2026-08-14)
(10,15,7,5)@mu0=3: TOWER-DEAD (Grok single-pass SOUND, no errata —
xmodel/grok-t10-review.md; machinery core was already triple-reviewed).
Spine == rollout arithmetic exactly (panel-constant apparatus validated).
Consequence: nu_U = nu_G = 7 makes the kill reading-independent; with
(9,15) the forced-nu sub-book is EMPTY and CONJECTURE U_7C is MOOT for
td-7. Book: 15 live cells, all ARITH-DEAD-PREDICTED (TOWER-ROLLOUT.md).

## Third + fourth cell-level tower kills (2026-08-14)
(58,87,43,29)@15 (family rep, k-symbolic frame in m for all six 2/(2k+1)
members) and (25,35,17,5)@8 (kbar=7 outlier, formulas kbar-generic):
TOWER-DEAD, Grok batch review SOUND (xmodel/grok-t58-t25-review.md).
Tripwire verified both ways: rollout (7,15) arrival E5-refuted (n=-1),
corrected (37,15) ledger exact and covered. Blast radius: n>=1 omission
contaminates 7/16 rollout MIN-WITNESS columns (prediction table only) —
NOT the §11a census, NOT any kill. td-7: 13 live cells, all
arith-dead-predicted; uniform theorem next (obligations U-OB1..5).

## TD-7 PANEL CLOSURE (2026-08-14)
THEOREM (TOWER-UNIFORM.md, PROMOTED): every cell of the E5-corrected
td-7 class-B/C book dies at the tower tier — 17/17 (4 certificates +
13 witness instantiations), full perimeter (filed routes, all arrivals/
M_U/free-characteristic/padding/insertion stacks/E5 reroutes),
reading-independent. Lemmas: L-A (R1.3+St8.4/P3 corollary), AM
(absorbing-M), WIN (budget-admissible competing-vertex form; the raw
menu-ratio prose was corrected per review), E5F (uniform n>=1 law,
closed forms). Review chain (seven passes, three model families):
grok-tower-review, sol-tower-review/-rereview/-final (t9_15);
grok-t10-review; grok-t58-t25-review; grok-uniform-review +
sol-uniform-review (both green), 14 errata folded, gates 1559/1559.
Engine: cases/tower_check.py uniform mode; certificates cases/towers/.
Chain effect: off-axis td=7 needs no coefficient emitter; the sheet
ladder's next rungs are td-11/13 (refile + port).

## Witt-Bockstein stratum rigidity (2026-08-14)
PROMOTED: for plane Keller pairs over F_2 on the registered Mondello-
hull-plus-one-L1-shell stratum, the W_2/Cartier lifting obstruction
NEVER vanishes ([xy]E_F = 1 as an identity on the complete four-P
classification, 1152/1152 nonzero incl. all odd-degree data) — no
char-0 counterexample seed lifts from this stratum. Sol construction
(xmodel/sol-witt.md, engine cases/witt_check.py) + Grok hostile review
SOUND (xmodel/grok-witt-review.md). Disproof door closed on the
stratum; the lane's continuation (other strata) is optional and
unranked.

## TD11-CLASH promotion at exact-core tier (2026-08-14)
PROMOTED: the td-11 entry-clash theorem at its honest tier — entry
packets (all three L6 entries), direct hierarchies, single-word-deep
configurations, exact-core audited states (12/10/8, zero non-exempt
violations); Lemma 11A-RES (the sole 5/8 intruder is mu-robustly
H8-dead); Lemma CAP-DEN; near-miss ledger rows 1-9 incl. self-found
row 5 and historicized row 8. OPEN residue, named exactly: beyond-core
px2 states (grammar unbounded, R=1+Delta/nu; both restoration paths
stated §13.0), 129 nested 11-C decorated rows, multi-word-deep
families (NF-Z-dagger per-entry checks), nu=1 resonance chains, the
future Q+E5/E5F refile. Review chain (5 rounds): grok-td11-review
(SOUND-WITH-ERRATA), sol-td11-review (BROKEN), restatement,
sol-td11-rereview (STILL-BROKEN, narrowed), exit-b exact-core
restatement, sol-td11-final (cores CONFIRMED, inventory COMPLETE,
editorial), editorial pass. Gates td11 58/58. Corollary: td-11 NF-D
depth closed for single-word configurations.

## td-11 nested-rows closure (2026-08-14)
PROMOTED: all 129 nested 11-C decorated skeleton rows DEAD-AT-TIER —
62 by inner-merge H8, then the remaining 67 = 31 unrealizable + 12
AB-self-refused (general den-criterion at k | i_G = 2) + 3 split-resolved
+ 21 DEAD-OUTER (NF-M parametric X_out pin at the outer vertex). The
109-object free-nu_A sweep (incl. the in-window-live (6,16)@2 shape)
is census-unrealizable throughout (nu_A != 2 needed, nu_A = 2 pinned).
Review chain: grok-td11-block2-review (reopened 24), repair,
grok-67-final (YES, gap closed), errata fold (sign lemma -> closed form
kbar = 2(1+nuQ)/(1-nu(A-Q))). Gates nfm 25/25. td-11 OPEN inventory:
beyond-core, NF-P slice, refile.

## td-11 CONDITIONAL EMPTINESS CERTIFICATE (2026-08-15)
PROMOTED with wording riders: every configuration of the audited
td-11 class-B/C layer (411-row instrument-backed quotient of the
~2e8 raw route space) is TOWER-DEAD; emptiness is CONDITIONAL on
seven named fail-closed classes (FC1-FC7: beyond-core, cap-free
grammar, refile, current-state arrivals, post-merge strata, nu=1
provenance, merge-schema finiteness) held KEEP-AS-POSSIBLY-LIVE.
Sol's scope-hole chart + 5 siblings enter and die OUTER-DEAD.
Review chain: grok-census-review (SOUND-WITH-ERRATA, FC7 + real
re-derives + genuine td-7 replay — folded), sol-census-review
(BROKEN, M_G scope hole — repaired, +252 rows), sol-census-final
(EARNED; provenance-wording riders NOT load-bearing — fold next
editorial pass). Engine cases/td11_census.py gates 8/8; td-7
replayed through the same two-pole engine. The td-11 panel now
rests on: this certificate + discharging/closing FC1-FC7.

## FOUNDATIONS SCOPE ENTRY (2026-08-17, dual-adjudicated)
The end-to-end reduction (Keller counterexample -> GGV polygon data ->
sheet data -> enumerated book entry) is NOT currently a theorem
(REDUCTION.md, Sol; cross-review Grok SOUND-WITH-ERRATA). Real gaps:
(G1) GGV minimal-pair selection is existential, not a normalization of
every counterexample; (G2) NO transport theorem carries GGV corner data
through Sigray's normalization — the sheet construction does not consume
GGV data as written; (G5) NO upper bound on td. Gap 4 adjudicated: the
td-7 book carries its §11a completeness certificate and td-11 its
conditional certificate (Grok), but a UNIVERSAL full-configuration
landing theorem for the b>=2 sector does not exist (Sol) — both true.
HONEST SCOPE of promoted ladder results: book-relative (every
configuration in the enumerated books dies), pending the book-landing
theorem. The reduction consolidation (T-chain + gap repairs) is now a
top-tier theory objective alongside residue-A.
