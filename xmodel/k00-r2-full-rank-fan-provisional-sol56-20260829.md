# K00 V20R2 valuation two: full reduced rank-fan exclusion

Author: Sol 5.6 research lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `PROVISIONAL_EXACT_DESK_THEOREM / DIFFERENT-MODEL REVIEW REQUIRED`

## 0. Result

On the exact normalized V20R2 K00 source over a characteristic-zero field,
there is no field-valued compatible jet of exact valuation two through
grade eight.

More precisely, retain

```text
C6=1,
k10[0]=kappa != 0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0] != 0,
d=Lambda^2 x+Lambda^3 y+Lambda^4 z+...,
x != 0.
```

The leading reduced quadratic cone has rank-zero, rank-one, and rank-two
strata for `DQ(x)`.  The rank-one and rank-two strata fail at grade six.
The rank-zero stratum is the previously named old plane.  On that plane the
next coefficient `y` again has rank-zero, rank-one, and rank-two strata; all
three fail at grade eight.  The last formerly open case, the rank-one
`Q(i)` branch, has a two-line hand obstruction.

This report upgrades the prior proposed `N-R` experiment to a provisional
exact theorem.  It also supplies two new grade-six exclusions outside the
old plane.  If a different model confirms the source reconstruction and all
six strata, the normalized V20R2 source will retain only valuations three,
four, and five: valuation one and every valuation at least six were already
promoted as impossible.  None of those remaining valuations is attained.

## 1. Exact source and replay boundary

The affine coordinates are

```text
C0=(1+d0)/256,  C1=d1,       C2=(1+d2)/16,
C3=d3,          C4=(3+d4)/8, C5=d5,          C6=1.
```

The seven rows are

```text
Phi_l = R_l(C,Lambda^2 k10,Lambda^6 k6,Lambda^10 k2)
        - Lambda^(12+l) delta_l,
delta=(0,mu2,0,mu4,0,mu6,Jdet/4).
```

The source open for exact valuation two is the named cover

```text
D(x0) union ... union D(x5),
```

not a normalization `x_j=1`.  The proof below obtains contradictions before
using `Jdet[0]`; its nonzero condition remains part of the licensed source.

Through grade eight, the target columns are absent.  Since `k6[0]=0`, the
first possible `Lambda^6 k6` contribution has grade at least nine; `k2`
starts later.  Only `kappa=k10[0]` can contribute to the displayed live
rows.  The replay also checks the identities that remove `d[6]`, `k10[1]`,
and `k10[2]` where they might superficially appear:

```text
DQ(ell)=0,  C3(ell)=0,  M4(ell)=0,
polar_M4(ell,y)=0 for every y on the reduced quadratic cone.
```

Here `Q`, `C3`, and `M4` are respectively the unloaded quadratic part, the
unloaded cubic part, and the quadratic part of the leading `k10` load.

The stdlib replay reconstructs these maps directly from the frozen 569-tail
JSON.  It does not import the compiler, use a CAS, call AWS, or write an
artifact.

## 2. The reduced leading cone and its exact rank fan

For a vector `q=(q0,...,q5)`, put

```text
A(q)=16 q1-4 q3+q5,
B(q)=q0-4 q2+2 q4.
```

The seven leading quadrics have reduced field-valued zero locus `A=B=0`.
Parameterize it without quotienting scale as

```text
x=(2b+2u, a, b, 8a+v, b-u, 16a+4v).
```

On this cone the exact differential factors rowwise as

```text
DQ_i(x)[q] = alpha_i(x) A(q) + beta_i(x) B(q),
```

where

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

All nonzero two-by-two minors are nonzero rational multiples of

```text
Delta=u^2+64v^2.
```

Thus the field-valued rank fan is exactly

```text
rank 0: u=v=0;
rank 1: Delta=0 and (u,v)!=(0,0);
rank 2: Delta!=0.
```

This is a reduced point-set statement.  No replacement of the original
seven-equation scheme by its radical is used for a nilpotent or multiplicity
claim.

## 3. Leading rank one dies at grade six

At grade four, `Q(x)=0`.  Grade five is `DQ(x)[y]=0`.  Row 6 of grade six is
independent of `y`, `z`, and every load:

```text
G6_6 = u(192v^2-u^2)/65536.
```

On rank one, over an algebraic closure,

```text
u=+8iv or u=-8iv,  v!=0.
```

Therefore

```text
G6_6=+(i/32)v^3 or G6_6=-(i/32)v^3,
```

which is nonzero.  Every leading rank-one valuation-two jet dies at grade
six.

## 4. Leading rank two dies at grade six

When `Delta!=0`, grade five forces `A(y)=B(y)=0`, hence every `Q_i(y)=0`.
Grade six is consequently

```text
DQ(x)[z] + C3(x) + kappa M4(x) = 0.
```

Rows 4 and 6 have zero `DQ(x)[z]` part.  After clearing nonzero rational
constants they give

```text
H6 = u(192v^2-u^2)=0,
H4 = u^3-448uv^2+64bv^2-bu^2-1024auv=0.
```

There are two cases.

### 4.1 `u=0`

Rank two gives `v!=0`, and `H4=0` gives `b=0`.  The row combinations whose
`DQ` parts vanish are then

```text
G6_3+(1/8)G6_1   = (1/4)v^2(v+3a),
G6_5+(1/128)G6_1 = -(3/64)v^2(v+2a).
```

They require both `a=-v/3` and `a=-v/2`, impossible for `v!=0`.

### 4.2 `u^2=192v^2`

Here `Delta=256v^2`, so `v!=0`.  Row 4 reduces to

```text
bv+2uv+8au=0.
```

The global quadratic syzygies provide two more zero-image combinations:

```text
S5=G6_5+(3/128)G6_1+(1/8)G6_3,
S7=G6_7+(1/512)G6_1+(1/128)G6_3.
```

In the localization at `v`, set `r=u/v`, `A0=a/v`, `K=kappa/v`.  Then
`r^2=192` and row 4 gives `b/v=-2r(1+4A0)`.  Exact reduction yields

```text
S5/v^3 =  1/8,
S7/v^3 = -1/64.
```

Either is a contradiction.  This closes the full leading rank-two stratum
at grade six.

## 5. Leading rank zero is the old plane

If `u=v=0`, write `s=b` and `t=8a`.  Then

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),  (s,t)!=(0,0).
```

Grades four and five vanish, and grade six becomes exactly `Q(y)=0`.
Parameterize its reduced field-valued locus as

```text
y=(2b+2u, a, b, 8a+v, b-u, 16a+4v)
```

and split again by `Delta_y=u^2+64v^2`.

## 6. Old-plane next rank two dies at grade eight

On `Delta_y!=0`, grade seven uniquely determines the two visible coordinates
of `z`:

```text
A(z)=2st,
B(z)=s^2-64t^2.
```

All seven grades through seven vanish.  At grade eight two source-independent
row combinations are

```text
G8_1+8G8_3 = -(3/256) D,
G8_4       = -(3/32768) F,
```

where

```text
D=t u^2-64t v^2-2suv,
F=s u^2-64s v^2+128tuv.
```

They obey

```text
sD-tF       = -2uv(s^2+64t^2),
sF+64tD     = (u^2-64v^2)(s^2+64t^2).
```

If `s^2+64t^2!=0`, these identities force `uv=0` and `u^2=64v^2`, hence
`u=v=0`, contrary to rank two.  If `s^2+64t^2=0`, then
`s=+8it` or `s=-8it` with `t!=0`; correspondingly

```text
D=t(u-8iv)^2 or D=t(u+8iv)^2.
```

Thus `D=0` forces `Delta_y=0`, again contrary to rank two.

## 7. Old-plane next rank zero dies at grade eight

Rank zero means `y=ell(a,b)` for arbitrary `a,b`.  Direct expansion shows
that every grade-eight row is independent of `a,b`; this is an exact
identity, not sampling.  It is therefore the already promoted zero-odd
calculation on the whole next rank-zero plane, not only at `y=0`.

Put

```text
z=(s^2,st/8,16t^2,0,0,0)+w,
WA=A(w),  WB=B(w).
```

The exact grade-eight identities are

```text
G8_1+8G8_3 = (3/2048) WA WB,
G8_4       = (3/524288)(WB^2-64WA^2).
```

Their common zero forces `WA=WB=0`.  The two remaining independent rows are

```text
G8_1 = (5kappa/4096)t(3s^2-64t^2),
G8_2 = (5kappa/65536)s(s^2-192t^2).
```

On `D(kappa) intersect (D(s) union D(t))` they have no common zero: if
`t=0`, the second forces `s=0`; if `t!=0`, the two nonzero equations require
both `s^2=(64/3)t^2` and `s^2=192t^2`.

## 8. Old-plane next rank one dies at grade eight

This is the formerly open `N-R` packet.  On the plus branch put

```text
u=8iv,  v!=0.
```

The complete grade-seven solution has one free scalar `lambda`:

```text
A(z)=2st+lambda v,
B(z)=s^2-64t^2+8i lambda v.
```

At grade eight the two zero-image equations are

```text
G8_1+8G8_3
  = (3v^2/256)(128t+16is+i lambda^2),

G8_4
  = (3v^2/4096)(-128it+16s-lambda^2).
```

Since `v!=0`, multiplying the second parenthesis by `i` and comparing with
the first forces `lambda^2=0`, hence `lambda=0`, and then `s=8it`.  With
these substitutions one remaining compatibility equation is

```text
G8_2+(i/2)G8_1 = -(5i/16) kappa t^3.
```

The source unit `kappa!=0` forces `t=0`, hence `s=0`, contradicting the
leading valuation-two open.  The minus branch is the exact conjugate:

```text
u=-8iv,
A(z)=2st+lambda v,
B(z)=s^2-64t^2-8i lambda v,
s=-8it,
G8_2-(i/2)G8_1 = +(5i/16) kappa t^3.
```

It dies identically.  This completes the sixth and last reduced rank cell.

## 9. Replay, controls, and resource class

Run from the repository root:

```text
python3 xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
```

The replay uses only Python's standard library and exact `Fraction`
arithmetic, with Gaussian rationals represented as pairs.  It independently:

1. checks the tails and compiler hashes;
2. validates all 569 tail weights and load-linearities;
3. reconstructs the unloaded and three load row-vectors under the literal
   V20R2 affine map;
4. verifies `Q6=0`, the factorization of `DQ`, all rank minors, and the
   omitted-coefficient identities;
5. expands the full old-plane systems through grade eight and checks every
   displayed equality coefficientwise over `Q` or `Q(i)`;
6. checks both conjugate rank-one branches;
7. verifies an in-memory source-custody mutation, a nonvacuous row-6 cubic
   coefficient mutation, the wrong grade-seven `B(z)` sign, and the
   load-bearing removal `kappa=0`.

Observed clean run:

```text
K00_R2_FULL_RANK_FAN_REPLAY=PASS
TAIL_TERM_COUNT=569
NONZERO_RANK2_MINORS=4
ROW6_MUTATION_KEY=0,0,0,0,1,2
MUTATION_CONTROLS=PASS
internal runtime: 2.536945 seconds
/usr/bin/time: real 2.57, user 2.55, sys 0.01 seconds
```

This is a desk-scale exact replay, far below the 60-CPU-second and 1-GiB
limits.  No Singular process, AWS job, web request, or external model was
used.

## 10. Scope, novelty, and nonclaims

The leading-rank-one and leading-rank-two grade-six exclusions are new.  The
old-plane next-rank-two and next-rank-zero claims were reviewer-derived and
unreviewed; this package independently reconstructs them.  The old-plane
next-rank-one hand obstruction is new and answers the prior `N-R` proposal.
This is not the refuted period-two `K00-RENORM` or `K00-SHIFT-LADDER`: every
grade and load arrival is rebuilt at literal valuation two.

The conclusion concerns field-valued finite jets in the exact normalized
V20R2 support.  It excludes same-source formal arcs because an arc truncates
to a grade-eight jet.  It does not exclude:

- valuations three, four, or five;
- a different K00 support or normalization;
- nilpotent scheme structure as a separate object;
- an algebraic or convergent germ outside this source;
- a polynomial Keller map, a counterexample, or JC2.

A finite compatible jet in another lane would not itself be an arc or map.
Promotion of this exclusion requires a different model to rebuild the
source rows and attack each exact rank-cell argument.

## 11. Custody

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json

2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py

2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
```

Only this new report and its new replay file were created.  No canonical or
existing artifact was edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11680`.
- Body SHA-256: `c596347cf5e343854b6838f8b7f3241c623de78250676033fc364d07bc23098c`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
