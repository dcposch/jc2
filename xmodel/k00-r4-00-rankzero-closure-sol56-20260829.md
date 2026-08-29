# K00 V20R2 valuation four `R4-00`: independent effective-rank-zero closure

Author: Sol 5.6 Ultra (independent exact replay lane)  
Date: 2026-08-29 UTC  
Basis commit: `792eecb189e754046fd3db054cefeae773f1a56d`  
Lifecycle: `SEALED EXACT R4-00 EFFECTIVE-RANK-ZERO EXCLUSION`

## 0. Result

On the frozen normalized V20R2 source, the hinted grade-12 entry, grade-13
fan, and all three effective-rank-zero rays are correct.  The rank-zero cell
has exact field-valued lifts through grade 17, but every lift is obstructed by
row 6 at grade 18.  Thus grade 18 is the first decisive grade on this cell.

More precisely, with

```text
d = Lambda^4 ell(s,t) + Lambda^5 ell(s1,t1) + Lambda^6 z + ...,
ell(s,t) = (2s,t/8,s,t,s,2t),
kappa = k10[0] != 0,       (s,t) != (0,0),
A(q)=16q1-4q3+q5,          B(q)=q0-4q2+2q4,
```

grade 12 forces the field-valued reduced set `A(z)=B(z)=0`.  Write the cone
coordinates of `z` as `(a,b,u,v)` and put

```text
U = u + (5/6)kappa*s,       V = v - (5/6)kappa*t.
```

The grade-13 effective matrix has rank zero exactly at `U=V=0`.  Grade 14
then leaves exactly the rational ray and a conjugate pair

```text
P0:  s = -(50/9)kappa^2,    t = 0,
P+:  s = -(25/9)kappa^2,    t = +(25i/72)kappa^2,
P-:  s = -(25/9)kappa^2,    t = -(25i/72)kappa^2.
```

After the grade-16 certificate, row 6 at grade 18 is respectively

```text
(5kappa/3)^9 / 2^19,        (5kappa/3)^9 / 2^20,
                             (5kappa/3)^9 / 2^20,
```

which is nonzero because `kappa != 0` in characteristic zero.  Hence the
entire effective-rank-zero cell is empty by grade 18.

## 1. Frozen inputs and independent replay

The replay reconstructs all seven affine rows directly from the frozen 569
tails and the frozen compiler normalization.  It imports only the generic
exact sparse-polynomial/series primitives and tail parser from the older
valuation-two replay; it imports no R4 producer result or formula.

```text
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
506c00ac6d07e7fd0a29c76a1404e673add364bc76fb73c13dc7cd9b94afeddf
  xmodel/k00-r4-00-rankzero-replay-sol56-20260829.py
```

The computation is Python-standard-library exact rational/Gaussian-rational
arithmetic.  It takes about five seconds locally; no CAS, AWS job, web access,
or heavy computation was used.  The `jc2-lean` firewall was maintained.

Replay command and terminal receipt:

```text
$ python3 xmodel/k00-r4-00-rankzero-replay-sol56-20260829.py
R4-00 EFFECTIVE-RANK-ZERO REPLAY PASS
tails=569; grade12_terms= (5, 5, 5, 2, 5, 0, 4)
grade13_matrix=p,q fan; rankzero_rays=P0,P+,P-
first_obstruction=grade18_row6; mutation_key= (0, 0, 0, 0, 3, 0)
runtime_seconds=4.621
```

## 2. Grade-12 entry reconstructed exactly

Write `Az=A(z)`, `Bz=B(z)` and

```text
H = (5/2048)kappa(s Az+t Bz) + (3/1024)(u Az-v Bz).
```

The seven literal grade-12 rows reconstructed from the tails are

```text
G1 = H - (3/2048)Az Bz,
G2 = (5/32768)kappa*s*Bz -(5/512)kappa*t*Az
     +(3/16384)u*Bz +(3/256)v*Az +(15/2048)Az^2,
G3 = -(1/8)H +(3/8192)Az Bz,
G4 = (3/524288)(Bz^2-64Az^2),
G5 = -(1/128)H -(3/262144)Az Bz,
G6 = 0,
G7 = -(1/1024)H.
```

No `a,b,s1,t1,k10[1]` occurs.  The exact certificates

```text
G3 + G1/8 = (3/16384)Az Bz,
G4          = (3/524288)(Bz^2-64Az^2),

Az^3 = (1/64)[ Bz*(16384/3)(G3+G1/8) - Az*(524288/3)G4 ],
Bz^3 = Bz*(524288/3)G4 + Az*(1048576/3)(G3+G1/8)
```

show that the common field-valued zero set is exactly `Az=Bz=0` over every
characteristic-zero field.  Conversely all seven rows vanish there.  This is
a set-theoretic statement; the literal row ideal is not asserted to equal the
radical ideal `(Az,Bz)`.

## 3. Grade-13 effective fan

On `Az=Bz=0`, let `(A7,B7)` be the transverse coordinates of the next jet and
define

```text
p = 6u+5kappa*s = 6U,
q = -6v+5kappa*t = -6V.
```

The complete grade-13 content is

```text
[G1]   1       [ p      q   ] [A7]
[G2] = ----    [ -4q   p/16 ] [B7],
        2048

G3=-G1/8,  G5=-G1/128,  G7=-G1/1024,  G4=G6=0.
```

The determinant is `(p^2+64q^2)/2^26`.  Thus the reduced effective fan is
rank two on `p^2+64q^2 != 0`, rank one on its punctured zero cone, and rank
zero exactly at `p=q=0`, equivalently `U=V=0`.  No flag/place/series
identification is involved: `A7,B7` are transverse series coefficients,
whereas `s,t,u,v,kappa` are lower-grade coefficient parameters.

## 4. Rank zero: grade-14 source and the three rays

Set `u=-(5/6)kappa*s` and `v=(5/6)kappa*t`.  Grade 13 vanishes identically.
At grade 14 the universal cokernel rows first give

```text
G3+G1/8    = (3/16384)A7 B7,
G5+G1/128  = -(3/131072)A7 B7,
G7+G1/1024 = -(3/2097152)A7 B7,
G4          = (3/524288)(B7^2-64A7^2),
G6          = 0.
```

Hence field-valued solutions have `A7=B7=0`.  The two remaining literal
source equations are exactly

```text
G1,14 = (5/36864)kappa*t*F1,
G2,14 = (5/589824)kappa*F2,

F1 = 27s^2 + 100s*kappa^2 - 576t^2,
F2 = 9s^3 + 50s^2*kappa^2 - 1728s*t^2 - 3200t^2*kappa^2.
```

The replay checks the polynomial identity

```text
576F2 - (1728s+3200kappa^2)F1
  = -512s(9s+25kappa^2)^2.
```

Because `kappa != 0` and `(s,t) != (0,0)`, the case `t=0` gives
`s=-50kappa^2/9`.  If `t != 0`, then `F1=F2=0`; the identity forces
`s=-25kappa^2/9`, and `F1=0` gives
`t^2=-(25kappa^2/72)^2`.  This is precisely `P0,P+,P-` above (the conjugate
points need a coefficient field containing a square root of `-1`).

## 5. Exact continuation and first obstruction

On each ray, the grade-16 universal rows reduce, with no residual dependence
on other jets or loads, to

```text
G3,16+G1,16/8 = (3/16384)A8 B8,
G4,16           = (3/524288)(B8^2-64A8^2).
```

Thus `A8=B8=0` field-valuedly.  After imposing only the already forced
`A7=B7=A8=B8=0`, the pristine row-6 grade-18 coefficient is the following
five-term base polynomial; every other coefficient that can arrive by grade
18 cancels identically:

```text
G6,18 = -(25/2048)t^4*kappa
         +(125/36864)s*t^2*kappa^3
         +(75/65536)s^2*t^2*kappa
         -(125/7077888)s^3*kappa^3
         -(25/8388608)s^4*kappa.
```

Substitution gives

```text
G6,18(P0) = 1953125/10319560704 * kappa^9
           = (5kappa/3)^9/2^19,
G6,18(P+) = G6,18(P-)
           = 1953125/20639121408 * kappa^9
           = (5kappa/3)^9/2^20.
```

There is no row-6 target before grade 19, so no source coefficient can absorb
these units.

To prove that grade 18 really is first, rather than merely sufficient, the
replay exhibits exact full-source lifts through grade 17:

1. On `P0`, set every nonbase jet/load coefficient to zero and set
   `mu2[2]=-(390625/35831808)kappa^8`; all seven rows through grade 17 vanish.
2. On `P+` and `P-`, set every nonbase coefficient and target to zero except
   `k10[2]=(5/6)kappa^2`; again all seven rows through grade 17 vanish.

In all three lifts row 6 at grade 18 is the unit displayed above.  A
deterministic in-memory mutation of the reconstructed row-6 coefficient at
`d`-exponent key `(0,0,0,0,3,0)` changes the grade-18 value, so the terminal
check is not vacuous.

## 6. Maximum safe integration

Safe canonical statement:

> On the normalized frozen K00 V20R2 exact-valuation-four source, the
> field-valued `R4-00` effective-rank-zero cell `U=V=0` has exactly three
> grade-14 geometric rays.  Each has a lift through grade 17, and each is
> killed by a nonzero row-6 coefficient at grade 18.  Hence this cell is
> empty through the grade-19 window.

This does not decide the rank-one or rank-two effective cells, any other
valuation/support/normalization, nonreduced scheme structure, convergence of
formal arcs, polynomial-map attainment, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8011`.
- Body SHA-256:
  `c073054c61ce1037fe01ccdd4dec03acbe6940775cf536246728d5eaa635ac38`.
- Frozen basis: `792eecb189e754046fd3db054cefeae773f1a56d`.
