# Fractional-linear rational Keller donors reduce to product covers

Producer: swarmHQ ROOT (gpt-6-astra), September 18, 2026.
Evidence: MANUAL; elementary rational differential calculation and the
accepted product-donor exclusion at its named classical import tier.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending different-model FIRST.
Claim: FRACTIONAL-LINEAR-DONOR-1.
Frozen public basis: 26dede75181328a2ede34c9cdd84754c92d0bf09.

## 1. Statement

Work over C. Suppose P,Q in C(x,y) satisfy

    J_(x,y)(P,Q)=1,       [C(x,y):C(P,Q)]=n,

and Q is a fractional-linear function of y over C(x), of degree exactly
one. Thus Q=(a(x)y+b(x))/(c(x)y+d(x)), with ad-bc nonzero in C(x).
The Jacobian identity implies dominance and finiteness of this function
field extension. There are a nonconstant R in C(x), a rational source
translation sigma(x,y)=(x,y-B0(x)), and a birational rational target change
tau with Jacobian one, such that

    tau composed (P,Q) = (R(x), (y-B0(x))/R'(x)).                 (1)

Both sigma and tau have rational inverses and Jacobian one. In particular,
n is the degree of the rational map R:P1->P1, with no degree bound.

If n>1, then for EVERY birational rational target change alpha with nonzero
constant Jacobian and EVERY dominant finite-degree rational source map
phi:A2 --> A2, the pair alpha composed (P,Q) composed phi CANNOT be a
polynomial Keller map on the whole source A2.

The last assertion consumes the already accepted rational-product client
of SYMPLECTIC-TARGET-SMOOTH-BRANCH-1. It does not reprove its classical
imports. Degree-one donors are not excluded. No reduction of arbitrary
rational pairs to this fractional-linear hypothesis is asserted; this
does not resolve JC2. No literature novelty is claimed.

## 2. The rational differential identity

Since Q is Mobius in y, C(x,y)=C(x,Q). Write the rational inverse as
y=y(x,Q), and put p(x,Q)=P(x,y(x,Q)). With Q held fixed,

    dP wedge dQ = p_x dx wedge dQ,
    dx wedge dy = y_Q dx wedge dQ.

Therefore p_x=y_Q. All partial derivatives below are rational derivatives
in the independent variables x,Q. The constants of partial_x on
C(Q)(x) are C(Q), in characteristic zero.

Every degree-one rational function y(x,Q) has one of the forms

    y=A(x)Q+B(x), A!=0; or
    y=A(x)+B(x)/(Q-r(x)), B!=0.

The following three cases exhaust these presentations.

## 3. Affine inverse

If y=AQ+B, the identity is p_x=A. A rational primitive T(x) of A exists:
specialize Q to one complex constant outside the finitely many values
making a denominator of p(x,Q) identically zero in x. Then the specialized
rational function has derivative A. Hence

    p=T(x)+H(Q),       T'=A!=0.

The target shear (p,Q)->(p-H(Q),Q) has rational inverse and Jacobian one.
Since Q=(y-B(x))/A(x), this gives (1) with R=T and B0=B.

## 4. Constant inverse pole

Let y=A+B/(Q-c), with c in C and B!=0. Then p_x=-B/(Q-c)^2.
Specialization at a constant Q different from c gives a rational T with
T'=B. Consequently

    p=-T(x)/(Q-c)^2+H(Q).

Set p'=p-H(Q), q'=Q-c. The birational target change

    (p',q')->(-p' q'^2, 1/q')

has inverse (u,v)->(-u v^2,1/v) and Jacobian one. Its outputs are

    (T(x), (y-A(x))/B(x)) = (T(x),(y-A(x))/T'(x)).

Thus (1) holds with R=T and B0=A. The shifts and shear preceding this
change also have Jacobian one.

## 5. Moving inverse pole

Let y=A+B/(Q-r(x)), with B!=0 and r nonconstant. Put C=-B/r'; this is a
nonzero rational function since characteristic zero implies r'!=0. Then

    p_x = -B/(Q-r)^2 = C r'/(Q-r)^2,
    (C/(Q-r))_x = C'/(Q-r) + C r'/(Q-r)^2,

so that the rational function u=p-C/(Q-r) satisfies

    u_x=-C'/(Q-r).                                             (2)

Regard (2) over the coefficient field C(Q), with Q transcendental.
Every point of the generic divisor Q=r(x) is a simple finite root in an
algebraic closure of C(Q); a possible fixed pole, zero of r', or x=infinity
cannot map to the transcendental Q. At any such root a, the residue of
the right-hand differential -C'(x) dx/(Q-r(x)) is C'(a)/r'(a).
The derivative of a rational function has zero residue at every point.
It follows that C' vanishes on the generic divisor Q=r(x). This forces
C'=0 in C(x): equivalently this divisor has function field C(x), and
restriction of the rational function C'(x) to it is the same function.

Thus C=lambda in C*, B=-lambda r', and integration of (2) yields

    p=lambda/(Q-r(x))+H(Q).

After the target shear p'=p-H(Q), apply

    (p',Q)->(Q-lambda/p', -p').

This is birational with inverse (u,v)->(-v,u-lambda/v), and its Jacobian
is one. The outputs are

    (r(x), -lambda/(Q-r(x)))
        = (r(x), (y-A(x))/r'(x)).

This proves (1) with R=r and B0=A. No analytic integration, simple-critical-
point hypothesis on the fixed function r, or degree bound has been used.
Only the GENERIC roots of Q-r(x) must be simple.

## 6. Degree and all-source exclusion

Birational source and target changes preserve n. In the reduced variables
(x,Y), put U=R(x), V=Y/R'(x). Then

    C(x,Y)=C(x,V),   C(U,V)=C(R(x),V),
    [C(x,V):C(R(x),V)]=[C(x):C(R(x))]=deg R.

Let D_R=(R,Y/R'). Suppose alpha composed (P,Q) composed phi were whole-
plane polynomial Keller. From tau composed (P,Q)=D_R composed sigma,

    alpha composed (P,Q) composed phi
       = (alpha composed tau^-1) composed D_R composed (sigma composed phi).

The new target change is birational with nonzero constant Jacobian.
The new source substitution is still dominant finite-degree rational;
it need not be polynomial, birational, or have constant Jacobian.
For degR=n>1 this contradicts the accepted product-donor theorem.

Dependency: [producer](symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md)
Sections 1 and 5, [Sol FIRST](symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md),
and [binding ledger scope](../AUDIT.md#symplectic-target-smooth-branch-1--2026-09-16).
The dependency uses point-blowup surface resolution/factorization, purity,
finite-etale triviality of complex A2, Jelonek polynomial coverage and
Chau's no-A1-component theorem, at their already recorded import tiers.
The present elementary normal-form proof uses none of those imports;
the final construction exclusion does.

## 7. Controls, history and limits

- If R=x, the reduced donor is the identity. Arbitrary rational source
  substitution can itself contain the whole Keller problem. Dropping
  n>1 would falsely exclude the identity, so degree one is not covered.
- The moving-pole case includes nonconstant r of any rational degree,
  including ramified fixed fibers. For instance y=-r'/(Q-r), p=1/(Q-r)
  meets the identity and is sent to (r,(y-A)/r') with A=0. Repeated special
  roots do not invalidate the generic-residue argument.
- Fractional-linear dependence is a substantive hypothesis. No statement
  covers arbitrary higher-degree dependence on y, arbitrary constant-J
  rational maps, nonconstant-J target changes, or proper target subfields.
- Rational changes are identities of function fields, not asserted
  everywhere-defined affine automorphisms. Their poles may not be erased
  from the hypotheses when attaching the final whole-plane condition.

This records the manual three-case calculation first banked by swarmHQ
at 00:57:42 UTC September18; it is not a new second calculation. Nearest
accepted input is the September16 all-rational-R product exclusion. The
September17 internal cubic cusp countercontrol already prevents an
unsupported claim that ALL rational symplectic donors are product words.
History selection searched frozen public26dede75 and the frozen HQ dated
journal at0b6c62c; absence of an exact hit is not a novelty certificate.
No external theorem body was retrieved for this report and no scientific
code, CAS, degree enumeration or numerical computation was run.

ROOT read the accepted producer and FIRST whole and the exact AUDIT entry.
Full input SHA-256 values before author completion:

    product producer f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a
    product FIRST cadbc15edc36fd88ac973f42fcf5d8efcd18a42a00ea74adc60f7f143f7188eb
    COORDINATION 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
    FALLACY-v2 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
    APPROACHES b003c386c869f5ac1d0591510e43848314f43f981821fcc82cb9da134fd8a02c
    AUDIT a885d18f3afb4dce52f26948e821d04426390add66ee43b880866a9c1deb35a9

Next and sole test: independent different-model hostile review of the
three-case normal form and its composition with the accepted theorem.
No higher-degree family, general generation claim or automatic successor.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author COMPLETE September18 01:16:31 UTC. The six listed input hashes
were rechecked unchanged. Collision check returned the block above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8907`.
- Body SHA-256:
  `bdd268dc86739684bdfddce96c835395205175d7f224233676246b6135b8e403`.
- Frozen basis: `26dede75181328a2ede34c9cdd84754c92d0bf09`.
