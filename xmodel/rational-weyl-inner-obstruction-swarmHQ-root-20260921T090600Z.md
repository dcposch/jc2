# Rational-inner dressing of one-coordinate Weyl pairs

Producer: swarmHQ ROOT (Codex coordinator, campaign Astra seat; hosted
model identity not independently attested).
Co-check: native Astra seat, same-model, completed September21,2026
08:43:12 UTC; not different-model hostile review.
Date: September21,2026 UTC.
Basis: 12275b5dac1133b91b693d056d544b98acbdba37.
Evidence: MANUAL, with the standard PBW/Ore inputs specified below.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED. Novelty UNKNOWN.

## Statement and scope

Let

    W = C<x,d | dx-xd=1>,       D = Frac(W).

For any nonconstant rational function R in C(x), put

    P = R(x),                 Q = (1/R'(x))*d.

The coefficient in Q is ON THE LEFT; R' means ordinary differentiation.
These elements satisfy [Q,P]=QP-PQ=1.

**Claim 1.** If T is any nonzero element of D and BOTH TPT^-1 and
TQT^-1 lie in W, then R=ax+b for constants a!=0,b in C. No bound on
the order or presentation size of the rational Ore element T is assumed.

**Claim 2.** The same necessary conclusion holds if the COMMON transformation
applied to P and Q is any finite composition of inner automorphisms of D
and actual polynomial Weyl automorphisms (elements of Aut_C(W), extended
to D). In particular it holds for beta Ad_T alpha with alpha,beta in Aut_C(W).
The transformations are applied in the ambient division ring, to both entries.

These claims exclude this construction for every R that is not an affine
linear polynomial. They do not assert that affine linearity is sufficient
for every T. Nor do they exclude arbitrary rational Weyl pairs, arbitrary
non-inner automorphisms or embeddings of D, different target subalgebras,
formal transformations, or higher Weyl algebras. No JC2/DC1 resolution follows.

## Dependencies and prior work

Standard algebraic inputs: the PBW normal form for the first Weyl algebra,
its Ore division ring, and the coefficient localization

    S = C(x)[d; partial_x],    d*f = f*d+f'.

S has the same division ring D. We use its Ore common-right-multiple
property. Polynomial-coefficient differential operators embed in S; the
order calculations below prove the required extension of order and leading
coefficient to D, rather than assuming a filtered inverse is polynomial.
Characteristic-zero simplicity of W is used only for the embedding terminology
in the nonbirational control; it is not used to prove Claims 1 or 2.
No source theorem about bispectrality, division-ring automorphism classification,
Jacobian bounds, positive characteristic, or birational Weyl invertibility
is imported into their proofs.

The earlier [birational Weyl dressing filter](birational-weyl-dressing-swarmHQ-root-20260915T082700Z.md)
assumes that the induced division-ring map is an AUTOMORPHISM. Its scope
explicitly leaves nonbirational embeddings outside. ROOT read that report
whole for comparison; the present proof does not depend on its statement or
imports. Claim 3 below exhibits an actual nonbirational donor in the present
family. Frozen public evidence and HQ history were checked before the initial
derivation. Neither those searches nor the elementary proof establish novelty.

## Proof of the order invariant

For nonzero A=sum_(j=0)^m a_j(x)d^j in S with a_m!=0, define
ord(A)=m and lc(A)=a_m. The relation d*f=f*d+f' shows

    ord(AB)=ord(A)+ord(B),    lc(AB)=lc(A)*lc(B).

Every term differentiating a coefficient has strictly lower differential
order. The leading coefficients multiply in the COMMUTATIVE field C(x).

Write a nonzero element of D as a right fraction a*b^-1 with a,b in S
nonzero, and set

    ord(a*b^-1)=ord(a)-ord(b),    lc(a*b^-1)=lc(a)/lc(b).

These definitions do not depend on the fraction. If a*b^-1=c*e^-1,
choose a common right multiple b*u=e*v. Rewriting the fractions with this
denominator gives a*u=c*v. The two product identities in S imply equality
of both order differences and leading-coefficient ratios.

They remain multiplicative in D. For a*b^-1 and c*e^-1, choose nonzero
u,v with b*u=c*v. Then b^-1*c=u*v^-1 and

    (a*b^-1)(c*e^-1)=(a*u)*(e*v)^-1.

The identities for b*u=c*v give precisely the sum of orders and product
of leading-coefficient ratios. In particular ord(T^-1)=-ord(T) and
lc(T^-1)=lc(T)^-1. Consequently, for every nonzero A,T in D,

    ord(TAT^-1)=ord(A),       lc(TAT^-1)=lc(A).

The second equality uses commutativity of C(x), not commutativity of D.

## Proofs of the claims

**Claim 1.** P has order0 and leading coefficient R. Its conjugate has the
same data. An element of W of differential order0 is multiplication by a
polynomial in x. Thus polynomial landing of P forces R in C[x], and in
fact TPT^-1=R(x). Q has order1 and leading coefficient 1/R'. Polynomial
landing of Q therefore forces 1/R' in C[x]. Since R' is itself a nonzero
polynomial, R' and its reciprocal are units of C[x]. Hence R'=a!=0 is
constant, and R=ax+b. This proves necessity only.

**Claim 2.** A polynomial Weyl automorphism extends to D by Ore localization.
If beta Ad_T alpha sends both entries into W, apply the W-preserving map
alpha^-1 beta^-1 to their images. The resulting pair is

    Ad_(alpha^-1(T))(P,Q),

so Claim 1 applies. A finite common word reduces to this form because

    alpha Ad_T alpha^-1 = Ad_(alpha(T)),

and a product of inner automorphisms is inner. No assertion that ALL
automorphisms of D have this form is needed or made.

**Claim 3: the family is not confined to birational donors.** Take R=x^2,
so P=x^2 and Q=(1/(2x))*d. Directly [Q,P]=1. The involution sigma of D
given by sigma(x)=-x and sigma(d)=-d fixes both P and Q. It fixes pointwise
the division subring they generate, but does not fix x. That subring is
therefore proper. The assignment of the standard Weyl generators to P,Q
is injective by characteristic-zero simplicity of W and extends to an
injective division-ring map with that proper image. No division-ring index
is asserted. Thus the old rational-inverse hypothesis is genuinely absent.

## Replay and controls

Desk-only; no CAS, chosen-prime check, finite-degree experiment or numerical
evidence. Recompute the Ore common-multiple identities above in the stated
generator order. Native same-model co-check confirmed the exact statements,
order extension, automorphism composition and following controls; this is
not different-model FIRST or a computational verification claim.

- R=x,T=1: both images lie in W, so affine R is not itself excluded.
- R=x,T=x: x*d*x^-1=d-x^-1 is outside W. The necessary R-condition does
  not guarantee polynomial landing for every T.
- R=x^2: the pole in lc(Q)=1/(2x) survives EVERY inner conjugation,
  regardless of lower-order cancellations. The sign involution proves the
  separate nonbirational assertion without an assumed index computation.

Original comparison-report SHA256:
04177c0617cb19c60ee9c3df564ffe4329848e3e0488fd6318ef34190f47077c.
FALLACY-v2.md SHA256:
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
Both were checked before and after the internal derivation/co-check.
Artifact sealing and hashing certify custody, not these algebraic claims.

## Limitations and next test

The next gate is a different-model hostile audit of these exact claims
before public promotion or load-bearing use. It may reject or narrow them;
it must not silently replace an inner transformation by an arbitrary one.
No automatic donor family, formal-pseudodifferential extension, degree
search, source retrieval or broader Weyl classification is proposed.

## OPENS RAISED

None. The general conjectures are not reissued as bounded tasks.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7682`.
- Body SHA-256:
  `d6e73079b60daf02449d818ff0713f8ec090da7c75f5883085329c350e950f85`.
- Frozen basis: `12275b5dac1133b91b693d056d544b98acbdba37`.
