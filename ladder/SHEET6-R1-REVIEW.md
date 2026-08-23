# SHEET6-R1-REVIEW.md — Adversarial review of the R1 cap-2 core kill (f29eafd)

Reviewer: Claude (adversarial pass, 2026-08-09). Status: COMPLETE.
Scope: the SHEET6-R1.md sec 6 claim "`systems/r1/r1_gmband_core.ms`
msolve GB = [1] (char 0, ~5 s) => minimal-tower genome UNSATISFIABLE at
coefficient level, conditional on core-emission faithfulness". Ground
truth: SHEET6-TEMPLATE.md 1a-1d, 2c (E3-E7); SHEET6-LT-REVIEW.md front
7; refs/sigray_full.pdf Prop 4.2 pp. 19-20 re-read on-page. Engines:
msolve 0.10.1 (local), r1_experiment.py emission re-run from
/tmp/r1_state.pkl.cap2 (byte-identical re-emission), independent
float64 rebuild of the G_m band written for this review (own code, no
engine imports; anchors: slot-0 = S_M P^2 / G_M P^3 to 4e-11, E1
slot-0 cancellation to 1.2e-15).

Verdicts:
- Front 1 (radical generators): **CONFIRMED FAITHFUL** — all 7 radical
  equations match TEMPLATE 1b under the declared gauge; W_i quartic
  correctly ABSENT (relaxation-only); no wrong order/sign anywhere.
- Front 2 (equation provenance): **FAIL — the 57 band rows are NOT true
  consequences of the template.** The row FAMILIES are the right
  template statements, but every shipped row is a silent cap-2
  TRUNCATION: the HIVAR lossy-row filter is defeated by exact sentinel
  cancellation in W_G = g^2 − f^3 (283 keys; all 57 shipped keys
  affected; 57/57 fail an independent full-degree numeric comparison).
- Front 3 (gauge/scale): **CONFIRMED NOT over-constrained** (det-420
  claim independently re-derived, = 10 in natural units); and the
  var/equation count alone (109 unknowns, 57 rows, no constant terms)
  already made GB = [1] impossible for the intended system.
- Front 4 (independent kill confirmation): **KILL REFUTED.** GB = [1]
  is an ARTIFACT OF msolve'S INPUT PARSER: the emitted file uses
  parenthesized coefficients, which are outside msolve's grammar and
  are silently mangled. Proven four independent ways (sec 4).
- Front 5 (echo rungs, 5df68d2): **CONFIRMED** — level-3 W2-collapse
  arithmetic re-derived by hand (all three t-conditions); Prop 4.2
  k1 = 1 legality reading verified on-page; SURVIVE-IN-PRINT stands.
- Front 6 (scope): **NOTHING DIED.** Status quo ante of SHEET6-R1 sec 4
  (partial clause) is the operative verdict; sec 6 must be retracted.

**NET: THE KILL IS SPURIOUS — doubly.** (1) msolve never saw the
intended system: its parser silently mis-reads the parenthesized
emission format (the reduced GB of the 7 radical equations ALONE comes
back provably wrong), and the [1] is reproducible from just 3 mangled
band rows with NO radical equations at all. (2) Even a correct parse
would have tested the wrong system: the "57 rows exact at cap 2" claim
is false — all 57 are truncations whose deg >= 3 content was silently
dropped by sentinel cancellation, and the banked core contains NONE of
the discriminating row families (all 84+54 C1-Gm and all 9 quotient
rows went lossy). The true cap-2-emittable system is PROVABLY
satisfiable (x = 0 plus any radical point is a solution). The
minimal-branch template is NOT excluded; the decision still rests on
the full-degree core (SHEET6-R1 sec 5 step 1), which has never been
run.

## 1. Front 1 — radical generators (7 equations, 9 generators)

File block (eqs 0-6) vs TEMPLATE 1b under the sec 3.0 gauge (A = 1,
sigma = 6, s0 = 1, a = 0):

- `r3^2-3`: base field Q(sqrt3). OK (a_i, all E6 data live there).
- `A1^3-(3+r3)`, `A2^3-(3-r3)`: a_{1,2} = (sigma/2)(1 ± 1/sqrt3) = 3 ±
  sqrt3 at sigma = 6 (TEMPLATE 1b line 86) — exact; alpha_i = the
  cube-orbit branch datum at level 32 (pi(G_m) = 16/21, TEMPLATE 1d
  "7 x 3 x 2" audit). Cubic form keeps all three roots: enumeration,
  not a choice. OK.
- `2*HW1^2-3*W1^2`, `2*HW2^2-3*W2^2`: hw_i = ±sqrt(3/2) w_i is the
  g-side pole pattern root: p_g@P_i = m_i eta (eta^2 − (3/2) w_i^2)
  (TEMPLATE 1b line 108). The engine's E5 z-identity gate
  (z(z−(3/2)w^2)^2 − (z−w^2)^3 = −(3/4)w^4 z + w^6, checked over the
  ring with w free) is verbatim TEMPLATE 2c-E5 lines 229-235; sign and
  normalization re-verified by hand. Quadratic form = both signs kept.
  OK.
- `2*EB^7-3`: eta_B^7 = B = (3/2)A = 3/2 (TEMPLATE 1b line 87; B-orbit
  eta-direction datum, 1d line 130). OK.
- Phi_42: `(1)+z^1*(1)+z^3*(-1)+z^4*(-1)+z^6*(1)+z^8*(-1)+z^9*(-1)
  +z^11*(1)+z^12*(1)` = z^12+z^11−z^9−z^8+z^6−z^4−z^3+z+1 = the 42nd
  cyclotomic polynomial (kappa = 42 common root, TEMPLATE 1a line 64;
  engine derivation from prod (x^d−1)^{mu(42/d)} re-checked). Right
  ORDER (a wrong order was the front-1 fear; it is not present). OK.
- W_1, W_2 have NO defining equation: the E5 quartic w_i^4 = k_i
  alpha_i^2 is deliberately deferred (engine comment line 88-90 "w_i
  FREE (E5 quartic relation deferred to terminal core)"). The doc's
  k_i (SHEET6-R1 sec 3.0, denominator a_i^3 with w^4 = k alpha^2)
  equals TEMPLATE line 239 (denominator a_i^2 c_i): alpha_i^2/a_i^3 =
  1/(a_i^2 alpha_i), c_i = alpha_i. Since the quartic is a TRUE
  template constraint that is OMITTED, the core is weakened, never
  over-constrained — safe for a kill, and the E5 discriminating load
  moves to the quotient rows (which all went lossy, sec 2).

The radical block defines a nonzero etale-over-two-free-parameters
algebra (W_1, W_2 free): it is satisfiable over C, all conjugate
branches simultaneously (7c enumeration subsumed). It cannot
contribute an inconsistency. FRONT 1: PASS.

## 2. Front 2 — provenance of the 57 band rows

Row census (re-derived from the cap-2 state; emission re-run is
byte-identical to the repo file, so the file = the state rows):

- Shipped 57 = ALL "WG-band" (W_G(n,s) = 0), s in {6,8,10,12,14,16,18},
  n in {0..11} u {24..36}. NO C1-Gm row, NO quotient row shipped.
- Lossy 311 = WG-band 164 + C1-Gm-g 84 + C1-Gm-f 54 + WG-quot 9.

(a) The FAMILIES are correct template statements. W_G := (g-jet)^2 −
(f-jet)^3 on the G_m arc (engine phase "wg") is the print-true tower
h1 = g^2 − s0 f^3, gauge a = 0, s0 = 1 — Prop 4.2(ii) re-read on-page:
h_{j+1} = h_j^{k_j} − s_j f^{l_j}, powers of f, NOT (f−a); LT-REVIEW 7b
mandate satisfied. Normalizations line up exactly (through-factor count
12/18, x-lead 126 = 126, G_R^2 = s0 S_R^3 = 1). Band slots 1..19 must
vanish and slot 20 must be proportional to qpat = eta (e3−a1)^2
(e3−a2)^2 (e3−b): this is TEMPLATE 1b G_m (p_h1 = H_M eta P^2 (eta^3−b),
deg 16, d_h1 = 8/21) + delta(G_m) = (10,0) — ten 1/21-steps = 20 slots
at 1/42 from the 18/21 top to the 8/21 pattern. Independent
verification: my own prefix-only numeric rebuild gives band slots 1..19
= 0 to 7e-15 relative and slot 20 nonzero — the cancellation depth is
real and the frame is right. The quotient rows' H_M-elimination
(cross-multiplication by qpat[16] = 1) imposes only proportionality:
weaker than the template statement, hence safe. The C1-Gm odd-slot
family is the (1/21)-lattice condition at the kappa = 21 vertex
(TEMPLATE 1a); at prefix level odd slots <= 20 vanish by the
C_7-phase sums (checked by hand: e_1..e_5 of the w-phase suborbit are
zero, first survivor e_6 at slot 30), consistent with the ledger
(odd C1 rows first appear at m = 41).

(b) BUT the shipped POLYNOMIALS are not those statements. Defect
mechanism (verified explicitly): vmul collapses any var-monomial of
degree > cap to the sentinel key (HIVAR,) with coefficient set to
RONE per vmul call; jmul accumulates these into small positive integer
counts. In W_G = jadd(g^2, jscal(f^3, −1)) the counts SUBTRACT.
Measured on the cap-2 state: g^2 and f^3 each carry sentinels at 461
keys; their sentinel coefficients are EQUAL at 283 keys and cancel
exactly — e.g. (0,6): 2 = 2; (0,12): 3 = 3; (0,18): 6 = 6; (2,16):
15 = 15; (36,6): 2 = 2. All 57 shipped keys are in the cancellation
set. The emit_gm_core lossy filter (`any(k[-1] == HIVAR)`) therefore
classified genuinely capped rows as "exact". The gate check "HIVAR
flags conservative" (gate 3) strips sentinels from BOTH sides before
comparing and never tested this.

(c) Consequence, quantified: an independent full-degree numeric
rebuild of the band (own code, random unknowns, anchors passing) shows
ALL 57 shipped rows disagree with the true W_G coefficients at
relative deviation ~1.0, with true values up to 1e15 x larger (the
dropped content includes e.g. deg-18 B-tail monomials with
combinatorial multiplicity). An epsilon-scaling test (unknowns x ->
eps x; eps = 1e-2/1e-3/1e-4 gives worst deviation 1.18/0.247/1.6e-3)
confirms the shipped rows are exactly the deg <= 2 slices — correct at
low degree, truncated above. A truncation is not a relaxation: at
cap 2 "row = 0" is neither implied by nor implies the true condition.
FRONT 2: FAIL — one of the two independent grounds for SPURIOUS.

## 3. Front 3 — gauge and scale consistency

- 4 continuous gauge parameters (x-scale lambda, y-scale mu, f-scale,
  g-scale) vs 4 conditions (A = 1, sigma = 6, S_R = 1, G_R = 1),
  triangular: A ~ mu^7 lambda^{-2}, sigma ~ mu^3 lambda^{-16/7} (from
  eta_Fs^7 ~ y^7/x^2, eta_Gm^3 ~ y^3/x^{16/7}); det = (−2)(3) −
  (7)(−16/7) = 10 ≠ 0 — the doc's "det 420" is this in 1/42-units.
  CONFIRMED not over-constrained. A, sigma ≠ 0 are structural
  (distinct pattern roots; a1 ≠ a2 forces sigma ≠ 0), so the gauge is
  reachable on any realization. s0 = 1 is then DERIVED via E1
  (G_R^2 = s0 S_R^3), not imposed. c0 never consumed (shift lemma,
  asserted; no c0 occurs in any emitted row — checked).
- Discrete choices: kept as full radical fibers (all conjugates), the
  correct enumeration-free form; residual discrete gauge slack is a
  symmetry, not a constraint.
- Count sanity THAT WAS MISSED: 118 vars = 109 engine unknowns + 9
  radical generators; 64 equations = 7 radical + 57 band. The radical
  block is satisfiable with 2 free parameters; the 57 band rows have
  NO constant term (verified from the state: no VExpr has a ()-key),
  so x = 0 satisfies them identically. Expected dim >= 54; an EMPTY
  variety was impossible a priori. The 5-second [1] on a system whose
  variety visibly contains a rational-radical point should have been
  the tell. FRONT 3: PASS (gauges), with the a-priori-impossibility
  observation charged to the sec 6 verdict note.

## 4. Front 4 — the [1] is a parser artifact (kill refuted)

Reproduced locally: msolve 0.10.1, `-g 2` on the repo file -> [1] in
0.02 s. Then:

1. **Radicals-only mis-parse (decisive).** The 7 radical equations
   alone return reduced GB `[3W2^2-2HW2^2, 3W1^2-2HW1^2, r3^2-3,
   A2^3-1, A1^3+1, 2EB^7-3, z^12+z^11+z^9+z^8+z^6+z^4+z^3+z-1]` —
   A1^3 = −1 and A2^3 = +1 instead of 3 ± sqrt3, and Phi_42 with all
   negative coefficients sign-flipped and constant −1. Over the
   intended ring these are false; msolve parsed different polynomials.
2. **Grammar micro-tests.** `x-(3+1)` -> GB [x+1]; `x+(-2)` -> [x-1];
   `x^3*(-1)+1` -> [x^3+1]; `(2+y)*x-1, y^2-3` -> [x-1, y^2-3]. msolve
   accepts parentheses silently and mis-evaluates them (no error, no
   warning). The msolve input grammar is expanded monomials with
   integer/rational coefficients; every one of the 57 emitted band
   rows is written as `(ring-poly)*xi*xj` with nested parens and
   embedded `+`/`-` — all mangled on read.
3. **Minimal artifact.** ddmin over the 57 rows: THREE mangled rows
   suffice for [1] — .ms eqs 40, 47, 61 = WG-band (27,6), (30,6),
   (36,6) — and the radical equations are NOT needed (GB of the 3
   mis-parsed rows alone is [1]). Each is 1-minimal (removing any one
   loses quick-[1]). The true content of these rows has no constant
   term; a 3-row homogeneous-free system in 100+ vars cannot have GB
   [1]. This is the "deep structural clash msolve found instantly" of
   sec 6: three garbage polynomials with garbage constants.
4. **Correct encoding.** Re-emitted the same 57 rows + radicals in
   msolve grammar (fully expanded, integer coefficients, no parens:
   /tmp/r1rev/core_correct.ms, byte-provenance from the same state).
   msolve then behaves like a real 118-var positive-dimensional
   problem (no output in 150 s, char 0 AND mod 65521) — no quick [1].
   Satisfiability of the true system needs no GB at all: x = 0 plus
   (z, r3, A1, A2, EB any conjugate; W_i = HW_i = 0) satisfies all 64
   equations by inspection.

A hand-verifiable contradiction chain over Q(sqrt3) therefore does NOT
exist for this core — the opposite: a hand-verifiable SOLUTION exists.
FRONT 4: the kill is SPURIOUS with certainty; no template feature is
contradicted by the banked system.

## 5. Front 5 — echo rungs (5df68d2), spot-checks

- mu-recursion (Prop 4.2 (9)/(iv), p. 19, re-read): mu3 = 3 + 5(17/6)
  = 103/6 and 4 + 5(23/6) = 139/6; L4@Fs bounds (mu3−1)·12+1 = 195 /
  267; generic tops 6·34 = 204 / 6·46 = 276; 9-degree = 3-coefficient
  collapse demanded. All CONFIRMED.
- Level-3 W2-collapse (sec 4.2 RUNG), re-derived by hand in t = eta^3:
  q^6 = H^6 t^2 P^6 (t−b)^6 with q = H eta P (eta^3−b): t^20 pins
  s2' = H^6; t^19: −6b − 6sigma = −10sigma <=> b = (2/3)sigma; t^18:
  15b^2 + 36b sigma + 15sigma^2 + 6a1a2 = 45sigma^2 + 10a1a2 <=>
  a1a2 = sigma^2/6 (using b = 2sigma/3). Both collapse conditions are
  IDENTICALLY the Prop 8.1(iv) ODE pin — "3 conditions, 2 unknowns, 0
  kills" is arithmetically right, residual degree 51 -> deg p_h3@Gm =
  144+51 = 195 / 216+51 = 267, saturating the bound EXACTLY. The
  orbit pin 6r = (1+r)^2 -> a2/a1 = 2 ± sqrt3 checks. CONFIRMED.
- Termination: 6r3 = 195/2, 267/2 not integers (no level-4 tie);
  delta_j strict descent is PRINTED (p. 20 proof re-read: delta_{j+1}
  = delta_j + kappa(d_{h_{j+1}} − k_j l_j d/k_j) < delta_j) — finite
  towers a priori. CONFIRMED.
- (1,2) legality: Prop 4.2 statement (p. 19) has k_j in N* with
  gcd(k_j, l_j) = 1 and (iii) (h_j^+)^{k_j} = s_j (f^+)^{l_j}: k1 = 1
  is admissible and (iii) reads h1^+ = s1 (f^+)^2 exactly as sec 4.3
  claims; no printed exclusion. The "bites only where the level-1 tie
  holds" vertex reading is consistent with the (iii) top-form
  semantics. CONFIRMED (SURVIVE-IN-PRINT and the disjoint-branch
  delta-spec stand).

## 6. Front 6 — verdict scope and the path forward

What actually died: NOTHING. Retract SHEET6-R1.md sec 6; the operative
verdict is sec 4's partial clause, unchanged: gate 15/15, linear
residue consistent to depth 54, decisive content = the FULL-degree
terminal core, never yet built or solved. The book of 4 + residue-A
configuration are unchanged; R1 remains per-branch decisive on
{minimal (3,4), (1,2), (2,3)-chain (6,17), (2,5)-chain (6,23)} with R6
print-closed on the other 6.

Required fixes before ANY future core verdict is bankable:

1. **Emission format**: emit msolve files ONLY as expanded
   integer-coefficient monomial sums (the re-encoder written for this
   review does this); add a round-trip guard — parse the emitted file
   with an independent reader and evaluate both against the state rows
   at a random point, AND run msolve on a known-satisfiable subset
   (e.g. radicals alone) expecting a non-[1] GB.
2. **Sentinel soundness**: make lossy-row detection cancellation-proof
   — either unique sentinel keys per capped event, or (cheaper) carry
   the lossy (n,s)-set as an explicit side-channel unioned across
   g^2, f^3 and the jets BEFORE any subtraction/combination; re-run
   the exactness census (the true exact-at-cap-2 count is <= 57 and
   possibly 0).
3. **[1]-plausibility guard**: before accepting an empty-variety
   verdict, test the explicit x = 0 (all-unknowns-zero) point and the
   radical-block GB; a kill certificate must name the row subset and
   survive re-derivation over Q(sqrt3) by hand (the sec 6 note skipped
   both).
4. **Full-degree build** (SHEET6-R1 sec 5 step 1) remains THE task:
   the discriminating families (C1-Gm odd slots, slot-20 quotient with
   its E5-quartic load, F_s band, later J-closure) are all outside the
   cap-2 window; at cap 2 the banked band rows are satisfied by x = 0
   and can never kill. Per-(orbit,k) sub-checkpointing at cap >= 4 or
   a FLINT/flat-poly backend; then eliminate ~half the unknowns by the
   rank-54 linear reduction; then msolve (mod-p first) on a correctly
   encoded core.
5. **Branch reuse**: the emission machinery (orbit model, arc, jets,
   band emitter) transfers to the three surviving branches; per-branch
   deltas are only (i) the staged G_m depth table — (1,2): insert one
   h1-resonance stage 18/21 -> 12/21 (quotient const*P^4, legality
   h1^+ = s1 (f^+)^2) -> 8/21; (2,3)/(2,5)-chains: h3-stages to
   195/42 resp. 267/42 with residual P^{24|36}(q^6 − H^6 P^10) and the
   finite (1,l)-tail — and (ii) a deeper G_m window plus higher jet
   powers (h2^6 needs var-degree tracking >= 12: full-degree backend
   is a prerequisite there too, not optional).

## 7. Reproduction

- Reproduce [1] + artifact: `msolve -g 2 -f systems/r1/r1_gmband_core.ms`
  (0.02 s locally); radicals-only and 3-row files: /tmp/r1rev/rad_only.ms,
  minimize scripts /tmp/r1rev/minimize*.py.bak.
- Re-emission (byte-identical) and correct re-encoding from
  /tmp/r1_state.pkl.cap2: /tmp/r1rev/reemit.py -> /tmp/r1rev/core_correct.ms.
- Sentinel-cancellation audit and independent numeric rebuild
  (anchors, 57-row comparison, prefix-only band, epsilon-scaling): the
  three /dev/stdin scripts recorded in the review transcript; state
  file required (regenerable via `--cap=2` phases per SHEET6-R1 3.0).
