# Printed characteristic-degree necessity: independent source audit

This audit reads the frozen Moh PDF at
`/tmp/jc2-lane.Q25z05/inputs/moh1983_jram340_configurations_of_roots.pdf`.
The parent mechanically verified the charged hashes before delegation. The
fresh extraction is `moh-layout.txt`; the retained page images are
`source-pages/p-NN.png`, where PDF page NN has printed page NN+139. Equations
lost by extraction were read from images. The source is Moh's article; calling
its Lemma 2.1 a “Keller lemma” identifies its hypothesis, not its authorship.
No source file, ledger, `jc2-lean`, or `ideation-*` was edited or executed.

## 1. Exact printed chain

**Printed p150, final two displays** (`source-pages/p-11.png`; extraction
lines 562–582) defines

\[
d_1=n,\quad d_{j+1}=\gcd(n,M_1,\ldots,M_j),\quad
n_j=d_j/d_{j+1},\quad q_1=M_1,\quad q_j=M_j-M_{j-1},
\]
\[
\lambda_j=\sum_{i=1}^j q_i d_i,\qquad
\mu_j=\lambda_j/d_j,\qquad \theta_j=\mu_j-M_j.
\]

The same page defines the expansion, with formal parameter eta,
`g(x,y)=eta^(-n)` and
`f(x,y)=eta^(-m)+sum_(j>-m) f_j(x) eta^j`. The index M_j is a
first nonzero coefficient index with a prescribed gcd drop. It is not a
label for an auxiliary polynomial root's degree.

**Printed p151, Lemma 2.1** (`source-pages/p-12.png`; extraction 593–613)
states that `J_(x,y)(f,g)` is a nonzero constant if and only if

\[
e:=\operatorname{ord}_\eta\left(\sum f_j(x)\eta^j-
                                  \sum f_j(0)\eta^j\right)=n-1,
\quad \deg_x f_{n-1}(x)=1.
\]

The prime in its proof is an actual x-derivative: the proof writes
`f_i'(x)=0` for `i<n-1` and `f_(n-1)'(x)` a nonzero constant. Thus all
`f_j(x)` with `j<e` are constants. The paragraph following the proof
establishes `M_i<=n-1` and `y in k(x,f(x,y),g(x,y))` for a genuine pair.

**Printed pp151–152** introduces `psi:k[x]->k`, `x->0`, and extends it to
`k[x][f,g]` with **f and g formal symbols**. It does not substitute zero
into the source-coordinate x of the composed pair. **Proposition 2.1, p152**
(`source-pages/p-13.png`; extraction 646–669) states that the d_r-th
approximate root commutes with this coefficient specialization. In
particular `T_r^psi(f,g)` lies in `k[f,g]`, whereas the unspecialized
`T_r(f,g)` has coefficients in `k[x]`. The paragraph below the proof spells
out this distinction explicitly (extraction 671–678).

**Printed p152, Proposition 2.2(1)–(3)** (same image; extraction 682–690)
has hypothesis `M_r<=e` and gives

\[
\deg_y T_r^\psi(f(x,y),g(x,y))
=\deg_y T_r(f(x,y),g(x,y))=-\mu_r.\tag{P2.2(1)}
\]

If `M_r<e`, both composed polynomials are monic in y, by part (2). If
`M_r=e`, part (3) instead gives leading term
`c f_e(x) y^(-mu_r)` with `c` a nonzero constant.

**Printed p154, end of proof** (`source-pages/p-15.png`; extraction
774–778) explicitly says that “monic” means that the coefficient of the
highest term is a unit. Since the coefficient ring is `k[x]`, this means
a nonzero scalar in k; it does **not** mean that the scalar has already
been normalized to 1.

**Printed p157, Proposition 3.1** (`source-pages/p-18.png`; extraction
934–943) gives the unique expansion

\[
T_{r+1}=T_r^{n_r}+\sum c_{j,\alpha}\,g^j
               \prod_{i=1}^{r}T_i^{\alpha_i},
\]

where `0<=alpha_i<n_i` for `i<r`; for `M_r<e`, also
`alpha_r<n_r`, and every nonzero summand has composed y-degree at most
`(-mu_r)n_r`. Exactly one summand attains that upper weight, and its
`alpha_r` is zero. Coefficients initially lie in `k[x]`. **Printed p159,
Remark** (`source-pages/p-20.png`; extraction 1048–1052) says the proposition
remains valid after psi. Hence the specialized expansion's target
coefficients are constants.

**Printed p174, Definition–Remark** (`source-pages/p-35.png`; extraction
1841–1843) defines the *effective* indices: exclude the final `M_h` if
`M_h=n-1`; denote the last remaining index by s. Consequently, for a
realized Keller datum, every `i<=s` has `M_i<e`, and each composed
`T_i^psi` has actual y-degree `-mu_i` and nonzero scalar leader. Extending
the scalar-unit assertion to a terminal `M_h=e` is false: that leader is
`c f_e(x)`, of x-degree 1.

These statements establish actual degree and attainment. Neither the root
chart's support bounds alone nor a numerical assignment of tower labels
establishes them for every point in a necessary chart.

## 2. The necessary-chart theorem

Let k have characteristic zero, and let a realized monic Keller pair
`(F,G)` of y-degrees `(n,m)` have the specified effective characteristic
data when read in Moh's order `(f,g)=(G,F)`. For every `i<=s`, there is a
specific specialized characteristic polynomial `T_i^psi(U,V)` in the
formal target variables, with constant coefficients, whose composition
`T_i^psi(G(x,y),F(x,y))` has y-degree `D_i=-mu_i` and leading coefficient
in `k^*`.

Every necessary chart intended to contain all such realized data may
therefore add the coefficient equations defining these compositions,
all scalar coefficients of y-powers greater than D_i, all positive
x-coefficients of the y^D_i coefficient, a scalar equation setting its
constant x-coefficient to a new variable `lambda_i`, and
`Z_i*lambda_i-1=0`. The theorem says these are necessary; it does not
say that every point satisfying them has the prescribed characteristic
data or a nonzero Jacobian.

There are two sound ways to make the target polynomials into chart
coordinates. First, construct them canonically. For monic `F(0,y)`, put

\[
R(U,V)=\operatorname{Res}_y(F(0,y)-V,\ U-G(0,y)).
\]

This is monic of U-degree n. On realized data it is the coefficient
specialization of the defining equation in Moh's construction. Take
the polynomial part of `R^(1/d_i)` as a Laurent expansion at `U=infinity`
to obtain the monic d_i-th approximate root. Its finitely many
coefficients are polynomials over Q in the original coefficient
coordinates: the recursion divides only by nonzero integers. Composing
it with `(U,V)=(G,F)` gives an explicit polynomial map. Proposition 2.1
licenses this map for realized data.

Second, retain the finite constant target coefficient family allowed by
Proposition 3.1 and existentially impose the degree and leader rows.
This may enlarge the canonical locus, which is safe for a necessary
chart kill. Its polynomials must be called family representatives unless
the canonical defining identities are also imposed. A point of this
enlargement is not automatically a realization.

## 3. Arithmetic for the two clients

`source-audit-controls.py/.json` mechanically recomputes the gcds,
increments, lambda values and degrees over Q.

| Datum | n,m | M | d | lambda | Actual degrees of T1,T2,T3 |
|---|---|---|---|---|---|
| (99,66) | 99,66 | -66,77,97 | 99,33,11,1 | -6534,-1815,-1595 | 66,55,145 |
| D=108 | 108,72 | -72,81,106 | 108,36,9,1 | -7776,-2268,-2043 | 72,63,227 |

Thus the first three degree ratios, including F, are `99:66:55=9:6:5`
and `108:72:63=12:8:7`. The second characteristic polynomials have degrees
55 and **63**. The auxiliary h2 degrees 33 and 36, and auxiliary h3
degrees 11 and 9, must not be substituted for characteristic degrees.
All listed M_i are strictly below e=98 or 107.

For T2, `n_1=3`. The formal T1 has target G-degree one, and its specialized
composition has y-degree m<n. Therefore `T1^psi=G+constant`: a nonconstant
polynomial in F in its remaining coefficient would have y-degree at
least n. Proposition 3.1 lists exactly the monomials

\[
1,\quad G,\quad G^2,\quad F,\quad FG,\quad F^2
\]

in addition to `G^3`. Their weights are `nj+ma<=3m` with `a<3`.
The unique maximum weight is the F^2 term. Monicity of F and G and
`D_2<3m=2n` force its coefficient to be -1. Absorb the constant shift of
T1 into the lower coefficients. The complete family is consequently

\[
Q=G^3-F^2+aG^2+bFG+cF+dG+e_0.\tag{*}
\]

All five lower targets are retained. In the degree-only family the
constant `e_0` is **not** determined by the upper-degree or leader rows:
it changes only `[x^0 y^0]Q`. The canonical approximate-root map fixes
it, but a necessary existential enlargement may leave it free.

The other four coefficients admit a polynomial triangular recovery
from the source coefficients. Starting with `Q0=G^3-F^2`, set

\[
b=-[x^0y^{n+m}]Q0,\quad Q1=Q0+bFG,
\]
\[
a=-[x^0y^{2m}]Q1,\quad Q2=Q1+aG^2,
\]
\[
c=-[x^0y^n]Q2,\quad Q3=Q2+cF,
\]
\[
d=-[x^0y^m]Q3,\quad Q4=Q3+dG.
\]

The selected leaders are 1 because F,G are monic. The heights are
165,132,99,66 for (99,66) and 180,144,108,72 for D=108. All unselected
coefficients, including positive x-coefficients at the selected heights,
remain equations. This is a valid elimination, not a coefficient cap.

## 4. Exact scalar rows, and the depth issue

For (*) the total degree is at most `L=2n=3m` because the chart starts
with total-degree bounds n,m on F,G. This is only an ambient finite
bound, not an assertion that `deg_(x,y)Q=D_2`. Write
`q_ij=[x^i y^j]Q`. The exact rows are

\[
q_{ij}=0\quad(j>D_2,\ i+j\le L),
\]
\[
q_{i,D_2}=0\quad(i\ge1,\ i+D_2\le L),\qquad
q_{0,D_2}-\lambda=0,\qquad Z\lambda-1=0.
\]

Every q_ij is a polynomial over Q in the original chart coordinates and
the target coefficients. For a graph map produced by exact rational
pivots, compose this polynomial map with that graph. If an occurring
variable ring is used for a Gröbner calculation, state its embedding and
retain the full free variables in the dimension account.

At the attained leading row one subtracts lambda; one never emits
`q_(0,D2)=0`. This is the same equality-versus-target distinction behind
the gate's leading-pole-row check. The localizer is additional; no source
dilation is spent to set lambda=1.

Proposition 2.2 alone asserts y-degree, not total degree. Under
`t=1/x,w=ty,z=w-1`, an individual physical coefficient `x^i y^j` of Q
lands in `t^(L-i-j)(1+z)^j`. At t-depth r one obtains a polynomial
`H_r(z)` of degree at most L-r; expanding it in `w=1+z` gives precisely
the physical coefficients with `i+j=L-r`. Thus the exact P2.2-only
y-degree row test on H_r is `deg_w H_r<=D_2` (plus the scalar-leader
exceptions). The stronger claim `H_r=0` for every `r<L-D_2` needs the
additional printed source argument supplied immediately below.

The attained coefficient `[x^0 y^D2]Q` lies at depth
`L-D_2=143` or **153**. These are earlier than the degree-zero Jacobian
depths 163 and 178, respectively, but are not small depths 0–8. Some
upper-degree equations have early bands, while the attainment row is
deep. Merely adjoining the symbol lambda to a truncated Q and setting
an unavailable coefficient to zero manufactures a false unit. A full
nonlocal characteristic equation may of course be added at stage 0,
but then the calculation has accessed the full coefficient chart and
is not a consequence of the former stage-0 truncation.

### 4a. The later printed source does license total degree and a top target

This is a substantive strengthening for the present `M3=n-2` clients.
**Printed p169, Proposition 4.5** (`source-pages/p-30.png`; extraction
1596–1599) assumes `deg g=deg_y g=n>1` and `M_r=n-2`; it states that
the highest homogeneous forms of g and the characteristic T_i for
`i<r` are powers of one common homogeneous form, with at most two
distinct linear factors. Since g is monic in y and its total degree
equals its y-degree, the common form has y-degree equal to total
degree. Its every power does too. Therefore for r=3, the composed
T2 has total degree equal to its already proved actual y-degree,
namely 55 or 63. This is a consequence in the existing coordinates.
No generic shear or source gauge is newly invoked.

The stronger root assertion in its **printed p172 proof**
(`source-pages/p-33.png`; extraction 1721–1768) resolves the specialized
polynomial notation and also covers i=r. It defines delta as the
minimum order of every root of `g product_(i=1)^r T_i^psi`. The
`delta>-1` case referred to from the first paragraph of the p166
proof (`source-pages/p-27.png`) is already a one-point case, with
pure y powers on top; it makes no coordinate transformation. In the
present chart g has a direction y=x and hence a root of order -1,
so delta<=-1 directly. The p172 contradiction assumes delta<-1,
applies Prop4.2, and forces every leading root polynomial to be a
pure power of pi, contradicting the definition of the minimum
root order. Thus delta=-1 in these very coordinates.

For a polynomial with nonzero scalar y-leader and y-degree D, having
all roots of order at least -1 implies the coefficient of y^(D-j)
has t-order at least -j, hence x-degree at most j. This proves total
degree at most D; the monic y^D term gives equality. Consequently
all `T_i^psi` for `i<=3` have total degrees equal to their y-degrees
in these clients, including T3 of degree 145 or 227.

Section 4 initially writes the Jacobian scalar as 1. The root-order
and common-form argument remains valid with arbitrary `Jc in k^*`:
in Prop4.1 its right hand side is multiplied by Jc, which alters
neither valuation comparisons nor the assertions that displayed
scalars are nonzero. Thus this deduction does not spend a second
normalization parameter or set the chart's Jc to 1.

There is more necessary information than a total-degree upper bound.
The common-form conclusion and the already fixed F top imply

\[
(T2)_{55}=\lambda y^{15}(y-x)^{40}\quad(99,66),
\]
\[
(T2)_{63}=\lambda y^{14}(y-x)^{49}\quad(D=108),
\]

with lambda nonzero. These are the 5th and 7th powers of the
degree-11/9 two-point basic form. A family representative whose
degree is below m differs from the canonical representative by at
most a constant: the four other target differences have distinct
y-degrees 5k,4k,3k,2k, all above D2. Hence retaining the five-target
family does not obstruct this necessary top-target choice.

A strengthened emitter may therefore impose every total-degree
coefficient above D2 equal to zero, then subtract the **entire**
displayed homogeneous target at degree D2, and localize lambda.
The normalized coefficient equations are `H_r=0` for
`r<L-D2`; at r=143/153 the rows subtract respectively
`lambda*w^15*z^40` or `lambda*w^14*z^49`, where w=1+z. These
stronger rows have their own printed necessity; they are not inferred
from P2.2 alone and must not be conflated with the weaker emitter.

An exact algebraic consequence explains the shallow Jacobian bands.
For (*) the chain rule gives

\[
J(F,Q)=(3G^2+2aG+bF+d)J(F,G).
\]

The first factor has total degree 2m=4k, since its leading term is
3G^2 and the other terms have smaller degree. If total deg Q<=D2,
then `deg J(F,Q)<=n+D2-2`. Unless J is zero, degree additivity in
the polynomial domain yields

\[
\deg J(F,G)\le D2-k-2=20\text{ or }25.
\]

Thus all Jacobian bands preceding t-power 143 or 153 are already
consequences of the strengthened characteristic block. This explains
why a stage 0–8 rerun may show no new Jacobian restriction even after
the cone's zero-Jacobian locus has been excluded. It does not force
J to be constant and does not prove a chart unit.

## 5. Failure on the whole four-constant Delta family

Let h be monic of y-degree k, and let
`F=h^3+B*h+C`, `G=h^2+D*h+E` with B,C,D,E in k. Every constant target
polynomial Q(F,G) lies in k[h]. If it is nonconstant of h-degree l, its
y-degree is exactly kl; if constant, its degree is 0 (with zero handled
separately). Hence no target polynomial has actual y-degree 55 when
k=33, or 63 when k=36. This proves that the entire degree-attainment
locus misses Delta, and therefore misses every restricted Delta_T.

This conclusion does not require Delta_T to be nonempty. It is not a
claim that the unrestricted source chart is empty. It also does not
claim that every Jacobian-zero pair belongs to Delta.

There is a useful caution: `[y^55]Q` need not vanish on **raw** Delta
without the degree-upper rows. For example
`h=y^33+y^22`, `Q=G=h^2` has a y^55 coefficient of 2 while its degree is
66. The obstruction is exact attainment after all higher terms have
vanished, not absence of the intermediate monomial in every power.

The exact symbolic control is stronger for the family (*). Its h^5,
h^4,h^3,h^2 coefficients have successive unit target leaders. They give

\[
b=-3D,\quad a=2B-3E,
\]
\[
c=-BD+2C-D^3+3DE,
\]
\[
d=B^2+BD^2-4BE+3CD+3E^2.
\]

After these substitutions Q is a constant in h; the h^1 coefficient
cancels identically. The remaining constant is retained in
`source-audit-controls.json` and is absorbable in e_0. Thus the
upper-degree-only chart keeps Delta, while its attained-degree row
forces lambda=0 there and the localizer then gives -1. This is a unit
on Delta, not a unit in the whole chart.

## 6. Safe early algebraic reduction on unrestricted outer blocks

Let K=k(x). Suppose

\[
F=h^3+A h+B,\quad G=h^2+C h+D,
\]

where h is monic of y-degree k and each of A,B,C,D has y-degree less
than k. Let the five target coefficients in (*) be scalars. If
`deg_y Q<4k`, then necessarily

\[
C=-b/3,\qquad A=(3D+a)/2.\tag{**}
\]

This follows directly from degrees and does not need an additional
approximate-root theorem. If C has positive y-degree r<k, then in
`G^3-h^6` the term `3C h^5` has y-degree `5k+r`. The terms `C^2 h^4`
and `C^3 h^3` have strictly lower degree because r<k. Every D term,
every term of `F^2-h^6`, and every lower target term also has strictly
lower degree. This contradicts the upper bound. Thus C is in K; the
y^5k coefficient is `3C+b`, which makes C the stated scalar in k.

After this substitution, Q's h^4 coefficient is
`L4=3D-2A+a`; all remaining terms have y-degree strictly less than 4k.
Since `deg_y L4<k`, a nonzero L4 would give degree at least 4k.
Therefore L4=0. This proves (**).

These implications have coefficient-level certificates: eliminate
C's y-coefficients from the top down, with rational leader 3; then the
constant-y row sets `3C+b=0`, including all x-coefficients. Eliminate
the coefficients of `3D-2A+a` from the top down with leader -2 on A.
No branch is removed. Both clients have D_2<4k, so the reductions
apply. They must be attached to their high-y-degree rows, not promoted
as independent source gauges.

There is a further exact reduction (independently checked by symbolic
expansion). Write `B=A3`, `D=B2` after (**), and set

\[
\mathcal A=a+b^2/4,\quad H=h-b/6,\quad
v=D+a/3+b^2/18,
\]
\[
p=d+bc/2-\mathcal A^2/3,\qquad
q=e_0+c^2/4-\mathcal A(d+bc/2)/3+2\mathcal A^3/27,
\]
\[
V=B-bD/4+ab/12+b^3/54-c/2.
\]

Then `deg_y v,deg_y V<k` and identically

\[
Q=-2VH^3+(3v^2/4+p)H^2-3vVH+v^3-V^2+pv+q.\tag{***}
\]

Let the exact monic y-division be `3v^2/4+p=S H+R0`, with
`deg_y R0<k`. In (***) every term other than
`(S-2V)H^3` has degree strictly less than 3k. Hence the necessary
bound `deg_y Q<2k` forces `V=S/2`. This eliminates B by rational
coefficient graph equations, provided its entire original source
support/valuation row system is transported onto the resulting graph.

After this substitution, perform exact monic division of the **whole**
Q by H^2. Its quotient must be zero. The remainder has degree less
than 2k and must have its coefficients at heights `D2+1,...,2k-1`
zero, scalar leader at D2, and localized nonzero leader. These are
exactly the original degree-and-attainment conditions. At D=108 the
remainder has nine high heights 64,...,71; at (99,66) it has ten high
heights 56,...,65. Each height means all x-coefficients, not one scalar
unless a coefficient-field representation and map is explicitly used.

One must not replace the whole-Q quotient by `R0=0`: the terms
`v^3` and `-(3/2)vSH` can have degree at least 2k and cancel terms of
`R0 H^2`. All divisions here are monic polynomial division and rational
constants, so no unrecorded nonvanishing-leader branch is discarded.

The strengthened total-degree face also transports exactly through
one further division. Suppose the reduced identity is
`Q=E H+L`, where `deg_y L<k`. Monic y-division by H respects the
total-degree filtration because `deg H=deg_yH=k`: a cancellation
of a term x^i y^j subtracts `x^i y^(j-k)H`, of the same or smaller
total degree. Thus `deg Q<=D` implies `deg E<=D-k` and `deg L<=D`.
If Q's degree-D homogeneous target is `lambda*P0^5` or
`lambda*P0^7`, and H's degree-k part is `P0^3` or `P0^4`,
homogeneous monic division has quotient target `lambda*P0^2` or
`lambda*P0^3` and zero remainder. Therefore the exact equivalent
strengthened conditions are

\[
\deg E\le D-k,\quad E_{D-k}=\lambda P0^2\text{ or }\lambda P0^3,
\quad \deg L\le D-1,\quad \lambda\ne0.
\]

The converse follows by multiplying E by H. In particular, all
coefficients of L of **total** degree at least D must vanish; a cap
only on its y-degree is insufficient. This equivalence uses no
unproved absence of cancellation and no division by a variable.

## 7. Uniform scope

The exact attained-degree and scalar-unit equations are uniformly
available for every *effective* characteristic index of every realized
Keller datum to which Moh's setup applies. Two-point geometry is not
needed for this necessity theorem. It is a useful additional family of
necessary-chart instruments for the family-C leaves and for D=108,
provided each leaf supplies its actual characteristic data and an
audited coordinate map. The user and prior prose refer to 38 leaves;
the receipt-verified supplementary roster mechanically contains 36
leaves under 20 parents. See `gauge-and-roster-audit.md` and its
independent count control; no missing records are inferred.

For realized **two-point** charts there is the additional uniform
total-degree conclusion. Proposition 4.3 on printed p166 says that
if no characteristic index equals n-2, then g's top has only one
linear factor. The contrapositive, together with `M_i<=n-1` and
the exclusion of terminal n-1 from the effective list, shows
`M_s=n-2` for any realized two-point datum. The p172 root-order
proof therefore applies with r=s and yields actual total degrees
equal to actual y-degrees for every effective characteristic T_i.
For i<s their top forms are powers of the common two-point form;
the last T_s can have the additional factor described by Prop4.6,
so its entire top must not be copied from the earlier indices.

Uniform existence does not make them a uniformly bounded-depth family.
Neither Proposition 2.2 nor Proposition 3.1 bounds their coefficient
depth by a small universal number. Nor does failure on Delta prove a
finite-stage kill of any full leaf. A leaf-level claim requires its full
ideal, gauge ledger, all retained target terms, localization/ring
controls, and leading-target subtraction. If those computations do not
decide the full chart, the correct leaf status remains OPEN.
