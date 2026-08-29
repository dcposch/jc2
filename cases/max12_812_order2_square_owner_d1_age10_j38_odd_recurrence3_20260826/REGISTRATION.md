# Registration: D1 `a>=10` grade-38 order-three odd recurrence

Date: 2026-08-26

Status: **PREREGISTERED REPAIRED DUAL-AWS EXACT-SOURCE OBSTRUCTION.**

An unfrozen, unlaunched draft inherited the `a>=13` jet depths and was found
incomplete for baseline `a=10`: it stopped at `A_3,k10_1`. It produced no
endpoint and no verdict. This registration supersedes that draft before the
source freeze. The repaired compiler derives every jet maximum mechanically
and requires `A_7` and `k10_6` to occur nontrivially at grade 38.

## Uniform claim under test

At the symbolic baseline write

```text
A=sigma^10*theta*Abar,
C=sigma^11*theta*Cbar,
R=sigma^10*theta*eta*Rbar.
```

Then `theta=sigma^n`, `eta=sigma^s` covers every
`a=10+n,c=a+1,r=a+s`. The compiler independently expands all four binomial
source summands and requires exactly these eleven primitive families through
absolute grade 38:

| grade | family | pole |
|---:|---|---:|
| 28 | `k6*C` | 1 |
| 31 | `A*C` | 1 |
| 32 | `C^2`, `k10*R*C`, `k2*R` | 2, 1, 1 |
| 34 | `k10*A^2` | 1 |
| 35 | `k10*A*C`, `k2*A` | 2, 2 |
| 36 | `k10*C^2`, `k6*R^2`, `k2*C` | 3, 1, 3 |

The first pole-order-four family is `k6*A*C/L^4` at grade 43. Increasing
`a` or `r` only delays every family. The mechanically derived jet bounds are

```text
A_7, C_10, R_6, k10_6, k6_10, k2_6, p_10,
mu2_10, mu4_6, mu6_2.
```

The compiler writes a canonical inventory of every analytic and transformed
literal-Faber source monomial through grade 38, plus every target monomial.

For a source of pole order at most three, the moving odd Faber rows obey

```text
Phi7 = -(p(sigma)/4)*Phi5
       -(3*p(sigma)^2/32)*Phi3
       -(5*p(sigma)^3/128)*Phi1.              (R3)
```

Since the Keller target contributes `-sigma^38*J/4` only to row 7, the exact
test is

```text
Phi7+(p(sigma)/4)Phi5+(3*p(sigma)^2/32)Phi3
    +(5*p(sigma)^3/128)Phi1
  = -sigma^38*J/4 mod sigma^39.               (J38-3)
```

The row equations would force `J=0`, contradicting `D(J)`. A PASS closes
the residual `a=10,11,12` contacts and overlaps the separately valid
order-two `a>=13` theorem.

## Acceptance

1. Independently enumerate all eleven primitive families and every induced
   normal/load/moving-connection monomial through grade 38; derive jet maxima
   from that list, not from a handwritten index formula.
2. Rebuild all seven frozen literal rows with those full jets and bridge them,
   modulo `sigma^39`, to the independent Laurent/binomial emitter. Require all
   seven bridge identities and live grade-38 `A_7,k10_6` sentinels.
3. Verify `(J38-3)` exactly over Q and `F_65521`, its homogeneous stability
   under `theta,eta`, and the unit ideal after adjoining `J^{-1}`.
4. Preserve the separate `a>=13` order-two result and its `a=12` negative
   control as an independent theorem/control.
5. Include a Pell positive control, rc 0, no diagnostics, and zero swap. All
   compiler and CAS work is AWS-only.

## Firewall

A PASS excludes only the registered D1 cone `a>=10,c=a+1,r>=a` on `D(J)`
for the seven literal Faber rows after the cited upstream gates. It does not
cover `a<10`, other D1 cells, excluded lifecycle charts, the whole square
component, order two, `(8,12)`, maximum twelve, or JC2.
