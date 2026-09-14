# Minor centres and exact source-parameter accounting

This is a derivation audit for the corrected engine, not a branch verdict.
Frozen copies were mechanically verified by the parent before this work.
No ledgers, jc2-lean, or ideation files are inputs or outputs of this audit.

## Every centre actually used

The source variable is y, t=x^-1, w=ty, z=w-1. The minor direction is y=0,
and the major direction is y=x. Def.5.1(1), printed Moh p.179, gives major
g-multiplicity (99/11)*8=72; its complementary minor packet has27 roots.
The degree11 approximate root has root counts8 and3 after applying Thm.1.1
to the complete coherent systems described in the frozen repair gate.
The degree66 polynomial has corresponding counts48 and18 (Def.3.1(4)
and Prop.6.1(2), printed pp.161,191). The degree99 counts are72 and27.

At the first minor splitting radius the minor disc contains its whole
27-root g-packet. A deck automorphism preserves the polynomial and the
initial rational direction y=0, so it preserves that packet. It takes this
disc to a same-radius disc containing all27 packet roots. Two equal-radius
ultrametric discs meeting are equal. Therefore the disc is Galois invariant.
Its strictly truncated centre is unique (Prop.1.2, printed p.147, and
Def.5.1(4), p.179), so every nonzero centre exponent is integral. This is
an actual orbit argument; the denominator of the split radius alone would
not prove the assertion. After placing the minor direction, only nonnegative
integer y-exponents remain below these positive radii.

Consequently the entire generic point at delta2 is

    y=jet0+u*t+(minor_a2+zeta)*t^2.

The strictly-below centre consists of jet0 and u. The at-level coordinate
minor_a2 is the chosen double-root position of the [2,1] splitting; it is
not a strictly-below centre coefficient. It must still occur in every
polynomial evaluation when the displayed face has double root zeta=0.
The signed separation between the two distinct roots is defined as3rho.
This invertible Q-linear parameter definition gives the product
(zeta-0)^2*(zeta-(-3rho)). No face coefficient is used as independent data.

At delta5/2 the entire strictly truncated centre is

    y=jet0+u*t+v*t^2+zeta*t^(5/2).

The cover t=s^2 acts on zeta by zeta->-zeta, since the centre is integral.
The [1,1,1] branch has three distinct roots of a monic odd cubic, hence its
root multiset is {0,a,-a} with a!=0. Defining c=a^2 gives the product
(zeta-0)*(zeta-a)*(zeta+a), reduced modulo a^2-c. c is localized, not fixed.
This derivation carries the full orbit; it does not set an arbitrary cubic
quadratic coefficient to zero by a second translation.

For a polynomial of degree D with minor root count3D/11 and major count8D/11,
the root-factor identity (Prop.1.2, p.147) gives

    ord_t Q(sigma_delta)=(3D/11)*delta-(8D/11).

For D=11 these are -2 and -1/2. Since K3=t^11*h3, the normalized leading
powers are denominator(delta)*(11+ord_t h3), i.e.9 and21. For D=99 they
are -18 and -9/2, and for D=66 they are -12 and -3. These are derived
valuations, not arbitrary cutoffs. The complete minimal required pole
ranges of K_F and K_G end immediately before their derived leading powers:
delta2 K_F81/K_G54; delta5/2 on s K_F189/K_G126. Any additional exact
leader condition at those powers needs the distribution-detector relation,
and is distinguished from the strict lower-pole vanishings.

`minor_maps.py` implements these constructions. It starts with the supplied
h3 polynomial and its declared generators, expands every represented source
monomial at the full carried centre, compares the leading product and all
lower coefficients, and eliminates only affine leaders in Q*. Each original
row is checked again using the final simultaneous map. No rho, c, u, jet0,
or minor_a2 is inverted. The old mode exists exclusively to reproduce the
historical restricted chart; it omits jet0/a2 and retains the historical
delta5/2 Hc pin, and is labelled as such in metadata.

## Translation calculation and gauge ledger

Use the source pullback T_(A,B)(x,y)=(x+A,y+B). This has determinant1 and
acts as identity on the projective line Z=0. Placing the two directions
therefore spends no source translation. If the old major intercept is a1,
and the old minor coefficients are j,u,a2 (or j,u,v), then expansion gives

    major_a1_new=major_a1+A-B,
    jet0_new=jet0-B,
    u_new=u,
    minor_a2_new=minor_a2-A*u,
    v_new=v-A*u.

The intercept map (A,B)->(A-B,-B) has determinant-1. Major and minor
intercepts can both be normalized, using one independent translation each.
The corrected chart uses only the first normalization, major_a1=0, and
keeps jet0 free. This retains a redundant diagonal translation; it is safe.
One should record that second parameter as available and unspent. Calling
it spent on Hc_11_0 is mathematically false, while spending it on a2 would
require a u!=0 cover and a separate u=0 case. The corrected chart does
neither. It carries minor_a2 without such a division.

| Parameter/action | Single use or explicit non-use |
|---|---|
| Source linear shear | Place first finite leading direction at y=0. |
| Independent relative source scale | Place second direction at y=x. |
| First source-translation combination B-A | Set major_a1=0. |
| Residual diagonal translation A=B | Unspent; jet0 and minor_a2/v are carried. |
| Uniform source dilation, with compensating monic target scales | Set beta=1 on beta!=0; beta transforms by lambda^-4. |
| Two target multiplicative parameters | Normalize leading F,G coefficients; canonical h2,h3 are then monic by definition. |
| Target additions | Unspent. |
| Cover generic-variable coefficient and selected conjugate | Coordinate/representative choices, not further source-group spends. |
| Approximate-root depression and coefficient pivots | Canonical internal coordinates and Q*-isomorphisms, not source actions. |
| rho or c localizer | Open-stratum condition, not numerical normalization. |

All terms of the corrected centred h3 template except its actual constant
contain (y-x): the strict-weight basis has positive (y-x) exponent whenever
r<=10, and the two allowed equality terms contain (y-x)^5 and (y-x)^2.
Hence h3(x,x)=Hc_11_0. Under the residual diagonal translation this value
is unchanged: h3(x+A,x+A)=Hc_11_0. Thus Hc_11_0 is translation invariant
and is free in both corrected branches. A separate shift of an auxiliary
root would create the forbidden h3^2 term in the canonical approximate-root
expansion; it is not a source translation.

## No unknown disappears because a valuation was rounded

The raw degree11 lower total-degree triangle has66 coefficient slots. The
D2 substitution t=s^3,z=pi*s^4 assigns monomial weight3r+4q. The derived
K3 valuation32 imposes one coefficient equation for each raw slot strictly
below32; it does not impose zero on the equality slots. Exact enumeration
has43 below,2 equal,21 above. The two equality slots are (4,5),(8,2).
After eliminating the43 scalar zero rows, the general face consists of the
fixed top pi^8 plus those two independent coefficients. The first may then
be solved from the independently derived K2 approximate-root face identity;
the second stays free at that comparison's level.

Using the old strict-support triangular basis for the21 above-face slots
and adjoining the two pure equality monomials is an invertible coordinate
choice on that full23-dimensional floor solution space. Within each t-row
the basis z^v*w^(d-v)=z^v*(1+z)^(d-v) has unit triangular coefficient matrix
in ascending z degree, so it removes no additional unknown. This is why a
safe template may use the old symbol names without confusing an equality
coordinate with an old Hc symbol. The zero rows and rank have to be recorded
before elimination; the phrase "make the floor strict" would instead add
unsupported equations on both equality slots.

Printed references used here are visible in the parent's fresh PDF
extraction; their stable source anchors are Moh (1983), printed p.147
Prop.1.2, p.149 Thm.1.1/1.2, p.161 Def.3.1(4), p.179 Def.5.1(1),(4),
and p.191 Prop.6.1(2). The already frozen repair gate gives the complete
coherent-system arguments and object distinctions needed for the two
canonical cube-root applications. This minor module does not identify
auxiliary h3 with a characteristic T polynomial.
