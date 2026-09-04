# K16 split-tail coefficients and nonvanishing on the Eagon--Northcott curve

Date: 2026-09-04  
Lane: `k16-brcr-closedform-sol56-20260903`  
Status: PARTIAL -- finite layer/generating representation derived; uniform nonvanishing remains open

## 0. Verdict

```text
DERIVED       An exact two-layer triangular recursion for every a_r,b_r,c_r
              (hence B_r,C_r), uniform in (t,r), with a finite path sum for
              its tangent layer; equivalently an explicit generating function
              in r.  It uses only the charged arrays and proved scalar pivots.

CORRECTION    Lowering the b3-degree by one raises residual weight by t+1, not
              by one spine band.  Thus the charged depth argument does NOT put
              b_r and c_r one and two further O(r) spine steps after a_r.  The
              general recursion reaches the complete tangent/constant spine
              through b2; no weight argument licenses truncating it.  The
              available honest closed form is therefore a t-indexed triangular
              recursion/path sum, not a rational function of (t,r) alone.

EXACT CAS     The t=3,4,5,6 top rows and all a_r,b_r,c_r,B_r,C_r were generated
              over A_t in characteristic zero.  Clean explicit polynomial
              files are supplied in box/k16brcr-20260903/.  Every requested
              coefficient has full allowed support; all pure-b4 leader
              scalars at these indices have nonzero quadratic norm.

GAMMA         The proposed global substitution beta=-C_1/B_1 is invalid off
              D(B_1).  Exactly at t=3 the q_(2,0)-axis is a rank-one component
              of Gamma on which B_1=C_1=W_1=0, while Q_3 at the lift is a unit
              scalar times q_(2,0)^4 and is nonzero.  This is a denominator-zero
              of the W_1 chart, not a (V0)-failure.  One must use all charts
              D(B_r), equivalently all W_r.

OPEN          No point with Q_t=0 on Gamma was found for t>=3.  Nonvanishing is
              charged exact/promoted through t=6, but the all-t statement is
              not proved by the layer formula.  The combined two-clause target is
                sqrt(I_2(N)+(W_1,...,W_(t-1))) = m
              factorwise; for the Q-only clause, saturate away the rank-zero
              ideal.  If clause (i) is supplied, the two tests are equivalent.
              It is never “W_1 is a unit” or “gcd(W_r) is a unit.”

CONTROL       At t=2 the same formulas give the y=1/5 b3-axis failure and the
              y=2/5 zero-dimensional/nonvanishing fibre exactly.

FINAL STATUS  OPEN[K16-Q-NONVANISHING-ON-GAMMA] is NOT RESOLVED.
              Verdict: PARTIAL, with the coefficient generating form derived
              and the exact residual/global-chart correction recorded below.
```

### 0.1 Scope, conventions, and frozen-input verification

This report reconstructs the split tail from the indexed coefficient formula
\(T_{t,k}=-[w^{4t+1-k}]\sigma_t(\Delta)\), derives the \(b_3\)-quadratic,
linear, and constant coefficients, and tests the resulting eliminants on the
Eagon--Northcott rank-one curve. No ledger files are edited.

The manifest was generated mechanically from
`xmodel/k16-brcr-closedform-sol56-20260903.run.v2`. All 13 frozen inputs passed
`sha256sum -c` before this skeleton was created.

The check printed `OK` for, in receipt order, all six charged reports,
`FALLACY-v2.md`, and all six charged Python drivers.  The manifest was not
copied from the prompt.  All computations below use those frozen copies as the
source; the new files are confined to `box/k16brcr-20260903/` and this report.

## 1. Imported specification and notation

### 1.1 Ring, normalization, and indexed tail formula

Put

\[
 q=2t+1,\qquad e=3t+1,
\]
\[
 H_t(y)=12q^2y^2-12q(t+1)y+(t+1)(3t+2),
 \qquad A_t=\mathbf Q[y]/(H_t).
\]

It is more economical to use

\[
 d=2qy-(t+1),\qquad 3d^2=t+1,
 \qquad
 g=\frac{et\{3d+2(t+1)\}}{6q^3}.
\]

The coefficient ring and its residual polynomial extension are

\[
 P_t=A_t[b_4,q_{2,0},\ldots,q_{t-1,0}],\qquad
 S_t=P_t[b_3],
\]

with weights \(1,2,\ldots,t-1,t+1\).  Every split-index calculation is to be
read factorwise in \(A_t\); a nonzero class in a product algebra need not be a
unit.

There are three potentially colliding notations in the sources.  In this
report \(\mathcal C_m=[L^m]C(L+b_4)\) denotes a translated coefficient array,
\(\mathcal B_m\) denotes the auxiliary integrated array called `B_m` in the
charged Sol report, and \(z_j\) denotes a high-spine unknown.  None of these is
the split-tail coefficient \(B_r\).  Likewise the auxiliary Laurent
coefficients called \(T_j\) in the w-picture are not terminal rows
\(T_{t,k}\).

The sign is fixed as follows.  The compact source uses \(R=-E_t\); hence, with
\(L=X-b_4\),

\[
 T_{t,k}=-[X^k]R
 =-\sum_{m\geq k}{m\choose k}(-b_4)^{m-k}R_m.
 \tag{1.1}
\]

Equivalently, after the complete high-spine substitution,

\[
 T_{t,k}=-[w^{4t+1-k}]\sigma_t(\Delta)+yg\,[k=0].
 \tag{1.2}
\]

For \(k_r=2t-1-r\), \(0\leq r<t\), the reciprocal exponent is
\(\nu_r=4t+1-k_r=2t+2+r\), and the constant correction in (1.2) is absent.
The source of (1.1)--(1.2), including the sign map, is the frozen
`k16-terminal-proof-sol56-20260903.md`, lines 58--66 and 214--226, and
`k16-terminal-proof-fable5-20260903.md`, lines 94--114.

### 1.2 TAIL-SPLIT, FITT, EN-CURVE, and LENGTH-SPLIT obligations

The charged TAIL-SPLIT statement is

\[
 T_{t,k_r}=a_rb_3^2+b_rb_3+c_r,
 \quad \operatorname{wt}(a_r,b_r,c_r)=(r,t+1+r,2t+2+r),                 \tag{1.3}
\]
\[
 a_0=-\alpha_t\in A_t^\times\quad(t\geq3),
\]
\[
 G_r=a_0T_{t,k_r}-a_rT_{t,2t-1}=B_rb_3+C_r,
\quad B_r=a_0b_r-a_rb_0,
\quad C_r=a_0c_r-a_rc_0.                                                \tag{1.4}
\]

The uniform leading scalar is

\[
 a_0=-{t(3t+1)\{(27t^3-30t^2+t-2)d+
                    6t^3+13t^2-3t+2\}
       \over12(2t+1)^2(3t-1)^2(3t+2)}.                                  \tag{1.5}
\]

Its norm has the sole admissible boundary zero \(t=2\), so (1.4) is valid
factorwise at every integer \(t\geq3\).  These statements are frozen
TOPTAIL (lines 93--174) and TAIL-SPLIT (the charged hsop report, lines
293--350).

For \(N=((C_r,B_r))_{r=1}^{t-1}\), FITT supplies

\[
 W_r=a_0C_r^2-b_0B_rC_r+c_0B_r^2                                      \tag{1.6}
\]

and identifies the support of the relevant Fitting module with
\(V(I_2(N)+(W_1,\ldots,W_{t-1}))\).  The literal Fitting ideal also contains
the auxiliary \(X_{rs}\), but its support/radical is the displayed locus.
EN-CURVE and LENGTH-SPLIT describe the
determinantal curve only after the relevant height/finiteness hypotheses:

\[
 d_\Gamma(t)={{3t+1\choose t-1}-{2t\choose t-1}\over t+1},
\qquad
2{3t+1\choose t-1}
=2{2t\choose t-1}+(2t+2)d_\Gamma(t).                                   \tag{1.7}
\]

Equation (1.7) is not used backwards to infer finiteness or nonvanishing.

### 1.3 Fallacy-v2 audit points

The affine cone, its weighted projectivization, the incidence lift, and a
chosen row chart are kept distinct.  No degree/length identity is promoted to
attainment.  No `sat()` computation is used; the saturation in Section 4 is a
mathematical reformulation and is accompanied by its affine radical form.  All
ring maps use the displayed generator order and the relation \(H_t=0\).
There is no prime-labelled derivative, no modular-to-characteristic-zero
promotion in this lane, and no exit-price assertion, so no `charge_basis` line
is due.

## 2. Exact reconstruction for \(t=2,3,4,5,6\)

### 2.1 Reproducible symbolic driver

`box/k16brcr-20260903/emit_exact_tail.py` imports the SHA-verified frozen
`singular_terminal_driver.py` and appends only coefficient extractions and
identity assertions.  It calls no `std`, `slimgb`, resultant, saturation, or
primary-decomposition routine.  Each generated job was run in the foreground
as

```bash
timeout 1200 stdbuf -oL Singular -q brcr_tT_exact.sing
```

and similarly, one factor at a time, for the two \(t=2\) roots.  All six jobs
printed `RECURRENCE_PASS`, `BRCR_DONE`, and `DRIVER_DONE`; no `FAIL`,
`error occurred`, or `div. by 0` marker occurs.  Aggregate wall time for the
durable one-core replay of the two controls and \(t=3,4,5,6\) was 19,416 ms.
`run_audit.tsv` records each exit status, elapsed time, marker count, absence of
standard-basis calls, and source/output/metadata hash.

`summarize_exact_tail.py` then used exact SymPy rational arithmetic to parse
the rows, verify every weighted support count, change coefficients from \(y\)
to \(d\), compute the quadratic norm

\[
 N_{A_t/\mathbf Q}(A d+B)=B^2-{t+1\over3}A^2,                           \tag{2.1}
\]

and carry out the \(t=3\) rank-one chart calculation of Section 4.  This stage
also ran under `timeout 1200`; its durable replay took 17,031 ms and is recorded
in `summary_audit.tsv`.

### 2.2 Full tail rows and coefficient extraction

The following files are the requested explicit polynomials.  Each contains,
in exact Singular syntax, all assignments

```text
T_(2t-1-r), a_r, b_r, c_r       (0 <= r < t),
B_r, C_r                         (1 <= r < t),
```

over the declared \(A_t\); no coefficient is decimalized or evaluated on a
single conjugate.

| \(t\) | coefficient relation | explicit file | bytes | SHA-256 |
|---:|---|---|---:|---|
| 3 | \(588y^2-336y+44=0\) | `box/k16brcr-20260903/explicit_tail_t3_exact.txt` | 9,219 | `140db530e06589fba3e77c97b81e0f77dc925a84b22f7ab398a0a0ca539e525c` |
| 4 | \(972y^2-540y+70=0\) | `box/k16brcr-20260903/explicit_tail_t4_exact.txt` | 52,771 | `31b98207088cf74e7600e2cee9a3761ad61c2c38221526c143aa91ef00b25a22` |
| 5 | \(1452y^2-792y+102=0\) | `box/k16brcr-20260903/explicit_tail_t5_exact.txt` | 167,465 | `aeb448bab69aec1fcccbddf1d575dd899fe0624102868a1c1181252ec0e48f73` |
| 6 | \(2028y^2-1092y+140=0\) | `box/k16brcr-20260903/explicit_tail_t6_exact.txt` | 703,708 | `b06b69090e141945f7ff4110f1164f3730016248b13bd6d2b42117676e58b06b` |

Thus “explicit” here means literal expanded polynomials, not a promise that a
recurrence could expand them.  Keeping the \(0.93\)-MB exact expansion in the
box rather than pasting it into this 20--40 KB proof report is the bounded-write
choice.  As an image/sign check, the beginning of the \(t=3\) top row is

\[
 T_{3,5}=a_0b_3^2+b_0b_3+c_0,
 \qquad a_0={-575d-340\over17248},                                     \tag{2.2}
\]

and the complete \(b_0,c_0\) are the `b_0` and `c_0` assignments in the first
file.  The generated source asserted (1.3) and (1.4) for every row before it
printed `BRCR_DONE`.

### 2.3 Support and leading-coefficient tables

Let

\[
 p_{t-1}(n)=[z^n]\prod_{j=1}^{t-1}(1-z^j)^{-1}.                         \tag{2.3}
\]

The support of every requested form is the complete set of monomials of its
weight.  The exact counts are:

| \(t\) | \(\#b_0\) | \(\#c_0\) | \((\#B_r)_{r=1}^{t-1}\) | \((\#C_r)_{r=1}^{t-1}\) |
|---:|---:|---:|---|---|
| 3 | 3 | 5 | 3, 4 | 5, 6 |
| 4 | 5 | 14 | 7, 8, 10 | 16, 19, 21 |
| 5 | 9 | 34 | 11, 15, 18, 23 | 39, 47, 54, 64 |
| 6 | 13 | 70 | 18, 23, 30, 37, 47 | 84, 101, 119, 141, 164 |

Precisely, these are \(p_{t-1}(t+1)\), \(p_{t-1}(2t+2)\),
\(p_{t-1}(t+1+r)\), and \(p_{t-1}(2t+2+r)\).  SymPy compared actual monomial
tuples rather than trusting Singular's printed term count.  It also checked
all \(a_r,b_r,c_r\), not only the displayed subset.  This is exact evidence at
\(t=3,4,5,6\), not an interpolation to all \(t\).

For a form \(F\) of weight \(w\), define its pure-\(b_4\) coefficient

\[
 \lambda_F(t,r)=[b_4^w]F=F(1,0,\ldots,0).                               \tag{2.4}
\]

In the charged `wp(1,2,...,t-1)` order with \(b_4\) dominant, full support and
\(\lambda_F\ne0\) imply

\[
 \operatorname{LT}(F)=\lambda_F(t,r)b_4^w.                              \tag{2.5}
\]

The complete exact table of \(\lambda\)'s, canonically printed as
`(A*d+B)/D`, is
`box/k16brcr-20260903/support_leaders_compact.tsv`; the longer table
`support_leaders.tsv` also gives every norm (2.1).  It has one line for each
\(a_r,b_r,c_r,B_r,C_r\), with an explicit `branch` column distinguishing both
\(t=2\) factors.  At \(t=3,4,5,6\), all requested leader norms are nonzero.
For orientation, the first nontrivial entries are

```text
lambda_b(3,0) =
 (17243090063480373390*d-21238981495666855551)/58053487971322161500
lambda_B(3,1) =
 (2278007000913733232200497*d-2715311442800994277694247)
 /98014258095453943435556000
lambda_B(3,2) =
 (-1914318319777506349029832717098*d+1539583842758608266161318625969)
 /194999630365446646687194065420000
```

The size of these scalars is itself diagnostic: unlike \(a_r\) at fixed small
\(r\), they have already accumulated the complete spine denominator.

## 3. Closed spine recursion for \(a_r,b_r,c_r\)

### 3.1 Spine substitution and depth filtration

Write \(u_i=q_{i,0}\), initially retaining \(u_t,\ldots,u_{2t}\) and
\(c_1,\ldots,c_{t-1}\), and put \(L=X-b_4\).  The charged translated arrays
are

\[
 U_m={q\choose m}b_4^{q-m}
 +\sum_{\substack{2\leq i\leq2t\\q-i\geq m}}
 u_i{q-i\choose m}b_4^{q-i-m},                                         \tag{3.1}
\]
\[
 \mathcal C_m={t-1\choose m}b_4^{t-1-m}
 +\sum_{\substack{1\leq j<t\\t-1-j\geq m}}
 c_j{t-1-j\choose m}b_4^{t-1-j-m}.                                    \tag{3.2}
\]

With out-of-range coefficients zero, set

\[
 \mathcal B_0=0,\qquad
 \mathcal B_{m+1}={g(3m+5)\mathcal C_m\over2y(m+1)},                    \tag{3.3}
\]
\[
 S_m={3g(m+1)U_{m+1}
 +\sum_{a+b=m-1}(3+2a-b)\mathcal C_a\mathcal B_b
 +(gb_3/2)(5m+7)\mathcal C_m
 \over y(2m+1)}.                                                        \tag{3.4}
\]

Then

\[
 V_m=\mathcal C_{m-2}-yb_3\delta_{m0},\quad
 Y_m=S_{m-1}-b_3\mathcal B_m-gb_2\delta_{m0},\quad
 Z_m=\mathcal B_{m-1}-gb_3\delta_{m0},                                  \tag{3.5}
\]
\[
 N_m=-\sum_{a+b=m}V_a(b+1)Y_{b+1}
 +\sum_{a+b=m}(a+1)V_{a+1}Y_b
 +2\sum_{a+b=m}(a+1)U_{a+1}Z_b,                                       \tag{3.6}
\]
\[
 P_m={N_{m+1}\over2y},\qquad
 R_m=\sum_{a+b=m}V_aP_b-
 \sum_{a+b=m}(a+1)U_{a+1}Y_b-yg\delta_{m0}.                             \tag{3.7}
\]

Equations (3.1)--(3.7), followed by (1.1), are the closed source before the
high variables are eliminated.  They are the frozen Sol report equations
(2.2)--(2.7), lines 78--159.

Order the \(2t+1\) high unknowns by weight:

\[
 z_j=c_j\ (1\leq j<t),\qquad
 z_j=u_j\ (t\leq j\leq2t),\qquad
 z_{2t+1}=b_2.                                                         \tag{3.8}
\]

The (c_j) on the right of (3.8) are the original high-spine coefficients;
the split-tail constants (c_r) are only those in (1.3) and (3.19).

Let

\[
 \Phi_j=[X^{4t+1-j}]R=p_jz_j+\rho_j(b_3,z_1,\ldots,z_{j-1}).             \tag{3.9}
\]

Weighted triangularity proves that no later variable occurs and that the
coefficient of \(z_j\) is the displayed scalar pivot.  For \(1\leq j<t\),

\[
 p_j={3te(A_Cd+B_C)\over
 (t+1)(3t+2)^3(4t-2j+1)},                                               \tag{3.10}
\]
\[
\begin{split}
A_C={}&9j^2t+18j^2-54jt^2-81jt-26j\\
    &+72t^3+144t^2+88t+16,\\
B_C={}&-9j^2t-10j^2+24jt^2+33jt+10j\\
    &-12t^3-20t^2-8t.
\end{split}
\]

For \(t\leq j\leq2t\),

\[
 p_j={-3te(q-j)(A_Qd+B_Q)\over
 (t+1)q(3t+2)^2(4t-2j+1)},                                             \tag{3.11}
\]
\[
 A_Q=12t^2+16t+4-j(3t+4),\qquad B_Q=2(t+1)(j-t),
\]

and

\[
 p_{2t+1}={gd\over2y}.                                                  \tag{3.12}
\]

The pivot formulas are the frozen Sol report, lines 186--212.  Its denominator
audit proves every \(p_j\) a unit for integer \(t\geq2\), factorwise at split
indices (lines 265--327).

### 3.2 Recurrences

Set \(x=b_3\).  Every solved \(z_j(x)\) is homogeneous of weight \(j\), while
\(\operatorname{wt}x=t+1\) and

\[
 j\leq2t+1<2(t+1).
\]

Therefore it has at most two possible \(x\)-layers,

\[
 z_j(x)=z_j^{(0)}+xz_j^{(1)},\qquad z_j^{(1)}=0\quad(j\leq t),            \tag{3.13}
\]

and no \(x^2\) term is possible.  Substituting (3.13) in (3.9) gives the
requested extension of the spine, coefficient by coefficient:

\[
 z_j^{(0)}=-p_j^{-1}\rho_j(0,z_{<j}^{(0)}),                              \tag{3.14}
\]
\[
 z_j^{(1)}=-p_j^{-1}[x]\rho_j
 \bigl(x,z_{<j}^{(0)}+xz_{<j}^{(1)}\bigr).                              \tag{3.15}
\]

This is an exact two-layer recursion, not an empirical fit.  It uses precisely
the same pivots as the original spine and hides no division by a polynomial in
the residual variables.

For an equivalent closed path form, evaluate at
\((x,z)=(0,\bar z)\), \(\bar z=(z_j^{(0)})\), and put

\[
 L_{j\ell}=\partial_{z_\ell}\Phi_j,\qquad
 h_j=\partial_x\Phi_j.                                                   \tag{3.16}
\]

Then \(L\) is lower triangular with diagonal \(p_j\), and

\[
 v=(z_j^{(1)})=-L^{-1}h.                                                 \tag{3.17}
\]

There is no implicit matrix inversion: for \(\ell\leq j\),

\[
 (L^{-1})_{j\ell}={\delta_{j\ell}\over p_j}
 +\sum_{m\geq1}(-1)^m
  \sum_{\ell=i_0<i_1<\cdots<i_m=j}
  {\prod_{a=1}^{m}L_{i_a i_{a-1}}
   \over\prod_{a=0}^{m}p_{i_a}},                                       \tag{3.18}
\]

with \(m\leq j-\ell\); it is zero for \(\ell>j\).  Formula (3.18) is the
finite Neumann/path expansion of a triangular inverse.

### 3.3 Closed form / generating function

Regard the unsolved terminal coefficient

\[
 f_r(x,z)=-[X^{k_r}]R(x,z).
\]

All derivatives in the next display are evaluated at
\((x,z)=(0,\bar z)\).  Since \(z(x)=\bar z+xv\) exactly, the chain rule and
(3.17) give

\[
 c_r=f_r,                                                               \tag{3.19}
\]
\[
 b_r=f_{r,x}+f_{r,z}v
     =f_{r,x}-f_{r,z}L^{-1}h,                                           \tag{3.20}
\]
\[
 a_r={1\over2}\left(
 f_{r,xx}-2f_{r,xz}L^{-1}h
 +(L^{-1}h)^T f_{r,zz}(L^{-1}h)
 \right).                                                               \tag{3.21}
\]

Equations (3.1)--(3.15), together with the finite tangent path sum
(3.18)--(3.21), are an exact finite indexed representation of \(a_r,b_r,c_r\).
Then (1.4) gives \(B_r,C_r\).
This is stronger than merely saying that a program terminates: every entry is
a specified finite coefficient convolution and every inverse is a proved unit.

There is also a concise generating-function form.  Let \(\Delta_t^\sharp\)
denote \(\sigma_t(\Delta)\) after (3.14)--(3.15), and let
\(\Pi_{[0,t-1]}\) select Laurent powers \(0,\ldots,t-1\).  Then

\[
 \mathcal Q_t(\xi,x)
 =-\Pi_{[0,t-1]}\left(\xi^{-2t-2}\Delta_t^\sharp(\xi,x)\right)
 =\sum_{r=0}^{t-1}(a_rx^2+b_rx+c_r)\xi^r.                               \tag{3.22}
\]

Consequently the three coefficient series are simply
\(-\Pi\xi^{-2t-2}[x^2]\Delta_t^\sharp\),
\(-\Pi\xi^{-2t-2}[x]\Delta_t^\sharp\), and
\(-\Pi\xi^{-2t-2}[x^0]\Delta_t^\sharp\).  Specializing
\(b_4=1,q_{2,0}=\cdots=q_{t-1,0}=0\) in (3.22) gives the promised finite
indexed definition of every leader scalar (2.4):

\[
 \lambda_{B}(t,r)=a_0\lambda_b(t,r)-\lambda_a(t,r)\lambda_b(t,0),
\quad
 \lambda_{C}(t,r)=a_0\lambda_c(t,r)-\lambda_a(t,r)\lambda_c(t,0).       \tag{3.23}
\]

Thus the leading coefficients are functions of \((t,r)\) given by the same
two-layer recursion, with the finite path sum evaluating its tangent layer.
The exact specializations through \(t=6\) are tabulated in the box.  No fixed
rational function in \(\mathbf Q(t,d)\) is asserted for the growing-depth
sequences in (3.23).

### 3.4 Exact checks against \(t=2,3,4,5,6\)

The generated rows directly assert (3.19)--(3.21) through coefficient
extraction, (1.3), and (1.4).  SymPy independently verifies the complete
weighted supports and the nonzero leader norms.  Formula (1.5) reduces to every
printed \(a_0\).  The \(t=2\) specializations are displayed in Section 5.

The depth accounting is the decisive correction to the suggested argument:

- For \(a_r\), a constant layer can occur only for \(j\leq r\), and a tangent
  layer only for \(j-(t+1)\leq r\).  This is the truncated spine
  \(C_1,\ldots,C_r\) and
  \(q_{t+1,0}^{(1)},\ldots,q_{t+1+r,0}^{(1)}\), exactly \(2r+1\) layer
  scalars.  The charged proof states this directly for \(r\leq t-2\).  At the
  boundary \(r=t-1\), the only extra weight-eligible variable is the separate
  integration constant \(b_1\); equations (3.5)--(3.7) use \(P_0'\), not that
  constant, so the terminal associate is independent of it and the same count
  remains valid.
- For \(b_r\), every tangent layer through \(q_{2t,0}^{(1)}\) and
  \(b_2^{(1)}\) is weight-eligible; its constant part already reaches through
  weight \(t+1+r\).  Thus no weight/depth argument licenses omitting the last
  tangent solve, even for \(b_0\).
- For \(c_r\), every constant layer has weight at most \(2t+1<2t+2+r\), so
  the entire constant spine is eligible.  Thus no such argument licenses
  omitting the last constant solve, even for \(c_0\).

The raw recurrence really contains the last pivot.  Varying \(b_2\) by
\(\delta\) in (3.5)--(3.7) gives

\[
 \delta R=g\delta\left[U'-{V\{V'-V'(0)\}\over2yL}\right].               \tag{3.24}
\]

Its \(L^{2t}\) term has coefficient
\(g(q-(t+1)/(2y))=gd/(2y)=p_{2t+1}\), rechecking the final diagonal, and
translation \(X=L+b_4\) can feed every top band with a power of \(b_4\).
Dropping the last constant or tangent pivot therefore requires a new uniform
cancellation identity after substitution; none follows from the charged
spine.  Equation (3.24) does not by itself rule out an accidental cancellation
in an individual final coefficient.

## 4. Restriction to the Eagon--Northcott curve

### 4.1 Rank-one kernel and the forced parameter \(\beta\)

At a rank-one point of \(N\), a finite lift has kernel \((1:\beta)\) and

\[
 C_r+\beta B_r=0\quad(1\leq r<t).                                      \tag{4.1}
\]

If \(B_s\ne0\), then \(\beta=-C_s/B_s\), and all such ratios agree.  This is
a cover by the opens \(D(B_s)\), not a single global fraction.  On that chart,

\[
 W_s=B_s^2Q_t,\qquad
 Q_t=a_0\beta^2+b_0\beta+c_0.                                          \tag{4.2}
\]

If all \(B_r=0\) but some \(C_s\ne0\), the kernel is \((0:1)\), there is no
finite \(b_3\)-lift, and \(W_s=a_0C_s^2\ne0\).  If all \(B_r=C_r=0\) at a
nonzero point, this is rank zero (criterion RANK clause (i)); over an algebraic
closure the unit-leading quadratic has a root and produces a genuine tail
obstruction.  These branches cannot be merged.

### 4.2 Cleared eliminants \(W_r\)

The algebraic identity

\[
 W_r=B_r^2T_{t,2t-1}
 -G_r\{a_0G_r-2a_0C_r+b_0B_r\}                                        \tag{4.3}
\]

shows (4.2) without division.  After base change to an algebraic closure of
each factor of \(A_t\), put

\[
 \mathfrak m=(b_4,q_{2,0},\ldots,q_{t-1,0}),\qquad
 K_t=I_2(N)+(W_1,\ldots,W_{t-1}).                                      \tag{4.4}
\]

The correct collective RANK target (clauses (i) and (ii) together) is

\[
 \sqrt{K_t}=\mathfrak m,                                                \tag{4.5}
\]

equivalently \(V(K_t)=\{0\}\), or

\[
 \operatorname{Proj}(P_t/K_t)=\varnothing,
 \qquad (K_t:\mathfrak m^\infty)=P_t.                                 \tag{4.6}
\]

All \(W_r\) have positive weight and vanish at the cone vertex, so no one of
them is a literal unit of the affine graded coordinate ring.  A gcd is also
the wrong invariant: the coordinate ring can be reducible/nonfactorial, and
even in a polynomial UFD gcd \(1\) does not say that a multivariable ideal has
no common projective zero.  The object in (4.5) is the ideal generated by all
row-chart eliminants.

For the Q-nonvanishing clause alone, let

\[
 J_0=(B_1,\ldots,B_{t-1},C_1,\ldots,C_{t-1}).                            \tag{4.6a}
\]

The rank-one locus is the determinantal locus minus \(V(J_0)\).  Its exact
projective residual is therefore

\[
 \operatorname{Proj}\left(P_t/((K_t:J_0^\infty))\right)=\varnothing.     \tag{4.6b}
\]

If clause (i), \(V(J_0)=\{0\}\), is already known, (4.6b) is equivalent to
(4.5).  Without clause (i), (4.5) would silently assert both open clauses.

### 4.3 Unit/nonunit test on \(\Gamma\)

The \(W_1\)-only proposal fails exactly already at \(t=3\).  Let

\[
 p=(b_4,q_{2,0})=(0,1).
\]

By weights, \(B_1(p)=C_1(p)=0\), while the exact axis coefficients of
\(B_2,C_2\) are nonzero.  Thus \(p\in\Gamma\), \(\operatorname{rank}N(p)=1\),
and \(W_1(p)=0\), but the valid chart is \(D(B_2)\).  Exact SymPy reduction in
\(A_3=\mathbf Q[d]/(3d^2-4)\) gives

\[
 Q_3(p,-C_2/B_2)=
 {247708991746515982000-458617889090405137250d
  \over339689253270252579894963},                                      \tag{4.7}
\]

with norm

\[
 -{1128865220069406498250000
 \over594567950987267927914970692827}\ne0.                              \tag{4.8}
\]

Moreover the computation checks exactly

\[
 W_2(p)-B_2(p)^2Q_3(p,-C_2/B_2)=0,
 \qquad W_2(p)\ne0.                                                     \tag{4.9}
\]

The full record is
`box/k16brcr-20260903/t3_q2_axis_control.json`.  Hence the zero of \(W_1\) is
not a candidate (V0)-failure after the denominator branch is handled: the
forced lift satisfies the linear rows but not the top row.  This is the direct
cone check requested in item (3).

### 4.4 Direct cone check of any vanishing locus

No actual zero of \(Q_t\) on \(\Gamma\) was found.  Charged results prove the
nonvanishing exactly at \(t=3,4\) and by the stated properness promotion at
\(t=5,6\) (frozen `k16-rank-criterion-fable5-20260903.md`, lines 414--418 and
478--488); they do not imply the all-\(t\) assertion.  The layer formula exposes
why it does not collapse to a scalar polynomial in \(t\): the projectivized
determinantal curve has weighted degree

\[
 d_\Gamma(t)={{3t+1\choose t-1}-{2t\choose t-1}\over t+1},              \tag{4.10}
\]

when the EN expected-height hypothesis holds; only then is the determinantal
locus the curve used here.  Its points have coordinates defined by
full-support, full-spine forms.
Nothing in (3.18)--(3.23) parametrizes those points by \(t\) alone.

A chart-safe homogeneous formulation is useful for future work.  Use the
weighted projective-bundle coordinate \([u:v]\) with the relative twist
\(\deg_P(v)-\deg_P(u)=t+1\), and impose

\[
 uC_r+vB_r=0,\qquad
 \widehat Q_t=a_0v^2+b_0uv+c_0u^2.                                    \tag{4.11}
\]

The chart \(u=0\) is automatically safe because
\(\widehat Q_t=a_0v^2\); on \(u\ne0\), \(v/u=\beta\).  The remaining exact
residual is to prove that (4.11) has no nonzero rank-one base point,
equivalently (4.6b), factorwise.  With rank-zero clause (i) added, this becomes
(4.5).  Neither the leading coefficient norms nor LENGTH-SPLIT proves that
disjointness.

## 5. The \(t=2\) control

### 5.1 \(y=1/5\)

Here \(d=-1\), and the generated tail is

\[
 T_{2,3}=-{77\over80}b_3b_4^3+{413\over128}b_4^6,
\]
\[
 T_{2,2}={7\over40}b_3b_4^4-{49\over128}b_4^7.                          \tag{5.1}
\]

Thus

\[
 a_0=a_1=0,\quad b_0=-{77\over80}b_4^3,\quad
 c_0={413\over128}b_4^6,\quad B_1=C_1=W_1=0.                           \tag{5.2}
\]

Both rows vanish on \(b_4=0\); the \(b_3\)-axis lies in the tail cone and its
dimension is one.  The unit-leading hypothesis behind TAIL-SPLIT/FITT fails,
so it would be invalid to apply the rank-two criterion on this factor.

### 5.2 \(y=2/5\)

Here \(d=1\), and

\[
 Q_2=-{28\over625}\beta^2
 -{34944\over3048625}b_4^3\beta
 +{675939222\over14870583025}b_4^6,                                   \tag{5.3}
\]
\[
 B_1=-{12047616\over11051265625}b_4^4,\qquad
 C_1={232682357376\over53905863465625}b_4^7.                            \tag{5.4}
\]

For \(b_4\ne0\),

\[
 \beta=-C_1/B_1={16030255\over4048574}b_4^3,
\]
\[
 Q_2(p,\beta)=-{2877765360673\over4097737858369}b_4^6\ne0,              \tag{5.5}
\]

and

\[
 W_1=-{60631935093139183828992
 \over72646052899365103388916015625}b_4^{14}.                           \tag{5.6}
\]

Thus \(V(W_1)=\{0\}\) in the one-variable base cone, the tail quotient has
length \(14\), and the cone is zero-dimensional.  Notice that the successful
\(W_1\) in (5.6) is still not a unit; it is a positive-degree parameter.

## 6. Verdict and exact residual

The requested coefficient derivation succeeds in the strongest form licensed
by the indexed source: the complete two-layer spine (3.14)--(3.15), finite
path sum (3.18), coefficient formulas (3.19)--(3.21), and row generating
function (3.22) determine \(b_r,c_r,B_r,C_r\) exactly for arbitrary \(t,r\).
They also prove why the hoped-for bounded-depth rational formula does not
follow: a loss of one power of \(b_3\) costs \(t+1\) units of residual weight,
so the depth filtration alone cannot discard the final high pivot when
computing \(b_0,c_0\).

The nonvanishing attack produces a definitive chart correction and an exact
negative control for the proposed proxy: \(W_1\) vanishes at a rank-one
\(t=3\) point where \(Q_3\) does not.  It produces no actual \(Q_t\)-zero for
\(t\geq3\).  Therefore the full chain

```text
rank-zero clause (i) + Q_t nonvanishing on the rank-one locus for all t
  => (V0) => (8.1) => constant spine / normalizer / second affine spine => (T)
```

cannot be promoted in this report.  The exact residual is:

\[
 \boxed{\text{For every integer }t\geq3\text{ and every factor of }A_t,
 \quad
 \operatorname{Proj}\bigl(P_t/((I_2(N)+(W)):J_0^\infty)\bigr)
 =\varnothing.}                                                        \tag{6.1}
\]

Equivalently, prove the homogeneous incidence system (4.11) has no nonvertex
rank-one zero.  Together with clause (i), (6.1) is the m-primary equality
(4.5), hence the full tail statement.  This is
OPEN[K16-Q-NONVANISHING-ON-GAMMA].  The verdict is **PARTIAL**, not “resolved”
and not “reduced to one scalar polynomial in \(t\).”

## Appendix A. Machine-readable formulas and tables

The explicit files in Section 2 are self-contained once their displayed
quadratic relation for `yy` is imposed.  `support_leaders.json` contains the
same branch-labelled leader table with separate norm fields.
`alpha_formula_checks.json` records all four reductions of (1.5), and
`t3_q2_axis_control.json` records every Boolean used in (4.7)--(4.9).  The raw
`brcr_t*.out` transcripts also include every \(W_r\), but the clean explicit
files intentionally stop at the requested \(T,a,b,c,B,C\) data to keep writes
bounded.

The \(t=2\) exact polynomial files are
`explicit_tail_t2_split_b0.txt` (\(y=1/5\)) and
`explicit_tail_t2_split_b1.txt` (\(y=2/5\)).

## Appendix B. Commands, resource bounds, and output hashes

No Singular process was backgrounded.  No job exceeded one core, the 1200 s
cap, or 18 seconds actual wall time in the durable Singular replay.  No large
standard basis was started.  `run_audit.tsv` and `summary_audit.tsv` are the
durable exit/timing/hash records; `charged_inputs.check.log` is the successful
13-entry receipt-derived input check.  Before sealing, `ps` and the charged
`killmine.py` detector are used to confirm that no lane job remains alive.

`artifacts.sha256` covers the other 46 files in the driver directory.  A final
`sha256sum -c` returned 46/46 `OK`; the manifest SHA-256 is
`d0beb760049ddc6ee9fa854c8189f71593b7449ab93f893d1b0fc2bed8c442ec`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `31120`.
- Body SHA-256:
  `8bda92147889a213b8423e7b82e44180513f8fbe79a7542ec064fc00d57771d7`.
- Frozen basis: `56c0810275f70ca2f2032724c90fac2073db1c32`.
