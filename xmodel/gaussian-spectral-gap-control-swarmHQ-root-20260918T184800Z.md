# A first-order Gaussian core does not supply the curvature spectral gap

Producer: swarmHQ ROOT (gpt-6-astra).
Date: September 18, 2026, UTC.
Basis: ed5b98bdc06ab5e2c4839a37c0b226869709b863.
Evidence tier: MANUAL, desk-only, explicit real differential and integral calculations.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.

## Statement and scope

On the EXISTING rational control

    M=C* times C,   G(s,y)=(s^2,y/(2s)),
    g=G* g_Eucl,   phi=|G|^2,   dmu=e^(-phi) dvol_g,

the following statements hold, with FULL REAL gradient conventions.

1. The metric is flat and Ric_g+Hess_g(phi)=2g pointwise. The measure
   is finite. There are source-compact smooth cutoffs approaching1 with
   energy tending to0, and C_c^infty(M) is dense in full real W^{1,2}(mu).
2. The smooth real function u(s,y)=Re(s) has mean0, belongs to W^{1,2},
   and satisfies

       integral |du|_g^2 dmu = integral u^2 dmu = pi^(5/2)/2.

   Consequently the gap2 inequality

       integral (f-mean_mu f)^2 dmu <= (1/2) integral |df|_g^2 dmu

   is FALSE for this space, even with the first-order core in Claim1.
   The infimum of mean-zero Rayleigh quotients is at most1; no exact
   spectral-bottom classification is asserted.
3. For the self-adjoint nonnegative operator A associated to the full-real
   closed Dirichlet form E(f,h)=integral <df,dh>_g dmu, u is in its domain
   and Au=u. Nevertheless integral |Hess_g u|_g^2 dmu=infinity.

This is a counterexample to an inference from these ANALYTIC premises,
not to JC2 and not to a Poincare estimate proved with additional actual-
polynomial-C2 hypotheses. M is not C2, and G is rational in (s,y).
No actual Keller metric is asserted incomplete or to have this spectrum.

## Dependencies and prior work

[The Gaussian cutoff report](gaussian-sobolev-cutoffs-swarmHQ-root-20260918T181400Z.md)
already records this EXACT G, its measure, the applicable cutoff construction,
and s^-1 in holomorphic L2 with lifted derivative outside L2. Its reviewed
real first-order core result does not assert a spectral estimate. The present
test uses Re(s), which DOES have finite first-order energy, and computes
the failing constant and the missing second-order integrability explicitly.
No new control family is introduced and no literature novelty is claimed.

The proof below is self-contained apart from local Sobolev mollification,
bounded truncation, and the standard definition of the operator associated
to a closed nonnegative quadratic form. It does not invoke a global
curvature-to-spectral-gap theorem or any JC2 foundational theorem.

## 1. Geometry, finite mass and the real first-order core

Use the global holomorphic coordinates (s,v) with v=y/(2s) on M. Then

    G(s,v)=(s^2,v),
    g=4|s|^2 |ds|^2+|dv|^2,
    phi=|s|^4+|v|^2,
    dmu=4|s|^2 exp(-|s|^4-|v|^2) dA(s)dA(v).

Here |ds|^2 means da^2+db^2 for s=a+ib, with the analogous convention
for v. G is a local isometry to the punctured Euclidean target. Thus
Ric_g=0 and Hess_g(phi)=2g follow by pulling back the local Euclidean
identities. Its degree is2 over {z_1!=0}, so mu(M)=2*pi^2; the same
value follows by radial integration.

For an explicit inner cutoff let eta_epsilon(s) vanish on |s|<=epsilon^2,
equal1 on |s|>=epsilon, and have derivative bounded by
C/(|s|*|log epsilon|) in between, using a smooth profile in log|s|.
The factor 4|s|^2 cancels between the inverse metric and the measure in
the s-gradient energy. Hence

    integral |d eta_epsilon|_g^2 dmu
       <= C' / |log epsilon| ->0.

Let theta_R(z_1,z_2) be a standard target cutoff, equal1 in B_R,
supported in B_2R, with Euclidean gradient <=C/R. Its pullback has
energy at most 2*C^2*pi^2/R^2. The product

    chi=eta_epsilon(s) * theta_R(s^2,v)

has compact support in M: s is bounded above and bounded away from0,
and v is bounded. The product-gradient inequality bounds its energy by
twice the sum of those two vanishing energies. Take epsilon->0 and R->infinity
to obtain 0<=chi_n<=1 tending pointwise to1 with energy tending to0.

For bounded f in full-real W^{1,2}, chi_n f tends to f in that norm:
dominated convergence handles (1-chi_n)f and (1-chi_n)df, while
||f dchi_n||_2 <= ||f||_infinity ||dchi_n||_2. For general real f, first
use bounded Lipschitz truncations converging in W^{1,2}. On each compact
support the coefficients and measure are smooth positive, so ordinary
local mollification gives C_c^infty approximation. This proves Claim1
without asserting a second-order or holomorphic core.

## 2. The exact Rayleigh quotient

The angular integral of u=Re(s) is zero; u is integrable, so mean_mu u=0.
Writing s=r exp(i theta), the real metric gives

    |du|_g^2 = 1/(4r^2).

Since integral_C exp(-|v|^2)dA(v)=pi,

    E(u,u) = 2*pi^2 integral_0^infinity r exp(-r^4) dr
           = pi^(5/2)/2,

    ||u||_2^2 = 4*pi^2 integral_0^infinity r^5 exp(-r^4) dr
              = pi^(5/2)/2.

The substitutions t=r^2 in the first integral and t=r^4 in the second
give the displayed constants (Gamma(3/2)=sqrt(pi)/2). These finite
integrals establish W^{1,2} membership directly. Dividing either by
mu(M)=2*pi^2 gives sqrt(pi)/4 for the normalized energy and variance.
The proposed factor1/2 would require a positive number to be at most
half itself. This proves Claim2.

## 3. Weak eigenfunction versus missing Hessian integrability

Define the local weighted Laplacian L=Delta_g-<dphi,d->_g. In (s,v)
coordinates, Delta_g u=0. The s-part of grad_g phi is
a partial_a+b partial_b, so Lu=-u. Integration against compactly
supported smooth f therefore gives

    E(u,f)=integral u f dmu.

Both sides are continuous in the W^{1,2} norm, and Claim1 makes compact
tests dense. The identity thus holds for every f in the full form domain.
By the defining characterization of its associated operator, u belongs
to Dom(A) and Au=u. No claim of essential self-adjointness of the
compactly supported differential operator is made.

On a local target branch put z=s^2. Then u=Re(z^(1/2)), whose holomorphic
second derivative is -1/(4 z^(3/2)). For the real Hessian in the z-plane,

    |Hess_g u|_g^2 = 2*| -1/(4 z^(3/2)) |^2 = 1/(8|z|^3).

On any bounded v-region of positive area, each target sheet therefore
has Hessian integral near z=0 proportional to

    integral_0^delta rho^(-3) * rho d rho = infinity.

Thus the form core and Lu in L2 do not supply the global second-order
identity needed to integrate the pointwise curvature calculation with u.
There is no contradiction with that local calculation.

## Replay and controls

Desk-only. All displayed integrals and derivatives are explicit; no CAS,
worker, numerical approximation or source import is used. The standard
Euclidean Gaussian identity-map control with f=Re(z_1) has Rayleigh
quotient2 instead of1, checking the REAL gradient and variance convention.
The old s^-1 control tests a different domain issue and is not reused as
a proof of holomorphic nondensity.

## Limitations and next test

This closes only the proposed implication from a real first-order core
and pointwise Gaussian curvature to the gap2 estimate. It supplies no
spectral conclusion for an actual polynomial Keller map on C2. Any such
route must add a valid global-domain argument or a specifically C2
constraint. No new family, higher-sheet calculation, density theorem,
completeness search or actual-source spectral claim follows automatically.
Different-model review of these three exact claims is the next bounded test.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7607`.
- Body SHA-256:
  `10aea0d7888dd1b55f6f87c258a9bbeee404c7153106138c7d45afaf0cd4e26f`.
- Frozen basis: `ed5b98bdc06ab5e2c4839a37c0b226869709b863`.
