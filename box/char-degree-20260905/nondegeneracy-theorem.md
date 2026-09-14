# The characteristic instrument excludes every identically-zero Jacobian point

This appendix proves a conditional theorem about the **full coefficient
chart**. It does not infer a chart unit or report an explicit surviving
coordinate assignment. It strengthens the Delta exclusion once the
printed, derived major faces and exact attained degree are included.

## Supplementary primary source

The one supplementary source, fetched independently of the charged Moh
PDF, is Ivan V. Arzhantsev and Anatoliy P. Petravchuk, *Closed and
Irreducible Polynomials in Several Variables*, arXiv:math/0608157v2
(20 May 2007), [primary PDF](https://arxiv.org/pdf/math/0608157).
The retained file is `arzhantsev-petravchuk-closed-polynomials.pdf`,
SHA-256
`70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28`.
Its layout extraction's lines 223–245 are the relevant portion of p5.

Lemma 4 on p5 identifies algebraic dependence in characteristic zero
with vanishing of the two-by-two Jacobian minors. Lemma 5 says that
algebraically dependent nonconstant polynomials are both polynomials
in one common polynomial H. The latter lemma follows there by Noether
normalization and the paper's Proposition 1 about integral closure.
For the present two-variable problem these statements supply
`J(F,G)=0 => F=f(H), G=g(H)` for some `H in k[x,y]` and `f,g in k[T]`.
These are the only external facts used below; the remaining argument
is derived here.

## Exact face hypotheses and their stage-0 derivation

Work over an algebraically closed characteristic-zero field. The source
coefficient chart has total degrees equal to y-degrees. Its leading
homogeneous forms, fixed by the printed two-point data, are:

| client | F top | G top | h2 degree | K2 D2 face |
|---|---|---|---:|---|
| (99,66) | `y^27(y-x)^72` | `y^18(y-x)^48` | 33 | `(pi^3-1)^8` |
| D=108 | `y^24(y-x)^84` | `y^16(y-x)^56` | 36 | `(pi^4-1)^7` |

Here `K2=t^k h2(t^-1,(1+z)t^-1)`, with k=33 or 36; its D2 weights
are 96 and 140. The covers are `(t,z)=(s^3,pi*s^4)` and
`(s^4,pi*s^5)`. The normalized F and G are

\[
K_F=K_2^3+tK_{A2}K_2+tK_{A3},\qquad
K_G=K_2^2+tK_{B1}K_2+tK_{B2}.
\]

All four outer remainder polynomials have y-degree less than k. Their
source-derived total-degree bounds and D2/D1 floors are those in
`source-audit.md` and the charged corrected reports. The faces above
are derived source targets; they are not new arbitrary coefficient
pins. The following calculation proves that the **offset-0 outer D1
rows** already remove every outer equality face, so the actual F/G
faces are powers of the K2 face at every stage 0–8.

For an outer block with normalized degree bound B, D2 floor W0, and
D1 threshold E0, enumerate exactly the sites

\[
0\le q<k,\quad r\ge0,\quad r+q\le B,\quad
u r+v q=W_0,
\]

where `(u,v)=(3,4)` or `(4,5)`. Every equality q is divisible by u.
The face is therefore `P(pi)=S(pi^u)`. At offset zero, the D1 row with
index j is `[epsilon^j]P(1+epsilon)=0`, for
`0<=j<E0-L*W0`, with L=3 or 2. Thus P has a root at pi=1 of that
multiplicity. Since the derivative of pi^u at pi=1 is u!=0 in the
field, S has the same multiplicity at its argument 1. The table gives
all equality powers and the required vanishing order.

| client/block | W0 | E0 | equality q | deg S | required order |
|---|---:|---:|---|---:|---:|
| 99 A2 | 189 | 583 | 0,3,...,30 | 10 | 16 |
| 99 A3 | 285 | 879 | 0,3,...,30 | 10 | 24 |
| 99 B1 | 93 | 287 | 0,3,...,21 | 7 | 8 |
| 99 B2 | 189 | 583 | 0,3,...,30 | 10 | 16 |
| 108 A2 | 276 | 566 | 0,4,...,32 | 8 | 14 |
| 108 A3 | 416 | 853 | 0,4,...,32 | 8 | 21 |
| 108 B1 | 136 | 279 | 0,4,...,24 | 6 | 7 |
| 108 B2 | 276 | 566 | 0,4,...,32 | 8 | 14 |

In each row the required order exceeds deg S, so S is zero. The
control `nondegeneracy-controls.py/.json` independently enumerates every
site and computes the ranks over Q of the matrices `binom(q,j)`:
`11,11,8,11` and `9,9,7,9`. These are full column ranks. Hence each
equality coefficient is an actual rational-row consequence.

The implementation contains precisely these offset-zero coefficient
rows in `box/g9966-corrected-20260905/engine.py:175` and
`box/d108-rekill-20260905/work/rekill_engine.py:330`. The D108 driver
independently confirmed their transportation through `outer_state(0)`;
the 99 driver does the same in the source map. A replacement engine
must preserve these source rows under every later graph substitution.

Consequently the actual leading faces are

\[
\operatorname{face}_{D2}F=(\pi^3-1)^{24},\qquad
\operatorname{face}_{D2}G=(\pi^3-1)^{16}
\quad\text{for }(99,66),
\]
\[
\operatorname{face}_{D2}F=(\pi^4-1)^{21},\qquad
\operatorname{face}_{D2}G=(\pi^4-1)^{14}
\quad\text{for D=108}.
\]

These formulas identify actual leading polynomials. Their physical
s-valuations are
`ord_s F=3*96-3*99=-9` and `ord_s F=3*140-4*108=-12`.
The nonzero polynomial faces ensure these are equalities, not floors.

## The theorem

**Theorem.** In either full source coefficient chart above, include the
offset-zero outer D1 rows and the stated nonzero K2 D2 face. Suppose
there is a constant-coefficient polynomial Q(F,G) having actual y-degree
55 in the first chart or 63 in the second chart. Then `J(F,G)` is not
the zero polynomial.

In particular the theorem applies to the five-target family
`Q=G^3-F^2+aG^2+bFG+cF+dG+e0` with all exact degree, scalar-leader and
localizer rows. It uses actual degree; a mere degree upper bound does
not suffice.

**Proof.** Assume J is identically zero. By the two cited lemmas,
`F=f(H)` and `G=g(H)` for a polynomial H and univariate f,g. Since F
depends on y, let `k=deg_y H>0`. Degree of composition over the domain
k[x] gives

\[
\deg_y F=(\deg f)k,\quad \deg_yG=(\deg g)k.
\]

The total degree of F similarly equals `(deg f) deg H`. Because
`deg F=deg_yF`, we have `deg H=deg_y H=k`. Every constant-coefficient
Q(F,G) is in k[H]; its actual positive y-degree is also a multiple of
k. Therefore

\[
k\mid\gcd(n,m,\deg_y Q).
\]

For (99,66), this gcd is 11, so k is 1 or 11. If `u=deg f=99/k`, then
the leading homogeneous form of F is a nonzero scalar times
`H_top^u`. Unique factorization of `y^27(y-x)^72` requires u to divide
both 27 and 72, hence to divide 9. The option k=1 gives u=99 and is
impossible. Thus k=11 and u=9.

For D=108, k divides 9, so k is 1,3 or 9. Unique factorization of
`y^24(y-x)^84` requires u=108/k to divide gcd(24,84)=12. Only k=9
works, and u=12.

Evaluate the common polynomial H on the D2 cover. The coefficients
of f are constants. Since F has negative s-valuation, H must have
negative s-valuation. At negative valuation, the highest power of H
in f(H) has strictly lower valuation than every lower power; no
cancellation with another f-term is possible. Therefore

\[
\operatorname{ord}_s F=u\operatorname{ord}_s H,
\qquad\operatorname{face}_{D2} F
   =\operatorname{lc}(f)\operatorname{face}_{D2}(H)^u.
\]

The valuations above give `ord_s H=-1` in each case. In particular the
F face is, up to a nonzero scalar, a ninth power or a twelfth power
in k[pi]. Every root multiplicity in it must be divisible by 9 or 12.
But the actual source faces have multiplicities 24 at each of the
three simple roots of pi^3-1, or 21 at each of the four simple roots
of pi^4-1. Neither 24 is divisible by 9 nor 21 by 12. Contradiction.
This proves the theorem. No Jacobian row was used in this argument.

## Consequence for an exact NONUNIT result

Suppose a stage's complete augmented ideal is explicitly declared in
a finite polynomial ring over Q, all localizations are represented by
Rabinowitsch equations, and a verified exact computation establishes
that the ideal is proper. A faithfully embedded occurring-variable
ring is also acceptable, with the free unused variables restored.
Extending scalars to the algebraic closure preserves properness;
equivalently, the quotient algebra tensored with an extension field
is nonzero. The weak Nullstellensatz then supplies a point over
`overline(Q)` satisfying every row, including every localizer.

Because the degree-and-leader rows give actual degree and the stage-0
source rows give the faces above, the theorem proves that this point
has `J(F,G)` **not identically zero**. Thus a correctly certified
NONUNIT augmented ideal establishes existence of a nondegenerate
necessary-chart survivor even if no coordinate assignment has been
extracted. It must be reported as **existence over the algebraic
closure**, not as an exhibited rational or algebraic point.

This does not show that J is a nonzero constant. Finite stages test
only some Jacobian coefficients; a nonconstant coefficient in an
untested band may be nonzero. It does not produce a Keller pair,
Jacobian-conjecture counterexample, complete datum realization, or
leaf kill. Conversely, a Gröbner timeout or an unchecked “dimension”
message is not a proof that the ideal is proper.

## Relation to T3 and uniformity

The first effective characteristic degree sequence is 66,55,145;
the second is 72,63,227. With F included, their degree gcds are 1.
Therefore imposing *all* effective attained-degree rows supplies a
different exclusion of J=0: the common generator above must have
y-degree 1 and total degree 1, forcing F's top to be a power of a
single linear form, contrary to the two-point top. This alternative
does not require the D2 face, but it requires the additional T3 rows.

For a general leaf, the same argument is a criterion, not an
automatic result: compute the gcd of the attained characteristic
degrees and check divisibility against the top and actual local face
multiplicities. In particular an effective tower ending before the
terminal `M_h=n-1` can have residual gcd greater than 1. The uniform
necessity theorem does not by itself say that all such leaves lose
every algebraically dependent point, nor that any leaf is empty.

No new exit-price assertion is made. No charge-basis line applies.
