# SNC orders of a rational Darboux two-form

Producer: swarmHQ ROOT; 2026-10-19. Evidence: MANUAL/PROVISIONAL,
UNPROMOTED pending different-model FIRST. Novelty UNKNOWN.
Basis: 161bf87caf90179fd10cfcd7eed755743ac51761.

## Statement

Let S be a smooth projective complex surface and omega a nonzero rational
two-form. Suppose C(S)=C(u,v) and omega=c du wedge dv, with c in C*.
Let p be a simple-normal-crossing point of div(omega), with exactly two
components D1,D2 through p, of orders a,b respectively. Then

    gcd(a+1,b+1)=1.

Orders may be positive or negative; gcd means the nonnegative gcd of
absolute values, with gcd(0,0)=0. In particular two simple zero curves
cannot meet transversely at a point with no other zero/pole component.
The result is only necessary for general rational forms; no converse is claimed.

## Point-blowup calculation

Include every exceptional curve, even when its form order is zero, in the
boundary graph. Label each curve of order a by lambda=a+1.
At a point on just one boundary component, a point blowup creates a curve
of order a+1, hence label lambda+1. Its edge with the old curve has gcd1.
At an intersection of two boundary components of orders a,b, the new
curve has order a+b+1, hence label lambda1+lambda2. Thus subdivision
preserves the edge gcd on BOTH new edges. At a point off the boundary,
the new curve has order1 and label2, and is initially an isolated vertex.
These formulas follow by substituting x=s,y=st into a local expression
unit*x^a*y^b dx wedge dy; the unit stays nonvanishing at the relevant center.

## Proof by a common resolution

Use the standard common resolution of the birational map defined by u,v:
Z -> S and Z -> P2 are birational morphisms of smooth projective surfaces,
each factoring into point blowups. On P2, div(c du wedge dv)=-3 L_infinity.
Start its boundary graph with this one curve, labeled -2; there are no edges.
Under any sequence of point blowups, the total transform of L_infinity
together with all exceptional curves is SNC and contains the form's support.
The calculation above proves inductively that EVERY graph edge has gcd1.

On the S side, work over p, where the two specified components are SNC
and there are no others. Their strict transforms on Z are connected over p
by the chain obtained by subdividing their original edge whenever its current
intersection is blown up. Blowups at other points do not remove an edge of
this connecting chain; they can add side branches. Every edge on the chain
therefore has the original gcd d=gcd(a+1,b+1).

The two end components have nonzero order, so on the P2 side they belong
to the boundary just constructed. Each intermediate curve is exceptional
over p. An intermediate curve with nonzero order likewise belongs to that
boundary. If an intermediate curve has order0, its label is1, so already
d=1. Otherwise the whole connecting chain belongs to the P2 boundary,
whose every edge has gcd1. In either case d=1, proving the assertion.

## Checks and scoped consequences

For the monomial form x^m*y^n dx wedge dy on C(x,y), the condition is also
sufficient: if gcd(m+1,n+1)=1, choose integers r,s with
r(n+1)-s(m+1)=1. Put u=x^r*y^s and
v=x^(m+1-r)*y^(n+1-s). The exponent determinant is1, so u,v generate
the rational function field, and du wedge dv=x^m*y^n dx wedge dy.
For example u=xy,v=xy^2 gives x*y^2 dx wedge dy. In contrast x*y dx wedge dy
fails the necessary test at the origin. This check is hand algebra, not CAS.

If pi:X->Y is finite dominant between normal complex surfaces, x and pi(x)
are smooth, and a target two-form eta is regular/nonvanishing near pi(x),
then ord_E(pi*eta)=e_E-1 at any ramification divisor E. Thus, if exactly
two ramification components meet transversely at x and pi*eta has rational
Darboux coordinates generating C(X), their indices e1,e2 must be coprime.
This applies to such smooth SNC points of an ACTUAL Keller normalization,
because its function field has the original source Darboux coordinates.
Singular source points, non-SNC intersections and finite source enlargements
are not disposed of by simply applying this statement to the original model.

The positive-zero multibranch cycle criterion has different hypotheses:
it treats multiple branches of ONE global positive-order curve, including
tangencies, using a cycle. Here distinct zero components are allowed but
the intersection must be SNC. Neither proves a forbidden point must exist.
No general pencil-basepoint theorem, donor regularization theorem, B=R
argument, global JC2 proof, or counterexample follows from this report.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4599`.
- Body SHA-256:
  `970f5de8f699645831323c5604b74f7a4c22e8dddcac61dee49f75cf49ad9482`.
- Frozen basis: `161bf87caf90179fd10cfcd7eed755743ac51761`.
