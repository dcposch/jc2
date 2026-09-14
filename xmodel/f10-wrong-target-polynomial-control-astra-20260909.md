# A full wrong-target polynomial control, and an exact fixed-A cokernel

September9,2026; owner /root/model_productivity. **UNREVIEWED conditional polynomial construction and fixed-ansatz obstruction.** The ODE below is an EXPLICIT HYPOTHESIS. Its existence theorem or current review is not consumed. No source point, F10 receiver, Keller pair or JC2 conclusion follows. ZERO mathematical subprocesses; all identities are manual and factored.

## 1. Hypotheses and conclusions

Let K have characteristic zero, q>=0 be an integer, and put

    r=q+1,       m=3q+4=3r+1,       n=5q+7=5r+2.

Suppose C,D in K[T] are monic of degrees3,5 and satisfy

    n T C'D - m T CD' - CD = -c,       c!=0.                 (1)

Define actual ordinary polynomials, with no truncation,

    Z=p^2-g,       T=p^r Z^m,
    A=p C(T),     B=p^2 Z D(T).                            (2)

Then their ENTIRE Jacobian is

    [A,B]_(g,p)=c p^2,                                    (3)

not c g. Their complete supports lie in m Delta,n Delta, where

    Delta={I,J>=0: 2I+J<=7, I-J<=2}.

Their weighted(2,1) tops are H^m,H^n for H=pZ^3, their ordinary degrees are7m,7n, their g-degrees are3m,3n, and their unique ordinary total leaders are p^(7m),p^(7n). Both weighted top assertions are exact, not merely hull bounds.

The literal first weighted correction of A from H^m is

    lambda p^(2q+3) Z^(2m),       lambda=[T^2]C!=0,         (4)

at weighted deficit7q+9. This identifies the difference from the displayed top; it does not by itself assert a canonical source remainder under further reference normalization.

There is also a stronger exact obstruction WITH THIS A FIXED: no polynomial Btilde in K[g,p], of ANY degree or support, can satisfy

    [A,Btilde]_(g,p)=c g.                                  (5)

This last assertion follows from a one-character polynomial cokernel, proved in Section6. It does not exclude a different A with the same weighted top and additional source-compatible coefficients.

## 2. Whole chain rule, target and fields

The change of ordinary polynomial coordinates (g,p)->(p,Z), Z=p^2-g, has determinant

    det d(p,Z)/d(g,p)=1.

Consequently the bracket in(g,p) equals the bracket in(p,Z). In these latter coordinates, T=p^r Z^m and direct factored differentiation gives

    A_p=C+rT C',              A_Z=m p T C'/Z,
    B_p=p Z(2D+rT D'),        B_Z=p^2(D+mT D').

The displayed quotients are only shorthand for polynomials with nonnegative exponents; for example pT/Z=p^(r+1)Z^(m-1). The determinant is

    [A,B]=p^2{(C+rTC')(D+mTD')-mTC'(2D+rTD')}
         =p^2{CD+mTCD'-(2m-r)TC'D}.

Since 2m-r=n, equation(1) makes the brace c. This proves(3) coefficientwise as a full polynomial identity, not just in a formal local ring or modulo a factor. In particular no expansion of the large powers is needed.

At T=0, equation(1) gives

    C(0)D(0)=c!=0.                                        (6)

Every construction and calculation stays over the given K. No algebraic closure, scalar root, extra field extension, c=1 gauge, coordinate inversion or output swap is required. The existence of such C,D is not part of this conditional result.

The literal residual against the desired target is especially small:

    [A,B]-cg=c(p^2-g)=cZ.                                 (7)

It vanishes on Z=0, but is a nonzero polynomial, with nonzero first normal coefficient c. Thus coincidence of target restrictions to the triple-root locus cannot establish the full target.

## 3. Full supports, both top degrees and the missing opposite faces

Write C=sum_(i=0)^3 C_i T^i, C_3=1. A term p*T^i is p^(1+ir) Z^(mi). Every monomial in it has exponents

    I=t,       J=1+ir+2(mi-t),       0<=t<=mi.

They are nonnegative and satisfy

    2I+J=1+i(r+2m)<=1+3(r+2m)=7m,
    I-J<=i(m-r)-1<=3(m-r)-1=2m.

No assertion about which lower C_i vanish is needed. Similarly a term p^2 Z*T^j of B, 0<=j<=5, has

    I=t,       J=2+jr+2(1+mj-t),       0<=t<=1+mj,

and hence

    2I+J=4+j(r+2m)<=4+5(r+2m)=7n,
    I-J<=j(m-r)-1<=5(m-r)-1=2n.

These are full support inequalities for every term, not a top-only polynomiality claim. The coefficient field has characteristic zero, so the attained endpoints in the highest terms are nonzero.

The highest weighted terms are

    p*T^3=p^(1+3r) Z^(3m)=p^m Z^(3m)=H^m,
    p^2 Z*T^5=p^(2+5r) Z^(1+5m)=p^n Z^(3n)=H^n.

Here 1+3r=m, 2+5r=n and1+5m=3n. No lower index attains the same weight. The points(0,7e) and(3e,e), e=m,n, occur. The support inequalities imply ordinary degree at most7e, with equality only at I=0,J=7e, and g-degree at most3e, attained at(3e,e). This proves all asserted exact degrees and monicity in p.

However the entire opposite(1,-1) faces are SINGLE MONOMIALS:

    ell_(1,-1)(A)=(-1)^m g^(3m)p^m,
    ell_(1,-1)(B)=(-1)^n g^(3n)p^n.                        (8)

Indeed the maximum i or j is required to attain weight2e, and then the maximal g term inside the corresponding Z power is required as well. Every lower index has strictly smaller anti-diagonal weight. In particular A(g,0)=B(g,0)=0 and the vertices(2m,0),(2n,0) are ABSENT.

As a separate literal comparison, any source client requiring the fuller opposite face

    (-1)^e g^(2e)(gp+1)^e

is not satisfied by(8). The construction proves membership in the containing support polygon and the top faces, not these additional boundary equations. This comparison is conditional on that explicitly displayed boundary requirement; no source theorem is imported or promoted here.

Under the polynomial quadratic cover g=a^2,p=b, put K0=b(b^2-a^2)^3. The total tops become K0^m,K0^n and the bracket becomes

    2c a b^2,

NOT2c a^3. Their difference is2c a(b^2-a^2). The covered polynomials are even in a, and still have degrees7m,7n. Equality of the two targets along b^2-a^2=0 is again only equality on that divisor, not an ordinary polynomial identity.

## 4. The first correction coefficient really is nonzero

Write C(T)=T^3+lambda T^2+mu T+nu. Formula(6) gives nu!=0. To derive lambda!=0 solely from the assumed ODE, set

    f(x)=x^3 C(1/x),       d(x)=x^5 D(1/x),       a0=n/m.

Then f(0)=d(0)=1. Since3n-5m=1, reciprocal differentiation of(1) gives

    m f d'-n f'd=-c x^7.

Thus (log d-a0 log f)'=O(x^7), and formal integration in characteristic zero yields d-f^a0=O(x^8). As deg d<=5, coefficients6,7 of f^a0 vanish.

If lambda=0, then f=1+mu x^2+nu x^3. The two coefficient conditions are exactly

    (a0)_2 nu^2/2+(a0)_3 mu^3/6=0,
    (a0)_3 mu^2 nu/2=0,

with falling factorial notation. The rational number a0=n/m is neither0,1,2. Since nu!=0, the second equation forces mu=0; the first then contradicts nu!=0. Therefore lambda!=0, without importing an existence theorem or a review verdict.

The COMPLETE literal difference is

    A-H^m=lambda p^(2r+1)Z^(2m)+mu p^(r+1)Z^m+nu p.

Put j0=r+2m=7q+9. The weights of these three displayed terms are respectively7m-j0,7m-2j0,7m-3j0. The first has a nonzero coefficient; hence(4) is indeed the first correction. After the quadratic cover this is also its ordinary homogeneous deficit. The statement concerns the displayed polynomials, not an unproved transfer to a canonical source chart.

## 5. A literal first repair has an exact nonzero residual

The residual cZ in(7) gives a precise low-cost discriminator, not a vague instruction to solve a large system. For example the ordinary polynomial

    E0=-D(0)Z^2/2

satisfies

    [A,E0]=-D(0)Z(C+rTC').

Thus replacing B by B+E0 cancels the leading normal target discrepancy, but leaves the ENTIRE residual

    [A,B+E0]-cg=-D(0)Z{C(T)+rTC'(T)-C(0)}
      =-D(0)Z{(1+r)mu T+(1+2r)lambda T^2+(1+3r)T^3}.    (9)

This is NONZERO, because D(0)!=0 and1+3r!=0. If mu!=0 its first Z-order is m+1; if mu=0, lambda!=0 gives first order2m+1. The substitution K[T]->K[p,Z], T=p^rZ^m, is injective, so different powers cannot secretly cancel. E0 is a degree4 polynomial, lies within the containing support envelope for B, and leaves the top and its anti-diagonal maximum unchanged; it does not restore the missing opposite face.

No iterative correction, convergence, completed lift or source point is asserted. In fact the next section proves that no polynomial correction of B, however large and not necessarily of this form, can attain the desired target while A stays fixed.

## 6. A global polynomial cokernel with A fixed

Work in the ACTUAL polynomial ring K[p,Z], not a localization. Give it the integer grading

    wt(p)=m,       wt(Z)=-r.

Then wt(T)=0 and A=pC(T) is homogeneous of weight m. The derivation [A,-] raises this weight by r, since the coordinate bracket has weight shift -(m-r). Every polynomial is a finite sum of weight components, despite the grading having both signs.

Suppose a polynomial Btilde satisfied[A,Btilde]=cg=c(p^2-Z). The right side has distinct weights2m and-r. The component of weight-r MUST therefore be supplied by the component E of Btilde of weight-2r, and

    [A,E]=-cZ.                                           (10)

No other homogeneous component can contribute or cancel this component. Since m=3r+1, gcd(m,r)=1. Every ordinary monomial p^iZ^j of weight-2r obeys

    mi-rj=-2r,

so i=r*l and j=2+m*l for an integer l>=0. Consequently the ENTIRE allowed component has the form

    E=Z^2 F(T),       F in K[T].

Direct factored differentiation now yields the exact operator

    [A,Z^2F(T)]
       =Z {m T C F'+2r T C'F+2CF}.                        (11)

If F is nonzero of degree s>=0, with leading coefficient f_s, the brace in(11) has degree s+3 and leading coefficient

    (ms+6r+2) f_s.

This coefficient is nonzero in characteristic zero: m,r are positive integers, C is monic cubic, and f_s!=0. Therefore the brace cannot equal the nonzero constant-c. If F=0, it is zero and also cannot equal-c. Equation(10) is impossible.

This proves(5) for every polynomial Btilde, with no degree cutoff, no assumption on its other weight components, and no formal-series-to-polynomial step. Equivalently the nonzero target character represented by Z is outside the polynomial image of this fixed-A derivation. A formal or localized correction could evade the finite-degree comparison, so it is not licensed by this argument.

The fixed-A obstruction actually uses only this explicit monic cubic C and the integers r,m; it does not use the existence of D or a prospective ODE gate. But it does NOT apply to arbitrary A with the same leading H^m. Changing A can change the derivation and its grading, so this is not a source-family exclusion by analogy.

## 7. Manual controls, provenance and scope

These controls are literal calculations, never executed tests or source points:

- Omitting the coordinate determinant or reversing(p,Z) would flip the sign. The direct determinant1 and2m-r=n fix the whole bracket as+c p^2.
- Changing only the claimed target from c p^2 to cg leaves the nonzero residual cZ. Agreement on Z=0 is insufficient; the cover residual2ca(b^2-a^2) makes the same point.
- The explicit E0 changes the whole polynomial B and cancels that first residual jet, but formula(9) remains nonzero. This is an actual failed polynomial correction, not a hardcoded zero test.
- In the fixed-A operator, F=1 gives2C+2rTC', whose cubic coefficient is2+6r!=0. Higher polynomial F cannot fix this by cancellation: its leading multiplier is the displayed ms+6r+2. Allowing Laurent/formal F is a different ring and is expressly outside the conclusion.
- Positive control OUTSIDE the cubic hypothesis: for a nonzero constant nu, take A=nu*p and Btilde=(c/nu)(p^2 Z-Z^2/2). Then[A,Btilde]=c(p^2-Z)=cg. Thus the fixed-A argument does not prohibit the monomial target in general; the positive degree of the specified C is load-bearing. This is not asserted to obey the cubic/quintic ODE hypotheses.
- The claimed containing polygon cannot substitute for fixed boundary coefficients: both missing(2e,0) vertices and the single-monomial faces(8) are exact failed boundary requirements.

The only mathematical parent is the explicitly hypothesized ODE(1). Neither its producer/gate nor root's optional coalesced reduction was read or used. No external theorem, current peer, source body, protected tree, AWS/SSH, mathematical subprocess, CAS, polynomial expansion by tool, coefficient builder, checker, solver or additional agent was used. The small reciprocal coefficient identities, all support inequalities and the cokernel are manual factored arguments.

This is a conditional wrong-target polynomial control with a proved obstruction to correcting B ALONE. It supplies no guarded receiver/source point, no standalone-ODE impossibility, no uniform F10 exclusion and no JC2 claim. The exact next missing source issue is whether a genuinely different, source-compatible A can meet the full target; this report gives no permission or theorem about that change.

The owned INPUT.md and READ-SCOPE.md freeze this task's hypothesis and read perimeter. Own whole/open check precedes the completion marker and artifact transaction. Terminal custody records current pins; all writers become IDLE at handoff, with no follow-on authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13114`.
- Body SHA-256:
  `5c10af2bdd1727b7ac34d0896b60ecb49cd03eb76a709aac2bea53f4d0bfb600`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
