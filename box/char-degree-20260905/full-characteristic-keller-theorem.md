# What imposing every effective characteristic degree would force

This theorem concerns a **full** recursively compatible characteristic
sequence. The present finite runs impose T2 only. It neither upgrades
those runs to Keller pairs nor asserts that the full sequence has a
solution.

## Algebraic theorem

Work over an algebraically closed field of characteristic zero. Let
`F,G in k[x,y]` have total degrees equal to their y-degrees, and let
`deg F=n`. Suppose constant-coefficient target polynomials
`T_i(U,V) in k[U,V]` compose as
`H_i=T_i(G,F)`, for i=1,...,s. Assume:

1. `T1=U+P(V)`, so its formal U derivative is 1.
2. The recurrence has the specialized Proposition-3.1 form
   `T_(i+1)=T_i^(n_i)+sum c_(j,alpha) V^j product_(l<=i) T_l^(alpha_l)`.
   Every summand of nonzero coefficient has weight
   `W=jn+sum alpha_l D_l<=n_i D_i`. A summand of equality weight has
   `alpha_i=0`; there is at most one such summand. All c are scalars.
3. Every H_i has **actual total degree** D_i and nonzero leader,
   with `D1=-M1`, strictly increasing M_i, and
   `D_(i+1)=n_i D_i-(M_(i+1)-M_i)`.

Then the composed formal derivative has actual total degree

\[
\deg\bigl((\partial_U T_i)(G,F)\bigr)=D_i+M_i.\tag{1}
\]

**Proof.** For i=1 the derivative is 1 and `D1+M1=0`. Assuming (1)
through i, differentiate the displayed recurrence in U, holding V
fixed. The derivative of its first term is

\[
n_i H_i^{n_i-1}(\partial_U T_i)(G,F),
\]

a nonzero polynomial of degree `n_i D_i+M_i`. For a lower summand,
differentiating its l-th factor produces degree at most `W+M_l`.
If W is strictly below `n_i D_i`, this is strictly below the first
term's degree, since `M_l<=M_i`. If W equals `n_i D_i`, the
restriction `alpha_i=0` means every differentiated factor has l<i,
so `M_l<M_i`, again strict. Thus no lower term can cancel the
first derivative's leading form. Its degree equals
`n_i D_i+M_i=D_(i+1)+M_(i+1)`. Induction proves (1).

The field characteristic, scalar coefficients, and actual total
degrees are essential. Degree upper bounds alone do not prove the
nonzero leading derivative term. Unspecialized coefficients in k[x]
would also add extra x-derivative terms to the chain rule below.

## The Jacobian bound

Because T_s has constant target coefficients, the chain rule gives

\[
J(F,H_s)=(\partial_U T_s)(G,F)\,J(F,G).
\]

The left side has total degree at most `n+D_s-2`. If J(F,G) is
nonzero, degree additivity and (1) give

\[
\deg J(F,G)\le n-M_s-2.\tag{2}
\]

For a two-point effective tower, `M_s=n-2`; hence J is either zero
or a nonzero constant. Formula (1) is also the total-degree analogue
of printed Moh Proposition 3.2(3), p159, with its specialization
remark on p161. Here it is proved directly for the allowed target
family, so no assertion that an arbitrary chart point is already a
realized datum is needed.

At T2 alone, (2) gives 99-77-2=20 and 108-81-2=25, exactly the
earlier shallow-band bounds. At T3, it gives zero in both clients.

## The unequal two-point top excludes the zero case uniformly

Suppose additionally that F's leading homogeneous form has exactly
two distinct linear factors, of unequal positive multiplicities,
and that the characteristic gcd identity holds:

\[
\gcd(n,D_1,\ldots,D_s)=\gcd(n,M_1,\ldots,M_s).
\]

Since `M_s=n-2`, this gcd divides 2. If J were identically zero,
the common-polynomial composition theorem would give
`F=f(H),G=g(H)` with H polynomial. The primary source is
Arzhantsev–Petravchuk, *Closed and Irreducible Polynomials in Several
Variables*, [Lemmas 4–5, p5](https://arxiv.org/pdf/math/0608157),
audited in `nondegeneracy-theorem.md`.

Let k0 be H's y-degree. Equality of total and y-degree for F makes
H's total degree k0 as well. Since F and every H_i lie in k[H],
k0 divides the displayed gcd, so k0 is 1 or 2. For k0=1, F's
top is a power of a single linear form, impossible. For k0=2,
F's top is a power of H's quadratic top. To have exactly two
distinct linear factors, that quadratic has each factor once;
F consequently has equal multiplicities n/2 at the two factors,
also impossible. Thus J is not zero.

Combining this with (2), the full compatible effective
characteristic-degree chart with these unequal two-point tops
**forces J(F,G) to be a nonzero constant**.

## Printed necessity and limits of the interpretation

The scalar recurrence and its weight/equality restrictions come from
Moh Proposition 3.1, p157, and the coefficient-specialization remark
on p159. Degree recurrence and gcd identity are the p150 and p154
characteristic arithmetic. Proposition 2.2, p152, gives exact y
degrees and unit leaders at effective indices. Proposition 4.3,
p166, implies a realized two-point tower must contain `M_s=n-2`;
Proposition 4.5, p169, supplies unequal top multiplicities. The
minimum-root-order argument in the proof of Proposition 4.5, p172,
gives total degree equal to y-degree for every effective H_i in the
existing coordinates. These source bridges were independently
audited in `source-audit.md`.

Thus imposing **all** such compatible attainment and total-degree
rows is a re-expression of the full Keller obstruction on these
two-point charts, not an automatically cheap source of leaf kills.
The earlier-index homogeneous faces follow the common top form;
the last characteristic face must not be copied from them without
its separate source formula. Prefix-only child data do not supply
the missing later target polynomials, their attainment rows, or a
child Keller hypothesis.

No computation in this appendix decides existence of a solution to
the full sequence. In particular, the verified T2-only chart
survivors, if present, may have nonconstant Jacobian of degree up
to 20 or 25. No exit price is asserted.
