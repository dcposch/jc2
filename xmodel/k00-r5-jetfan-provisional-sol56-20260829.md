# K00 V20R2 valuation five: leading jet fan and grade-19 residual locus

Author: Sol 5.6 research lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `PROVISIONAL EXACT PARTIAL EXCLUSION / RESIDUAL LOCUS OPEN`

## 0. Result

For exact transverse valuation five in the normalized V20R2 K00 source,
the leading rank-two and leading rank-one cells are empty by grade 14.
Both exclusions are field-valued characteristic-zero statements and hold
after algebraic closure.  They use two literal raw-row cokernel identities,
not a period or renormalization inference.

The leading rank-zero cell is not closed here.  It is exactly the old plane

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),       (s,t)!=(0,0),
```

and grade 12 sends the next coefficient back to the same reduced quadratic
cone.  The remaining grades 13 through 19 form the precisely typed
constructible locus `K00-R5-R0-RESIDUAL/v1` in Section 6.  On that locus the
terminal contracted equation is the genuine two-term K10/K6 problem

```text
[Lambda^19](p10 D10+p6 D6)=5 Jdet[0].
```

This package does **not** decide whether the intersection with
`D(Jdet[0])` is empty.  Thus valuation five is reduced, not excluded and not
attained.  The residual is mathematical elimination work; it is not blocked
by a missing source type.

## 1. Literal source and true valuation-five calendar

Write

```text
d=Lambda^5 x+Lambda^6 y+Lambda^7 z+Lambda^8 w+...,
p10=Lambda^2 k10,       k10[0]=kappa != 0,
p6 =Lambda^6 k6,        k6[0]=0,
p2 =Lambda^10 k2,       k2[0]=0.
```

The five boundary zeros for `k6,k2,mu2,mu4,mu6` are substituted before
coefficient extraction.  In particular `p6` starts at grade 7 and `p2`
starts at grade 11.  Direct reconstruction of the 569 frozen tails gives
the following first possible arrivals:

| literal sector | transverse degree | first grade |
|---|---:|---:|
| unloaded `Q` | 2 | 10 |
| K10 `M4` | 2 | 12 |
| K6 linear part | 1 | 12 |
| unloaded cubic | 3 | 15 |
| `mu2` target | 0 | 15 |
| K2 linear part | 1 | 16 |
| K10 cubic | 3 | 17 |
| K6 quadratic | 2 | 17 |
| `mu4` target | 0 | 17 |
| `mu6` and `Jdet` targets | 0 | 19 |

For the exact contracted identity, `D10,D6,D2` have respective minimum
transverse degrees `3,2,2`.  Therefore through grade 19 only

```text
p10 D10, p6 D6, -Lambda^19 Jdet*h/4
```

can occur; `h(0)=20`.  Contracted grades 17 and 18 set the two load terms
to zero, while grade 19 gives the displayed terminal equation.  No target
or load is moved to an earlier grade in this analysis.

## 2. Leading cone and rank fan

The grade-10 equations are the same literal unloaded quadrics as quadrics,
not by a shift claim.  Put

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4.
```

Their reduced field-valued zero locus is `A=B=0`, parameterized by

```text
x=(2b+2u,a,b,8a+v,b-u,16a+4v).
```

The exact differential is

```text
DQ_i(x)[q]=alpha_i(x) A(q)+beta_i(x) B(q),
```

with

```text
i     alpha_i                       beta_i
1     (3/1024)u                    -(3/1024)v
2     (3/256)v                      (3/16384)u
3    -(3/8192)u                     (3/8192)v
4      0                              0
5    -(3/131072)u                   (3/131072)v
6      0                              0
7    -(3/1048576)u                  (3/1048576)v.
```

Every nonzero two-by-two minor is a nonzero rational multiple of

```text
Delta=u^2+64v^2.
```

Hence the leading fan has exactly rank two (`Delta!=0`), rank one
(`Delta=0,(u,v)!=(0,0)`), and rank zero (`u=v=0`).  This is a reduced
field-valued split only; no nilpotent scheme claim is made.

## 3. Leading rank two is empty at grade 14

Assume `Delta!=0`.  Grade 11 forces

```text
A(y)=B(y)=0.
```

The K6 linear row-vector vanishes on this four-plane.  At grade 12 the
K10 quadratic inhomogeneity is in the image of `DQ(x)` and fixes exactly

```text
A(z)= (10/3) kappa v,
B(z)=-(10/3) kappa u,
```

leaving the four-dimensional common kernel free.  Grade 13 is again
solvable in the image.  If the rank parameters of `y` are denoted
`(u_y,v_y)` and `k10[1]=kappa_1`, it fixes

```text
A(w)= (10/3)(kappa v_y+kappa_1 v),
B(w)=-(10/3)(kappa u_y+kappa_1 u),
```

again with arbitrary common-kernel additions.

At grade 14, remove the new `DQ(x)` image term and call the remaining
seven-vector `E`.  The free common-kernel additions, `kappa_1`, `k10[2]`,
and the dormant K6 coefficient all cancel from the following two exact
cokernel rows:

```text
E_4                 = (25 kappa^2/131072)(64v^2-u^2),
E_3+(1/8)E_1        = (25 kappa^2/4096)uv.
```

Both must vanish.  Since `kappa!=0`, they imply `uv=0` and
`u^2=64v^2`, hence `u=v=0`.  This contradicts `Delta!=0`.  Thus the full
leading rank-two cell is empty by grade 14.

## 4. Leading rank one is empty at grade 14

Over an algebraic closure write

```text
u=epsilon 8 i v,       epsilon in {+1,-1},       v!=0.
```

Grade 11 says `B(y)=epsilon 8i A(y)`.  Write

```text
A(y)=lambda v,       B(y)=epsilon 8i lambda v.
```

The zero-image row 4 at grade 12 is

```text
-(3/4096)v^2 lambda^2=0.
```

Thus `lambda=0`, so `y` lies in the common four-plane `A=B=0`.  Grade 12
then fixes one normal combination of `z`; retain its tangent freedom as
`tau`:

```text
A(z)=(10/3)kappa v+tau v,
B(z)=-(10/3)kappa u+epsilon 8i tau v.
```

After the grade-13 image solve, all kernel freedoms and dormant load
coefficients again disappear from two grade-14 cokernel rows:

```text
E_4 = (v^2/4096)(-3tau^2+100kappa^2),

E_3+(1/8)E_1
    = epsilon i (v^2/2048)(3tau^2+100kappa^2).
```

Their simultaneous vanishing gives both
`3tau^2=100kappa^2` and `3tau^2=-100kappa^2`.  In characteristic zero this
forces `kappa=0`, contrary to the source unit.  Both conjugate rank-one
branches are therefore empty at grade 14.

## 5. Leading rank zero and the exact next gate

Rank zero gives

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),       (s,t)!=(0,0).
```

Direct literal reconstruction verifies, for every `(s,t)`,

```text
Q(x)=0,       DQ(x)=0,       C3(x)=0,
M4(x)=0,      L6(x)=0.
```

Consequently grades 10 and 11 vanish and grade 12 is exactly

```text
Q(y)=0.
```

Its reduced field-valued locus is again `A(y)=B(y)=0`, with the same
rank-two/rank-one/rank-zero fan.  This is a literal second cone, not a
period theorem: subsequent arrival grades differ because `mu2`, `mu4`,
`mu6`, and `Jdet` enter at 15, 17, 19, and 19.

## 6. Precisely typed residual through grade 19

`K00-R5-R0-RESIDUAL/v1` is the following constructible coefficient locus
over a characteristic-zero field:

```text
x=ell(s,t),                         (s,t)!=(0,0),
d=Lambda^5 x + sum_{n=6}^{14} Lambda^n d[n] mod Lambda^20,

k10=sum_{j=0}^{7} k10[j] Lambda^j,  k10[0]!=0,
k6 =sum_{j=1}^{8} k6[j] Lambda^j,
k2 =sum_{j=1}^{4} k2[j] Lambda^j,

mu2=sum_{j=1}^{5} mu2[j] Lambda^j,
mu4=sum_{j=1}^{3} mu4[j] Lambda^j,
mu6=mu6[1] Lambda,
Jdet=Jdet[0],                        Jdet[0]!=0,

Q(d[6])=0,
[Lambda^g] Phi_i=0                  (i=1,...,7; g=13,...,19).
```

Every `Phi_i` here is the literal frozen-tail row after the V20R2 affine
coordinate map and honest load shifts.  The listed coefficient ranges are
exactly the ranges that can reach grade 19; no omitted later coefficient can
change one of these equations.  The canonical text of this specification
has SHA-256

```text
b2488b33365e6bfeb1fe031b76386d8c2a6293cf42e7727765fc3d6521514498.
```

The next producer should split `d[6]` by its same three rank cells and
eliminate grades 13 through 19, retaining `Jdet[0]` as an open rather than
normalizing it prematurely.  The contracted grades 17--19 should be used as
a scalar prepass, but the raw odd-row cokernels must remain because the even
targets arrive during this window.

This residual locus is called "surviving" only in the campaign sense that
the present exact identities do not eliminate it.  This report does not
assert it has a field-valued point, a compatible arc, or a map.

## 7. Replay, controls, and resource class

Run from the repository root:

```text
python3 xmodel/k00-r5-jetfan-replay-sol56-20260829.py
```

Observed clean run:

```text
K00_R5_JETFAN_REPLAY=PASS
TAIL_TERM_COUNT=569
NONZERO_LEADING_RANK2_MINORS=4
RANK2_GRADE14=EMPTY_BY_ROW4_AND_S3
RANK1_GRADE12=TANGENT_PARAMETER_ZERO
RANK1_GRADE14=EMPTY_BY_ROW4_AND_S3
RANK0_GRADE12=NEXT_REDUCED_QUADRATIC_CONE
RANK0_RESIDUAL_SPEC_SHA256=b2488b33365e6bfeb1fe031b76386d8c2a6293cf42e7727765fc3d6521514498
MUTATION_CONTROLS=PASS
runtime about 0.54 seconds; maximum RSS about 15 MB
```

The replay uses standard-library exact rational/Gaussian-rational sparse
polynomials.  It reconstructs all 569 tails, rechecks the leading cone and
rank minors, and verifies every displayed rank-one/rank-two identity with
arbitrary intermediate kernel variables.  Controls detect a one-byte source
mutation, a wrong K10 sign in the grade-14 inhomogeneity, and the forbidden
`k6[0]` boundary mutation (which would falsely move the first K6 arrival
from grade 12 to grade 11).

No Singular process, AWS resource, web request, or external model was used.

## 8. Nonclaims and custody

This is a partial finite-jet theorem inside the normalized K00/V20R2
source.  It does not exclude the rank-zero residual, prove its nonemptiness,
infer a recurrence in valuation, identify a finite jet with a formal or
algebraic arc, change support or normalization, or imply a polynomial Keller
map, counterexample, or JC2.

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json

2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py

2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py

eb8513b622e9c6fa839f9f20f32ff4c4fc9207a8591cdb6b292ab141f159522b
  xmodel/k00-r5-jetfan-replay-sol56-20260829.py
```

Only this new report and its new replay were created.  No canonical or
existing artifact was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10113`.
- Body SHA-256:
  `cdd37ff2f2c7fa07803105c57dca34d56ffe159b77afd29fb0e5644b6f67517a`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
