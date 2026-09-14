# F10 coalescence forces a polynomial four-parameter reference

Coordinator/root, September9,2026. NEW / UNREVIEWED manual proof.
No mathematical subprocess of any size. This is a necessary reference
normal form, not an exclusion, a receiver construction, or JC2.

## 1. Literal hypotheses and conclusion

Use INCREASING exponents m=3q+4,n=5q+7,q>=0. Let A,B be ordinary
characteristic-zero polynomials in g,p satisfying the following explicit
receiver hypotheses (they are the accepted16k conclusion after output swap):

    ell_(2,1)(A)=H^m, ell_(2,1)(B)=H^n, H=p(p²-g)³,
    [A,B]_(g,p)=c*g, c!=0,
    supp(A),supp(B) contained in m*Delta,n*Delta,
    Delta={I,J>=0: 2I+J<=7, I-J<=2},
    ell_(1,-1)(A)=(-1)^m*g^(2m)*(gp+1)^m,
    ell_(1,-1)(B)=(-1)^n*g^(2n)*(gp+1)^n.

Apply the finite canonical A-reference construction of accepted16l to the
cover g=a²,p=b, whose degree7 root is K=b(b²-a²)³. Assume that a triple
minimizer enters that theorem's COALESCED regime. The imported16l conclusions
used here are exactly

    j=ord_s F=7q+9>7,
    r=(7m-1)/(3m),
    ord_s alpha>=2r, ord_s beta>=3r

for its depressed cubic right coordinate, with original integral orders.
No existence of such a pair or regime is asserted.

Then the canonical reference descends to an ORDINARY polynomial R(g,p)
with support contained in Delta and the exact normalized root faces. In
Z=p²-g it has the form

    R=pZ³+(a2*p²+a1*p-1)*Z²+B4(p)*Z+C6(p),           (1)
    deg B4<=4, deg C6<=6.

Moreover the affine polynomial change

    z=Z+(a2*p+a1)/3

puts the SAME reference exactly into

    R=p*z³-z²+u*z+v,                                 (2)

where a2,a1,u,v are field scalars. The pair's bracket in the (p,z)
coordinates is exactly

    [A,B]_(p,z)=c*(p²+(a2/3)*p+a1/3-z).              (3)

The ENTIRE transformed pair has support in [0,m]x[0,3m] and
[0,n]x[0,3n], with those upper corners attained. Its ordinary degrees
are exactly4m,4n. Its leading forms for weight(p,z)=(m,-(q+1)) are
p*C(T),p²*z*D(T), T=p^(q+1)*z^m, with the SAME cubic/quintic
ODE as16l. The lower-weight corrections are not set to zero.

All claims are over fields, not arbitrary coefficient schemes with
nilpotents. They do not say A or B is a polynomial in R alone. Their full
remainders, scalar terms, finite degree bounds and all Jacobian equations
remain to be solved or contradicted.

## 2. Why the canonical reference really has the source root polygon

Write the accepted combined-homogeneous reference as

    R_s=K+sum_(i=1)^7 s^i R_(7-i),
    A_s=f_s(R_s)+F,
    f_s(T)=T^m+sum_(h=0)^(m-2)gamma_h*s^[7(m-h)]*T^h.

The scalar corrections start at order14, and F starts at j>7. Thus,
through order7 inclusive, A_s and R_s^m are IDENTICAL. This is the
load-bearing extra fact missing from an arbitrary polynomial-root ansatz.

Inductively every R_(7-i) is even in a. At order i its defining equation
is m*K^(m-1)*R_(7-i) equal to a coefficient of A_s minus the terms built
from earlier reference coefficients. The right side is even by induction;
the nonzero divisor K^(m-1) is even. Applying a->-a and subtracting forces
the quotient to be even. Therefore every coefficient is a polynomial
in g=a²,p=b; no fractional or negative g exponent is introduced.

Let nu denote the maximum (1,-1)-weight in these ordinary g,p variables.
For nonzero polynomials nu(UV)=nu(U)+nu(V), because their nonzero initial
forms multiply in an integral domain. Here nu(H)=2. Suppose inductively
that all earlier R_(7-h) have nu<=2. Every earlier-product contribution
at order i in R_s^m has nu<=2m, as does [s^i]A_s by the FULL source
support inequality. If R_(7-i) had nu>2, its contribution
m*H^(m-1)*R_(7-i) would have nu>2m and could not cancel. Hence nu<=2
for every reference coefficient. Their (2,1)-degrees are 7-i. Together
with ordinaryness this proves supp(R) contained in Delta, not merely a
statement about its leading form. The argument uses j>7; it is not
asserted in a separated regime with a smaller j.

On nu=2 the integer equations I-J=2 and 2I+J<=7 leave only the points
(3,1) and (2,0). Thus the root's exposed face is -g³p+d*g². Homogenizing
weights(g,p)=(2,1) makes its second term d*s³*g². The exact source face is
(-1)^m*g^(2m)*(gp+s³)^m. Compare its s³ coefficient with that of R_s^m;
all other antiweights are smaller and cannot contribute. Since the top
coefficient is (-1)^m and m!=0, this gives d=-1. Thus the ENTIRE root
face is -g²*(gp+1); the s³ comparison also proves its endpoint is attained.

## 3. Exact polynomial cubic, not a formal assumed shape

The substitution g=p²-Z is a polynomial automorphism preserving the
weighted degree (g,p)=(2,1), or equivalently (Z,p)=(2,1). The bound
I<=3 in Delta shows that R has degree at most3 in Z. Its Z³ coefficient
is exactly p: a constant coefficient would contribute an uncancellable
g³ term of antiweight3, while the coefficient of p is fixed by the top H.
All other weighted-degree7 terms are already in pZ³. Therefore

    R=pZ³+A2(p)Z²+B4(p)Z+C6(p),
    deg A2<=2, deg B4<=4, deg C6<=6.

The coefficient of g² at p=0 is A2(0), so the root face just proved
gives A2(0)=-1. This is (1). No division by p has occurred in this
polynomial representation or in the affine change in the conclusion.

Use the homogeneous versions

    a_s=a2*s*p²+a1*s²*p-s³,
    b_s=sum_(h=0)^4 b_h*s^(5-h)*p^h,
    c_s=sum_(h=0)^6 c_h*s^(7-h)*p^h,
    R_s=pZ³+a_s Z²+b_s Z+c_s.

Here a_s,b_s,c_s are scalar coefficient polynomials of R, not the
original receivers or the rescaled ODE polynomials.

At either actual triple line put X=p and zeta0=p^(1/3)Z. The reference
is now an exact cubic in zeta0 over the Laurent coefficient field, with
leading coefficient1 and quadratic coefficient a_s*p^(-2/3). Its exact
depression uses

    zeta=p^(1/3)*(Z+a_s/(3p)),
    alpha=p^(-4/3)*(p*b_s-a_s²/3),
    beta=c_s-a_s*b_s/(3p)+2a_s³/(27p²).              (4)

This is also the right-coordinate algorithm in16l for this particular
reference. At each iteration its coefficient remains a cubic, so the
part divisible by zeta² is a CONSTANT multiple of zeta². Every step
is a translation, and the unique total translation killing the quadratic
coefficient is the one displayed. Thus this calculation does not assume
that an arbitrary nonlinear normal form has the same named coefficients.
Both actual triple charts give the same (4), since the reference is even
in a and depends only on a²=p²-Z.

## 4. Coalescence removes all remaining nonconstant coefficient functions

For m>=4 the resonance satisfies 4<2r<5 and 6<3r<7. Integral original
orders therefore force ord_s alpha>=5 and ord_s beta>=7. The first
condition in (4) compares the coefficients of orders1 through4 and gives

    b4=0,
    b3=a2²/3,
    b2=2a2*a1/3,
    b1=(a1²-2a2)/3.                                 (5)

Only b0 is unrestricted. This comparison uses the exact p*b_s-a_s²/3,
so in particular the sign from A2(0)=-1 is retained.

Set h=(a2*p+a1)/3, z=Z+h. Direct expansion of the cubic, without any
high power of A or B, gives the coefficients

    z²: A2-3p*h=-1,
    z : B4-2A2*h+3p*h²=B4-3p*h²+2h=u,
    constant: V(p)=C6-B4*h+A2*h²-p*h³,
    u=b0+2a1/3.

Equations (5) prove that the coefficient of z is this constant u;
deg V<=6. Homogeneously, the affine shift is
z=Z+(a2*s*p+a1*s²)/3, and the same expression becomes

    R_s=p*z³-s³*z²+u*s⁵*z+V_s(p),
    V_s(p)=sum_(h=0)^6 v_h*s^(7-h)*p^h.

Depressing the last remaining quadratic term now gives exactly

    alpha=u*s⁵*p^(-1/3)-s⁶/(3p^(4/3)),
    beta=V_s(p)+u*s⁸/(3p)-2s⁹/(27p²).               (6)

The last two terms of beta have orders8 and9, so ord_s beta>=7 forces
v_h=0 for h=1,...,6. Consequently V_s=v*s⁷ and (2) follows at s=1.
Conversely every reference of the form (2), with the indicated weighted
homogenization, has alpha of order>=5 and beta of order>=7. Its splitting
scale is therefore at least7/3, strictly greater than the resonance r.
This converse concerns the REFERENCE only; it constructs no A,B,F or
solution of the source equations. Coalescence at one of the two triple
lines gives the same reference condition at the other; it does not turn
the source problem into two independent choices of u,v.

## 5. Full smaller rectangles and the actual negative-weight initial

Put rho=(7m-1)/(3m) for the local rescaling parameter, and r0=q+1,
so m=3r0+1. Denote the transformed ENTIRE polynomials by A'(p,z),B'(p,z).
The substitutions g=p²-Z and Z=z-h(p) do not increase weighted degree
for weight(p,z)=(1,2): all terms of g have weight<=2. They also do not
increase antiweight weight(p,z)=(-1,1): g has leading term -z of
antiweight1, while its other terms have antiweight<=0. Consequently
every monomial p^i*z^j of the e-th output, e=m or n, still satisfies

    i,j>=0, i+2j<=7e, j-i<=2e.

Both entire exposed faces transform exactly: the weighted top is
p^e*z^(3e), because the invertible homogeneous substitution g=p²-z
sends H exactly to p*z³. The opposite face is z^(2e)*(pz-1)^e, because
its monomial substitution g->-z,p->p is injective. Lower-weight terms
cannot reach either face, so no unspecified noncancellation is assumed.

Let A'_s=s^(7m)*A'(p/s,z/s²). In section4's exact depressed coordinate,

    z=p^(-1/3)*s^rho*Y+s³/(3p).

Here 3>rho. The leading s-order contributed by a monomial p^i*z^j is

    7m-i-2j+rho*j
       =7m-(mi-r0*j)/m,

and its coefficient is p^(i-j/3)*Y^j. For a fixed j the order determines
i uniquely, and different j have different Y powers. These leading
contributions therefore cannot cancel. Accepted16l proves that the
valuation of the FULL A'_s in this chart is3m*rho=7m-1 and of the FULL
B'_s is3n*rho=7n-n/m; it is not only a statement about their reference
parts. Thus their maximum weight(p,z)=(m,-r0) is exactlym andn:

    mi-r0*j<=e for every monomial of the e-th output.           (7)

Combine twice (7) with r0 times i+2j<=7e. Since
2m+r0=7r0+2, this gives (7r0+2)*i<=e*(7r0+2), hence i<=e.
The other inequality then gives j<=i+2e<=3e. The already attained
monomial p^e*z^(3e) is the coordinatewise upper corner, proving both
whole rectangles and the exact ordinary degrees4e.

Finally replace Y by p^(1/3)*z in16l's initial expressions
P=p*C(Y^m/p^(1/3)), Q=p^(5/3)*Y*D(Y^m/p^(1/3)). Because
(m-1)/3=r0, the actual negative-weight initials are exactly

    A'_initial=p*C(T), B'_initial=p²*z*D(T),
    T=p^r0*z^m,
    n*T*C'*D-m*T*C*D'-C*D=-c.

The bracket's top is c*p², but its ENTIRE target is still (3). Earlier
weight corrections may interact before the lower target terms occur;
no first-order deformation around these initials is asserted exhaustive.

## 6. Exact target, useful boundary chart, and limitations

The Jacobian of (g,p)->(p,Z=p²-g) is +1, and (p,Z)->(p,z=Z+h(p))
also has determinant1. Since g=p²-z+h(p), the chain rule gives (3).
Neither the term -c*z nor the two affine-in-p terms may be discarded.
The change is genuinely polynomial with polynomial inverse; the fractional
depression in (4) is used only for analysis, never as a source automorphism.

The reference itself has a transparent rational fibration. If t!=v then
R=t is parametrized by z!=0 and

    p=(t+z²-u*z-v)/z³.

Thus this generic reference fiber is a copy of the multiplicative line.
This says NOTHING about the generic fiber of A, which has a nonzero
remainder F and may have different topology. On z!=0 the coordinate
change (p,z)->(R,z) has determinant z³; consequently its exact target is

    [A,B]_(R,z)=c*z^(-9)*[
       (R+z²-u*z-v)²
       +(a2/3)*z³*(R+z²-u*z-v)
       +(a1/3)*z⁶-z⁷ ].                             (8)

This is an identity in a localization, not a claim that arbitrary
Laurent pairs lift back to polynomials. It identifies the missing finite
boundary z=0 explicitly. The right side has no z^-1 term: its numerator
has degree at most7 in z, so a residue argument ignoring changes in A
cannot itself produce a contradiction.

Controls, all by hand and no constructed Keller source:

- R=pZ³-Z² satisfies both normalized root faces and coalesces: (6) with
  u=v=0 has splitting scale3. The opposite face does NOT immediately
  forbid coalescence.
- Adding p⁴*Z preserves the root polygon and both faces, but contributes
  an order1 term to alpha. It violates (5) and is not coalesced at r>2.
  Thus the normal-form conclusion genuinely uses coalescence, not just
  a Newton support census.
- If F could start at order<=7, the order-by-order identity with R_s^m
  would fail at that order and the polygon induction would no longer
  prove its claim. No separated reference is being classified here.
- A rational reference fiber does not make A a rational polynomial;
  replacing A by f(R) would remove the nonzero F required by16l.

## 7. Read scope, dependencies and next use

Scientific imports: accepted16k's RECEIVER CONCLUSION as the explicit
hypotheses in section1, and accepted16l's finite construction/coalesced
j,r conclusions. No unreviewed wrong-target or linearized-deformation
result is a premise. No separated-task body was read.

Current hashes checked before the current selected reads:

- xmodel/f10-all-parameters-source-interface-astra-20260909.md:
  cc6edcb767bd22bddcdbe7dd89cfe1cfd260f66b145122889d50edd585c7c021.
  Current WHOLE read, including the source's stated primary-import scope.
- xmodel/f10-coalesced-resonance-reduction-coordinator-20260909.md:
  d225258c605617037d4d74b2cdce9430ce1fc8ac49e81d01dc1b125d76ad0ee1.
  Root-authored and previously WHOLE; current reread of sections3–end.
- Their accepted Fable gates were previously collected receipt-first and
  read WHOLE; current hashes rechecked, not a new whole-read assertion:
  sourcegate9dc342bdd00a4fc7e1a22d5540a4544962acf7eb2f699fc4ae2e93bdb1fb0052;
  localgate221a5d584c5a412c9b1ac8b51f6bb936e616108b40391a0cb0a50759465f38ff.

A targeted web query about polynomial maps with linear Jacobian returned
proper-map and unrelated classifications; no web theorem or source is used
in this proof. It was not a broad campaign sweep or a novelty census.
All new algebra above is manual. Only this leased partial report and its
transactional publication metadata are owned; no shared/public/protected
write, CAS, source-power expansion, matrix computation or AWS action.

The next useful consumer must retain the full A/B corrections, the exact
target (3) or (8), and ordinaryness across the displayed finite boundary.
No conclusion about the actual112/196 exception, an all-q F10 exclusion,
properness of a complete ideal, or JC2 is made. Different-model review is
required before promotion or a dependent research lane.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only check; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14741`.
- Body SHA-256:
  `978d296382b3aaee0aded2d59ffb771114f56b24b5d28a836b3337773deaa9c8`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
