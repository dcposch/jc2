# TD6-GLOBAL-COMPATIBILITY-GATE — bare obstruction versus centered polynomial origin

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Target: the first genuinely global implication after the dual-confirmed D73
local equality control, tested on sharp single-pole class SP-2.  No new book
cell, D-series object, sparse search, or canonical edit is made.

## Verdict

**CENTERING-ESCAPE / FINITE-JET-CONTROL / STOP.**  There is a real global
polynomial obstruction in the *bare* chart

\[
  s=y^{-1},\qquad t=xy^4,
\]

but LR2 does not pin that chart.  It permits a common unramified Puiseux
truncation below height four.  The legal choice

\[
  x=y^{-1}+t y^{-4}
  \quad\Longleftrightarrow\quad
  T:=xy^4-y^3=t
  \tag{1}
\]

makes the centered coordinate `T` a global polynomial and defeats the bare
divisibility argument.

More sharply, there are explicit global polynomials inside the sharp SP-2
Newton rectangles, with boundary patterns

\[
  p_f(T)=T^{15},\qquad p_g(T)=T+T^{25},
\]

whose special fiber has exactly the same three-branch, total-`Lambda = 3`
equality mechanism as D73 and whose Jacobian equals one through successively
the first and second transverse orders.  A coefficientwise Bezout recursion
then constructs polynomial-origin approximants to *every* finite one-sided
x-chart order when the fixed global degree cap is dropped.

Thus neither the illegal `t`-independent `s^3` in the bare D73 formula nor any
fixed finite amount of one-sided x-chart data is a global obstruction by
itself.  The first missing implication really must use the **full fixed-degree
polynomial-origin module together with the pinned opposite-side data and exact
all-order `J=1`**, not merely the local germ or a bare-chart monomial rule.
No terminal class is killed or realized.

## 1. Hypotheses and provenance

The class under control is SP-2 from `SHEET6-LROOT.md`: in the campaign's
notation

\[
 (k_f,l_f)=(60,15),\quad (k_g,l_g)=(100,25),\quad
 R=\pi(G)=4,\quad \kappa_G=1,
\]

with one x-side cluster and no split or characteristic exponent below height
four.  Its x-side Newton rectangles, written as ordinary exponent bounds, are

\[
  0\leq i\leq15,\ 0\leq j\leq60\quad(f),\qquad
  0\leq i\leq25,\ 0\leq j\leq100\quad(g),
\]

with corners `x^15 y^60` and `x^25 y^100`.

The D73 control chose zero common truncation and the bare coordinate
`t=xy^4`.  LR2 pins *agreement* of all branches below height four; it does not
pin their common coefficients to zero.  A common `y^-1` coefficient is not a
characteristic exponent: for the D73 pole order five it is the index `5`,
divisible by the current gcd `e_0=5`, and it creates no split because it is
shared.  Hence (1) is allowed by exactly the local data presently on the
ledger.  A constant common term can be removed linearly, but the `y^-1` term
cannot be removed by a polynomial shear in `y`.

Charged inputs and hashes:

| artifact | SHA-256 |
|---|---|
| `ladder/SHEET6.md` | `50b4dc45bf091af35a481fead04b7f8f5b120008e97065bf0a5f80ff4ef7b4e3` |
| `ladder/SHEET6-CAMPAIGN.md` | `fca34f4cad606c9097cdb87c4e9e51609ab5c73d16a03efd764a7c06cdc4ccbb` |
| `ladder/SHEET6-LROOT.md` | `17b3875e98e31c09f8c8810a942d2d8424af07033c6d5af89d56f665377334d9` |
| `ladder/SHEET6-LT-REVIEW.md` | `82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6` |
| D73 producer | `90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de` |
| D73 different-model review | `3c0df2009432646bc6b93fa36f4c688b24af9e8df22629755303e89fde0fac3a` |

The R6/deeper-tower and redesigned-R1 artifacts were read as scope controls:
they concern the two-pole residue-A genome and already show why y-side window
consistency is not global `J`-closure.  Nothing below is imported into those
objects or represented as a replacement for their branch-specific gates.

## 2. The bare-chart obstruction is exact, but its hypothesis is not pinned

Let `R >= 2` and use the bare chart `x=t s^R`, `y=s^-1`.  A monomial is

\[
  x^i y^j=t^i s^{Ri-j}.
\]

If a polynomial `h(x,y)` is holomorphic at `s=0` in this chart, its
coefficient of `s^k`, `k>0`, is divisible by

\[
  t^{\lceil k/R\rceil}.
  \tag{2}
\]

Indeed every contributing monomial has `k=Ri-j` with `j>=0`, hence
`i >= k/R`.  Consequently `h_s(s,0)=0`.  If both members of a polynomial
Keller pair were holomorphic in the same bare chart, then

\[
  (f_sg_t-f_tg_s)(s,0)=0.
\]

But `dx wedge dy=s^{R-2} ds wedge dt`, which is nonzero for `s != 0`.
This is an exact contradiction.

For D73 at `R=4`, (2) also diagnoses the visible defect: its coefficient
`s^3/(3q'(t))` is nonzero at `t=0`, so it cannot be the chart expansion of a
polynomial in the *bare* coordinates.

The inference to SP-2 fails at one precise premise.  With a shared truncation
`phi(s)=s`, the actual centered chart is

\[
  x=s+t s^4=s(1+t s^3),\qquad y=s^{-1},
\]

and the polynomial `x^3` contributes a nonzero `s^3` coefficient at `t=0`.
Thus `f_s(s,0)` need not vanish.  LR2 supplies no theorem forcing
`phi=0`, and the opposite-side template has not yet been used to do so.

## 3. Exact fixed-rectangle polynomial control

Put, in the original affine coordinates,

\[
  u=xy-1,\qquad T=xy^4-y^3=y^3u.
  \tag{3}
\]

Then

\[
  Tx^3=u(1+u)^3,
  \qquad
  \det\frac{\partial(x,T)}{\partial(x,y)}=y^2(1+4u).
  \tag{4}
\]

### 3a. First transverse order

Define

\[
\begin{aligned}
 f_3&=T^{15}+\frac13x^3,\\
 g_3&=T+T^{25}+\frac59T^{10}x^3.
\end{aligned}
\tag{5}
\]

These are global polynomials.  Their supports lie in the SP-2 rectangles and
their height-four boundary patterns are exactly `T^15` and `T+T^25`.
Direct differentiation gives the exact identity

\[
 J(f_3,g_3)
 =(1+u)^2(1+4u)
  \left(1+\frac{50}{9}T^9x^3\right).
 \tag{6}
\]

In the centered chart `u=Ts^3`, `x=s(1+Ts^3)`, so

\[
  J(f_3,g_3)=1+O(s^3).
\]

The pair is **not** Keller—(6) is visibly nonconstant—but it meets the exact
leading Jacobian equation which the bare argument claimed was impossible.

On the exact special fiber `f_3=0`,

\[
  x^3=-3T^{15},\qquad
  g_3=T-\frac23T^{25}.
  \tag{7}
\]

Because `gcd(3,15)=3`, (7) has three normalized branches.  Taking `T` as
uniformizer, each has `x=rho*T^5`, `rho^3=-3`, and (4) gives
`y=(1+u)/x` with `u=O(T^16)`.  Hence each branch has `y`-pole order five,
the common term is `x=y^-1`, the first separation is at order
`T^21 ~ y^(-21/5)`, and `g_3` has multiplicity one.  Thus

\[
  \sum\Lambda=3=\pi(G)-1
\]

exactly as in D73.  This is a polynomial-origin control of the entire local
equality mechanism, not a polynomial Keller realization.

### 3b. Second transverse order, still in the same rectangles

Set

\[
\begin{aligned}
 f_6={}&f_3-left(T+\frac{25}{27}T^9\right)x^6,\\
 g_6={}&g_3-left(\frac53T^{11}+\frac{125}{81}T^{19}\right)x^6.
\end{aligned}
\tag{8}
\]

Every monomial of `f_6` still satisfies `i<=15,j<=60`, and every monomial
of `g_6` satisfies `i<=25,j<=100`; the two corner coefficients remain one.
Exact sparse differentiation and centered substitution give

\[
  J(f_6,g_6)=1+O(s^6),
  \tag{9}
\]

with valuation exactly six.  Thus the fixed SP-2 rectangles already absorb
two successive transverse Jacobian corrections.  No first- or second-order
global wedge mismatch exists.

## 4. Arbitrary finite one-sided jets without a fixed degree cap

Equations (3)--(4) also give a clean formal theorem over the coefficient ring
`Q[T]`.  Complete only in the transverse variable `x`, so the ambient ring is
`Q[T][[x]]`.  Let `w=Tx^3` and let `u(w)` be the unique formal solution of

\[
  u(1+u)^3=w,\qquad u(0)=0.
\]

Existence and uniqueness use the formal implicit-function theorem at `u=0`:
the derivative of `u(1+u)^3` there is one, so no localization or nonvanishing
hypothesis on `T` is required.  For formal series `F(x,T),G(x,T)`, the exact
Keller equation in this one-sided completion is

\[
  F_xG_T-F_TG_x=x^2u'(Tx^3).
  \tag{10}

Write

\[
 F=T^{15}+\sum_{n\ge1}A_n(T)x^n,
 \qquad
 G=T+T^{25}+\sum_{n\ge1}B_n(T)x^n.
\]

At coefficient `x^(n-1)`, after the lower coefficients are fixed, (10) is
the single linear equation

\[
 n\bigl(A_nq'-p'B_n\bigr)=H_{n-1}(T),
 \tag{11}
\]

where `H_(n-1)` is already polynomial.  Here

\[
  p'=15T^{14},\qquad q'=1+25T^{24},\qquad \gcd(p',q')=1.
\]

In fact there is an explicit Bezout identity in `Q[T]`,

\[
 q'-\frac53T^{10}p'=1.
\]

Therefore (11) has polynomial solutions at every order.  The only scalar
divisions in the recursion are by the positive integer `n` (and the displayed
rational constants), so this statement is characteristic zero.  Lagrange
inversion gives the target explicitly:

\[
 u'(w)=\sum_{k\ge0}(-1)^k\binom{4k+2}{k}w^k.
\]

Truncating after any `n=N` produces `F_N,G_N in Q[T,x]`; composing with the
global polynomial `T=xy^4-y^3` gives actual members of `Q[x,y]`.  Their
boundary patterns remain `p,q`.  The bracket in (10) is correct modulo
`x^N`; multiplication by the coordinate factor
`y^2(1+4u)=x^-2(1+u)^2(1+4u)` therefore gives

\[
 J(F_N,G_N)=1+O(x^{N-2}).
\]

Thus any prescribed one-sided order `M` is obtained by taking `N>=M+2`.
The replay constructs and independently verifies the coefficient recursion
through `x^18`.

This statement deliberately drops the fixed SP-2 degree rectangles.  The
degrees of `A_n,B_n`, and hence the ordinary `x,y` degrees after composition,
grow with `N`.  In the replay's canonical solution, the `x^9` coefficient of
`F` already has `T`-degree ten, outside the naive `Q[T,x]` rectangle allowance;
only the explicit truncation through `x^6` in section 3b is asserted to stay
inside the fixed SP-2 rectangles.  The `x^9` event is **not** an SP-2
obstruction: `Q[T,x]` is a strict subring of the true polynomial-origin
completion.  For example, the global polynomial `xy=1+u(Tx^3)` has an
infinite `Q[T][[x]]` expansion.  A valid fixed-degree obstruction must compile
the full original `Q[x,y]` rectangle and the opposite end, rather than mistake
this convenient subring for all polynomial origins.

Finally, this is intrinsically one-sided.  The completion is only along the
x-side place `x -> 0`, `xy -> 1`; it neither constructs nor constrains the
r9/M2 pole-side expansion, the other points at infinity, global mapping
degree, or the finite affine critical locus.  The infinite formal pair need
not converge or algebraize, while each finite truncation has merely a high-
order Jacobian congruence, not `J=1` exactly.

## 5. Smallest missing implication and successor discipline

The smallest honest implication left for SP-2 is:

> Given the full fixed Newton rectangles, the sharp LR2 centered x-side
> cluster, and the pinned r9/M2 y-side pole/terminal patterns, prove that no
> single pair of polynomials can realize both chart expansions while satisfying
> `J=1` exactly—or exhibit such a pair.

The control above makes three restrictions mandatory for any successor:

1. **Centering is data.**  Carry the full shared integer truncation
   `phi(s)=c_1s+c_2s^2+c_3s^3`; setting it to zero is an additional theorem,
   not a gauge already supplied by LR2.
2. **Use the full polynomial-origin module.**  Compile coefficients directly
   from the finite `C[x,y]` rectangles (or an exactly equivalent module), not
   only from `C[T,x]` or a local analytic ring.
3. **Couple both ends before interpreting a contradiction.**  The x-chart
   alone admits arbitrary finite formal Keller jets.  A useful row must either
   consume the opposite-side r9/M2 patterns or be an exact all-order/global
   support identity.

A bounded successor is therefore a direct two-chart coefficient transport for
SP-2, with the three common-centering coefficients explicit and with exact
Jacobian rows emitted from the original rectangle.  The first gate should be
rank/consistency at the earliest band where the y-side entry family enters;
a contradiction confined to the bare or `C[T,x]` chart is pre-registered as a
wrong-object stop.

## 6. Scope and stop

This report proves:

- the bare-chart divisibility lemma and its exact scope;
- an explicit centered global-polynomial control matching the SP-2 x-side
  boundary data and local equality mechanism;
- two transverse Jacobian corrections within the fixed SP-2 rectangles; and
- arbitrary finite one-sided polynomial-origin Keller jets without a fixed
  degree cap.

It does **not** prove that `f_3,g_3` or `f_6,g_6` is Keller; both have
nonconstant Jacobian.  It does not construct the r9/M2 opposite-side pole
tree, establish mapping degree six, realize or kill SP-2, affect the other
seven terminal classes, close landing/coverage, `G2-PSC`, or `G2-BD`, or
prove/disprove JC2.

Verdict for this bounded gate: **STOP the bare-divisibility/global-illegal-term
attack.**  Bank the centered control and move only to a genuinely two-chart,
fixed-origin compatibility compiler.

## 7. Exact replay

Artifact:

```text
cases/td6_global_compatibility_20260824/replay.py
SHA-256 d5d0d4d4209ef115b952571082c37252eb0f1e032e02f182cdccf516b29519d9
```

Run:

```bash
python3 cases/td6_global_compatibility_20260824/replay.py
```

Expected terminal line: `TD6 global-compatibility replay: PASS`.  The replay
uses only exact `fractions.Fraction` sparse arithmetic; it expands both global
polynomial pairs, checks their Newton rectangles, differentiates the exact
Jacobians, verifies centered valuations `3` and `6`, checks the special-fiber
reduction, audits 1,326 bare-chart monomials, and reconstructs (11) through
`x^18`.
