# Audit of Opus5 terminal-receiver Lemmas R1--R3 and the missing unit-load section

Date: 2026-08-27

Status: **EXACT INDEPENDENT AUDIT.  R1--R3 CONFIRMED AT RADICAL/FIELD-POINT
SCOPE; RAW-ROW RECEIVER-EMPTINESS STRATEGY REFUTED BY AN ALL-DEPTH
`D(k)` ZERO SECTION.**

This audit writes only this report.  It did not read or touch `jc2-lean`, use
the network or AWS, or run a CAS.  All calculations were exact sparse
polynomial arithmetic with Python `Fraction` values and a direct replay of
the frozen 569 canonical tails.

## 1. Custody and exact replay surface

The following bytes were read independently.

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848  tails.json (569 canonical terms)
5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587  V20 actual-total emitter
0807540484b93ee12b6d6b7ea2b90a7e80418fd29fa7633bc9a8ab3485269f14  V21 all-depth replay
f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff  V21 RESULT.json
14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501  V23 exact AST parser/census
ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641  V23R1 RESULT.json
c9f89344b4fc92e3ed1deade74a3cbd6301a5d45d9178aa3096f52aa6714b293  V28 exact-Q RESULT.json
093298e352d3dcfd3eceb59d5f30338c42ed7a1bb322ccd5c590125ca7e44d3e  V30 exact-Q RESULT.json
22018489bbf27c91d5d973ac6e2ec00780fa079e6b07b6d386ce45dc5737de1f  V33 exact-Q RESULT.json
b7e8d54982d8e6db28e36fc57decf76b7e13811958faff7172bfa768c7272648  V36 exact-Q compile_result.json
04974b5c2949a5f9992ac5c2faad8bbfb16c446281b9c02ca12752a065fe80e5  audited Opus5 report
```

For grades 10--15 I parsed the general-`rho` V23R1 `a1_ordered` rows and
set `a1=0`.  For grades 16--18 I parsed the exact-Q V28/V30/V33 rows and set
`a1=0`; those three exports had already set `rho=0`.  Grade 19 was parsed
from the V35 row bytes whose seven hashes and Q/F65521 shadows are checked
by V36.  Every identity below was tested as literal zero residual in the
exact AST representation.

This exposes one defect in Opus5's proposed V36 receiver census: the frozen
grades 16--18 do **not** support its advertised `rho != 0` leaf, because
V28/V30/V33 killed `rho` during compilation.  General-`rho` receiver bytes
currently stop at grade 15.  This defect is superseded by the all-depth
unit-load section in section 4.

## 2. R1--R3 verdict

All statements below are over characteristic zero (and the displayed
pointwise arguments work whenever the denominators and the factor 128 are
invertible).  "Forces" means on field-valued points, equivalently after
passing to the radical; the rows need not contain the variables themselves
scheme-theoretically.

### R1: confirmed

On the receiver `a1=0`, the literal identity is

```text
Tg12_3 - (rho^2/2) Tg12_1 = (3/16)e0*e1.
```

Together with

```text
Tg12_4 = (3/32)(e0^2 + rho^2*e1^2)
```

and, on `rho=0`, the surviving square `(3/32)e1^2` in `Tg12_2`, this forces
`e0=e1=0` with no localization.  Opus5's proof and scope are correct.

### R2: confirmed

After `e0=e1=0`, exact subtraction gives

```text
Tg14_3 - (rho^2/2) Tg14_1
  = (3/16)ee0*ee1 - (ell1/2)Tg13_1,
Tg14_4 = (3/32)(ee0^2 + rho^2*ee1^2).
```

Hence the row ideal forces `ee0*ee1=0`, and its radical forces
`ee0=0` and `rho*ee1=0`.  R2 is correct at precisely this radical/pointwise
scope.

### R3: confirmed on `D(k)`

If `rho != 0`, R2 gives `ee1=0`, and after the preceding zeros the two
grade-13 rows are exactly

```text
Tg13_1 = (5/256) k*cs1*(3*rs1^2 + 16*cs1^2*rho^2),
Tg13_2 = (5/1024)k*rs1*(rs1^2 + 48*cs1^2*rho^2).
```

On `D(k*rho)` their only common field-valued zero is `cs1=rs1=0`: if both
were nonzero, three times the second bracket minus the first would give
`128*cs1^2*rho^2=0`.

If `rho=0`, then on `D(k)` the exact restrictions are

```text
Tg13_2 = (5/1024)k*rs1^3,
Tg13_1 |_(rs1=0) = (3/8)aa0*ee1.
```

Thus `rs1=0` and `aa0*ee1=0`.  R3 is correct.  Its conclusion is a cut on
the raw necessary equations, not an honest-chart existence or emptiness
statement.

## 3. Sharpened minimal radical cascade on `rho=0, D(k)`

There is no need for Opus5's four-leaf split.  Using only grades
13,14,15,16,18, the `rho=0` branch reduces to two leaves.

Work after R1--R3, so

```text
e0=e1=ee0=rs1=rho=0,       aa0*ee1=0.
```

First set

```text
F = aa0*ee1                         = (8/3)Tg13_1,
G = 4*aa0*ec3 - 4*aa1*ee1*ell1 + ee1^2
                                      = (32/3)Tg14_2,
H = ee1^2*ell1                     = -(32/3)Tg15_4.
```

The exact certificate

```text
ee1^3 = ee1*G - 4*ec3*F + 4*aa1*H
```

forces `ee1=0` in the radical.  This removes the proposed
`ee1=0`/`aa0=0` branch entirely.

Next, after `ee1=0`, put

```text
F2 = aa0*ec3 = (8/3)Tg14_2,
G2 = 8*aa0*aa1*cs1*ell1 - aa0^2*rs2 + ec3^2
                                      = (32/3)Tg16_4.
```

Then

```text
ec3^3 = ec3*G2 - (8*aa1*cs1*ell1 - aa0*rs2)*F2,
```

so `ec3=0` in the radical.

After `ec3=0`, define

```text
A = 16*Tg14_1
  = 6*aa0*ez3 - 5*cs1^3*ell1*k,
B = 32*Tg15_3
  = -6*aa0*ell1*ez3 - 12*aa0^2*cs1
    + 5*cs1^3*ell1^2*k.
```

The identity

```text
B + ell1*A = -12*aa0^2*cs1
```

puts `aa0^2*cs1` in the ideal.  Finally, with

```text
H18 = 128*Tg18_6
    = 24*aa0*cs1*ell1*ez3 + 12*aa0^2*cs1^2 - 8*aa0^3
      + 15*cs1^4*ell1^2*k,
F3  = aa0^2*cs1,
```

one has

```text
8*aa0^4 = (42*ell1*ez3 + 12*aa0*cs1)*F3
           - aa0*H18 - 3*aa0*cs1*ell1*A.
```

Thus `aa0=0`; then `A=0` and `k != 0` give
`cs1^3*ell1=0`.  The minimal reduced support is therefore

```text
e0=e1=ee0=ee1=rs1=ec3=aa0=rho=0,
cs1=0  or  ell1=0,                  with k != 0.
```

The two leaves have the following nonzero-row counts after substitution:

| leaf | g15 | g16 | g17 | g18 | g19 |
|---|---:|---:|---:|---:|---:|
| `cs1=0` | 2 | 3 | 5 | 6 | 7 |
| `ell1=0` | 1 | 2 | 3 | 4 | 5 |

Grade 19 is included because V36 checks the seven exact row shadows.  It
does not reduce the branch count, and no raw-row calculation can empty
either leaf because both contain the section below.

For reference, the literal receiver row term census is

```text
grade 10: 0,0,0,0,0,0,0
grade 11: 0,0,0,0,0,0,0
grade 12: 2,3,3,2,3,0,3
grade 13: 8,10,12,3,13,0,13
grade 14: 18,24,30,6,35,0,36
grade 15: 35,49,67,14,86,6,92
grade 16: 54,66,74,26,54,14,23       (rho=0 export)
grade 17: 88,119,148,56,128,39,68    (rho=0 export)
grade 18: 136,202,267,111,269,95,177 (rho=0 export)
grade 19: 200,319,446,199,515,200,402 (rho=0 export)
```

This reproduces Opus5's total of 2,787 terms through grade 18 and gives
5,068 through grade 19.

## 4. Decisive omission: an on-`D(k)` all-depth raw zero section

Define the receiver assignment

```text
K00: every source coordinate except rho and k is zero;
     k is arbitrary and nonzero.
```

It lies in `V(J1+J2) cap D(k)` at the raw source/localizer level.  In the
actual-total emitter,

```text
p=-2*rho^2,  c=0,  r=p^2/4,
az=ac=ez=ec=0,
k10(sigma)=k,  shifted into the load as k*sigma^4,
k6=k2=0.
```

I replayed every one of the 569 frozen canonical-tail monomials without a
grade truncation.  The only load patterns occurring are

```text
(0,0,0): 280,  (1,0,0): 190,  (0,1,0): 72,  (0,0,1): 27.
```

Thus the `k10` part is linear in `k`.  On K00 the contribution census by
row is

```text
row:                    1   2   3   4   5   6   7
no-load contributions: 0  11   0  15   0  17   0
k10 contributions:     0   9   0  11   0  15   0
combined contributions:0  20   0  26   0  32   0
```

The no-load and `k10` sums each cancel separately to the zero polynomial in
`Q[sigma,rho]` in every row.  This independently extends V21's off-family
`Z00` calculation: the frozen finite-tail raw source has an exact
all-depth `D(k) x A^1_rho` zero section.  Direct substitution also kills all
70 frozen receiver rows through grade 19.

This is the disambiguation the Opus5 report missed:

- `Z00` has `k=0` and is off the named unit-`k10` family.
- `K00` has `k!=0`, satisfies the Rabinowitsch equation with `v=k^-1`, and
  is on the named open **at raw-row/localizer scope**.
- `K00` is **not** evidence that the honest saturated Rees chart is
  nonempty.  The Rees kernel, chart equations, and routing/coverage data are
  absent from the raw-row system and may exclude it.

## 5. Strategic consequence and smallest fail-closed next case

The R1--R3 cascade is valid descriptive algebra, but deeper raw receiver
rows can never make `V(J1+J2) cap D(k)` empty for this frozen source: K00
survives all depths, not merely grades 10--19.  Therefore the proposed
raw-row `std` leaf and any further raw grade export are strategically
incapable of deciding the on-family receiver.

The smallest fail-closed implementation is a desk-scale **K00 registration
and honest-equation discriminator**:

1. pin the 569 tails and emitter above;
2. replay the no-load and unit-`k10` cancellations separately, requiring
   exactly the `11+9`, `15+11`, `17+15` contribution split;
3. bridge all 70 frozen rows through grade 19 and require zero at K00;
4. include `1-v*k`, with the positive control `k=v=1`, and require Z00 to
   fail that localizer;
5. then evaluate the **genuine saturated Rees kernel/chart/routing
   equations** at K00.

Only step 5 is a live discriminator.  A nonzero honest equation gives the
first valid exclusion target/certificate; simultaneous vanishing would
upgrade K00 from a raw necessary-condition point toward an honest chart
candidate.  Neither outcome may be inferred from the present audit.

No Gate-T, receiver-chart, order-two, maximum-twelve, or JC2 verdict is
claimed.
