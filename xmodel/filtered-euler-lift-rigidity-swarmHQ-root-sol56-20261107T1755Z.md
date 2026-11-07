# Filtered Euler rigidity for the index-three cusp filtration

Producer: swarmHQ ROOT coordinator (configured gpt-6-astra; hosted identity unverified).
Independent hostile reviewer: configured gpt-5.6-sol / ultra; hosted identity unverified.
Date: 2026-11-07 UTC.
Basis: a636e88e7cfc086340c87f66ff149e48f0120d63.
Claim: FILTERED-EULER-LIFT-RIGIDITY-1.
Evidence tier: MANUAL. Lifecycle: PROVISIONAL.
Independent verdict: CONFIRM_EXACT_FILTRATION_THEOREM. Literature novelty unassessed.

## Statement and scope

Let B=C[x,y] and w=x^2-y^5. Every element has a unique expression
f(y,w)+x g(y,w). Give its normal monomials the weights

    delta(x)=5, delta(y)=2, delta(w)=3,
    delta(x^epsilon y^a w^b)=5 epsilon+2a+3b, epsilon in {0,1},

and let delta of a nonzero polynomial be the maximum such weight.
Set delta(0)=-infinity. Suppose F^*:B -> B sends x to P and y to Q,
Jac(P,Q)=J is a nonzero constant, and for some integer e>=1,

    delta(F^*f)=e delta(f) for EVERY nonzero f in B.                 (1)

Then e=1, P=alpha x and Q=beta y, where alpha,beta are nonzero constants
and alpha^2=beta^5. Conversely these diagonal maps satisfy (1) with e=1.
If J=1, additionally alpha beta=1 and alpha^7=1.

This is an exact full-filtration hypothesis. It is stronger than merely
assigning weights to P,Q, or specifying a candidate action at infinity.
No claim that an arbitrary Keller map preserves this filtration is made.

## Dependencies and prior work

The proof below is self-contained commutative algebra and polynomial calculus.
It uses separability of finite field extensions in characteristic zero,
with the required derivation argument given explicitly below. It assumes no
integrality of B over F^*B, properness, complete vector field, extension across
an omitted boundary, or finite Rees morphism.

The campaign's earlier exact index-three lift analysis excluded a generic
cusp-unit case and one semigroup-hole case, but left all higher cusp factors
k>=2 open. The theorem and its full-lift corollary close that remaining question
for this one filtration. The key additional input is a polynomial derivation
on the entire source ring and its leading action on the entire graded image.
The earlier finite jets and ramification counts did not supply this input.
No exhaustive historical or literature novelty claim is made.

[Evidence and replay](../box/filtered-euler-lift-rigidity-swarmHQ-20261107T1755Z/README.md)
retain the exact producer proof and independent hostile review.

## Proof

### 1. The filtration and its actual Euler derivation

The associated graded ring is

    A0=C[X,Y,W]/(X^2-Y^5),  deg(X,Y,W)=(5,2,3).

Indeed reduction by the monic relation x^2=y^5+w gives the stated unique
normal basis; its highest-weight relation is X^2=Y^5 and the same normal
basis leaves no additional initial relation. This ring is a domain, since
X^2-Y^5 is irreducible. Thus delta is multiplicative, its nonnegative pieces
are finite dimensional, and A0 has transcendence degree two.

The actual polynomial Euler derivation

    E=5x partial_x+2y partial_y

preserves the filtration: E(w)=10w, and each normal monomial is an eigenvector.
The eigenvalue of w is 10, although its filtration degree is 3.
These two different weights must not be identified.

### 2. Transporting E without assuming an inverse polynomial map

The constant nonzero Jacobian gives polynomial derivations

    D_P=(Q_y partial_x-Q_x partial_y)/J,
    D_Q=(-P_y partial_x+P_x partial_y)/J.

They satisfy D_P(P)=D_Q(Q)=1 and D_P(Q)=D_Q(P)=0. Therefore

    D=5P D_P+2Q D_Q

is polynomial on all of B and D(F^*f)=F^*(Ef) for every f in B.
The exact scaling (1) induces an injective graded homomorphism
phi:A0 -> A0 multiplying degrees by e.

### 3. The transported derivation cannot have positive filtered order

For any polynomial derivation L, the normal basis and Leibniz rule show

    delta(Lf)<=delta(f)+q,
    q=max(delta(Lx)-5, delta(Ly)-2, delta(Lw)-3).

The maximum is attained on a generator unless L=0. In particular every
polynomial derivation has finite filtered order. If q>0 for D, its leading
part is a nonzero degree-q derivation Dbar of A0.
But D(F^*f)=F^*(Ef) and delta(Ef)<=delta(f), so Dbar kills phi(A0).

Let K=Frac(A0), K0=Frac(phi(A0)). Both are finitely generated fields of
transcendence degree two over C. Thus K/K0 is finitely generated algebraic,
hence finite; it is separable because the characteristic is zero.
The derivation Dbar extends by the quotient rule to K and vanishes on K0.
For a in K, differentiate its minimal polynomial m over K0:

    0=Dbar(m(a))=m'(a) Dbar(a).

Separability gives m'(a)!=0, so Dbar(a)=0. This contradicts Dbar being nonzero.
Consequently D has filtered order at most zero. This step uses an algebraic
extension of GRADED fraction fields, not finiteness of B over F^*B.

### 4. All degree-zero derivations on this actual ring

For a derivation L preserving delta, the complete possible images are

    Ly=a+b y,
    Lx=c0+c1 y+c2 w+c3 y^2+c4 x+c5 yw.

The term yw has degree 5 and cannot be omitted. Differentiating w=x^2-y^5 gives

    Lw=(2c4-5b)y^5+2c5 xyw+2c3 xy^2+2c2 xw
        -5a y^4+2c1 xy+2c0 x+2c4 w.

These are distinct normal monomials. Requiring delta(Lw)<=3 first kills the
degree-10 coefficients of y^5 and xyw, and then the terms of degrees 9,8,7,5.
It follows that a=c0=c1=c2=c3=c5=0 and 2c4=5b. Hence L=mu E.

Apply this to D. Both D_P and D_Q have divergence zero, since mixed
partials commute and J is constant. Therefore

    div(D)=5 D_P(P)+2 D_Q(Q)=7=div(E).

Thus D=E. Since D(P)=5P and D(Q)=2Q, the actual Euler weights give
E(P)=5P and E(Q)=2Q. The only monomials of those respective weights are
x and y. Thus P=alpha x,Q=beta y. The nonzero Jacobian gives alpha beta!=0.
Applying (1) to y forces e=1; applying it to w forces alpha^2=beta^5,
since otherwise alpha^2 x^2-beta^5 y^5 has filtration degree 10 instead of 3.
This proves the theorem and the stated Jacobian-one specialization.

## Corollary: exclusion of every higher full polynomial lift

Consider the actual weighted Rees ring

    S=C[X,Y,W,T]/(X^2-Y^5-WT^7), deg(X,Y,W,T)=(5,2,3,1),

with Poisson bracket

    {X,Y}=T^7, {Y,W}=-2X, {X,W}=-5Y^4, {T,-}=0.

It embeds as X=x t^5,Y=y t^2,W=w t^3,T=t in B[t].
Suppose U,V,H are homogeneous polynomial elements of S of respective weights
5e,2e,3e, e>=1, satisfying

    U^2-V^5=T^(7e) H,

and their reductions modulo T define an injective Poisson map A0 -> A0.
These assumptions describe a FULL polynomial lift, not just a finite jet.
Then e=1. In particular all higher cusp-factor cases k>=2 in this fixed
full-polynomial-lift problem are excluded.

To prove it, bracket the relation with V:

    -2U {U,V}=T^(7e) {V,H}.

The element T is prime because S/(T)=A0 is a domain, and U is not divisible
by T by injectivity of the central map. Hence T^(7e) divides {U,V}.
The quotient has weight zero, so {U,V}=c T^(7e) for a constant c.
Cancellation yields {V,H}=-2c U; reducing modulo T and using the prescribed
Poisson map gives c=1. Specializing T=1 therefore produces a polynomial
Keller pair P,Q with Jac(P,Q)=1. Injectivity of the central graded map gives
exact scaling (1) for every nonzero f. The theorem forces e=1.

Nothing here excludes a merely rational or completed-local lift, supplies
an algebraization theorem, or covers arbitrary filtrations/eigenvaluations.

## Review, replay, and limitations

Desk-only. The independent reviewer checked the whole producer argument,
the degree-zero enumeration including yw, the finite separable field step,
the divergence calculation, and the complete Rees consumer. Its verdict was
CONFIRM_EXACT_FILTRATION_THEOREM. ROOT checked the entire sealed review and
its reading/receipt record. The evidence manifest pins all published files.
No Lean or computer-algebra certificate is claimed. Standard algebraic
foundations are not newly formalized or separately literature-audited.

JC2 remains unresolved. A next meaningful mathematical step would establish
which additional actual source filtrations have this derivation rigidity,
or obtain an actual Keller-map reduction to one of them. Neither step is
included here. No degree search or repeated finite-jet test is implied.

## OPENS RAISED

None. The existing arbitrary-map realization and finite-normalization gaps
remain open; this report introduces no new OPEN identifier.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `a636e88e7cfc086340c87f66ff149e48f0120d63` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8555`.
- Body SHA-256:
  `c6f0f113efe0fad1b8281953da1b40e02c018e1f5ff371fad936a815c1c4a6b3`.
- Frozen basis: `a636e88e7cfc086340c87f66ff149e48f0120d63`.
