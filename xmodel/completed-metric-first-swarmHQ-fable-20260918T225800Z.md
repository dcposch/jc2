# Independent FIRST and corrections: completed-metric geodesic obstruction

Reviewer: Fable 5.1 (requested fable/max; hosted identity not independently attested).
Integrator: swarmHQ ROOT (gpt-6-astra), September 18, 2026.
Reviewed producer commit: 1b9fa5f66ed30afef9db45e7dd62e7ad4572712d.
Evidence tier: MANUAL, independent explicit length and comparison calculations.
Lifecycle: completed FIRST; promotion is recorded separately in AUDIT.md.

## Scope and custody

[Producer](completed-metric-geodesic-swarmHQ-root-20260918T223631Z.md),
full SHA256 a7b34f1bce50114f83d1a0d1b1e0afb909efef65dee1a2d6297c9dfdc8fca617.

For M={(s,t) in C^2:t!=0} and pi(s,t)=(s,t^2+s^2), the completion X of
the Riemannian path metric pi*Euclidean is not locally CAT(0) at the
added point o=p(0). Every neighborhood of o contains two distinct
minimizing geodesics with the same endpoints. This is a fixed rational
punctured-source control, NOT a polynomial Keller map on the whole C^2
and NOT a counterexample to JC2.

Fable read the producer, FALLACY-v2 and COORDINATION snapshots whole.
Reviewer pre/post pins and the terminal launcher receipt agree. ROOT
verified terminal supervisor, absent original processes and absent service
cgroup before receipt-first collection and whole report/log reads. The
receipt records DONE/exit0, CLEAN/BODY_SEALED and three unchanged inputs;
its end time is September18 22:56:07 UTC. The review records a measured
22:55:31 clock immediately BEFORE its final write, not a post-write
completion measurement. ROOT rehashed originals and execution components
against the receipt; temporary input snapshots had been removed by the
launcher's normal cleanup, so no independent post-termination snapshot
rehash is claimed.

Preserved terminal originals, unchanged after removing write bits:

- Review SHA256: ad12ab145fcbca84ec2384ca58512930a8738d8f1549b45c4a1123b3a5ae69eb
- Receipt SHA256: d976cb26e75e4583ff1fe2fcb125e044af9a889471a4cb2ac1ed95aa7590a9c2
- Log SHA256: b6bd1d7db0e868f4560135ecc8e0a5d35e96c8abc77f923eb7dc06a886cdc29a

The legacy report is a receipt-bound BODY-END body, not a canonical
post-body-sealed report. It is preserved without metadata repair. This
separate integration uses the canonical local publication lifecycle.
Nonmathematical delivery deviations are recorded in HQ's operational
journal; this mathematical verdict is not a certification of execution
protocol compliance. No charged-input drift was found.

The mathematical review below is ROOT's structured summary, not a
verbatim copy. It retains the reviewer's essential correction and excludes
one overbroad reviewer inference, explicitly identified below.

## Independent claim checks

1. Coordinate and metric scope — CONFIRMED. For
   G(t,y)=(t^2,y/(2t)), T(a,b)=(b,a+b^2), s=y/(2t), one has
   T composed G=pi(s,t). The original-coordinate determinant is -1;
   the normalization-coordinate determinant is 2t. T is not a Euclidean
   isometry, so prior spectral/operator conclusions do not transfer.
   The identification with the earlier campaign control is a contextual
   cross-reference; the new calculation needs only the displayed map.

2. Completion endpoints — CONFIRMED. At fixed s, a radial t-tail costs
   |t|^2; a full phase circle costs 4*pi*|t|^2. Thus the radial limits
   give one point p(s) independent of phase. The length identity makes
   pi 1-Lipschitz and extends it to X, with pi(p(s))=(s,s^2). On
   |s|,|s0|<=R the horizontal-plus-radial path gives

       d_X((s,t),p(s0)) <= sqrt(1+4R^2)|s-s0|+|t|^2.

   This proves convergence in the actual completion, not just in target
   coordinates. The image pi(M) misses the parabola, so p(s) is added.

3. Two isometric arcs — CONFIRMED. For real a>0,
   gamma_±(r)=(r,±sqrt(a^2-r^2)), -a<r<a, project to (r,a^2).
   Subarc lengths and projected distance lower bounds both equal
   |r2-r1|; the coordinate estimate supplies common endpoints p(-a),p(a).
   Both extend to isometric copies of [-a,a]. Their midpoints (0,a)
   and (0,-a) have positive distance: exiting a compact coordinate ball
   around the first costs a uniform positive length. The isometric
   embedding into the completion preserves that distance; equal target
   images do not identify the midpoints.

4. Arbitrarily small neighborhoods — CONFIRMED. For |r|<=a, the paths

       alpha_±(lambda)=(lambda*r,±sqrt(lambda*a^2-lambda^2*r^2))

   have positive radicand for 0<lambda<1 and project to
   (lambda*r,lambda*a^2). Their completion endpoints and lengths give
   d_X(o,gamma_±(r))<=sqrt(r^2+a^4)<=sqrt(a^2+a^4). Hence every
   neighborhood of o contains both full arcs for sufficiently small a.

5. Local CAT(0) failure — CONFIRMED with the convention clarification
   below. Both restricted and intrinsic neighborhood metrics work: all
   needed distances along the displayed arcs remain attained inside the
   neighborhood, while the midpoint separation stays positive.

6. Control and excluded conclusions — CONFIRMED at producer scope.
   A Euclidean identity-map chord has a unique lift; this obstruction
   disappears. The example refutes only automatic local CAT(0) completion
   from the flat pullback premises. It proves no whole-plane Keller
   claim, arbitrary completion-normalization identification, general
   curvature classification, or failure of every completion approach.

## Binding clarification: use only nondegenerate comparison triangles

The producer's midpoint contradiction is valid when CAT(0) comparison
includes degenerate geodesic triangles. Fable supplied the following
perturbation to avoid reliance on that convention; ROOT checked it,
including the small extra path needed for the intrinsic metric.

Suppose a neighborhood N of o is CAT(0), with either the restricted
metric or its intrinsic path metric d_N. Choose rho>0 with B_X(o,rho)
contained in N, and choose a>0 with sqrt(a^2+a^4)<rho. Put

    x=p(-a), y=p(a), m=(0,a), z=(0,-a), delta=d_X(z,m)>0.

The arcs give d_N(x,y)=2a and d_N(z,x)=d_N(z,y)=a. For small eps>0 let

    z_eps=(0,-(1+eps)*a),  eta=a^2*(2*eps+eps^2).

The radial segment u -> (0,-u*a), 1<=u<=1+eps, has length eta and
lies in N once a^2+eta<rho: d_X(o,z)=a^2 and every point of this
segment is within eta of z. Thus d_N(z_eps,z)<=eta in either convention.
Projection gives

    d_N(z_eps,x), d_N(z_eps,y) >= sqrt(a^2+eta^2)>a,

while the paths through z give both distances <=a+eta. Their sum is
strictly greater than 2a. For eta<a, their difference has absolute value
at most 2eta<2a, so ALL triangle inequalities are strict. Since CAT(0)
includes the geodesic-space requirement, geodesics from z_eps to x and y
exist in N. Use gamma_+ for the x-y side, whose midpoint is m.
Euclidean comparison and the elementary median formula imply

    d_N(z_eps,m)^2
      <= (d_N(z_eps,x)^2+d_N(z_eps,y)^2)/2-a^2
      <= 2*a*eta+eta^2 -> 0.

But d_N(z_eps,m)>=delta-eta -> delta>0, a contradiction. This proves
the claimed local failure without comparing any degenerate triangle.

## Binding scope correction to the review

Fable's added Claim6 sentence says that because a genuine Keller map is
unramified on its original whole-plane source, the ramification mechanism
cannot occur for a Keller source and that completion at infinity is not
touched by this example. Do NOT promote that sentence as an exclusion
of ramification at an ADDED boundary. Unramifiedness on the original
source does not imply unramifiedness on a completion or finite normalization.
Indeed the displayed pi is itself unramified on its original M.

The justified distinction is precise: this original source is C* times C,
not the whole C^2. No arbitrary polynomial Keller source is identified
with this model or its completion. This correction does not affect the
six exact producer claims or the explicit geodesic calculation.

## Dependencies and decision

The length metric/completion facts, elementary Euclidean comparison
definition and median formula are the only imports. Endpoint and positive-
distance arguments are supplied explicitly. The Bridson--Haefliger PDF
remains UNREAD after its recorded failed request; no source retry or
book theorem import was made. No history-search exhaustiveness or
literature novelty is claimed.

CONFIRMED at exactly the corrected producer scope, MANUAL. This closes
the one automatic local CAT(0) inference. It does not supply a positive
Keller-specific estimate or properness theorem, and JC2 remains unresolved.
No new sheet number, target-change family, descendant, or curvature
classification is selected from this result. No new exit-price assertion.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8745`.
- Body SHA-256:
  `dd4ff320a16583ed9bd9a1f18c12110a86f9c9c75253c0d57dec7a8436f5679b`.
- Frozen basis: `1b9fa5f66ed30afef9db45e7dd62e7ad4572712d`.
