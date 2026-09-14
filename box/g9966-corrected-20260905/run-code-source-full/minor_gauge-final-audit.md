# Hostile final audit of the optional jet0 gauge

Verdict: the displayed diagonal source translation is a valid global gauge
for the complete corrected necessary chart. A unit on the audited jet0=0
computation therefore implies emptiness of the free-centre chart. This does
not follow merely from obtaining a unit after setting a coordinate to0; it
follows from the explicit polynomial action and inverse below. The audit
covers `translation-proof.md`, `translation_controls.py/json`, and
`deep_gauge_accelerated.py`. No branch unit is asserted by this note.

## Exact coordinate action and inverse

For a source polynomial Q of total-degree bound D, write

    K(t,z)=t^D Q(t^-1,(1+z)/t).

A coefficient c_(r,p)t^r z^p is the source monomial
c_(r,p)x^(D-r-p)(y-x)^p. Under the diagonal pullback
Q_q(x,y)=Q(x+q,y+q), its (y-x)^p factor is unchanged and its x factor becomes
(x+q)^(D-r-p). Therefore the exact normalized action is

    T_q K = sum c_(r,p)t^r z^p(1+qt)^(D-r-p).

Every exponent D-r-p is a nonnegative integer in the represented full
coefficient box. Thus the action is polynomial in q and the coefficients,
unit triangular in increasing r, and preserves the y-degree bound p. Direct
source composition gives T_a T_b=T_(a+b), with polynomial inverse T_(-q).
The binomial Vandermonde identities in `translation_controls.py` verify the
coefficient group law through every source normalization degree used here.
The general proof is the same identity for arbitrary nonnegative exponent.

This action applies separately to h3, h2, C2, C3 and all four outer blocks
using their actual normalization degrees. Canonical approximate roots commute
with the action: apply the source automorphism to the depressed remainder
identity, preserving monicity and every remainder y-degree bound; uniqueness
of the canonical approximate root identifies the translated root. No auxiliary
root is reset by an independent additive normalization.

For an outer coefficient Q normalized at degree D, its effective contribution
is t*K_Q at normalization degree D+1. The formula gives exactly

    T_q^(D+1)(t*K_Q)=t*T_q^D(K_Q).

Consequently every inner and outer polynomial identity commutes with this
translation. `minor_gauge-transport-controls.py` supplies independent sparse
polynomial checks of the inner identity, all four one-t shifts, both F/G
identities, the physical source pullback, and the Jacobian chain rule.
This adds the multiplication check that an earlier comment in
`translation_controls.py` mentioned but its original code did not execute.

## All centres and faces are transported

The translated minor root is the old root series evaluated at x+q, minus q.
At the two branch radii its complete retained coordinates are

    jet0_new=jet0-q,
    u_new=u,
    minor_a2_new=minor_a2-q*u       (delta2),
    v_new=v-q*u                    (delta5/2),
    rho_new=rho, c_new=c.

The double-root position minor_a2 is transported, not omitted. In particular
nothing divides by u, and the u=0 slice is fully covered. The generic-variable
coefficient retains leading value1; all additional terms in the re-expansion
of (1+qt)^(-delta) occur strictly above the splitting radius. For delta2 this
also preserves the signed separation3rho between the two at-level roots;
for delta5/2 it preserves the conjugate orbit relation a^2=c.

The major ordinary centre stays0 because the translation is diagonal. Its
major direction y=x is fixed. Re-expanding the y-term alpha*t^(1/3) first
changes it at t^(4/3), strictly above the D1 y-radius4/9 as well as the D2
radius1/3. Thus both labelled major discs, beta=1, the D2 K2 face, and the
allowed h3 face are preserved. The raw formula also proves D2 stability
coefficientwise: translation increases r and preserves p, hence cannot
create a term below a previously imposed weight floor, and preserves the
coefficients at that floor.

For each generic-point evaluation, the transformed local parameter differs
from the original one by units with leading value1 and by terms above the
chosen radius. Substitution therefore acts triangularly on the complete
strict-lower coefficient rows and on the at-floor face differences. The
inverse source translation gives the inverse triangular action. This proves
preservation of the full D1 and minor incidence ideals, including C2/C3 and
outer remainder floors and the nonzero F/G face equalities. It does not rely
on the slogan that translating a face alone is harmless.

## Jacobian and unused source parameter

The source translation has determinant1, so

    J(F_q,G_q)(x,y)=J(F,G)(x+q,y+q).

It preserves the full positive-degree Jacobian ideal. Once those coefficients
vanish, the constant scalar is unchanged, and its nonzero Rabinowitsch
localization is preserved. It also preserves a descending prefix of Jacobian
degrees: translating a homogeneous term can only lower its degree. The
finite split of the degree162 band is harmless because its transformation
receives only degree163 terms, all already identically0.

Two independent source translations survive placing the two directions at
infinity. The first combination was spent on the major ordinary centre.
The generic corrected chart kept jet0 free and left the diagonal combination
unspent. The optional wrapper uses exactly that second parameter. It spends
no additional dilation and does not set rho or c to1. Hc_11_0 remains free:
all other h3 terms contain (y-x), while the source constant obeys

    h3(x,x)=Hc_11_0,
    h3(x+q,x+q)=Hc_11_0.

The equality coordinate E82 is also preserved at the D2 face; any later
value such as20/9 remains the consequence of a coefficient row, not a
translation choice.

## Why this slice covers every component

Let X be the complete corrected coefficient chart, with the declared
localizer rho or c. Its coordinate jet0 transforms by jet0-q. The maps

    X -> X_(jet0=0) x A1,
    p -> (T_jet0(p), jet0),

and

    (p0,j) -> T_(-j)(p0)

are polynomial inverses. Every coefficient and every retained centre is
transported by the same action. Hence this is an isomorphism of the entire
chart, including all its components and the u=0 locus. A point on the slice
lifts to a point with any desired jet0, including1; a unit on the slice forces
X to be empty. Nonunit full-chart dimensions differ from slice dimensions
by1. No unknown was discarded merely because a convenient point set it to0.

The computational wrapper first derives the generic source state, then applies
the exact ring map jet0->0 to all h3/C2/C3 images. It changes the same minor
series emitter before later expansions. Its cache clearing separates the
generic and gauged local substitutions. It removes only jet0 from the free
generator list and keeps minor_a2 or v and Hc_11_0. I found no second pin or
uncarried centre in that implementation.

The independent final verifier autodetects this wrapper from the initial
state metadata, checks its exact SHA-256, imports it before reconstructing
the source chart, and verifies the generic source maps followed by the
jet0->0 specialization. It still replays every saved QQ* and radical step
and regenerates terminal rows on their recorded preceding locus. Merely
checking names or specializing the final map without this transport argument
is explicitly insufficient.
