# R2 independent child-data derivation (conditional datum, not an exhibited pair)

Frozen source: `/tmp/jc2-lane.yqyWvI/inputs/moh1983_jram340_configurations_of_roots.pdf`.
Root reports the charged hashes mechanically verified. This lane independently ran
pdftotext and rendered pp.150,154,179,197 from that PDF into `r2-child-*` files.
The p.150 recipe literally uses `f_i(x) != 0`; constants DO count.

## Named failing datum

Parent n=96,m=72,M=(-72,36,78,94),d=(96,24,12,6,2),
V2=4,V3=3,V4=5. Thus us=1,vs=5,ds=6. Prop.6.3 gives a polynomial pair
F(gamma,pi),G(gamma,pi), monic in pi, with degrees12,16 and
J(F,G)=c gamma^3 (nonzero c; orientation changes its sign). It also carries
H=T2^psi(F,G), Q=T3^psi(F,G), with pi degrees30,53.
These latter numbers are independent computations from p.150:
mu1=-72; mu2=4*(-72)+(36-(-72))=-180;
mu3=2*(-180)+(78-36)=-318, then divide by6.

Everything here beginning 'the child' means: IF a source polynomial pair realizing
this census row exists, form its actual Prop.6.3 child. No source polynomial pair
has been supplied or constructed. That qualification cannot be removed: such a
source pair would be a Keller counterexample. The computation can refute an
inherited-label identity without exhibiting such a counterexample.

## Own eta expansion; no substitution of the parent's fixed-x series

Work in k[gamma]((eta)) where eta=G^(-1/16), holding gamma fixed, exactly as
p.150 requires. Then G=eta^-16 and F=eta^-12+higher terms.
Proposition3.1 (pp.157-159, including specialization psi) gives canonical forms:

H(F,G)=F^4-c G^3 + terms of (12,16)-weight <48,

Q(F,G)=H^2-c' F G^3 + lower canonical terms of weight <60.

Here c,c' are nonzero constants; normalization may set c=1. The canonical lower
terms of H have F exponent<4; those of Q are F^a G^b H^e with a<4,e<2.
Uniqueness of weights is elementary: 12a+16b=48 has the unique solution
(a,b)=(0,3) with a<4; 12a+16b+30e=60 has the unique solution
(a,b,e)=(1,3,0) with a<4,e<2. All lower weights in Q are even.
The equations hold as polynomials in the symbols F,G before and after descent;
Prop.6.3 supplies the exact degrees of the substituted H,Q.

Let A be the Puiseux root of H(U,eta^-16)=0 with the same leading eta^-12 term
as F. Newton/Hensel recursion puts A in k((eta^4)). Its derivative H_U at A
has order -36 and leading coefficient nonzero. Since the actual H(F,G) has
order -30, the unique local expansion gives

F=A+a eta^6+terms of order>6, with a in k^*.

This is also a direct use of the Hensel Taylor valuation: -30=-36+6. No term
with exponent not divisible by4 can occur before6. Hence the actual M2 is6,
and gcd(16,-12,6)=2.

Now set U=A+eta^6 W in Q(U,eta^-16). Its initial equation at order -60 is a
nondegenerate quadratic in W with two nonzero simple roots. Choosing the root
a just selected gives a Puiseux root B of Q(U,eta^-16)=0 in k((eta^2)). The
leading derivative is 2H H_U, order -30-36=-66; the derivative of the other
weight60 term F G^3 has order -48 and is strictly later. Canonical lower terms
have strictly later derivative order as well. Since actual Q(F,G) has order-53,

F=B+b eta^13+terms of order>13, with b in k^*.

Thus no odd exponent precedes13 and the coefficient at13 is nonzero. The
actual p.150 chain, independently reconstructed in the child's own eta variable,
is therefore

M'=(-12,6,13), d'=(16,4,2,1), M'_4=infinity.

For extra coefficient-field control, the chain-rule identity at fixed eta is
F_gamma|eta=J(F,G)/G_pi. Since G_pi has leading 16 eta^-15, all coefficients of
F below exponent15 are constant in gamma. The nonzero constants at6 and13
are consequently not coefficients one may discard under the p.150 recipe.
The campaign's M,d labels are correct on this named conditional child.

Do not use the p.154 displayed recovery formula without checking its indices:
its denominator as printed appears inconsistent with the p.150 definitions.
The safe recurrence derived directly from p.150 is
mu_j=(d_(j-1)/d_j)mu_(j-1)+M_j-M_(j-1).
It gives the same child M2=6 and M3=13.

## The actual top V changes under inversion

Parent radii from frozen shape.def51, also directly from Def.5.1(3), are
(delta1,delta2,delta3,delta4)=(1/3,2/7,1/7,-1).
Parent D3 contains (96/6)*5=80 roots of g; chosen D2 contains (96/12)*3=24.
At D3 Proposition4.6 and Definition5.1 give g's leading polynomial as p^8,
with deg p=10; the selected next major branch is a root of p of multiplicity3.

Normalize the common constant centre of D3 to y=0, allowed by translation.
Its logarithmic radius is1/7. The source coefficients lie in k((t)),t=x^-1,
so the seventh-root Galois action permutes nonzero leading coefficients in
orbits of7. A nonzero root of p of multiplicity3 would force degree>=21>10.
The selected multiplicity3 root is consequently0. The remaining degree7 is
one nonzero orbit with every root simple. Thus g has56 roots of the form

y=C t^(1/7)+higher, C nonzero,

and its24 roots in D2 have order>1/7.

At us=1 the actual Prop.6.3 map is

gamma=1/y,
z=sum_(j<5) a_j gamma^j+pi gamma^5,
x=(y-e-z)/b, b nonzero.

For one nonzero orbit put t=s^7, y=C s+... . Inverting on the physical place
with y as parameter gives x=C^7 y^-7+... and

pi=-b C^7 gamma^2+terms of smaller gamma-growth.

Seven conjugate source cover series become one inverse series, since their
C^7 agrees. Accordingly the56 source roots give exactly8 child pi-roots
with the same nonzero gamma^2 leading coefficient. The24 zero-centred source
roots have y-order>1/7 and hence, on inversion, strictly smaller pi growth than
gamma^2. Any remaining finite-x branches above y=0 also have smaller growth:
the finite x term is multiplied by gamma^-5 and the fixed a_j terms have
j<5. The child has degree16 in pi, so the remaining8 child roots all have
zero coefficient at gamma^2.

The same calculation also checks that the union with the approximate-root
polynomials has this as its actual top disc, rather than assuming a top radius
from the monomial-Jacobian extension of Definition5.1. Proposition4.6(2) gives
source T3 leading p^25 q, with q degree15 and all roots simple, including every
root of p. Galois symmetry therefore makes q consist of0 and two nonzero
7-orbits. One nonzero orbit coincides with that of p; the other is disjoint.
At the first orbit T3 has multiplicity26 per source coefficient, producing
7*26/7=26 child roots at C_* gamma^2. The q-only orbit produces7/7=1 child
root at a distinct nonzero C_** gamma^2. Its remaining53-26-1=26 child roots
have smaller growth. The lower T1,T2 roots are distributed with g by
Proposition4.6(1), so no greater growth arises from them. Thus the union has
actual top radius-2 and three first-split coefficients0,C_*,C_**; only the
first two carry roots of G.

Therefore the child's top disc has the concrete G split8+8, i.e. its
G leading polynomial is const*(pi-C_*)^8*pi^8 with C_* nonzero after scaling
at gamma^2. Its own d'_3 is2 and n'/d'_3 is8. Either proper major child
subdisc therefore has

V'_3=8/(16/2)=1,

not the inherited campaign label V3=3. Its own top C-TOP inequality is1<=2.
This is a first-principles inverse-series count; it does not identify flags,
physical places, and cover series. The explicit denominator7 conversion is
why the unadjusted source multiplicity cannot be reused as the child V.

This proves that the named datum passes THIS top screen when its V is
computed in its own chart, conditional on source realization. It does not
prove the source datum realizable or surviving all other screens.

## Independent obstruction / limitation

In fact the next layer appears to contradict cumulative Galois symmetry already
at the source. Once the selected multiplicity3 branch is forced to0 above, D2
has centre0 and radius2/7. Its g leading polynomial is a fourth power of a
polynomial of degree6 (24 roots /4). It has a nonzero splitting coefficient
only in orbits of7, impossible in degree6. This is the sort of stabilizer
information the enumeration's cumulative-denominator window may forget.
Root is investigating this separately. It prevents presenting n96,m72 as an
exhibited admissible source row, but does not repair the false V inheritance.

The safe outcome for this subtask is: own M,d verified; inherited top V
refuted by conditional inverse-series computation; actual source realization
OPEN (and probably independently impossible); no proof of936 arbitrary
source kills follows merely by assigning inherited V to the child's disc.
