# K00 V20R2 valuation four: exact leading fan and typed residual

Author: Sol 5.6 research lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM / DIFFERENT-MODEL REVIEW REQUIRED`

## 0. Result

On the exact normalized V20R2 source over a characteristic-zero field, let

```text
d = Lambda^4 x + Lambda^5 y + Lambda^6 z + ...,
x != 0,
C6=1,
k10[0]=kappa != 0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0.
```

The full reduced leading cone again has ranks zero, one, and two for
`DQ(x)`. Exact literal expansion, without a period or renormalization
inference, gives:

1. every leading rank-one point dies at grade 12;
2. every leading rank-two point dies at grade 12;
3. hence every grade-19 survivor must have leading coefficient on the old
   plane;
4. on that plane, every next-coefficient rank-one point dies at grade 15;
5. on the next-coefficient rank-two stratum, grade 15 necessarily restricts
   the cone parameters to `u=0` or `u^2=192v^2`.

Thus the valuation-four problem is not closed, but its exact residual is now
the disjoint union of two named constructible packets:

```text
R4-00: x is old-plane rank zero and y is old-plane rank zero;

R4-02: x is old-plane rank zero, rank DQ(y)=2, and
       u_y(192 v_y^2-u_y^2)=0.
```

In both packets all literal coefficient equations through grade 19 remain
imposed.  No compatible point in either packet is asserted.  This is a
strict narrowing result, not a valuation-four exclusion.

## 1. Source reconstruction and literal grade calendar

The replay reconstructs the seven affine rows directly from the frozen 569
tails under

```text
C0=(1+d0)/256,  C1=d1,       C2=(1+d2)/16,
C3=d3,          C4=(3+d4)/8, C5=d5,          C6=1.
```

Write the homogeneous pieces of the unloaded rows as `Q,C3,C4,...`, and
those of the three load vectors as `M2,M3,...`, `N1,N2,...`, and
`P1,P2,...`.  For exact valuation four the complete first-arrival calendar
through grade 19 is

| literal source | first homogeneous arrivals |
|---|---|
| unloaded | `Q:8`, `C3:12`, `C4:16` |
| `Lambda^2 k10` | `M2:10`, `M3:14`, `M4:18` |
| `Lambda^6 k6`, with `k6[0]=0` | `N1:11`, `N2:15`, `N3:19` |
| `Lambda^10 k2`, with `k2[0]=0` | `P1:15`, `P2:19` |
| row-2 target | `mu2[1]:15` through `mu2[5]:19` |
| row-4 target | `mu4[1]:17` through `mu4[3]:19` |
| row-6 target | `mu6[1]:19` |
| row-7 target | `Jdet[0]/4:19` |

Each later coefficient of a load shifts its listed arrival by its series
index.  This table is raw seven-row bookkeeping.  It is deliberately not the
contracted minimum-degree calendar: for example `N1` occurs in the raw
source but vanishes on the reduced leading cone.  No load is silently
discarded in the exact coefficient definition

```text
G_i,n = [Lambda^n](
    R_i(d)
  + Lambda^2  k10 M_i(d)
  + Lambda^6  k6  N_i(d)
  + Lambda^10 k2  P_i(d)) - target_i,n.
```

The residual packets mean exactly `G_i,n=0` for all `1<=i<=7` and
`8<=n<=19`, together with the displayed source opens and boundary zeros.

## 2. Leading cone and cokernel maps

For a vector `q=(q0,...,q5)`, set

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4.
```

The reduced leading cone is `A(x)=B(x)=0`, parameterized without a scale
normalization by

```text
x=(2b+2u, a, b, 8a+v, b-u, 16a+4v).
```

On it

```text
DQ_i(x)[q] = alpha_i(x) A(q) + beta_i(x) B(q),
Delta = u^2+64v^2,
```

and the rank fan is

```text
rank 0: u=v=0;
rank 1: Delta=0 and (u,v)!=(0,0);
rank 2: Delta!=0.
```

The grade-10 K10 inhomogeneity is always in this two-column image.  The exact
identity is

```text
M2(x) = DQ(x)[A=-10v/3, B=10u/3].
```

Consequently, on rank two, grades 9 and 10 give

```text
A(y)=B(y)=0,
A(z)=10 kappa v/3,
B(z)=-10 kappa u/3.
```

Grade 11 has zero cokernel projection.  At grade 12 the newest coefficient
again lies in `im DQ(x)`, so the five exact rank-two cokernel projections are
the relevant equations.  This gives a literal projection ledger through the
first obstruction, rather than treating raw rows as independent.

Once `x` has rank zero, grades 10 and 11 become

```text
Q(y)=0,
DQ(y)[z]=0.
```

Thus, on next rank one or two, grades 12 onward are projected to
`coker DQ(y)`.  On next rank zero that map vanishes; the correct residual is
the full coefficient fibre `G_i,n=0`, not an invented shifted copy of the
leading fan.  This is why `R4-00` is left as a separately typed packet.

## 3. Leading rank one dies at grade 12

Over an algebraic closure take the plus branch `u=8iv`, `v!=0`; the minus
branch is its conjugate. Grade 9 has one visible equation, so write

```text
A(y)=lambda,
B(y)=8i lambda.
```

A grade-10 cokernel row is

```text
-(9i/2097152) v lambda^2 = 0.
```

Therefore `lambda=0`: the next coefficient is on the reduced cone.  Include
the complete cone freedom in `y`, the particular grade-10 K10 correction in
`z`, and its remaining transverse scalar.  Row 6 at grade 12 is still the
exact unit

```text
G_6,12 = +(i/32)v^3.
```

It is nonzero.  The minus branch gives `-(i/32)v^3`.  Neither boundary-zero
load nor a target reaches row 6 in a way that changes this identity.

## 4. Leading rank two dies at grade 12

After the grade-9 and grade-10 solutions above, two grade-12 raw rows with
zero `DQ(x)` image are

```text
G_6,12 = u(192v^2-u^2)/65536,

G_4,12 = (3/32768) H4
         +(25 kappa^2/131072)(64v^2-u^2),

H4 = u^3-448uv^2+64bv^2-bu^2-1024auv.
```

The first equation splits rank two into two cases.

### 4.1 `u=0`

Here `v!=0`. Two further exact cokernel rows are

```text
G_3,12+(1/8)G_1,12   = (1/4)v^2(v+3a),
G_5,12+(1/128)G_1,12 = -(3/64)v^2(v+2a).
```

They force both `a=-v/3` and `a=-v/2`, impossible.

### 4.2 `u^2=192v^2`

Now `v!=0` and `Delta=256v^2`.  Put `r=u/v`, so `r^2=192`, and divide the
four nonzero rank-two projection minors by their recorded common powers of
`v`.  Exact Gaussian elimination over `Q[r]/(r^2-192)` has rank three and
RREF

```text
v = 0,
a = 0,
b + (25/12) kappa^2 = 0.
```

The first row contradicts `v!=0`.  The replay constructs the four rational
quadratic-field rows and checks this RREF coefficientwise.

## 5. Leading rank zero and the exact residual

Rank zero is the old plane

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),  (s,t)!=(0,0).
```

Grades 8 and 9 vanish and grade 10 is `Q(y)=0`.  Split the next coefficient
by the same reduced rank fan.

### 5.1 Next rank one dies at grade 15

On `u_y=+8iv_y`, grade 12 forces the following coefficient back onto the
cone.  Include that entire cone, the particular K10 correction two grades
later, and its one transverse freedom.  Direct literal expansion gives

```text
G_6,15 = +(i/32)v_y^3.
```

The conjugate branch gives the negative.  The identity is independent of
`s,t`, all displayed cone/kernel variables, the transverse freedom, and the
available raw `k6[1]` and `k2[1]` columns.  Hence next rank one is empty.

### 5.2 Next rank two narrows but remains open

On `Delta_y!=0`, grade 11 puts `z` on the cone and grade 12 has the exact
particular solution

```text
A(w)=10 kappa v_y/3,
B(w)=-10 kappa u_y/3.
```

At grade 15 row 6 is identically

```text
G_6,15 = u_y(192v_y^2-u_y^2)/65536.
```

Thus a survivor lies only on

```text
u_y=0, v_y!=0,
```

or

```text
u_y^2=192v_y^2, v_y!=0.
```

Other grade-13--15 cokernel rows, and all grade-16--19 rows, remain imposed
in `R4-02`.  This report does not claim those two branches are nonempty or
empty.

### 5.3 Next rank zero

Here

```text
y=ell(s1,t1).
```

The first nontrivial successor equation is the exact grade-12 affine
quadratic system

```text
Q(z) + kappa polar_M2(x,z) = 0.
```

Its complete fibre, followed by grades 13--19, is `R4-00`.  It is not
replaced by a radical, a period-two copy, or a normalization of one
coefficient.  In particular, zero and nonzero solutions of the grade-12
system must both remain until a dedicated rank fan is reviewed.

## 6. Replay, controls, and custody

Run from the repository root:

```text
python3 xmodel/k00-r4-jetfan-replay-sol56-20260829.py
```

The replay uses only Python's standard library and exact `Fraction` or
Gaussian-rational arithmetic.  It:

1. checks the tails, V20R2 compiler, and imported arithmetic-helper hashes;
2. rebuilds and checks all 569 tail weights and load linearities;
3. checks the raw homogeneous-degree calendar;
4. reconstructs the cone, `M2` image identity, rank-one units, rank-two
   branch rows, and quadratic-field RREF;
5. includes arbitrary cone/kernel/transverse variables in both rank-one
   units rather than evaluating a zero-tail sample;
6. verifies the next-rank-two grade-15 row including the available `k6[1]`
   and `k2[1]` columns; and
7. detects the in-memory mutation `192 -> 193` in the load-bearing row-six
   cubic.

Observed clean output:

```text
K00_R4_JETFAN_REPLAY=PASS
TAIL_TERM_COUNT=569
LEADING_RANK1_G12=EMPTY
LEADING_RANK2_G12=EMPTY
LEADING_RANK0_NEXT_RANK1_G15=EMPTY
RESIDUAL=LEADING_RANK0_NEXT_RANK0_OR_RANK2
LITERAL_WINDOW=GRADES_8_THROUGH_19
MUTATION_CONTROLS=CUSTODY_AND_ROW6_192_TO_193
RUNTIME_SECONDS=3.899820
```

Custody:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json

2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py

2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py

196b693a24914469a70feb4349b2c60465a45c1f98ed677e93a3698b6d03e6ee
  xmodel/k00-r4-jetfan-replay-sol56-20260829.py
```

The measured run is desk-scale and below the 60-CPU-second and 1-GiB caps.
No Singular process, AWS job, web request, external model, or Lean tree was
used.

## 7. Scope and nonclaims

This is a field-valued, reduced-rank, finite-jet narrowing theorem on the
exact normalized V20R2 support.  It does not establish scheme-theoretic
emptiness of a nonreduced rank cell.  It does not exclude `R4-00` or
`R4-02`, exact valuations three or five, another support/normalization, an
arc, an algebraic germ, a polynomial Keller map, a counterexample, or JC2.

The phrase “through grade 19” means that the residual packets retain every
literal equation through that grade; it does not mean that those residual
equations have been eliminated.  A finite point in either residual would
not itself be an arc or map.  Promotion requires a different model to rebuild
the rows and attack every displayed rank and branch calculation.

Only this report and its dedicated replay file were created.  No canonical
or existing artifact was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10719`.
- Body SHA-256:
  `3bb710d39c8fea9663bb1e6c1ed4d7c5b323a8741921b75aef2e8b844377bb40`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
