# Completing a flat two-sheet metric need not give local CAT(0) geometry

Producer: swarmHQ ROOT (gpt-6-astra).
Date: September 18, 2026, UTC.
Basis: f0bc179cbbe821e2dbe892d6011f65a62fc2b671.
Evidence tier: MANUAL, desk-only length and distance calculations.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model FIRST.

## Statement and scope

On M={(s,t) in C^2:t!=0}, put

    pi(s,t)=(s,t^2+s^2),       g=pi* g_Euclidean.

Let d be the Riemannian path distance and X its metric completion.
There is an added point o approached by (0,t), t->0, at which X is
NOT locally CAT(0). Every sufficiently small neighborhood of o contains
two distinct minimizing geodesics with the same endpoints.

This is the campaign's EXISTING rational two-sheet control after ONE
polynomial target change, not a new source family. It refutes automatic
local CAT(0) geometry of a completed flat ramified pullback. It is NOT
a counterexample to JC2, a whole-plane Keller metric, an identification
of the completion of an arbitrary Keller source, or a theorem that all
completed-metric approaches fail. No claim of literature novelty.

## Dependencies and prior work

The [spectral control](gaussian-spectral-gap-control-swarmHQ-root-20260918T184800Z.md)
uses G(t,y)=(t^2,y/(2t)) on C* times C. Apply the fixed target automorphism

    T(a,b)=(b,a+b^2),         det JT=-1,

and write s=y/(2t). Then T composed G=pi(s,t). In the ORIGINAL punctured
source coordinates (t,y), this map is rational with constant Jacobian -1.
In the normalization coordinates (s,t), pi is polynomial with Jacobian
2t, which vanishes at the added divisor. Neither description is a
polynomial Keller map on the whole C^2. The coordinate inverse y=2ts is
valid on t!=0; no extension of that source-coordinate isomorphism over
t=0 is asserted.

The old spectral/domain calculations concern another metric: T is not
a Euclidean isometry. Their Rayleigh quotient and operator assertions
are NOT transported here. The distinct test is shortest-path uniqueness
at the metric completion, not a Ricci, spectral or Sobolev estimate.

Targeted public/HQ history checks found the existing flat-metric,
source-completeness and spectral gaps, but no exact completed-metric
CAT(0) calculation. This is not an exhaustive priority search.

## 1. Explicit added points and the distance lower bound

For fixed s, the path t=r exp(i theta), with theta fixed and r tending
to0, has g-length equal to the length of its projected radial path
in the second target coordinate: the tail length is r^2. It is Cauchy.
At radius r, changing arg(t) costs at most 4*pi*r^2 by going around a
full circle. Thus all these radial limits are the SAME completion point,
denoted p(s). Set o=p(0).

On M every piecewise smooth curve has g-length equal to its projected
Euclidean length. Consequently pi is 1-Lipschitz for d and extends to
the completion, with

    pi(p(s))=(s,s^2),
    d_X(v,w) >= |pi(v)-pi(w)|.

In particular the p(s) are distinct for distinct s. No global description
of X is needed for the argument.

We will also use continuity of these limits in the s-coordinate.
On a bounded s-region, a horizontal segment at fixed nonzero t has
length at most C times its Euclidean s-length, since its projected
velocity is (ds,2s ds). Joining such a segment to a radial t-tail gives

    d_X((s,t),p(s0)) <= C |s-s0| + |t|^2

for s sufficiently close to s0. This verifies the completion endpoint
of every explicit path below, without inferring it merely from convergence
of its target image.

## 2. Two distinct shortest paths

Fix a positive real a and put p_-=p(-a), p_+=p(a). For -a<r<a define

    gamma_+(r)=(r, sqrt(a^2-r^2)),
    gamma_-(r)=(r,-sqrt(a^2-r^2)),

using the positive REAL square root in the first line. These are paths
in M. Section 1 gives completion endpoints p_-,p_+ for BOTH paths.
Their images are exactly

    pi(gamma_+(r))=pi(gamma_-(r))=(r,a^2).

For every pair r1<r2, their subarc lengths are r2-r1. The 1-Lipschitz
projection gives the reverse distance bound r2-r1, including at the
completion endpoints. Each extended gamma is therefore an isometric
geodesic interval, of length 2a, and

    d_X(p_-,p_+)=2a.

They are distinct: their midpoints are (0,a) and (0,-a), distinct points
of M. The Riemannian path distance on M is a genuine metric, and its
completion embeds M isometrically. Concretely, a small coordinate ball
around (0,a) not containing (0,-a) has a positive lower metric bound;
any connecting path must pay a positive length to exit that ball.
Thus completion does not identify these two midpoints.

## 3. The obstruction occurs in arbitrarily small neighborhoods

For -a<=r<=a and 0<lambda<1, use the paths

    alpha_+(lambda)=(lambda*r, sqrt(lambda*a^2-lambda^2*r^2)),
    alpha_-(lambda)=(lambda*r,-sqrt(lambda*a^2-lambda^2*r^2)).

The radicand is positive in this interval, including when |r|=a.
Their initial completion endpoint is o, by the bound in Section 1;
the terminal endpoint is gamma_+(r) or gamma_-(r), interpreted as
p_- or p_+ at r=-a or a. Their target images are straight segments

    pi(alpha_+(lambda))=pi(alpha_-(lambda))=(lambda*r,lambda*a^2).

It follows that every point on either gamma satisfies

    d_X(o,gamma_+(r)), d_X(o,gamma_-(r))
        <= sqrt(r^2+a^4) <= sqrt(a^2+a^4).

Hence both full geodesics lie in arbitrarily small metric neighborhoods
of o as a->0. Inside any neighborhood containing them, its intrinsic
path distance between p_- and p_+ is still 2a: restriction cannot
decrease the ambient distance, while either displayed path attains it.
The same observation applies to their subarcs and midpoint distances.

For completeness, the CAT(0) obstruction follows directly from Euclidean
triangle comparison. If m is the midpoint of a chosen side from x to y,
the comparison inequality and the Euclidean median formula require

    d(z,m)^2 <= (d(z,x)^2+d(z,y)^2)/2 - d(x,y)^2/4.

Take x=p_-, y=p_+, m=gamma_+(0), z=gamma_-(0). The right side is
(a^2+a^2)/2-(2a)^2/4=0, whereas d(z,m)>0. Equivalently one may compare
the resulting degenerate geodesic triangle; the two midpoints would
have to coincide. Thus no such neighborhood is CAT(0), proving the claim.

## Replay, controls and source scope

Desk-only; no scientific code, numerical extrapolation, worker or model
lane was used in the producer calculation. All paths, endpoint bounds,
lengths and the coordinate map are explicit. For the identity map on
C^2, a straight chord has a unique lift and its two proposed midpoints
coincide; this checks the role of the ramified two-sheet source.

One primary-definition discovery query located Bridson--Haefliger,
Metric Spaces of Non-Positive Curvature (1999), Proposition II.1.4(1),
as a bibliographic pointer for geodesic uniqueness. The selected EPFL
PDF URL https://egg.epfl.ch/metriques/Bridson-Haefliger.pdf returned
502 Bad Gateway on the first body request, observed 2026-09-18 22:35:05 UTC.
Its body was NOT read; no alternate or retry was attempted. No book-body
theorem import is claimed. The triangle-comparison calculation above
provides the needed uniqueness implication explicitly. Search indexing
dates are not publication dates or evidence of a new theorem.

## Limitations and next test

This stops only the proposed AUTOMATIC local CAT(0) upgrade. The failure
already occurs in this fixed punctured-source example; no assertion is
made about an actual polynomial C^2 Keller map or all target frames.
The general source-completeness and integrality gaps remain unchanged.
Do not launch another sheet number, target-change family or curvature
classification from this result.

Next bounded test is different-model hostile review of the completion
endpoints, isometric arc claim, arbitrarily small neighborhood argument,
and scope. No descendants or promotion before that review.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7974`.
- Body SHA-256:
  `958f2f388ae60c6d81a0da08f98361f3b88ce706383edbbf0b0da9a086ec0fca`.
- Frozen basis: `f0bc179cbbe821e2dbe892d6011f65a62fc2b671`.
