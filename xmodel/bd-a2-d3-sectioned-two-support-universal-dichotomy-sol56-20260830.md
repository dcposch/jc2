# D3 sectioned two-support row: universal forest and marked-cluster dichotomy

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, sublane `/root/sectioned_two_support_universal`  
Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`  
Lifecycle: **EXACT SCOPED PRODUCER / ROW OPEN / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Maximum-safe verdict

Assume the binding degree-three Hodge/four-row theorem and an **actual normal
morphic proper-block occurrence** of the sectioned two-support row

```text
m=1,       T=t_1+t_2,       t_1!=t_2,
D=-F_1-F_2,                 local CFS levels (1,1).       (0.1)
```

There is a finite universal reduction, but not yet a universal exclusion.

1. The plane-net basepoint mass splits by support:

   ```text
   sum_(j over t_i) m_j=3                  for i=1,2.     (0.2)
   ```

   Since every `m_j<=3`, the positive multiplicities over each marked fibre
   have exactly one of the three partitions

   ```text
   3,              2+1,              1+1+1.             (0.3)
   ```

   Thus there are six unordered support-marked cluster pairs.  In particular
   the formerly retained unmarked partition `2+2+2` is impossible.

2. Every component of both marked fibres on the relatively minimal rational
   elliptic surface is contracted by the plane model and lies in the
   first-leg boundary.  The binding morphic rational-forest theorem therefore
   excludes good reduction and every multiplicative Kodaira type `I_n`,
   including `I_1`.  Both marked minimal fibres must be additive.

3. Euler number twelve and Shioda--Tate leave exactly **25 unordered
   Kodaira-symbol pairs**, refining 19 pairs of minimal discriminant orders.
   They are listed in Section 4.  This list is necessary, not an assertion
   that all pairs occur with the required class-`(3,3)` polarization.

4. For a local direct lowering of CFS slope `(1,1)`, the ordinary tangent cone
   of the defect germ is the special cubic of the lowered minimal model.  It
   is smooth exactly when that cubic has good reduction; its ordinary blowup
   exposes a smooth genus-one exceptional curve and is forbidden.  More
   generally the three positive-slope CFS cells `(1,1),(1,2),(2,3)` expose an
   anticanonical weighted face birational to the lowered special cubic, so
   smooth reduction is forbidden in all three cells.

5. Smooth tangent cones are **not** forced.  The literal raw-degree-three
   soluble level-one model

   ```text
   Phi=tau*y^2*z-x^3-tau^3*x*z^2                         (0.4)
   ```

   lowers to a minimal type-`III` Weierstrass model.  Its defect tangent cone
   is the cuspidal cubic `tau*y^2-x^3`, and its good boundary resolution is a
   rational tree.  Hence exact level one, normality, solubility, the raw degree
   cap and the rational-forest gate do not by themselves close (0.1).

The correct successor is the finite intersection of the six marked cluster
cells, the 25 additive Kodaira pairs, the four canonical CFS slope cells and
the five additive nullcone reductions with the **same two global raw
coefficient frames**.  Any survivor must then face complete ramification and
actual block incidence.  No polynomial map or JC2 conclusion is claimed.

## 1. Charged scope

Let

```text
X subset P2 x P1,       r:Y->X,       f=q r,
h:Y->S,                 g:S->P1
```

be the objects of the binding Hodge theorem.  In (0.1), `S` is a rational
elliptic surface with a section, `K_S=-F`, and

```text
Delta=K_Y-r^*K_X<=0,
Delta=h^*(-F_1-F_2)+K_(Y/S).                            (1.1)
```

Put `L=r^*O_X(1,0)`.  The ambient intersection ledger is

```text
L^2=3,                L.F=3,                K_Y.L=3.    (1.2)
```

Factor `h` into point blowups.  In the orthogonal total-transform basis,

```text
L=h^*M-sum_j m_j E_j^*,
K_Y=h^*K_S+sum_j E_j^*,                                (1.3)
```

where `m_j>=0` is the order of the pushed plane net at the possibly
infinitely-near centre.  Zero-multiplicity resolution vertices remain
separate data and are never discarded.

All uses of boundary genus or cycles below are conditional on the actual
proper block.  That occurrence supplies an everywhere-defined dominant
morphism from `A2` to the first-leg image.  Mere rational domination of an
abstract surface would not license the forest theorem.

## 2. The exact local mass is three at each support

Outside `t_1,t_2`, equation (1.1) identifies the anti-effective divisor
`Delta` with the effective relative canonical divisor of the blowup sequence.
Both vanish there.  Hence every `h`-blowup lies over one of the two marked
fibres.

Let `J_i` be the set of blowups over `t_i`.  Splitting (1.1) by its disjoint
vertical supports gives

```text
Delta_i=h^*(-F_i)+sum_(j in J_i) E_j^*.                 (2.1)
```

Every component of `Delta_i` is `r`-exceptional, while `L` is pulled back
from `X`; consequently `L.Delta_i=0`.  Equations (1.2)--(1.3) now give the
local identity, not merely its global sum:

```text
0=L.Delta_i=-L.F_i+sum_(j in J_i)L.E_j^*
             =-3+sum_(j in J_i)m_j.                    (2.2)
```

This proves (0.2).

The fibre-degree bound is also local.  If `nu_j>=1` is the multiplicity of
the current total transform of `F_i` at the `j`-th centre, then

```text
F_Y-nu_j E_j^* is effective.
```

Nefness of `L` gives

```text
3=L.F_Y>=nu_j L.E_j^*=nu_j m_j,
```

so `m_j<=3`.  The positive partitions of three are precisely (0.3).

Up to swapping the two marked supports, the six global marked rows are

| fibre `t_1` | fibre `t_2` | unmarked positive partition |
|---|---|---|
| `3` | `3` | `3+3` |
| `3` | `2+1` | `3+2+1` |
| `3` | `1+1+1` | `3+1+1+1` |
| `2+1` | `2+1` | `2+2+1+1` |
| `2+1` | `1+1+1` | `2+1+1+1+1` |
| `1+1+1` | `1+1+1` | `1+1+1+1+1+1` |

The previous global identity `sum_j m_j=6` follows by adding (2.2), but loses
the marked information.  In particular `2+2+2` cannot be split into two
positive mass-three clusters and is now excluded.  Nothing here bounds the
number of `m_j=0` vertices.

## 3. The actual morphic forest forces additive fibres

Write a marked Kodaira fibre on `S` as

```text
F_i=sum_k a_k Theta_k,                     a_k>0.
```

In (2.1), the coefficient of the strict transform `Theta_k^Y` is exactly
`-a_k`: the relative canonical divisor contains only `h`-exceptional curves.
Every `Theta_k^Y` is therefore in the `r`-exceptional locus.  The first-leg
image misses its contraction point, so the complete good-resolution transform
of the fibre is boundary in an actual proper block.

The morphic rational-forest theorem now excludes all semistable cases:

- `I_0` contains a smooth genus-one component;
- `I_1` becomes a cycle after resolving its node: the rational strict
  transform and the node exceptional meet by two edges;
- `I_n`, `n>=2`, already has cyclic reduced dual graph.

Thus each marked fibre is one of

```text
II, III, IV, I_n* (n>=0), IV*, III*, II*.               (3.1)
```

All components of these additive fibres are rational and their embedded
strict-SNC resolutions are trees.  This makes (3.1) necessary, not sufficient:
higher jets or extra exceptional curves may still create forbidden topology.

## 4. Exact 25-pair global table

For an additive Kodaira fibre, let `delta` be its minimal discriminant order
and `r` its root rank.  In characteristic zero,

| type | `delta` | `r` | lower `v(c4)` | lower `v(c6)` |
|---|---:|---:|---:|---:|
| `II` | 2 | 0 | 1 | 1 |
| `III` | 3 | 1 | 1 | 2 |
| `IV` | 4 | 2 | 2 | 2 |
| `I0*` | 6 | 4 | 2 | 3 |
| `I1*` | 7 | 5 | 2 | 3 |
| `I2*` | 8 | 6 | 2 | 3 |
| `IV*` | 8 | 6 | 3 | 4 |
| `I3*` | 9 | 7 | 2 | 3 |
| `III*` | 9 | 7 | 3 | 5 |
| `I4*` | 10 | 8 | 2 | 3 |
| `II*` | 10 | 8 | 4 | 5 |

Here `r=delta-2`.  A rational elliptic surface has total discriminant degree
twelve and Picard rank ten.  Shioda--Tate gives total fibre-root rank at most
eight.  For the two marked additive fibres these two tests coincide:

```text
delta_1+delta_2<=12,
r_1+r_2=delta_1+delta_2-4<=8.                           (4.1)
```

The 25 unordered symbol pairs satisfying (4.1) are:

| pair | `delta_1+delta_2` | remaining discriminant degree | lower `(v4 sum,v6 sum)` |
|---|---:|---:|---:|
| `II + II` | 4 | 8 | `(2,2)` |
| `II + III` | 5 | 7 | `(2,3)` |
| `II + IV` | 6 | 6 | `(3,3)` |
| `II + I0*` | 8 | 4 | `(3,4)` |
| `II + I1*` | 9 | 3 | `(3,4)` |
| `II + I2*` | 10 | 2 | `(3,4)` |
| `II + IV*` | 10 | 2 | `(4,5)` |
| `II + I3*` | 11 | 1 | `(3,4)` |
| `II + III*` | 11 | 1 | `(4,6)` |
| `II + I4*` | 12 | 0 | `(3,4)` |
| `II + II*` | 12 | 0 | `(5,6)` |
| `III + III` | 6 | 6 | `(2,4)` |
| `III + IV` | 7 | 5 | `(3,4)` |
| `III + I0*` | 9 | 3 | `(3,5)` |
| `III + I1*` | 10 | 2 | `(3,5)` |
| `III + I2*` | 11 | 1 | `(3,5)` |
| `III + IV*` | 11 | 1 | `(4,6)` |
| `III + I3*` | 12 | 0 | `(3,5)` |
| `III + III*` | 12 | 0 | `(4,7)` |
| `IV + IV` | 8 | 4 | `(4,4)` |
| `IV + I0*` | 10 | 2 | `(4,5)` |
| `IV + I1*` | 11 | 1 | `(4,5)` |
| `IV + I2*` | 12 | 0 | `(4,5)` |
| `IV + IV*` | 12 | 0 | `(5,6)` |
| `I0* + I0*` | 12 | 0 | `(4,6)` |

Equivalently, before the order-eight, -nine and -ten symbols are refined,
there are 19 unordered discriminant-order pairs:

```text
(2,2),(2,3),(2,4),(2,6),(2,7),(2,8),(2,9),(2,10),
(3,3),(3,4),(3,6),(3,7),(3,8),(3,9),
(4,4),(4,6),(4,7),(4,8),(6,6).                         (4.2)
```

The seven rows with zero remaining discriminant degree are the cheapest
global cells: `II+I4*`, `II+II*`, `III+I3*`, `III+III*`, `IV+I2*`,
`IV+IV*`, and `I0*+I0*`.

## 5. Global invariant-degree refinements

For the minimal rational elliptic surface,

```text
c4_min in H0(P1,O(4)),       c6_min in H0(P1,O(6)).     (5.1)
```

Therefore a nonzero `c4_min` has total vanishing order four and a nonzero
`c6_min` has total vanishing order six.  The lower orders in the last column
of Section 4 force

```text
II+II* or IV+IV*     => c4_min identically zero,
III+III*             => c6_min identically zero.        (5.2)
```

These are not contradictions.  If `c4_min=0`, then `j=0`, and the allowed
additive types are `II,IV,I0*,IV*,II*`; exactly nine pairs from Section 4
remain:

```text
II+II, II+IV, II+I0*, II+IV*, II+II*,
IV+IV, IV+I0*, IV+IV*, I0*+I0*.                        (5.3)
```

If `c6_min=0`, then `j=1728`, and exactly four pairs remain:

```text
III+III, III+I0*, III+III*, I0*+I0*.                   (5.4)
```

When neither invariant vanishes identically, the actual orders, not merely
the displayed lower bounds, must fit the degree budgets (5.1).  This is a
finite open/closed refinement of the 25 rows.

## 6. CFS slopes, tangent cones and the five additive reductions

Work over `C[[tau]]` at one marked support.  The generic ternary cubic is
soluble, so its minimal level is zero.  An exact level-one integral model
with coefficient valuation zero is nonminimal.  Cremona--Fisher--Stoll
Theorem 4.3 and Lemma 4.4 imply that, after integral coordinate equivalence,
one of the four nontrivial canonical pairs

```text
(a,b)=(0,1),(1,1),(1,2),(2,3)                          (6.1)
```

is admissible:

```text
tau^(a+b+1) divides Phi(x,tau^a*y,tau^b*z).             (6.2)
```

Then

```text
H=tau^(-a-b-1) Phi(x,tau^a*y,tau^b*z)                  (6.3)
```

is integral of level zero.  Pair `(0,0)` is absent because the original
coefficient valuation is zero.  This is an exhaustive four-slope split; it
does not say that the raw global degree cap survives the integral gauges.

For `(a,b)=(1,1)`, reverse (6.3) and work in the affine chart `x=1`:

```text
Phi=tau^3 H(1,y/tau,z/tau).
```

The ordinary degree-three tangent form in `(y,z,tau)` is

```text
TC(Phi)=H_0(tau,y,z).                                  (6.4)
```

Thus the projectivized tangent cone is a smooth plane cubic exactly when the
lowered special cubic `H_0` is smooth.  The ordinary blowup then has that
smooth cubic as exceptional divisor and resolves along it, exposing a
genus-one boundary component.

For each positive-`a` pair in (6.1), use the weighted blowup of affine
`(y,z,tau)` with weights `(a,b,1)`.  Its initial face has weighted degree

```text
a+b+1=a+b+1=sum of the weights.                         (6.5)
```

On the chart `tau!=0` its equation is `H_0(1,Y,Z)=0`.
If `H_0` is smooth, the normalization of the complete weighted face is
birational to `H_0` and has genus one.  Hence good reduction is excluded in
all three positive-slope cells, while the `(0,1)` cell is already excluded
in the good case by the contracted minimal elliptic fibre in Section 3.

If the minimal fibre is multiplicative, its regular model is `I_n`; Section
3 supplies the cycle independently of presentation.  If it is additive,
`c4(H_0)=c6(H_0)=0`, so the nonzero reduced ternary cubic is one of the five
nullcone orbits

| orbit | representative | singular locus |
|---|---|---|
| cusp | `y^2*z-x^3` | point |
| conic plus tangent | `x*(x*z-y^2)` | point |
| three concurrent lines | `x*y*(x-y)` | point |
| double line plus line | `x^2*y` | line |
| triple line | `x^3` | line |

The first three reduced supports resolve as rational trees.  The last two
are nonreduced and higher jets are load-bearing.  The actual Kodaira list in
Section 4 is the invariant way to retain only rational-tree minimal fibres;
the nullcone label alone does not determine the complete defect resolution.

Combining (0.3), (4.1), (6.1) and this five-orbit list gives a finite local/
global skeleton.  It is not legitimate to choose the gauges independently at
the two supports: they must reconstruct one raw global class-`(3,3)` cubic.

## 7. Literal raw-degree-three additive control

The additive branch is nonempty locally within the campaign's literal degree
cap.  Put

```text
H=y^2*z-x^3-tau*x*z^2,
Phi=tau^3 H(x/tau,y/tau,z)
   =tau*y^2*z-x^3-tau^3*x*z^2.                         (7.1)
```

The section is `[0:1:0]`.  The lowered model is the minimal Weierstrass
equation

```text
y^2*z=x^3+tau*x*z^2,
```

with

```text
c4=-48*tau,       c6=0,       Disc=-64*tau^3.           (7.2)
```

It has Kodaira type `III`.  The reverse transformation raises the invariant
orders by `(4,6,12)`, so `Phi` has exact CFS level one and orders
`(5,infinity,15)`.

The generic cubic is smooth.  At `tau=0`, the total-space singular points are

```text
p=[0:0:1],             q=[0:1:0].                       (7.3)
```

At `q`, the local equation has leading form `tau*z-x^3`, and the splitting
lemma gives an `A_2` rational double point.  At `p`, in `z=1`, the equation is

```text
tau*y^2-x^3-tau^3*x,
```

with projectivized ordinary tangent cone the cuspidal cubic
`tau*y^2-x^3=0`.  Blowing up `p` in the `tau` chart gives the type-`III`
Weierstrass surface `Y^2-X^3-tau*X=0`; resolving its `A_1` point and making
the reduced fibre strict SNC produces only rational curves and a tree.  Both
singularities are isolated, so the hypersurface is `S_2+R_1` and normal.

Thus (7.1) passes exact level, solubility, normality, additive fibre topology,
rational-forest topology and the literal local base-degree-three cap.  It is
only a local DVR model.  It does not glue two supports, define a finite target
projection, or occur in a proper block.

## 8. Exact finite successor

The next family-wide computation should be organized as follows.

1. Mark `t_1,t_2` and retain one of the three mass partitions (0.3) at each.
   Keep zero-multiplicity resolution vertices and proximity data.
2. At each support run the four admissible CFS slopes (6.1) through the five
   additive nullcone reductions.  Record every integral gauge rather than
   truncating a gauged series as though it were raw.
3. Reconstruct one global raw family

   ```text
   F=F_0+tF_1+t^2F_2+t^3F_3
   ```

   in a single coefficient-base frame.  Impose the same section, generic
   smoothness, total-space normality, finite target projection, the two exact
   level-one principal opens and one of the 25 Kodaira rows.
4. Start with the seven zero-remainder rows in Section 4, then the `j=0` and
   `j=1728` strata.  Their global invariant divisors are most rigid.
5. A surviving normal rational surface is still only a surface control.
   Compute the complete source ramification divisor, its normalization genera
   and boundary incidence before testing the actual first-leg image.

The symbolic problem is finite but the two local frames are coupled.  If its
elimination grows, freeze the exact coefficient ring, gauges, opens and
planted control (7.1) before moving it to AWS.

## 9. Desk replay

The replay is

```text
ops/bd_a2_d3_sectioned_two_support_universal_dichotomy_replay.py
SHA-256 f87d30f1b6424ad414237adb82edc85e64be9fe334488f517674c608f8d6bc24
```

It enumerates the 25 symbol pairs and 19 order pairs, the six marked cluster
pairs, the invariant-zero sublists, the four CFS slopes, and the exact
additive control (7.1).  It has zero Python AST `assert` nodes.

```bash
d3u_tmp=$(mktemp -d)
python3 ops/bd_a2_d3_sectioned_two_support_universal_dichotomy_replay.py \
  > "$d3u_tmp/ordinary.json"
python3 -O ops/bd_a2_d3_sectioned_two_support_universal_dichotomy_replay.py \
  > "$d3u_tmp/O.json"
python3 -OO ops/bd_a2_d3_sectioned_two_support_universal_dichotomy_replay.py \
  > "$d3u_tmp/OO.json"
cmp "$d3u_tmp/ordinary.json" "$d3u_tmp/O.json"
cmp "$d3u_tmp/ordinary.json" "$d3u_tmp/OO.json"
wc -c "$d3u_tmp/ordinary.json"
shasum -a 256 "$d3u_tmp/ordinary.json"
```

The three outputs are byte-identical, 7031 bytes, with SHA-256

```text
7291c3dec807f590d33a2d2e527595f46ede63f0a918a4a26bd7c0159f9fb448.
```

The mutation

```bash
python3 ops/bd_a2_d3_sectioned_two_support_universal_dichotomy_replay.py \
  --mutate-local-control
```

exits nonzero with

```text
FAIL:reverse-(1,1) local control identity failed
```

The report layer, not the replay, proves the discrepancy intersection,
Kodaira/forest classification, Shioda--Tate bound, invariant line-bundle
degrees and weighted-face birational statement.

## 10. Firewalls and nonclaims

- This report does not eliminate the sectioned two-support row or decide JC2.
- A surface control is not a proper block, and a local DVR control is not a
  global surface.
- A smooth tangent cone is proved only in the corresponding lowered-good
  cell; exact level one does not force it.
- A nullcone label does not determine the complete resolution graph.
- The 25 Kodaira pairs and six cluster pairs are necessary lists, not
  occurrence claims.
- The two local CFS gauges cannot be selected independently of the single raw
  global degree-three presentation.
- Zero plane-net multiplicity is not equivalent to crepant/ADE discrepancy.
- Boundary topology is invoked only through the actual everywhere-defined
  morphic first leg, never through rational domination.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18645`.
- Body SHA-256:
  `1f274a7dc93e70e9eea171036e6e9ff790b50e9d4776b5d4076758fd0f0517a1`.
- Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`.
