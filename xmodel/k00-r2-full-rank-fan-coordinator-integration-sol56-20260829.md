# K00 V20R2 valuation two: coordinator integration of the full rank fan

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `PROMOTED EXACT FINITE-JET EXCLUSION / REPAIRED`

## Binding verdict

Promote the exact valuation-two exclusion with the repairs below.  Over any
characteristic-zero field, the normalized V20R2 source has no field-valued
compatible jet of exact `Lambda`-valuation two through grade eight.  Hence no
same-source formal arc can have valuation two, because its grade-eight
truncation would be such a jet.

The precise source is

```text
C6=1,
k10[0]=kappa!=0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
Jdet[0]!=0,
d=Lambda^2 x+Lambda^3 y+Lambda^4 z+...,
x!=0.
```

The grade-eight theorem does not use `Jdet[0]!=0`; that open remains part of
the named source.  No algebraic closure is required: an isotropic rank-one
branch is absent over the base field or dies by the displayed quotient-ring
identity.

## Evidence and independent reconstruction

The Sol producer is
`xmodel/k00-r2-full-rank-fan-provisional-sol56-20260829.md`, full SHA-256
`2ebd1d78391a145c446d2113a1801e342118773c6fd9ce63be183dfd94f15a58`,
body SHA-256
`c596347cf5e343854b6838f8b7f3241c623de78250676033fc364d07bc23098c`.
Its stdlib replay has SHA-256
`2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4`
and reconstructs all 569 frozen tails.

Three different-model cross-reviews independently rebuilt the seven rows
from those tails rather than treating the producer replay as an oracle:

```text
Grok 4.6  full 50d2a1082b27effd25930acc1c0f8979508281f989b47a8df35441e7c07ae068
          body 20e87709b665ec3f5175c10d21535fba15b9360b67f070ea407c8bee071a5d2e

Opus 5    full 34e90f2999207cf002e6ad7b95e4ab31219bbc42f384312b99567cbfe1b8f39d
          body 006fd2e67fecc8f545265c9dc834be739608d2c5b2cf68edf5f6c5d13bde2653

Fable 5   full 3e4eed762d6eacaeab67c753f386fa90f03cb27a6596c243e83ebf6fff658b77
          body a0c7f687d2c77004ca5a8f521e8b152ebff4ea30842c525cd60c3bfcdb9c0ca3
```

All three return `PASS` or `PASS_WITH_REPAIR` on the mathematics.  Opus
used an independent sparse-series engine, quotient rings
`Q[r]/(r^2+64)` and `Q[t]/(t^2-192)`, a separate univariate numerical path,
and a 569-term sensitivity census: all 450 terms capable of contributing
through grade eight changed a live row under mutation, while the 119 later
or dormant terms remained invisible.  Fable kept the removable load and jet
variables symbolic and supplied the ideal-membership check missing from one
producer replay control.  Grok independently reconstructed every cell and
its mutation controls.  Agreement is not a vote; these distinct exact
reconstructions are the promotion evidence.

## Complete reduced rank fan

Put

```text
A(q)=16q1-4q3+q5,
B(q)=q0-4q2+2q4.
```

The leading reduced cone is exactly `A(x)=B(x)=0`, parameterized by

```text
x=(2b+2u,a,b,8a+v,b-u,16a+4v).
```

On it every row of `DQ(x)` factors through `(A,B)`, and its four nonzero
two-by-two minors are rational multiples of

```text
Delta=u^2+64v^2.
```

Thus rank one is `Delta=0,(u,v)!=(0,0)`, rank two is `Delta!=0`, and rank
zero is the old plane `u=v=0`.

At leading rank one, row 6 at grade six is

```text
u(192v^2-u^2)/65536 = +- i v^3/32,
```

so the cell is empty.  At leading rank two, row 6 reduces to `u=0` or
`u^2=192v^2`; the first branch requires both `v+3a=0` and `v+2a=0`, while
the second has exact cokernel constants `S5=v^3/8` and `S7=-v^3/64`.
Both are empty.

Rank zero gives

```text
x=ell(s,t)=(2s,t/8,s,t,s,2t),       (s,t)!=(0,0),
```

and grade six sends `y` to the same reduced cone.  Its three rank cells all
die at grade eight:

- rank two by the exact `D,F` rows and the identities
  `sD-tF=-2uv(s^2+64t^2)` and
  `sF+64tD=(u^2-64v^2)(s^2+64t^2)`, including the two isotropic source
  branches;
- rank zero by whole-plane invariance, the ideal `(W_A,W_B)`, and the two
  incompatible `kappa`-cubics on `D(s) union D(t)`;
- rank one by `lambda=0`, `s=+-8it`, and the terminal unit
  `-+(5i/16)kappa t^3` on both conjugate branches.

These six cells exhaust `x!=0`; there is no hidden leading component.

## Repairs folded into promotion

1. The producer replay's cell-five check discarded free `w` components
   before proving they were harmless.  Fable independently verifies that
   each terminal-row difference lies in `(W_A,W_B)`.  Promotion consumes
   that membership result, not the under-verifying control alone.
2. The statement that `k6[0]=0` by itself postpones the K6 load is
   insufficient: some K6 monomials have constant companion factors.  Direct
   substitution shows the complete constant-evaluated K6 coefficient is zero
   in all seven rows.  That exact cancellation is the reason no K6 term
   reaches grade eight.
3. Distinguish the seven-row calendar from the contracted grade-19 calendar.
   In the seven-row system, the K10 quadratic load arrives at `2+2r`, not
   `2+3r`; the latter is the transverse-degree floor of the contracted row.
   The valuation-two proof already uses the literal correct calendar.
4. The composition census must include `v_Lambda(d)=infinity`.  At `d=0`
   all seven loaded rows vanish through grade 19 except the row-seven target
   `-Lambda^19 Jdet/4`, which contradicts `Jdet[0]!=0`.  Combining this with
   the promoted valuation-one and valuation-at-least-six exclusions leaves
   precisely finite valuations `3,4,5` possible on this support, none known
   to occur.

The external global-selector sections contain separate claims, including a
correlated proper-root/pole-vertex error, that are rejected in the round
synthesis.  They are not dependencies of this K00 promotion.

## Scope

This is a reduced field-valued finite-jet theorem on one normalized support.
It does not describe nilpotent scheme structure, prove a surviving jet or
arc exists, algebraize a formal object, construct a polynomial map, produce a
counterexample, or decide JC2.  Other supports and normalizations remain open.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6045`.
- Body SHA-256:
  `614a04b6ca4e4c3620fbb3ca8928d4075dcec9814824dbf2b669fe049a41651d`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
