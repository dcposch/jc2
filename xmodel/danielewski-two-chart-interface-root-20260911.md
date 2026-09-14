# Unrestricted Danielewski two-chart endpoint and linear extension test

ROOT manual research / UNREVIEWED. No regular scalar pair, new exclusion,
novelty claim or JC2 resolution. Research first2026-09-11 13:08:56UTC;
publication opened13:22:31, original reserve13:34/HARD13:42UTC unchanged.
Frozen basis0d39df3c9fd69c939a8420c54d03228b9077777d.

The construction target need not impose the quotient's involution: an
arbitrary regular scalar-bracket pair on T={t²-1=x²Z} would already imply
a polynomial JC2 counterexample. This is a KNOWN external surface question,
explicit in Dubouloz's2009 Basel abstract. It broadens the present quotient-S
search endpoint; it does not prove that every counterexample comes from T.

## 1. Exact sufficient endpoint, with no symmetry requirement

Work over C. Set D_±={x=0,t=±1} in T. The two charts T minus D_- and
T minus D_+ cover T, since the two deleted lines are disjoint. Their explicit
isomorphisms with A2 are

    j_+(x,y)=(x,1+x²y,2y+x²y²),
    j_-(x,v)=(x,-1+x²v,-2v+x²v²).

The inverse y=(t-1)/x² agrees with Z/(t+1) where the latter is defined;
these two formulas cover the first chart. The analogous formulas
v=(t+1)/x²=Z/(t-1) cover the second. On their overlap x!=0,

    v=y+2/x².                                      (1)

The surface is smooth: all partial derivatives of t²-1-x²Z can vanish
only if t=x=0, which contradicts its equation. The form

    omega=dx wedge dt/x²

is dx wedge dy or dx wedge dv on the two charts. It is therefore globally
regular and nowhere zero. Equivalently, near x=0 it equals
dx wedge dZ/(2t), with t a unit there.

Suppose H,G in O(T) satisfy dH wedge dG=c*omega, c in C*. Both chart
restrictions are polynomial Keller maps. Neither can be an automorphism.
Indeed, if (H,G) restricted to j_+(A2) had polynomial inverse (a,b), the
regular function b(H,G) on all of T would agree with y=(t-1)/x² on a dense
open. At the generic point of D_-, however, x is a uniformizer and t-1
is a unit; this rational function has a pole of order two. This is a
contradiction. Exchange the signs for the other chart. This proves the
sufficient counterexample implication without a degree criterion or a
finite-morphism assumption. It does NOT produce H,G.

Conversely, polynomials P,Q in C[x,y] give such a regular pair on T exactly
when their substitutions P(x,v-2/x²), Q(x,v-2/x²) are polynomials in x,v
and J_(x,y)(P,Q)=c in C*. The functions glue by (1), and the Jacobian
remains c because the transition has determinant one. Thus the simultaneous
polynomiality/full scalar-Jacobian criterion is exact in both directions.

The quotient map q:T->S, (x,t,Z)->(A,U,Z)=(x²,xt,Z), uses the free
involution sigma(x,t,Z)=(-x,-t,Z). Its invariant ring is
C[x²,xt,Z] with relation U²=A+A²Z. Previous pairs on S pull back to the
sigma-invariant part of the present target. Functions such as x are regular
on T and not invariant, so imposing invariance unnecessarily restricts this
sufficient construction space. No existence of an unrestricted scalar pair,
or strict containment between nonempty solution sets, is inferred.

## 2. Full linear extension criterion and the remaining nonlinear identity

On the localization x!=0, write uniquely

    H=sum_m x^m p_m(t),          p_m in C[t],

with finite Laurent support. For every m<0 put k_m=ceil(-m/2). Then

    H belongs to O(T)
    iff (t²-1)^k_m divides p_m(t) for every m<0.    (2)

Proof: on the first chart expand p_m(1+x²y) at t=1. Its Taylor term of
order j has x-exponent m+2j and y-exponent j. A given pair of exponents
can come from only one m, so there is no cancellation between different
m blocks. Polynomiality requires precisely (t-1)^k_m|p_m for m<0.
The second chart similarly requires (t+1)^k_m|p_m. These factors are
coprime. Conversely both divisibilities eliminate every negative x-power.
For m>=0 there is no restriction. This proves (2), including cancellations
WITHIN each entire p_m, not a termwise test on the original x,y monomials.

Consequently O(T)=C[x,y] intersect C[x,v] inside C[x,x^-1,y]. For the
grading wt(x)=1, wt(t)=0, wt(Z)=-2, its weight-m piece is x^m C[t] for
m>=0 and x^epsilon Z^k_m C[t] for m<0, where epsilon=m+2k_m is0 or1.
This also reconstructs the hypersurface ring directly from the intersection.

For G=sum_n x^n q_n(t), the FULL scalar bracket criterion is the finite
Laurent coefficient convolution

    sum_(m+n+1=ell) (m p_m q_n' - n p_m' q_n)
        = c if ell=0, and 0 otherwise.             (3)

Here primes differentiate t and every nonzero Laurent block is retained.
Formula(3) follows from {H,G}=x²(H_x G_t-H_t G_x), with x derivatives
taken at fixed t. It is not a new independent equation or a linearized
substitute for the bracket. Equations(2) are separately linear extension
conditions; (3) is the still-undecided quadratic interaction across them.
No support, total-degree, or pole-order bound is justified by this description.

The exact cancellation control H=Z=2y+x²y² becomes -2v+x²v² after (1).
Its two summands individually create negative x-powers, which cancel in
their sum. A monomial-by-monomial divisibility filter would falsely discard
this actual global function. A highest-block-only argument would also omit
the different (m,n) pairs that contribute to the same ell in (3).

## 3. Exactness and two-bracket controls do not supply one pair

The apparent rational one-form beta=dt/x is globally regular. On x!=0
this is clear; on t!=0 differentiation of the defining equation gives

    beta=(Z/t)dx+(x/(2t))dZ.

These opens cover T. Direct differentiation on their dense overlap gives
d beta=-omega, hence the identity holds globally. Thus nonzero second
cohomology alone cannot obstruct this particular volume form.

The Poisson relations are

    {x,t}=x²,     {x,Z}=2t,     {t,Z}=2xZ.

They yield the explicit identity

    {x,tZ}=3t²-1,      {xt,Z}=4t²-2,
    1=2{x,tZ}-(3/2){xt,Z}.                         (4)

This is a sum of TWO brackets of actual global polynomials, not one
scalar-bracket pair. Adding their arguments produces cross terms and is
not licensed. Ordinary Poisson homology, exactness, or a bracket-span
calculation therefore gives no closing test for the present endpoint.

Even the globally submersive coordinate H=x has no regular scalar mate.
On x!=0, {x,G}=c forces G_t=c/x², so G=c*t/x²+a(x) with
a(x) in C[x,x^-1]. Formula(2) at weight -2 would require
t²-1 to divide the nonzero linear polynomial c*t+a_-2, which is
impossible. No local smoothness or nonvanishing differential is enough.
The separate Astra task tests whether the COMPLETE unrestricted transition
and bracket provide any additional all-degree discriminator; its live
report is not a premise of this ROOT interface.

## 4. Primary fit, historical limits and allocation

The precise surface-to-A2 question was explicitly posed in Dubouloz's
[2009 Basel abstract](https://dubouloz.perso.math.cnrs.fr/GdTs/GdTAutos/Prog-Basel-09-11.pdf),
page2, which also explains why naive differential cohomology does not
immediately decide it. The broader reduction mentioned in that abstract is
NOT a theorem here reducing every JC2 map to this fixed T. The two-page
document was read whole through web and then from the hash-pinned local PDF.

The [2021 bracket-width paper](https://ems.press/content/serial-article-files/26631)
studies D_p={xy=p(z)}, not our x²Z=t²-1. Its printed pages1620–1622
distinguish sums of brackets from single brackets, leave a width-one versus
two question, and make their higher-degree theorem conditional on
Hypothesis(J). None supplies the missing pair or its impossibility on T.
Local PDF pages20–24 were read, not the whole paper. No theorem from it is
imported into sections1–3.

Primary PDF pins are

    basel-2009.pdf:
    b97a28d832703e66ce874b83de2cf07254ecc28078ffc45b128e05b6f36c47f7
    bracket-width-2021.pdf:
    5275f17154e83821076d8e851fb8cde99a3da1e4346517f07f774d721848710a

in box/danielewski-two-chart-interface-root-20260911/. SOURCES.md records
URLs and scope. Primary downloads are documentary retrieval, not scientific
execution. The preceding Moskowicz involution check and rational-deck
history check recovered already-known scope failures, not a new exclusion.
Selected exploratory reads of old reports were not freshly pinned whole
imports; the arguments above are self-contained. Some broad search outputs
clipped, so no exhaustive history or full-corpus novelty check is claimed.

Decision: retain the unrestricted surface as a broader sufficient construction
endpoint and the exact two-chart acceptance criterion, at MANUAL/UNREVIEWED
scope. This is a known classical question, not a new faster proof mechanism.
No finite degree farm, sparse/invariant ansatz, scientific execution or
automatic echo review is selected. A positive actual regular pair would
require independent full polynomial review before any JC2 claim. A theorem
excluding this one T would not by itself prove JC2.

QUANTITY: existence of a FINITE-support pair satisfying all of(2) and(3),
not bounded-order survival or a sum of brackets. CHEAPEST CURRENT TEST:
the assigned bounded manual all-degree transition discriminator; planning
under20minutes UNMEASURED, not a runtime estimate. No new canonical OPEN
or computational authority. Original ROOT publication reserve13:34/
HARD13:42UTC remains fixed. Final WHOLE readback, postpins and transaction
are required before consumption; no live external/AWS scientific process.

## COLLISIONS

status: KNOWN

- Exact T-to-A2 problem is documented in2009; no novelty claim. The
  invariant-S target is a subspace of the unrestricted sufficient target.
  Old rational-deck and generic cohomological shortcuts remain stopped.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9746`.
- Body SHA-256:
  `067091cdd2a4afc91361b0df2682da23c0d8e44f396ee84de8b0770d8d5f8849`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
