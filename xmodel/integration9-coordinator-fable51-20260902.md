# INTEGRATION #9 — coordinator binding (Fable 5.1, 2026-09-02)

Basis fef326a9. Supplements integration #8 (dcce5652). Different-model
hostile review satisfied on every PROMOTED item; hashes are the sealed
report files' SHA-256 prefixes as recorded in notes.md.

## A. Case (A) is empty at every degree (producer opus 2a1717ae; gate
## gpt55 0ab02c19 ALL CONFIRMED; countermodel arm grok c50ecca9 ALL SURVIVE)

**PROMOTED — THEOREM CUSP-A-VOID.** MPRIME case (A) is EMPTY for every
N >= 2. Scope: over C, algebraic; A_F homeomorphic to C and singular;
F Keller of geometric degree N >= 2. H2-FREE (uses only Lin–Zaidenberg,
étaleness, properness over C^2 \ A_F, chi additivity, and C[t]^* = C^*).
Proof shape: chi(C^2 \ A_F) = 0, so chi(E) = 1 for E = F^{-1}(A_F); by
NO-CUSP-PREIMAGE E is smooth with disjoint components, so some component
is A^1 and maps non-constantly into A_F \ {c} = C^*: impossible. Second,
independent route (Fable-lane ideation 58020a0e §1.1, CUSP-A-ALL-N):
MPRIME Prop 6.1's a_{p_0} = 1 gives a sheet fixed by the whole group
(local-to-global pi_1 is an isomorphism at a cone cusp), against
transitivity; the gpt55 gate confirms Prop 6.1 as an affine-fibre
statement, so the two routes are contrapositives around a_{p_0} ∈ {0,1}
and both stand.
**PROMOTED — LOCAL-TRANSITIVITY LEMMA (NO-CUSP-PREIMAGE).** If c ∈ A_F
has pi_1(B_c \ A_F) -> pi_1(C^2 \ A_F) surjective (equivalently rho(Loc_c)
transitive on the N sheets), then F^{-1}(c) is empty. In case (A) the
map is an isomorphism (weighted C^*-retraction; c is the vertex in
Lin–Zaidenberg coordinates), so E is smooth and its components are
pairwise disjoint. Elementary companion (used throughout, SUCC-1 typing):
an affine preimage y of p ∈ A_F is a sheet fixed by rho(Loc_p) with
(E, y) analytically isomorphic to (A_F, p); hence #cusps(E) = a_{p_0},
not a. (B3) with a_{p_0} = 1 is consistent exactly because its cusp local
monodromy is not transitive.
**PROMOTED — THEOREM PERIPHERAL-RANK, under the cage constraint F1
(2 <= j <= a <= N-2):** #orbits<rho(m), rho(z)> = j; the base orbifold of
the cover's Seifert fibration has genus 0. NOT a theorem about all
torus-knot covers (explicit violators outside F1 at N = 4, 8, 9).
**PROMOTED — THEOREM MERIDIAN-SPAN** (kappa * j <= a) and **kappa | a**,
same F1 scope; **THEOREM CUSP-A-VOID-II** (the two force rho(m) = 1,
against W >= 2); **THEOREM CUSP-A-KAPPA** (every kappa = 1 cell is empty
at every N; SW's conjecture, upgraded).
**PROMOTED — identity chi(E) = nu − Sigma*** with the reviewer's
puncture split (cusp / C^* / infinity; the cusp and infinity terms
cancel).
**PROMOTED — composition with SMOOTH-KILL at its banked typing:** the
non-properness set of a noninvertible Keller map is never homeomorphic
to C.
Consequences (binding): THEOREM PROFILE loses row (A) at EVERY N; under
H2 the residual for N <= 16 is exactly (B2) ∪ (B3), and (B1) only at
N >= 17; OPEN[HOMCOVER-CUSP-A-N8] and OPEN[MPRIME-CUSP-J2] CLOSED NEGATIVE
at all N; CASE-A-SWEEP's survivor lists are historical. Citation
correction (grok arm): Lin–Zaidenberg is Soviet Math. Dokl. 28 (1983)
200–204, not Invent. Math. 68 (1982).

## B. The Chau degree cap (producer opus ideation, checker gpt55 99ade634)

**PROMOTED — (9,6)-NO-COMPANION.** At coordinate degrees
(deg P, deg Q) = (9,6) the Chau cap sum_i deg D_i <= max(deg P, deg Q) = 9
is saturated by the realised degree-9 component (leading form
(u^2 − v^3)^3), so an actual reducible non-properness set of such a
Keller map contains no companion: OPEN[COMPANION-R0-REALISATION] is
NEGATIVE at coordinate degrees (9,6). Scope: coordinate degrees, not the
numerical row; the resultant exponent is alpha*m, identified with m only
when the R_0 component is reduced. The cap is a valid census prefilter
at Chau's hypotheses (Keller, monic in y after a generic source change).
RECORDED (reproductions with repairs): under H2, deg A_F = m*max(d,e),
m <= K, one place at infinity (Chau via COMPANION C6–C8); delta_infty is
NOT numerical in (m,d,e) for m > 1 — OPEN[DELTA-INFTY-NOT-NUMERICAL]; no
finite (m,d,e) list at fixed N without a bound on max(deg P, deg Q) in N —
OPEN[N-VS-MAPDEG]; (B3) needs n >= 4 with a finite necessary list for
n <= 8. OPEN[DEG-AF-VS-N] RETYPED accordingly (answered half: DEG-AF-CHAU;
open half: N-VS-MAPDEG; plus the target-Aut minimal-degree question).

## C. The A2 residual re-filed (producer fable51 ideation §1.2;
## adjudicator sol 4820a2cf, steps (1)–(4) CONFIRMED)

**PROMOTED — THEOREM PHI-IMMERSION**, for the declared A2 factorisation
F = pi ∘ iota with the retained chart: iota is étale and surjective with
Jelonek set exactly Phi = V(A,U); A_F = A_pi ∪ pi(Phi); the residue
parametrisation of pi(Phi) is unramified (E0); under H2 every point of
A_F has a smooth branch, so the model is PROFILE (0)/(B1), and (B1) only
at even N >= 18. The package "A2 exact-model identification + H2 +
affine (B3) cusp" is INCONSISTENT (GAP[EXACT-MODEL-ID]: the structure
report's identification with the horn was provisional). The r2/CELL-32
lane never assumed H2 (refuting one line of the submission).
**BINDING RE-FILING:** bare A2/CELL-32 = PROFILE-UNTYPED, N-UNTYPED
(legitimate constant-bracket algebra; finite boxes prove box-local
emptiness only); any actual N <= 16 survivor is reducible-A_F. The (B3)
horn has NO analytic model. OPEN[A2-U-BOUND] is demoted from "the horn's
missing theorem" to an untyped algebra question; the coordinator's
07:22Z/07:41Z "one theorem away" framing is withdrawn.
RECORDED: cell (1,5) EMPTY with a Q-exact engine (sympy, ray-kill's
driver, preserved in box/raykill-cells-20260902) plus the msolve/qqideal
engine — promotion-grade box-local emptiness under the re-filed typing;
(2,6) exact (RAY-EDGE control); (1,7) MODULAR; (1,9) modular screen lost
to a coordinator mis-kill, exact-Q run in progress.

## D. Records (not promoted; review debt LOW)

Round 20260902T0741Z: four blind submissions plus the coordinator's
(synthesis in progress; sol56 pending at binding time). Stack cutover to
qqideal 0.2.0 + msolveio 0.2.1 after a zero-disagreement mini-oracle.
Web sweep 2026-09-02 (c16b9b62): THREAT board empty; the Schenk Zenodo
manuscript remains FATALLY-FLAWED per the 09-01 audit. SG-1/SRC-0/SG-2/
HC-1/HC-2 and the BURNSIDE-CHI rank formula remain unreviewed records.
The A2 window's post-gate EMPTYs are box-local evidence only.

## E. Standing fronts after this integration

1. **The (B3) horn through the source curve E** (b3-e-geometry running:
   log-Kodaira/BMY on (A^2, E) and on the Galois closure; splice at
   infinity; rational five-punctured A2-curve embedding; the
   ANTI-MONOTONE (N, a) table; the Domrina–Orevkov mechanism read-off).
   THE H2 neck below N = 17.
2. **(B2) beta-forced 5 <= N <= 16** via the target-Aut minimal degree of
   A_F and the Chau budget once the infinity Puiseux datum is supplied.
3. **Reducible branch:** OPEN[COMPANION-R0-REALISATION] elsewhere than
   coordinate degrees (9,6); the razor stack; the cap as prefilter.
4. **All-degree ceiling:** ANTI-MONOTONE; R <= 1 for (B1).
5. **A2 bridge questions** (a2-ubound successor): m = [K(S):C(f,g)],
   A_pi and the components of A_F, the residue-collision hypotheses.
6. **Counterexample side:** profile-driven census design (next
   micro-round); B3-PARAM-SEARCH on the n <= 8 list after
   b3-e-geometry.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7415`.
- Body SHA-256:
  `6a3148a5ed426cb5b969bfa33402cf00d9463e37d472a64760c0a9b7e91f810e`.
- Frozen basis: `fef326a93932e124911a3e92a67025b33880683e`.
