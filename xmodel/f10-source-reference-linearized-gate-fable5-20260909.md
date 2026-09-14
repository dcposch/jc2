# Fable5.1 hostile gate: coalesced polynomial reference and next-target linearization

Fable5.1, September9,2026, invitation 10:14:45Z, hard stop 10:39:45Z. Independent
gate over characteristic-zero fields. All six charged inputs were read WHOLE from the
lane inputs after the ordered pins matched byte-for-byte; every arrow below was
rederived by hand, ZERO mathematical subprocesses of any size. No source/provenance
path, peer body, log, receipt, protected tree, fetch or AWS was touched.

Pins verified in charged order (sha256sum of the six input files):
e87e5133... reference proof (body 978d2963..., 14741 B) / 990a3f0a... its artifact;
95221835... linearized discriminator (body 89364311..., 16270 B) / c9a5e895... its
artifact; d225258c... accepted16l reduction; 221a5d58... its accepted Fable gate.
The 16k receiver conclusion is used ONLY as the explicit hypotheses of the reference
proof, as charged; 16l is used only through its imported conclusions j=7q+9,
r=(7m-1)/(3m), ord alpha>=2r, ord beta>=3r and the full-A/B valuations 3mr, 3nr.

## Summary verdicts

| Item | Verdict | First exact failure |
|---|---|---|
| A canonical reference, faces, Delta support, cubic shape, A2(0)=-1 | CONFIRMED | none |
| B exact depression, (5), affine shift, four-parameter form, target (3) | CONFIRMED | none |
| C transformed faces, valuation, rectangles [0,e]x[0,3e], degrees 4e, initials, (8) | CONFIRMED | none (import boundary stated) |
| D standalone linearization, L, determinant c, affine line, dual numbers | CONFIRMED | none |
| E extra conditions, C2!=0, d4, top-preserving a, q=0 fixed-face contradiction | CONFIRMED | none; not a source obstruction |
| F composition and limits | CONFIRMED as limits; missing implication identified below | no exclusion follows |

Notation clash, not an error: the discriminator's Z and r are the reference proof's z
(post-shift) and r0=q+1; the reference proof's r=rho=(7m-1)/(3m) is 16l's resonance.

## A. Canonical reference and the source root polygon

Identity through order7. f_s has scalar terms at orders 7(m-h)>=14 (h<=m-2) and F
starts at j=7q+9>=9. So A_s == R_s^m mod s^8, and at each i<=7 the equation
mK^(m-1)R_(7-i)=[s^i]A_s-(products of earlier R's) holds EXACTLY; the complement
choice of 16l plays no role because F_i=0 there. K^(m-1) is a nonzero divisor, so
R_(7-i) is unique. CONFIRMED.

Even descent. A_s=s^(7m)A(a^2/s^2,b/s), K and (inductively) earlier R's are even in
a, so K^(m-1)R_(7-i) is even; K^(m-1)(a,b)[R(a,b)-R(-a,b)]=0 in the domain forces
R_(7-i) even, hence a polynomial in g=a^2,p=b, homogeneous of (2,1)-degree 7-i.
CONFIRMED.

Antiweight induction. nu=max(I-J). nu(UV)=nu(U)+nu(V) (initial forms multiply in a
domain), nu(H)=2 from -g^3p. [s^i]R_s^m = mH^(m-1)R_(7-i) + sum over products
H^(m-k)R_(7-h_1)...R_(7-h_k), k>=2, all h_l<i, each of nu<=2(m-k)+2k=2m by
induction; nu([s^i]A_s)<=2m by I-J<=2m for A. If nu(R_(7-i))>2 the first term has
nu>2m and cannot cancel. So nu(R_(7-i))<=2, 2I+J=7-i<=7, I,J>=0: supp(R) in Delta.
CONFIRMED.

Face. Lattice points of Delta with I-J=2 are exactly (2,0),(3,1) (I<=3). The nu=2
part of R_s is -g^3p+d s^3 g^2 (g^2 has 2I+J=4, order3). Homogenized source face
of A: g^(2m+k)p^k has s-power 7m-4m-3k=3(m-k), so it is (-1)^m g^(2m)(gp+s^3)^m.
The nu=2m part of R_s^m is (-1)^m g^(2m)(gp-d s^3)^m. Since A_s and R_s^m agree at
order3, the s^3 coefficients (-1)^m m g^(2m)(gp)^(m-1)(-d) and (-1)^m m g^(2m)(gp)^(m-1)
match, so d=-1 (char0, m!=0), the face is -g^2(gp+1) and g^2 is attained. CONFIRMED.

Cubic shape. deg_g R<=3 so deg_Z R<=3. The Z^3 coefficient r(p) satisfies
-r(p)g^3 in Delta: g^3p^J needs J>=1 (I-J<=2) and J<=1 (2I+J<=7), and H fixes r=p.
In (Z-exp i, p-exp j) Delta reads 2i+j<=7, i-j<=2 because the top antiweight
monomial of p^jZ^i is (-1)^i g^i p^j, injective in (i,j). Removing the weight-7
terms (all in pZ^3): deg A2<=2, deg B4<=4, deg C6<=6. At p=0, Z=-g so the g^2
coefficient of R is A2(0)=d=-1. Shape (1) CONFIRMED, over any field of char0.

## B. Exact depression and the four-parameter form

Homogeneous a_s=a2 s p^2+a1 s^2 p-s^3 (weight3), b_s, c_s (weights5,7). With
zeta0=p^(1/3)Z, R_s=zeta0^3+a_s p^(-2/3)zeta0^2+b_s p^(-1/3)zeta0+c_s, a monic
cubic; shifting by a_s p^(-2/3)/3 gives alpha=b_s p^(-1/3)-a_s^2 p^(-4/3)/3
=p^(-4/3)(p b_s-a_s^2/3) and beta=c_s-a_s b_s/(3p)+2a_s^3/(27p^2): (4) CONFIRMED.
16l's right change removes at order s^l the zeta^2 multiple h_l; for a monic cubic
h_l is a scalar, so each step is a translation, the composite is a translation, and
the unique translation killing the quadratic coefficient is the displayed one. The
reference depends on a only through a^2=p^2-Z, so both triple lines give the same
(4). CONFIRMED.

Orders. r=7/3-1/(3m): 2r=14/3-2/(3m) lies in (4,5) for m>=2, 3r=7-1/m in (6,7).
alpha,beta have integral s-orders (p b_s-a_s^2/3 and c_s-... are s-polynomials), so
ord alpha>=5, ord beta>=7. Expanding by hand:
a_s^2=a2^2 s^2p^4+2a2a1 s^3p^3+(a1^2-2a2)s^4p^2-2a1 s^5p+s^6,
p b_s=b4 s p^5+b3 s^2p^4+b2 s^3p^3+b1 s^4p^2+b0 s^5p.
Orders1..4 give b4=0, b3=a2^2/3, b2=2a2a1/3, b1=(a1^2-2a2)/3, i.e. (5); order5
leaves u=b0+2a1/3 free. The -s^3 of a_s is exactly what produces -2a2 in b1 and
2a1/3 in u. CONFIRMED.

Affine shift. h=(a2p+a1)/3, A2=3ph-1. z^2: A2-3ph=-1. z: 3ph^2-2A2h+B4
=B4-3ph^2+2h; with (5), B4=(a2^2/3)p^3+(2a2a1/3)p^2+((a1^2-2a2)/3)p+b0 and
3ph^2=(a2^2p^3+2a2a1p^2+a1^2p)/3, 2h=(2a2p+2a1)/3, so the z coefficient is
b0+2a1/3=u exactly. Constant V=C6-B4h+A2h^2-ph^3, deg<=6. Homogeneously
R_s=pz^3-s^3z^2+u s^5 z+V_s. Depressing zeta0'=p^(1/3)z with quadratic coefficient
-s^3p^(-2/3): alpha=u s^5p^(-1/3)-s^6/(3p^(4/3)), beta=V_s+u s^8/(3p)-2s^9/(27p^2):
(6) CONFIRMED. ord beta>=7 kills v_h s^(7-h)p^h for h=1..6, so R=pz^3-z^2+uz+v.
Converse: any (2) has ord alpha>=5, ord beta>=7, splitting scale
min(5/2,7/3)=7/3>r. Reference-only, as stated. CONFIRMED.

Target. det d(g,p)/d(p,Z)=det[[2p,-1],[1,0]]=1 and the shift has determinant1, and
directly [A,B]_(p,Z)=-g_Z[A,B]_(g,p)=[A,B]_(g,p). So
[A,B]_(p,z)=c(p^2-Z)=c(p^2+(a2/3)p+a1/3-z): (3) CONFIRMED. The polynomial shift is
the automorphism; p^(1/3) and -1/(3p) enter only the analysis. CONFIRMED.

Controls rechecked: u=v=0 gives orders6,9, scale3; b4=1 puts b4p^5 at order1 in
p b_s. Both as stated.

## C. Transformed faces, valuation, rectangles, initials, localized target

Inequalities. g=p^2-z+(a2p+a1)/3 has (p,z)=(1,2)-weight<=2 and (-1,1)-antiweight
max(-2,1,-1,0)=1, so g^Ip^J maps to weight<=2I+J<=7e and antiweight<=I-J<=2e, with
i,j>=0: i+2j<=7e, j-i<=2e. CONFIRMED.
Faces. Top weight-7e part of the image is the image of H^e under the homogeneous
top part g->p^2-z, and H=p(p^2-g)^3->pz^3 exactly, so p^e z^(3e). Antiweight-2e
part is the image of (-1)^e g^(2e)(gp+1)^e under g->-z,p->p, monomial-injective:
(-1)^e z^(2e)(1-pz)^e=z^(2e)(pz-1)^e. Lower terms cannot reach either face.
CONFIRMED.
Valuation. z=p^(-1/3)s^rho Y+s^3/(3p), rho<7/3<3: in z^j the term with k shift
factors has order rho j+k(3-rho), so p^iz^j in A'_s=s^(7m)A'(p/s,z/s^2) leads at
7m-i-2j+rho j=7m-(mi-r0 j)/m (using rho-2=(m-1)/(3m)=r0/m) with coefficient
p^(i-j/3)Y^j. At the minimal order only leading terms occur, distinct j give
distinct Y^j and fixed j fixes i, so no cancellation. Hence val=7m-max(mi-r0j)/m.
Import: 16l's full initials P=V^m+U (monic, degree3m) at 3mr=7m-1 and monic Q at
3nr=7n-n/m in the same chart (zeta=p^(1/3)(z-s^3/(3p))=s^rY). So max(mi-r0j)=m
resp. n: (7). Twice (7) plus r0 times i+2j<=7e gives (2m+r0)i<=(2+7r0)e with
2m+r0=7r0+2, so i<=e, then j<=i+2e<=3e; (e,3e) is attained by the top face and
satisfies mi-r0j=e(m-3r0)=e. Rectangles and ordinary degrees4e CONFIRMED.
Initials. Y->p^(1/3)z, X->p sends T=Y^m/X^(1/3) to p^((m-1)/3)z^m=p^(r0)z^m,
P=XC(T)->pC(T), Q=X^(5/3)YD(T)->p^2zD(T); 16l's (B) divided by3 is
nTC'D-mTCD'-CD=-c. Weight of p^2z is 2m-r0=n. CONFIRMED.
Localized target. R=t!=v never meets z=0 (R=v there), and p=(t+z^2-uz-v)/z^3 gives
a bijection with z!=0: G_m fiber of the REFERENCE only. d(R,z)/d(p,z)=R_p=z^3, and
[A,B]_(p,z)=R_p[A,B]_(R,z), so (8) follows by substituting p; numerator degree<=7
in z, so no z^(-1) term. Nothing about the fiber of A is inferred. CONFIRMED.
Boundary of the verdict: the valuation of the FULL A'_s,B'_s is imported from 16l
(coalesced triple minimiser, lambda_split>=r); this gate re-verified only that the
import is applied to the identical object and chart.

## D. Standalone linearization

Variation space. gcd(m,r)=1; mi-rj=-m-r gives i=rl-1,j=ml+1,l>=1, monomial
(Z/p)T^l, positive degree k0l+1, 7m=3k0+1 so l<=3; mi-rj=-2r gives Z^2T^l,
degree k0l+4, 7n=5k0+4 so l<=5. Complete, dimensions3 and6. CONFIRMED.
Bracket. (A0)_p=C+rTC', (A0)_Z=mpTC'/Z, (B0)_p=pZ(2D+rTD'), (B0)_Z=p^2(D+mTD');
the rmT^2C'D' terms cancel and r-2m=-n, so [A0,B0]=p^2(CD+mTCD'-nTC'D)=cp^2.
[A0,Z^2F]=Z{mTCF'+(2rTC'+2C)F}; [(Z/p)U,B0]=Z{-nTDU'-((m+r)TD'+3D)U}: (5).
CONFIRMED.
Change of unknowns. det[[C,TC'],[nD,D+mTD']]=CD+mTCD'-nTC'D=c; (7) inverts (6)
exactly; C(0)D(0)=c so U(0)=0 iff h(0)=0. Substituting (6) into (5) by hand: the
h' terms cancel (nTCD-nTDC), the v' terms give T(CD+mTCD'-nTC'D)v'=cTv', the h
terms give h[(n-m-r)TCD'+(2rn/m-n)TC'D+(2n/m-3)CD]=h(r+1)c/m, and the v terms,
after eliminating T(mCD''-nC''D) by the derivative of (1) (the T^2C'D' coefficient
n-2m+r vanishes), give (2/m)(mTCD'-nTC'D+CD)v=2cv/m. So (8) with m-2r=r+1.
Independently the field X=(Z/p)h d_p+(Z^2/p^2)k d_Z, k=(v-rh)/m, has X(T)=(Z/p^2)Tv,
X(A0)=(Z/p)U, X(B0)=Z^2F, and div(cp^2X)=cZ{h+rTh'+2k+mTk'} agrees with (8). The
Lie-derivative identity holds in K[p,p^-1,Z]; both images are polynomial and the
polynomial ring injects, so the polynomial identity follows. X is a device only.
CONFIRMED.
Classification. (9): v(0)=-m/2; deg v=s>=2 gives [T^(s+3)]U=v_s(3b-2-ms)/b
=m(1-s)v_s/b!=0 (3b-2=m), against deg U<=3; s=1 gives zero, so v=-m/2+aT,
h=-aT(m+2)/b=-3aT. Then U_a=-(m/2)TC'+aT(TC'-3C), and F_a uses 1-3n=-5m. Degrees:
TC'-3C=-lambda T^2-2mu T-3nu, TD'-5D of degree<=4. Kernel K(T(TC'-3C),T(TD'-5D)),
nonzero by -3C(0). Rank8 into the9-dimensional degree<=8 space; -c in the image.
Dual numbers: epsilon^2 kills [deltaA,deltaB], giving c(p^2-epsilon Z); no
evaluation at epsilon=1 exists. CONFIRMED.

## E. Extra conditions, top preservation, q=0 fixed-face test

[T^7] of (1): nTC'D->3d4+2lambda, mTCD'->4d4+5lambda, CD->d4+lambda; total
d4(3n-4m-1)+lambda(2n-5m-1)=m d4-n lambda=0. CONFIRMED.
Reciprocal: C'(T)=3x^-2 f-x^-1 f', so (1) is x^-8 fd(3n-5m-1)+x^-7(mfd'-nf'd)=-c,
i.e. mfd'-nf'd=-cx^7; (d f^-a0)'=O(x^7) gives d=f^a0+O(x^8). With lambda=0,
[x^6]=(a0)_3 mu^3/6+(a0)_2 nu^2/2, [x^7]=(a0)_3 mu^2 nu/2 (partitions (3,0),(0,2),
(2,1)); a0=n/m in (5/3,7/4] so mu=0 then nu=0, contradiction. lambda!=0 CONFIRMED.
U_3=-3m/2-a lambda, F_5=-(1+5m)/2-a d4=-3n/2-a d4; a=-3m/(2lambda) zeroes both
since d4=(n/m)lambda. CONFIRMED.
Polygon: (Z/p)T^k=p^(rk-1)Z^(mk+1) and Z^2T^k both have maximal antiweight
(m-r)k+2=(2r+1)k+2; k=3 gives 2m+3, k=5 gives (10m+11)/3=2n+3, both outside, and
A0's own maximal antiweight is 3(m-r)-1=2m, so no cancellation. For the
top-preserving solution k<=2,4: 4r+4=2m-(2r-2), 8r+6=2n-(2r-2): strictly below for
q>=1, attained at q=0. CONFIRMED.
(10): U_2=-m lambda-2a mu=m(3mu/lambda-lambda). d4=a0 lambda, d3=a0 mu
+a0(a0-1)lambda^2/2 from [x],[x^2] of f^a0; F_4=-(1+4m)d4/2-2a d3 and
3m(a0-1)-(1+4m)=-2m give F_4=(n/m)U_2. So the q=0 zero-face condition is
mu=lambda^2/3. CONFIRMED.
q=0: scaling C_t=t^-3C(tT) multiplies every term of (1) by t^-8, reciprocal
coefficients (lambda/t,mu/t^2,nu/t^3); lambda=1, mu=1/3, f=(1+x/3)^3+bx^3,
b=w-1/27. f^(7/4)=(1+x/3)^(21/4)+(7/4)bx^3(1+x/3)^(9/4)+(21/32)b^2x^6(1+x/3)^(-3/4)
+O(x^9). Adjacent-ratio factors: [x^7]/[x^6] of (1+x/3)^(21/4) is (-3/4)/(7*3)
=-1/28; [x^4]/[x^3] of (1+x/3)^(9/4) is (-3/4)/(4*3)=-1/16; [x](1+x/3)^(-3/4)=-1/4.
binom(9/4,3)=15/128, Q6=(7/4)(15/128)/27=35/4608. binom(21/4,6)
=3^3*5*7*13*17/(2^16*3^2*5)=4641/65536, P6=1547/(65536*243),
s=P6/Q6=1547*9/(128*243*35)=221/17280. f7+f6/4=(3/14)P6+(3/16)Q6 b=0 gives
b=-(8/7)s=-221/15120; then f6=sQ6(1-8/7)+(21/32)(64/49)s^2=(s/7)(6s-Q6) and
6s-Q6=(5304-525)/69120=177/2560, so f6=(221/17280)(177/17920)!=0. All short
factors CONFIRMED by hand; no scalar test executed.
Collapsed faces: pT^i has maximal antiweight (m-r)i-1, unique maximum at i=3,
monomial (-1)^m g^(3m)p^m; p^2ZT^j gives (-1)^(5m+1)g^(3n)p^n=(-1)^n g^(3n)p^n.
These are single vertices, not (-1)^e g^(2e)(gp+1)^e. So freezing them is a
changed-hypothesis test at a non-source base point: NOT a q=0 source obstruction.
CONFIRMED as the discriminator states.

## F. Composition and the missing implication

Compatible interface. The reference proof's initials pC(T), p^2zD(T) with 16l's
ODE are exactly the discriminator's A0,B0 with (1), and its top target cp^2 is the
discriminator's [A0,B0]; the -cz of (3) sits at weight -r0, i.e. drop k0=2m+r0,
the discriminator's linearized target. The two results compose without
contradiction. No exclusion follows, and none is claimed by either author.
Intervening corrections are forced, not optional. In (p,z) the opposite face
z^(2e)(pz-1)^e contains -e p^(e-1)z^(3e-1), of weight e-(2r0+1): both A' and B'
carry nonzero drop-(2r0+1) corrections (-m and -n). Consistently, R^m contributes
m(pz^3)^(m-1)(-z^2)=-m p^(m-1)z^(3m-1) from the -z^2 of (2). Every drop 1..k0-1 may
carry further terms; the targets c(a2/3)p (drop m) and c a1/3 (drop2m) must be
produced by them, and neither result treats those two equations.
The exact missing implication. For the actual pair the drop-k0 equation is
L(U,F)=-c-N(T), where Z N(T)=sum over i+j=k0, i,j>=1 of [A'_i,B'_j] (a bracket at
weight -r0 is Z times a polynomial in T, of degree<=8 by the degree bound
i+2j<=7(m+n)-3=8k0+2). L has rank8 into the9-dimensional target, so solvability
is ONE scalar condition: the cokernel functional must annihilate N. Nothing in
either report computes N, the functional, or their pairing; uniform compatibility
at N=0 neither implies nor excludes solvability at the actual N. That is the gap
between "linearized compatible" and "actual drop-k0 equation solvable", and it is
the only place where an exclusion or a realisation could come from at this weight.
Also missing: the drop-m and drop-2m equations, all later drops, polynomiality of
any integrated lift (dual numbers give no epsilon=1 evaluation), the separated
regimes lambda_split<r, the simple line b=0 as a second chart, the inverse/reverse
source lift, and the F10 orientation. Both results can stand while F10, the
112/196 exception and JC2 remain unresolved; there is no full ideal certificate,
source realization, integrated lift or all-regime cover. CONFIRMED as limits.

## Perimeter and own checks

Read: the six charged inputs only, WHOLE, after pin verification. Written: this
file and box/f10-source-reference-linearized-gate-fable5-20260909/ (README and
input hashes) only. No CAS, Python, toy, matrix, resultant, coefficient script or
numerical check; all algebra above is manual and factored. No OPEN token is
raised, consumed or closed; no seal line and no exit-charge declaration line are authored. Own
whole-body read and the own-only raised-OPEN/collision check precede the marker.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only check; no corpus scan.

<!-- BODY-END -->
