# Transverse-line theorem: uniform full-C rank191, with precise limits

2026-09-06. Producer: Astra, /root/nonemptiness_certificate.
Evidence: desk proof plus tiny literal/exact controls; PRODUCER-CHECKED.
Different-model review is required before promotion. No CAS solve, fleet
operation, heavy computation, or performance measurement was performed.

Root's uniform full-C rank191 argument survives. It applies at EVERY
characteristic-zero base point of the frozen source, and also on the
unrestricted h-lift base. It concerns the map including the constant
Jacobian coefficient, not automatically the positive-only map.

At a base admitting an actual full Keller pair, the positive-only (C,a)
block is also injective modulo the additive constant. Off that locus this
stronger statement is not claimed.

A separate desk lemma below gives190 constant positive-row pivots after a
W-adapted rational source-basis change. That lemma is not yet instantiated
as a source matrix or benchmarked; it does not give a chosen constant191minor.

## Literal source facts and field

The frozen source is
box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json,
SHA256778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea.
Its192-dimensional rational C-space V_C, linear injection and identity slots
are certified in the already sealed filtered-pivot packet. Source residuals
are empty. Base variables and C variables are disjoint.

Physical coordinates are X=x,W=y-x. A normalized row (r,z,e) with normalizer
N contributes e X^(N-r-z) W^z. The literal W=0 rows give

    h3(X,0)=Hc_11_0,
    C2(X,0)=C2c_22_0,
    C3(X,0)=X+C3c_33_0,
    D(X,0)=B2c_64_0 X+B2c_65_0,
    C(X,0)=A3c_97_0 X+A3c_98_0.

Hence, writing h=h3^3+C2*h3+C3 and a base scalar c,

    h(X,0)=X+c,
    G=h^2-bh/3+D,
    G(X,0)=X^2+(2c-b/3+B2c_64_0)X
                 +(c^2-bc/3+B2c_65_0).

The restriction is monic quadratic at EVERY base point. Meanwhile
deg G=66 and G_top=H^6 for H=(X+W)^3 W^8. Every element of V_C has total
degree<=35 and W-degree<=32; its possible degree33 monomials have W exponents
24 through32, never33.

These are valid over any characteristic-zero field k after any choice of
the base coefficients. All degree comparisons below are actual polynomial
degrees. No generic nonvanishing hypothesis or parameter localization is used.

## Primary theorem interface

Arzhantsev–Petravchuk, “Closed and irreducible polynomials in several
variables,” arXiv:math/0608157v2, p.5, Lemmas4–5, provide exactly the needed
statements. In characteristic zero, vanishing two-variable Jacobian of two
nonconstant polynomials implies algebraic dependence; algebraically dependent
nonconstant polynomials over a field belong to one polynomial algebra k[R],
with R closed. The latter statement is over the given field, not merely its
algebraic closure. [Primary PDF, p.5](https://arxiv.org/pdf/math/0608157)

Since G is nonconstant in characteristic zero, its gradient is not identically
zero; the Jacobian matrix rank in Lemma4 is therefore1, not the rank-zero
exception. Constants are handled separately.

## Uniform kernel theorem for the FULL coefficient map

Let P be a nonconstant element of V_C and suppose J(P,G)=0. The cited lemmas
give polynomials R in k[X,W] and phi,psi in k[T] with

    G=phi(R), P=psi(R).

Restrict to W=0. Since G(X,0) has degree2, R(X,0) is nonconstant and

    deg(phi) * deg_X(R(X,0)) =2.

Thus deg(phi)=1 or2. Polynomial composition also gives
66=deg(phi)deg(R).

If deg(phi)=1, then deg(R)=66, hence deg(P)>=66, contradicting deg(P)<=35.
If deg(phi)=2, then deg(R)=33 and deg(psi)=1.

Write the leading coefficient of phi as alpha. The top identity
alpha R_top^2=H^6 implies that R_top has nonzero W^33 coefficient. One can
see this directly by setting X=0: the right side is W^66, so the W^33
coefficient of R_top cannot vanish. Since psi is linear, P also has a
nonzero W^33 coefficient, contradicting the actual C support.

Therefore

    ker(V_C -> k[X,W], P |-> J(P,G)) = k*1,

and the FULL coefficient matrix has rank191 at every base point. This is not
only a generic-rank or numerical-sample statement.

For the h-lift, the exact metadata shows that its sole W-zero auxiliary is
Hfact_0_0, while all nonconstant h auxiliary positions have physical degree
at most31. The coefficient of X at W=0 stays1, and h_top stays H^3.
Thus h(X,0)=X+Hfact_0_0 and the same theorem holds even BEFORE imposing the
160 monic h-source definitions. It consequently also holds on their quotient.

## Positive rows are different; conditional (C,a) uniqueness

Dropping the constant output coefficient changes the kernel condition to

    J(P,G)=kappa in k,

not J(P,G)=0. The uniform theorem above alone does not show that kappa=0.
For example P=X,G=X^2+W has J(P,G)=1: it lies in the positive-row kernel,
but not the full kernel. This example illustrates the map distinction, not
a counterexample in the degree66 family.

Now assume the fixed h,D,b base admits an ACTUAL pair F,G with
J(F,G)=j in k*, deg(F)=99 and deg(G)=66. Let

    P=Delta C+(Delta a/2)h,  Delta C in V_C,

and suppose its positive Jacobian coefficients vanish, so J(P,G)=kappa.
Set Q=P-(kappa/j)F. Then J(Q,G)=0.

At a Keller point the full centralizer of G is k[G]. Indeed, a decomposition
G=phi(R) would imply j=phi'(R)J(F,R); a nonzero constant product in
k[X,W] forces phi'(R) to be a unit, hence phi has degree1 in characteristic
zero. Combining this with the same common-polynomial lemma for any
nonconstant commuting Q gives Q in k[G].

If kappa is nonzero, deg(P)<=35 implies deg(Q)=99. But a nonconstant
polynomial in G has degree a positive multiple of66, never99.
Therefore kappa=0. Then P is in k[G] and has degree<66, so P is constant.
The W^33 coefficient of P is Delta a/2, because h has that coefficient1
and every Delta C has W-degree<=32. Thus Delta a=0 and Delta C is constant.

Consequently, at a base admitting a full Keller pair, the positive-only
(C,a) linear block has kernel exactly the additive constant. After removing
that constant, its192 columns are independent. This is conditional on the
Keller point; it does not prove existence of one or license dropping the
inverse-J equation.

The Keller hypothesis cannot be omitted for this enlarged block. At the
actual source specialization D=0,b=0 one has G=h^2, and the nonconstant
direction P=h (Delta a=2, Delta C=0) has zero Jacobian with G. These points
need not be Keller points. They refute a uniform full-rank (C,a) claim over
the entire unrestricted source base.

## What uniform rank licenses algebraically, not computationally

Delete the constant C column and call the full matrix M, with191 columns.
Its entries lie in the polynomial base ring A over Q (247 source variables,
or407 variables on the unrestricted h-lift base). Every geometric fiber has
rank191. Therefore the ideal of191-by-191 minors is the unit ideal of A:
otherwise a maximal ideal would yield an algebraic-closure point where all
minors vanish. This is the weak Nullstellensatz, with faithful descent to Q.

A polynomial left inverse exists. If sum q_S det(M_S)=1, and E_S selects the
rows of M_S, then

    L=sum q_S adj(M_S) E_S
    satisfies L M=I_191.

This also gives split injectivity after arbitrary base change, including
nonreduced Q-algebras. It is stronger than a statement only about reduced
points, but it is not an explicit small certificate.

It does NOT automatically give one constant selected191minor, sparse
cofactors, a cheap left inverse, or manageable residual substitution.
The one-column matrix (t,1-t)^t has rank1 everywhere and maximal-minor ideal
(1), but neither selected minor is constant. Finding the required Bezout
combination can relocate a difficult ideal-membership computation.
No such combination or191minor has been computed here.

## Additional desk lemma:190 constant POSITIVE pivots

This does not require the total-degree66/top-support argument. Let
V_0={P in V_C : P(X,0)=0}. The literal restriction map has image span{1,X},
so dim_Q(V_0)=190.

Choose a rational basis of V_0 adapted to increasing minimum W-order r>=1.
Within each fixed r, echelonize the leading W-coefficient polynomials in X,
ordering their distinct X degrees i decreasing and normalizing their leading
coefficients to1. This is a finite constant Q basis change on the SOURCE
space, respecting all mixed homogeneous components.

For a basis polynomial

    P=W^r p_r(X)+higher W-orders, deg_X p_r=i,

the lowest W coefficient of its Jacobian is exactly

    [W^(r-1)]J(P,G)=-r p_r(X) G_X(X,0)
                         =-r p_r(X)(2X+t).

Its X^(i+1) coefficient is the constant -2r. A later basis column with
larger minimum W-order cannot reach this output W-order. Within the same
W-order, a later column of smaller X degree cannot reach X^(i+1).
Thus the selected matrix is lower triangular with constant nonzero diagonal
-2r. All selected rows are POSITIVE degree, since their physical positions
are (i+1,r-1), of total degree i+r>=1.

This proves existence of190 constant positive-row pivots in that adapted
basis, for every monic-quadratic transverse restriction. It is a constructive
basis-selection lemma, but the actual190-column source transformation and
minor have NOT been emitted or benchmarked in this desk task. It is not a
claim about one chosen minor in the original source-coordinate basis.

After such elimination, one nonconstant C coordinate remains; the full
rank191 theorem implies that its full residual coefficient column generates
the unit ideal. It still does not supply a constant final entry or cheap
Bezout expression. The prior189 high-degree pivots remain valid, and the
failed24-prefix expansion remains a failed measured construction.

## Exact negative and literal controls

box/linear-c-transverse-rank-20260906/line_support_check.py uses only JSON,
small rational arithmetic and tiny polynomial dictionaries, with no CAS
library. It verifies the literal transverse rows, degree33 support and h-lift
auxiliary restrictions. It also checks:

- Drop the transverse-line condition: G=H^6 and P=H have J(P,G)=0.
  P is in the ACTUAL C source space, realized by coefficients1,3,3,1 at
  A3c_87_8,A3c_87_9,A3c_87_10,A3c_87_11. But G(X,0)=0.
- Drop the C-support condition: R=H^3+X, G=R^2 and P=R have zero Jacobian,
  G(X,0)=X^2 and the correct degree66 leading form, but P has nonzero W^33.
- Positive-only is not full: J(X,X^2+W)=1.

These are controls of the hypotheses, not contradictions to the theorem
on the actual fully constrained source. All checks passed.

Code SHA256:
a9e0e4656dba723b38403b2c61c13f5e4813257d70f2ba03f90b9116e0045f9e.
Result JSON SHA256:
4f21b2ef4a28af4c264b935c9c9100247b6906fb17c775a390ab25f03265a20f.
Replay:

    python3 box/linear-c-transverse-rank-20260906/line_support_check.py

No collected blind report was needed or read; no live Opus/Sol report was
read. No shared ledger was edited, and no worker was touched. All owned
writers are finished. The result is a theorem-interface improvement, not a
performance result, properness certificate, counterexample or resolution of JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11131`.
- Body SHA-256:
  `4d38bb2510b1e5cf6c0414ca3290fdbd7bca7adf18e871ebe990fb632e9d9a05`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
