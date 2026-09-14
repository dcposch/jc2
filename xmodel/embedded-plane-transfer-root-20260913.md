# Embedded-plane transfer from the explicit higher-dimensional counterexample

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
One construction discriminator, not a JC2 solution or a new low-sheet theorem.

## Statement and missing construction step

Let G=(R,T,S) be the following polynomial map over C, with u=xy:

```
R=2x-3x^2y-x^3b,
T=-((1+u)^3b+y^2(1+u)(4+3u))/2,
S=y+3x(1+u)^2b+3xy^2(4+3u).
```

Every point fiber of G has at most three points. The same bound holds for
G times an identity map, and after source/target polynomial automorphisms.
In particular it holds for Long's explicit four-dimensional symplectic map,
using its stated polynomial factorization through G times id.

Consequently, suppose j:A2->A^n is a polynomial embedding (more generally,
is injective on points), Phi is one of those ambient maps, and a plane Keller
map h satisfies Phi composed with j = i composed with h for a polynomial
map i:A2->A^n. Then h is an automorphism. No degree bound on j, i or h is
imposed. Injectivity of i and symplecticity of j are not needed.

This rules out importing the ambient collisions by an embedded source plane
whose ENTIRE ambient image factors through a plane Keller pair. It does NOT
rule out projecting the ambient outputs to two polynomials without such a
factorization, nor a noninjective source parametrization. Those are different
construction mechanisms; no extension to either is asserted.

## Exact fiber calculation, including exceptional targets

Fix output values (r,t,s). On x!=0 introduce w=1+xy and
a=2-3xy-x^2b, then v=w/x. Direct substitution gives

```
R=xa,
S=x^(-1)(2+4w-3aw^2),
T=(aw^3-w^2-w)/(2x^2).
```

Since a=r/x, the last two equations become

```
s=2/x+4v-3rv^2,
2t=rv^3-v^2-v/x.
```

Eliminating 1/x yields

```
p(v)=rv^3-2v^2+sv+4t=0,
x=2/p'(v),       p'(v)=3rv^2-4v+s.
```

The derivative cannot vanish at a root corresponding to a finite source
point. Given such a root, x is unique, then y=v-1/x is unique, and
b=(2-3xy-r/x)/x^2 is unique. Hence there are at most three x!=0 points
when r!=0, and at most two when r=0. If x=0, necessarily r=0, and the
equations reduce to y=s and b=-2t-4s^2, giving exactly one such point.
Thus every fiber has at most three points, even on r=0 or the discriminant.
No inference from the cardinality of one special fiber is used.

Sharpness control: at (r,t,s)=(0,1/8,0) the three points are
(0,0,-1/4), (1,-3/2,13/2), and (-1,3/2,13/2).
The quadratic p=-2v^2+1/2 gives the two nonzero-x points, and the separate
x=0 calculation gives the third. Repeated roots of p with p'=0 are excluded
points, not additional branches or positive-dimensional fibers.

## Plane consequence: consume the accepted bound, do not reprove it

For each z in A2, j injects h^(-1)(z) into Phi^(-1)(i(z)). Thus every
fiber of h has at most three points. Since h is Keller, it is dominant and
generically finite; its generic mapping degree is therefore at most three.
The already-accepted Orevkov theorem excludes mapping degrees two and three
for complex plane Keller maps. The remaining birational Keller case is an
automorphism. These classical inputs are consumed at their existing tier;
this report does not reverify them or confuse mapping degree with total
polynomial degree.

The injective-source hypothesis matters: dropping it would permit arbitrarily
many parameter points to represent one ambient point, so the counting argument
would no longer bound a fiber of h. Likewise, merely knowing
h=projection composed with Phi composed with j does not give
Phi composed with j=i composed with h: discarded outputs can distinguish
points identified by the projection.

## Direct canonical-pair check

Long's polynomial coordinates (x,y,b,D) make the fiber {R=r,D=d} equal to
the surface R(x,y,b)=r. For r!=0, x is a unit and elimination of b identifies
this surface with Gm times A1. For r=0 it is the disjoint union of x=0,
an A2 with coordinates (y,b), and {2-3xy-x^2b=0}, again Gm times A1.
The two factors are comaximal since
1=(2-3xy-x^2b)/2+x(3y+xb)/2.

No Gm-times-A1 component admits a dominant morphism from A2: the pullback of
its invertible coordinate must be a nonzero constant, leaving image dimension
at most one. On the A2 component the remaining output pair is
(T,S)=(-(b+4y^2)/2,y), explicitly an automorphism. Thus simply fixing this
canonical output pair gives no plane counterexample, independently of a
coefficient search. This is a check of that literal reduction, not a
classification of all symplectic reductions or arbitrary output projections.

## Provenance and stopping decision

Primary source: [Long, arXiv2608.23777v1](https://arxiv.org/html/2608.23777v1),
selected sections1--7, especially Proposition4.1 and equation54. Read via
primary HTML; NOT a whole-paper/appendix audit, and no source program run.
The core formulas and polynomial coordinate factorization are the consumed
data. The fiber count above is independently derived here. The argument for
the displayed G itself does not assume its ambient Jacobian or symplectic
claims. The four-dimensional application uses the source's explicit
coordinate isomorphism, not an unexamined dimensional identification.

Canonical history checked before authoring: AUDIT's August24
EXACT-COFRAME and NORMALIZATION RANK-TWO entries, including the accepted
Orevkov mapping-degree-two/three closure; selected coframe producer passages;
WHOLE September6 polynomial-graph obstruction report; current APPROACHES
graph/output scope; September8 sweep report; selected recent graph reports.
The coframe proposal was a duplicate and was not restarted. The old graph
theorems concern projections and do not themselves prove the factorization
statement here. Scoped searches are not exhaustive evidence of novelty.

Input hashes: AUDIT33150f4239b7c988cdfc5d4acce3d2bd25a3498eae6dc129a3ea63c56ee9efba;
APP56fb4bb586423d850a1c46c4a028440b28b8c4a039b46c13737a8b65f82dce0b;
COORD517fca6f67f3d705f9b4045e10f9039aaf11bf3280dfd27bb90bf003ee4a3ead;
graph1ab4e6791e6a38fd9a8313161a546554a57efcf5207bc32d42dfa4b492dd8e21;
sweep364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc.
No raw primary HTML/PDF checksum is claimed from browser access.

Decision: stop this embedded-source/full-output-factorization shortcut.
No ambient collision re-verification, low-degree proof lane, parameter/slice
farm, noninjective-source descendant or arbitrary-projection search follows.
The complete JC2 construction endpoint remains unmet. One different-model
FIRST is required before promotion of this scoped obstruction.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6585`.
- Body SHA-256:
  `0cdce63e8076949b172f64be0166bc49280f66b30486acb678c72fbd60eb1177`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
