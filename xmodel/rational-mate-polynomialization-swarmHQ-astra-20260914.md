# Rational Liouville mates do not polynomialize by dominant source substitution

Producer: swarmHQ Astra, independent bounded check of ROOT's supplied claim.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Not a different-model FIRST. Basis: 6630ded0152bf1880f43ead2e0ba757820c0e327.

## Statement and verdict

Work over C. Fix any nonzero Q(t) in C[t] and any polynomial I(t) with
I'=Q, including an arbitrary integration constant. In C(x,y), set

    t=x^3 y,   p=x^2 Q(t),   q=I(t)/(2p^2).

Then J_(x,y)(p,q)=1. Nevertheless, there is no dominant rational map
psi:A2_(u,v) --> A2_(x,y) for which both compositions f=p o psi and
g=q o psi are polynomials and J_(u,v)(f,g)=1.

Verdict: the supplied obstruction survives the manual audit. The argument
actually excludes any nonzero constant composite Jacobian. Dominance need
not be birationality. This stops this complete rational-pair construction,
not arbitrary rational Keller maps or arbitrary source transformations.
It neither proves JC2 nor produces a polynomial counterexample.

## Rational Jacobian

The coordinates (x,t) generate C(x,y), with inverse y=t/x^3. Calculations
here are in rational differential forms, not at the divisor x=0:

    dx wedge dy = x^(-3) dx wedge dt,
    dp = 2x Q(t) dx + x^2 Q'(t) dt,
    dq = (1/2)p^(-2) Q(t) dt - I(t)p^(-3) dp.

Consequently

    dp wedge dq = x Q(t)^2 p^(-2) dx wedge dt
                = x^(-3) dx wedge dt = dx wedge dy.

All divisions occur in the function field; Q and p are nonzero there.
This proves the literal rational Jacobian identity, for every choice of
the additive constant in I.

## Polynomialization obstruction

Suppose the indicated psi and polynomial Keller pair exist. Write
B=C[u,v], K=Frac(B). Dominance supplies an injective C-field homomorphism
psi*:C(x,y) -> K. Put X=psi*(x), T=psi*(t). Then

    f=X^2 Q(T),   g=I(T)/(2f^2),   I(T)=2f^2 g.                 (1)

Here X,T initially belong only to K. No evaluation of these rational
functions on their pole sets is used. The injectivity makes X and T
nonconstant and algebraically independent. Also f,g are nonconstant,
nonzero and algebraically independent, as follows already from their
nonzero constant Jacobian.

Since deg(I)>=1, its leading coefficient is a nonzero complex constant.
Dividing I(Z)-2f^2 g by that coefficient gives a monic polynomial in B[Z]
annihilating T. The ring B is integrally closed in K, so T belongs to B.
This is the crucial justification for the pointwise step below.

Let a be any root of Q. A nonconstant polynomial T on C^2 attains a:
restrict T to a line on which it is nonconstant and use algebraic closure
of C. Choose z with T(z)=a. Differentiating the now-polynomial identity
(1) gives, in Omega^1_(B/C),

    Q(T)dT = 4fg df + 2f^2 dg.

The two covectors df(z),dg(z) form a basis because their Jacobian is a
nonzero constant. At z the left side vanishes, so the coefficient
2f(z)^2 of dg(z) is zero. Thus f(z)=0, and (1) implies I(a)=0.
Every root of I'=Q is therefore also a root of I. No value of X at z
was assumed to exist.

This forces I to have exactly one distinct root. Indeed write
I=c product_(i=1)^r (t-a_i)^(m_i), with distinct a_i and m=sum m_i.
At a_i, the derivative I' has multiplicity exactly m_i-1 in
characteristic zero. Those multiplicities sum to m-r. All roots of I'
have just been accounted for, so m-r=deg(I')=m-1. Hence r=1 and

    I=c(t-a)^m,   c in C*,   m>=1,
    f^2 g=(c/2)(T-a)^m.                                    (2)

The assertion includes the linear case: I' is then constant and has no
roots, and the same count gives r=1.

A polynomial Keller pair in B has gcd(f,g)=1: if an irreducible h divides
both, the product rule makes h divide J(f,g), impossible. Likewise g is
squarefree: h^2 dividing g makes both derivatives of g divisible by h,
again contradicting the constant nonzero Jacobian. Since g is nonconstant,
choose an irreducible h dividing g. Its valuation in f^2 g is exactly 1,
by coprimality and squarefreeness. Equation (2) gives

    1=m*ord_h(T-a).

The right side is a nonnegative integer multiple of m, so m=1. Thus Q=c
is a nonzero constant. Now f=cX^2 makes X integral over B, by the monic
equation Z^2-f/c=0. Since X lies in K, normality gives X in B. It remains
nonconstant by the injectivity of psi*. The polynomial product rule yields

    J(f,g)=2c X J(X,g),

which cannot be a nonzero constant because X is a nonunit of B. This is
the contradiction. No finiteness, regularity or invertibility of psi as
a whole-plane morphism was assumed at any step.

## Controls, dependencies and scope

The simplest member Q=1, I=t has p=x^2 and q=y/(2x), with rational
Jacobian 1. It illustrates the last obstruction directly: any successful
polynomialization would make the pulled-back x a nonconstant polynomial
whose factor divides the composite Jacobian.

A positive control against the false statement that every rational
formula is non-polynomializable is p=x, t=xy, q=t/p=y. The identity
source map makes this a polynomial Keller pair. In this control the
identity is t=pq, not the squared relation (1); there is no concluding
nonconstant square factor. The proof must not be advertised without its
specific p=x^2 Q(t), q=I(t)/(2p^2), t=x^3 y hypotheses.

The integration constant cannot evade the obstruction: the derivative
step forces every critical value of I to be zero for that very choice
of constant. If such a choice exists, the multiplicity argument still
forces I to be linear and reaches the square-factor contradiction.
For example I=t^2 has its only critical value zero, but (2) with m=2
is still incompatible with squarefree g and coprime f,g.

The prior exact-curve ROOT report was read for provenance only:
xmodel/exact-plane-curve-genus-swarmHQ-root-20260914.md. No conclusion
about genus or exactness of its fibers is used in this proof. Applicable
policy and FALLACY-v2.md were read, and APPROACHES Section 8's stopped
Poisson/rational-gauge paragraph was checked. That older test asked for
a rational invariant of the same Keller map and reached stable-image
rigidity; this test instead asks whether a specified complete rational
pair admits any dominant rational source polynomialization. ROOT's new
draft was not inspected. No exhaustive historical or literature novelty
claim is made.

This is a manual check of ROOT's proposed argument, not independent
discovery of the family and not different-model review. The only invoked
algebra is explicit field pullback, normality and unique factorization
of C[u,v], the product rule, and elementary one-variable root counting.
There was no CAS, scientific Python, degree search, test suite, paid lane,
cloud computation, nested-repository inspection or shared-ledger edit.
Administrative finalization and hashing are not mathematical computation.
No successor family or degree search is selected.

## COLLISIONS

EMPTY (manual). No new machine-tagged OPEN is raised. The broad scanner
was not run; the scoped history check is not a complete corpus audit.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7033`.
- Body SHA-256:
  `ea018a531d4caa1e3a0406794736c3e6cc55eb23a60315a62bf646c280e69da9`.
- Frozen basis: `6630ded0152bf1880f43ead2e0ba757820c0e327`.
