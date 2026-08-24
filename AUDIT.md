# AUDIT.md — campaign evidence and trust-boundary ledger

This file began as the soundness audit of GGV Proposition 4.3 subcase (2), the
`(8,28)` family, and now carries promoted campaign claims and corrections. It
is not a live queue or avenue-ranking document; see `COORDINATION.md` and
`APPROACHES.md` for those roles.

## Founding audit — GGV Proposition 4.3 subcase (2), the (8,28) family

> **SUPERSEDING EVIDENCE ERRATUM (2026-08-23).** On a characteristic-zero
> input, msolve 0.10.1's `-g` **unit-basis short circuit** can print `[1]`
> from the first machine-prime computation and return before CRT or rational
> reconstruction, while still printing
> `#field characteristic: 0`.  Consequently the archived characteristic-zero
> `[1]` outputs are modular trace evidence, not Gröbner bases or membership
> certificates over Q.  This supersedes the original Claim 6 inventory and
> every later proof-tier reading of the same output surface in this file.
> The files under `dist/jc72108-theory-bundle-v1/` are an immutable historical
> snapshot and still contain the superseded wording; they must be regenerated
> from the corrected canonical sources before any further distribution.
>
> The generic chart `chartG` remains an exact internal theorem because
> `jc72108/systems/open_8_28_c2_chartG.q.ms` itself contains the generator
> `-1`; its one-term certificate is independent of msolve.  No rational
> cofactor is archived for `cCa2` or `cCa6`, so the campaign's own three-stratum
> characteristic-zero proof is incomplete.  Finitely many modular unit
> ideals do not repair that gap without an effective bad-prime bound or a
> reconstructed rational certificate.  Separately, the full `(72,108)`
> exclusion retains exact characteristic-zero support from the independently
> replayed Helali and Suzuki artifacts documented in `jc72108/CROSSCHECK.md`
> and retained in `archive/crosscheck.tgz`; inference from those explicit
> systems to the degree family remains conditional on the GGV-Horruitiner
> reduction, normalization, and transcription bridge.

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
  → per-stratum evidence:
      chartG: exact symbolic −1 derivation + modular corroboration
      cCa2:   first-prime/mod-p [1] traces; no internal Q certificate
      cCa6:   first-prime/mod-p [1] reports; no internal Q certificate
```

Composition: a solution over any char-0 field K is a solution over the
algebraic closure K̄ (claim 1); it can be torus-normalized within K̄ (claim 2);
the normalized solution survives to the Cascade3 core (claim 3) and hence lies
in one of the three strata (claims 4, 5).  The intended final step requires a
Q-coefficient certificate `1 = Σ h_i f_i` on every stratum.  The internal
record supplies that step only for `chartG`, so this proof skeleton stops at
`cCa2`/`cCa6`.  The separate external exact-certificate route is summarized in
the erratum above.  Subcase (1) is **not** covered by this internal audit.

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

## Claim 6 — What the archived msolve `[1]` output actually certifies

**Correct algebraic criterion.** If a rational Gröbner basis calculation or
an independently verified identity really establishes `1 ∈ I ⊂ Q[vars]`,
then `1 = Σ h_i f_i` for rational cofactors and the stratum has no point over
any characteristic-zero field.  The localization equations in these systems
make ordinary ideal membership the right criterion.

**The archived output does not establish that premise.** In msolve 0.10.1,
the characteristic-zero `-g` path starts at a machine prime.  If that modular
basis is `[1]`, the unit-basis branch can return before multimodular
reconstruction; the printer nevertheless repeats the input characteristic as
zero.  Thus a complete header followed by `[1]:` authenticates a completed
first-prime calculation, not a basis over Q.  This warning is specific to the
unit short circuit: a successful non-unit characteristic-zero run continues
through CRT/rational reconstruction, and its printed non-unit basis remains a
Q-level result within the ordinary trust placed in the engine.

**Corrected inventory:**

| stratum | archived `-g` trace | exact internal Q certificate | modular corroboration |
|---|---|---|---|
| chartG (27 vars) | char-0 header + first-prime `[1]` | **YES:** literal generator `-1`, one-term cofactor | `[1]` at the recorded primes |
| cCa2 | char-0 header + first-prime `[1]` | **NO:** Singular lift timed out; `jc72108/runs/cCa2_lift.txt` is empty | `[1]` at the recorded primes |
| cCa6 | historical fleet report of the same output surface; no local Q output | **NO:** lift not attempted/completed | historical multi-prime `[1]` reports; local p-output is not archived |

The cCa2 and chartG `.q.out` files contain only the eight-line header and
`[1]:`; they contain neither a rational basis reconstruction nor cofactors.
No cCa6 rational output is present locally.

**Why several primes still are not a proof.** A characteristic-zero system
can become the unit ideal at finitely many exceptional primes.  For example,
`(p_1 p_2 p_3 x - 1)` has a rational zero but reduces to the unit ideal at
each `p_i`.  Therefore two, three, or any other fixed finite number of
modular `[1]` verdicts is corroborating evidence only unless their size or
product exceeds a proved effective bad-prime bound, or the modular data are
reconstructed and verified as an exact rational certificate.  The bounds
calculated in `jc72108/CERT-UPGRADE.md` put the banked primes far below such a
threshold.

**Mod-p caveat.** The historical `leaf_to_msolve` path also lacked a guard
against coefficient loss during per-equation denominator clearing.  Later
reduced re-emissions strengthen the modular evidence but cannot promote it to
characteristic zero.

**Status.** `chartG` is theorem-grade internally.  `cCa2` and `cCa6` are
modular/trace-grade internally.  Exact characteristic-zero exclusion of the
full external case-2 coefficient system is supplied separately by the Helali
replay in `jc72108/CROSSCHECK.md`; it is not a cofactor certificate for these
two internal chart ideals.

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
2. **msolve correctness for the modular screens.** The recorded `[1]`
   verdicts are first-prime/mod-p evidence.  Agreement at 2-3 primes and on
   two machines mitigates implementation accidents but does not turn those
   screens into a characteristic-zero certificate.
3. **Steps still lacking machine-checkable certificates:**
   - Cofactor certificates 1 = Σ h_i f_i: **chartG — obtained** (trivial
     1-term lift, systems/open_8_28_c2_chartG.lift.sing / chartG_culprit.sing);
     **cCa2 — Singular lift(I,1) TIMED OUT** (runs/cCa2_lift.txt is empty;
     input systems/open_8_28_c2_cCa2.lift.sing); **cCa6 — lift not
     attempted**. Until cCa2/cCa6 lifts (or an equivalent reconstructed
     certificate) exist and are re-verified by an independent exact checker,
     those two internal strata have no characteristic-zero proof.
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

5. **Separate external completion.** `jc72108/CROSSCHECK.md` records exact
   Helali and Suzuki replays for both Proposition-4.3 subcases, with the
   archived bundles retained in `archive/crosscheck.tgz`.  Those certificates
   preserve the conditional `(72,108)` exclusion without using the internal
   cCa2/cCa6 traces.  Their perimeter is the faithful normalization and
   transcription of the explicit coefficient systems and the correctness and
   exhaustiveness of the upstream GGV-Horruitiner Proposition-4.3 reduction;
   the lower
   bound 125 additionally uses the upstream enumeration saying this is the
   sole remaining family below 125.

---

## Remaining obligations before any public claim

- [ ] **Commit the audit scripts**: ghost audit (claim 3), 6-point symbolic
      audit (claim 7), and the chart/kill-split emitter session code
      (claims 4-5), as re-runnable tests under tests/.
- [ ] **Write the standalone −1 lemma** for chartG: identify equation #3's
      bracket position, lay out the substitution chain, state the excluded
      denominator primes (upgrades chartG to paper-grade).
- [ ] **Certificates for cCa2 and cCa6, if a self-contained internal proof is
      still desired**: rerun cCa2 lift with more
      time/memory or extract cofactors by other means; attempt cCa6 lift;
      then verify all three certificates with the independent FLINT/Nemo
      checker (../plan-72-108.md Phase 4).
- [ ] **Second GB engine** (Singular/Macaulay2/Groebner.jl) reproducing
      [1] at one prime for each stratum — removes single-engine risk even
      before lifts land.
- [ ] **Archive fleet trace artifacts** into runs/: cCa6 first-prime and p-run
      outputs, third-prime outputs, with full headers, initial-prime logs,
      input hashes, random seeds, msolve versions, and host info.  Do not label
      a characteristic-zero-header `-g` output as a Q certificate.
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

This subsection audits the separate integer-token/parser hazard only.  Its
"clean" labels do **not** authenticate characteristic-zero `[1]` output; the
2026-08-23 superseding erratum applies independently.

**VERDICT: NO accepted campaign verdict rests on a corrupted input.
Contaminated-verdict count = 0.** Per relied-upon verdict class:

1. **(72,108) subcase (2) — the claim-6 inventory.** The char-0-header
   files are outside this parser hazard, but only `chartG` has an internal
   exact certificate; cCa2/cCa6 are first-prime traces. The mod-p
   corroboration lanes at p=65521/1048573 DID use unreduced files,
   but all are word-sized (max 1.34e9 < 2^63): msolve parsed the
   intended systems. Re-verified empirically today (see re-runs). The
   third prime 2147483629 > 1.34e9: those emissions are reduced by
   construction. chartG additionally rests on the symbolic -1 (claim
   7), msolve-free. The full subcase-(2) characteristic-zero verdict stands
   via the separate exact Helali/Suzuki record, conditional on the shared
   reduction/transcription bridge; it does not stand on the internal msolve
   traces.
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
4. **Sheet-6 R1.** All r1 mod-p files reduced (see above), so their modular
   verdicts are clean with respect to this parser hazard.  The claimed
   characteristic-zero upgrades for the ZU/UZ leaves, Q0 family/control, and
   Q2 l13 stratum used the same first-prime `-g` output surface and are
   reclassified as modular/trace evidence absent exact cofactors.  In
   particular, the active l13 "proof-tier" base and its characteristic-zero
   downstream consequences are open.
5. **conjE.** The 96 characteristic-zero-header `[1]` files are first-prime
   traces, not rational Gröbner certificates.  `CERT-UPGRADE.md` gives an
   exact two-row identity for the `(i,ell)=(1,1)` B-subset family; the other
   five reported HOLD rows remain modular/trace-grade.  None proves
   Conjecture E or is load-bearing for a global JC2 conclusion.
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

## SUPERMIND/GUO BOUNDED CERTIFICATE INTAKE (2026-08-24)
xmodel/intake-supermind-guo-20260824.md (producer) and
xmodel/review-external-intake-grok.md (different-model hostile review:
**CONFIRMED WITH GAPS**). This is an artifact/provenance intake, not an
independent proof count and not an unconditional degree theorem.
- PROMOTED AT THE STATED ARTIFACT TIERS: the SuperMind first-layer and Case-II
  exact Python checks; the pinned Case-I Singular characteristic-zero
  52-dimensional/good-specialization full-rank terminal; Guo's authoritative
  790-file manifest and its exact/hash/regression/conditional audits; the
  degree-21 passport enumeration; the advertised characteristic-zero FGLM
  *program* replay; and the two row-split polynomial identities.
- EXACT CROSSWALK: SuperMind and Guo use the same two Proposition-4.3 Laurent
  systems under a lossless renaming, and their Helali/Suzuki reductions give
  exact zero remainders to the common quintic. Neither proof path invokes
  msolve `-g`.
- GAPS/QUALIFIERS: the SuperMind Python regeneration of the pinned Case-I
  `.sing` file capped; Guo's Sage-only lift, `V(c)`, `D != 0`, and `D=E=0`
  terminal expansions were not rerun. Guo's FGLM script uses Singular
  `modStd(I,1)` on a nonhomogeneous global-order ideal: the advertised program
  replay passes, but it is not to be described as a fully rational `std`
  certificate.
- NO GLOBAL PROMOTION: coordinate equivalence and artifact correctness do not
  establish social or derivational independence. Both bounded exclusions
  still depend on the GGV-Horruitiner reduction/transcription bridge. Thus no
  unconditional exclusion of every `(72,108)` counterexample, no unconditional
  degree-125 theorem, and no implication for JC2 is recorded here.

## Lift retirement (2026-08-13)
cCa2/cCa6 char-0 lift certificates: RETIRED under the last-chance rule
(no LIFT-CERT at the post-outage ultramem check; runs killed).
**CORRECTION (2026-08-23):** those lifts were load-bearing for the campaign's
own characteristic-zero chart proof.  Three independent modular `[1]`
verdicts plus satisfiability/emission guards are strong evidence but do not
imply `1` belongs to the rational ideal.  The internal cCa2/cCa6 proof status
is therefore open.  The separately replayed exact Helali/Suzuki systems
preserve the conditional external `(72,108)` conclusion.
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
  Robustness at the modular tier: the banked ctlB_satonly controls
  (quotient rows + s1F saturation, NO E5/E6 rows) are `[1]` at the recorded
  primes, and ctlB's rows are a SUBSET of the full tier's rows, so
  EMPTY(ctlB) => EMPTY(full) over those same finite fields for ANY E5/E6
  rows, 243 or 729.  The fam characteristic-zero-header `[1]` is only a
  first-prime trace, so this subset argument supplies no Q-level kill.
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

## ODD-PRIME FIRST-WITT SURVIVOR (2026-08-24)
xmodel/round2-witt-oddprime-20260824.md and
cases/round2_witt_oddprime/ (exact producer plus independent replay), with
xmodel/review-witt-oddprime-claude.md (different-model hostile review:
**CONFIRMED**).
- PROMOTED AT THE FINITE-FIELD/`W_2(F_3)` TIER ONLY: over `F_3`,
  `(P,Q)=(x-x^3,y)` has Jacobian one, generic degree three, and the distinct
  marked points `(0,0)` and `(1,0)` collide at `(0,0)`.  Its unrestricted
  first Witt obstruction vanishes.
- EXPLICIT LIFT: in `W_2(F_3)=Z/9`,
  `(P_2,Q_2)=(x+8x^3,y+3x^2y)` has exact integer determinant
  `1+27x^2+72x^4`, hence determinant one modulo 9, and the same marked
  collision persists.  Independent implementations, a third hostile
  recomputation, and the frozen manifest all agree.
- CONSEQUENCE AT THIS SCOPE: the promoted characteristic-two obstruction on
  the registered Mondello stratum is not a blanket first-Witt obstruction at
  odd primes or on other supports.
- NOT SHOWN: no `W_3`, bounded-support compatible all-Witt tower, `Z_3` or
  characteristic-zero polynomial lift, germ, or JC2 counterexample follows.
  The displayed correction already enlarges support.

## UNRESTRICTED-SUPPORT ALL-WITT ARTIN--SCHREIER CONTROL (2026-08-24)
xmodel/witt-tate-control-20260824.md (exact closed-form producer plus internal
audit), with xmodel/review-witt-tate-control-claude.md (different-model hostile
review: **CONFIRMED**). This is a separate descendant/control, not a widening
of the finite `W2-SURVIVOR` case above.
- PROMOTED AT THE ALL-WITT / RESTRICTED-ANALYTIC CONTROL TIER: for every odd
  prime `p` and `n>=1`, over `W_n(F_p)=Z/p^n`,
  `F_n=(x-x^p, y*sum_{j=0}^{n-1}(p*x^(p-1))^j)` has exact integer determinant
  `1-p^n*x^(n*(p-1))`, hence determinant one modulo `p^n`. The maps are
  compatible under every Witt truncation and the fixed distinct points
  `(0,0),(1,0)` collide at every level. Each map is finite etale of rank `p`.
- LOAD-BEARING ESCAPE: `Q_n` has exactly `n` monomials and degree
  `1+(n-1)(p-1)`. Thus support and degree grow linearly. The inverse limit is
  the nonpolynomial restricted-analytic/rational bidisc map
  `(x-x^p,y/(1-p*x^(p-1)))` in `Z_p<x,y>`, still finite etale of rank `p`,
  determinant one, and noninjective. It is not a polynomial endomorphism of
  affine two-space.
- CONSEQUENCE AT THIS SCOPE: no later finite Witt obstruction can kill this
  seed when growing support is allowed, and compatible lifting through every
  finite level does not by itself yield a characteristic-zero polynomial.
  The missing uniform-support-or-polynomial-limit criterion was already
  stated in `xmodel/sol-witt.md` section 6; this is its first explicit
  same-seed witness.
- NOT SHOWN: no bounded-support or uniformly bounded-degree tower, alternate
  polynomial lift, impossibility theorem for other lifts, complex polynomial
  map, germ, or JC2 counterexample follows.
- GOVERNANCE: the coordinator accepts this as the synthesis's single
  explicitly provisional, closed-form descendant while review ran, not as a
  same-generation enumerative `W3`/support-search cap. It is now independently
  confirmed; the W search root remains stopped.

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
every counterexample; (`G2-PSC`) NO transport theorem carries GGV corner data
through Sigray's normalization — the sheet construction does not consume
GGV data as written; (G5) NO upper bound on td. Gap 4 adjudicated: the
td-7 book carries its §11a completeness certificate and td-11 its
conditional certificate (Grok), but a UNIVERSAL full-configuration
landing theorem for the b>=2 sector does not exist (Sol) — both true.
HONEST SCOPE of promoted ladder results: book-relative (every
configuration in the enumerated books dies), pending the book-landing
theorem. The reduction consolidation (T-chain + gap repairs) is now a
top-tier theory objective alongside residue-A.

## td-12 type-(3,5) book (2026-08-18)
PROMOTED AT THE HONEST / LIST-RELATIVE TIER: all 14 entry-level cells
of the td-12 type-(3,5) book (poles 2 x (6,1,2,5) — the single
below-bound filed entry) are TOWER-DEAD on the ENUMERATED 74-gap
candidate list (78 raw): 6 SPINE-DEAD-H8 + 8 CLASH-DEAD-FIRSTDEATH,
conditional on the SEVEN named fail-closed classes (a)-(g).
List-completeness is LIST-RELATIVE with residuals named (Lemma
FD-TRICHOTOMY); the u=1 gap-1/3 candidate is exhibited UNREFUSED =
the named load-bearing residual (class (c)/NF-P). No X vertex exists
at this entry: the kill is the first-death refusal theorem (den-
refusal of every enumerated candidate maximal gap), replacing the
td-7/td-11 X-clash pattern. TDBOUND consequence: the filed ladder's
live frontier is exactly {residue-A} plus the unadjudicated
above-bound entries (td 8, 10, 12-(2,3)/(2,5), 14). Review chain:
grok-td12-review (SOUND-WITH-ERRATA — round-2 errata folded: 74/78
candidate recount vs the stale 54, corrected budget-10 core
multipliers, de-tautologized spine checks, citation hygiene). Engine
cases/td12_book.py, 14 gates, exit 0. Source: BOOK-TD12.md.

## D23 FIBER-LOCAL NONEMPTINESS (2026-08-19)
PROMOTED AT THE FIBER-LOCAL / MOD-p TIER: on the radical_point chart fiber
of the D21 window (the CORE2 object, SHEET6-DIRECTIONB 7.S3), the depth-23
Row_22 obstruction does NOT eliminate the window: V(row22red) is nonempty
over the algebraic closure of F_p at p = 105337, 105673, 200257.
Chain: NF reduction of the 6 compat rows against the banked 397-element
fiber GB (8.S4 payload; point-identity gates 72/72 x2 primes) -> affine
structure A = C.diag(uW1^2,uW2^2,uW1^2,uW2^2), C constant rank 2 -> exact
rank-2 residual g1,g2,g3 with V(fiberGB+g) = proj V(row22red), EMPTY iff
EMPTY (rank pinned by saturated scales) -> msolve GB 509 elements != [1]
at all three primes (det23 lanes, 63s each; det23_p*.out banked).
Witnesses: 6 explicit F_p points per prime at 105337/105673, verified
400/400 emission rows in python-flint, back-solved to FULL 72-variable
depth-23 configurations (54/54+76/76+77/77 rows; cases/d23_witnesses_*.json,
8.S6). Survivor locus dimension 11 (all three primes; g's cut codim 2).
Review: Grok hostile recompute CONFIRMED all load-bearing claims incl.
bidirectionality + scope honesty (xmodel/grok-det23-review.md); Sol
independent structural convergence + 85% prior (xmodel/sol-avenues3.md).
SCOPE LIMITS (explicit): one radical fiber of 36; mod p only (no char-0
statement); chart-local; says nothing about the other fibers or about
DEPTH-STAB germ certification (e-spec unbanked, experimental readings
fail closed). Supersedes: the row22compat/row22red 12h timeouts (now
explained as nonempty-GB grinds; rc=124 x3 + x2 banked, third lane killed
at 305GB post-confirmation, rc=137).

## FILTERED DIFFERENTIAL NEWTON LEMMA (2026-08-19)
PROMOTED AT THE ABSTRACT-THEOREM TIER: the filtered Newton/Hensel lifting
theorem for the Euler/Ore linearization (xmodel/sol-newton-lemma.md
Theorem 3.1 + Cor 3.2 + supporting lemmas): over any field (incl. char p),
a residual of global t-order D lifts to a formal solution whenever
D >= 2e+1, where e = the delayed-parametrix loss of the linearization;
Euler terms need no conjugation. Proof: Sol (Route B contraction);
review: Grok hostile replay CONFIRMED (xmodel/grok-newton-review.md).
SCOPE WITHHELD (per both documents): no promoted e+ at any point, no
D23/D25 germ certified, CYCLIC-30/BRIDGE-30/PARAM-30/FILTER-30
application gates open. This closes CONJECTURE E-HENSEL and supplies the
mechanism awaiting a D25 survivor with a certified e+.

## FIBER EQUIVARIANCE THEOREM (2026-08-20)
PROMOTED (scoped algebraic theorem + exact D25 realization): the 36
radical fibers of the D21 window form a single free orbit (G-torsor) under
G = (C3)^2 x (C2)^2, acting by diagonal scalings with entries in
{+-1, +-omega, +-omega^2} subset F_p at both banked primes; the fiber
transports are F_p-SCHEME isomorphisms, and the character identity
F_{l,g.lambda}(T_g x) = chi_l(g) F_{l,lambda}(x) holds as an exact
monomial-dictionary identity on all 9,792 generator-edge row pairs of the
parked D25 systems (residuals R1-R5 character 0). Proof: Sol
(xmodel/sol-pcc-orbits.md); review: Grok hostile recompute CONFIRMED
(xmodel/grok-orbits-review.md). RESIDUAL GAPS (named, minor): un-rerun
source-pkl weights; 216 witness checks pending; future-emission fidelity
must be re-gated per new emission. CONSEQUENCE: one fiber decides all 36
at D25 (and at any depth whose emission passes the fidelity gate) --
per-fiber cost /36 permanently; the atlas support identity is explained.

## D25 FAMILY NONEMPTINESS + CELL STRUCTURE (2026-08-21)
PROMOTED AT THE MODULAR TIER (p = 105337 and 105673; emission-fidelity
caveat inherited from SHEET6-DIRECTIONB sect 9; chart-local as always):
the depth-25 residue-A family systems are NONEMPTY of dimension 14 --
and moreover each of the 36 fiber systems is 16 DISJOINT COPIES OF A^14
over F_p (union: 576 cells), identified by an exact certificate: 2 lift
pivots (minor = unit x uW1^2 uW2^2) + 8 Laurent-unit base pivots with
well-founded DAG, hcore/hlin ideal-membership from raw rows, explicit
per-fiber witnesses vanishing 34/34, Jacobian ranks 14/18. NO Groebner
basis was required; the 48h union lanes are superseded.
Chain: Sol certificate (xmodel/sol-ideas-0821.md) -> independent
mechanical replay CONFIRMED (cases/d25_certificate_replay.json, 9.S2;
negative controls 24/24) -> Grok hostile recompute CONFIRMED
(xmodel/grok-d25cert-review.md: 72/72 fibers, freeness verified).
The pre-registered ECO-D25 codim-2 prediction is REFUTED (height-1 cut).
CONSEQUENCE: the residue-A window survives depth 25 family-wide with
smooth rational cell structure; the kill direction has now failed at
D23 and D25; the discriminating question moves to germ certification
(corrected e+ on the A^14 cells vs the Newton criterion) and, on the
kill side, to whatever mechanism could terminate a cell tower that
grows codimension strictly slower than depth.

## PURE-BOUNDARY JACOBIAN IDENTITY + G5 CLASS-KILL (2026-08-23, dual-confirmed)
Two EXACT, hand-checkable results from the G5/rooftop lane
(xmodel/sol-rooftop.md), independently CONFIRMED by Grok adversarial
recompute (xmodel/grok-rooftop-review.md, direct computation + toy checks).

(1) PURE-BOUNDARY JACOBIAN IDENTITY. Let f,g in k[x,y], F,G their degree-d,e
homogenizations, J(f,g)=f_x g_y - f_y g_x. Chain rule gives
dF/dX = Z^{d-1} f_x(X/Z,Y/Z), so
    F_X G_Y - F_Y G_X = Z^{d+e-2} * J(f,g)(X/Z,Y/Z).
KELLER case J=j in k*:  F_X G_Y - F_Y G_X = j * Z^{d+e-2}  (all critical
contributions created at the line at infinity). Grok toy-verified on the
elementary automorphism f=x+(y+x^2)^2, g=y+x^2 (LHS = Z^4 exactly) plus five
more pairs; homogeneity, dehomogenization, and monomial-uniqueness all clean.
Corollary: det D[F^beta:G^alpha:Z^N] = c*F^{beta-1}G^{alpha-1}Z^{N+d+e-3}.
TIER: EXACT, dual-model confirmed. This is the polynomial-origin datum the
formal countermodels lack.

(2) G5 CLASS-KILL (permanent NO-GO). The family f_B=x^{Balpha}+y,
g_B=x^{Bbeta}+y^{Bbeta-1} (coprime 2<=alpha<beta) has: finite normalized
multi-Rees algebra, antinef/complete rooftop (definitional), and the balanced
common leading power F_d=(X^B)^alpha, G_e=(X^B)^beta (so even J(F_d,G_e)=0),
YET normalized rooftop energy
    E_MR = td/(alpha beta) = d(e-1)/(alpha beta) = B^2 - B/beta  ->  infinity.
Grok CONFIRMED td=d(e-1) (Gauss-irreducibility of P(X)-v, deg_x = d(e-1)>e)
and the energy arithmetic on six triples. Non-Keller (J not constant), so not
a G5 counterexample -- it REFUTES the implication class
{finite generation, rooftop convexity, common leading power} => uniform bound.
Also Hodge index / Teissier-Rees-Sharp / reverse-AF give e_inf(I,J)<=N^2, i.e.
E_MR >= 0 -- the WRONG SIGN (G5 needs the upper/near-max bound).
CONSEQUENCE: any proof along this rooftop route MUST use the full Keller
identity (1), not finite generation, convexity, Hodge, mixed volume, or the
leading-form shadow of Keller. CORRECTION: KJN(C),
deg Psi = alpha beta * td <= C(alpha beta)^2, gives the type-relative ceiling
td <= C alpha beta; it is not equivalent to an absolute G5 ceiling unless a
separate theorem supplies a bounded/cofinal type menu with valid provenance.
The EXACT, dual-model-confirmed tier here applies to the identity and the
class-kill, not to the still-conjectural KJN estimate.

## RAW BOUNDARY PASSPORT/CAPACITY PROBE RETURNS COSTUME (2026-08-24)
xmodel/round1-boundary-passport-20260824.md and
cases/round1_boundary_probe/ (exact QQ producer run; coordinator byte-identical
replay), with xmodel/review-round1-proof-gates-claude.md (different-model
hostile review: **CONFIRMED**). This is a route-falsification result, not a
theorem about every possible compactified boundary invariant.
- Exact control suite: identity; `T_n=(x,y+x^n)` for n=2,4;
  `T_4^{-1} o T_4`; the promoted Henon automorphisms at r=0,1; and the
  non-Keller class-kill member only as a negative control. One explicit
  boundary blow-up chart is included.
- VERDICT **COSTUME** for the tested raw proposals. Gradient-cokernel
  Fitting/Smith splits, log-coframe Smith splits, and action-primitive pole
  orders vary under polynomially equivalent presentations and/or the explicit
  blow-up; tame and Henon automorphisms make them arbitrarily large, while
  exact orbit minimization returns the identity data. The stable Keller-suite
  outputs are the log-determinant volume orders and zero residues of exact
  meromorphic differentials, both consequences of `J=1` rather than stronger
  capacity data.
- KILLED AT THIS SCOPE: untwisted action-residue charge, raw primitive pole
  order as an invariant budget, raw `Q`/`Fitt_1`/Smith filtration as a
  coordinate-free passport, unsigned raw log-coframe/localized-Chern charge,
  and raw boundary exponent as a uniform consumable cap.
- NOT KILLED: the exact pure-boundary identity; use of `Q` as a checksum after
  a proved choice-independent minimization/compactification; boundary-twisted
  forms; or a signed global invariant using complete polynomial data. Those
  redesigns first owe covariance/minimality and positivity, and no theorem lane
  is opened by the present computation.

## TRACE-REGULARITY AUDIT: CURRENT CONTACT PACKET IS INSUFFICIENT (2026-08-24)
xmodel/round1-trace-regularity-20260824.md and
cases/round1_trace_probe/ (exact producer run; coordinator byte-identical
replay), with xmodel/review-round1-proof-gates-claude.md (different-model
hostile review: **CONFIRMED**).
- EXACT CHARACTERISTIC-ZERO REDUCTION: for a generically finite plane Keller
  map of function-field degree `d`, regularity of the first `d` field power
  traces of `x` and `y` is equivalent to integrality/finiteness and hence to
  automorphy. This is an honest reformulation of the missing finiteness step,
  not a shortcut to it; the required cutoff `d` is itself unbounded.
- EXACT UNDERDETERMINATION CONTROL: two denominator-42 formal completions have
  identical retained support, contacts, gcd chain `42 -> 6 -> 2 -> 1`, indices
  `(7,3,2)`, leading data, and full `m=1` principal parts, but their `m=2`
  residues are respectively 84 and 168. The varying coefficient sits at
  offset 126, beyond the last retained level 79.
- CONSEQUENCE AT THIS SCOPE: the current contact-only packet does not determine
  the quadratic trace principal part. The missing datum is an
  affine-target-divisor-tagged completed branch pairing, including coefficient
  convolution and residue-field traces. Do not build a general TRACE-REG
  engine from the current packet.
- NOT SHOWN: the formal pair is not a Keller countermodel; TRACE-REG is not
  refuted; no nonautomorphic Keller map is produced; and no claim is made that
  every augmented packet is insufficient or that a universal trace cutoff is
  impossible.

## NORMALIZATION/DIFFERENT RECEIVER DOES NOT FIX QUADRATIC MOMENTS (2026-08-24)
xmodel/round2-norm-moment-sep-20260824.md and
cases/round2_norm_moment_sep/ (exact producer), with
xmodel/review-norm-moment-sep-grok.md (different-model hostile review:
**CONFIRMED**).
- PROMOTED AT THE FORMAL-LOCAL CONTROL TIER: for `t=u^42`, the two exact
  Darboux completions
  `x_b=u^-84+u^-42+u^-30+u^-10+u^-5+b*u^42`,
  `y_b=42*q*u^41/(d x_b/du)`, with `b=1,2`, have the same finite local
  algebra, different `(42u^41)`, conductor exponent, selected contact/gcd
  decoration, coordinate valuations, local Jacobian two-form, and complete
  first trace principal part.
- DECISIVE SEPARATION: the `t^-1` coefficients of `Tr(x_b^2)` are 84 and 168.
  Thus the displayed local algebra/different/contact/Jacobian packet does not
  determine even the quadratic coordinate moment.  Coordinate multiplication
  data differ, as they must, and can carry the missing information.
- HARD STOP HONORED: the preregistered native-source type gate was not run once
  `DIFFERENT-INSUFFICIENT` fired.  No claim is made that a native GGV packet
  cannot populate a richer target-divisor-tagged receiver.
- NOT SHOWN: these are formal-local controls, not polynomial Keller maps; no
  global polynomial-origin identity is excluded, TRACE-REG is unaffected at
  its honest finiteness-equivalent scope, and no JC2 conclusion follows.

## G2-BD/KJN FORMAL SEPARATION + PUISEUX gcd DICTIONARY (2026-08-23; terminology corrected)
The unification lane (xmodel/sol-unify.md) asked whether one Keller bound
closes both local objectives. It found a NOTATION COLLISION in the "shared
nu" and two non-implications in a weakened formal system; the earlier
"independent walls" verdict is superseded by the scoped reading below.
- EXACT Puiseux gcd dictionary (Lemma 1.1): for a pole branch with denominator
  kappa_i and characteristic gcd-drops nu_j, prod_j nu_j = kappa_i (telescoping
  gcd chain, e_s=1 by minimality). Residue-A ladder: 1 -x7-> 7 -x3-> 21 -x2->
  42, so kappa(P_i)=42=7*3*2.
- The ROOFTOP nu_P is only the LEAF decoration (final factor 2); the DEPTH
  product is over ALL characteristic vertices (7*3*2). The Belyi passport
  {2,3} ramification is a degree-4 QUOTIENT invariant AFTER common-carrier
  cancellation -- the factor 7 lives in the same genome but nowhere in the
  passport. Carriers cancel exactly: (C^4 h1)^3/(C^3 f)^4 = h1^3/f^4.
- KJN(C) =/=> UCD: formal countermodel (Lemma 2.2) inserts r characteristic
  vertices (q=q'=2, w=2 preserved) keeping td=6, deg Psi=36, E_MR=1 fixed
  while kappa_i = 42*2^r -> infinity. Even restricting factors to {2,3} fails.
- UCD =/=> KJN(C): formal family (Lemma 3.1) kappa_P=6 fixed, b_P=b odd -> inf,
  giving E_MR=b, td=6b -> infinity.
Both countermodels are FORMAL (satisfy the tree/arithmetic identities, no known
polynomial-origin Keller realization). CORRECTED CONSEQUENCE: they separate
the post-residue-A carrier predicate `G2-BD` from the type-relative KJN
predicate in the weakened formal system. They say nothing about `G2-PSC`, the
global GGV-to-Sigray transport/fidelity obligation, and do not prove
non-implication inside the class of actual polynomial Keller maps. The
dictionary is exact but this separation is single-model/banked formal
evidence, not a promoted two-way independence theorem. The unrestricted K2C
bridge proposed here is explicitly superseded by the later dual-confirmed
Henon refutation; only appropriately restricted minimal/nonautomorphic
residue-A variants remain open.

## TYPE-RELATIVE KJN: LOCAL SUFFICIENT LEMMA RPMC(C) => KJN(C) (2026-08-23; corrected)
The former G5 lane (xmodel/sol-kjn.md) gives a proved-in-lane sufficient
reduction from a LOCAL one-root capacity lemma to type-relative KJN. It does
not reduce the absolute td-ceiling without the separate type-menu/provenance
theorem stated below.

EXACT structures (all char 0; F,G degree d=Balpha,e=Bbeta homogenizations;
M=d+e-2; accepted input: the dual-confirmed pure-boundary identity
F_X G_Y - F_Y G_X = j Z^M):
- GRADIENT MATRIX FACTORIZATION (the Keller-specific object). A=[[F_X,G_X],
  [F_Y,G_Y]] has det = j Z^M, so the cokernel Q has Fitt_0(Q)=(Z^M): Q is
  supported scheme-theoretically on the M-fold thick line M*L_inf with NO extra
  Jacobian curve. After removing exceptional monomials, the transformed det is
  a UNIT off the strict transform of Z=0. This is the exact datum that ordinary
  ramification effectivity, Chern/Hilbert data, and coprimality all discard.
  (Its Hilbert poly chi(Q(t)) = M t + (3M-(d-1)^2-(e-1)^2)/2 still scales
  quadratically in B, so ordinary invariants alone give no B-independent bound.)
- ENERGY LOCALIZATION (EXACT). Common leading power forces F_d=xi H^alpha,
  G_e=eta H^beta, deg H=B, div_{Linf}(H)=sum mu_i P_i, sum mu_i=B. The rooftop
  energy splits with NO cross-terms over proper roots: E_MR = sum_i E_i,
  E_i = (1/2) sum_{p > P_i} (R_p/alpha - S_p/beta)^2.
- Coprimality lower quantum (EXACT): each nonzero R_p/alpha - S_p/beta has
  |.| >= 1/(alpha beta), so its square >= 1/(2(alpha beta)^2) -- a lower bound,
  not the needed upper bound.

CONJECTURE RPMC(C) (root-weighted pure-minor capacity): for each proper root,
E_i <= C mu_i / B, under the pure-minor identity hypothesis.
THEOREM 7.1 (PROVED conditional reduction): RPMC(C) => KJN(C). Sum E_i over
roots, sum mu_i = B => E_MR <= C => deg Psi = (alpha beta)^2 E_MR <=
C(alpha beta)^2. So RPMC(1) => sharp KJN(1) => td <= alpha beta at each
provenanced fixed type. CORRECTION: an absolute/cofinal TDBOUND conclusion
also requires an independently justified bounded type menu, and even that
would not close the transport, source, landing, or coverage gaps needed to
make the full book ladder unconditional.

SEPARATION FROM THE CLASS-KILL DECOY (EXACT, sec 8). The non-Keller control
f_B=x^d+y, g_B=x^e+y^{e-1} has Q_B = d(e-1)X^{d-1}Y^{e-2}Z - e X^{e-1}Z^{d-1}
!= j Z^M (an EXTRA Jacobian curve), yet at the first boundary valuation its
log-effectivity coefficient equals +1, IDENTICAL to a Keller pair. Therefore
log-effectivity alone cannot be the Keller step; the separating datum is
precisely the VANISHING of the residual Jacobian curve in the transformed
gradient cokernel. E_MR = B^2 - B/beta for this family violates RPMC's C mu/B
demand, with no contradiction because the matrix-factorization hypothesis fails.
TIER: reduction + all listed structures EXACT/PROVED (single-model, sol-kjn);
RPMC(C) is the open local lemma. NOT YET Grok-reviewed.

Bridge status (companion, xmodel/sol-k2c.md): UNRESTRICTED K2C is FALSE
(explicit Henon automorphism tower, td=1, kappa=42*2^r -> inf). The review was
pending when this entry was drafted; the next entry records Grok's independent
confirmation. Thus unrestricted UCD does NOT follow from the bounded-td data.
No KJN => `G2-BD` theorem is established; the restricted route still needs its
own UCD-A-min bound (degree-minimal nonautomorphic type-(2,3) residue-A). The
two local predicates remain unbridged; the only conditional bridge presently
named is CONJECTURE K2C-min.

## UNRESTRICTED K2C REFUTED: HENON AUTOMORPHISM TOWER (2026-08-23, dual-confirmed)
Theorem 2.1 of xmodel/sol-k2c.md, independently CONFIRMED by Grok hostile
recompute (xmodel/grok-k2c-review.md) with explicit hand computation.
Generators H_q(u,v)=(v, v^q - u), J=1, inverse (u,v)->(u^q - v, u). Fix r>=0,
s=r+4, indices q=(7,3,2,...,2); P_0=x,P_1=y,P_{i+1}=P_i^{q_i}-P_{i-1};
(f_r,g_r)=(P_s,P_{s+1}). Then (all CONFIRMED (i)-(vi)):
  - Phi_r is a polynomial AUTOMORPHISM of A^2, J=1, hence td=1;
  - pole orders at the unique place infinity: n_0 = prod_{j=1}^{s-1} q_j =
    7*3*2^{r+1} = 42*2^r; characteristic indices (7,3,2,...,2);
  - pole Puiseux denominator kappa_r = 42*2^r -> INFINITY;
  - deg f_r = kappa_r, deg g_r = 2 kappa_r;
  - the FULL pure-boundary identity holds: (F_r)_X(G_r)_Y-(F_r)_Y(G_r)_X =
    Z^{3 kappa_r - 2} (Grok verified Z^124 at r=0 by direct expansion).
CONSEQUENCE: bounded td + polynomial origin + the full boundary identity do
NOT bound kappa -> UNRESTRICTED K2C is FALSE. Grok confirms the scoping is
legitimate: the family is one-pole, reduced type (1,2), degree-minimizes to a
linear automorphism (kappa=1), never type (2,3), does not realize residue-A.
NET: unrestricted UCD does not follow from bounded td plus polynomial origin
and the boundary identity. Because this automorphism never realizes residue-A,
the construction addresses neither `G2-PSC` nor the restricted `G2-BD`
obligation. That residue-A route still needs UCD-A-min; the only conditional
bridge presently named is CONJECTURE K2C-min. TIER: EXACT, dual-confirmed.

## TYPE-RELATIVE KJN CHAIN: RPMC(C) <=> PC(C), POLAR-EXCESS BRIDGE (2026-08-23; corrected)
xmodel/sol-rpmc.md executes two of the three sol-kjn §7 bullets EXACTLY (single
-model tier), reducing RPMC to a concrete polar-capacity bound.
- THICK-LINE DEGENERATION (EXACT/PROVED). At a root of multiplicity mu, the
  gradient cokernel is a free k[[u]]-module of rank M=d+e-2; z-multiplication
  has ONE Jordan block of length M over k((u)), exactly TWO blocks (r, M-r) at
  u=0 with 1<=r<=d-1, M-r>=e-1, and Smith form diag(1,...,1,u^c,0), c=alpha*mu-1.
  So exactly ONE transverse elementary-divisor defect of exact size alpha*mu-1;
  all jump COUNTS determined, jump EXPONENTS not.
- POINT-BASIS = INTERSECTION DEFECT (EXACT/PROVED). With n_P =
  i_P(F-lambda Z^d, G-nu Z^e) and Delta_P = alpha*beta*B*mu - n_P (a nonnegative
  integer): E_P = Delta_P/(alpha beta) and sum_{p>P}(beta R_p - alpha S_p)^2 =
  2 alpha beta Delta_P. Hence the stronger quantum E_P >= 1/(alpha beta).
- EXACT POLAR BRIDGE (PROVED, pure-minor used exactly): on the normalization
  branches gamma of a general F-fiber above P (m_gamma = ord_gamma z),
  Delta_P = sum_{gamma|P} max{0, ord_gamma F_X - (d-2) m_gamma}.
- REDUCTION: CONJECTURE PC(C): sum_gamma max{0, ord_gamma F_X - (d-2)m_gamma}
  <= C alpha beta mu / B. By the above, PC(C) <=> RPMC(C), and Theorem 7.1
  gives the one-way implication RPMC(C) => KJN(C). No converse from KJN to the
  rootwise capacity bound is proved.
- KELLER SEPARATION (EXACT): for the class-kill decoy the residual Jacobian
  curve adds branch order de-d-1; intrinsic polar excess is only 1 while the
  actual defect is de-d, so the bridge (0.6), freeness, and nilpotence all fail
  exactly because Fitt_0 != (Z^M). Sanity gate holds.
STATUS: PC(C) <=> RPMC(C) => KJN(C) (type-relative). The remaining step on
this sufficient route is to bound
the intrinsic polar excess of the generic fiber at a Keller root by C alpha beta
mu/B. No finite B-independent C obtained. TIER: DECISIVE PARTIAL (single-model).

## TWO LOCAL SUFFICIENT ROUTES, NOT BOTH FOUNDATIONAL WALLS (2026-08-23; corrected)
The type-relative mass route (xmodel/sol-pc.md) and post-residue-A bounded-delay
route (xmodel/sol-ucda.md), both at the single-model tier. Neither addresses
the separate global transport obligation `G2-PSC`.

Type-relative KJN route: PC(C) <=> CONJECTURE DIR(C)
(displaced-intersection retention). For general
lambda,nu at a boundary root of mult mu (c=alpha*mu-1):
    n_P = i_P(Phi - lambda z^d, Gamma - nu z^e) >= e(c+1)(1 - C/B^2).
Since e(c+1) = alpha beta B mu, DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C). PC's
1/B factor is thus a 1/B^2 RELATIVE intersection-retention bound.
New EXACT structures (PROVED):
 - canonical fiber differential omega = dy/f_x = -dx/f_y = dg/j; polar-excess
   term a_gamma = ord_gamma F_X - (d-2)m_gamma = -ord_gamma omega - 1; adjunction
   SIGNED identity Delta_inf - K_inf = 2 - 2 g_C - s (does NOT cap the positive
   part; the finite-end compensator K_inf is uncontrolled).
 - Smith telescope: higher z-filtration torsion tau_q <= min(q,M-q)(alpha*mu-1),
   i.e. every higher jump bounded by the first Smith defect c=alpha*mu-1.
 - semicontinuity gives n_P <= i_P (UPPER); DIR needs a LOWER bound. Wrong way.
STATUS: DIR(C) is a sufficient crux for type-relative KJN. Any finite
B-independent C gives td <= C alpha beta; an absolute/cofinal TDBOUND theorem
additionally needs an independently justified bounded type menu and provenance.

`G2-BD`: CONJECTURE A-SCALE => UCD-A-min => bounded delay. These are one-way
sufficient implications, with no converse claimed. DECISIVE NEGATIVE on using
degree-minimality alone:
by the char-0 coordinate-cusp theorem a type-(2,3) rectangular cusp pair is
ALREADY Aut-orbit degree-minimal at every common scale, so degree minimality
gives NO bound deg f <= Phi(6,(2,3)). (Contrast: the Henon type-(1,2) tower is
removable because V-U^2 is a coordinate; that mechanism is absent for reduced
type with both entries > 1.) Constant Jacobian gives only ord_t f_y = 3-kappa_i
(compatibility); branch conductor c(P_i)=2 delta(P_i) >= 2(kappa_i-1) is a LOWER
bound. Neither caps kappa_i.
A-SCALE: a+b <= B_A for orbitwise degree-minimal nonautomorphic residue-A pairs
(Sigray rectangle base (a,b)) => kappa_i <= deg f = 2(a+b) <= 2 B_A =: K_A.
Conditional K_A=42 only under the global-coordinate-tail hypothesis.
STATUS: A-SCALE is a sufficient `G2-BD` crux for this residue-A architecture;
a counterexample sequence to that bound, if one exists, lives in the
non-removable type-(2,3) carrier direction.

CORRECTED LOCAL MAP: DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C), and
A-SCALE => UCD-A-min => `G2-BD`. KJN remains type-relative; none of the reverse
arrows just omitted is established. The Henon result dual-confirms only the
failure of unrestricted K2C/UCD. The local reductions remain single-model,
DECISIVE PARTIAL; they do not close `G2-PSC`, source, landing, or coverage.

## NO TWO-WAY LOCAL DIR/A-SCALE UNIFICATION: DIFFERENT/CONTACT LEDGER (2026-08-23; corrected)
xmodel/sol-bridge2.md compares the two local sufficient routes (DIR for
type-relative KJN, A-SCALE for `G2-BD`). CORRECTED VERDICT: no equivalence or
common controlling invariant is obtained; this is not a promoted symmetric
independence theorem and does not concern `G2-PSC`.
- EXACT different/contact ledger (PROVED): on a pole branch gamma of a general
  f-fiber, with m=ord z, p=pole order of g, I_gamma = contact with the other
  branches of the fiber germ:
     ord_gamma F_X = (d-2)m + p,   c(gamma) + I_gamma = (d-3)m + p + 1,
  hence the branch polar defect Delta_gamma = p (= 3 on residue A, the pole
  order of g), while the conductor 2 delta(gamma) measures the branch different.
  The common ledger carries an UNCONTROLLED CONTACT term I_gamma.
- CONSEQUENCE: a bound on the polar excess (DIR) does NOT, in the formal
  ledger, bound the conductor/kappa_i; the l=0,nu=2 tower keeps Delta_gamma=3
  while kappa_i, delta -> infinity. In the other direction, A-SCALE does imply
  a coarse residue-A DIR bound by bounding the whole degree scale. Thus the
  established comparison is asymmetric: DIR does not recover A-SCALE, while
  A-SCALE supplies a coarse DIR only on the fixed residue-A inventory.
- CONCRETE residue-A germ arithmetic (all EXACT): characteristic exponents
  (b1,b2,b3)=(54,74,79), approximate-root generators (42,54,398,1199), conductor
  c(P_i)=2278, delta(P_i)=1139, contact I_i=4656, d=168, m=kappa=42, p=3. The
  ledger closes with no slack (ord F_X = 6975 = 6972 + 3). DIR ratio
  B*Delta_P/(alpha beta mu) = 84*6/(6*63) = 4/3, so DIR(4/3) is EQUALITY on the
  filed residue-A root (independent of the large conductor 2278).
- DECOYS (Henon automorphism tower, non-Keller class-kill) BOTH have intrinsic
  polar excess 1 and conductor -> infinity, but are excluded by ORTHOGONAL
  mechanisms: Henon by orbit-minimality, class-kill by pure-Jacobian support
  (Fitt_0=(Z^M)). Neither Delta nor delta alone excludes both; no local
  no-decoy rigidity statement using only either displayed invariant is
  presently established.
- Equivalent reformulation of a **uniform residue-A conductor ceiling** (not
  of `G2-BD` or A-SCALE): CONJECTURE CONTACT-DEFICIT
  `(d-3)kappa_i - I_i <= K_A`. By the ledger with pole order `p=3`, this is
  exactly `c(P_i) <= K_A+4`; combined with
  `c(P_i) >= 2(kappa_i-1)`, it is a sufficient route to UCD-A-min and hence
  `G2-BD`. No converse from carrier boundedness or A-SCALE is asserted.
TIER: ledger + arithmetic EXACT/PROVED (single-model); the no-equivalence
assessment is banked but not hostile-reviewed/promoted. NET: no present local
lemma merges the two sufficient routes. This does not rule out a stronger
future theorem proving both, and it leaves `G2-PSC` and the other foundational
landing/coverage obligations untouched.

## DIR CENSUS + THE ALGEBRAIZATION CONVERGENCE (2026-08-23)
xmodel/sol-dircensus.md, full rootwise census of the td<=12 books.
- R_P = B*Delta_P/(alpha beta mu_P), Delta_gamma = pole order of g.
- Max FULLY-SPECIFIED filed R_P = 4/3 (residue-A Y-root, equality); actual
  Keller controls (Henon) only 1/2. But td<=12 type-(2,3) book rows FORCE
  max_P R_P >= 3/2, 5/3, 11/6, 2 (td=9,10,11,12) under any Keller lift; these
  are weighted averages so the mass-bearing root can be larger still. => C=4/3
  is NOT a supported DIR ceiling.
- DIR(C) <=> CONJECTURE RPC: sum_{gamma|P} p_gamma <= C alpha beta mu_P/B. The
  pure-minor identity gives only Delta_P <= alpha beta B mu_P (R_P <= B^2), the
  wrong B-scale. VERDICT: DIR NEUTRAL, no finite C supported (single-model).
- DIR counterexample lead (additive pole-mass axis): [3A;A,1,2]^2, pole profile
  (3A,3A), td=6A; any Keller lift => max R_P >= A -> infinity.
CONVERGENCE ASSESSMENT: both local conjectures have formal counterexample families
(A-SCALE: carrier tower kappa=42*2^r; DIR: [3A;A,1,2]^2 pole-mass tower), and
BOTH are gated by the SAME meta-question -- do these formal Newton/entry
families ALGEBRAIZE to actual polynomial Keller pairs? Algebraize(either) =>
JC2 counterexample (provided the advertised nonautomorphic realization and
provenance are certified). CORRECTION: failure to algebraize these particular
families would not prove the universal bounds, much less JC2; other formal
families and the source, `G2-PSC`, landing, off-axis, and type-provenance gaps
remain. TIER: census EXACT/book-relative; the convergence claim is a
single-model lead assessment, not a stopping rule or promoted reduction.

## DATED STRATEGY-STATUS CORRECTION — G2 SPLIT AND ARROWS (2026-08-23)

This entry explicitly supersedes every overloaded `G2`, `KJN <=> RPMC`, and
`UCD-A-min <=> A-SCALE` reading in the same-day roadmap entries above. It does
not retract their exact local identities; it corrects their global strategic
interpretation and status. The current detailed dependency theorem is
`ladder/REDUCTION.md`; this entry records the evidence/status correction.

- **`G2-PSC` (packet/sheet compatibility)** is the missing global theorem
  transporting a selected GGV packet/corner, with provenance, to a specified
  decorated Sigray pole tree faithfully enough for the book machinery.
- **`G2-BD` (bounded delay/carrier)** begins only after residue-A has been
  reached and asks for the carrier/delay bound needed to enter a finite book.
  Neither scoped obligation implies the other.
- A hybrid proof using GGV restrictions in the Sigray stage owes `G2-PSC`. A
  pure Sigray proof may bypass `G2-PSC` by selecting/minimizing the hypothetical
  counterexample wholly in that frame, but then it may not claim the unused
  GGV farm as input and still owes Sigray source, all-branch landing/coverage,
  `G2-BD` where used, and type/td control.
- The correct same-constant local arrows are
  `DIR(C) <=> PC(C) <=> RPMC(C) => KJN(C)`. There is no proved converse
  `KJN => RPMC`. KJN yields only `td <= C alpha beta` at a provenanced fixed
  type; absolute/cofinal control needs an independent bounded type menu with
  bounded constants.
- The correct architecture-scoped delay arrows are
  `A-SCALE => UCD-A-min => G2-BD`. No converse holds on present evidence, and
  restricted UCD-A-min does not imply the unrestricted UCD refuted by Henon.

STATUS: the pure-boundary identity/class-kill and unrestricted Henon
obstruction are dual-confirmed at their stated scopes. The KJN/RPMC/PC/DIR,
UCD-A-min/A-SCALE, formal countermodel, and DIR/A-SCALE comparison work is
single-model decisive partial unless separately reviewed later. In particular,
there is no promoted independence theorem joining `G2-PSC`/`G2-BD` to the
G5/type-ceiling side, no promoted merger theorem, and no implication making
the complete book ladder unconditional.

## D43 FULLY-RECONSTRUCTED RESIDUE-A FAMILY = NONEMPTY (2026-08-23, MOD-p / INTERNAL)
xmodel/sol-d43full.md; cases/d43_full_{family.py,certificate_p*.json,floor_p*.json}.
Fixed Sigray scale B=84, fiber a00pp, p=105337 & 105673. NOT char-0, NOT a
polynomial Keller map -- explicitly INTERNAL/UNREVIEWED/MOD-p.
- The fully graph-preserving family (218 nonredundant rows = 34 parked + 95 old
  graph bands 6-24 [the D21/D23/D25 reconstruction dropped by the prior
  overapproximation] + 89 late graph bands 26-42, in 184 vars) is NONEMPTY at
  both primes. Explicit 184-coordinate witness per prime satisfies all 218
  generators AND the independent full survivor gate (184/184 pristine residuals
  zero, s9_nu_ge_43 PASS, 18/18 floor checks; negative control tf1_57+=1 breaks
  18 rows). Method: exact 101-var slices only (no full-file msolve), decoded
  points replay all 184 graph rows.
- CORRECTION to the 2026-08-23 ~08:35 D43 note: the earlier "94 nonzero old
  coefficients" was a WITNESS-FAILURE count, not a missing-generator census; the
  properly reconstructed system imposes all 95 old-graph rows and is NONEMPTY.
- CONSEQUENCE: NO first depth kill. The fixed-B=84 residue-A carrier SURVIVES
  through depth 43. Floor ell+ >= 37 unchanged (window lower bound; e_plus still
  E_PLUS_CANDIDATE / certified=null; D75 = first Newton-cert depth). This is a
  live A-SCALE/carrier signal, but tests only FIXED B=84 depth -- it does NOT
  disprove A-SCALE (unbounded B), lift to char-0, or algebraize. Grok review
  pending. The A-SCALE resolution now hinges on the ALGEBRAIZATION gate, not on
  more fixed-scale depth.

## D43-FULL NONEMPTY: GROK-CONFIRMED + ALGEBRAIZATION GATE MAPPED (2026-08-23)
- grok-d43full-review.md CONFIRMS the 2026-08-23 D43-full entry: Completeness
  COMPLETE (10.8 omitted class present; no second overapproximation), Witness
  SOUND (independent replay both primes, 184/184+34/34 rows vanish incl. 10
  out-of-slice band-42 rows, floor_gate 18/18 byte-equal), Scope HONEST.
  Tier upgrade: MOD-p result is now DUAL-CONFIRMED. Scoped caveats (not holes):
  witness is the CELL ORIGIN (FREE=0), so the separate §10.7 fact "0/42 completed
  D25 points prolong at rung 26" stands (NONEMPTY != every point prolongs); 9
  band-10 rows degenerate to identities at the origin; old-graph hash audit is
  weaker than the late-graph byte regression.
- sol-lift.md maps the algebraization gate (mod-p -> char-0 -> polynomial Keller)
  as 8 stages: stage 0 (mod-p witness) DONE; stage 2 (char-0 point) settled by
  relative-smoothness/Hensel (KNOWN THEOREM) once a common integral model exists;
  stages 3-8 (inverse-limit survival, convergence/algebraicity, global gluing,
  polynomial+J=const, unbounded scale) all OPEN, stage 7 HARDEST. VERDICT: no
  known obstruction AND no known construction -- the carrier is modularly viable,
  not demonstrably algebraizable. Two primes+CRT do NOT give char-0; one Z_p-point
  does. Candidate obstructions (GCT-A/K2C/A-CONDUCTOR) all conjectural.
- NEXT (bounded, decisive): char-0 lift of the B=84 witness (relative smoothness
  => Hensel). Launched as sol-clift. B=168 scale test + reorg held for DC.

## D43 CHAR-0 LIFT SCREEN: p^2 PASSES, STAGE 2 OPEN (2026-08-23)
xmodel/sol-clift.md; cases/d43_char0_lift.py + d43_char0_lift_p105337.json.
- EXACT POSITIVE: coefficient radicals (r3, zeta42, A1, A2, h) Hensel-lifted to
  Z/p^2 (all defining residuals zero); the pristine 184-row Euler source system
  has rank J = 129 = rank[J | -F/p] and an explicit 24-coordinate correction
  replays 184/184 rows zero mod p^2 (direct reevaluation, not linear
  prediction). NO first-order local obstruction to lifting the D43 witness.
- EXACT: full special-fiber Jacobian rank of the 218-row system at the witness
  is 131 (tangent dim 53), with a certified unit 131x131 minor (det=810 mod p).
- NOT OBTAINED: common integral 218-row model (the d43red band .pkl checkpoints
  are ABSENT locally -- artifact-recovery item, likely box01), all-218 integral
  p^2 replay, local Krull dimension (Singular std capped 10 CPU-min), localized
  generation, p-flatness => the unit minor is NOT a standard-smooth certificate;
  Stacks 02H6 not invocable. X_43(C) != empty REMAINS OPEN.
- VERDICT: STAGE 2 OPEN -- no local obstruction found, no Hensel certificate.
  Next concrete item: recover/re-derive the band checkpoints to build the
  common integral model, then the dimension/flatness certificate.

## D43 MODULAR SOURCE/NF FIDELITY REVIEWED WITH SCOPED GAP; STAGE 2 OPEN (2026-08-23/24)
xmodel/sol-d43int.md (producer) and xmodel/review-d43-nf-fid-grok.md
(different-model hostile review: **CONFIRMED WITH GAPS**).
- EXACT, DUAL-MODEL CONFIRMED: the fully reconstructed modular presentation has
  184 variables and 218 rows = 34 parked + 95 old graph + 89 late graph rows at
  both primes; the row/eta census, checkpoint schema/prime/band/fiber, and all
  recorded canonical hashes replay. The 34 parked rows are the prime-specific
  D25 `.ms` files; the checkpoint payloads contain no integral or trace data.
- PRODUCER-FULL + INDEPENDENT SPANNING CORROBORATION at p=105337: the producer
  replay reconstructs all 184 checkpoint rows coefficient-by-coefficient as
  `R_raw = R_NF + sum Q_j G_j` (24.9M raw / 38.9M NF / 102.9M quotient-trace
  terms), dictionary-exact against the checkpoints. Grok independently parsed
  the 509 reducers and rebuilt tuple grevlex division on 2,355 groups across 62
  rows, including every group through band 14 and a row at every later band;
  zero mismatches. It also checked a bijection and origin evaluation on all
  382,824 groups. The remaining 122 fat-row dictionary remainders and the full
  producer replay were not regenerated, so this clause is corroborated rather
  than fully dual-recomputed.
- SCOPE CORRECTION: this establishes that the **checkpoint NF rows** are the
  stated modular source reductions. At band 42 the final `rung_kernel` assembly
  adjoins the `Xf_alpha`/`Xg_beta` P4P1 correction; those names are absent from
  the checkpoints and the 184 source-to-NF traces. Thus “all assembled graph
  polynomials are covered by those checkpoint traces” would overstate the
  reviewed result. The separately hashed modular assembly/census still passes,
  and the source-honesty gate below now accounts for the sidecar explicitly.
- Bandwise local-normal-form engine (nested pivots + product criterion, no std):
  localized generation on the fixed parked fiber PASSES through band 32; band 34
  is a 300s timeout (not a nonzero remainder). The 9 band-10 origin identities
  are locally generated by earlier pivots (not a hidden quadratic cut).
- STILL OPEN (stage 2): common integral presentation (the D23 reducer basis and
  parked rows exist only as prime-specific modular objects), all-218 p^2 replay,
  local dimension 53, generation by the 131 unit-minor equations, p-flatness,
  any Z_p / char-0 point. The reviewed source-defined D25-to-D27 one-band
  signal below makes its full-cell compatibility locus the next discriminator.
  Decide that locus before integral D43 engineering; only a separately reviewed
  coherent stratum could license re-emission over the radical number ring with
  reducer-to-parked traces and non-origin local membership.

## D43 BAND-42 P4P1 SIDECAR IS SOURCE-DERIVED AND ORIGIN-ONLY (2026-08-24)
xmodel/round2-p4p1-honesty-20260824.md and
cases/round2_p4p1_honesty/ (exact producer plus independent replay), with
xmodel/review-p4p1-honesty-grok.md (different-model hostile review:
**CONFIRMED; exact-source / MOD-p compiler-interface tier**).
- EXACT SOURCE IDENTITY: the sidecar correction is
  `42*S_M*G_M*(3*alpha-2*beta)*p(eta)^4*p'(eta)`. A direct four-term Euler
  expansion and an independent factored-product derivation agree before
  specialization; the actual `rung_kernel` subtraction matches all ten rows.
- EXACT BASE-IDEAL STATUS: neither checkpoint contains `Xf_alpha` or
  `Xg_beta`. At both registered primes, all twenty sidecar coefficients are
  nonzero constants and hence remain unchanged under the registered
  509-element `I23` Groebner bases. The correction is not zero modulo the base
  ideal and is load-bearing away from its sidecar zero line.
- VERDICT `ORIGIN-ONLY`: at the named completion `alpha=beta=0`, used by the
  modular origin witness, the correction vanishes; at the fixed control
  `(alpha,beta)=(1,0)` it changes all ten rows. Therefore no wrong mathematics
  invalidates that origin witness. The defect was the provenance/scope slogan:
  checkpoint source traces do not themselves cover the later sidecar.
- REVIEW HARDENING: the hostile reviewer independently derived the identity,
  executed the live `rung_kernel` assembler on empty input and all ten real
  checkpoint rows at both primes, and recomputed every exact `I23` normal form.
  The sidecar-zero locus is the line `3*alpha-2*beta=0`; nonzero graph
  reconstruction witnesses away from that line are outside this origin gate.
- CLEAN WORDING: “checkpoint rows are source-to-NF traced modulo `I23`; final
  assembly adjoins the displayed exact source-derived sidecar, which vanishes
  at the named origin.” No integral emitter, general D43 nonemptiness,
  compatible tail, germ, characteristic-zero point, or JC2 inference follows.

## D25-TO-D27 SOURCE TRANSITION: ONE-BAND FREE-TAIL SIGNAL (2026-08-24)
xmodel/round1-dtransition-20260824.md and
cases/round1_dtransition/ (producer), with
xmodel/review-dtransition-grok.md (different-model hostile review:
**CONFIRMED**).
- SCOPE: exact modular arithmetic at `p=105337,105673`, fiber `a00pp`, one
  chart, four named points, and band 26 only. The unreduced recurrence gives a
  typed projection `X27 -> X25`, adding exactly ten band-26 rows and ten
  first-occurrence coordinates without changing a lower row. It imports no
  D43 or `D43-NF-FID` artifact.
- POSITIVE POINTWISE SIGNAL: at each of two named witnesses,
  `rank(A)=rank([A|b])=4`; the affine fiber has dimension six, and all twelve
  displayed kernel lifts (six at each prime) replay through the unreduced
  source recurrence to band 26.
- NEGATIVE POINTWISE SIGNAL: at each of two deterministic interior points,
  `rank(A)=4` but `rank([A|b])=5`; exact left-cokernel pairings are nonzero, so
  those points do not prolong through this band.
- VERDICT `FREE-TAIL-SIGNAL`: compatible one-band fibers exist over the two
  witnesses while other D25 points are cut. The same lifted directions leave
  nonzero residuals at bands 30, 36, and 40. Therefore this proves no
  component, dominance, full-cell rank statement, band-28 persistence,
  compatible inverse system, formal germ, characteristic-zero point, or
  polynomial Keller map. The registered next gate is the source-defined
  compatibility locus on one full promoted D25 cell, stopping before band 28.

## D25 CELL-0 BAND-26 COMPATIBILITY LOCUS IS NONEMPTY, RANK AT LEAST FIVE (2026-08-24)
cases/round1_dtransition_fullcell/ and
xmodel/round1-dtransition-fullcell-20260824.md (producer), with
xmodel/review-dtransition-fullcell-grok.md (different-model hostile review:
**CONFIRMED**).
- SCOPE: `p=105337`, fiber `a00pp`, promoted cell-0 `A^14`, fixed
  `(W1,W2)=(31931,9457)`, and the source-defined band-26 compatibility problem
  only. The six functions are the canonical left-cokernel contractions of the
  unreduced ten-row source block after exact D25 and band-24 triangular
  pullback. No D43 artifact enters.
- NONEMPTY + LOWER RANK BOUND: the cell origin is a certified common zero. Its
  exact `6 x 14` Jacobian has rank five, witnessed by a nonzero `5 x 5` minor
  of determinant 39793. Hence the compatibility locus on this modular cell is
  nonempty and the generic differential rank is at least five. The
  preregistered rank-six-at-origin gate failed.
- MIXED FULL-CELL BEHAVIOR: the deterministic same-cell point with free
  coordinates `1,...,14` is cut by compatibility; its function vector is
  `(23070,55420,82249,287,11111,1237)` and its Jacobian again has rank five,
  with displayed minor 104469. Thus the pointwise witness/interior split was
  not merely a comparison between different cells.
- SOURCE/TANGENT CHECK: the full reconstruction and a scratch rerun are
  byte-identical. Independent differentiation confirms the cell, 86-row
  D21/Row-22, prefix, and band-24 frontier chains. The shared-prefix derivative
  is `1-C_k`; replacing it by `-C_k` changes the origin minor and makes the
  sequence-point frontier tangent inconsistent at `x68=uf18`.
- OPEN UPPER BOUND: the constant row vector
  `(104372,48519,44983,31248,84848,1)` annihilates function values and
  Jacobians at the two registered points and four hostile extra probes, but no
  global polynomial-identity certificate was obtained. Do not infer generic
  rank exactly five, dimension, reducedness, or component structure.
- NO DESCENT INFERENCE: nothing here proves a non-origin compatible rank-six
  point, band-28 persistence, a compatible inverse system, formal germ,
  characteristic-zero point, algebraization, polynomial Keller map, or JC2
  counterexample. The licensed provisional continuation was the separate
  source-stationarity gate, not another depth computation; it has since
  returned producer/replay `NO-TYPED-STATIONARITY` because the current full
  source does not classify its first x-side directions. The following entry
  records its separate hostile confirmation.

## D SIX-BAND PURE-Y LAW CONFIRMED; FULL SOURCE NOT TYPED (2026-08-24)
xmodel/round2-dstate-gate-20260824.md and cases/round2_dstate_gate/
(exact producer plus independent replay), with
xmodel/review-dstate-grok.md (different-model hostile review:
**CONFIRMED**).
- POSITIVE SCOPED RESULT: at the two registered modular D25 witnesses, the
  unreduced pure-`y` source through band 40 has the corrected 30-input /
  30-output six-band state, including `H_29` at start 36. The shifted
  first-occurrence layers at bands 26, 32, and 38 are exact `10 x 10` types;
  their truncation squares commute coefficientwise, dual and grouped source
  derivatives agree, and `M_38-2*M_32+M_26=0` after six-shift relabeling.
- FIRST FULL-SOURCE INTERFACE: independently,
  `[t^42]E_full=[t^42]E_y+42*S_M*G_M*(3*alpha_1-2*beta_1)*p(eta)^4*p'(eta)`.
  Both partials are nonzero over `Q` and at both registered primes.
- VERDICT `NO-TYPED-STATIONARITY`: the current constructor has no x-side
  argument; its 30 streams contain neither `alpha_1` nor `beta_1`; and no
  source-derived held/derived/independent classification, chain rule,
  six-shift relabeling, or projection map for them is banked. Choosing one
  would invent the state map.
- NOT SHOWN: the three-layer affine check is not an all-depth stationarity
  theorem. No finite full-source state, Ore/Spencer/Fitting or syzygy object,
  band-28 persistence, D43 result, inverse system, germ, characteristic-zero
  point, algebraization, polynomial Keller map, or JC2 inference follows.
  The frozen `UNBOUNDED-STATE` label is not implemented as a producer branch;
  future reuse must close that driver-completeness gap. It does not alter this
  verdict because the omitted factor directions form a finite but untyped list.
- FROZEN-SOURCE DOCUMENTATION CAVEAT: the header of `cases/valuation_e2.py`
  still narrates the earlier 29-output candidate (`E_29=0`, start sum 240),
  although the same file later records its refutation. The source byte is
  preserved because several manifests pin it. This confirmed entry supersedes
  that header for live state: include `H_29` at start 36, giving 30 outputs and
  start sum 276; the legacy tool's 29-output diagnostic remains historical.

## EXACT-COFRAME PRIORITY + FIXED BROUGHTON/COHN NO-GO (2026-08-24, DUAL-CONFIRMED)
`xmodel/exact-coframe-gate-20260824.md` and
`cases/exact_coframe_gate_20260824/` (exact producer/replay), with
`xmodel/exact-coframe-gate-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**) and the citation-preserving
`xmodel/exact-coframe-gate-20260824-erratum.md`.
- CLASSICAL ONE-WAY CERTIFICATE: if both rows of
  `M in SL_2(C[x,y])` are closed, polynomial integration gives
  `M=J(P,Q)`. Jung--van der Kulk plus the chain rule puts the determinant-one
  Jacobian of every plane automorphism in `E_2(C[x,y])`. Literal
  `M notin E_2` therefore gives a characteristic-zero plane Keller
  nonautomorphism. This uses no quotient `SL_2/E_2` and no normality claim.
- PRIORITY CORRECTION: the bridge/reformulation is not campaign-new. Wright's
  1978 weak Jacobian theorem supplies the converse for a **full** Jacobian in
  `GE_2`; its exact Theorem 6/page-250 wording is frozen from primary-research
  restatements because the original Elsevier body was inaccessible. The
  canonical DOI is `10.1016/0022-4049(87)90004-1` despite the 1978 year.
- COHN LINEAGE: the standard Cohn matrix is non-elementary by Cohn Proposition
  7.3 and Park's leading-row certificate. Entry substitution `y -> 2y`
  preserves nonmembership and gives
  `C_B=[[1+2xy,x^2],[-4y^2,1-2xy]]`; its first row is
  `d(x+x^2y)`. The frozen report's reference to Cohn section 8 is corrected to
  the end of section 7. The retrieved arXiv:2412.03688 artifact is v1,
  2024-12-04; an unsupported 2026 manuscript date is withdrawn.
- SCOPED NEW NEGATIVE: every determinant-one polynomial completion of the
  fixed first row is uniquely `L(h)C_B`. Its second row is closed exactly when
  `(1+2xy)h_y-x^2h_x=6y`. On the preregistered three-term support the exact
  linear map has rank 3 and augmented rank 4, with an explicit unit
  certificate. Globally, the weight recurrence forces
  `c_n=(-1)^n(n+3)` and an uncancelled terminal term for every finite
  polynomial. The rational/formal control
  `h=y^2(3+2xy)/(1+xy)^2` has precisely the nonterminating series.
- SOURCE HAZARD: Shpilrain--Yu Proposition 2.4's printed claim that an
  arbitrary second row beneath a gradient first row in `GE_2` must itself be
  a gradient is false as printed: `L(y)` is elementary, has first row `dx`,
  and has non-closed second row `(y,1)`. Wright assumes a full Jacobian; this
  stronger assertion is not imported.
- SCOPE: this closes only the complete fixed-first-row / one-left-shear
  Broughton/Cohn family. It does not close `E_2 C E_2` with a changed first
  row, produce a Keller pair, or prove/disprove JC2. No second shear, support
  widening, or generic sparse search is licensed by this result.

## NORMALIZATION RANK-TWO NO-GO (2026-08-24, KNOWN-THEOREM/REDERIVATION TIER)
`xmodel/completion-pair-gate-20260824.md` (self-contained producer proof), with
`xmodel/completion-pair-rank2-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- PROMOTED AT KNOWN-THEOREM/REDERIVATION TIER: a complex plane Keller map
  cannot have function-field degree two. For
  `A=C[P,Q]`, `B=C[x,y]`, and the normalization `R` of `A` in `Frac(B)`,
  Zariski Main embeds `Spec B` as an open in `Spec R`. Rank two, trace
  splitting, and `Pic(A)=0` give
  `R=A+Az ~= A[z]/(z^2-h)` with `Tr(z)=0` and
  `Omega_(R/A)=(R/(2z))dz`. Keller etaleness on the open chart makes `z` a
  unit of `B`; since `B^*=C^*`, scalar trace forces `z=0`, a contradiction.
  Equivalently, every squarefree branch factor gives the forbidden principal
  boundary relation `div_X(q_i)=2E_i`.
- WORDING CAVEAT: `j(U)=X` gives finiteness; concluding automorphy in general
  also invokes triviality of connected finite etale covers of `A^2_C`. The
  rank-two unit/trace contradiction itself does not need that extra sentence.
- KNOWNNESS: quadratic extensions are Galois, so this statement follows from
  the classical Galois case (Campbell/Razar/Wright/Bass--Connell--Wright).
  Orevkov, *On three-sheeted polynomial mappings of C^2*, Theorem 1.1, defines
  multiplicity as generic fibre cardinality and proves that a complex plane
  Keller map has multiplicity neither two nor three. Thus a rank-three
  continuation is also known-closed; this says nothing about polynomial total
  degree three.
- GLOBAL LOW-SHEET CHECKSUM: the preceding producer proof itself stops at
  rank two, but **generic mapping/topological degree four is not open**.
  Domrina, *On four-sheeted
  polynomial mappings of C^2. II. The general case*, Izv. Math. 64:1 (2000),
  1--33, proves that no four-sheeted complex plane polynomial map has nonzero
  constant Jacobian (MathNet `im273`). Żołądek, *An application of
  Newton--Puiseux charts to the Jacobian problem*, Topology 47 (2008),
  Theorem 6.12, proves invertibility for topological degree at most five.
  Hence the first open mapping/topological degree is six, consistently with
  `ladder/SHEET6.md`. The round-0719 packet's global reading of “ranks at
  least four untouched” was a priority error and licensed no quartic replay.
- SCOPE: this rank-two gate is not a new theorem, a finiteness proof in
  arbitrary rank, or a JC2 result. Its local proof does not rederive the
  separate known rank-four/five theorems.

## WEIGHTED D LEVEL-TWO SOURCE GATE (2026-08-24, DUAL-CONFIRMED SOURCE-TYPING TIER)
`xmodel/weighted-d-source-gate-20260824.md` and
`cases/weighted_d_source_gate_20260824/` (exact producer/replay), with
`xmodel/weighted-d-source-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- FROZEN-PERIMETER VERDICT: at basis
  `dd11599b07eb05591b5c006791005eef19457d8e`, all 25 registered source hashes
  match, but no promoted producer supplies a named normalized full-polynomial
  source completion and typed tangent maps through
  `alpha_1,beta_1,alpha_2,beta_2`. P4P1 symbols are external compiler
  variables; `eplus43` is an unreviewed zero/independence constructor choice
  and stops before factor level two.
- EXACT AMBIENT ALGEBRA: the coordinate change through `q^2=t^84`, the
  unreduced identity
  `B_full=R^2 C^5 B+R C^5(theta R)A+R^2 C^4(theta C)D`, and every displayed
  level-42/84 chain-rule term independently replay. Level 84 contains the old
  carrier `c_1`; `c_2` drops out only because `B_0=D_0=0`.
- PROMOTED STOP: `NO-TYPED-SOURCE/NO-QUOTIENT` means that no quotient test is
  presently licensed, not that a mathematical quotient is nonexistent. The
  free formal span is an acceptance target, not `T_src`; it cannot certify
  `TWO-DRIVER`, a Hankel pivot, a recurrence, or a state dimension.
- RESURRECTION: require one producer artifact reconstructing the first two
  factor levels from `phi_f,phi_g` (or an exact R2/h-Newton model), with the
  named point, stable source labels, tangent maps, relations, and full chain
  rule. Another external sidecar or modular D row is not enough.
- SCOPE: no band 28/deeper D, D43 integral, syzygy/Spencer/Fitting, germ,
  characteristic-zero point, polynomial Keller map, or JC2 inference follows.

## HAMILTONIAN KAPPA CLASS + `x+x^n y` FAMILY NO-MATE (2026-08-24, DUAL-CONFIRMED SCOPED TIER)
`xmodel/hamiltonian-kappa-gate-20260824.md` and
`cases/hamiltonian_kappa_20260824/` (exact producer/replay), with
`xmodel/hamiltonian-kappa-review-grok-20260824.md` (different-model hostile
review: **CONFIRMED**).
- EXACT CLASS: for a polynomial `P` with unimodular gradient, choose a
  polynomial vector field `V(P)=1` and put
  `kappa(P)=[div V] in C[x,y]/D_P(C[x,y])`.  The syzygy module of
  `(P_x,P_y)` makes this independent of `V`.  Subtracting `hD_P` and applying
  the polynomial Poincare lemma proves
  `kappa(P)=0` iff some polynomial `Q` satisfies `[P,Q]=1`, with all signs
  independently checked.
- PRIORITY: Friedland 2001 already defines this cokernel and its
  Gauss--Manin operator, whose value at one is `kappa(P)`.  Dimca--Saito type
  the same element as `partial_t[dx wedge dy]` in the Brieskorn module.  No
  primary source or gate result supplies a finite universal receiver forcing
  this class to be nonzero for every noncoordinate.
- SCOPED FAMILY THEOREM: for every integer `n>=2`,
  `P_n=x+x^n y` has unimodular gradient.  The weight
  `w(i,j)=i-(n-1)j` exhausts all monomials that could contribute to
  `[P_n,Q]=1`; coefficient recursion gives a nonzero infinite chain and an
  uncancelled terminal term for every finite polynomial.  Hence no polynomial
  mate exists.  The replay passed 4,979 exact checks and the rational/formal
  slice is correctly nonpolynomial.
- SCOPE: this is a controlled infinite-family theorem whose members are not
  Keller coordinates; literature novelty is not claimed.  The class is an
  exact reformulation of the missing mate, not a new global obstruction.  No
  generic sparse widening, universal receiver, proof, or counterexample to
  JC2 follows.

## DUAL-PENCIL INFINITY DEFECT IS JUMP-ONLY, NOT THE PROPOSED DIVISOR (2026-08-24, DUAL-CONFIRMED DEFINITION STOP)
`xmodel/dual-pencil-definition-gate-20260824.md` (corrected producer), with
`xmodel/dual-pencil-hostile-audit-20260824.md` (internal hostile source audit:
**PASS WITH SCOPED CORRECTION**) and
`xmodel/dual-pencil-review-grok-20260824.md` (different-model review:
**CONFIRMED**).
- EXACT CORE: for a Keller pair and every nonzero direction
  `H=aP+bQ`, `H` is a polynomial submersion.  Suzuki's primitive
  factorization gives connected generic fiber and total infinity defect
  `delta(H)=1-chi(G_H)=b_1(G_H)>=0`.
- ENDPOINT: `delta(H)=0` makes the generic fiber `A^1`; the resulting
  coordinate direction, together with its Keller mate, makes the original
  pair an automorphism.  Thus any hypothetical nonautomorphic Keller pair has
  positive defect in every pencil direction.
- TYPE VERDICT: the universal defect therefore has horizontal support over
  the whole dual line, not a finite effective divisor.  Subtracting the
  generic value leaves only a jump cycle and destroys the proposed
  degree-zero endpoint.  At constant polynomial degree, Siersma--Tibar
  Proposition 5.1 gives a nonpositive jump coefficient; at the possible
  degree-drop direction the coefficient remains uncontrolled.  This corrects
  the producer's original sign assertion without changing
  `PRIOR-ART / JUMP-ONLY / TYPE-FAIL`.
- SCOPE: the signed jump cycle is a resolution-independent finite formal
  cycle, but no finite **effective** divisor with the proposed degree-zero
  endpoint, GRR formula, new positivity obstruction, or JC2 result follows.
  No dual-pencil descendant is licensed without a genuinely new typed object.

## AS109 SUPPORT GRAMMAR STOP + CARRY CORRECTION (2026-08-24, DUAL-CONFIRMED CORRECTED SPECIFICATION TIER)
`xmodel/as109-support-gate-20260824.md` and
`cases/as109_support_20260824/` (frozen specification and exact controls),
with `xmodel/as109-support-review-grok-20260824.md`, the frozen
`xmodel/as109-support-gate-20260824-erratum.md`, and
`xmodel/as109-carry-erratum-review-grok-20260824.md` (different-model
follow-up: **CONFIRMED**).
- REGISTERED STOP: a cap of eight correction slots does not bound literal
  exponents.  For every `m>=1`, the exact triangular automorphism
  `G_m=(x+109y^m,y)` gives a two-slot first layer and a five-slot two-layer
  union after exact successor transport; its exponents remain unbounded.
  Nonlinear residual support
  changes along the exact source-gauge orbit, so no finite exhaustive graph
  exists without a proved gauge section or groupoid transition rule.  No
  enumerator or AWS job ran; no cap-eight existence or nonexistence statement
  follows.
- CARRY ERRATUM: for integral digit lifts, put
  `C_1=L(A_0,B_0)-x^108` and `K=C_1/109` after the first congruence.  The
  correct second digit is
  `K+L(A_1,B_1)+N_0=0 mod 109`; marked-section equations have analogous
  evaluation carries.  A five-slot countercontrol passes the frozen
  uncarried `E1/E2` but has
  `det J-1=109^2*x^108 mod 109^3`.  This supersedes claim 2 of the original
  review only at the inference from the correct determinant expansion to an
  uncarried generic second digit.
- SURVIVING OBSTRUCTION: the parametric triangular family has `C_1=0` and
  its successor equation over `Z`, so its carry is identically zero.  Hence
  `NO-FROZEN-GRAMMAR`, the unbounded-support witness, and the stopped scope
  survive the correction exactly.
- CONDITIONAL HENSEL BRIDGE: any exact polynomial
  `F in Z_109[x,y]^2` reducing to `(x-x^109,y)` with `det J_F=1` has the
  following property: for each fixed residue `b`, the 109 source balls
  `(a,b)+109Z_109^2`, indexed by `a`, each map bijectively onto the target
  ball `(0,b)+109Z_109^2`.  It is therefore noninjective over `Q_109`;
  adjoining finitely many
  coefficients and two preimages gives a finitely generated characteristic-
  zero field that embeds in `C`, hence a complex Keller counterexample.  This
  assumes an exact lift and does not assert one exists.
- CONDITIONAL CONTRACTION: let `U'` be a finite free gauge-fixed coefficient
  module and `W` a finite residual module with
  `x^108 in W`, `L(U') subset W`, and `N(U') subset W`.  An integral right
  inverse `R:W->U'` whose image is the chosen section makes
  `T(u)=R(x^108-109N(u))` a strict contraction.  `CLOSED-SUPPORT + UNIT-L`
  would therefore construct the exact lift needed above.  No known support
  meets these hypotheses.
- SCOPE: this is a corrected specification stop plus two conditional
  resurrection lemmas.  There is no `HEIGHT-CERT`, `NO-CYCLE-AT-8`, found
  lift, characteristic-zero inference, proof, or counterexample to JC2.

## D73 DIRECTION-COLLISION STRICTNESS HAS AN EXACT EQUALITY CONTROL (2026-08-24, DUAL-CONFIRMED LOCAL TIER)
`xmodel/d73-strict-or-equality-20260824.md` (producer), with
`xmodel/d73-strict-or-equality-review-grok-20260824.md` (different-model
hostile review: **CONFIRMED**).
- EXACT LOCAL GERM: in the infinity chart `s=y^-1`, `t=xy^4`, put
  `q=t+t^25`, `g=q(t)`, and
  `f=t^15+s^3/(3q'(t))`.  Both `dx wedge dy` and `df wedge dg` equal
  `s^2 ds wedge dt`, so the analytic germ has Jacobian one exactly.  Its
  height-four data match sharp SP-2:
  `(k_f,l_f)=(60,15)`, `(k_g,l_g)=(100,25)`, `pi(G)=4`, `kappa_G=1`, and
  direction multiplicity 15.
- EQUALITY: on `f=0`, a holomorphic unit change gives `S^3=t^15`.  There are
  exactly three normalized branches, each with `y`-pole order five, first
  contact `21/5`, and `Lambda=1`.  Hence the collided direction has
  `sum Lambda=3=pi(G)-1`, attaining Proposition 7.3's lower bound despite
  multiplicity greater than one.
- GENERIC-FIBER TYPE CHECK: for small generic `a`, the fifteen simple roots
  of `t^15=a` lie in one local neighborhood, but their values
  `q(t_i)` are pairwise distinct.  Each puncture has local multiplicity three
  while the cover over any one target value has degree three.  Adding all
  fifteen multiplicities would illegally mix fifteen different `g`-fibers.
- SOURCE WORDING: Sigray Proposition 7.3 says equality holds **if** the
  direction root is simple; it states no converse.  The two former
  `iff mult=1` readings in `ladder/SHEET6-LROOT.md` are corrected to the
  one-way statement.  Direction multiplicity alone therefore cannot force
  the hoped-for strict extra delta unit.
- SCOPE: `f` is rational/analytic, not a global polynomial in `(x,y)`.  This
  is a local equality control, not a Keller counterexample, a realization or
  kill of any of the eight terminal classes, or a global equality theorem.
  The remaining implication must use global polynomial realizability,
  opposite-side compatibility, or an additional branch elsewhere on the
  same compactified fiber.  No proof or counterexample to JC2 follows.
- REVIEW METADATA: some Grok reports across this and successor batches contain
  inaccurate human-written review windows. The authoritative automatic runner
  times and frozen hashes are recorded in the immutable
  `xmodel/review-window-erratum-20260824.md` and its cumulative `-v2`
  successor; no mathematical verdict changes.

## AS109 INDEPENDENT-SLOT + QUADRATIC-Y NO-GOS (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-closed-support-gate-20260824.md` and
`xmodel/as109-quadratic-coupling-gate-20260824.md`, with hostile
different-model reviews `xmodel/as109-natural-nogo-review-grok-20260824.md`
and `xmodel/as109-quadratic-review-grok-20260824.md`: **CONFIRMED**.

- INDEPENDENT-SLOT THEOREM: report/review SHA-256 are
  `b3fa62651673db06b89fb6ad8217ebc2a61bacd5940b7a08501a1f3a47a7d717` /
  `3b0d369c678a518614be0218c434eec97c43af0747aa8a26906256e12d2b13d5`.
  In a full independently variable literal-slot module, a unit right inverse
  at `x^108` forces `(0,x^108 y)`. Nonlinear closure and polarization then
  force every `x^(108k)` into the finite residual module, a contradiction.
  This excludes the raw independent-slot certificate, not genuinely coupled
  modules or arbitrary fixed support.
- QUADRATIC FIELD THEOREM: report/review SHA-256 are
  `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` /
  `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2`.
  Over every characteristic-zero field, a Keller pair whose two coordinates
  have `y`-degree at most two is a polynomial automorphism. The cubic
  Jacobian coefficient makes quadratic tops proportional; a target `GL_2`
  operation makes one coordinate affine; the mixed coefficient gives
  `b_2=k a_1^2`; a polynomial target shear removes it; the affine pair has an
  explicit triangular inverse. No algebraic closure, source substitution, or
  nonconstant denominator is used.
- AS109 CONSEQUENCE: an exact lift with both correction `y`-degrees at most
  two would be an automorphism over `Q_109`, contradicting the already
  reviewed 109-ball Hensel noninjectivity. Thus a surviving lift needs
  essential coefficient coupling and, at this tier, `y`-degree at least
  three in one correction. No lift, arbitrary-support no-go, or JC2 inference
  follows.

## TD6 CENTERING ESCAPE + FINITE-JET CONTROL (2026-08-24, DUAL-CONFIRMED STOP TIER)

`xmodel/td6-global-compatibility-gate-20260824.md` (producer SHA-256
`b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17`)
with `xmodel/td6-global-compatibility-review-grok-20260824.md` (review
SHA-256
`f3e468f415fdd7bd1aa85962090d34a55bf6ff15d469c28373347cf1c7cc42ac`):
**CONFIRMED `CENTERING-ESCAPE / FINITE-JET-CONTROL / STOP`**.

- BARE LEMMA: in the zero-centered chart `x=t s^R`, `y=s^-1`, every positive
  `s^k` coefficient of a polynomial holomorphic there is divisible by
  `t^ceil(k/R)`. If both members of a Keller pair were holomorphic in that
  same chart, the Jacobian would vanish at `t=0`, an exact contradiction.
- CENTERING ESCAPE: LR2 does not force the shared lower truncation to zero.
  The legal choice `x=s+t s^4`, `y=s^-1` has the polynomial Eggers coordinate
  `T=xy^4-y^3=t`, so the bare divisibility inference is not available.
- GLOBAL POLYNOMIAL CONTROLS: explicit pairs inside the fixed SP-2 rectangles
  reproduce its height-four patterns and three-branch
  `sum Lambda=3` mechanism. Their centered Jacobian errors have exact orders
  three and six. Neither pair is Keller. A characteristic-zero Bezout
  recursion in `Q[T][[x]]` constructs arbitrary finite one-sided Keller jets
  only after dropping the degree cap; degrees grow and no convergence,
  algebraization, or opposite-chart statement follows.
- NEXT GATE: fixed `Q[x,y]` rectangles, explicit common-centering
  coefficients, the opposite r9/M2 chart, and exact global `J=1` must be
  imposed together. No terminal class is killed or realized. The two
  LaTeX-only producer slips are frozen in
  `xmodel/td6-global-compatibility-format-erratum-20260824.md`; code and math
  are unchanged.

## SECANT IDEMPOTENT REMOVES COLLISION SATURATION (2026-08-24, DUAL-CONFIRMED ACCELERATOR TIER)

`xmodel/fresh-connection-gate-20260824.md` (producer SHA-256
`666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`)
with `xmodel/secant-idempotent-review-grok-20260824.md` (review SHA-256
`6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`):
**CONFIRMED**.

For `I=(F(x,y)-F(u,v))`, diagonal ideal `Delta=(x-u,y-v)`, constant
Jacobian `c`, and any polynomial secant matrix `A`, put
`e=c^-1 det A` in `C=S/I`. The adjugate gives `e Delta=0`; restriction to
the diagonal gives `1-e in Delta`; hence `e^2=e`, uniquely among elements
with those two properties. Moreover

```text
I:Delta = I:Delta^infinity = I+(det A)
```

as schemes, with `eC` the reduced diagonal quotient and `(1-e)C` the off
factor. Different secant conventions give the same class modulo `I`. This is
a substantial software simplification to one explicit third generator, but
making that ideal unit for all characteristic-zero Keller maps is exactly
injectivity/JC2. The identity is standard neighboring secant/Bezoutian and
collision-ideal algebra; no priority novelty is promoted.

## PROJECTIVE COLLISION CONNECTEDNESS IS COSTUME (2026-08-24, DUAL-CONFIRMED NEGATIVE TIER)

`xmodel/secant-projective-connectedness-gate-20260824.md` (producer SHA-256
`cabfa347efc22b90b1c4c0808ceb1e1ac0bce235d35e8e28d9f27cc6bc614fb2`)
with `xmodel/secant-projective-review-grok-20260824.md` (review SHA-256
`99b7649365a3fbae34932c2bacc03ad141507f74a6ca55d2945bc427e0404957`):
**CONFIRMED `COSTUME / NEED-Z-SATURATED-INFINITY-DATUM`**.

- The honest projective closure is cut out by `K:Z^infinity`, not the two
  naive homogenized difference equations `K`. A nontrivial tame automorphism
  gives an exact control: the naive complete intersection contains two whole
  infinity surfaces; saturation exponent four removes them and leaves only
  the diagonal, while the secant off ideal saturates to `(1)` at exponent
  three.
- Over `F_3`, the Artin--Schreier Keller collision has honest saturated
  diagonal/off components meeting scheme-theoretically on the doubled line
  `(X-U,Y-V,Z^2)`. Thus affine etaleness can move all contact to the boundary
  without contradiction.
- Consequently projective complete-intersection connectedness supplies no
  general obstruction and kills no named characteristic-zero family. A live
  descendant needs the source-derived saturated boundary-intersection cycle
  on a pinned compactification. No proof or counterexample follows.

## AS109 CUBIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-cubic-coupling-gate-20260824.md` (producer SHA-256
`198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820`)
with `xmodel/as109-cubic-review-grok-20260824.md` (review SHA-256
`2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef`):
**CONFIRMED**.

- FIELD THEOREM: every Keller pair over an arbitrary characteristic-zero
  field whose two coordinate `y`-degrees are at most three is a polynomial
  automorphism. Equal cubic tops reduce by constant target `GL_2`; an
  affine/cubic top reduces by `g-k f^3`; lower cases use the quadratic theorem.
- GENUINE `(2,3)` CASE: UFD valuations normalize the leading coefficients to
  `h^2,h^3`. A constant target addition aligns the two rational depression
  shifts and gives
  `f=z^2+U`, `g=z^3+Vz+W`, `z=hy+r`. The Jacobian equations are
  `V'=3U'/2`, `W'=0`, `hU'V=j`. Polynomial constant terms give the monic
  equation `r^3-(3D+2c)r+2(G-w)=0`; integral closure makes `r,U,V`
  polynomials. Their unit product then contradicts `V'=3U'/2`.
- DESCENT/SCOPE: automorphy descends from the algebraic closure by uniqueness
  or faithful flatness. No source coordinate change, support cap, `x`-degree
  bound, or finite-Witt inference is used. An exact AS109 lift with both
  correction `y`-degrees at most three would be an automorphism over `Q_109`
  and contradict Hensel noninjectivity. Thus a surviving lift needs
  `y`-degree at least four in one correction. No quartic theorem, lift,
  arbitrary-support no-go, novelty claim, or JC2 decision is promoted here.

## SECANT x AS109 IS LOCAL-RANK COSTUME (2026-08-24, DUAL-CONFIRMED NEGATIVE TIER)

`xmodel/secant-as109-cross-gate-20260824.md` (producer SHA-256
`f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`)
with `xmodel/secant-as109-review-grok-20260824.md` (review SHA-256
`16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029`):
**CONFIRMED `COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM`**.

- The seed collision algebra has `t=x-u`,
  `I_0=(t(1-t^108),y-v)`, `e_0=1-t^108`; its off factor is the product of
  108 copies of `F_109[u,y]`. The 108 CRT projectors and their Teichmuller
  lifts record the already-known Hensel collision sheets.
- On every off sector `x-u` is a unit and the adjugate identity gives
  `e=(x-u)^-1(a_22 f_1-a_12 f_2)`. Scheme-theoretically
  `(f_1,f_2,e)=(f_1,f_2)` after localization, and at a collision
  `de=(x-u)^-1(a_22 df_1-a_12 df_2)`. Thus a compiler that already includes
  matching-precision collision equations gains coefficient/tangent rank zero
  from the raw secant row, including its carried digit equations.
- Trace, norm, factor count, and derived support are ranks or consequences of
  the analytic split, not new bounded polynomial constraints. Resume only
  with an independently constructed finite normalization, bounded polynomial
  branch algebra, or global elimination datum that couples all 108 sectors
  and adds positive rank. No contradiction, finite constraint, lift, or JC2
  decision follows.

## AS109 QUARTIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/as109-quartic-discriminator-gate-20260824.md` (producer SHA-256
`8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`)
with `xmodel/as109-quartic-review-grok-20260824.md` (review SHA-256
`3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e`):
**CONFIRMED**.

- FIELD THEOREM: over every characteristic-zero field, a Keller pair whose
  two coordinate `y`-degrees are at most four is a polynomial automorphism.
  Equal/top-divisible cases reduce to the independently re-proved cubic base;
  the only new actual pair is `(3,4)`.
- GENUINE `(3,4)` CASE: after UFD normalization and aligned depression,
  `f=z^3+uz+v`, `g=z^4+az^2+bz+c`. The five coefficient rows are
  `4u'-3a'`, `4v'-3b'`, `2au'-3c'-ua'`,
  `bu'+2av'-ub'`, and `bv'-uc'`. They give
  `(4u/3+2alpha)v=delta` and the constant Jacobian row. Polynomial constant
  terms yield a degree-ten monic eliminant for the rational shift; integral
  closure makes all depressed coefficients polynomial, and every
  conserved-product branch then contradicts a nonzero constant Jacobian.
- AS109 CONSEQUENCE/SCOPE: no exact AS109 lift has both correction
  `y`-degrees at most four. A survivor needs `y`-degree at least five in one
  correction, with arbitrary `x`-degree and coefficient coupling still
  allowed. No quintic theorem, arbitrary-support no-go, lift, priority claim,
  or JC2 decision follows.

## TD6 TWO-CHART FIRST BAND AND NUMERICAL NEXT-ROW KILL (2026-08-24, DUAL-CONFIRMED FINITE TIER)

The first-band producer/review
`xmodel/td6-two-chart-first-band-20260824.md` /
`xmodel/td6-two-chart-first-band-review-grok-20260824.md` have SHA-256
`cb373892233bddaf1b8fbf7722335ca43ee366b337151c3b244d2604d8168bf2` /
`265c1103391e2bae889c018bb0637fe486e7292644c0295e4f9965e5085e7a25`.
The next-row producer/review
`xmodel/td6-two-chart-next-row-20260824.md` /
`xmodel/td6-two-chart-next-row-review-grok-20260824.md` have SHA-256
`32124d20ec84ef59d5b116639176b12053f5da6de1a9458dd4a2095d6b1618f0` /
`12834c356c2c26243522b2609753370118ecd2c8ed87907033ca27e926d2ac2f`.
Both hostile reviews are **CONFIRMED**.

- FIRST BAND: one licensed SP-2/r9-M2 specialization uses common centering
  `(1,1,1)`, the selected F1 orbit polynomial, zero dead stretch, and
  `A=1/9` in the unchanged `(15,60)/(25,100)` rectangles. One shared global
  coefficient system has exact rank `3508/3602`, nullity 94. Its deterministic
  rational witness satisfies all stated transport rows, `[s^-2]J=0`, and
  `[r^0]J=1`; it fails the next rows and is not Keller.
- NEXT ROW: exact affine parameterization of the entire 94-space freezes
  `f1=-384t^14/25`,
  `g1=-128/125-(128/5)t^24`, and
  `[t^13]f2=66927/625`. Hence every point satisfies
  `[s^-1 t^13]J=-18858/3125`, an exact `Q-EMPTY` certificate. The apparent
  quadratic next band collapses to affine-linear; the pole row is unnecessary
  for the contradiction.
- SCOPE: the first band is nonempty and the next band empty only for these
  selected numerical moduli. SP-2 and all eight td6 terminal classes remain
  alive. The valid successor varies the licensed common centering, F1 orbits,
  dead stretch, and pole parameter while preserving their source-typed
  transport. Further bands at this dead numerical point add no information.

## AS109 QUINTIC-Y NO-GO (2026-08-24, DUAL-CONFIRMED SCOPED TIER)

`xmodel/quintic-y-frontier-preflight-independent-20260824.md` (producer
SHA-256
`598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978`)
with `xmodel/quintic-y-review-grok-20260824.md` (review SHA-256
`ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e`):
**CONFIRMED**.

- FIELD THEOREM: every Keller pair over an arbitrary characteristic-zero
  field whose two coordinate `y`-degrees are at most five is a polynomial
  automorphism. The confirmed quartic theorem handles all lower patterns;
  the only new actual pairs are `(2,5)`, `(3,5)`, and `(4,5)`.
- NEW PAIRS: `(2,5)` has an uncancellable `3rho^5/8` finite-pole term and a
  final polynomial unit-product contradiction. `(3,5)` has a cubic first
  integral; finite-pole leading equations have subresultant 441, while every
  nonconstant polynomial point on the resulting singular Weierstrass cubic
  gives `R'Psi(R)` with `deg Psi=6` and nonzero leading coefficient.
  `(4,5)` has two polynomial first integrals; weighted `(2,3,4)` finite-pole
  equations have no point (resultant `-12180258816` on the nonzero branch),
  and every polynomial-infinity branch gives a nonzero term of degree
  `8q-1` in the constant Jacobian row.
- AS109 CONSEQUENCE/SCOPE: no exact AS109 lift has both correction
  `y`-degrees at most five. A surviving coupled section must allow
  `y`-degree at least six. Sextic pairs, arbitrary support, existence of a
  lift, priority, and JC2 remain open.

## AS109 GENERIC DEGREE, `A_infinity`, AND DECK-DESCENT REDUCTION (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

The producer/review pairs
`xmodel/as109-hensel-global-degree-cross-gate-20260824.md` /
`xmodel/as109-degree-cross-review-grok-20260824.md` have SHA-256
`7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` /
`fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6`;
`xmodel/as109-ainfinity-deck-descent-gate-20260824.md` /
`xmodel/as109-ainfinity-review-grok-20260824.md` have SHA-256
`f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` /
`a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76`.
Both hostile reviews are **CONFIRMED**.

- DEGREE/SPLIT: conditionally on an exact integral AS109 lift, with
  `M=Q_109(P,Q)`, `L=Q_109(x,y)`, and `d=[L:M]`, complete-ring parameter
  Hensel gives 109 distinct `M`-embeddings into the target-tube fraction
  field. Hence `d>=109` and
  `L tensor_M E = E^109 x A_infinity`, with
  `dim_E A_infinity=d-109`. After descent to a finitely generated coefficient
  field and abstract embedding in `C`, the **generic degree `d`** persists;
  the displayed 109-adic tube splitting is not transported to `C`.
- VALUED MEANING: after height-one localization/completion, the 109 integral
  roots are precisely the Hensel sheets; every other geometric root has a
  negative source valuation. Thus `dim A_infinity` is the exact sum of
  valued-initial multiplicities at negative extended weights, axes included.
  A fixed finite support admits a finite exact discriminator. Mixed volume or
  generic tropical intersection is not that discriminator.
- TWO MISSING KEYS: finiteness of the formal fibre algebra over the complete
  target ring would force `d=109` and `A_infinity=0`, but abstract etale and
  Zariski-Main data do not. A rational `L`-factor of the self-fibre algebra is
  exactly an element of `Aut_M(L)`, but a formal permutation of the 109 split
  factors does not descend. `A_infinity=0` together with a descended
  109-cycle would give a cyclic Galois degree-109 Keller extension and a
  contradiction; neither key is proved.
- CONTROLS/SCOPE: triangular non-Keller maps realize every `d>=109` and every
  residual rank while retaining the same local split, and can have trivial
  rational deck group. No degree congruence, `109|d`, properness, lift
  obstruction, or JC2 conclusion follows from local Hensel data alone.

## MOSKOWICZ PRIME-DEGREE PROOF IS UNSUPPORTED (2026-08-24, DUAL-CONFIRMED SOURCE-AUDIT TIER)

`xmodel/moskowicz-prime-degree-source-audit-20260824.md` (SHA-256
`929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210`)
with `xmodel/moskowicz-prime-degree-review-grok-20260824.md` (SHA-256
`a32082a89077b17bb9f9df4d2b518d8e7ad6de4e126a35cf0d49b446bb0d5a06`):
**CONFIRMED `REFUTED-AS-PROOF / HEADLINE NOT ESTABLISHED`**.

- The load-bearing first case of arXiv:2407.13795v1 attributes to a
  MathOverflow answer the implication that a stated rare-monomial property
  forces extension degree two. The answer proves no such universal
  implication. Exact Kummer controls
  `C(s^n,v) subset C(s,v)`, with `x=s+v`, `y=s+2v`, satisfy that property for
  every `n>=2`, so the printed inference is false.
- These controls are not Keller subfields. They refute the proof step, not
  the prime-degree statement itself, and produce no counterexample.
- The paper's second case is repairable: after choosing a nonzero generic
  linear parameter, Wang's intersection theorem and Gwozdziewicz's
  injectivity-on-one-line theorem show that a complex Keller map with
  `xy in C(P,Q)` is an automorphism. This repaired implication does not use
  prime degree. The paper cannot be consumed to exclude degree 109.

## AS109 `xy` MEMBERSHIP ROUTE STOPS (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-xy-membership-gate-20260824.md` (SHA-256
`09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729`)
with `xmodel/as109-xy-membership-review-grok-20260824.md` (SHA-256
`04c4d3dc8342141c4b1cb615e232a00053a056825fddbe55dd3ba5c2b44b8ac0`):
**CONFIRMED `SHARP NO-GO FOR MEMBERSHIP`**.

- On the tube `(P,Q)=(109S,1+109T)`, the Hensel sections satisfy
  `x_a y_a = a mod 109`; their 109 images are distinct. Therefore
  `[M(xy):M]>=109`, so `xy` lies in neither `M=Q_109(P,Q)` nor the target
  ring. Nonmembership survives coefficient-field extension to `C`, closing
  the proposed client of the repaired Moskowicz implication.
- If separately `A_infinity=0`, then `d=109`, `L=M(xy)`, and the tube-local
  monic minimal polynomial reduces to `Z^109-Z`. Its trace, norm, and
  discriminant are split-etale tautologies and yield no obstruction. This is
  not a global integral equation over `Q_109[P,Q]`.
- The univariate root-translation test is equivalent to supplying the missing
  descended deck action; it is not forced by symmetric coefficients. No lift
  is excluded or constructed.

## SEXTIC PARTIAL-`y` CLOSURE AND BOUNDED-SIX SYNTHESIS (2026-08-24, DUAL-CONFIRMED FIELD-THEOREM TIER)

The genuine sextic leaves and synthesis have the following producer/review
SHA-256 pairs:

- `(4,6)`: `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` /
  `183ad7d6eab8b9f74041c2eb7d29180b2c75a4bc84d82bfeb681f29a55b9c32c`;
- `(5,6)`: `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` /
  `d7b4f0e033f63f5e8f1f62b44f98ae23b566071cd34c810c18199cd099f88b70`;
- bounded-six synthesis: `1078bbdd47ccf085900b93b165ee268d314d2cc4e387b30ad81c4a40817e12f3` /
  `81669337bf038ae2bb2d81c20bec7ef92a97eaeaa03f906d0a20c33bf20a9115`.

All three hostile reviews are **CONFIRMED**. Over every characteristic-zero
field, every Keller pair whose two actual partial `y`-degrees are at most six
is a polynomial automorphism. The proof ledger closes `(4,6)` by its
imprimitive local-normalization branches and `(5,6)` by the third integral,
weighted common-factor identity, two polynomial boundaries, and infinity
contradiction; target reductions cover every other pair. Therefore an exact
AS109 lift has at least one correction of `y`-degree at least seven.

This entry promotes mathematical validity only. It makes no novelty claim:
the separate source-shear history audit may supply a shorter classical proof
and a stronger frontier. No arbitrary-support AS109 no-go, lift existence,
or JC2 inference follows.

## TD6 SYMBOLIC-MODULI THIRD-BAND CHAIN (2026-08-24, DUAL-CONFIRMED FINITE-FAMILY TIER)

The moduli-uniformity, paired-point, and moduli-uniform third-band
producer/review SHA-256 pairs are respectively:

- `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` /
  `d95e0d684464c2f56b76ceb5cf32158d47ed907565216ff2974ca1d5f883730b`;
- `a98de6d23ff2942360c328e4eeb6c08e24a122b0f9c964a5ad586cf0b009e9f2` /
  `3f2462b2c61d01a39769cc82cf3e9a04732e2bc824edea92bcb0eb9c449d3ad7`;
- `0d3e2dc8e57b03060582d6906212ae707cb1d42b10416cff85117daa93b4ed7b` /
  `582933fca15c8e1005460591f795102d43c60a9733b8bc19f0b7bdbd716784ef`.

All three hostile reviews are **CONFIRMED**.

- UNIFORM NEXT ROW: on the retained x-boundary/F1 pattern,
  `[s^-1 t^13]J=(6/5)(5E2-2E1^2)`, independently of common centering and of
  pole/dead-stretch data absent from that coefficient. The real form is
  negative definite, but over `C` its zero curve carries a genuine
  56-dimensional paired finite-band survivor on the normalized slice.
- PAIRED POINT: the first explicit quadratic point on that curve dies at the
  next centered row, where the whole 56-family has
  `[s^0 t^0]J=81/15625`. This kills only that point.
- UNIFORM THIRD BAND: on the entire moduli curve, the constant centered row
  cuts to an irreducible sextic `F(S)`. Adjoining the cubic pole scale gives a
  degree-18 field; the remaining centered equations have homogeneous rank
  `25/58`, and an exact left syzygy has nonzero residual, including
  `(136875/29)A`, at all 18 conjugates. Hence the fixed normalized reduced-
  boundary family is empty at this band.
- SCOPE/NEXT: SP-2 and every terminal class remain alive because x-boundary,
  dead-stretch, centering, and other boundary moduli were fixed. The valid
  successor varies one such datum and tests its pairing with the existing
  left syzygy; another band on the empty family is invalid.

## PARTIAL-`y` SOURCE-SHEAR HISTORY STOP AND FIRST TRUE FRONTIER (2026-08-24, DUAL-CONFIRMED CLASSICAL-THEOREM TIER)

`xmodel/as109-partial-y-history-stop-20260824.md` (SHA-256
`6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`)
with `xmodel/as109-partial-y-history-review-grok-20260824.md` (SHA-256
`f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd`):
**CONFIRMED `ALL MAXIMUM ACTUAL y-DEGREE <=8 IS CLASSICAL; FIRST
FUNDAMENTAL REMAINDER (6,9) WITH 3|H`**.

- SHEAR THEOREM: for actual degrees `m=da`, `n=db`, `gcd(a,b)=1`, the top
  Jacobian row gives `a_m=alpha h^a`, `b_n=beta h^b`. With `H=deg h` and a
  sufficiently large triangular source shear `y -> y+x^L`, the exact total
  degrees are `a(H+dL)`, `b(H+dL)` and their gcd is `H+dL`.
- CLEAN CLASSICAL INPUTS: if `gcd(H,d)=1`, Dirichlet makes this gcd prime and
  Nagata's repair of Appelgate--Onishi applies. If `gcd(H,d)=2`, it can be
  made `2p` and the independent Guccione--Guccione--Valqui theorem applies.
  Magnus is only the coprime-total-degree theorem; the gap in Zoladek's
  neighboring argument is not consumed. The field statement descends from
  `C` to every characteristic-zero field.
- COVERAGE/PRIORITY: every pair with partial gcd at most two is therefore
  classical. Equal-degree `GL_2` and divisible-degree target shears then cover
  all 81 ordered pairs with maximum actual `y`-degree at most eight. Hence
  the campaign's `(4,6)`, `(5,6)`, and bounded-six proofs remain correct
  alternate certificates but are not first exclusions. Consecutive-degree
  widening is stopped as duplicate history.
- FIRST REMAINDER: at maximum nine, the only fundamental residue is `(6,9)`
  with `3|H`; `(9,9)` is derivative through target reduction. The leading
  family `F=K^2`, `G=K^3`,
  `K=z^3+u t^2 z+v t^3`, has zero binary Jacobian and a positive-dimensional
  leading-boundary locus. It is not Keller; it proves only that the earlier
  coprime finite-map certificate does not transfer. The valid successor is a
  gauge-quotiented transverse deformation and cokernel test, not generic
  coefficient search.
- AS109 COROLLARY: conditionally on an exact lift, maximum actual `y`-degree
  at most eight is impossible by reviewed Hensel noninjectivity. Maximum
  exactly nine reduces, by an integral target operation and possible swap, to
  `(6,9)` with `3|H`. Its first non-top `y^13` row is automatically divisible
  by `109^2`; an exact primitive-core control rules out a universal first-row
  valuation contradiction. No lift, arbitrary-support no-go, or JC2 result
  follows.

## GCD3 `(6,9)` FIRST COMMON-CUBIC GATE (2026-08-24, DUAL-CONFIRMED STRUCTURAL TIER)

`xmodel/gcd3-69-common-cubic-first-gate-20260824.md` (SHA-256
`f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8`)
with `xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md`
(SHA-256
`5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503`):
**CONFIRMED `KUMMER SPLIT / FULL-CUBIC BOUNDARY TYPE-FAIL /
COMMON-CUBIC UNION UNIQUE DS / FIVE PLUS KAPPA`**.

- SOURCE NORMALIZATION: after `a_6=h^2,b_9=h^3` and `s^3=h`, the `y^13`
  row makes `delta=3A-2B` constant. A nontrivial cubic Kummer action forces
  `delta=0`; a cube core makes `h` a constant times a polynomial cube but
  leaves `delta!=0` live. The depression `z=sy+A/6` is over `k(x)(s)`, not a
  polynomial source automorphism, and its two boundary values are polynomial
  but need not vanish.
- BOUNDARY FIREWALL: a chosen boundary root licenses reduction only modulo
  its minimal polynomial. Reduction modulo the full depressed cubic requires
  an independently proved orbit of degree three; squarefreeness alone is
  insufficient. An exact split-root perturbation is a `TYPE-FAIL` of the
  stronger boundary inference, not of any conclusion derived from extra
  Jacobian rows.
- CONSTANT-W SCHEME: after solving the eight high binary rows, the residual
  radical has exactly the common-cubic surface and one order-three
  Davenport--Stothers curve. They meet set-theoretically only at the triple
  cubic; the original scheme is nonreduced along the common component. The
  DS identities, constant Wronskian `378*lambda^7`, and nonzero resultant are
  exact and independently reconstructed.
- SOURCE HIGH ROWS: in the aligned nontrivial-Kummer branch, all eight high
  source rows integrate exactly. Kummer weights and constant target gauges
  leave five moving coefficients plus one essential weight-zero constant
  `kappa`; a path persisting on the common component has
  `f=K^2,g=K^3+kappa*K` and zero source bracket. One associated-graded common
  point does not prove such persistence.
- CONDITIONAL DS STOP: only under pure DS entry, weighted Euler gives
  `(lambda^7)'=j/(81s)`. Exact finite/infinity valuations, the reviewed
  `3|deg(h)` residue, and both polynomial boundaries exclude that pure path.
  Entry from the full source system is not inferred.
- SCOPE/NEXT: this does not solve the four lower Pfaffian rows, terminal row,
  filtered boundary/component persistence, or cube mismatch, and does not
  exclude `(6,9)` or decide JC2. The licensed successor is precisely those
  lower rows in the five-plus-`kappa` form, componentwise with the true
  minimal boundary factor, while `delta!=0` runs independently.

## AS109 WILD-SYMPLECTIC COMPLETED-BIDISC GATE (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-wild-symplectic-conductor-gate-20260824.md` (SHA-256
`c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c`)
with `xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md`
(SHA-256
`a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a`):
**CONFIRMED `GAUGE-TRIVIAL / CONTROL-ONLY`**.

- COMPLETED TORSOR: conditionally on an exact integral lift of
  `(x-x^p,y)`, `Z_p<x,y>` is finite free etale of rank `p` over
  `Z_p<P,Q>`. The special Artin--Schreier translations lift uniquely to a
  free constant-`C_p` torsor action on the closed unit bidisc, and the chain
  rule makes every deck transformation determinant one.
- GAUGE TRANSITIVITY: any two determinant-one restricted-analytic lifts of
  the same special map are uniquely right-equivalent by a near-identity
  restricted-analytic symplectomorphism. Thus unrestricted completed
  cohomology has one gauge orbit. The statement does not provide a rational
  or polynomial deck map, act on `A_infinity`, or imply generic degree `p`.
- FIRST DIGIT: the exact norm, order, divergence, and invariance equations
  form one affine orbit under divergence-free right gauges. Nevertheless
  every solution has `[x^(p-1)y]Q1=1`; independent exact compilers at
  `p=3,5` give quotient dimension zero and recover the rational cotangent
  tower through depths two through four.
- SCOPE/NEXT: the forced monomial is a first-digit floor, not an unbounded
  support theorem, and the growing cotangent representative is not known to
  be minimal. A valid successor must define minimal support or degree inside
  the unique completed orbit with uniformly bounded polynomial gauges, or an
  algebraic boundary conductor invariant under a specified bounded
  equivalence. No `p=109` brute force, lift, fixed-support exclusion,
  `A_infinity` conclusion, or JC2 decision follows.

## AS109 BOUNDED POLAR CONDUCTOR (2026-08-24, DUAL-CONFIRMED CONDITIONAL TIER)

`xmodel/as109-bounded-polar-conductor-gate-20260824.md` (SHA-256
`2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b`)
with `xmodel/as109-bounded-polar-conductor-review-grok-20260824.md`
(SHA-256
`bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa`):
**CONFIRMED `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`**.

- EXTERIOR DIVISOR: for every odd prime `p`,
  `C_p=(x-x^p,y/(1-p*x^(p-1)))` is an integral restricted-analytic
  determinant-one lift. Over `Qpbar` its rational second coordinate has
  exactly `p-1` reduced affine vertical polar components, all at valuation
  `-1/(p-1)` and outside the closed unit bidisc. This divisor is neither the
  projective line at infinity nor the residual factor `A_infinity`.
- NO POLYNOMIAL CANCELLATION: for every polynomial Keller right map
  `phi=(X,Y)`, without assuming invertibility or JC,
  `gcd(1-p*X^(p-1),Y)=1`. Thus the rational pole cannot cancel. Under a
  polynomial symplectic automorphism the polar divisor pulls back
  isomorphically; under a merely Keller right map only noncancellation, not
  preservation of the component count, is claimed.
- CANONICAL CONDUCTOR: conditionally on a polynomial lift `F`, the reviewed
  completed-orbit theorem gives the unique identity-branch gauge in the
  orientation `C_p o Phi_F=F`. The maximum total degree `kappa_n(F)` of its
  canonical reduction modulo `p^n` tends to infinity. A uniform degree bound,
  or a uniform bound on the nested support cardinalities, would make
  `Phi_F` polynomial and contradict the no-cancellation lemma.
- FINITE CAPS: every fixed simultaneous map/gauge degree pair fails at some
  finite Witt depth by a finite-tree inverse-limit argument. At the first
  natural caps `D_F=D_phi=p`, depth two survives and depth three is empty for
  every odd prime. Exact independent controls give coefficient/augmented
  ranks `12/13` and `32/33` at `p=3,5`, with forbidden monomials `x^4y` and
  `x^8y`; additional `p=7,11` checks are controls only.
- SCOPE/NEXT: this does not exclude a polynomial lift or give a growth rate,
  identify `A_infinity`, descend a deck action, compute at `p=109`, or decide
  JC2. The licensed successors are a quantitative lower growth law for
  `kappa_n` or intrinsic-cap elimination, and an independently proved
  comparison with the valued initial systems governing `A_infinity`.

## TD6 SMALLEST Q-BOUNDARY DEFORMATION (2026-08-24, DUAL-CONFIRMED TWO-POINT TIER)

`xmodel/td6-boundary-q2-deformation-gate-20260824.md` (SHA-256
`f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`)
with `xmodel/td6-boundary-q2-deformation-review-grok-20260824.md` (SHA-256
`6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c`):
**CONFIRMED `TWO-EXACT-EMPTY-SPECIALIZATIONS / STOP`**.

- SOURCE/SCOPE: inside the already-cut normalized SP-2 chart-pattern
  control, retain the fixed rectangles, center, zero dead stretch, reduced
  F1 pattern, r9 relation, sextic, and degree-18 pole field, and deform only
  `p=t^15`, `q_B=t+B*t^2+t^25`. This is the smallest displayed q-jet, not a
  complete SP-2 boundary normal form.
- `B=1`: the exact chain has ranks `3508/3602`, then `36/94`, then tangent
  rank `25/58`, and is empty at the centered input row `t^4`. Its residue
  differs from the frozen `B=0` residue by exactly `-14012/145`, so the
  obstruction is genuinely `B`-sensitive rather than copied unchanged.
- ADAPTIVE POINT: at the exact secant-cancellation candidate
  `B_*=rho_0/(14012/145)` in the degree-18 field, the full `B`-dependent
  rebuild has ranks `3470/3602 -> 132`, `+38 -> 94`, `+38 -> 56`, tangent
  rank `25/56`, and is again empty at `t^4`. The residual has nonzero
  `1,A,A^2` components, directly refuting affine secant extrapolation.
- SCOPE/NEXT: neither generic `B` nor the one-parameter family is killed;
  other q-jets, centering, dead stretch, F1 data, SP-2, all terminal classes,
  and JC2 remain open. The licensed successor is symbolic fraction-free
  elimination over `E[B]` plus separate treatment of every pivot/rank-jump
  locus. Sampling or an adjoint shortcut alone is not a certificate.
