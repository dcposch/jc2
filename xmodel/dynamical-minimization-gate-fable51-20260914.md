# FIRST: integer Keller dynamics and a minimization control

Fable 5.1, different-model hostile reviewer, 2026-09-14, lane opened 19:56 UTC.
Charged producer: xmodel/keller-dynamical-minimization-swarmHQ-root-20260914.md.

## Verdict

PASS at the named-import tier for both producer statements and for all five
audit items. No refutation. Two harmless locator/wording notes below. Nothing
here is a Keller-specific lowering step or a JC2 argument, as the producer says.

## Input custody

All five sha256 values were recomputed in /tmp/jc2-lane.ugBFbX/inputs and
matched the charged pins before any mathematical reading:

- producer 84837d2d29fd8b60c6e10a7de6cf7fa10d7b428a8e02c46a494e4b8ae3e24957
- manifest f370ac725264f71e5593abc3bc9be062e7d46083014de46b9b65f76c0fcc5c2e
- PDF e85b214ae52e6d04a42807f5e4234d945b17bcdd12e2939efbb7fa7c41ae2381
- text 30400b3a1e1df8e99b8a4461546d9a32cd5aec4715038125ef7f9443e17ea874
- prior INTAKE 3af0eb610ed6155d7bffcfbc75d7b0c01437a52f3728e2d68ad0a99319b2d7ee

The first 5652 bytes of the producer hash to the manifest body_sha256
edcb3bd34836a461772cbf4d3b3a7380e7e2fac273cef138c6dc233a2762c657 and end at
the standalone BODY-END line. pdftotext of the charged PDF to stdout at
printed 213, 216 and 220 reproduced the coordinate convention, the irrational
thinness sentence and the Prop 2.5 matrix sentence of the charged text.

## Primary read scope

Whole producer; whole prior INTAKE, whose accepted premise (constant
determinant 0<|c|<=1 gives lambda1 >= d) is consumed, not re-audited. FJ text
lines 1-120 (introduction, Theorem C, p.213 convention), 200-300 (sections
1.2-1.4), 300-490 (sections 1.5-2.3: Props 2.1-2.8, proofs of 2.4, 2.5, 2.8,
Examples 2.11-2.12), 760-960 (section 5: (5.1), Props 5.1-5.3, (5.2),
Lemma 5.4, printed proofs of 5.1 and 5.2). No whole-paper audit.

## Claim 1, integrality and lambda1 >= d: PASS, import tier

Let JF = 1 and let d be the generic fibre count, which is FJ's topological
degree lambda2. F is dominant. lambda1 >= d is the premise, and d >= 1.

lambda1 = 1: integral; the premise forces d = 1; the Jacobian identity is
vacuous and unused.

lambda1 > 1: then d <= lambda1 < lambda1^2. Only lambda1 > 1 is used for the
strict inequality, never d < lambda1 or properness. Section 2 opens with an
arbitrary dominant polynomial map. Prop 2.3 gives nu in V1 with F_* nu =
lambda1 nu, hence d(F,nu) = lambda1 and F_bullet nu = nu; Prop 2.2 gives
d(F,.) > 0 on V1 "even when F is not proper". Thinness: A maps V0 to
[-2,+inf] (section 1.3) and A <= 0 on V1 by the section 1.4 definition, so
A(nu) is finite. The formula A(nu) + nu(JF) = d(F,nu) A(F_bullet nu) is stated
in the printed proof of Prop 2.8 "for all nu in V1" for that general map,
citing [30, Lemma 7.6]; (5.2) restates it. Its section 5 placement restricts
nothing. Since nu(1) = 0, (lambda1 - 1) A(nu) = 0, so A(nu) = 0. Section 1.3:
"An irrational valuation has irrational skewness and thinness", so nu is not
irrational. Under lambda2 < lambda1^2, Theorem 2.4(a) makes nu the unique
eigenvaluation, so it is the nu_* of Prop 2.5; case (ii) is excluded and case
(i) gives lambda1 in N. Zero-thinness divisorial or infinitely singular nu_*
are not excluded, as stated. The determinant enters only through nu(const) = 0
and the premise; the det 1 restriction is conservative and correct.

## Claim 2, attained minimum and one-sided reduction: PASS, elementary

Chain rule: det D(alpha F beta) = 1 for alpha, beta in Aut_1, and bijections
preserve the generic fibre count, so Claim 1 reapplies to each alpha F beta.
The value set contains lambda1(F) and lies in Z_{>=d}, a nonempty set of
integers bounded below, so it has a least element. This is attainment, not a
floor. beta(alpha F beta)beta^{-1} = beta alpha F with beta alpha, beta^{-1}
in Aut_1; lambda1 is conjugacy invariant (FJ p.212, or directly from
deg((beta G beta^{-1})^n) <= deg beta . deg G^n . deg beta^{-1} both ways). So
the two-sided set equals {lambda1(gamma F): gamma in Aut_1}. No invariance
under independent changes is used, and none holds (H_m below). No degree
bound on a minimiser, no algorithm, no lowering follows.

## Claim 3, M control, pointwise part: PASS, import tier

M = (x^2 y, x y). Inverse: u/v = x and v^2/u = x^2 y^2/(x^2 y) = y, so M is
birational and d = 1. JM = det[[2xy, x^2],[y, x]] = 2x^2 y - x^2 y = x^2 y,
non-constant. M sends {x=0} and {y=0}, distinct irreducible curves meeting at
the origin, to the origin. For arbitrary polynomial automorphisms alpha, beta
(no determinant condition used anywhere), f = alpha M beta sends
beta^{-1}{x=0} and beta^{-1}{y=0}, distinct irreducible curves meeting at
beta^{-1}(0), to alpha(0). f is dominant, lambda2(f) = 1, lambda1(f) >= 1.

Suppose lambda1(f) = 1. Then lambda2 = lambda1^2 and section 5 applies. Either
deg f^n is bounded (Prop 5.2) or deg f^n/1^n is unbounded (Prop 5.1); the
split is exhaustive. Prop 5.2: f is a polynomial automorphism, injective, so
it contracts no curve. Prop 5.1 at lambda1 = 1: f = (P(x), A(x) y + O_x(y^0))
= (ax+b, A(x) y + B(x)) in affine coordinates. By the p.213 convention this
means after conjugation by a polynomial automorphism; the printed proof
straightens the rational pencil via [30, section 7.4], i.e. the Line Embedding
Theorem, so a linear reading would be false in general. Conjugation by a
bijection carries contracted curves to contracted curves and preserves
distinctness and incidence; independent source/target bijections would too,
so the reading is immaterial. An irreducible curve contracted by the skew form
has constant first coordinate, hence is a vertical line, and distinct vertical
lines are disjoint. Contradiction. So lambda1(f) > 1 for every alpha, beta,
covering translations and all automorphism degrees.

## Claim 4, uniform sqrt2 gap: PASS, import tier

Pointwise lambda1(f) > 1 does not bound the infimum; the producer says so and
supplies the correct tool. For each f, lambda2 = 1 < lambda1(f)^2, so Prop 2.5
and its printed proof apply: lambda1 in N (then >= 2), or lambda1 not in Q with
irrational nu_*, and then lambda1 is the spectral radius rho of a 2x2 matrix
[[a,b],[c,d]] with nonnegative integer entries (printed 220). Hand check:

- b = 0 or c = 0: triangular, rho = max(a,d) in Z, so rho >= 2.
- b, c >= 1, a = d = 0: rho = sqrt(bc); rho > 1 forces bc >= 2, so
  rho >= sqrt2 (bc = 2 gives exactly sqrt2; the floor is not claimed sharp).
- b, c >= 1, a + d >= 1: entrywise the matrix dominates [[1,1],[1,0]] or its
  simultaneous row/column permutation; Perron monotonicity gives
  rho >= (1+sqrt5)/2 > sqrt2.

Hence the infimum over all frames is >= sqrt2 > 1 = d(M). "Quadratic integer"
alone would not do: (-1+sqrt13)/2 = 1.30 is a quadratic integer below sqrt2,
but its trace -1 is unrealisable by a nonnegative matrix. The matrix
description is load-bearing and the producer uses it.

Controls. Identity: lambda1 = d = 1. H_m = (y, y^m - x): DH_m =
[[0,1],[-1, m y^{m-1}]], det 1; inverse (u^m - v, u), polynomial, det 1;
writing H_m^n = (p_n, p_{n+1}) with p_{n+1} = p_n^m - p_{n-1} gives
deg p_{n+1} = m deg p_n, so lambda1 = m, while H_m^{-1} H_m = id has
lambda1 = 1 = d. Frame values need not equal the attained minimum, as stated.
M itself: lambda1(M) = rho[[2,1],[1,1]] = (3+sqrt5)/2 with lambda2 = 1,
matching Prop 2.5(ii) through Example 2.11; the swapped frame M(y,x) gives
1+sqrt2. Both exceed sqrt2.

## Claim 5, scope: PASS as stated

No lowering theorem, "minimum <= d", properness, inverse, complete scalar pair
or JC2 consequence is claimed or implied. Mismatch search: FJ's lambda2 is the
topological degree, i.e. the INTAKE's generic degree; Props 2.2, 2.3, 2.8 and
(5.2) carry no properness hypothesis; Prop 2.5's dichotomy needs
lambda2 < lambda1^2 and both uses supply it; Theorem 2.4(a) supplies the
uniqueness identifying Prop 2.3's nu with Prop 2.5's nu_*; Props 5.1-5.2 need
only dominance and lambda2 = lambda1^2 = 1. No counterexample found: every
polynomial automorphism has integral lambda1 (Example 2.12, Friedland-Milnor),
consistent with Claim 1. The M control has contracted curves, impossible for a
Keller map, so it rejects only the degree-only premise for general birational
maps and says nothing about Keller minimization.

## Limits and corrections

- Import tier: Props 2.3, 2.5 (with [30, Th. A'] and [30, Th. 7.7] inside its
  proof), the Jacobian formula [30, Lemma 7.6], Theorem 2.4(a), Props 5.1-5.2
  and Friedland-Milnor are consumed as published statements, not re-proved.
- Locator: the range -2 <= A <= 0 combines section 1.3 (A >= -2) with the
  section 1.4 definition of V1 (A <= 0); the producer credits section 1.3
  alone. Harmless.
- Wording: Prop 5.1's form also carries deg A >= 1; omitted, not needed.
- Observation, not promoted: the integrality half of Claim 1 seems not to
  need the premise (the lambda2 = lambda1^2 case would run through section 5
  with the same thinness step); unaudited, and the producer's route stands.
- No computation, no exact infimum for M, no sharpening of sqrt2, no novelty
  or priority check. No exit-price assertion is made.

<!-- BODY-END -->
