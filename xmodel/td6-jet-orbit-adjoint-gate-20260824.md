# TD6-JET-ORBIT-ADJOINT — the smallest boundary class is transverse

Date: 2026-08-24  
Charged clean basis: `1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`  
Status: **PROVISIONAL PRODUCER / EXACT FIRST-ORDER GATE / STOP**

## Verdict

At the degree-18 sextic points of the frozen normalized SP-2 control, the
first omitted q-boundary coefficient

\[
 q_B(t)=t+B t^2+t^{25}
\]

is not a formal source-parameter gauge after the registered linear chart and
the `p=t^15` section are fixed.  The smallest truncated boundary-jet quotient
has one transverse class, represented by `q_2`.  Exact differentiation of
the complete staged transport/Jacobian elimination, including the derivative
of the normalized left syzygy, gives

\[
 \boxed{c'(0)=-{4720\over29}\ne0},                 \tag{1}
\]

where `c(0)=rho` is the frozen nonzero `t^4` compatibility residue.
Every base rank is stable to first order.  Thus `q_2` genuinely changes the
obstruction and licenses an exact one-parameter compatibility polynomial.
It is not killed by a gauge argument.

The verdict is

```text
Q2-TRANSVERSE / NONZERO-FIRST-DERIVATIVE /
EXACT-COMPATIBILITY-POLYNOMIAL-LICENSED
```

This is not emptiness of the full `B`-family.  A nonzero derivative at an
already inconsistent point is not a tangent-family kill.  It proves neither
SP-2 nor any terminal class empty.

## 1. Frozen object and source typing

The replay imports by exact hash the frozen q2 compiler and uniform
third-band field.  It retains:

- rectangles `f:(15,60)`, `g:(25,100)`;
- centered chart
  \[
  y=s^{-1},\qquad x=s+s^2+s^3+t s^4;
  \]
- x-boundary `p=t^15`, `q=t+t^25` at the base point;
- the normalized F1 pattern
  \[
  R(z)=(z-1)^2(z^2-Sz+D),
  \]
  with `Q=-2S^2+2S+5D-3=0`;
- zero r9 dead stretch;
- `L=25(1-S+D)` and `L^8 A^3=9`;
- the sextic cut `F(S)=0` and exact degree-18 field
  \[
  E=\mathbb Q[S,A]/(F(S),A^3-9/L^8);
  \]
- transport, first centered Jacobian row, the preceding centered row, and
  the inherited affine pole row before the frozen `t^4` incompatibility.

The source-typing audit separates five different notions that had been
conflated by the point probes.

### 1.1 Full source-coordinate orbit

For the infinitesimal local reparametrization

\[
 t\longmapsto t+\epsilon t^2,
\]

the complete tangent is

\[
 \delta T=t^2,\qquad
 \delta p=15t^{16},\qquad
 \delta q=t^2+25t^{26}.              \tag{2}
\]

The chart component and the two over-cap boundary terms are essential.  The
vector `delta q=t^2` by itself is not (2).  Modulo the orbit, it can be
represented as

\[
 -\delta T=t^2,\qquad
 -\delta p=15t^{16},\qquad
 -\delta q=25t^{26}.                 \tag{3}
\]

The audit constructs the truncated orbit vectors for `1,t,...,t^6` and
row-reduces them.  They have rank seven.  Adding the q2-only vector raises
the rank to eight.  Hence the fixed-linear-chart section is transverse, and
`q_2` represents a nonzero quotient class there.

The `t^4` coefficient of a compatibility series whose first nonzero term is
`rho*t^4` is unchanged under (2): substituting `t+epsilon*t^2` first changes
degree five.  This supplies the exact zero-adjoint gauge control.

### 1.2 Target gauges

Four independent determinant-one target tangents are present:

1. translation of `f`;
2. translation of `g`;
3. reciprocal scaling `(delta f,delta g)=(f,-g)`;
4. the rectangle-preserving lower shear `delta g=f`.

Their boundary vectors have rank four.  Translations and the lower shear
leave the Jacobian exactly unchanged; reciprocal scaling leaves it unchanged
to first order.  They are quotient directions, not boundary moduli.  In
particular, `p_0`, `q_0`, and the `q_15=p` direction cannot be counted as
new transverse jets.

### 1.3 The p-boundary section

Inside the 15-fold-root stratum, differentiating
`a(t-b)^15` shows that the only polynomial p-side tangents are the
`t^15` scale and `t^14` translation directions.  Both belong to the
normalization/reparametrization ledger.  Coefficients below `t^14` change the
root partition and therefore leave the smallest same-stratum gate.  The
`t^16` term in (2) is a coordinate-orbit term outside the fixed linear-chart
degree cap; it is not an independently licensed p-boundary deformation.

After the section

```text
p=t^15,  q(0)=0,  q'(0)=1,
```

the first remaining q-boundary coefficient is exactly `q_2`.

### 1.4 F1 orbit and pole scale

The chain orbit has already been scaled to `C=1`; the unordered extra orbits
are represented by `S,D`.  At a sextic point the tangent equations in
`(S,D,L,A)` are

\[
\begin{aligned}
(-4S+2)\,dS+5\,dD&=0,\\
-9H^2\,dS+9H^2\,dD&=0,\\
25\,dS-25\,dD+dL&=0,\\
8\,dL/L+3\,dA/A&=0,
\end{aligned}                                      \tag{4}
\]

where `H=1-S+D`.  This matrix has rank `4/4` over `E`.  The first two
rows have determinant `9H^2(7-4S)`, and the replay verifies

\[
 F(7/4)=-53875/512\ne0.
\]

Thus F1-orbit and pole-scale moduli cannot move by themselves while the
already imposed source equations remain fixed.  They can still occur as
forced compensators in a later centering, dead-stretch, or boundary pencil.

### 1.5 Centering and dead stretch

The three common centering coefficients and the eleven r9 dead-stretch
coefficients are licensed data that were frozen in this control.  No proved
source automorphism normalizes them while keeping all three charts and the
rectangles in the registered form.  They are therefore not silently placed
in the gauge subspace.  They are also not part of the present *smallest
q-boundary order-two quotient*.  Their adjoint columns require separate
matrix-derivative pencils because they change the transport matrix itself.

## 2. Ranked tangent table

| rank | tangent family | quotient status | exact first-order result | disposition |
|---:|---|---|---|---|
| 1 | q2-only | one-dimensional transverse basis after the registered section | all inherited ranks stable; `c'(0)=-4720/29` | derive exact `B` compatibility numerator |
| 2 | full `t^2` reparametrization (2) | pure source-coordinate orbit | `t^4` sensitivity `0` | quotient away |
| 3 | two translations, reciprocal scaling, `g+=epsilon f` | four-dimensional target gauge | Jacobian sensitivity `0` | quotient away |
| 4 | `(dS,dD,dL,dA)` alone | no source-compatible tangent: rank `4/4` | rigid on the frozen equations | use only as forced compensators later |
| 5 | common centering `dc1,dc2,dc3` | licensed, not audited as gauge | not computed in this scoped gate | next matrix-changing pencil |
| 6 | dead stretch `d6,...,d16` | licensed, not audited as gauge | not computed in this scoped gate | staged by first entering exponent |

There is no vanishing **transverse** adjoint direction in the one-dimensional
smallest quotient.  The vanishing directions in the table are genuine gauge
controls.  Because `c(0)!=0`, this does not license a family kill: equation
(1) instead says that the obstruction moves and may have a finite nonzero
root.

## 3. Exact differentiated elimination

The replay works over the dual field

\[
 E[\epsilon]/(\epsilon^2),\qquad B=\epsilon.
\]

It does not use the invalid compatible-base shortcut
`lambda^T(delta b-delta A*u)`.  Gaussian elimination is differentiated
itself.  Derivative-only entries in already-pivoted columns are reduced; this
is exactly where the `lambda' A` term enters.  Affine parameterizations are
then replayed coefficientwise over the dual field.

The stages are:

| stage | exact result |
|---|---:|
| transport only | rank `3470/3602`, dimension `132` |
| first centered Jacobian band | rank `38/132`, dimension `94` |
| preceding centered + inherited pole rows | rank `38/94`, dimension `56` |
| current centered homogeneous rows | rank `25/56` |
| affine current elimination | first inconsistent input row `t^4`, after three pivots |

There are no first-order rank-change rows at the first-J, preceding paired,
or current-through-`t^4` stages.

At `B=0`, the replay reproduces the frozen residue

\[
\begin{aligned}
\rho={}&{1\over3625}(2495634-4154976S+4405068S^2\\
&-2488119S^3+761922S^4-105084S^5)
+{136875\over29}A.
\end{aligned}                                      \tag{5}
\]

The dual left syzygy has support on four current rows, and its derivative is
nonzero on three of them.  Direct replay against the unreduced matrix proves

\[
 \lambda(\epsilon)^T A(\epsilon)=0,
 \qquad
 \lambda(\epsilon)^T b(\epsilon)
 =\rho-{4720\over29}\epsilon.                     \tag{6}
\]

The derivative is a cancellation of two individually large exact elements:

\[
 c'(0)=\lambda_0^T b'(0)+\lambda'(0)^T b_0.
\]

All nonconstant `S` slots and the `A` slot cancel between the two summands;
their remaining rational constants differ by

\[
 {-654310000\over4020125}=-{4720\over29}.
\]

The complete two summands and every syzygy weight are serialized by the
replay.  The dual-syzygy digest is

`9527d18e4fbd48d0e6771cb9a45e1c4ffd6e33dfdc9c5cdc052fa6e37c883272`.

This also explains why the old point secant is not the derivative.  The
frozen `B=1` result gives

\[
 c(1)-c(0)=-{14012\over145},
\]

whereas (1) is `-23600/145`.  The difference is real information from the
varying solves/syzygy, not arithmetic noise.

## 4. Fast exact successor: staged E[B] pencils

The correct successor is not a `3602`-variable elimination over `E[B]` and
not another point sample.

1. Reuse the constant rank-`3470` transport factorization.  Its right-hand
   side is affine in `B`, so its particular response is affine and the 132
   homogeneous directions stay rational.
2. Form the roughly `40 x 132` first-J pencil.  It is genuinely affine in
   `B`: f-transport is B-independent, g-transport is affine, and
   `q'_B=1+2Bt+25t^24`.
3. Apply fraction-free elimination over `E[B]`.  Record a generic pivot minor
   and every exceptional factor before passing to the 94-dimensional
   rational parameterization.
4. Propagate only that reduced family through the preceding centered/pole
   rows, obtaining the generic 56-dimensional family and its own pivot
   factors.
5. Clear registered denominators in the current compatibilities, compute the
   gcd of their numerators, and recurse only at roots of the compatibility or
   pivot/resultant factors.  Rebuild exact systems at those roots.

Adjoint derivatives can reduce the number of samples: (1) supplies Hermite
data at zero and proves the compatibility numerator is locally nonconstant.
They do **not** certify interpolation by themselves.  A reconstructed
rational function becomes theorem-grade only after:

- a fraction-free/Bareiss numerator and denominator degree bound is printed;
- more exact value/derivative conditions than that certified bound are used;
- the reconstructed cross-multiplied identity is replayed symbolically (or
  on a provably sufficient deterministic evaluation set); and
- every root of the pivot product is handled as a separate rank stratum.

This staged design retains `lambda'`; normalizing and differentiating the
left-null equations is mandatory at every sample.

## 5. Reproducibility and scope

Run from the repository root:

```text
python3 cases/td6_jet_orbit_adjoint_20260824/orbit_audit.py
python3 cases/td6_jet_orbit_adjoint_20260824/replay.py
```

Both scripts use exact `fractions.Fraction` and the frozen nested degree-18
field only.  No floating point, modular inference, AWS, protected process,
degree widening, generic sparse search, or canonical top-level edit is used.

| artifact | SHA-256 |
|---|---|
| exact dual replay | `fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198` |
| canonical dual stdout | `cd87743d3859a5fa5d4275f7e599a43a9565d0a16a01de4c133bd925b7df0ebf` |
| orbit/source audit | `90bd44ebd6ed810e6d686d44bd84f2f852d623b22a371f137e215436394b967b` |
| canonical orbit stdout | `e158eba810deac8334ec408d1acad313a677fe37552a36006d152f6b45718eb5` |
| imported q2 compiler | `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357` |
| imported uniform-third replay | `7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8` |
| q2 point-probe report | `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0` |
| completed q2 hostile review | `6df0d9c9dde4c4e8991b73da1c807ce40b4f44c2b587949c2312aaebf469665c` |

The orbit audit verifies the source/gauge ranks and (2)--(4).  The main
replay rebuilds every stage, replays both affine parameterizations
coefficientwise, verifies the dual left syzygy against the unreduced current
matrix, and exits nonzero on any rank, residue, derivative, or hash mismatch.

**Scoped conclusion.**  `q_2` is the sole transverse class in the smallest
registered boundary-jet quotient and has nonzero first derivative (1).  The
full `B`-family, centering family, dead-stretch family, broader p-boundary
strata, SP-2, all terminal classes, and JC2 remain open.  This result requires
different-model hostile review before canonical promotion.
