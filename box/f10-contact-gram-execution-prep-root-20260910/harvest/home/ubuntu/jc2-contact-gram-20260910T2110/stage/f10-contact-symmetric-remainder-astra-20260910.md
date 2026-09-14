# Symmetric common-quadratic contacts: exact equations and exceptional points

2026-09-10. Astra producer, UNREVIEWED. First action 00:53:18 UTC;
fixed stop 01:08:18 UTC; publication reserve starts 01:06:18 UTC.
Manual mathematics only. No mathematical subprocess or coefficient artifact.

## 1. Outcome and charged scope

The symmetric representation and its finite-free etale rank-two ordered
cover are valid with the ENTIRE stated guard. The divisor V=1/3 is solved
scheme-theoretically: W=1/27 and there are exactly three reduced rational
symmetric points, or six ordered points. Thus the whole complex guarded
locus is NONEMPTY. None of those points is in 5/3<x<y<2.

Whole-locus finiteness remains GAP on V!=1/3. No positive-dimensional
component is exhibited. Section 5 gives the precise remaining elimination
predicate for the four explicit equations; no generic count or resultant
nonvanishing is asserted.

Exactly three inputs were SHA256-pinned before use:

- box/f10-contact-symmetric-remainder-prep-20260910/ROOT-CARD.md:
  59b8311aec88528b17ba3a73ebf0147f8d230e1d141373bfd2cd1442bca905f4.
- xmodel/f10-two-exponent-contact-discriminator-astra-20260909.md:
  4bbecd357077b422fbe636de61c9feefc5b304d88eea0a872b476456b1fbdf30.
- xmodel/f10-two-exponent-contact-gate-fable5-20260909.md:
  4a46e7f605759016829fcfb8ad92586fa9ebe875c4b5a62835b603c8b0ab1e90.

The new card was read WHOLE after its hash check. The parents' current
hashes matched the earlier WHOLE reads, expressly authorized for same-byte
reuse. The qualified accepted17w formulas alone are premises: the gate's
incidental e_y Cramer sign is positive, and u-normalization is a field-point
fact or explicit u-unit chart. No unreviewed September10 result, previous
geometry bound, linked provenance, or live report/code is a premise.

## 2. Literal quartics and the exact four small equations

Put a(X)=720A_X and b(X)=5040B_X. From the literal accepted17w formulas,

    a(X)=X^4+a3 X^3+a2 X^2+a1 X+a0,
    a3=30V-14,
    a2=71-270V+180V^2+120W,
    a1=-154+780V-900V^2+120V^3-600W+720VW,
    a0=120-720V+1080V^2-240V^3+720W-1440VW+360W^2;

    b(X)=X^4+b3 X^3+b2 X^2+b1 X+b0,
    b3=42V-18,
    b2=119-504V+420V^2+210W,
    b1=-342+1974V-2940V^2+840V^3-1470W+2520VW,
    b0=360-2520V+5040V^2-2520V^3
       +2520W-7560VW+2520V^2W+2520W^2.

These are hand expansions, not machine-generated coefficient files.
For example the scalar factors of a are
(X-2)(X-3)(X-4)(X-5) and 30V(X-2)(X-3)(X-4);
those of b are (X-3)(X-4)(X-5)(X-6) and
42V(X-3)(X-4)(X-5). They give respectively the displayed -14,-18
and 30V,42V cubic coefficients, verifying the card's suggestion.

Let q(X)=X^2-sX+p. Its monic reductions, valid over every Q-algebra, are

    X^2=sX-p,
    X^3=(s^2-p)X-sp,
    X^4=(s^3-2sp)X+(p^2-s^2p).

The four remainder equations are exactly

    F_a1=s^3-2sp+a3(s^2-p)+a2*s+a1=0,
    F_a0=p^2-s^2p-a3*s*p-a2*p+a0=0,
    F_b1=s^3-2sp+b3(s^2-p)+b2*s+b1=0,
    F_b0=p^2-s^2p-b3*s*p-b2*p+b0=0.             (1)

No leading coefficient is inverted in (1); their coefficients are the
literal small polynomials displayed above. In particular the formula is
defined at V=1/3 and at every further Euclidean/subresultant exceptional
divisor. Define

    Delta=s^2-4p,
    Gamma=36p+9s^2-114s+181,
    Omega=15s^2-36p-30s+35,
    G=W*p*(p-s+1)*(9p-15s+25)*(p-2s+4)*Delta
      *(s-3)*(4-s)*Gamma*Omega,
    R=Q[s,p,V,W,G^-1]/(F_a1,F_a0,F_b1,F_b0).

## 3. Whole-ring maps, guards, and nilpotents

Let C be the ROOT-CARD ordered ring
Q[x,y,V,W,H^-1]/(A_x,B_x,A_y,B_y). There is an exact isomorphism

    C ~= R[x]/(x^2-sx+p),             y=s-x.     (2)

In one direction send s to x+y and p to xy. Put d=y-x. Direct multiplication
gives p=xy, p-s+1=(x-1)(y-1),
9p-15s+25=(3x-5)(3y-5), p-2s+4=(2-x)(2-y),
Delta=d^2 and G=dH. Thus either ring's guard inverts exactly the required
factors of the other ring; no divisor or W=0 point is silently restored.

For the equation read-back, write a(X)=q(X)h(X)+F_a1 X+F_a0.
Evaluation at x,y gives a(x),a(y). Conversely, if both evaluations vanish,
their difference is (x-y)F_a1=0. The guard makes x-y a unit, so F_a1=0
and then F_a0=0. The identical argument treats b, and 720,5040 are units.
This proves both directions of (2) in arbitrary coefficient rings, with
nilpotents retained, not just at field points.

The algebra on the right of (2) is free of rank two over R. Its derivative
2x-s=x-y is a unit since (2x-s)^2=Delta, so it is etale and faithfully
finite over R. Accordingly emptiness and total Krull dimension agree
between R and C. A zero-dimensional conclusion for either would still
require exclusion of prescribed rational/integer specializations.

## 4. The entire V=1/3 divisor: exactly three symmetric points

The difference a-b has cubic coefficient 4-12V, as suggested. At V=1/3
the ENTIRE difference simplifies by hand to

    a(X)-b(X)=(10/3)(1-27W)
              *[X^2-3X+4/3+24W].              (3)

For a direct coefficient check, its quadratic, linear and constant terms
at V=1/3 are respectively

    10/3-90W,
    -10+270W,
    40/9-40W-2160W^2
       =(40/9)(1-27W)(1+18W).

Reducing (3) modulo q gives the linear coefficient
(10/3)(1-27W)(s-3). Since s-3 is an EXISTING factor of G, it is a unit.
Therefore R/(3V-1) forces W=1/27 as an exact ideal consequence, without
inverting 1-27W or discarding its zero locus.

At V=1/3,W=1/27 the common monic quartic is

    a(X)=b(X)
      =(X-1/3)(X-2/3)(X-4/3)(X-5/3)
      =X^4-4X^3+(49/9)X^2-(26/9)X+40/81.      (4)

The guard removes the root 5/3 and the diagonal. Every other factor of
the guard survives exactly the following three unordered choices:

| {x,y} | s | p | Gamma | Omega |
|---|---:|---:|---:|---:|
| {1/3,2/3} | 1 | 2/9 | 84 | 12 |
| {1/3,4/3} | 5/3 | 4/9 | 32 | 32/3 |
| {2/3,4/3} | 2 | 8/9 | 21 | 3 |

Here W=1/27; no remaining root is 0,1,5/3 or 2, the roots are distinct,
and none of the displayed sums is 3 or 4. This verifies ALL factors of G,
not only Gamma and Omega. These points prove R and C are nonzero.

They exhaust this divisor scheme-theoretically. Indeed (4) is split and
squarefree. The ordered ring obtained from a(x)=a(y)=0 is initially a
product of sixteen copies of Q. The guard retains exactly the six ordered
distinct pairs among the three surviving roots. Hence

    C/(3V-1) ~= Q^6,             R/(3V-1) ~= Q^3.          (5)

For the second equality, the involution exchanging x,y pairs the six
factors. The invariant subring of the quadratic algebra (2) is precisely
R: invariance of u+v*x implies v(2x-s)=0 and thus v=0. This remains valid
after taking the quotient. Thus no nilpotent multiplicity is being hidden
in (5). None of these six ordered exponent pairs meets 5/3<x<y<2.
This describes the closed slice only: it does not prove that these points
are isolated in the full R, or prevent a curve from meeting this slice.

## 5. Exact remaining GAP and controls

Set T=Q[s,p,V,W], F=(F_a1,F_a0,F_b1,F_b0), and

    I=F : [G*(3V-1)]^infinity in T.                      (6)

The unresolved generic-chart question is whether

    T[(G*(3V-1))^-1]/F

is zero or zero-dimensional. Together with the fully solved divisor (5),
this is equivalent to whole-locus finiteness. This saturated ideal is
specified by the literal four equations (1), not by an uncomputed asserted
eliminant. A concrete equivalent elimination predicate is

    I intersect Q[V] contains a nonzero polynomial,
    I intersect Q[W] contains a nonzero polynomial.       (7)

To justify equivalence: such polynomials bound V,W algebraically at every
prime of the localized ring; x,y then satisfy the monic quartic a, and
s=x+y,p=xy are algebraic too, so every component has dimension zero.
Conversely a zero-dimensional finite-type Q-algebra is finite-dimensional;
V and W satisfy nonzero univariate annihilators, whose cleared localizing
powers put them in the saturation (6). This also includes the zero ring.
Neither membership/nonvanishing statement in (7) is established here.

No further leading coefficient was inverted. Thus a possible vanishing
quadratic or linear Euclidean remainder has been RETAINED in (1), not
silently dropped; its dimension verdict is part of (6)-(7). The cubic
leading factor 3V-1 is the only additional chart split, and its full closed
divisor was handled in section 4. No generic Euclidean calculation is
promoted across an exceptional divisor.

Changed-object controls: without the factor s-3, equation (3) would not
force W=1/27; its linear remainder can vanish on s=3. Without Delta, two
field evaluations at x=y would repeat one row and would not force the
linear remainder to vanish; the difference-unit step in (2) is essential.
Replacing nonempty finite points (5) by a claim of a curve is equally
invalid. These controls explain the exact guard and the remaining limit.

Verdict: whole complex EMPTINESS REFUTED by exact guarded rational points;
V=1/3 divisor fully solved; whole complex FINITENESS remains GAP at (7).
No positive-dimensional countercomponent, prescribed-locus exclusion,
late-source forcing/companion closure or JC2 conclusion is asserted.

## OPEN(S) RAISED

- ASSIGNED GAP ONLY; no new canonical ID: prove or refute (7) for the
  exact saturated four-equation ideal (6). No follow-on coefficient work,
  subresultant computation, runtime, or task is authorized by this report.

## COLLISIONS

status: EMPTY

- Own assigned report and box were ABSENT at the first action. No corpus,
  historical, live-body, linked-provenance or shared-file scan occurred.

The own WHOLE report/PINS and own-only OPEN/collision extraction were
checked at 01:00:08 UTC. The completion edit records that check and clarifies
that a reduced closed slice does not imply isolation in the full scheme.
All mathematics was manual; no mathematical subprocess ANY size, code or
coefficient artifact, network, AWS, SSH, process inspection, new agent,
Git/shared/protected work, or external follow-on occurred. Only own
apply_patch documentary writes and the existing publication transaction
were used. Root retains custody checks and any first different-model gate;
this producer gives no promotion authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10155`.
- Body SHA-256:
  `ef41e886fe433cac9fc780bb46390b5922838ffcec3ec7cd35e7fd00ef47b2f8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
