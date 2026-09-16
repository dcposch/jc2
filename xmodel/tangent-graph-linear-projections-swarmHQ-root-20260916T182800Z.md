# All-seed tangent graphs: no linear plane projection is Keller

Producer: swarmHQ ROOT (Astra assigned context; exact hosted model not exposed).
Date: 2026-09-16 18:28 UTC.
Basis: 670ac5214197aea555a2aa590e01ce5974a089c4.
Evidence: MANUAL, self-contained characteristic-zero polynomial calculation.
Lifecycle: PRODUCER-CHECKED / PROVISIONAL pending different-model FIRST.
Claim: TANGENT-GRAPH-LINEAR-1. No external novelty claim; JC2 unresolved.

## Statement

Work over a field k of characteristic zero, with independent x,y. Let
gamma be a nonzero polynomial in k[x,y], set u=1+xy, w=gamma*u, and take
p,q in k[w] such that

    d=deg(p)>=2,           q'(w)=w*p'(w)/2.

Suppose ALL THREE following rational expressions are polynomials on the
WHOLE source plane:

    C=x*gamma,
    D=(p(w)+2*gamma)/(x*gamma),
    E=(q(w)+gamma*w)/(x^2*gamma^2).

No bound is placed on gamma, p or q. Put n=deg_y(gamma)>=0, write h(x)
for its nonzero y^n coefficient, and define

    a=x*h,       a'=h+x*h',
    M=(d-1)*n+d,        alpha=[w^d]p,
    beta=[w^(d+1)]q=d*alpha/(2*(d+1)).

For J(f,g)=f_x*g_y-f_y*g_x, the exact partial-y degrees and coefficients are

    deg_y J(C,D)=d*(n+1)-1,
    lc_y  J(C,D)=d*alpha*a^(d-1)*a';

    deg_y J(C,E)=d*(n+1),
    lc_y  J(C,E)=(d+1)*beta*a^(d-1)*a';

    deg_y J(D,E)=2*M,
    lc_y  J(D,E)=(d-1)*alpha*beta*a^(2*d-3)*a'.       (1)

These degrees are positive and pairwise distinct. Consequently every
affine-linear target map k^3->k^2 of rank two, applied to (C,D,E), has
nonconstant Jacobian; rank less than two gives zero Jacobian.

The conclusion also survives any polynomial postcomposition k^2->k^2
of the projected pair and any polynomial automorphism of the source
parameter plane. It excludes counterexamples constructed in this scope,
not arbitrary plane maps or arbitrary three-output polynomial maps.

## Proof of the exact degrees

All degree calculations may be made in k(x)[y]. Whole-plane polynomiality
is explicitly assumed and is used for the final constant/unit assertions.
We never replace the source by D(x*gamma).

The polynomial a=x*h is nonzero and has nonzero derivative. Indeed
h=sum h_i*x^i gives a'=sum(i+1)*h_i*x^i, not zero in characteristic zero.
This includes n=0 and nonconstant h; no genericity assumption is used.

The leading y-term of w is a*y^(n+1). In the numerator of D, p(w)
has degree d*(n+1), strictly above deg_y(2*gamma)=n. Dividing by
x*gamma therefore gives the exact leading term

    D=alpha*a^(d-1)*y^M + lower y-terms.           (2)

The derivative identity implies deg(q)=d+1 and the displayed nonzero
beta. Its possible additive constant is unrestricted. The leading degree
of q(w) is (d+1)*(n+1), strictly above deg_y(gamma*w)=2*n+1:
their difference is (d-1)*n+d>0. Consequently

    E=beta*a^(d-1)*y^(M+1) + lower y-terms.        (3)

The leading term of C is a*y^n. If f and g have leading y-terms
A(x)y^r and B(x)y^s, the coefficient of y^(r+s-1) in J(f,g) is

    s*A'*B-r*A*B'.                               (4)

All lower y-terms contribute lower powers. Formula (4) also holds when
r=0<s: the zero r term simply disappears; it does not require a
nonzero y-derivative of f.

Apply (4) to C,D. Its coefficient is

    alpha*a^(d-1)*a' * (M-n*(d-1))
      =d*alpha*a^(d-1)*a',

nonzero, at degree n+M-1=d*(n+1)-1. For C,E the same calculation gives
coefficient (d+1)*beta*a^(d-1)*a' at degree n+M=d*(n+1).
For D,E the two leading coefficient functions are proportional, but
their y-exponents differ by ONE. The coefficient in (4) is therefore

    alpha*beta*(d-1)*a^(2*d-3)*a' * ((M+1)-M),

nonzero, at degree M+(M+1)-1=2*M. This proves all of (1).

The first degree is at least one. The second exceeds it by one, and

    2*M-d*(n+1)=(d-2)*n+d>0.                     (5)

There is no equal-degree cancellation case, even at d=2 or n=0.

## All constant linear projections and polynomial postcompositions

Let L be the constant 2-by-3 matrix of an affine-linear projection.
Cauchy--Binet expresses the projected Jacobian as

    det(L_CD)*J(C,D)+det(L_CE)*J(C,E)
      +det(L_DE)*J(D,E).                         (6)

If rank(L)=2, at least one coefficient is nonzero. The largest y-degree
whose coefficient is nonzero in (6) cannot cancel, by (1) and (5).
It is positive. If rank(L)<2 all coefficients vanish.

For any polynomial target postcomposition H of the projected pair T,

    J(H o T)=J(H)(T)*J(T).

Both factors are polynomials in k[x,y]. Their product cannot be a
nonzero constant when J(T) is nonconstant or zero. This step does NOT
exclude an arbitrary map k^3->k^2 depending nonlinearly on all three
outputs, because its Cauchy--Binet coefficients need not be constants
or factor through one fixed linear projection.

For a polynomial source automorphism psi, J(psi) is a nonzero constant
by the inverse chain rule, and psi^* reflects constant polynomials.
Thus J(T o psi)=J(T)(psi)*J(psi) retains the same obstruction. This is
only a reparametrization of the same entire source graph.

## Attachment to the literal tangent construction

The existing tangent presentation has

    gamma=gamma0+b1*x*y+b2*x^2*z,
    gamma0!=0, b2!=0, w=gamma*(1+xy),

and the same C,D,E, required polynomial on the whole three-dimensional
source. Restricting to ANY polynomial graph z=Z(x,y) gives nonzero gamma,
because gamma(0,y)=gamma0. It also preserves whole-plane polynomiality.
Thus (1)--(6) apply to every such graph and every admissible seed p,q.

The earlier first-pair report already derives d>=2 from literal whole-
triple polynomiality and q'=wp'/2. For clarity the current theorem takes
d>=2 as an explicit hypothesis; it does not silently extend to arbitrary
degree-one rational presentations. No assertion about the ambient
Jacobian determinant is needed in this proof.

## Manual controls and excluded stronger statements

1. n=0 is nonvacuous in the larger plane statement. Take gamma=1,
   p(w)=-2*w^2+2*w-2 and q(w)=-(2/3)*w^3+(1/2)*w^2-5/6.
   Then q'=wp'/2 and the whole polynomials are

       C=x, D=-2*y-2*x*y^2, E=-(3/2)*y^2-(2/3)*x*y^3.

   The minors are -2-4xy, -3y-2xy^2, and (14/3)y^3+(4/3)xy^4.
   Their y-degrees are 1,2,4; the leaders -4x,-2x,(4/3)x agree with (1).
   This is a plane control, not asserted to be a whole ambient triple.

2. The old fixed core at z=0 corresponds to gamma=2-3xy,
   p(w)=-3w^2+4w, q(w)=-w^3+w^2. It gives

       C=2x-3x^2y,
       D=y+12xy^2+9x^2y^3,
       E=4y^2+7xy^3+3x^2y^4.

   With n=1,d=2,a=-3x^2, formula (1) gives degrees 3,4,6 and
   leaders -108x^3,-54x^3,54x^3. These follow directly by differentiating
   the displayed leading terms, without a program or a finite-degree inference.

3. Dropping d>=2 really changes the conclusion. With gamma=1,
   p=-2w and q=-w^2/2-1/2, the whole triple is
   (x,-2y,-y^2/2); the first pair is Keller. The third leading coefficient
   in (1) would have factor d-1=0, so the proof cannot be extrapolated.

4. In the fixed core, the alternative source plane x=0 has outputs
   (z+4y^2,y,0), and two outputs form a plane automorphism. Thus no claim
   about other graph orientations or arbitrary embedded planes follows.

No bound on polynomial degree or support is introduced. Arbitrary
nonlinear three-output maps, rational changes with poles, other source
orientations, and general affine-plane descents remain outside scope.

## History, evidence and stopping decision

This combines the mechanism of the September6 fixed-core/all-graph linear
theorem with the all-seed presentation of September15's first-pair result.
The new scope permits E and all constant linear outputs for EVERY seed
degree; it is not a new mechanism for proving arbitrary JC2.
The September12 one-sided/all-output theorem remains a distinct stronger
output scope on a restricted graph family for a fixed core.

Whole producer reports read; bounded related Markdown searches found no
exact all-seed three-minor theorem. This is not an exhaustive priority check.
Initial/post-read integrity pins are recorded before publication:

- tangent-graph-first-pair-swarmHQ-root-20260915T180230Z.md:
  4a2b0b3b92ca94b54c8807c39fa1afed0fd6bf60e3b866fdb4fa588a0ab2de3d
- alpoge-polynomial-graph-obstruction-astra-20260906.md:
  1ab4e6791e6a38fd9a8313161a546554a57efcf5207bc32d42dfa4b492dd8e21
- equivariant-graph-nonlinear-obstruction-root-20260912.md:
  8ae6ee53450d7a7ef4e688cf768903ca9900f8e4f176088076c3c8bf9cdde828

All inputs above are in xmodel/. Shared COORDINATION SHA256
9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e;
FALLACY-v2 SHA256
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

No CAS, scientific code, sampled search, source download, worker or paid
launcher was used. Documentary hashing, collision checking and transactional
publication do not verify the mathematics. One different-model hostile
review is required before promotion. No dependent work or automatic
nonlinear-output, graph-orientation, degree or parameter successor is selected.

## OPENS RAISED

None. General JC2 remains unresolved.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9145`.
- Body SHA-256:
  `2ffe27b9706c2a2a8067666c5f03f0c533b156183a8dcdd34e9a89f8fce8c000`.
- Frozen basis: `670ac5214197aea555a2aa590e01ce5974a089c4`.
