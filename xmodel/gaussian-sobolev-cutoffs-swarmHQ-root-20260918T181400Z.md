# Gaussian finite-energy cutoffs for a polynomial Keller source

Producer: swarmHQ ROOT (gpt-6-astra); native Astra same-model co-check.
Date: September 18, 2026, UTC.
Basis: 8c1a455646e71e7068124a6f47bcdf6f4597378a.
Evidence tier: MANUAL, desk-only; elementary algebraic and analytic facts stated below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.

## Statement and scope

Let F=(F_1,F_2):C^2 -> C^2 be a polynomial map with nonzero constant
complex Jacobian. Let N=[C(x,y):C(F_1,F_2)], put g=F^*g_Eucl on the real
four-dimensional source, and put dmu=exp(-|F|^2)dvol_g. Define W^{1,2}
using the FULL REAL weak differential and norm

    ||u||_W^2 = integral (|u|^2+|du|_g^2) dmu.

The same notation applies to complex-valued functions by taking their real
and imaginary parts.

1. There are chi_n in C_c^infty(C^2;[0,1]) tending to1 almost everywhere,
   with integral |dchi_n|_g^2 dmu ->0. The total mass is N*pi^2.
2. C_c^infty is dense in this precise W^{1,2} space.
3. Let D_i be the lift of complex differentiation partial/partial z_i
   from the target, and let bar D_i be its conjugate. If a,b are in this
   W^{1,2} and F_i b is in L^2(mu), then, with inner product linear in
   its first argument,

       <D_i a,b> = <a,-bar D_i b+F_i b>.

   For holomorphic b the bar D_i term vanishes. This is a scoped
   integration identity, not a determination of every maximal operator domain.

No completeness, polynomial inverse, strong commutation, holomorphic compact
core, higher-order domain equality, or integrability of arbitrary source
polynomials is asserted. These claims do not resolve JC2.

## Dependencies and prior work

The September13 14:27 entry in notes.md (basis above, lines39908--39962)
records the Gaussian adjoint/core/boundary-flux gap: naive source cutoffs
have growing lifted-derivative coefficients, and target cutoffs need not
be source-compact. The September13 18:34 calculation already gives the
finite-degree target-sublevel volume identity; that identity is not new here.

The new step is to remove an arbitrarily small-energy neighborhood of a
target algebraic curve BEFORE pulling back. Finiteness over its complement
makes the pulled-back support compact in the actual source. This settles
the real first-order Sobolev cutoff issue, not the entire holomorphic
operator-domain problem recorded in the old entry.

The proof uses monic algebraic equations, smooth normal-coordinate charts,
the change-of-variables formula, the weak Sobolev chain/product rules and
local mollification on compact sets. It imports no specialized JC2,
completeness, stochastic, or weighted-operator theorem. The newly screened
arXiv:2602.01016v4 is NOT a dependency. No literature novelty claim is made.

## 1. A genuine finite covering off one algebraic curve

Identify A=C[z_1,z_2] with C[F_1,F_2] inside B=C[x,y]. Nonzero Jacobian
gives algebraic independence of F_1,F_2 and a finite function-field
extension of degree N. Clear denominators in monic equations for x and y
over Frac(A): there is a nonzero h in A such that x,y are integral over
A_h. Thus B_h=A_h[x,y] is finite over A_h. The Jacobian condition makes
the resulting map over U={h!=0} finite etale, with N sheets.

For clarity, properness here is only over U. If K is a compact subset of U,
the coefficients of these monic equations are uniformly bounded on K.
The elementary root bound bounds both x and y on F^{-1}(K). This preimage
is also closed in C^2, hence compact. No global properness has been used.

Replace h by the product of its distinct irreducible factors without
changing U. Write Z={h=0}; Z is a reduced affine complex algebraic curve
(or empty) with a finite singular set. The preimage F^{-1}(Z) is the zero
set of a nonzero polynomial and has real measure zero.

Since F is a local isometry for g, finite-cover change of variables gives

    integral_source a(F) dmu = N integral_U a(z) exp(-|z|^2) dz

for nonnegative measurable a. The omitted zero sets have measure zero,
so taking a=1 gives mu(C^2)=N*pi^2.

## 2. Small-energy removal of Z on a target compact

Fix a radius R, a distance tolerance delta>0 and an energy tolerance tau>0.
There is a smooth eta:C^2->[0,1] which vanishes on a neighborhood of
Z intersect closed B_R, equals1 outside the delta-neighborhood of Z,
and satisfies integral |deta|^2 dz < tau. Its derivative is compactly
supported. Here is the elementary critical-codimension construction.

First cover the finitely many singular points meeting the target compact
by very small balls, using smooth cutoffs rho_sing equal to1 on smaller
balls. In real dimension4, a rescaled fixed bump of radius r has gradient
L^2 norm O(r). Choose the balls inside the delta-neighborhood of Z and
make their combined gradient norm smaller than sqrt(tau)/2.

The portion of Z intersect closed B_R outside those inner balls is a
compact subset of the smooth locus. Cover it by finitely many relatively
compact normal-coordinate charts, with tangential cutoffs equal to1 on
smaller patches covering that compact set. In each chart use normal radius
r in the two-dimensional normal disk and a smooth profile q_epsilon:
equal to1 for r<=epsilon^2, equal to0 for r>=epsilon, and satisfying

    |q_epsilon'(r)| <= C/(r*|log epsilon|)

in between. Such a profile is obtained by smoothing a fixed cutoff of
log(r)/log(epsilon). Its normal energy is O(1/|log epsilon|), and its
normal L^2 mass tends to0. Multiplication by the fixed tangential cutoff
adds a gradient term tending to0 as well. Smooth metric/volume distortion
is uniformly bounded on each chosen chart. Supports can be confined to
the delta-neighborhood of Z.

If the resulting number of charts is M>0, choose their epsilons after M is
known so that each chart cutoff rho_j has gradient norm less than
sqrt(tau)/(2M). For M=0 the product below is empty. Set
eta=(1-rho_sing)*product_j(1-rho_j). Since every factor
is in[0,1], the product rule and the L^2 triangle inequality give

    ||deta||_2 <= ||d rho_sing||_2 + sum_j ||d rho_j||_2 < sqrt(tau).

At every point of Z intersect closed B_R some factor vanishes throughout
a neighborhood. Thus eta has all the stated properties. This order of
choices avoids multiplying the singular-point energy by a chart count
that might grow when the singular balls shrink. If Z is empty, take eta=1.

## 3. Pullback cutoffs and their energy

Choose smooth theta_n in[0,1], equal to1 on B_n, compactly supported in
B_{2n}, and with |dtheta_n|<=C/n. Apply Section2 with R=2n,
delta=1/n and tau=1/n^2 to obtain eta_n. Put

    a_n=theta_n eta_n,             chi_n=a_n composed F.

The support of a_n is a compact subset of U: eta_n vanishes on a
neighborhood of Z intersect closed B_{2n}. Section1 therefore proves
chi_n belongs to C_c^infty of the WHOLE source. Every fixed z outside Z
has positive distance from Z, so a_n(z)=1 for all sufficiently large n.
This proves the claimed almost-everywhere convergence on the source.

The local-isometry and covering identities give exactly

    integral |dchi_n|_g^2 dmu
      = N integral_U |d(theta_n eta_n)|^2 exp(-|z|^2) dz
      <= 2N C^2*pi^2/n^2 + 2N/n^2 ->0.

Dominated convergence and finite mu also give chi_n->1 in L^2(mu).

## 4. Density in the full real first-order space

For u in W^{1,2}, bounded Lipschitz truncations converge to u in W^{1,2}.
For complex u, truncate real and imaginary parts separately. This follows
from the weak chain rule and dominated convergence for u and du.

For a fixed bounded truncation v, multiplication by chi_n yields compactly
supported W^{1,2} functions converging to v. Indeed, dominated convergence
handles (1-chi_n)v and (1-chi_n)dv, while

    ||v dchi_n||_{L^2(mu,g)} <= ||v||_infinity ||dchi_n||_{L^2(mu,g)} ->0.

Every compactly supported W^{1,2} function can be approximated by compactly
supported smooth functions using a finite chart cover and local mollifiers.
On that compact neighborhood the smooth positive metric and weight are
uniformly comparable with Euclidean ones. Diagonalizing these three
approximations proves Claim2. No holomorphic approximants are asserted.

## 5. The precise integration identity

In target local coordinates, the Gaussian compact-test formal adjoint of
D_i is -bar D_i+F_i. This follows directly by differentiating exp(-|z|^2),
with D_i=partial/partial z_i. The same formula holds on source charts
because g and its volume are pulled back through the local biholomorphism.

For b in W^{1,2} with F_i b in L^2, the displayed adjoint expression is in
L^2, so its weak compact-test identity is defined. Approximate a in the
full real W^{1,2} norm by compactly supported smooth a_j using Section4.
Then D_i a_j->D_i a and a_j->a in L^2, allowing passage to the limit in
the identity. This proves Claim3 without estimating a product of two
unbounded functions against dchi_n. For holomorphic b, bar D_i b=0.

## Replay and negative controls

Desk-only. No CAS, floating-point computation or degree cutoff is used.
The identity map is the complete positive control (h=1, eta_n=1).

Use only the previously recorded rational control at e=2:

    G(s,y)=(s^2,y/(2s)) on C* times C.

It has Jacobian1 and is a two-sheeted covering of C* times C. In coordinates
v=y/(2s), its pullback Gaussian measure and lifted u-derivative are

    dmu=4|s|^2 exp(-|s|^4-|v|^2) dA(s)dA(v),
    D_u=(1/(2s)) partial_s at fixed v.

The same cutoff proof applies, but b=s^{-1} is holomorphic and in L^2(mu)
whereas D_u b=-1/(2s^3) is not in L^2. Near s=0 the respective radial
integrals are proportional to integral r dr and integral r^{-3} dr.
Thus a finite-energy cutoff does not put all holomorphic L^2 functions
in the first-order domain. This is NOT a whole-plane polynomial Keller
counterexample. No replacement control family is investigated.

## Limitations and next test

The old generic real first-order cutoff obstruction is removed under the
stated Keller hypotheses. Holomorphic subspace density, common domains
stable under repeated lifted derivatives, and any source-specific
integrability forcing degree1 remain unproved. Real C_c^infty density is
not a holomorphic core and does not imply strong commutation of unbounded
operators. Independent review of Claims1--3 and the control is the next
bounded test; no new analytic-family or completeness search is authorized
by this report.

## OPENS RAISED

None. The retained global domain/integrability problem is not relabeled
as a new scoped open or an automatic descendant.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10604`.
- Body SHA-256:
  `13204ce0986a9ad38eba05fa71f759aa307c66b7cafb9782ed8e28fcfdfd8451`.
- Frozen basis: `8c1a455646e71e7068124a6f47bcdf6f4597378a`.
