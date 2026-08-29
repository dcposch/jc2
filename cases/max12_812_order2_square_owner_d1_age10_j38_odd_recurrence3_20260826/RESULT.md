# Result: uniform D1 `a>=10` grade-38 order-three obstruction

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

The earlier unfrozen draft which stopped at `A_3,k10_1` remains no-verdict.
This is the mechanically repaired, source-complete producer.

## Exact theorem produced

In characteristic zero, after the registered upstream square/D1 gates, the
seven literal Faber source equations have no point on the Keller chart `D(J)`
with

```text
ord_sigma(A)=a,  ord_sigma(C)=a+1,  ord_sigma(R)=r,
a>=10, r>=a.
```

At the symbolic baseline put

```text
A=sigma^10*theta*Abar,
C=sigma^11*theta*Cbar,
R=sigma^10*theta*eta*Rbar.
```

Every source contribution through absolute grade 38 has pole order at most
three. Consequently the moving odd Faber rows satisfy

```text
Phi7+(p(sigma)/4)*Phi5+(3*p(sigma)^2/32)*Phi3
    +(5*p(sigma)^3/128)*Phi1 = 0 mod sigma^39.       (R3)
```

The only odd target is `-sigma^38*J/4` in row seven. The corresponding
combination of the full equations is therefore exactly
`-sigma^38*J/4 mod sigma^39`. Vanishing of all seven rows forces `J=0`;
adjoining `iJ*J-1` gives the unit ideal before radicals.

## Complete source inventory and jet ceiling

The compiler independently binomial-expands all four source summands rather
than importing a handwritten wall list. At baseline `a=r=10,c=11`, the
primitive polar families through grade 38 are exactly:

| first grade | family | coefficient | pole |
|---:|---|---:|---:|
| 28 | `k6*C/L` | `3/4` | 1 |
| 31 | `A*C/L` | `3/4` | 1 |
| 32 | `k10*R*C/L` | `5/8` | 1 |
| 32 | `k2*R/L` | `1/2` | 1 |
| 32 | `C^2/L^2` | `3/8` | 2 |
| 34 | `k10*A^2/L` | `5/32` | 1 |
| 35 | `k10*A*C/L^2` | `5/16` | 2 |
| 35 | `k2*A/L^2` | `1/4` | 2 |
| 36 | `k10*C^2/L^3` | `5/32` | 3 |
| 36 | `k2*C/L^3` | `1/4` | 3 |
| 36 | `k6*R^2/L` | `3/8` | 1 |

The first pole-order-four family is `k6*A*C/L^4` at grade 43. Increasing
`a` or `r` only delays every family.

Expanding every normal component, load jet, inverse-connection term, and
Faber transform yields 10,407 analytic monomials and 6,921 collected literal
source monomials. Both characteristics emit byte-identical inventory SHA

```text
884922fede59bc3540a61aa089a9ed92f65235b269330d63b9195afa69019297.
```

The jet maxima are derived from that inventory, not entered by hand:

```text
A_7, C_10, R_6, k10_6, k6_10, k2_6, p_10,
mu2_10, mu4_6, mu6_2.
```

Engine sentinels require nonzero grade-38 occurrences of both formerly
omitted extremes `A_7` and `k10_6`. All seven frozen literal rows bridge
modulo `sigma^39` to the independent Laurent/binomial emitter.

The target rows retain every licensed jet:

```text
row 2: grades 28..38, mu2 through mu2_10;
row 4: grades 32..38, mu4 through mu4_6;
row 6: grades 36..38, mu6 through mu6_2;
row 7: grade 38, J/4.
```

## Why the coefficients are forced

Put `s=p/2`, `Y(x)=sum h_(2m+1)x^m`, and
`Phi(x)=sum Phi_(2m+1)x^m`. The frozen Faber matrix is

```text
Phi(x)=(1-s*x)^(-1/2) Y(x/(1-s*x)).
```

A pole-`q` basis `x^e/(1+s*x)^q`, `0<=e<q`, becomes
`x^e(1-s*x)^(q-e-1/2)`. For terminal row seven (`M=3`) and pole ceiling
three, multiplication by

```text
(1-s*x)^(-1/2)
```

makes every such basis term a polynomial of degree at most two. Its first
four coefficients are precisely

```text
1, p/4, 3*p^2/32, 5*p^3/128.
```

Thus (R3) is a formal Laurent-to-ordinary identity, not an interpolation
from the `a>=13` order-two calculation. Substitution of the moving series
`p(sigma)` commutes with it.

## Uniform contact coverage

The source relation is polynomial in independent `theta,eta`; both exact
engines verify its `theta` and `eta` derivatives vanish modulo `sigma^39`.
Substitution `theta=sigma^n`, `eta=sigma^s` gives every integer
`a=10+n,r=a+s`. After common ramification, the same homogeneous argument
covers rationally valued arcs. Neither variable is inverted, and raising a
contact only delays the complete baseline support.

## AWS custody

Exact Q on Box03 and the independent `F_65521` software control on r6d each
return engine rc zero and validator PASS. Both print every required marker
exactly once, compiler stderr is empty, no rejected diagnostic occurs, and
both record zero swaps. Exact Q is the characteristic-zero endpoint;
`F_65521` is not used as a substitute for it. Full launch and resource data
are in `AWS_LAUNCH_METADATA.md`; every retrieved evidence byte is pinned by
`EVIDENCE.sha256`.

The Chebyshev/Pell identity is a nonempty engine heartbeat only. It is not an
input to the D1 obstruction.

## Firewall

This producer excludes only the registered D1 cone
`a>=10,c=a+1,r>=a` on `D(J)` for the seven literal source rows after the
cited upstream gates. It does not by itself cover `a<=9`, other D1 fan
cells, excluded lifecycle charts, the whole square component, order two,
`(8,12)`, maximum twelve, or JC2. Promotion requires fresh hostile review.
