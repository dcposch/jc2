# K00 V20R2 valuation five: internal hostile audit of the provisional jet fan

Auditor: Sol 5.6 internal adversarial lane  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `INTERNAL SAME-MODEL AUDIT / REPAIR_REQUIRED / NOT PROMOTION EVIDENCE`

## Verdict

Do not promote or consume the sealed valuation-five producer as written.
Its leading rank-two exclusion is exact.  Its leading rank-one exclusion also
survives, but only after a grade-13 branch equation omitted by the report and
replay is restored.  The advertised `K00-R5-R0-RESIDUAL/v1` digest does not
hash the displayed residual, and the displayed coefficient ranges mix inert
coordinates with implicit zero specializations.  The residual therefore has
no licensed client until a newly sealed v2 producer repairs its type and
replay.

The audited producer is
`xmodel/k00-r5-jetfan-provisional-sol56-20260829.md`, full SHA-256
`82e6512d4a80ae4bdcf8847e6b0a6ed45ed6d03b4898479e946cab3084fd24a0`,
body SHA-256
`cdd37ff2f2c7fa07803105c57dca34d56ffe159b77afd29fb0e5644b6f67517a`.
Its replay is
`xmodel/k00-r5-jetfan-replay-sol56-20260829.py`, SHA-256
`eb8513b622e9c6fa839f9f20f32ff4c4fc9207a8591cdb6b292ab141f159522b`.
The producer remains immutable evidence of the attempted argument.

## Exact leading-rank checks

The reduced leading cone is confirmed by

```text
Q3+(1/8)Q1 = (3/16384) A B,
Q4         = (3/524288)(B^2-64A^2).
```

Thus its characteristic-zero field-valued zero set is `A=B=0`.

On leading rank two, all seven grade-12 and grade-13 equations vanish under
the stated solves.  The two grade-14 cokernel rows are exactly

```text
E4          = (25 kappa^2/131072)(64v^2-u^2),
E3+(1/8)E1 = (25 kappa^2/4096)uv.
```

They force `u=v=0`, contrary to rank two.  This part passes the internal
reconstruction.

On leading rank one write

```text
u=epsilon 8 i v,       v!=0,
f=u_y-epsilon 8 i v_y.
```

Grade 12 correctly forces the report's `lambda=0`.  But for its proposed
particular next solve, grade 13 also has the exact cokernel equation

```text
G13_2+(epsilon i/2)G13_1
  = (epsilon 3i/1024) v tau f.
```

The report's statement that grade 13 is automatically soluble is therefore
false; one must split `tau*f=0`.  The exclusion survives both branches:

```text
tau=0:  E4=(100 kappa^2 v^2)/4096 != 0;

f=0:    -3tau^2+100kappa^2=0,
         3tau^2+100kappa^2=0,
         hence kappa=0, contradiction.
```

This repairs the mathematics of the leading rank-one kill, not the submitted
proof/replay custody.  A replacement must assert all seven grade-12 and
grade-13 equations and replay both branches.

## Residual hash and type failure

The producer prints residual digest
`b2488b33365e6bfeb1fe031b76386d8c2a6293cf42e7727765fc3d6521514498`.
That is the hash of a private shorthand in the replay, not of the displayed
Section 6 block.  The displayed block hashes to
`2538761a9ddd304366bd9fecab22e25a163b7d5972785f69bb8640b56e07789d`
with its trailing line feed, or
`2e65b58d516e4775e83a1ebc95bc170e48a82b3a9cf835fa2276fec50f003bc1`
without it.  The shorthand omits the literal `Phi_i` definition, target
rows, target signs and shifts, the `Jdet/4` factor, and the explicit `Jdet`
series declaration.  Mutating those data therefore cannot change the claimed
digest.

Direct dependency reconstruction on the rank-zero substitution gives first
load orders

```text
ord K10=12,       ord K6=7,       ord K2=5.
```

Equations through grade 19 use only

```text
d[6..13], k10[0..5], k6[1..6], k2[1..4].
```

The displayed `d[14]`, `k10[6,7]`, and `k6[7,8]` are inert.  Conversely,
writing the truncated sums `mod Lambda^20` sets omitted inert jet
coefficients to zero.  The object is consequently neither the minimal
coefficient projection nor the full jet locus with its free affine factors.
The replay does not expand the grade-13--19 residual equations, derive these
ranges, parse the target shifts/signs, or replay the contracted identity; its
claimed residual mutation control is only a comparison of hard-coded text.

The contracted statement itself checks independently: `h(0)=20`, the
transverse degree floors of `D10,D6,D2` are `3,2,2`, and the even-target
multipliers have zero constant term.  Through grade 19 it is therefore

```text
[Lambda^19](p10 D10+p6 D6)=5 Jdet[0].
```

This exact identity does not repair the malformed residual locus.

## Maximum retained provisional statement

The same-model audit supports, but cannot different-model promote, only:

> Over a characteristic-zero field, every exact valuation-five normalized
> V20R2 jet compatible through grade 14 has leading coefficient
> `x=ell(s,t)`, `(s,t)!=(0,0)`.  Both nonzero-rank leading strata are empty.
> On the remaining rank-zero stratum, grades 10 and 11 vanish and grade 12 is
> exactly `Q(d[6])=0`, whose reduced field-valued locus is `A=B=0`.

A new producer must restore the grade-13 split, define the literal target
rows

```text
-delta_(l,2) Lambda^14 mu2 -delta_(l,4) Lambda^16 mu4
-delta_(l,6) Lambda^18 mu6 -delta_(l,7) Lambda^19 Jdet/4,
```

choose a minimal projection or a full locus with free factors, hash those
canonical bytes, and make the replay derive the calendar and contracted
checks.  No residual point, arc, scheme, map, counterexample, or JC2
conclusion is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5321`.
- Body SHA-256:
  `53cd0fd2b9c6fd4fccd1e36c078c824fdf8804eebc89976373c536a3f72733d1`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
