# D3 sectioned one-support row: polarization ledger and finite CFS threat map

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, independent audit lane  
Frozen basis: `b7dadb6549367948eeb948124d0f0a8429b99d05`  
Lifecycle: **EXACT PROVISIONAL THREAT MAP / ROW OPEN / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Maximum-safe verdict

Consider the promoted degree-three row

```text
m=1,                 T=2t,
D=-2F_t,             local CFS level=2,
S->P1 sectioned,     rho(Y)>=12.                         (0.1)
```

The row is **not eliminated** on the current committed basis.  Four exact
structural reductions do, however, make its next computation finite and much
smaller.

1. For the plane polarization `L=r^*O_X(1,0)`, all relative-minimalization
   blowups lie over `t`.  If `m_j` are the nonnegative multiplicities of the
   induced rational plane net on `S`, counted in the orthogonal total-transform
   basis, then

   ```text
   sum_j m_j=6,                    M^2=3+sum_j m_j^2.    (0.2)
   ```

   Formally, the positive `m_j` give the eleven partitions of six listed in
   Section 3.  Nefness against the total fibre gives the additional exact
   bound `m_j<=3`; hence only seven of the eleven formal partitions can occur.

2. Every component already present in the Kodaira fibre `S_t` has strictly
   negative discrepancy on its strict transform in `Y`, and is therefore
   `r`-exceptional.  In an actual proper-block occurrence, where the promoted
   everywhere-defined first leg and its full image are licensed, the corrected
   morphic rational-forest theorem excludes smooth or multiplicative fibre
   topology.  Thus the fibre is one of

   ```text
   II, III, IV, I_n* (0<=n<=4), IV*, III*, II*.          (0.3)
   ```

3. The central nonzero ternary cubic is in the invariant-theoretic nullcone.
   Up to constant projective equivalence it has one of five standard orbit
   types: cusp; conic plus tangent; three distinct concurrent lines; double
   line plus line; or triple line.

4. The local soluble control

   ```text
   y^2 z=x^3+t^13 z^3                                  (0.4)
   ```

   is normal, generically smooth, exact level two over `C[[t]]`, has minimal
   Kodaira type `II`, local `p_g=2`, and a rational-tree good resolution.
   This proves that Hodge level, normality, solubility, local geometric genus,
   additive fibre topology, and rational-forest topology do not by themselves
   close (0.1).  It is only a local control: the coefficient `t^13` violates
   the required literal raw coefficient-base degree three.  No claim is made
   that its analytic germ cannot have some different presentation.

The load-bearing successor is therefore a two-pass soluble CFS computation
inside the **literal raw degree-three family**, followed by the polarization
cluster tests.  Finite jets remain local data; no survivor is an occurrence
until normal global gluing and the actual proper-block first leg are supplied.

## 1. Charged interface and custody

The binding input is the reviewed integration

```text
95f2f9fc72d6560749aef090ce91dbd0ef3398ed705bcede69258425ad4ca9de
  xmodel/bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md

087953ec71175d8e470cd2aa89dd7928ef0ab88223009c619e2d95dc39287637
  xmodel/bd-a2-d3-hodge-level-divisor-sol56-20260830.md
```

It supplies an integral normal class-`(3,3)` hypersurface
`X subset P2 x P1`, the minimal projective resolution `r:Y->X`, the fibration
`f=q r`, and the relative minimalization `h:Y->S`.  In row (0.1), `S` is a
rational elliptic surface with a section,

```text
K_S=-F,                 D=h_*(K_Y-r^*K_X)=-2F_t,
Delta=K_Y-r^*K_X<=0,    Delta=h^*D+K_(Y/S).              (1.1)
```

The exact Hodge/CFS scaling at `t` is

```text
v(c4_plane)>=8,         v(c6_plane)>=12,
v(Disc_plane)>=24,
[v(c4_plane)<12 or v(c6_plane)<18].                     (1.2)
```

The bracket is a union of principal opens, not a closed generator.  The local
generic cubic is soluble: the section of `S` gives a `C((t))`-point on the
generic genus-one curve, so its minimal CFS floor is level zero.

The rational-forest theorem used below is only the reviewed morphic
correction

```text
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md.
```

It applies to an everywhere-defined dominant morphism `A2->V`, and not to
mere rational domination.  Every use in this report is explicitly conditional
on an actual proper-block occurrence supplying that morphism and controlling
its full image.

## 2. Plane polarization and its cohomology

Put `A=O_X(1,0)`, `B=O_X(0,1)`, and `L=r^*A`.  Since
`K_X=B` by adjunction and an exceptional divisor has zero intersection with a
pullback from `X`, the intersection numbers are

```text
L^2=3,                  L.F=3,                  K_Y.L=3. (2.1)
```

These are direct ambient intersections: in `P2 x P1`, `A^2B=1` and
`[X]=3A+3B`.

There is also a useful exact cohomology check.  The ambient restriction
sequence is

```text
0 -> O_P2xP1(-2,-3) -> O_P2xP1(1,0) -> O_X(A) -> 0.
```

All cohomology groups of `O_P2(-2)` vanish, so projection to `P1` gives

```text
q_*O_X(A)=O_P1^3,              R^1q_*O_X(A)=0.          (2.2)
```

Normality gives `r_*L=O_X(A)`.  Projection formula gives
`R^1r_*L=R^1r_*O_Y tensor O_X(A)`, and the promoted one-point row says its
pushforward to the coefficient base has length two.  Leray therefore gives

```text
f_*L=O_P1^3,                   length(R^1f_*L)=2.        (2.3)
```

Equation (2.3) is a consistency check on any proposed model.  It is not, by
itself, an Euler or height obstruction.

## 3. Exact blowup and basepoint ledger

### 3.1 Every `h`-blowup lies over the one support

Over a base value `s!=t`, equation (1.1) reads

```text
Delta|_(Y_s)=K_(Y/S)|_(Y_s).
```

The left side is anti-effective and the right side is the effective relative
canonical divisor of the blowup sequence.  Hence both vanish there.  Thus no
curve contracted by `h` lies over `s`; all blowup centres are over `t`.

### 3.2 Derivation of `sum m_j=6`

Factor `h` into point blowups.  The morphism `Y->P2` defined by the complete
three-dimensional space `H^0(Y,L)` induces a rational plane net on `S`.
Cancel the common divisorial factor of the three pushed sections and let `M`
be the resulting mobile divisor class.  Then, in the orthogonal
total-transform basis,

```text
L=h^*M-sum_j m_j E_j^*,
K_Y=h^*K_S+sum_j E_j^*.                                 (3.1)
```

Here `E_j^*` is the total transform on `Y` of the exceptional curve born at
the `j`-th blowup.  The three pushed sections define a base ideal; `m_j` is
its order at that (possibly infinitely near) centre.  Thus `m_j>=0`.
Extraneous resolution blowups on which the net is already regular have
`m_j=0`.

Total transforms satisfy

```text
(E_i^*.E_j^*)=-delta_ij,        h^*NS(S).E_j^*=0.
```

Since `K_S=-F` and `M.F=L.F=3`, intersecting the two expressions in (3.1)
and using (2.1) gives

```text
3=K_Y.L=K_S.M+sum_j m_j=-3+sum_j m_j.
```

Therefore

```text
sum_j m_j=6.                                             (3.2)
```

Squaring the first expression in (3.1) gives the second exact identity

```text
M^2=3+sum_j m_j^2.                                      (3.3)
```

### 3.3 The eleven formal partitions and the fibre-degree pruning

Ignoring zeros and chronology, (3.2) has exactly eleven unordered positive
partitions:

| positive multiplicities | `sum m_j^2` | `M^2` | fibre-degree test |
|---|---:|---:|---|
| `6` | 36 | 39 | excluded |
| `5+1` | 26 | 29 | excluded |
| `4+2` | 20 | 23 | excluded |
| `4+1+1` | 18 | 21 | excluded |
| `3+3` | 18 | 21 | retained |
| `3+2+1` | 14 | 17 | retained |
| `3+1+1+1` | 12 | 15 | retained |
| `2+2+2` | 12 | 15 | retained |
| `2+2+1+1` | 10 | 13 | retained |
| `2+1+1+1+1` | 8 | 11 | retained |
| `1+1+1+1+1+1` | 6 | 9 | retained |

The last column follows without assuming that the fibre is reduced.  Let
`nu_j>=1` be the multiplicity at the `j`-th centre of the current total
transform of `F_t`.  At the birth of `E_j`, and hence after all later
pullbacks,

```text
F_Y-nu_j E_j^* is effective.                            (3.4)
```

The divisor `L` is nef because it is pulled back from `P2`.  Intersecting
(3.4) with `L` gives

```text
3=L.F_Y >= nu_j L.E_j^*=nu_j m_j,
```

so every `m_j<=3`.  This removes precisely the four partitions having a part
at least four.  Proximity and fibre-multiplicity inequalities can prune the
seven retained rows further, but they have not been exhausted here.

Zeros require separate bookkeeping.  They do not enter a partition of six
and are not bounded by (3.2).  Nor is

```text
m_j=0  <=>  crepant/ADE
```

valid.  A zero says only that this total-transform direction carries no
plane-net base multiplicity.  A crepant ADE root is instead detected by zero
coefficient in `Delta`; zero-multiplicity blowups may also decorate a
noncrepant resolution cluster, and an ancestor total transform can have
positive `m_j` because of later descendants.  Any computation must retain
the `m_j=0` resolution vertices and the discrepancy labels independently.

## 4. The original fibre is exceptional and must be additive

Write the Kodaira fibre on `S` as

```text
F_t=sum_i a_i Theta_i,                  a_i>0.
```

From `Delta=h^*(-2F_t)+K_(Y/S)`, the coefficient on the strict transform
`Theta_i^Y` is exactly

```text
coeff_(Theta_i^Y)(Delta)=-2a_i<0,                       (4.1)
```

because `K_(Y/S)` has only `h`-exceptional components.  The discrepancy
divisor of a resolution of a normal surface is supported on the
`r`-exceptional locus.  Hence every `Theta_i^Y` is contracted by `r`.  This
does not assert that every component subsequently born by a blowup is
`r`-exceptional: a zero-discrepancy carrier must ultimately map onto the
one-dimensional plane fibre.

Now impose the additional occurrence hypothesis from a proper block.  The
actual first leg gives an everywhere-defined dominant morphism
`A2->V`, and `V` omits the singular point over which the curves in (4.1) are
contracted.  Their complete transforms are therefore boundary in a common
good completion.  The morphic rational-forest theorem forces their
normalizations to be rational and their dual multigraph to be acyclic.

This excludes:

- `I_0`, because its component has genus one;
- `I_n` for `n>=2`, because its component graph is a cycle;
- `I_1`, because resolving the node gives a rational strict transform and an
  exceptional curve joined by two edges, again a cycle.

Consequently only the additive tree types in (0.3) remain.  Shioda--Tate on
the rational elliptic surface gives

```text
10=rho(S)=2+rank MW(S)+sum_v rank R_v.
```

For `I_n*`, the root rank is `n+4`, hence `n<=4`.  The minimal discriminant
order at `t` is therefore between two and ten.  Exact level-two scaling gives
the useful finite check

```text
26<=v_t(Disc_plane)=24+v_t(Disc_min)<=34.               (4.2)
```

Without the actual morphic first leg and full-image statement, this entire
forest pruning is unavailable.  Rational domination alone does not license
it.

## 5. Five central nullcone types

Reduce the raw ternary cubic modulo `t`.  Equation (1.2) makes both basic
ternary-cubic invariants vanish on the nonzero reduction.  Thus it lies in
the nullcone.  Over `C`, the nonzero nullcone has the following five
projective orbit types, with convenient representatives:

| type | representative |
|---|---|
| irreducible cusp | `y^2z-x^3` |
| smooth conic plus tangent line | `x(xz-y^2)` |
| three distinct concurrent lines | `xy(x-y)` |
| double line plus a distinct line | `x^2y` |
| triple line | `x^3` |

Degenerations among rows are already represented lower in the table; the
zero cubic is excluded because every coefficient-base fibre is a nonzero
Cartier plane cubic.  This five-orbit split is only the first residue step.
Higher coefficients and the open exact-level condition still vary in
positive-dimensional families.

## 6. Exact local positive control

Let `R=C[[t]]` and consider the integral ternary Weierstrass cubic

```text
Phi: y^2z=x^3+t^13z^3.                                  (6.1)
```

It has the section `[0:1:0]`.  In the chart `z=1`, the gradient of
`y^2-x^3-t^13` vanishes only at `(x,y,t)=(0,0,0)`.  The projective point at
infinity is smooth because the `z`-derivative is `y^2` there.  Thus the total
surface has one isolated hypersurface singularity; hypersurface `S_2` plus
regularity in codimension one proves normality.  The generic cubic is smooth.

The integral change

```text
x=t^4X,                y=t^6Y
```

and division by `t^12` gives the minimal equation

```text
Y^2z=X^3+tz^3,                                           (6.2)
```

of Kodaira type `II`.  For (6.1),

```text
c4=0,                  v(c6)=13,        v(Disc)=26;
```

for (6.2), the corresponding orders are `infinity,1,2`.  The invariant
differences are `(8,12,24)` in weights `(4,6,12)`, so the soluble ternary
cubic has exact CFS level two and satisfies the upper open in (1.2) via
`v(c6)=13<18`.

### 6.1 Exact `p_g=2`

The affine singularity is the Brieskorn--Pham singularity of exponents
`(2,3,13)`.  The Newton-nondegenerate geometric-genus formula counts positive
triples satisfying the weak inequality

```text
i/2+j/3+k/13<=1.
```

Necessarily `i=j=1`, after which `k<=13/6`; hence only `k=1,2` occur.  There
is no boundary equality.  Therefore

```text
p_g(y^2-x^3-t^13)=2.                                    (6.3)
```

### 6.2 Exact rational-tree verification

Pairwise coprimality is not being used as an unsupported graph slogan.  The
link is the Seifert manifold `Sigma(2,3,13)`.  Up to orientation it has
normalized Seifert data

```text
(-1; (2,1),(3,1),(13,2)).
```

The determinant in the abelianized Seifert presentation is

```text
|-1*2*3*13 + 1*3*13 + 1*2*13 + 2*2*3|
=|-78+39+26+12|=1.                                      (6.4)
```

Thus the link is an integral homology sphere.  For completeness, the
standard plumbing exact sequence for a good resolution with component genera
`g_i`, dual multigraph `Gamma`, and intersection matrix `I` gives

```text
dim_Q H_1(link;Q)
=2 sum_i g_i+b_1(Gamma)+nullity_Q(I).                   (6.5)
```

The exceptional intersection matrix of a normal surface singularity is
negative definite, so its nullity is zero.  Equations (6.4)--(6.5) force
every `g_i=0` and `b_1(Gamma)=0`.  Hence every good resolution has rational
components and a tree dual graph: its boundary invariant is `tau=0`.

The two primary topological inputs behind this explicit check are
Brieskorn's homology-sphere criterion for Brieskorn links and the standard
Seifert/plumbing homology presentation; see E. Brieskorn, *Beispiele zur
Differentialtopologie von Singularitaeten*, Invent. Math. 2 (1966), and
W. Neumann--F. Raymond, *Seifert manifolds, plumbing, mu-invariant and
orientation reversing maps*, in Algebraic and Geometric Topology, LNM 664
(1978), Theorem 4.1.  Equation (6.4) independently performs the determinant
calculation for this exponent triple.

This control therefore passes all of the listed **local** numerical and
topological tests.  It fails the campaign presentation at the literal raw
level: `t^13` is not a coefficient of degree at most three on the fixed
coefficient base.  It is not a class-`(3,3)` occurrence and supplies no
proper-block morphism.  Its only role is to prevent a false local closure and
to show why raw degree three must be consumed in the successor.

## 7. Other obstruction routes: current exact status

### Euler and fibre configurations

A rational elliptic surface has total fibre Euler number twelve.  Each type
in (0.3) consumes between two and ten, and the remaining singular fibres can
absorb the complementary Euler number.  Blowups over `t` raise both `e(Y)`
and `rho(Y)` one at a time.  The promoted lower bound of two blowups is
consistent with (3.2), which in fact forces at least two positive
multiplicities because each is at most three.  No contradiction follows
without an independent upper bound or a restriction on the other fibres.

### Section height

Shioda--Tate supplies the root-rank bound used above, but the promoted
interface does not identify a nontrivial Mordell--Weil section whose height
could be forced negative.  The existence of the zero section alone is
compatible with every additive type in (0.3).  A height argument must first
derive a specific section or multisection class from `M` and its basepoint
cluster; finite jet data do not provide one.

### Weighted boundary

There is no universal weight face presently forced across all five nullcone
types and all seven retained polarization partitions.  Control (6.1) shows
that any proposed face theorem using only exact level two and `p_g=2` must
also use literal degree three or another global occurrence input.

## 8. Concrete finite two-pass CFS successor

Work in the literal raw family at `t=0`,

```text
F=F_0+tF_1+t^2F_2+t^3F_3,                              (8.1)
```

with spatially homogeneous ternary cubics `F_i`.  The computation should be
run as follows.

### Pass A: level two to lower level

1. Normalize `F_0` to each of the five representatives in Section 5, retaining
   the stabilizer action rather than quotienting away coefficient parameters.
2. Impose the closed divisibility conditions `t^8|c4` and `t^12|c6`, while
   keeping the exact-level upper disjunction in (1.2) as two principal-open
   charts.  Keep normality and generic smoothness as opens.
3. Run the CFS ternary-cubic minimization algorithm, including every singular
   point/line branch prescribed by the reduction.  One successful pass must
   lower the level by at least one.  Record the integral coordinate matrix,
   scalar factor, transformed raw coefficients, and induced infinitely-near
   basepoint centre.  If the model drops directly to level zero, retain it as
   a terminal local shard.

### Pass B: residual level one to level zero

4. For every level-one output, renormalize its nonzero reduction and rerun the
   same finite CFS branch tree.  Solubility forbids a positive-level minimal
   critical floor, so the second successful pass must end at level zero.
   “Two-pass” means at most two successful level-lowering passes; it does not
   mean two fixed elementary line moves, and the bounded inner CFS iterations
   must still be enumerated.
5. Reconstruct the associated plane-net cluster on `S`.  Reject any shard
   unless its positive multiplicities satisfy one of the seven retained rows
   in Section 3, the proximity inequalities, `sum m_j=6`, and
   `M^2=3+sum m_j^2`.  Track zero-multiplicity resolution/ADE vertices
   separately.
6. Compute the minimal Kodaira symbol.  Under an actual morphic occurrence,
   retain only (0.3) and enforce (4.2).  Without that occurrence, mark the
   fibre-topology filter unavailable rather than silently applying it.

The fixed regression controls should include (6.1): it must pass the local
CFS, normality, solubility and topology checks, then be rejected at the raw
degree-three presentation gate before any global-occurrence tests.  Include a
level-one critical insoluble control to ensure the sectioned floor-zero branch
is not confused with the Halphen floor-one branch.

Any surviving finite jet is only a local formal shard.  It must next be glued
inside the global class-`(3,3)` family, checked for normality and generic
smoothness on the declared opens, and matched to the actual finite incidence
and everywhere-defined first-leg image.  If the exact elimination ceases to
be desk-scale, freeze the coefficient ring, orbit chart, opens and expected
control outputs before moving it to AWS.

## 9. Firewalls and nonclaims

- This report does not eliminate row (0.1), construct it, or decide JC2.
- It does not infer boundary topology from a dominant rational map.
- It does not infer solubility, global normality, or a proper-block occurrence
  from a finite jet.
- It does not equate basepoint multiplicity zero with crepant discrepancy.
- It does not claim that all eleven formal partitions occur; four are already
  excluded by `L.F=3`, and the remaining seven are only necessary cases.
- It does not infer local geometric genus from the reduced exceptional graph.
  Control (6.1) has `p_g=2` and nevertheless has a rational-tree resolution.
- It does not claim that the degree-thirteen control has no analytically
  equivalent degree-three presentation; it records only that the exhibited
  raw model violates the fixed literal campaign presentation.

The maximum-safe advance is therefore the exact ledger (0.2), its
fibre-degree pruning, the conditional additive list (0.3), and the five-orbit
two-pass CFS successor.  The sectioned one-support row remains live.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20801`.
- Body SHA-256:
  `f202705ad4992611ff75795918c9d929c693e1e54c03ba3501fe06f4262efda9`.
- Frozen basis: `b7dadb6549367948eeb948124d0f0a8429b99d05`.
