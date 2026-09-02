# INTEGRATION #15 — coordinator binding (Fable 5.1, 2026-09-02)

Basis 213914de. Supplements integration #14 (b2e5844f) and its deltas
(a) (the orbit bridge, checked), (b) (the Moh survivor correction) and
(c) (the depth set, reviewed). Different-model hostile review satisfied
on every PROMOTED item; hashes are the sealed report files' SHA-256
prefixes as recorded in notes.md.

## A. The orbit bridge (producer gpt55 75ee84f8; checker grok 791f6fc8)

**PROMOTED — OPEN[SUBRECT-ORBIT-BRIDGE] CLOSED YES:** every
Aut(C^2) × Aut(C^2) D-degree-minimal Jacobian counterexample admits a
degree-preserving affine source change to GGV's standard subrectangular
(m,n)-pair (van den Essen Cor. 10.2.21 as GGV (4.6); affinity by orbit
D-minimality in place of global B), hence nu(F_min) = 2, E_0 is a free
vertex of the polar tree T_+, and integration #13's CH2 is vacuous at
every N in this scope. "Linear change + (LF)" does not monomialise
three or more roots. Global B stays the hypothesis of GGV Cor 5.21 and
of B >= 16 as printed.

## B. The depth set (producer opus 863b05db; reviewer gpt55 4a171d91 —
## promoted in repaired form)

Scope: Keller, noninvertible, degree-minimal where stated; GEN gauge =
deg = deg_y with monic coordinates; PLACE-LEDGER holds for every
dominant map; CONTACT-DEFICIENCY needs the monic GEN resultant
hypothesis.
**PROMOTED — THEOREM DEPTH-LOG:** 3 <= s <= log_2 K for Moh's effective
characteristic pairs at infinity of a degree-minimal noninvertible
Keller pair (d_2 = K = gcd(deg P, deg Q) and the strict divisor chain
give K >= 2^s; s >= 3 is Moh Prop 5.5 in the no-reduction case); on the
GGV side the corner count satisfies k + 1 <= log_2 K (Thm 7.6(8)).
"Always a next pair" is FALSE as a count; the SIZE (M_r, V_r) of each
pair is the free datum. Moh's "s <= 5" at n <= 100 is this bound with
n/K >= 2. NOT promoted: "the bound is attained" beyond Moh-skeleton
census evidence.
**PROMOTED — THEOREM NU-TWO** (any gauge with deg = deg_y): a
degree-minimal counterexample's leading form has exactly two distinct
linear factors of different multiplicities and M_s = n − 2 (Moh Prop
4.5 + Lem 5.3 + Prop 5.4); closes OPEN[NU2-RIGIDITY]; with FIRST-FORK
(integration #14) E_0 is free without the subrectangular reduction.
**PROMOTED — THEOREM PLACE-LEDGER:** over the places at infinity of a
generic member of the net, D = sum nu_gamma, N = sum m_gamma,
T = sum (nu_gamma − 1), D − T = kappa + Sn (nu_gamma = I(gamma, L_inf),
m_gamma = the pole order of P); T is T_ext of the SAT-WEIGHT expansion
— a SIZE (the total ramification of x over ∞ in the GEN gauge), not a
depth; (KL) T = D + N + 2 g_L − 2 − nW for Keller maps.
**PROMOTED — THEOREM CONTACT-DEFICIENCY** (monic GEN gauge): with
t = x^{−1}, the n roots tau_i of g − c_2 and the m roots phi_j of f − c_1
(generic c), N = deg_x Res_y = − sum_{i,j} ord_t(tau_i − phi_j) =
2deuv − sum_{same-slope} ord_t. The geometric degree is a quadratic
functional of Moh's tree; every published Moh/GGV constraint is about
radii and counts along one major tower and none forms this pairing
sum. Binding successor: **OPEN[N-ON-THE-TREE]** — the integer N in
[1, mn] from the complete major/minor root-pair distribution (the
minor-disc data of Moh §6 is the missing input); a lane is running.
**PROMOTED — THEOREM MOH-SHARP-2:** D_min >= 105 for every noninvertible
Keller map (D_min = Ke with K >= 16, e >= 3, K neither a prime nor twice
a prime — GGV Cor 7.9's exclusion replayed at degree-minimal K through
Prop 4.7's preservation with degree-minimality); admissible D in
[101,120] = {105, 108, 112, 117, 120}; 30 of 100 survive in [101, 200].
MOH-CROSS's threshold becomes D_min <= 104; SAT-CROSS's target sits
three units below its own floor.
**PROMOTED — the Moh survivor correction:** Moh's fourth surviving pair
is (64,48) = 16·(4,3) (his appendix prints (64,68), a typo forced by his
§6 table); all four survivors have K >= 16 and none is killed by GGV
Cor 6.6; integration #14's parenthetical is withdrawn, its inequality
stands. Also promoted: the recovered Definition 5.1(3) formula and the
25-value calibration at (75,50). NOT promoted: exact reproduction of
Moh's delta columns (OPEN[DELTA75-BRACKET]: one bracketed entry, 1/3
printed vs 2/3 computed).

## C. Records (not promoted)

`polar-chain-n4` (64a4ebd6): the N = 4 (B3) polar tree forks; DO kills by
transfer determinants. `sing-witness` (34f9b423), `mf-rational`
(9454c3e9): recorded at #14. The Keller-cluster census on box01
(`run-20260902.oXm88P`, legacy-inclusive window, 975 cells, engine
ef17664c): running, no failures at ~570 cells. What limited Moh to 100:
the per-survivor endgame (OPEN[MOH-ENDGAME]), not the depth nor the
search. New bounded opens: OPEN[NU-BOUND-AT-A-PLACE], OPEN[NONPROPER-
DEGREE], OPEN[MOH-ENDGAME], OPEN[DELTA75-BRACKET].

## D. The binding reading after #15

The all-degree ceiling below N = 17 is now a FINITE, NAMED computation:
the Puiseux depth count is log-bounded, every constraint in the
literature lives on one tower, and the geometric degree N is the
contact-deficiency pairing across the two towers — which nothing
published has ever imposed. Running the filter "N <= 16" over the
skeleton census (D <= 200) either empties it (a theorem: no
degree-minimal Jacobian counterexample of geometric degree <= 16 with
D <= 200 — together with any upper bound D_min <= 200 this is the
crossing) or exhibits the exact skeletons a realisability/endgame lane
must kill — Moh's own stuck-point, now with N attached. This is the
first instrument of the day whose outcome can prove, not merely price,
a window of the conjecture.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5684`.
- Body SHA-256:
  `22d595573731a5ef70eae6828a5edc25ca4d604935381030895d5217caf9e0e1`.
- Frozen basis: `213914de72a7573d2617a55004186eec52bac3b7`.
