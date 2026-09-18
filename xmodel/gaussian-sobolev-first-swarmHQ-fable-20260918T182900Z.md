# Independent FIRST and scope corrections: Gaussian Sobolev cutoffs

Reviewer: Fable 5.1 (requested model=fable, effort=max; hosted identity not independently exposed).
Integrator: swarmHQ ROOT (gpt-6-astra).
Date: September 18, 2026, UTC.
Reviewed producer commit: 0ad11f45906b4647ea3d4b2b054b20f3de90639d.
Evidence tier: MANUAL, independent hostile review.
Lifecycle: completed FIRST; promotion is recorded separately in AUDIT.md.

## Reviewed result and custody

[Producer](gaussian-sobolev-cutoffs-swarmHQ-root-20260918T181400Z.md),
full SHA256 ebc99617025da3f63305d27e629fbb36edebab98beb4ba5b4d421235464df5fb.

The reviewer read the whole producer, FALLACY-v2 and COORDINATION from
immutable charged snapshots. All three pre/post hashes matched; terminal
receipt reports DONE/exit0, CLEAN/BODY_SEALED and unchanged inputs.
ROOT independently verified termination before receipt-first collection,
then read the whole terminal review and log. No external source or
scientific computation was used. The historical notes cited by the producer
were not re-read by this reviewer and are not proof dependencies.

Retained terminal original hashes:
- Review: 87919278a10f61ae8fc1a7d46877e9fc903802d21d29888b49643dee3b9ccbf3
- Receipt: e6342ab5a60b8527012bcb11dbc837a72942ea550ce71e1266cccad2eb18b019
- Log: 45be0909fcfc4fe273ae2021ce13ce88e3b5354bd76da31783f22b43343c3aaa

The mathematical review sections below are preserved verbatim. Operational
paths and receipt metadata are omitted from this public integration.

## ROOT binding clarifications

The reviewer confirms all three producer claims and their controls. ROOT
accepts those conclusions, with the following corrections to REVIEWER
commentary, not changes to the frozen producer:

1. The parenthetical in review Claim4 saying that g is in general incomplete
   is NOT accepted for an actual whole-plane polynomial Keller map. Its
   completeness is not assumed or proved here; no noninvertible example is
   known from this argument. Read that passage only as a statement that the
   proof does not use completeness.
2. The rational control proves strict inclusion of the first-order domain
   in holomorphic L2. Strict inclusion alone is NOT a proof of nondensity.
   The final review's stronger density inference is not part of promotion.
   Neither density nor nondensity in the holomorphic subspace is asserted.
3. The two minor proof-presentation points are valid elementary
   clarifications: properness over U plus the local covering property gives
   N sheets; finitely many singular-ball cutoffs can be combined as
   rho_sing=1-product(1-rho_j), with gradient norm bounded by the sum.
   The existing proof's budget order accommodates that choice.
4. Promote only the finite-energy cutoffs, density in the FULL REAL
   weighted W1,2 space, the stated pairwise integration identity, and the
   checked L2/non-L2 control. No maximal complex-operator domain equality,
   holomorphic core, strong commutation, polynomial integrability,
   completeness or JC2 conclusion is obtained. No novelty claim.

## Verbatim mathematical review

<!-- REVIEW-MATH-BEGIN -->
## Per-claim verdicts

### 1. Finite map over U={h!=0}, degree N, source-compact preimages: CONFIRMED

Reconstruction. Nonzero constant Jacobian gives dF_1, dF_2 pointwise
independent, so a minimal relation P(F_1,F_2)=0 would force both partials
of P to vanish on the image; hence F_1,F_2 are algebraically independent
and Frac(B) is a finite extension of Frac(A) of some degree N. Clearing
denominators of the monic minimal polynomials of x and y over Frac(A) gives
a nonzero h in A with x,y integral over A_h. Since B_h = C[x,y,1/h(F)] =
A_h[x,y], B_h is a finite A_h-module, and Spec B_h = F^{-1}(U).

Elementary properness over U, checked: on a compact K inside U, |h| is
bounded below, so the A_h-coefficients of the monic equations are bounded
on K; the Cauchy root bound |root| <= 1 + max|coeff| bounds |x| and |y| on
F^{-1}(K); F^{-1}(K) is closed as the preimage of a closed set. Compact.
Nothing global is used. A proper local homeomorphism onto connected U is a
finite-sheeted covering; the sheet number is the generic fibre count N.

Reduction of h to its radical does not change U; Z is then a reduced plane
curve with finite singular set; h(F) is a nonzero polynomial (F dominant),
so F^{-1}(Z) has real measure zero. The change-of-variables identity with
factor N is the N-sheeted local-isometry covering formula, and dvol_g is
absolutely continuous, so omitting F^{-1}(Z) costs nothing. a=1 gives mass
N*pi^2 since the plane Gaussian integral is pi. The constant Jacobian never
appears explicitly because dvol_g = |J|^2 dvol already absorbs it.

Minor omission (not a gap): the sentence "finite etale with N sheets" does
not spell out flatness or the covering-map step; both are standard and the
report's own root bound already supplies the properness needed.

### 2. Small-energy removal of Z on a target compact: CONFIRMED

Singular balls: a bump rescaled to radius r has gradient L^2 norm O(r) in
real dimension 4 (gradient O(1/r), volume O(r^4)). Finitely many singular
points inside the closed ball, radii below delta, combined norm below
sqrt(tau)/2. Checked.

Smooth part: the closed remainder of Z in the closed R-ball outside the
open inner balls is compact and inside the smooth locus. Tubular charts
(t,s) in R^2 x R^2 with Z={s=0}; profile q_eps(r)=Psi(log r/log eps) with
Psi smooth, 1 for argument >= 2, 0 for argument <= 1, gives q=1 on r<=eps^2,
q=0 on r>=eps and |q'| <= C/(r|log eps|) with C=sup|Psi'|. Normal energy:
integral from eps^2 to eps of (C^2/(r^2 log^2 eps)) 2 pi r dr = 2 pi C^2 /
|log eps|, tending to 0. Normal mass <= pi eps^2, tending to 0, so the
tangential-cutoff gradient term (sup|d psi|^2 times chart area times normal
mass) also tends to 0. Chart distortion is bounded on a relatively compact
chart. Supports shrink into the delta-neighbourhood by uniform continuity
of the chart map on the compact tangential support. Checked.

Circularity check: the order is (i) singular radii fixed with energy below
sqrt(tau)/2, (ii) chart count M fixed by covering the resulting compact
smooth remainder, (iii) eps_j chosen after M with each chart energy below
sqrt(tau)/(2M). M may depend on the singular radii, but the singular energy
is already fixed and the chart energies are chosen last. No circular bound.

Product bookkeeping: eta is a product of finitely many [0,1]-valued smooth
factors; d eta = sum over k of (product of the other factors) d f_k, each
other-factor product has modulus <= 1, so |d eta| <= sum |d f_k| pointwise
and Minkowski gives the displayed bound below sqrt(tau). Vanishing on a
neighbourhood of Z in the closed ball: inner open balls for the singular
part, and the chart set {psi=1 interior, |s|<eps^2} for smooth points.
eta=1 outside the delta-neighbourhood because every factor is 1 there.
d eta compactly supported. M=0 empty product = 1 handled; Z empty gives
eta=1; Z nonempty but missing the R-ball gives rho_sing=0, M=0, eta=1.

Minor omission (not a gap): rho_sing must be a single [0,1] function; take
1-rho_sing as the product of the per-ball factors (or disjoint balls). The
same triangle inequality then applies.

### 3. chi_n smooth, source-compact, ->1 a.e., g-energy ->0: CONFIRMED

supp a_n lies in the closed 2n-ball and misses an open neighbourhood of Z
within that ball, so supp a_n is a compact subset of U; by Claim 1 its
preimage is compact in the source, and supp chi_n is a closed subset of it.
chi_n = a_n o F is smooth with values in [0,1]. For fixed z outside Z,
dist(z,Z)>0, so for n > max(|z|, 1/dist) both theta_n and eta_n equal 1 at
z; F^{-1}(Z) is null. Energy: g = F^* g_Eucl gives |d(a o F)|_g = |da| o F
pointwise, and the N-sheeted covering formula with the nonnegative
integrand |d a_n|^2 exp(-|z|^2) gives the displayed equality. With
|d(theta eta)|^2 <= 2|d theta|^2 + 2|d eta|^2 (both factors in [0,1]),
the first term integrates to at most 2 C^2 pi^2/n^2 and the second to at
most 2 tau = 2/n^2 (exp(-|z|^2) <= 1). Total <= 2 N C^2 pi^2/n^2 + 2N/n^2,
exactly as displayed. Target infinity is handled by theta_n and the finite
Gaussian mass; no decay of eta_n is needed since d eta_n is compactly
supported. L^2 convergence by dominated convergence with finite mu. The
arbitrary nonzero constant Jacobian only enters through dvol_g. Checked.

### 4. C_c^infty density in the full real weighted W^{1,2}: CONFIRMED

The weight exp(-|F|^2)|J|^2 is smooth and positive and g is a smooth
metric on the source C^2, so W^{1,2}(mu,g) sits inside W^{1,2}_loc(R^4)
with the ordinary distributional differential. Truncation: T_k u ->u with
d(T_k u) = 1_{|u|<k} du by the weak chain rule and dominated convergence,
applied to real and imaginary parts. Cutoff: for bounded v, (1-chi_n)v and
(1-chi_n)dv tend to 0 by dominated convergence and ||v d chi_n|| <=
||v||_inf ||d chi_n||, which tends to 0 by Claim 3. This is exactly where
boundedness is needed and is why truncation precedes cutoff. Mollification:
the source is one global chart R^4; on a compact neighbourhood of the
support the weight and g are uniformly comparable to Lebesgue/Euclidean,
so Euclidean mollification converges in the weighted norm and keeps
supports inside that neighbourhood. Diagonalise the three steps.

Smuggling check: no completeness of g (g is in general incomplete), no
uniform geometry, no distance-function cutoff, no second-order estimate,
no Bakry-Emery or spectral input is used anywhere. The target-side cutoff
pulled back through the finite covering replaces the usual distance cutoff.

### 5. Scoped identity <D_i a,b> = <a,-bar D_i b + F_i b>: CONFIRMED

Local computation checked with the inner product linear in the first
slot: d/dz_i of exp(-z bar z) = -bar z_i exp(-|z|^2); integrating by parts
for compactly supported smooth a against bar b exp(-|z|^2) gives
-<a, bar D_i b> + <a, z_i b>, using conj(bar D_i b) = d(bar b)/dz_i and
conj(z_i b) = bar z_i bar b. Signs and conjugations correct. On the source
the same local coordinates z=F(p) give dvol_g = dz, so the identity holds
for a in C_c^infty and b in W^{1,2}_loc by the definition of the weak
derivative (D_i, bar D_i have polynomial coefficients from the constant
Jacobian inverse). |D_i w| and |bar D_i w| are bounded by a constant times
|dw|_g, so bar D_i b is in L^2(mu) for b in W^{1,2}, and with F_i b in L^2
the right-hand vector is in L^2(mu). Both sides are then continuous in a
for the W^{1,2} norm, and Claim 4 supplies C_c^infty approximants of a.
No product of two unbounded functions is estimated against d chi_n.

Promotion check: the statement is a pairwise identity for a in W^{1,2},
b in W^{1,2} with F_i b in L^2. It is not an operator-domain equality,
not an adjoint computation on the maximal domain of D_i, and does not
cover a with only D_i a in L^2. The report says so at lines 30-32 and
208-210. Not silently promoted.

### 6. Positive control and the rational e=2 control: CONFIRMED

Identity map: h=1, U=C^2, Z empty, N=1, chi_n=theta_n, the classical
Gaussian cutoff. Rational control G(s,y)=(s^2, y/(2s)): Jacobian
determinant (2s)(1/(2s)) - 0 = 1; two preimages (s=+-sqrt u, y=2sv);
in (s,v) coordinates the map is (s^2,v), so dmu = |2s|^2 exp(-|s|^4-|v|^2)
dA(s)dA(v) = 4|s|^2 exp(...) and D_u = (1/(2s)) d/ds at fixed v. Checked.
b=1/s: |b|^2 dmu has radial factor r^{-2} r^2 r dr = r dr near 0, finite.
D_u b = -1/(2 s^3): radial factor r^{-6} r^2 r dr = r^{-3} dr, divergent.
Total mass 4 integral |s|^2 exp(-|s|^4) dA times pi = 2 pi^2 = N pi^2 with
N=2, consistent with Claim 1. No contradiction: b is holomorphic and in
L^2 but not in W^{1,2}, so neither the density claim nor the scoped
identity applies to it; it shows the holomorphic first-order domain is
strictly smaller than holomorphic L^2. Not a whole-plane polynomial
Keller counterexample: G has the factor 1/s and is defined on C* x C.

## Scope judgement

The result precisely narrows the old real first-order cutoff gap: on an
actual polynomial Keller source with its pulled-back Gaussian measure,
C_c^infty is dense in the full real W^{1,2} and the scoped Gaussian
integration identity holds, without global properness or completeness.
The larger gap stays intact and is correctly disclaimed: density inside
the holomorphic subspace, a holomorphic compact core, maximal-domain
equalities, strong commutation, common domains under repeated lifted
derivatives, and integrability of arbitrary source polynomials are neither
proved nor implied, and the e=2 control shows the first cannot follow
from finite-energy cutoffs alone. No novelty claim is made or endorsed.

FALLACY-v2 check: no exit claim, no charge_basis line needed; no pole or
floor/attainment reasoning is used; ring identifications (A inside B,
B_h = A_h[x,y]) are explicit. No OPEN raised by the report or by me.

Recommendation: promotable at the stated scope (Claims 1-3 of the frozen
report, evidence tier MANUAL/PROVED-elementary), subject to ROOT's
administrative collision check.

<!-- REVIEW-MATH-END -->

## OPENS RAISED

None. The retained holomorphic/operator-domain problem is not a new
descendant or a new named open.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13307`.
- Body SHA-256:
  `4325105e7e9be2facb797e6e52269a0a29ab442dd0884ca599869b826e2bab4b`.
- Frozen basis: `0ad11f45906b4647ea3d4b2b054b20f3de90639d`.
