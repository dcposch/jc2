# K00 V20R2 valuation three: clean-room source and threat packet

Coordinator preflight: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: **EXACT SOURCE/PREFLIGHT PACKET — NOT A GRADE-19 PRODUCER**

## 0. Disposition

The normalized V20R2 valuation-three lane is correctly typed and has a
desk-scale exact first reduction.  Direct expansion from the frozen 569
tails, without using a valuation-two/four/five period claim, proves:

1. leading rank one and leading rank two are empty at grade 9;
2. leading rank zero is the old plane, and grade 8 sends the next coefficient
   to the same reduced quadratic cone;
3. the old-plane/next-rank-two cell is empty at grade 11;
4. the old-plane/next-rank-one cell is empty at grade 12; and
5. on the old-plane/next-rank-zero cell, grade 10 sends the third coefficient
   to the cone, after which K10 shifts the grade-11 linearization to a new
   effective rank fan.  Its effective rank-zero cell dies, while its two
   effective rank-one cells and effective rank-two cell remain.

Thus the complete unresolved cover after these deductions has three
geometric cells, bundled as

```text
R3-00-ER1(epsilon),  epsilon=+1,-1;
R3-00-ER2.
```

The effective-rank-one cells carry the remaining grade-12--19 equations and
the effective-rank-two cell does likewise.  No compatible
grade-19 point, formal arc, map, counterexample, or valuation-three
attainment is asserted.  The active producer must independently reconstruct
these identities and then decide or serialize the three residuals.

An external Grok primary lane emitted no report because its paid balance was
exhausted.  Its transient, unsealed output agreed that the leading nonzero
ranks die at grade 9 and the next nonzero ranks die by grade 12.  That is
operational corroboration only; no claim below consumes it as evidence.

## 1. Frozen source and literal normalization

The sole source is the reviewed V20R2 compiler, specialized at

```text
C0=(1+d0)/256,  C1=d1,       C2=(1+d2)/16,
C3=d3,          C4=(3+d4)/8, C5=d5,          C6=1.
```

The seven rows are

```text
Phi_l = R_l(d)
      + Lambda^2  k10 A10_l(d)
      + Lambda^6  k6  A6_l(d)
      + Lambda^10 k2  A2_l(d)
      - Lambda^(12+l) delta_l,

delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

Exact valuation three means

```text
d=Lambda^3 x+Lambda^4 y+Lambda^5 z+...,
x=(x0,...,x5) != 0.
```

Retain, without rescaling,

```text
k10[0]=kappa != 0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0.
```

The leading open is the honest cover

```text
D(x0) union ... union D(x5).
```

There is no licensed action here that sets one `xj`, `kappa`, or `Jdet[0]`
to one.  The five boundary zeros must be substituted before coefficient
extraction.  `Jdet` is the Jacobian source parameter, not either collision
ideal `J1` or `J2`.

Frozen source pins are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/
  aws_compile_v2_jsat/run/output/compiled_v2/tails.json

2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/
  compile_contracted_source_v20r2.py
```

The first file has 569 load-affine, weight-homogeneous tails and canonical
semantic digest `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`.

## 2. Minimal global coefficient projection

The full V20R2 jet has 164 free columns after its five boundary zeros.  After
imposing exact valuation three, only the following 122 columns can affect a
row through grade 19:

```text
d_j[n], j=0,...,5, n=3,...,16                 84
k10[n], n=0,...,11                             12
k6[n],  n=1,...,10                             10
k2[n],  n=1,...,6                               6
mu2[n], n=1,...,5                               5
mu4[n], n=1,...,3                               3
mu6[1]                                           1
Jdet[0]                                          1
                                                ---
                                                122
```

The omitted full-source columns are free affine factors invisible to grades
6--19; they are not zero.  A producer may use either this minimal projection
or the full source, but it must say which.  A minimal producer must replay the
dependency cutoff; a full producer must list the inert free factors.  Mixing
minimal ranges with implicit zero truncations is forbidden.

The literal coefficient packet has all 98 indexed root slots

```text
(l,g),  l=1,...,7,  g=6,...,19,
```

including any roots that are structurally zero.  Omitting a zero slot changes
the public row indexing and is not allowed.

## 3. Exact grade calendars

### 3.1 Rowwise homogeneous support

Direct reconstruction gives the following nonzero transverse degrees in
rows 1 through 7:

```text
R:    234 | 234 | 2345 | 2345 | 2345 | 3456 | 23456
A10:   23 | 234 |  234 |  234 | 2345 | 2345 | 2345
A6:    12 |  12 |  123 |   23 |  123 |  234 | 1234
A2:     1 |   1 |    1 |   12 |   12 |   12 |  123
```

These are actual supports after the K00 affine coordinate map, not only
degree floors.

### 3.2 Literal seven-row first arrivals

For homogeneous degree `q`, the first arrivals are

| source piece | first anchors through grade 19 |
|---|---|
| unloaded `R^[q]` | `q=2,3,4,5,6` at `6,9,12,15,18` |
| `k10[0] A10^[q]` | `q=2,3,4,5` at `8,11,14,17` |
| `k6[1] A6^[q]` | `q=1,2,3,4` at `10,13,16,19` |
| `k2[1] A2^[q]` | `q=1,2` at `14,17` |
| targets | `mu2[1]:15`, `mu4[1]:17`, `mu6[1]:19`, `Jdet[0]/4:19` |

Later `k10[j]` shifts the corresponding K10 anchor by `j`.  Later `k6[j]`
and `k2[j]` shift their displayed `j=1` anchors by `j-1`.  Coefficient
convolutions populate intermediate grades, so the producer must expand every
grade, not only this anchor table.

In particular, the literal K10 quadratic arrives at

```text
2+2*3=8,
```

the boundary-correct K6 linear term at `6+1+3=10`, and the boundary-correct
K2 linear term at `10+1+3=14`.

### 3.3 Contracted calendar is different

For

```text
Rmix = p10 D10+p6 D6+p2 D2
     + Lambda^14 mu2 u2+Lambda^16 mu4 u4+Lambda^18 mu6 u6
     - Lambda^19 Jdet h/4,
h=20+63d4,
```

the exact degree supports are

```text
D10: 3,4,5,6,7;  D6: 2,3,4,5;  D2: 2,3,4;
u2: 1,2,3;       u4: 1,2;      u6: 1.
```

At valuation three the anchors visible through grade 19 are

```text
D10^[3,4,5]: 11,14,17;
D6^[2,3,4]:  13,16,19;
D2^[2]:      17;
mu2*u2:      18;
-5 Jdet[0]:  19.
```

Later load coefficients again fill later grades.  Thus the contracted row is
a useful necessary scalar prepass, but cannot replace the raw seven rows.
The raw K10 quadratic arrives at grade 8 while contracted `D10` first arrives
at grade 11; raw K6 linear arrives at grade 10 while contracted `D6` first
arrives at grade 13.  This is the principal calendar mutation to reject.

## 4. Reduced leading cone and rank fan

Put

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4.
```

The original seven leading quadrics have reduced characteristic-zero
field-valued zero set `A(x)=B(x)=0`.  Parameterize it, without scale
normalization, by

```text
x=(2b+2u,a,b,8a+v,b-u,16a+4v).
```

On it

```text
DQ_i(x)[q]=alpha_i(x) A(q)+beta_i(x) B(q),
Delta=u^2+64v^2,
```

and the four nonzero `2 x 2` minors are nonzero rational multiples of
`Delta`.  Hence the complete reduced fan is

```text
rank 2: Delta != 0;
rank 1: Delta = 0, (u,v) != (0,0);
rank 0: u=v=0.
```

Over an algebraic closure the rank-one branches are

```text
u=epsilon*8*i*v,  v!=0,  epsilon=+1,-1.
```

This rank fan is only a field-valued constructible cover.  The producer must
retain the original quadrics if it makes any scheme or nilpotent claim.

## 5. Desk-scale exact deductions

All identities in this section are checked coefficientwise by the preflight
replay in Section 8.

### 5.1 Leading rank one and two die at grade 9

On rank two, grade 7 sends `y` to the cone and grade 8 has the exact normal
solution

```text
A(z)= (10/3) kappa v,
B(z)=-(10/3) kappa u.
```

At grade 9 the five cokernel rows are literally the already familiar cubic
vector, freshly reconstructed at valuation three.  In particular,

```text
G9_6 = u(192v^2-u^2)/65536,

G9_4 = (3/32768)
       (u^3-448uv^2+64bv^2-bu^2-1024auv).
```

The `u=0` branch forces `b=0` and then both `v+3a=0` and `v+2a=0`.  The
`u^2=192v^2` branch has the exact two quotient constants `1/8` and `-1/64`.
Both contradict rank two.

On rank one write

```text
A(y)=lambda*v,
B(y)=epsilon*8*i*lambda*v.
```

Grade 8 contains

```text
G8_4=-(3/4096)v^2 lambda^2,
```

so `lambda=0`.  After the complete grade-8 normal solve, including its
tangent parameter, row 6 at grade 9 is

```text
G9_6=epsilon*i*v^3/32,
```

which is nonzero.  Both conjugate branches die.  These are literal
coefficient identities, not a period inference from valuation two.

Therefore every valuation-three survivor has

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),  (s,t)!=(0,0).
```

### 5.2 The second cone and its rank-two kill

For `x=ell(s,t)`, grades 6 and 7 vanish and grade 8 is exactly

```text
Q(y)=0.
```

Split `y` by the same reduced rank fan.  On next rank two, grade 9 sends `z`
to the cone and grade 10 has the exact normal solution

```text
A(w)=2st+(10/3)kappa*v,
B(w)=s^2-64t^2-(10/3)kappa*u.
```

At grade 11 two cokernel rows are

```text
G11_3+(1/8)G11_1 = -(3/2048)D,
G11_4             = -(3/32768)F,

D=t*u^2-64t*v^2-2s*u*v,
F=s*u^2-64s*v^2+128t*u*v.
```

They satisfy

```text
sD-tF       = -2uv(s^2+64t^2),
sF+64tD     = (u^2-64v^2)(s^2+64t^2).
```

The nonisotropic and two isotropic source cases give the same exact
contradiction with `Delta_y!=0` as the displayed identities themselves.
Thus next rank two is empty at grade 11.

### 5.3 Next rank one dies at grade 12

Let

```text
u_y=epsilon*8*i*v_y,  v_y!=0.
```

Grade 9 writes the tangent part of `z` as

```text
A(z)=lambda*v_y,
B(z)=epsilon*8*i*lambda*v_y.
```

Grade 10 again gives `-(3/4096)v_y^2 lambda^2=0`, hence `lambda=0`.
The grade-10 normal solution for `w` has one tangent parameter `tau`:

```text
A(w)=2st+(10/3)kappa*v_y+tau*v_y,
B(w)=s^2-64t^2-(10/3)kappa*u_y
     +epsilon*8*i*tau*v_y.
```

At grade 11, row 4 forces

```text
s=epsilon*8*i*t,
```

so `t!=0`.  If `(u_z,v_z)` are the rank parameters of the cone coefficient
`z`, the remaining rank-one cokernel is

```text
(3/128) tau*v_y*v_z
+(epsilon*3i/1024) tau*v_y*u_z
-(5/128) tau*t*v_y*kappa
-(epsilon*5i/16) t^3*kappa = 0.
```

It forces `tau!=0` and then fixes one linear combination of `(u_z,v_z)`.
However, after retaining an arbitrary full grade-11 image solution and every
kernel/tangent and available load coefficient, row 6 at grade 12 is the exact
identity

```text
G12_6=epsilon*i*v_y^3/32.
```

This is nonzero on the rank-one open.  Both next-rank-one cells are therefore
empty at grade 12.  The grade-11 analysis remains in the replay specifically
to prevent a producer from skipping an intermediate compatibility equation.

### 5.4 Next rank zero: a third cone

For

```text
y=ell(a,b),
```

grade 9 vanishes.  Write `AZ=A(z)`, `BZ=B(z)`.  Two grade-10 identities are

```text
G10_1+8G10_3 = (3/2048) AZ*BZ,
G10_4        = (3/524288)(BZ^2-64AZ^2).
```

They force `AZ=BZ=0`; all seven grade-10 rows then vanish.

The next split is **not** the rank of `DQ(z)`.  At grade 11 the coefficient
`w=d[6]` also enters through the K10 quadratic polarization with the old-plane
coefficient `x`.  If `(u_z,v_z)` are the cone rank parameters of `z`, put

```text
U=u_z+(5/6)kappa*s,
V=v_z-(5/6)kappa*t,
Delta_eff=U^2+64V^2.
```

The complete grade-11 linear block in `(A(w),B(w))` factors with exactly the
same `alpha_i,beta_i` table as `DQ`, but evaluated at `(U,V)`.  Its four
nonzero minors are multiples of `Delta_eff`.  Splitting by `DQ(z)` would
therefore be an incomplete and generally wrong cover.

On effective rank zero, `U=V=0`, the inhomogeneous grade-11 rows include

```text
E11_1=(5kappa/4096)t(3s^2-64t^2),
E11_2=(5kappa/65536)s(s^2-192t^2).
```

They have no common solution on
`D(kappa) intersect (D(s) union D(t))`, so effective rank zero is empty.

On effective rank one write

```text
U=epsilon*8*i*V,  V!=0.
```

The sixth cokernel condition is exactly

```text
E11_2+(epsilon*i/2)E11_1
  =(5kappa/65536)(s+epsilon*8*i*t)^3.
```

It forces `s=-epsilon*8*i*t`, with `t!=0`.  The remaining image coordinate
is solvable on `D(V)`.  This defines `R3-00-ER1(epsilon)`, retaining every
literal equation at grades 12--19.

On effective rank two, `Delta_eff!=0`, all five grade-11 cokernel rows vanish
identically and both normal coordinates of `w` are solvable on
`D(Delta_eff)`.  This defines `R3-00-ER2`, again retaining grades 12--19.

## 6. Required producer case tree

The producer must cover, and either exclude or explicitly pass forward, all
of the following disjoint field-valued cells:

```text
L2                         killed at grade 9;
L1(+), L1(-)               killed at grade 9;
L0-N2                      killed at grade 11;
L0-N1(+), L0-N1(-)         killed at grade 12;
L0-N0, then E0             killed at grade 11;
L0-N0, then E1(+), E1(-)   -> R3-00-ER1(+), R3-00-ER1(-);
L0-N0, then E2             -> R3-00-ER2.
```

Here `L` and `N` denote the ranks of `DQ(x)` and `DQ(y)`.  `E` denotes the
grade-11 **effective** rank in `(U,V)`, not the rank of `DQ(z)`.  Zero
coefficients belong to rank-zero cells; they must not be lost by projectivizing
`y` or `z`.  Both conjugate rank-one branches must be replayed, even when one
is obtained formally by conjugation.

The producer should continue each of the three residual cells from grade 12
sequentially.  Every grade must be imposed before solving the next; the
valuation-five audit's missing grade-13 `tau*f` equation is the explicit
failure mode to prevent.  A rank change of a later linearization triggers a
fresh constructible split rather than a generic solve.

## 7. Minimal producer and replay contract

### Minimal remaining-rank-zero discriminator

The smallest honest successor discards all cells already killed above and
starts from exactly

```text
x=ell(s,t), (s,t)!=(0,0),
y=ell(a,b),
z=(2d+2u,c,d,8c+v,d-u,16c+4v),
U=u+(5/6)kappa*s,
V=v-(5/6)kappa*t.
```

It must independently replay grades 6--10, then form the complete grade-11
linear block and split

```text
E0: U=V=0;
E1(epsilon): U=epsilon*8*i*V, V!=0;
E2: U^2+64V^2!=0.
```

`E0` must close by the two displayed cubics.  On `E1(epsilon)`, impose
`s=-epsilon*8*i*t`, retain `D(t*kappa*V)`, solve the one image coordinate of
`w`, and project all seven grade-12 rows to its six-dimensional cokernel.  On
`E2`, retain `D(kappa*(U^2+64V^2))` together with
`D(s) union D(t)`, solve both normal coordinates of `w`, and project grade 12
to the five-dimensional cokernel.  Any surviving cell then proceeds one grade
at a time through 19.  This is the minimal
discriminator; jumping directly to grade 15 or to the contracted grade-19 row
would miss possible intermediate branch equations.

### Producer

1. Pin basis `31777ce9...`, tails, compiler, coordinate map, source columns,
   boundary zeros, target rows/signs/shifts, and `Jdet/4`.
2. Independently reconstruct the 569 tails and emit the 98 ordered literal
   roots for grades 6--19.  Do not import this preflight as an equation oracle.
3. Emit either the full exact-valuation-three locus or the 122-column minimal
   dependency projection, with a proved list of inert free factors.
4. Reconstruct the leading cone and every cell in Section 6.  In particular,
   derive the K10-shifted `(U,V)` fan rather than splitting by `DQ(z)`.  For
   every division, record the localizer (`v_y`, `V`, `Delta_y`, `Delta_eff`,
   `kappa`, or a source-open chart) and retain the complementary cell.
5. Use the contracted grades only as necessary scalar equations.  Replay all
   seven raw rows at every claimed solution or obstruction.
6. For an empty cell, emit a checkable exact identity, ideal-membership
   certificate, or complete localized Groebner certificate.  A proper
   aggregate superlocus or a nonzero normal form is not an emptiness proof.
7. For a surviving cell, serialize its literal coefficient equations,
   equalities, inequalities/localizers, variable order, and source map in a
   public canonical format.  Hash those exact public bytes, not a private
   shorthand.  State whether the serialization is full or minimal.
8. If elimination is heavy or uncertain, freeze and run it on AWS.  The
   source reconstruction and displayed preflight identities remain desk-scale.

### Independent replay

The replay must use a separately implemented tail/series evaluator and check:

- all source and artifact hashes plus the canonical semantic tail digest;
- the rowwise degree support, 98 root slots, 122-column dependency census,
  and dormant-frontier controls (`d[17]`, `k10[12]`, `k6[11]`, `k2[7]`);
- restriction of all five boundary-zero constants before extraction, with a
  negative unrestricted-source fixture for each;
- every displayed grade-6--11 identity with arbitrary kernel/tangent
  variables, not a zero-tail sample;
- both Gaussian conjugate branches and exact base-field descent wording;
- every grade-12--19 residual root after each substitution;
- the contracted residual against the literal combination
  `h*Phi7-sum u_i Phi_i` through grade 19; and
- any elimination certificate by direct substitution or ideal membership in
  the original seven-row presentation.

Mandatory mutations must alter or fail the result:

```text
valuation 3 -> 2 or 4;
raw K10 quadratic grade 8 -> contracted grade 11;
k6[0] or k2[0] resurrected;
target sign or Jdet/4 changed;
K10/K6/K2 load labels or contraction order swapped;
C0/C2/C4 affine normalization changed;
192 -> 193 in the grade-9 row-six cubic;
one D/F sign changed;
effective `(U,V)` replaced by the unshifted `(u_z,v_z)`;
one Gaussian branch omitted or its sign conjugated incorrectly;
one grade-12--19 equation deleted;
one claimed active frontier column deleted and one dormant column activated;
one residual localizer dropped;
public residual bytes changed without changing the claimed digest.
```

## 8. Preflight replay and custody

Run from the repository root:

```text
python3 xmodel/k00-r3-source-preflight-sol56-20260829.py
```

Observed output:

```text
K00_R3_SOURCE_PREFLIGHT=PASS
FROZEN_TAIL_TERMS=569
LITERAL_ROOT_SLOTS_GRADES_6_TO_19=98
MINIMAL_GLOBAL_ACTIVE_COLUMNS=122
LEADING_RANK1_AND_RANK2=EMPTY_AT_GRADE9
OLDPLANE_NEXT_RANK2=EMPTY_AT_GRADE11
OLDPLANE_NEXT_RANK1=EMPTY_AT_GRADE12
GRADE11_EFFECTIVE_RESIDUALS=R3-00-ER1_PLUS_MINUS,R3-00-ER2
PERIODICITY_ASSUMPTIONS=NONE
MUTATION_CONTROLS=CUSTODY,CALENDAR,EFFECTIVE_K10_SHIFT,CONJUGATE_SIGNS,192_COEFFICIENT
```

The replay SHA-256 is

```text
bac4b6888ccc27ba91b59ceacfbcadfcc3270dd386095218d51038f1d38486aa
```

It uses only standard-library exact rational/Gaussian-rational sparse
arithmetic and the byte-pinned valuation-two arithmetic engine
`2c918d5b...`.  Its observed runtime was under nine seconds in both ordinary
and optimized mode.  It writes no
file and starts no CAS, AWS, web, model, or formalization process.

## 9. Scope firewall

The deductions are field-valued finite-jet statements on one exact normalized
support.  They do not infer periodicity, scheme-theoretic emptiness, existence
of any residual point, lift a point to an arc, algebraize an arc, construct a
Keller map, exclude another support, or decide JC2.  A complete exclusion of
all three residual cells would exclude same-source valuation-three formal arcs
by truncation; a surviving finite jet would not itself be an arc or map.

No shared ledger, AWS resource, external lane, or `jc2-lean` path was touched
while preparing this packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19763`.
- Body SHA-256:
  `c2fffead93bdebdf017d6536fe6640cbf6ec93ed8a13a0477d90ed42c0efbdcd`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
