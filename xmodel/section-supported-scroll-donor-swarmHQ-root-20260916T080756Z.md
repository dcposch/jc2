# Section-supported Hirzebruch donors: no ruling-degree restriction

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra same-model algebra check.
Date: September 16, 2026. Basis: d61a52e690ced7d6f2be3d6e107d9d47513a304a.
Evidence: MANUAL, with the accepted all-contact logarithmic theorem below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED pending different-model hostile review.
Claim: SECTION-SUPPORTED-SCROLL-DONOR-1. JC2 remains unresolved.

## Statement

Let Y=F_e over C, e>=0, with ruling pi:Y->P1 and fiber class f.
Let Phi:Y->P2 be a finite morphism and ell any target line. Write

    L=Phi^*O_P2(1), D_infty=Phi^*ell, R=Ram(Phi),
    B=supp(D_infty) union supp(R), U=Y minus B.

Assume EVERY irreducible component of B is a section of this ruling.
There is no dominant everywhere-defined morphism A2->U.

There is no restriction on L.f, deg(Phi), ramification multiplicities,
the multiplicities in D_infty, or contact orders of the sections. The first
leg need not be finite or etale. The full boundary is used, not a selected
subcollection. Multisections, vertical boundary components, other surface
models and arbitrary Keller normalizations are outside this statement.

## Prior scope and the source correction

The accepted [fiber-degree-one theorem](scroll-fiber-one-donor-astra-20260912.md)
uses L.f=1 to make the two relevant horizontal components reduced sections.
Its [independent gate](scroll-fiber-one-donor-gate-fable5-20260912.md) retains
that hypothesis. This report removes that restriction in the stated
section-supported case; it does not claim to reprove the old theorem's
separate cases with vertical boundary components.

The [September 16 source correction](projective-bundle-v2-correction-swarmHQ-root-20260916T072000Z.md)
withdraws the old assertion that one-point contact of order greater than
one obstructs an A2 complement. Corrected [van Dobben v2, Theorem 3.1](https://arxiv.org/pdf/2608.27341v2)
allows arbitrary contact order at one support point. That theorem motivates
the present applicability test but is NOT a premise of the proof below.

The retained geometric input is the accepted
[all-contact logarithmic integration](bd-a2-firstleg-log-kodaira-coordinator-integration-sol56-20260830.md):
for the complement of two sections meeting over s distinct base points,
the logarithmic plurigenus is n(s-2)+1 for s>=2. Consequently such a
complement cannot receive a dominant regular A2 map. Contact multiplicities
do not replace s. Its earlier Sol/Opus review chain is consumed as accepted;
this report does not duplicate that proof audit.

Whole charged local reads and full SHA256 pins:

- Fiber-degree-one producer: 1aede0f67970ff01b9a599352086a7c72d51cf610e1ae52db088f9e3fc2f0997.
- All-contact integration: ff25ba27388c02698013483e2e5537f18ed39e918e5cb0cb4c099a75ef42f298.
- Source correction: 0bd775af7ed40e75b13f532aa0086bd120a647c3bfd83541a1331071b4b04c75.

## 1. Three or more support components

Pic(Y)=Z S_0 direct-sum Z f, with S_0 a minimal section. If B has at
least three distinct components B_i, there is a nonzero integer relation
sum n_i[B_i]=0 in Pic(Y). Hence a rational function z has principal divisor
sum n_i B_i. This divisor is nonzero because the components are distinct
and not all n_i vanish, so z is nonconstant. Both z and z^-1 are regular
on U. A dominant A2->U would pull z back to a nonconstant unit of C[x,y],
which is impossible. This is the previously accepted unit obstruction.

The boundary is nonempty because Phi is finite surjective and ell is
nonempty. Thus it remains to handle one or two support components.

## 2. Generic ramification along the inverse image of ell

If a section D appears with multiplicity a in D_infty, Phi maps D
finitely onto ell. In characteristic zero its generic tangential map is
separable. The coefficient of D in R is therefore exactly a-1.
This is the ramification coefficient at the generic point, not the
possibly larger behavior at isolated intersections with other components.

Also L is ample, K_Y.f=-2, and each section has intersection one with f.
The ramification formula is R~K_Y+3L, with full multiplicities retained.

If B consists of a single section D, write D_infty=aD, a>=1. Then
R=(a-1)D, so K_Y~-(2a+1)D. Intersecting with f gives 2=2a+1,
an impossibility. No single-section case exists.

If B consists of two sections D,E and both lie over ell, write
D_infty=aD+bE with a,b>=1. Then R=(a-1)D+(b-1)E, so

    K_Y~-(2a+1)D-(2b+1)E.

Intersection with f gives 2=2a+2b+2, again impossible. This argument
also handles equal Picard classes; independence of D,E was not assumed.

Consequently the only remaining two-component case has

    D_infty=aD,    R=(a-1)D+rE,    a>=1, r>=1,

where E does not map into ell. Intersection with f additionally gives
r=2a-1. The precise value is a consistency check, not needed below.

## 3. Remove the fixed normal ramification before restricting

Let h=Phi|D:D=P1->ell=P1. For a point p of D not in E choose local
analytic target coordinates (z,w) with ell={w=0}. Near p the full
pullback of w is t^a times a unit, where t is transverse to the smooth
section D. Absorbing a holomorphic a-th root of that unit into t gives
coordinates (s,t) in which

    Phi(s,t)=(g(s,t),t^a),
    det(dPhi)=a*t^(a-1)*partial_s g.

Near p, R is precisely (a-1)D, because no other boundary component
passes through p. Therefore partial_s g is a unit, and h is unramified
at p. We conclude that every ramification point of h lies in D intersect E.
This conclusion does not restrict the raw divisor R to a component it
contains, and it makes no claim of a scheme identity at the intersections.

The degree of h is

    delta=deg(L|D)=L.D=a D^2.

It is positive because L is ample. If delta=1, integrality implies
a=1 and D^2=1. Then deg(Phi)=L^2=a^2 D^2=1. A finite degree-one
morphism onto the normal P2 is an isomorphism, contradicting the Picard
ranks two for F_e and one for P2. Thus delta>=2.

Riemann--Hurwitz gives total ramification 2delta-2. Each point contributes
at most delta-1, so h has at least two distinct ramification points.
Therefore D and E meet at at least two distinct points. As both are
sections, these points lie over at least two distinct ruling-base points.

## 4. Finish and preserve the boundary of the result

Here U=Y minus(D union E). The accepted all-contact logarithmic theorem
applies with the actual distinct intersection support just proved. It
excludes every dominant regular A2 first leg. Combined with the unit and
one-component arguments, this proves the statement in all its cases.

In particular a finite-cover construction cannot use any corrected
two-relative-hyperplane A2 complement on a Hirzebruch surface as this full
etale donor, even with nonreduced inverse image of the target line.
Recognizing an abstract A2 complement still does not provide a compatible
finite map. No theorem puts arbitrary Keller sources into this boundary
type, and nothing here resolves JC2, the general first-leg problem, or
the multisection/singular-completion cases.

Controls: two sections can have an A2 complement while meeting once,
even tangentially; that fact is NOT contradicted. The obstruction above
comes from the finite map and its COMPLETE ramification/line boundary.
Locally (s,t)->(s,t^a) has fixed normal ramification (a-1){t=0} but
unramified restriction to that divisor, explaining why the residual
argument is essential. Counting contact multiplicity as multiple support
points would be erroneous. A map merely rational or generically finite
need not have ample L or finite section restrictions, and is not covered.

QUANTITY: existence of any dominant A2 first leg into the exact stated
donor, with no ruling-degree bound. CHEAPEST TEST: local residual-Jacobian
calculation, support split and Riemann--Hurwitz; performed manually.
No scientific computation, degree enumeration or new exit-price assertion.
Targeted history comparison found the narrower fiber-degree-one attachment
and the accepted log/unit mechanisms; no claim of literature novelty.
No automatic higher-degree, multisection or boundary-family successor.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8239`.
- Body SHA-256:
  `218bc6356e35ff384f6594b3a4ed5234dd9fe8a9aaa68e45e86dc03cbc2071cd`.
- Frozen basis: `d61a52e690ced7d6f2be3d6e107d9d47513a304a`.
