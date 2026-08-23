# The level-42 x-side and the D43 corrected-operator specification

**Status:** implementation specification, not a D43 measurement. The
algebraic level-42 formulas below are exact. The advertised
\(184\times180\) shape is conditional on **CONJECTURE X-SIDE-30**. No
numerical value of the two level-42 x-factor coefficients is present in the
repository, and this specification does not assign one.

**Scope:** residue A, B-frozen, no-log, `PIN42`,
\(W_1W_2\ne0\), in the named modular charts at 105337 and 105673. The
specializations \(p=\eta^6-6\eta^3+6\) and the displayed \(S_M,G_M\)
below are scoped to this normalization. They are not asserted for another
chart or an unfrozen B-side.

**Controlling ruling:** `xmodel/sol-h29-dichotomy.md`. Its
band-\(\le40\) certificate proves only

\[
                         \ell(L_s^+)\ge 37
\]

at each named completed operator carrying the \(H_{29}u^0\) obstruction.
D23 and D25 used the same \(174\times170\) projection. The first new
\(H_{29}\) coordinate is

\[
              y_1=t^{42}e_{29}=H_{29}u^1,\qquad u=t^6,
\]

so D43, whose selected levels satisfy `level < 43`, is the first possible
second floor measurement. It is also the first band at which the normalized
x-side enters.

The words **FACT** and **EXACT DERIVATION** below denote repository facts or
formal coefficient identities. Every extrapolation not proved in the
repository is explicitly labelled **CONJECTURE**. A failed conjectural gate
enlarges or stops the computation; it is never implemented by zero-filling.

## 1. Corrected source and target coordinates

### 1.1 The banked 30 y-tail input streams

The current source module is

\[
 X_y=\bigoplus_{q=1}^{30}t^{r_q}k[[u]],\qquad u=t^6.
\]

The deterministic stream order and allowed residues are

| order | family | residues \(\rho\) |
|---:|---|---|
| 1--6 | `tf1` | \(0,1,2,3,4,5\) |
| 7--12 | `tf2` | \(0,1,2,3,4,5\) |
| 13--18 | `tg1` | \(0,1,2,3,4,5\) |
| 19--24 | `tg2` | \(0,1,2,3,4,5\) |
| 25--27 | `tg01` | \(0,2,4\) |
| 28--30 | `tg02` | \(0,2,4\) |

Their shifts are

\[
 r_\rho=6+\rho\quad(\rho\ne4),\qquad r_4=16,\qquad
 \sum_qr_q=288.                                             \tag{1.1}
\]

The missing would-be shift \(r=10\) is `PIN42`: it pins the root-series
coefficient of **absolute** level \(32+10=42\). It is not the normalized
x-factor correction at **operator** level 42.

A coordinate `(family,r)` has global source level \(r\), absolute root-tail
level \(32+r\), and belongs to the unique residue stream
\(\rho\equiv r\pmod6\). In stream coordinates its \(j\)-th coefficient has
level \(r_\rho+6j\).

### 1.2 The corrected 30 target streams

\[
 Y^+=\bigoplus_{a=0}^{29}t^{s_a}k[[u]]e_a,
\]

where

\[
 s_a=6+2((a+1)\bmod3)\quad(0\le a\le28),\qquad
 s_{28}=16,\qquad s_{29}=36,\qquad \sum_as_a=276.           \tag{1.2}
\]

The label `(H_a,j)` means the target \(t^{s_a+6j}e_a\). In particular,

\[
 (H_{29},0)=t^{36}e_{29},\qquad
 (H_{29},1)=t^{42}e_{29}.                                  \tag{1.3}
\]

**CONJECTURE CYCLIC-30.** These are all output streams at every depth.
Only the finite pure-y grading through band 41 is banked. At row 42 the
compiler must retain and audit every pristine eta component with \(a\ge30\).
The slot-aware degree bound used by the present construction is
\(\deg_\eta\Phi_y\le14\), \(\deg_\eta\Gamma_y\le20\) through \(t^{42}\),
so the possible surplus is eta 30--33; that bound itself must be established
before truncation. A new independent component enlarges the target; it may
not be discarded because it misses the 30-stream selector.

## 2. The x-side interface

### 2.1 Exact normalized factor streams

For a genuine polynomial pair, take the y-leading polynomials

\[
\begin{aligned}
 \phi_f(x)&=[y^{126}](f-a)
   =c_f x^{42}+c_{f,41}x^{41}+\cdots+c_{f,0},\\
 \phi_g(x)&=[y^{189}]g
   =c_g x^{63}+c_{g,62}x^{62}+\cdots+c_{g,0}.
\end{aligned}                                               \tag{2.1}
\]

The branch-product factorization in `SHEET6-DIRECTIONB.md` gives the exact
normalized, eta-independent factors

\[
\begin{aligned}
 U_f(t)&=\frac{\phi_f(t^{-42})}{c_ft^{-1764}}
       =1+\sum_{m=1}^{42}\alpha_m t^{42m},
       &\alpha_m&=\frac{c_{f,42-m}}{c_f},\\
 U_g(t)&=\frac{\phi_g(t^{-42})}{c_gt^{-2646}}
       =1+\sum_{m=1}^{63}\beta_m t^{42m},
       &\beta_m&=\frac{c_{g,63-m}}{c_g}.
\end{aligned}                                               \tag{2.2}
\]

Thus the finite x-factor input sequences are

\[
  (\alpha_1,\ldots,\alpha_{42}),\qquad
  (\beta_1,\ldots,\beta_{63}),                              \tag{2.3}
\]

with factor-coordinate levels \(42m\). If
\(\phi_f=c_f\prod_i(x-\xi_i)\) and
\(\phi_g=c_g\prod_j(x-\zeta_j)\), then
\(\alpha_1=-\sum_i\xi_i\) and \(\beta_1=-\sum_j\zeta_j\).

The D43 Euler/J window directly consumes only

\[
       \alpha:=\alpha_1,\qquad \beta:=\beta_1,\qquad
       U_f=1+\alpha t^{42}+O(t^{84}),\quad
       U_g=1+\beta t^{42}+O(t^{84}).                        \tag{2.4}
\]

These sequences are not six-step \(k[[u]]\) tail streams. They are finite
sparse factor coordinates supported at \(42m=7m\) powers of \(u\). Unless a
proved bridge expresses them in the 30 streams, an implementation should
represent their tangent directions as a sparse x-side column sidecar.

**CONJECTURE X-SIDE-DERIVATION.** The pending LR2/R2 x-side model derives
the values and tangent maps of (2.3), with all its h-Newton budget equations,
from legal polynomial/source data. LR2 proves the single-cluster geometry;
it does not supply these coefficients or their Jacobian. `SHEET6-R1.md`
section 16.5 explicitly records this model as future work.

### 2.2 Mandatory tangent classification

At a named completion, each consumed x coefficient must be classified as
exactly one of:

1. **held fixed:** its value is part of the completion and its differential
   is excluded from the declared Newton source for a proved reason;
2. **derived:** it is an explicit function of the 30 y-tail streams, and the
   exact chain-rule row \(D\alpha,D\beta\) is supplied;
3. **independent:** it is a genuine filtered tangent coordinate.

Cases 1 and 2 can preserve 180 columns. In case 3, D43 normally has two
additional level-42 columns and shape \(184\times182\). Row 42 sees only one
linear combination of them, but the other direction may engage later; it
cannot be quotiented away from a single-window kernel observation. A proved
source quotient which retains only that combination would instead give
\(184\times181\).

This classification is the load-bearing content of:

> **CONJECTURE X-SIDE-30.** The level-42 x-side contributes no independent
> source direction and no independent output stream outside the corrected
> 30-by-30 model, after proved bridge/gauge relations.

If the classification is absent, the certifier must stop before constructing
a loss matrix.

### 2.3 Causal structure

The normalized-factor convolution gives the following onset rules.

| datum | assigned factor level | first possible residual level | first effect on a y-tail differential of level \(r\) |
|---|---:|---:|---:|
| value \(\alpha_m\) or \(\beta_m\) | \(42m\) | \(42m\) | \(42m+r\) |
| independent \(D\alpha_m\) or \(D\beta_m\) | \(42m\) | \(42m\) | \(42m\) |
| product \(\alpha_i\beta_j\) | \(42(i+j)\) | \(42(i+j)\) | later by convolution |

Consequences for the band-42 window:

- only \(\alpha,\beta\) can affect the residual value;
- if \(\alpha,\beta\) are held fixed, their multiplication of a registered
  y-tail variation starts at \(42+6=48\), so it does not alter the
  30-tail derivative through row 42;
- if they are derived, \(D\alpha,D\beta\) add a chain-rule contribution at
  row 42 in the existing 30 columns;
- if they are independent, their new columns are zero below row 42;
- a nonzero derivative of \(\alpha\) or \(\beta\) with respect to a source
  coordinate whose declared level exceeds 42 would violate the current
  filtration and must fail the causality gate or force a corrected source
  filtration.

Higher fixed x coefficients contribute at later convolutions. “The first
x-side term is at 42” is not permission to omit the later coefficient
consumption manifest in a deeper compiler.

## 3. Exact row-42 formula

### 3.1 Full product identity

Put

\[
 \theta=t\frac{d}{dt},\qquad
 \Phi_{\rm full}=U_f\Phi_y,\qquad
 \Gamma_{\rm full}=U_g\Gamma_y,
\]

and define

\[
 \mathcal B(\Phi,\Gamma)
  =(\theta\Phi-12\Phi)\Gamma_\eta
   -\Phi_\eta(\theta\Gamma-18\Gamma).                       \tag{3.1}
\]

In the gauge used by `cases/valuation_e2.py`,

\[
 \mathcal E_{\rm full}
   =\mathcal B(\Phi_{\rm full},\Gamma_{\rm full})+42t^{20}.
\]

Because \(U_f,U_g\) are eta-independent, direct product differentiation
gives the **EXACT DERIVATION**

\[
\boxed{
\begin{aligned}
 \mathcal B_{\rm full}
  ={}&U_fU_g\mathcal B_y\\
    &+U_g(\theta U_f)\Phi_y\Gamma_{y,\eta}
     -U_f(\theta U_g)\Phi_{y,\eta}\Gamma_y .
\end{aligned}}                                             \tag{3.2}
\]

The inhomogeneous \(42t^{20}\) is added after (3.2); it is not multiplied by
\(U_fU_g\).

Write

\[
 \Phi_y=\sum_iF_i(\eta)t^i,\qquad
 \Gamma_y=\sum_iG_i(\eta)t^i.
\]

The banked lead identities are

\[
\begin{aligned}
 F_0(\eta)&=S_Mp(\eta)^2,&
 S_M&=\frac{7^{12}}{2^6},\\
 G_0(\eta)&=G_Mp(\eta)^3,&
 G_M&=-\frac{7^{18}}{2^9},\\
 p(\eta)&=(\eta^3-a_1)(\eta^3-a_2)
          =\eta^6-6\eta^3+6 .
\end{aligned}                                               \tag{3.3}
\]

Row 0 is identically zero:

\[
          -12F_0G_0'+18G_0F_0'=0.                          \tag{3.4}
\]

Extracting \(t^{42}\) from (3.2), using (3.4), gives

\[
\boxed{
 [t^{42}]\mathcal E_{\rm full}
 =[t^{42}]\mathcal E_y
 +42S_MG_M(3\alpha-2\beta)p^4p'.}                           \tag{3.5}
\]

Equivalently, before using Row 0, the two corrections are

\[
\begin{aligned}
 \alpha(30F_0G_0'+18G_0F_0'),\\
 \beta(-12F_0G_0'-24G_0F_0').
\end{aligned}                                               \tag{3.6}
\]

Equations (3.2)--(3.6) are exact coefficient algebra. The unproved part is
the legal value and tangent provenance of \(\alpha,\beta\), not the
product-rule calculation.

### 3.2 The requested \(H_{29}u^1\) scalar

Write the full bidegree coefficients as

\[
 F_{i,r}=[t^i\eta^r]\Phi_y=[\eta^r]F_i(\eta),\qquad
 G_{j,s}=[t^j\eta^s]\Gamma_y=[\eta^s]G_j(\eta).
\]

Eta differentiation shows that an eta-29 residual term has \(r+s=30\).
The **complete**, implementation-facing pure-y coefficient is therefore

\[
\boxed{
 h^{\,y}_{29,1}
 :=[t^{42}\eta^{29}]\mathcal E_y
 =\sum_{\substack{i+j=42\\r+s=30}}
   \bigl((i-12)s-(j-18)r\bigr)F_{i,r}G_{j,s}.}              \tag{3.7}
\]

Under the slot-42 eta bounds (5.1), only \(10\le r\le14\) and
\(s=30-r\) can occur. In particular, if

\[
 f_i=F_{i,12},\qquad g_i=G_{i,18},
\]

then

\[
 \sum_{i+j=42}(18i-12j)f_i g_j                             \tag{3.8}
\]

is only the \((r,s)=(12,18)\) summand of (3.7), not the whole
coefficient. Off-direction \((\eta t^{20})^m\) insertions make the other
degree pairs genuine; an implementation must use (3.7).

For the finite window, define

\[
 H_{29}u^j:=[t^{36+6j}\eta^{29}]\mathcal E,\qquad j=0,1.
\]

Writing \([\eta^{29}]\mathcal E=t^{36}H_{29}(u)\) as an all-depth series
additionally consumes **CONJECTURE CYCLIC-30**; formula (3.7) does not.

As \([\eta^{29}]p^4p'=6\), the complete answer is

\[
\boxed{
\begin{aligned}
 [u^1]H_{29}
  &=[t^{42}\eta^{29}]\mathcal E_{\rm full}\\
  &=h^{\,y}_{29,1}
    +252S_MG_M(3\alpha-2\beta)\\
  &=h^{\,y}_{29,1}
    -\frac{9\,7^{31}}{2^{13}}(3\alpha-2\beta).
\end{aligned}}                                             \tag{3.9}
\]

There is no honest numerical specialization of (3.9) in the current
repository because \(\alpha,\beta\) are not banked. Assigning them zero is
only a constructor/control assignment. It becomes a legal named completion
only if exact polynomial or LR2/R2 provenance proves that those zero values
belong to the scoped source scheme.

At a genuine D43 survivor, (3.9) must evaluate to zero as a residual row.
The loss test concerns the derivative row and the unit codomain target
\(t^{42}e_{29}\); it does not treat the residual value itself as the
obstruction.

In the existing held-lead tails tangent convention,

\[
 D([u^1]H_{29})
  =Dh^{\,y}_{29,1}
   +252S_MG_M(3D\alpha-2D\beta).                            \tag{3.10}
\]

If \(S_M,G_M,p\) are also allowed to vary, use the unsimplified full
product rule; (3.10) assumes, as the current 30-tail source does, that they
are held fixed.

### 3.3 Exact ten-row x vector

The polynomial \(p^4p'\) has the following nonzero coefficients:

| eta power \(a\) | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \([\eta^a]p^4p'\) | -23328 | 101088 | -186624 | 191808 | -120528 | 47952 | -12096 | 1872 | -162 | 6 |

Therefore the x correction to the **residual value** in all ten selected
row-42 outputs is

\[
       42S_MG_M(3\alpha-2\beta)\,p^4p'.
\]

Its derivative correction is
\(42S_MG_M(3D\alpha-2D\beta)p^4p'\). If \(\alpha,\beta\) are two
independent coordinates, their columns are respectively

\[
       126S_MG_M\,p^4p',\qquad -84S_MG_M\,p^4p'.            \tag{3.11}
\]

They are proportional in this window, with source-kernel direction
\((D\alpha,D\beta)=(2,3)\). Their \(H_{29}u^1\) entries are

\[
                   756S_MG_M,\qquad -504S_MG_M.            \tag{3.12}
\]

**CONJECTURE X-CUBE-RELATION.** If a pristine scoped identity
\(U_g^2=U_f^3\) is proved, then \(2\beta=3\alpha\) and the first x
correction cancels. A common translated cluster gives the same
cancellation. The repository's lead/tower identities and LR2 geometry do
not presently prove this coefficient identity on the required source
scheme. The implementation must not consume it without an exact polynomial
or two-sided reconstruction certificate, including its tangent consequence.

## 4. The band-42 matrix and the coefficient blocks

### 4.1 Canonical weighted registries

Under **CONJECTURE X-SIDE-30**, select

\[
\begin{aligned}
 \mathcal R_{42}
   &=\{(a,j):s_a+6j\le42\},\\
 \mathcal C_{42}
   &=\{(\mathrm{family},r):r\le42,\ r\text{ allowed for the family}\}.
\end{aligned}                                               \tag{4.1}
\]

The old counts were 174 rows and 170 columns. The ten new rows, all of
global level 42, are

~~~text
(H2,6), (H5,6), (H8,6), (H11,6), (H14,6),
(H17,6), (H20,6), (H23,6), (H26,6), (H29,1).
~~~

The ten new columns are

~~~text
(tf1,41), (tf1,42),
(tf2,41), (tf2,42),
(tg1,41), (tg1,42),
(tg2,41), (tg2,42),
(tg01,42), (tg02,42).
~~~

The four \(r=41\) columns are the \(u^5\) coordinates of the residue-5
ordinary streams and have absolute tail level 73. The six \(r=42\)
columns are the \(u^6\) coordinates of the residue-0 streams and have
absolute level 74. Hence

\[
                       M_{43}\in k^{184\times180}.           \tag{4.2}
\]

Equation (4.2) is conditional. Independent \(\alpha,\beta\) give
\(184\times182\); a proved one-coordinate x quotient gives
\(184\times181\); any surplus output adds rows.

For artifact stability, define the canonical serialized order to be:

1. the exact old ordered row registry, followed by the ten new rows in the
   order printed above;
2. the exact old ordered `GIDX` column registry, followed by the ten new
   columns in the order printed above;
3. any proved independent x-side columns after those, ordered by
   `(factor, m)`.

The current a-major/family-major comprehensions would insert new labels
inside the old lists. An internal implementation may use that order, but it
must project and reorder by stable labels before hashing. A naïve top-left
slice is not an acceptable legacy gate unless the append-only serialization
above has first been enforced.

### 4.2 Do not conflate three matrices

The following are different objects:

1. \(L_s^+\), conditionally a formal 30-output by 30-input
   \(k[[u]]\langle\Theta\rangle\) operator;
2. \(M^+(N)\), its square first-\(N\)-coefficients truncation of shape
   \(30N\times30N\);
3. \(M_{43}\), the weighted all-coordinate window (4.2), whose shape is
   \(184\times180\).

A square first-\(N\)-coefficient slice earns the name \(M^+(N)\) only after
**normalized-prefix causality** is checked:

\[
 D_{(q,i)}H_{a,j}=0
 \quad\text{for every }i\ge N,\ 0\le j<N,\ a,q.             \tag{P_N}
\]

This includes every chain-rule contribution through
\(D\alpha,D\beta\). Global-level causality alone does not imply
\((P_N)\): a later coefficient of a low-shift input stream can still have
global level below an early coefficient of a high-shift output stream.

Subject to \((P_1)\), the candidate leading slice is

\[
 M^+(1)\in k^{30\times30},
\]

with rows \((a,0)\) and columns \((q,0)\). The x factor starts too late to
alter it directly, although a different pure-y completion can change its
entries.

After the finite x-side/source census and \((P_2)\) pass, D43 makes the
formerly withheld second block computable:

\[
 M^+(2)\in k^{60\times60},                                  \tag{4.3}
\]

with

\[
\begin{aligned}
 \text{rows}&=\{(a,j):0\le a<30,\ j=0,1\},\\
 \text{columns}&=\{(q,i):1\le q\le30,\ i=0,1\},\\
 M^+(2)_{(a,j),(q,i)}
   &=D_{(q,i)}H_{a,j}.
\end{aligned}                                               \tag{4.4}
\]

In the current coordinate registry the column `(q,i)` is
`(family,r_q+6i)`. Record

\[
                 \delta^+(2)=60-\operatorname{rank}M^+(2). \tag{4.5}
\]

If \((P_2)\) fails—specifically, if \(D\alpha\) or \(D\beta\) has support
on any \((q,i\ge2)\) which hits an output \((a,j<2)\)—the displayed
\(60\times60\) array is only a submatrix and \(\delta^+(2)\) remains null.

Neither \(N=1,2\) nor equality of their defects proves stabilization,
\(d^+\), an Ore section, or a finite \(e^+\). \(M^+(3)\) contains
\(H_{29}u^2\) at level 48 and is outside D43.

If independent x directions exist, (4.3) remains a named 30-stream
subblock, not the full operator. Do not apply the square index formula to
the enlarged rectangular source.

## 5. Builder contract

### 5.1 Required parameterization

The existing constants are insufficient:

~~~text
current:  DBUILD = 42  -> slots 0..41
          RMAX  = 40
          GD    = 170

D43:      DBUILD = 43  -> slots 0..42
          RMAX  = 42
          nominal GD = 180, conditional on X-SIDE-30
          ETA_DIM = 34 only after the slot-aware eta bound is certified
          minimum pure-y source cap = 75 (absolute levels < 75)
          actual cap = maximum named by the x-side consumption manifest
~~~

Build a configured engine instance; do not mutate module constants after
import. Recompute every dependent array, Toeplitz/jet dimension, `GIDX`,
row registry, and hash header from the configuration. The character table
`Z=[z^m]` remains length 42 because it represents \(C_{42}\), not the jet
truncation length.

The row-42 build must establish, independently of an already truncated
array,

\[
 \deg_\eta\Phi_y|_{t^{\le42}}\le14,\qquad
 \deg_\eta\Gamma_y|_{t^{\le42}}\le20,\qquad
 \deg_\eta\mathcal E|_{t^{\le42}}\le33.                    \tag{5.1}
\]

A support-bound traversal of the product DAG is sufficient. A brute
global-degree build through eta 314 is also sufficient, but then the
`float64` accumulation bound used by the old 34-slot engine must be
reproved or replaced by exact modular accumulation. Merely setting
`HMAX = 34` and observing no stored eta-34 coefficient is circular.

`orbit_levels()` currently uses `vals.get(r, 0)`. In D43 mode that behavior
is forbidden. Every consumed coefficient must appear in a completeness
manifest as:

- a represented D25/D43 coordinate with exact value;
- a newly solved completion coordinate;
- a deliberate, named finite-support completion value; or
- a proved irrelevant coordinate outside the consumption range.

Absence from the builder is not the value zero.

### 5.2 Full-product construction and differentiation

The production path must:

1. build the pure-y \(\Phi_y,\Gamma_y\) through slot 42;
2. obtain \(U_f,U_g\) and their tangent data from the x-side manifest;
3. form \(U_f\Phi_y,U_g\Gamma_y\) before calling the Euler-row constructor;
4. add \(42t^{20}\) exactly once;
5. differentiate the full products in the declared source coordinates.

An independent path must implement (3.2) directly and agree
coefficient-for-coefficient with the full dual-number or
automatic-differentiation path. Both the value array and every gradient
column must agree.

The x-side manifest must contain at least:

~~~text
provenance kind and source artifact hashes
phi_f / phi_g degree and leading-coefficient checks, or an exact LR2/R2 derivation
alpha, beta and every other factor coefficient consumed
tangent class: fixed | derived | independent
Dalpha, Dbeta in stable source labels when derived
factor-coordinate filtration levels
all R2/h-Newton budget equations and replay status, when used
coefficient-consumption maximum and proof that later data cannot enter
~~~

If a full polynomial pair is available, extract (2.1) independently from
the polynomial coefficients and from the root/branch product, and require
exact equality. If only a formal LR2 construction is available, this
two-sided reconstruction is part of **CONJECTURE X-SIDE-DERIVATION** until
proved.

### 5.3 Three separately named run modes

1. **`LEGACY_BAND40_REGRESSION`.** Use each named old completion and require
   the exact projection replay in section 8.
2. **`D25_COMPLETION_BAND42`.** Keep one named D25 completion, supply its
   legal x-side, and extend only the derivative window. This is an operator
   smoke test. It need not satisfy pristine Rows 26--42 and is not a D43
   survivor or a depth measurement.
3. **`D43_SURVIVOR`.** Consume a compatible D43 residual certificate,
   including all y- and x-side data, and differentiate at that same point.
   Only this mode is the genuine D43 floor measurement.

The output artifact must record the mode. Results from mode 2 may never be
reported under mode 3 language.

The commissioned pilot for mode 3 is fixed:

~~~text
first prime       105337
fiber             a00pp
cell              one named fourth-root D25 cell
base presentation promoted D25 A^14 presentation
second replay     105673
~~~

Its artifact must contain an exact map \(s_{43}\to s_{25}\), exact equality
on every coordinate represented by the named D25 cell, and a separate list
of newly adjoined completion coordinates. A failure to prolong that one cell
is not family-wide emptiness.

## 6. D43 jets versus the D25 jets bank

### 6.1 Frontier levels

The D25 pristine Row-24 generator stops at absolute tail level 56. Its
frontier uses the four ordinary families at level 51 and all six families at
level 56. Its full-live symbolic registry reaches the dormant ordinary
levels 53 and 55, but the named old e-plus evaluator does not solve or store
their values: its zero-completion rule and `vals.get(r,0)` supply zero.
They are therefore banked coordinate slots/labels, not banked nonzero
completion values or retained coordinates of the reduced D25 cell.

For even \(12\le k<42\), `xmodel/sol-algkill.md` proves the pure-y
first-occurrence rule

\[
\begin{aligned}
 O_k&=\{\mathrm{tf1,tf2,tg1,tg2}\}_{k+27},\\
 E_k&=\{\mathrm{tf1,tf2,tg1,tg2,tg01,tg02}\}_{k+32}.
\end{aligned}                                               \tag{6.1}
\]

The D43 extension appends pristine row blocks

\[
                    k=26,28,30,32,34,36,38,40,42.
\]

Its provisional frontier is:

| pristine row \(k\) | four ordinary tails \(k+27\) | all six tails \(k+32\) | status |
|---:|---:|---:|---|
| 26 | 53 | 58 | proved occurrence law |
| 28 | 55 | 60 | proved occurrence law |
| 30 | 57 | 62 | proved occurrence law |
| 32 | 59 | 64 | proved occurrence law |
| 34 | 61 | 66 | proved occurrence law |
| 36 | 63 | 68 | proved occurrence law |
| 38 | 65 | 70 | proved occurrence law |
| 40 | 67 | 72 | proved occurrence law |
| 42 | 69 | 74 | **CONJECTURE POST41-FIRST-OCCURRENCE** |

The Row-42 extrapolation crosses the first x-side band and must be replaced
by a direct occurrence census. The table is an acceptance expectation, not
permission to prune an unexpected coordinate.

### 6.2 Exact count reconciliation

The nine displayed frontiers contain \(9(4+6)=90\) coordinates.

- Eight ordinary coordinates, four at level 53 and four at level 55, are
  already inside the D25 jets bank, although a reduced D25 cell may have
  frozen or pruned them.
- The other 82 frontier coordinates require new level coverage.
- A complete raw tail-bank extension from cap 56 through cap 74 adds 90
  symbols:
  - four ordinary families at every absolute level 57--74:
    \(4\cdot18=72\);
  - `tg01,tg02` at even levels 58,60,...,74:
    \(2\cdot9=18\).
- Of those 90 newly banked symbols, the eight ordinary coefficients at
  levels 71 and 73 are not frontier variables for Rows \(\le42\) under
  (6.1), but belong to the complete source/completion registry.

The D25 notes call the full-live D25 generator a 103-live-variable build.
If that complete registry is retained unchanged and the 90 raw tail slots
above are appended, the corresponding raw count is 193 before any
independent x variables. This arithmetic is registry bookkeeping, not a
claim that 103 solved D25 completion values were banked.

This is not the parked-system variable count: the reduced 28-variable D25
presentation did not retain levels 53/55 as free cell coordinates, so
adjoining all 90 provisional frontier variables gives the ruling's conditional
\(28+90=118\) variables. The 89 provisional new scalar equations give
\(34+89=123\) rows: Row 30 has nine selected eta components, while each of
the other eight appended rungs has ten. Those 118/123 counts remain
conditional on
**CONJECTURE POST41-FIRST-OCCURRENCE**, **CONJECTURE X-SIDE-30**, and the
surplus bridge.

The derivative window adds only ten source columns relative to band 40:
the absolute-level 73/74 coordinates listed in section 4. The nonlinear
residual compiler nevertheless needs the complete values through level 74,
plus every further datum required to derive the x-side factors.

### 6.3 D43 point input requirements

A `D43_SURVIVOR` certificate must provide:

- the pilot identifiers and exact \(s_{43}\to s_{25}\) map required in
  section 5.3;
- exact values for ordinary `tf1,tf2,tg1,tg2` coefficients through absolute
  level 74, except the separately recorded `PIN42`;
- exact values for even `tg01,tg02` coefficients through level 74;
- a reconstruction of the formerly dormant D25 levels 53 and 55 rather than
  an inherited implicit zero;
- \(\alpha,\beta\), their provenance, and their tangent classification;
- every extra coefficient named by the x-side consumption manifest;
- exact zero replay of all selected pristine rows through 42 and every
  retained surplus/R2/chart/pin row.

The inherited deep-label identification must be replayed exactly before
prolongation:

~~~text
tf1_49 <-> tg1_49
tf2_49 <-> tg2_49
tf1_54 <-> tg02_54
tf2_54 <-> tg01_54
tg1_54 <-> tg2_54
~~~

The certificate must store both emission labels and true stream labels, plus
the 86-row banked cross-match which fixes this involution. A D43 builder may
not regress to the obsolete emitted names.

Odd pristine rows through 41 may use the proved pure-y grading. D43 includes
no odd row beyond the x-side boundary. Eta-30--33 row-42 vanishing and the
ten-variable Row-42 frontier are finite gates, not consequences of the
pre-42 proof.

## 7. Certified loss on the enlarged window

Let \(M\) be the **full legal** band-42 matrix: \(184\times180\) only in the
30-stream cases, or the corresponding larger matrix when x directions are
independent. Let \(b_i\) be the global level of row \(i\), \(c_j\) the
global level of column \(j\), and

\[
                    C_n=\{j:c_j\ge n\}.                     \tag{7.1}
\]

For every integer \(0\le n\le42\) and every unit target \(e_i\) with
\(b_i\ge n\), test whether

\[
                    e_i\in\operatorname{im}M[:,C_n].        \tag{7.2}
\]

An uncovered target certifies

\[
                         \ell(L_s^+)\ge b_i-n+1.
\]

The finite-window lower bound is therefore

\[
\boxed{
\underline\ell_{42}
 =\max\left(
 0,\ 
 \max_{\substack{0\le n\le42\\b_i\ge n\\
 e_i\notin\operatorname{im}M[:,C_n]}}
 (b_i-n+1)\right).}                                        \tag{7.3}
\]

Run a literal brute-force scan over all \(n=0,\ldots,42\). An optimized
constant-column-set interval scan may also run, but its answer and maximizing
records must equal the brute-force result. The profile schema must record
both the minimum included column level and the number of eligible columns;
the old schema's second field stores a threshold, not a column count.

For every maximizing pair \((n,i)\), emit an exact sparse dual certificate

\[
       \lambda^TM[:,C_n]=0,\qquad \lambda^Te_i=\lambda_i=1. \tag{7.4}
\]

Store stable row labels in \(\lambda\), not numeric positions alone. Verify
(7.4) independently after deserialization.

Required interpretations are:

- if \(H_{29}u^1\) is uncovered at \(n=0\), then
  \(\underline\ell_{42}\ge43\);
- if it is covered but another level-42 unit target is uncovered at \(n=0\),
  the same floor follows by a different mechanism;
- if no new target raises the maximum and the recomputed
  \(H_{29}u^0\) target remains uncovered, only \(\ell\ge37\) is proved;
  this is not \(\ell=37\);
- an empty D43 survivor chart is a finite-depth scheme result, not a loss
  result.

At D43 the Newton threshold is \(\lfloor(43-1)/2\rfloor=21\). The scan
still proves only lower bounds; it constructs no causal right section and no
finite \(e^+\). The artifact must therefore retain

~~~text
e_plus_certified = null
d_plus_stabilized = null
e_plus_idx = null
~~~

unless separate all-depth section and stabilization certificates actually
discharge the corresponding gates.

Columns above level 42 may be omitted from (7.2) only after source
completeness and causality prove that they project to zero. If
\(\alpha,\beta\) are independent, their level-42 columns must be included;
scanning the 180-column submatrix would be invalid.

## 8. Mandatory band-\(\le40\) regression

The extension is accepted only if it reproduces the old object as a
label-selected restriction at the **same named old completion**.

For every banked D23/D25 fixture:

1. build the extended value and derivative arrays without changing the old
   completion values;
2. select rows of level \(\le40\) and old columns of level \(\le40\);
3. reorder them to the exact old row and `GIDX` registries;
4. reconstruct legacy-shaped arrays
   `V[0:34,0:42]` and `G[0:34,0:42,0:170]`, serialize them with the
   legacy `operator_hash()` routine, and require equality to the per-point
   hash stored in the JSON fixture;
5. independently run the legacy builder, construct its \(174\times170\)
   weighted matrix, and require entrywise/byte equality to the
   label-projected extended matrix; then bank a dedicated matrix digest
   because the old JSON does not contain the literal matrix;
6. rerun and reproduce the old grading, causality, bridge, \(M^+(1)\),
   residual, loss, and known pass/fail maps.

The extended array hash itself cannot equal the old hash: it has 43 t slots
and 180 or more gradient columns. Only the explicitly reconstructed
legacy-shaped arrays are passed to the legacy serializer.

The expected D23 distributions are:

| quantity | required result |
|---|---|
| points | 36 |
| window rank | 117 at 27 points; 115 at 9 |
| \(\delta^+(1)\) | 25 at 27; 26 at 9 |
| \(\underline\ell_{40}\) | 37 at all 36 |
| residual first window level | 24 at all 36 |
| formal germs certified | 0 |

The expected D25 distributions are:

| quantity | required result |
|---|---|
| accepted sampled completions | 360 |
| window rank | 115 at all 360 |
| \(\delta^+(1)\) | 26 at all 360 |
| \(\underline\ell_{40}\) | 37 at all 360 |
| residual first window level | 26 at 288; 30 at 72 |
| `c4_support_starts_exact` | pass at 288 interior points; known fail at 72 all-cell-zero witnesses |
| formal germs certified | 0 |

Baseline artifact hashes are:

~~~text
cases/d23_eplus.json
  71e0b6b0314cda79a12ba6887957339f429ba17d96cb159b9e8059015645d2f6
cases/d25_eplus.json
  891fb93761b33cc2236283806f1d83b10b3640a47f85887be4ec9f8bea1bc6c4
~~~

Also reproduce:

- the Row-24 90-entry symbol digest
  `ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29`;
- its eta support \(2,5,\ldots,26\) and rank-four Schur block;
- the banked emitted D25 shapes/hashes and every pristine D25 row;
- the \(H_{29}u^0\) characteristic-zero check

\[
 \frac{\partial [t^{36}\eta^{29}]\mathcal E}
      {\partial\,\mathrm{tf1}_{48}}
 =-\frac{147880611647231905314470776689}{1024}.
\]

The legacy-shaped hash equality and the independently rebuilt matrix
equality belong to `LEGACY_BAND40_REGRESSION`. A genuine D43 prolongation
may assign formerly unspecified completion data at levels 53/55 and above,
which can change derivative entries even below band 42. At that actual
point, recompute \(H_{29}u^0\) nonmembership and emit a fresh dual witness;
do not compare it to an unrelated zero completion.

## 9. Acceptance gates for `cases/eplus_certify.py`

The extension must fail closed unless every applicable gate below passes.

1. **PREFIX-REPLAY.** Before any extension, reproduce the Row-24/D25
   prefix and all results in section 8.
2. **SOURCE-CENSUS-42.** List every y- and x-side value consumed, its
   provenance, tangent class, stable label, and filtration level. Prove 180
   columns or enlarge the matrix.
3. **OUTPUT-CENSUS-42.** Prove the slot-aware eta bounds (5.1), then
   extract and audit every row-42 eta coefficient, especially all
   \(a\ge30\). Prove the ten selected outputs are complete modulo an
   explicit two-sided surplus bridge, or enlarge the target.
4. **XSIDE-ONSET.** Verify \(U_f-1,U_g-1\) vanish through level 41.
   A synthetic constructor-level perturbation of \(\alpha\) or \(\beta\)
   must change no lower row; it is a legal source perturbation only when
   the tangent classification permits it.
5. **XSIDE-PROVENANCE.** Verify (2.1)--(2.4) from a polynomial pair or
   discharge **CONJECTURE X-SIDE-DERIVATION** with exact LR2/R2
   reconstruction and budget-row replay.
6. **ROW42-IDENTITY.** Compare the direct full-product row with (3.5) at
   every eta coefficient. Check the exact vector in section 3.3 and the
   scalar formula (3.9).
7. **TWO-PATH-DIFFERENTIAL.** Compare the full dual/AD derivative with the
   independently grouped product-rule derivative (3.2), including
   \(D\alpha,D\beta\).
8. **NEGATIVE-XSIDE-CONTROLS.** Always check the synthetic factor response
   vector by perturbing \(\alpha,\beta\) separately at constructor level.
   If they are independent source coordinates, check the two legal columns
   (3.11), the H29 entries (3.12), their 3:-2 ratio, and zero effect below
   42. If derived, check the chain-rule contribution in the existing
   columns. If held fixed, assert that no \(\alpha,\beta\) source columns
   exist.
9. **D43-RESIDUAL.** In `D43_SURVIVOR` mode, every one of the 184 selected
   pristine coefficients and every retained surplus, chart, pin, and R2 row
   must evaluate to zero at the same completion used for differentiation.
   Verify the pilot identifiers, \(s_{43}\to s_{25}\) map, newly adjoined
   completion list, and inherited DEEPMAP replay.
10. **CAUSALITY-42.** Every nonzero matrix entry must have
    `row_level >= column_level`; this is measured, not imposed by blanking
    entries.
11. **ORE/GRADING-42.** Rerun the congruence, support-start,
    odd-row, eta-surplus, and affine-in-stream-index audits through the new
    band. The affine Ore audit applies to the 30 \(u\)-streams, not to
    independent finite sparse x columns. Congruence and absence of support
    below the declared \(s_a\) are hard. Equality of the first nonzero
    derivative level to \(s_a\) is a generic/structural diagnostic, not a
    universal pointwise gate: legitimate specialized points can have a
    delayed start, as the 72 D25 zero-cell fixtures do. The pre-42 proofs do
    not certify row 42.
12. **REGISTRY/HASH.** Hash the ordered row registry, ordered column
    registry, completion manifest, value array, full matrix, and
    band-\(\le40\) restriction separately.
13. **PREFIX-CAUSALITY/M2.** Check \((P_1)\) and \((P_2)\) against every
    registered column, including derived-x chain rules. Only if \((P_2)\)
    passes may the \(60\times60\) 30-stream slice (4.3) be called
    \(M^+(2)\) and assigned \(\delta^+(2)\). Otherwise label it a submatrix
    and leave \(\delta^+(2)\) null. Make no stabilization claim; if the full
    source is larger, also label it as a 30-stream subblock.
14. **Y0-RECHECK.** At the actual D43 completion, recompute and certify the
    old \(H_{29}u^0\) nonmembership.
15. **LOSS-BRUTE/FAST.** Require agreement of the literal and optimized
    scans in section 7, including \(n=0\), maximizing target labels, and
    exact dual witnesses.
16. **CROSS-PRIME.** Run first at 105337 and replay at 105673 with
    identical registries, symbolic incidence/character patterns, and
    verdict semantics. Equality of evaluated nonzero support is diagnostic
    only unless a common-lift theorem rules out prime-specific modular
    cancellation.
17. **GENERAL NEGATIVE CONTROLS.** Perturb a source point coordinate with a
    recorded incidence, a matrix entry hit by a stored dual witness, one
    registry label/order entry, and one deliberately omitted manifest
    coefficient. The corresponding replay, hash, causality, or witness
    gate must fail.
18. **FAIL-CLOSED-FIELDS.** Unless separate all-depth certificates are
    supplied, require `e_plus_certified`, `d_plus_stabilized`, and
    `e_plus_idx` to remain null.

## 10. Conjecture and stop ledger

The following statements are not proved by this specification:

- **CONJECTURE CYCLIC-30:** no additional all-depth output stream;
- **CONJECTURE BRIDGE-30:** universal two-sided pristine/emitted bridge;
- **CONJECTURE FILTER-30:** the full source-dependent normalization is
  filtered and has no hidden negative shift;
- **CONJECTURE PARAM-30:** an all-depth causal right section exists with a
  finite stated loss;
- **CONJECTURE X-SIDE-DERIVATION:** legal LR2/R2 data determine all consumed
  x-factor values and tangent maps;
- **CONJECTURE X-SIDE-30:** those data add no independent source/output to
  the 30-by-30 corrected operator;
- **CONJECTURE POST41-FIRST-OCCURRENCE:** the ten-variable frontier law
  survives Row 42;
- **CONJECTURE POST41-GRADING:** the finite grading/surplus pattern survives
  the first x-side row;
- **CONJECTURE X-CUBE-RELATION:** \(U_g^2=U_f^3\) at the required pristine
  source tier.

A finite D43 matrix can still certify a pointwise lower bound without proving
the all-depth conjectures, provided its finite source/output census,
completion, full formula, and causality are exact. It cannot certify a
30-by-30 index or section if **CONJECTURE X-SIDE-30** fails.

The implementation must stop and rederive its source/target model upon any of:

- an unclassified \(\alpha,\beta\) tangent;
- a nonzero independent eta-surplus row;
- a source coordinate absent from the consumption manifest;
- a causality violation;
- a normalized-prefix-causality failure followed by any claim of
  \(M^+(N)\) or \(\delta^+(N)\);
- a mismatch in the band-\(\le40\) named-completion regression;
- failure of the direct/dual row-42 identity;
- an unexpected Row-42 first occurrence.

## 11. Primary repository anchors

- `xmodel/sol-h29-dichotomy.md`, especially sections 2--4.
- `xmodel/sol-newton-lemma.md`, equations (1.0)--(1.11), (2.1), and
  sections 5 and 8.
- `SHEET6-DIRECTIONB.md`, section 0 and sections 8.S7--8.S9.
- `SHEET6-DIRECTIONB-REVIEW.md`, section 1.
- `SHEET6-R1.md`, section 16.5.
- `SHEET6-LROOT.md`, Lemma LR2.
- `xmodel/sol-algkill.md`, section 3.
- `xmodel/sol-round6.md`, sections 1--2.
- `cases/valuation_e2.py`, source registry, `build_jets`, `euler_rows`, and
  structure gates.
- `cases/eplus_certify.py`, `window_object` and `delayed_loss_scan`.
- `cases/d25_eplus.py`, the D25 completion/replay wrapper.
- `cases/d23_eplus.json` and `cases/d25_eplus.json`, the legacy result
  fixtures.
