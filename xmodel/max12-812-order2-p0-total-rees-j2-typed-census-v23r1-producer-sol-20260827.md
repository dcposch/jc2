# Producer report: typed J2 prefix census V23R1

Producer: Sol Ultra

Date: 2026-08-27

Status: **PRODUCER-CHECKED DESIGN CENSUS; V22R1 DEPENDENCY PROVISIONAL.**

## Result

A restricted-AST exact-Q rewrite of all 42 exported source rows at grades
10--15 formed the two standard source restrictions over
`J1=(rs,cs,c0,c1)`:

```text
T-a0 source chart:    J1=0, a1=a0*qa1
ordered T-a1 source:  J1=0, a0=0
```

All seven grade-10 rows vanish on both restrictions, reproducing the reviewed
prefix control.  The only pure exceptional terms occur at grade 15.

On the a0 chart they form the exact vector

```text
Tg15_3 = -(1/16)  a0^3*qa1^3                         + nuisance
Tg15_4 = -(3/16)  a0^3*qa1^2                         + nuisance
Tg15_5 = -(3/16)  a0^3*qa1 -(3/32)a0^3*qa1^3*rho^2  + nuisance
Tg15_6 = -(1/16)  a0^3 -(3/16)a0^3*qa1^2*rho^2      + nuisance
Tg15_7 = -(3/32)  a0^3*qa1*rho^2
          -(3/128)a0^3*qa1^3*rho^4                  + nuisance.
```

On the ordered a1 restriction the pure terms are

```text
Tg15_3 = -(1/16)  a1^3               + nuisance
Tg15_5 = -(3/32)  a1^3*rho^2         + nuisance
Tg15_7 = -(3/128) a1^3*rho^4         + nuisance.
```

Setting `qa1=0` recovers only `Tg15_6=-a0^3/16`; the ordered a1 values are
already the reviewed A10 point controls.  Thus the V21 point theorem is the
constant/closed-complement face of a coherent full cubic chart vector, not an
isolated numerical coincidence.

## Sparse structure

The especially useful grade-15 row 6 has only 19 terms on the a0 chart and 12
on the ordered a1 restriction.  Its nuisance variables are confined to

```text
aa0,aa1,cs1,cs2,e0,e1,ee0,ee1,ell1,rs1,rs2
```

(with the obvious smaller support in some terms).  The grade-11/12 core is
also small.  For example, on the a0 chart, up to the nonzero scalar `3/8`,

```text
Tg11_1/a0 = e1+qa1*e0,
Tg11_2/a0 = e0+qa1*rho^2*e1,
Tg12_4    = (3/32)(e0^2+rho^2*e1^2).
```

This identifies a bounded homogeneous cofactor search or a small determinant
stratification as the next computation.  It does not yet show that any cubic
lies in the full ideal: the nuisance terms must be cancelled by explicit
source-row cofactors.

## V1 fail-closed repair

V1 wrote no `RESULT.json`.  Its positive control compared the whole
`(a0,qa1,rho)` chart polynomial to the point `A00`, forgetting that `A00`
also sets `qa1=0`.  The failure was a test-specification error and exposed the
additional pure `qa1` terms above.  R1 pins the V1 parser/rewriter unchanged
and repairs only that control.  The V1 output directory is quarantined.

```text
V1 erratum SHA-256     9c00c9df4dbb1526ad8fcae4460fc409304d5d5497192f0e3b5da8eb26bcf8a0
R1 freeze SHA-256      cf10b39bd96cfc30b6e61c0fe217e9f0414eda4fa32d43feaef3d6eff7476963
R1 implementation     2273305ed0745add26a961eec50c927cca9865e21f1bf96df69a0b21a3208ea1
R1 RESULT.json         ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641
```

The replay took 0.42 seconds and about 25 MiB RSS locally, within the
preregistered light-parser boundary.

## Relation to prior high-contact theorem

The already promoted fixed-`p=0` high-contact Cech theorem
(`4aeee798...`) has exact identities `g15[6]=-a0^3/16` and, after two
triangular pivots on the ordered complement, `g15[3]=-a1^3/16`.  V23 does
not silently generalize that theorem: the generic total-source chart retains
the jet nuisance terms displayed here and includes lower contact strata.  A
future direct certificate may recover the high-contact pivots as one face,
but must prove cancellation in the full typed source ideal.

## Scope and next step

This is a literal source-row rewrite, not a Rees saturation, radical
calculation, or chart verdict.  It consumes provisional V22R1 only as a cheap
speculative child; rollback is immediate if V22 review fails.  Fable5 is now
independently trying to derive the exact low-degree certificate or the
smallest sound AWS ansatz.  No expensive computation has been launched.

Nothing here proves either J2 chart empty, supplies unwritten Rees equations,
extends a formal arc, or establishes Gate T, order two, maximum twelve, or
JC2.
