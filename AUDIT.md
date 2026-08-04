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
