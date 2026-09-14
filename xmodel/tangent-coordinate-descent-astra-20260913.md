# A global coordinate-descent obstruction for a clean tangent-sweep stratum

Astra /root/execution_reliability, September13,2026. Actual first UTC
08:40:35. MANUAL / PRODUCER-CHECKED / UNPROMOTED, with the named classical
curve theorems retained as imports. ROOT collector. Original network cutoff
08:52UTC, reserve08:58UTC/HARD09:02UTC unchanged. No scientific execution,
AWS action, new agent, shared edit or protected-tree/mirror access.

## Statement: arbitrary target coordinates, explicit extra hypotheses

Use the WHOLE polynomial tangent-sweep triple from TASK, over C:

    u=1+xy, gamma=gamma0+a*xy+b*x^2*z, w=gamma*u, C=x*gamma,
    F=(C,D,E)=(C,(p(w)+2gamma)/C,(q(w)+gamma*w)/C^2), b!=0.

Retain q'=w*p'/2 and both full polynomial divisibilities. Write
p=w*A(w), q=w^2*B(w), as forced by admissibility. Consider the UNBOUNDED
stratum with

    deg p=d>=5, p1=p'(0)!=0, gcd(A,B)=1.                 (S)

**Claim. There is no polynomial target coordinate h(C,D,E) whose pullback
h(F) is a polynomial source coordinate.** No homogeneity, affine-linearity,
tameness, or degree bound on h is assumed.

The conditions (S) are additional, NOT consequences asserted for every
admissible p. This report constructs no new ambient example and does not
classify the remaining p1=0 or gcd(A,B)!=1 strata. The accepted actual plane
mapping-degree<=5 closure is not used or re-proved.

Classical imports used below are: each irreducible nonproperness component
of a generically finite polynomial A2 map admits polynomial A1 parametrization
(Jelonek), and every closed A1 in A2 is a coordinate line
(Abhyankar--Moh--Suzuki). These are the same standard curve inputs appearing
in AUDIT's promoted ASYMPTOTIC-COMPLEMENT rigidity entry, targeted read
3668--3692; this tranche is not a fresh primary-source audit of them.
No Abhyankar--Sathaye implication from an A2-like fibre is used.

## 1. The sweep hypersurface has a finite A2 normalization

Let Sigma be the closure of

    (C,w) -> (C,p(w)/C,q(w)/C^2), C!=0.

Define a polynomial map on A2_(C,v):

    nu(C,v)=(C, v*A(Cv), v^2*B(Cv)).                 (1)

Its image closure is Sigma. It is finite and birational under (S).
Indeed w=Cv is integral over the image ring, since p(w)=C*D has a nonzero
constant leading coefficient. Choose a(w),b(w) with a*A+b*B=1. Then

    v^2-a(w)*D*v-b(w)*E=0

is monic over the ring with w adjoined. Thus v is integral too, and
C[C,v] is finite over the image ring. Birationality follows from
C(p(w),q(w))=C(w): the extension degree divides both d and d+1 by the
degree formula for rational functions (or Luroth). Therefore nu is the
normalization of the irreducible hypersurface Sigma.

Every root alpha of p' is nonzero under (S), and at Cv=alpha,

    partial_v nu=(0,p'(Cv),(v/2)*p'(Cv))=0.          (2)

There is at least one such root. The finite birational normalization is
not an isomorphism, so Sigma is NOT normal, in particular not A2.
At C=0, nu maps isomorphically onto the parabola

    Psi=D^2-4*p1*E=0,

because B(0)=p1/4. Finiteness ensures that this is the entire reduced
intersection Sigma with C=0, not merely one visible chart.

## 2. A plane-coordinate lemma detects the inhomogeneous obstruction

**Lemma.** If s(C,v) is a polynomial coordinate and s_v vanishes on
Cv=alpha, alpha!=0, then s is affine in C.

On that hyperbola, s_C never vanishes, since s is a coordinate and s_v=0.
The Laurent polynomial s(C,alpha/C) therefore has derivative with no zeros
on C*. A nonzero Laurent polynomial without zeros is a monomial; integrating
shows s(C,alpha/C)=a*C^n+b, a!=0 and integer n!=0. (A C^-1 derivative
cannot be the derivative of a Laurent polynomial.) The coordinate fibre
s=b is an A1 disjoint from the hyperbola. Consequently Cv-alpha restricts
to a nonzero constant on this A1, so Cv is constant. A nonconstant A1
cannot lie in Cv=beta!=0, because its two polynomial coordinate functions
would then be units and hence constants. It follows that s=b is an axis.
Irreducibility of the coordinate fibre makes s-b a scalar multiple of C
or v; s_v=0 on the hyperbola selects C. This proves the lemma.

We also need its disconnected-fibre version. If a nonconstant polynomial
f on A2 has generic fibres which are disjoint copies of A1, then f=P(s)
for a polynomial coordinate s and a one-variable polynomial P. To see
this, straighten one generic A1 component to s=0 by Abhyankar--Moh--Suzuki.
Every component of every other generic fibre is disjoint from that axis,
so s is a nonzero constant on it. Infinitely many resulting parallel axes
force f to be independent of the other coordinate. This does not assume
generic connectedness or make any assertion about all special fibres.

For f=h composed with nu, the chain rule gives the polynomial identity

    f_v=p'(Cv)*(h_D(nu)+(v/2)*h_E(nu)).              (3)

If f=P(s) has the preceding generic-fibre property, P'(s) cannot vanish
identically on Cv=alpha: that would put a closed hyperbola inside a
coordinate A1 fibre. Equation (3) forces s_v=0 there. The lemma therefore
gives f=P0(C) for some nonconstant polynomial P0.

## 3. An actual coordinate pullback supplies precisely those A1 fibres

Suppose h and H=h(F) are coordinates. For general c the restriction

    F_c : S_c={H=c} -> T_c={h=c}

is a polynomial Keller map A2->A2 of degree N=d+1. Source/target coordinate
changes give the Keller assertion. Degree N survives over general c by
restricting a dense finite-etale rank-N open in the target; the coordinate
source fibre is irreducible and meets its preimage densely. This is not a
degree assertion about an arbitrary exceptional plane.

The polynomial f=h composed with nu is not constant. Otherwise Sigma
would be the entire irreducible coordinate hypersurface h=b, hence normal,
contradicting (2).

Here is the actual boundary attachment, rather than an assumed commutation
of nonproperness with every section. On C!=0 form the finite cover with
constant-leading-coefficient equation (rescaled to be monic)

    W(w)=q(w)+(w/2)*(C*D-p(w))-C^2*E=0.             (4)

The source over this open is exactly the complement of gamma=0 in this
cover, where gamma=(C*D-p(w))/2, x=C/gamma, and the inverse source stage
recovers y,z. The deleted locus is the sweep incidence (1). After a generic
cut h=c it is one-dimensional, not a whole surface component: f is
nonconstant, while the monic finite cover of the target surface is pure
dimension two. Thus these boundary points remain in the closure of the
source open. In its finite normalization they remain boundary points too;
equivalently, approaching gamma=0 with C!=0 makes x=C/gamma escape.
Their images are therefore actual nonproperness curves of F_c. Taking
closures includes their C=0 points, without asserting anything about an
arbitrary exceptional cut.

For general c the curve f=c in the NORMALIZATION A2 is smooth. The finite
map to Sigma intersect T_c is birational on each component, since a
generic cut meets the normalization's non-isomorphism locus only in
finitely many points. No curve component is contained in C=0 for general c.
It consequently gives the curve normalizations of the just-attached
nonproperness components. Jelonek's polynomial parametrization theorem
makes each such normalization A1. Thus the generic fibres of f are disjoint
A1s, and section2 proves

    h(nu(C,v))=P0(C), deg P0=k>=1.                  (5)

Choose c additionally so that P0(C)=c has k distinct nonzero roots and
c!=P0(0). No claim about the other fibres is needed.

## 4. The missing hyperplane sheets force the Euler contradiction

Put h0(D,E)=h(0,D,E), Z={h0=c}, and l=chi_c(Z). Equation (5) on the
parabola gives h0=P0(0) there, so Z avoids Psi=0 for this c.

The full C=0 source has two disjoint pieces x=0 and gamma=0; gamma0!=0
is forced by polynomiality and J(F)!=0. On x=0 the map to (D,E) is a
triangular isomorphism: D=k0*y with k0!=0, E=l0*z+m0*y^2 with l0!=0.
These forms also follow directly from weights (1,-1,-2) and the constant
Jacobian. On gamma=0, using coordinates (x,u) in C* times A1,

    D=(p1*u+2)/x, E=((p1/4)*u^2+u)/x^2,
    Psi=4/x^2.                                    (6)

This is a finite-etale degree-two cover of Psi!=0, with inverse data
x^2=4/Psi, u=(D*x-2)/p1. Therefore every point of Z has exactly THREE
source preimages on C=0: one from x=0 and two from gamma=0. Since N>3,
Z is itself in the nonproperness locus of F_c: properness near such a
point would give a finite-etale degree-N cover, contrary to that exact
fibre count. If h0 is constant, Z is empty for general c. Otherwise Z is
smooth for general c, and each of its components, being a nonproperness
component of F_c, is A1 by the same curve theorem. Hence in both cases

    l is a nonnegative integer,
    chi_c(S_c intersect {C=0})=3*l.                (7)

This is where the actual plane-source hypothesis matters. Without it,
the Euler characteristic of a generic h0 fibre need not be nonnegative.

It remains to count on C!=0, INCLUDING contacts of every order. The
generic fibre of (4) has N roots. Its derivative is gamma. At a deleted
root w0 its multiplicity is

    m(w0)=2+ord_(w0)(p').                          (8)

All remaining roots are simple. Deficits add over distinct tangency
parameters even if their images coincide at a node. By (5), the entire
deleted incidence over T_c intersect {C!=0} is exactly k disjoint A1s:
one whole w-line for each root of P0(C)=c. On each such line the Euler
integral of (8) is 2+deg(p')=N. Finite-map pushforward of constructible
Euler characteristic therefore gives

    chi_c(S_c intersect {C!=0})
      =N*chi_c(T_c intersect {C!=0})-N*k
      =N*(1-l-k).                                 (9)

Adding (7) and (9) yields the complete-fibre identity

    chi_c(S_c)=N-N*k-(N-3)*l <= 0,                 (10)

whereas the assumed source coordinate makes S_c=A2 and chi_c(S_c)=1.
This contradiction proves the stated clean-stratum claim.

## 5. Scope attacks, history and the changed test

The stratum is nonempty in arbitrarily high degrees, not an empty generic
condition. ROOT supplied the following manual family during this tranche;
the displayed identities and divisibilities were checked here by hand.
For any integer m>=5 set

    gamma0=1, a=-(m+1)/m, b=1,
    A(w)=(4-2*(m+1)*w^(m-1))/(m-1),
    B(w)=(1-m*w^(m-1))/(m-1), p=w*A, q=w^2*B.

Direct differentiation gives q'=w*p'/2. At w=1, A=-2, B=-1,
B'=-m and (1+a)*B'=1. These cancel the constant term of u*A(w)+2
and both the constant and x-linear terms of u^2*B(w)+u, respectively,
so the FULL x and x^2 divisibilities hold. The gamma divisibilities are
already built into p=w*A and q=w^2*B. Also p'(0)=4/(m-1)!=0;
common roots A=B would require 2/(m+1)=1/m, impossible. Thus (S)
holds and N=m+1 is unbounded. This is an instantiated known ambient
construction, not a claimed novel family, a degree6 search, or a plane
counterexample. No computation or different-model review is claimed.

The auxiliary hyperbola lemma genuinely needs the exact divisor and a
coordinate, not merely a submersion. Likewise generic rationality is not
enough: the argument uses normalization A1, not A1 with punctures. The
normalization proof uses gcd(A,B)=1 load-bearingly; dropping it can leave
unaccounted boundary charts. The p1!=0 condition is used both in (6) and
in the nonzero critical hyperbola. These are explicit residual strata,
not automatically excluded by a generic coefficient argument.

As an algebraic sign/control check on (10), h=C has k=1, Z empty, and
the formula gives Euler0, agreeing with its visible C* times A1 fibre.
It is not a new review of ROOT's already completed component calculation.
If one removes the A1/nonnegative-l consequence, (10) alone is NOT a
contradiction for N>3; negative l can compensate. Keeping that boundary
term is essential. No computational control was run.

The old rational S(x,y/x) pole obstruction was whole read and concerns a
different object. [Kistner--Shaska Proposition3.21](https://arxiv.org/html/2608.02863v1#S3.SS10)
blocks their particular graded rational substitution through a negative
Lambda power; it does not classify arbitrary target-coordinate pullbacks.
The present argument is not that homogeneous descent or a suspension claim.
The source construction scope was checked in
[Gao sections3.1--3.3 and3.5](https://arxiv.org/html/2608.00222v1#S3.SS3),
plus stage definitions/equations7--8 in section4.3; no whole-paper or
independent ambient-example audit is claimed. The two raw HTML acquisitions
were frozen and hashed before network cutoff. Selected theorem text, not
every byte of the HTML wrappers, was read.

Frozen task/map/protocol and the old tangent-sweep report were SHA-before-
WHOLE read. ROOT's completed component report was SHA-before-WHOLE read as
an additional same-model input, not FIRST. Targeted AUDIT history searches
found no exact hyperbola-coordinate/Euler closure; no exhaustive novelty
claim follows. ROOT independently reported the same Euler identity during
this tranche; that corroboration is not different-model review.

The decisive construction question has changed: any coordinate-descent
escape inside this literal unbounded family must violate at least one of
the two explicit clean-stratum conditions, or break a named proof bridge
under hostile review. There is no license for a degree4/5 search, a finite
coefficient farm, a generic-as-universal assertion or an automatic boundary-
stratum successor. ROOT may first commission ONE different-model review
of the normalization/curve-normalization/boundary/Euler chain. No JC2 proof,
counterexample, all-family closure or promotion is asserted.

No network request occurred after08:43:30UTC, before the08:52UTC cutoff.
PINS and terminal custody supply exact hashes and writer-idle time. The
only executed Python was the unchanged administrative finalizer.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13851`.
- Body SHA-256:
  `f2542caef4b109c68c73d9075a9c8b9c8318cfb55be0ad76ef9f78c80bc00b7f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
