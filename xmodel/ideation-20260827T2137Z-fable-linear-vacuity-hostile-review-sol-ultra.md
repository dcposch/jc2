# Hostile review of Fable5 T3 / erratum E0 — exact-p-power linear vacuity

Date: 2026-08-27  
Reviewer: Sol Ultra, different model from the Fable5 producer  
Target: `xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md`  
Target SHA-256: `b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a`

## Verdict

**T3 is confirmed at its narrow, literal scope.**  In the licensed
exact-`p`-power presentation, the `F_n`-linear part of the row
`m=n+22` class is exact for every `k_m=1` row with `m>=28`.  Independent
exact-`Q` localization ranks reconstructed from the frozen raw windows give

```text
P rows 23..36: 3,4,3,4,3,0,3,0,3,0,3,0,1,0   (26 through 34; 27 total)
Q rows 23..36: 4,5,4,4,4,0,4,1,4,0,4,1,2,0   (35 through 34; 37 total)
```

Thus Fable5's `27/37` all-window linear totals and its specific erratum at
rows 28/30 are correct.  The promoted receiver-dimension law and the
`42/51/12/87` twelve-row totals are **not wrong**: they remain abstract
target-dimension/height ceilings.  What is wrong is the promoted sentence
that realized stable-range equality on the control lasts through row 30;
for the licensed exact-`p`-power new-slot map it already fails at row 28 and
the uniform equality range is rows **23--27**.

Two scope repairs are mandatory.  “Class-exact” applies only to the
`F_n`-linear term, not necessarily to the nonlinear carry in the full
`q_n`.  Also, a negative `H`-power in that carry does not prove generic
nonexactness.  No claim that the later nonlinear rows are generically
nonvacuous is licensed by T3.

## 1. Independent derivation

The now-promoted all-row coefficient formula gives, for `n>=1`,

```text
(q_n)_linear = (1/4) F_n p^(n-6).
```

Put `m=n+22`.  Since `p^28=H^7`, this is

```text
(q_n)_linear = p^m * F_n/(4H^7).
```

Relative to `p^m`, exactness is measured by

```text
nabla_m = d + (m/4)dH/H,
nabla_m(c) = H^(-m/4) d(H^(m/4)c).
```

If `k_m=1`, the divisor of `H^(m/4)` is integral.  Geometrically (or after
the harmless constant-field extension already required for the character
language), `H^(m/4)` is a polynomial up to a nonzero scalar.  For `m>=28`,

```text
H^(m/4) * F_n/(4H^7) = (1/4)F_n H^(m/4-7)
```

is polynomial, hence has a polynomial primitive.  Therefore the displayed
linear term is `nabla_m`-exact.  This proves T3 without a finite pole ansatz.

Equivalently, take `j=m mod 4` in `{0,1,2,3}` and

```text
e=(n-6-j)/4.
```

Then `(q_n)_linear=(F_n/4)H^e p^j`, and the literal cleared equation is

```text
4H c' + j H'c = H^(e+1) F_n.                 (1)
```

The frequently copied shifted equation

```text
4H c' + j H'c = F_n                          (2)
```

drops the required `H^(e+1)` factor.  Integer-shifting a connection is an
isomorphism only when the source is shifted with it.  Equation (2) happens
to reproduce the useful early-row operators/ranks, but from row 28 onward
it is not the licensed new-slot equation.  This is the exact source of E0.

## 2. Independent frozen-window rank reconstruction

I read the raw `F` slots directly from
`cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json`.
Their positive-weight `X`-degree sets have dimensions

```text
n=1..8 : 16,15,14,13,12,11,10,9
n=9..14:  7, 6, 5, 3, 2,1
n>=15  :  0.
```

No producer `/tmp` code was used.  The independent exact calculation was as
follows.  Let `R=rad(H)`, `S=R H'/H`, and let `A_n` be the literal frozen
degree set.  For each `a in A_n`, the licensed source is `X^a H^e`.  With a
primitive numerator `C` over `R^M`, common-denominator clearing gives image
columns

```text
B_d = R (X^d)' + ((j/4)S - M R')X^d
```

and source columns

```text
A_a = R^(M+1) H^e X^a.
```

The exact class-map rank is

```text
rank_Q([A_a | B_d]) - rank_Q([B_d]).
```

Fraction Gaussian elimination was run independently at `M=4,6`,
`d=0..70`; both caps gave identical answers.  The finite-pole leading-term
equation makes `M=4` complete for P/Q (the worst source pole order is four),
and degree 70 exceeds the infinity bound.  Checks were made on

```text
P: H=(X^4-1)^2,
Q: H=(X^3-(2/5)X)^2 (X^2-1),
```

and again on the independent squarefree/coprime Q fixture
`H=(X^3-X)^2(X^2-4)`; the Q tables agree byte-for-byte as integer lists.

The licensed and dropped-factor (“shifted”) tables are:

```text
rows                         23 24 25 26 27 28 29 30 31 32 33 34 | 35 36
P licensed                    3  4  3  4  3  0  3  0  3  0  3  0 |  1  0
P shifted                     3  4  3  4  3  4  3  4  3  3  3  3 |  1  1
Q licensed                    4  5  4  4  4  0  4  1  4  0  4  1 |  2  0
Q shifted                     4  5  4  4  4  5  4  4  4  4  4  2 |  2  1
```

The squarefree `r=8` control independently gives licensed ranks

```text
7,8,7,7,7,0,7,7,6,0,5,3,2,0
```

on rows 23--36.  In particular row 28 has rank zero, not eight.  This
directly refutes “stable equality through row 30” in the licensed
presentation.

## 3. Exact maximum correction to the promoted record

Retain unchanged:

1. `[q_n dX]` lands in `H^1_dR(U,nabla_m)` and
   `dim H^1=r-1+k_m` for every licensed row.
2. The torsor packaging and four-row target total.
3. The twelve-row abstract ceilings `42/51/12/87`.
4. The literal row-25/26 new-slot operators and ranks.
5. The not-before height arithmetic, explicitly as a statement about the
   homogeneous class-gate tower, not the polynomial determinant system.

Replace only the realized-linear language by:

> For the licensed exact-`p`-power new-slot maps, equality with the receiver
> dimension holds uniformly on P, Q, and the squarefree control through rows
> 23--27.  At every `k_m=1` row with `m>=28` the new-slot linear class is
> identically exact.  On the frozen P/Q windows the degree-one tower ranks
> through row 34 are 26/35 and the entire infinite tower's degree-one ranks
> are 27/37.  These do not replace the abstract 42/51 class ceilings: later
> nonlinear carry classes may still cut, but no such realization theorem is
> presently proved.

Consequently the old row-28/30 agreement and any linear-time
`GATE-MARCH` rate based on `r-1+k_m` are mathematically wrong, while the
cohomological theorem itself is merely over-read, not false.

## 4. Proposed linear-in-`G` `D28` discriminator

**Verdict: not typed as a `0 versus 4` test, and its stated cost is
underestimated.**

1. The affine target was written incorrectly.  It is
   `D1=...=D21=0, D22=1, D23=...=D27=0`, not `D1=...=D27=0`.
2. With every `F` coefficient numeric, the determinant rows are linear in
   the 276 positive-weight `G` slots.  The frozen supports have about 695
   scalar coefficient positions through row 27 and ten at row 28, so one
   numeric exact-`Q` solve is genuinely desk-scale.
3. Leaving the eleven `F_6` slots symbolic makes terms `F_6 G_b` bilinear.
   The task is then row reduction over `Q(F_6)` or elimination over an
   eleven-variable polynomial ring, not a few-hundred-unknown `Q`-linear
   solve.  A numeric solve cannot recover a codimension in the `F_6`
   window.
4. Satisfying class gates through row 27 does not guarantee a polynomial
   `G` solving the lower affine determinant target.  The proposal supplies
   no such lower-target point or compatible family, so its generic random
   prefix can simply die before `D28`.
5. Most importantly, R7R1 proves polynomial-row solvability implies the
   class gate; the converse over the polynomial support window is not
   proved.  Therefore a raw `D28` compatibility condition depending on
   `F_6` would measure polynomial descent/support, not validate the shifted
   class equation.  “Four conditions” would not refute T3, and “zero” would
   only be consistent with it.

The clean class-level discriminator is already the three-line proof in §1.
A well-typed artifact successor would first exhibit an actual point (or
parameterized family) of the correct lower affine target, then compute the
projected Zariski tangent map in the `F_6` and `G` directions.  Its result
must be labelled a **polynomial-descent/window** rank, not a class-gate rank.

## 5. Scope and custody

This report confirms only a degree-one statement and its exact finite-window
ranks.  It proves no nonlinear-row nonvacuity, tower finiteness, endpoint
death, face emptiness, family exclusion, Keller pair, or JC2 result.  No AWS
resource or live lane was contacted.  No canonical file was edited.  The
nested `jc2-lean` tree was never entered, listed, searched, read, or changed.

Recomputed source pins at review time:

```text
b3f3886c7783ce22e060865206a700f0aab356caf6f708f75f355e99b684517a  xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa  cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py
489647cf5726c46401f4c48c394de64d01ff73fff3a5d3168231428add1c0ea5  cases/ggv_quarter_root_characteristic_r7r1_20260827/FREEZE.md
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
053c85a59c5ec0c63e1c0683771afb90d041573906656d5ad8a5b6c761e62588  AUDIT.md (working copy read for this review)
```
