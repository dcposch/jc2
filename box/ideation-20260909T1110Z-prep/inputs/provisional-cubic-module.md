# F10 compressed boundary: the complete cubic module

2026-09-09. Pure manual algebra; ZERO mathematical subprocesses. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. **PROVISIONAL, for independent review.** The ring theorem below has its own explicit elementary hypotheses. Its interpretation for actual F10 sources is conditional on the provisional full-source compression; no live gate is a premise.

## 1. Exact result and source boundary

Let K be the characteristic-zero coefficient field of the stated source, and let u,v0 be any scalars of K, including zero. In K(p,z) put

    S=p z^3-z^2+u z,  R=S+v0,  t=z^-1,
    p=t-u t^2+S t^3,
    x=S t=p z^2-z+u,
    y=S t^2-u t=p z-1.

The two elements S,p are algebraically independent. Write B=K[S,p]. Then the WHOLE intersection in this fixed common field is

    T := K[p,z] intersection K[S,t]
       = B + B x + B y,                         (1)

with a unique expression on the right. As a B-algebra it has exactly the presentation

    T = B[X,Y]/(X^2-uX-SY,
                 XY+X-Sp,
                 Y^2+Y-pX+up),                (2)

where X maps to x and Y to y. In particular T is finite FREE of rank three over B, not merely generically of rank three. No inversion of u, S or p occurs in this statement. This identifies the common finite-boundary ring, not a polynomial coordinate system on it and not a degree-three Keller map.

Sections 4–5 give necessary AND sufficient, finite polynomial divisibility tests for an arbitrary polynomial of t-degree at most three or five to lie in T. Thus they replace the compression parent's unspecified negative-z coefficient conditions exactly, without dropping their special fibers. Sections 6–7 specialize the module bounds to the entire compressed source pair and retain its entire Jacobian equation.

The permitted parents, freshly pinned before WHOLE reads, are:

- Compression: `xmodel/f10-source-polynomial-cubic-quintic-compression-astra-20260909.md`, SHA-256 `9b77ece0a8076d0a8ef498f0a9c152e1de52e85c7ce3cd6b575d5475d0d3337c`.
- Reference: `xmodel/f10-coalesced-source-reference-coordinator-20260909.md`, SHA-256 `e87e5133a0072c309b6acdc4ab692b07bc4f6f545214c37df39a3042edf1ef70`.

Their precise status/read perimeter is in the owned READ-SCOPE.md and PINS.json. No other mathematical text was read. In particular the compression's claimed identification with the actual source intersection is imported CONDITIONALLY; the proof of (1)–(2) below uses only the displayed coordinate formulas.

## 2. A free three-element algebra, with no hidden relations

The displayed rational inverse formulas give K(S,t)=K(p,z), so S,t are algebraically independent. Work in this polynomial chart K[S,t], substituting p=t-u t^2+S t^3. A polynomial in p of positive degree over K[S] has positive t-degree, with nonzero leading coefficient because S is an indeterminate. This proves the algebraic independence of S,p.

Over K(S,p), the element t has degree exactly three. Indeed

    S T^3-u T^2+T-p

is irreducible: in K(S)[T,p] it has p-degree one and coefficient of p equal to -1. A factor of p-degree zero would have to divide -1 in K(S)[T], so is a unit. Gauss's lemma passes this irreducibility to K(S,p)[T]. The leading coefficient S is nonzero in that field. Consequently 1,t,t^2 are linearly independent over K(S,p). The triangular change

    x=S t,  y=S t^2-u t

has nonzero diagonal coefficients S,S, so 1,x,y are also independent over that field and hence over B.

Direct factored identities in the common field give

    x^2=u x+S y,
    x y=S p-x,
    y^2=p x-u p-y.                             (3)

For the last identity, use y=t(x-u) and p=t(y+1), yielding y(y+1)=p(x-u). For the middle one, multiply the equation for p by S and subtract x. These are identities of polynomials in both charts, not identities verified at sampled points.

It follows that the B-span T0=B+Bx+By is a subring. In the abstract quotient (2), every monomial in X,Y reduces to a B-linear combination of 1,X,Y: each quadratic in X,Y has a replacement of strictly smaller X,Y-degree. The quotient maps onto T0, and independence of 1,x,y shows that this map has zero kernel. Thus (2) presents T0 exactly and T0 is free of rank three. Generic irreducibility was used only to prove independence, not to remove any closed fiber from the result.

## 3. The WHOLE intersection, and the two charts

The functions x,y are ordinary in both charts, so T0 is contained in the intersection. For the reverse containment the following two identities are decisive:

    z=(x-u)/y,     t=p/(y+1).                  (4)

They hold in the common field because x-u=zy and y+1=pz. Thus

    K[p,z] subset T0[y^-1],
    K[S,t] subset T0[(y+1)^-1].                (5)

The localizations on the right intersect in T0. Explicitly, if f belongs to both, then y^N f and (y+1)^M f lie in T0 for some nonnegative N,M. The ideals (y^N) and ((y+1)^M) are comaximal: powers of two comaximal principal ideals remain comaximal. A Bezout combination equal to one therefore expresses f as a T0-linear combination of these two elements of T0. This proves f belongs to T0, and proves (1). There is no normality, integral-closure or generic-regularity shortcut here.

This also verifies the suggested projective geometry entirely algebraically. In the chart w=1 the equation

    p z^3-z^2 w+u z w^2-S w^3=0

gives K[p,z]; in the chart z=1 it gives K[S,t], with t=w/z. Their common overlap has z and t invertible. On the first chart, the complement of D(y) has y=0, hence pz=1; it lies in the second chart and in D(y+1). On the second chart, the complement of D(y+1) has y=-1=t(St-u), hence t is invertible; it lies in the first chart and in D(y). Furthermore

    K[p,z][y^-1]=T0[y^-1],
    K[S,t][(y+1)^-1]=T0[(y+1)^-1]

by (4). These two principal opens cover Spec T0 since y and y+1 generate the unit ideal. They identify their gluing with the entire projective cubic, including both finite-boundary charts. Thus that cubic is indeed affine and finite flat of degree three over Spec B, by the already proved free algebra presentation. No external proper/quasi-finite theorem is needed.

Specialization is not suppressed: every fiber of (2) has vector-space length three, even when it is nonreduced. For example at S=p=u=0, its algebra is

    K times K[epsilon]/(epsilon^2).

To see this, -y is an idempotent; on its zero component x=y=0, while on its one component y=-1 and x^2=0. This is a control against a false three-distinct-sheets or etale assertion. A fiber may be nonreduced without contradicting the two global charts or freeness. We do NOT identify a specialization of an intersection of fields with a new intersection of specialized fields.

## 4. A degree filtration with no cancellation ambiguity

For a nonzero a(S,p) in B of p-degree i, its image in K[S,t] has t-degree 3i and leading coefficient S^i times its leading p-coefficient. The same calculation gives

    deg_t(b(S,p)x)=3 deg_p(b)+1,
    deg_t(d(S,p)y)=3 deg_p(d)+2.                (6)

The three displayed degrees are distinct modulo three. In an expression a+bx+dy the largest of the three is therefore unique and cannot cancel. This applies to every coefficient polynomial, not only a generic coefficient value. Zero summands can simply be omitted.

Consequently for f in T of t-degree at most N, its unique module expression has

    deg_p a <= floor(N/3),
    deg_p b <= floor((N-1)/3),
    deg_p d <= floor((N-2)/3),                 (7)

with a negative bound meaning that the corresponding summand is zero. These bounds are also sufficient. In particular degree three gives four K[S] coefficient slots, and degree five gives six K[S] coefficient slots. These are module descriptions, not dimensions of a source solution space.

## 5. Exact cubic and quintic inverse-pole tests

All divisions in this section mean EXACT polynomial division by a displayed power of S in K[S]. They are divisibility requirements, never a localization or an assumption S!=0. Coefficient polynomials may equivalently be written in R=S+v0.

### 5.1 Arbitrary degree at most three

Write f=sum_{i=0}^3 f_i(S)t^i. Then f belongs to T if and only if the following three successive quantities are polynomials in S:

    a=f_3/S,
    d=(f_2+u a)/S,
    b=(f_1-a+u d)/S.                           (8)

When they are polynomials, the unique expression is

    f=f_0+a p+b x+d y.                         (9)

Proof: (7) leaves exactly this form. Substituting p,x,y shows its t^3,t^2,t^1 coefficients to be Sa, -ua+Sd, a+Sb-ud, respectively. Solving these equations from the highest degree gives (8). The constant coefficient is f0, since p,x,y all vanish at t=0. This proves necessity and sufficiency.

Equivalently, without recursively named quotients, the three conditions are

    f_3 in (S),
    S f_2+u f_3 in (S^2),
    S^2 f_1-S f_3+u S f_2+u^2 f_3 in (S^3).   (10)

Thus all negative z powers in f(pz^3-z^2+uz,z^-1) vanish precisely when (8), or (10), holds. No other negative-power equation is implicit or omitted.

### 5.2 Arbitrary degree at most five

Write f=sum_{i=0}^5 f_i(S)t^i. Define successively

    d_star = f_5/S^2,
    b_star = (f_4+2u S d_star)/S^2,
    a      = (f_3+u S b_star-(S+u^2)d_star)/S,
    d      = (f_2+u a-S b_star+u d_star)/S,
    b      = (f_1-a+u d)/S.                    (11)

Then f lies in T if and only if ALL five displayed quotients are polynomials. Its unique expression is

    f=f_0+a p+(b+b_star p)x+(d+d_star p)y.      (12)

For an explicit manual check of the signs, the only extra products needed beyond the cubic case are

    p x = S t^2-u S t^3+S^2 t^4,
    p y = -u t^2+(S+u^2)t^3-2u S t^4+S^2 t^5.

Together with (9), these give, in descending order, coefficients

    f_5=S^2 d_star,
    f_4=S^2 b_star-2u S d_star,
    f_3=S a-u S b_star+(S+u^2)d_star,
    f_2=-u a+S d+S b_star-u d_star,
    f_1=a+S b-u d.

This proves (11) exactly. These are degree-at-most-five factored checks, not an expansion of an actual large source output.

### 5.3 Manual changed-object controls

The element t is NOT in T: (8) gives a=d=0 and b=1/S. It passes the first two cubic tests and fails the last. Thus deleting the last test genuinely changes the ring, despite preserving ordinaryness in the t-chart.

The elements x=St, y=St^2-ut, and p=t-ut^2+St^3 pass and reconstruct exactly their named module basis expressions. Changing y to St^2 passes if u=0, when it equals y, but fails if u!=0: (8) gives d=1 and b=u/S. Thus the test retains the special u=0 stratum instead of imposing u!=0 or erroneously dropping it.

The leading t-coefficient condition alone is insufficient even for the cubic: St^3 has the permitted leading shape, but its inverse is p-z^-1+u z^-2 and is not ordinary for any scalar u. For u!=0 the second test in (8) fails; for u=0 the last one fails. This is a literal changed polynomial, not a claim of a source/Jacobian counterexample.

## 6. The entire compressed A/B pair in this module

Import only the compression's stated necessary hypotheses: r>=1, m=3r+1, n=5r+2, the full coefficient bounds deg_S A_i<=m-ri and deg_S B_i<=n-ri, and

    A_3=kappa_A S, B_5=kappa_B S^2,
    kappa_A kappa_B=c!=0.

The source inverse-pole conditions are now exactly equivalent to unique representations

    Ahat=A0(S)+kappa_A p+b_A(S)x+d_A(S)y,

    Bhat=B0(S)+a_B(S)p
          +(b_B(S)+b_star(S)p)x
          +(d_B(S)+kappa_B p)y.                (13)

Here the recursively recovered coefficients in (8), (11) satisfy

    deg A0<=m,  deg b_A<=2r,   deg d_A<=r,
    deg B0<=n,  deg a_B<=2r+1,
    deg b_star<=r, deg d_B<=3r+1, deg b_B<=4r+1. (14)

For example d_A=(A_2+u kappa_A)/S has degree at most r; b_A then has degree at most 2r. In the quintic recursion d_star=kappa_B, followed by the bounds r, 2r+1, 3r+1, 4r+1, in that order. These statements use exact polynomial quotients, not rational functions with removable poles assumed. Conversely (13) with these bounds gives all the original coefficient degree bounds upon the displayed substitution. The exact original top/ODE faces, monicity and Jacobian are additional constraints on these coefficients, not consequences of these bounds alone. In particular the compression's monicity says A0 and B0 have leading coefficients one in their respective degrees m,n.

This is a complete bounded-module parametrization of the inverse-ordinary part of the proposed compressed client. It introduces no hidden localization, new gauge, missing coefficient or assumption on the values at S=0. All coefficients in (13) are ordinary one-variable polynomials.

## 7. Retaining the FULL bracket rather than a cubic-norm shortcut

There is a short exact derivative rule for arbitrary f=a(S,p)+b(S,p)x+d(S,p)y. Write

    V_f=a_p+b_p x+d_p y,
    W_f=a_S+b_S x+d_S y,
    Q=1-2u t+3S t^2,

where coefficient derivatives treat S,p as independent. In the actual (S,t) chart,

    f_S=W_f+t^3 V_f+b t+d t^2,
    f_t=Q V_f+S b+(2S t-u)d.                  (15)

These follow just from p_S=t^3, p_t=Q, x_S=t, x_t=S, y_S=t^2, y_t=2St-u. For the entire two polynomials (13), their exact retained equation is

    (Ahat_S)(Bhat_t)-(Ahat_t)(Bhat_S)
       = c(1+u t-ell t p-t p^2),               (16)

with the derivatives given by (15) and p=t-ut^2+St^3. Since R=S+v0, the bracket orientation is unchanged. Formula (16) retains every coefficient and every term of the compression's Delta; no discriminant, norm, leading coefficient, or three-sheet trace replaces it.

The ring T need not even be closed under the (S,t) bracket: direct differentiation gives [x,p]_(S,t)=2p-t, which is NOT in T because t is not. Thus its rank-three algebra structure alone cannot justify a polynomial Poisson-coordinate or norm argument. Formula (15) is an evaluation rule in the whole polynomial chart K[S,t], not a claim that this bracket restricts to T.

Conditionally using the compression's u=-h and its full-source ring identity, (1) identifies exactly that common actual-source/receiver ring. Conversely module membership plus the same identification supplies inverse ordinaryness. This report does not verify the specified receiver support, complete faces, canonical/coalesced attachment or full equation (16) for any candidate, or claim they follow just from module membership. A separately proved sufficient endpoint need not reproduce the historical necessity chain; no such sufficiency theorem is asserted here. The map Spec T to Spec K[S,p] has length-three fibers; neither coordinate pair (Ahat,Bhat) nor the original source map is thereby assigned field degree three. No source point, proper ideal, unit certificate, F10 exclusion, or JC2 conclusion is proved.

## 8. Scope and completion

The root scratch rank-three proposal is established as an exact standalone ring theorem, with the precise presentation and complete degree-three/five inverse tests. This is stronger than checking a generic reference fiber and narrower than solving the source equations. It resolves the named inverse-polynomiality ambiguity as a finite algebraic module condition, not by discarding it.

All identities and controls were proved by hand. No mathematical subprocess of any size, source expansion, primary lookup, peer/live gate read, CAS, solver, AWS action, new agent, canonical edit, or public write occurred. Only the two named parents and publication-mechanics help were read. Source pin postchecks and immutable publication custody are retained in the owned box. Independent review is required before promotion. No continuation or compute authority is implied.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only check; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15665`.
- Body SHA-256:
  `aa4468209b5a2ea91cf7b0c177ff9d12d46141ea57e4de7d138b574c1d671901`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
