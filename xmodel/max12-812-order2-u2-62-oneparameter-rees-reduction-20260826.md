# `(8,12)` order two, `U=2,[6,2]`: exact one-parameter Rees reduction

Date: 2026-08-26

Status: **EXACT PRODUCER REDUCTION; PROVISIONAL PENDING HOSTILE REVIEW.**

## 0. Statement

In the source-typed strict-Rees client for the order-two `U=2,[6,2]`
profile, localize at the unit `R=1+tau`.  Retain all seven finite load
variables.  After the changes

```text
C_i=B_i                         (i even),
C_i=R B_i                       (i odd),
J=R j,
Lambda=tau^3 varrho,
```

the complete seven-row family is the flat toric pullback of the
one-parameter family

```text
Phi_ell =
 r_ell(C, Lambda^2 k10, Lambda^6 k6, Lambda^10 k2)
 - Lambda^(12+ell) delta_ell,

delta_1=delta_3=delta_5=0,
delta_2=mu2, delta_4=mu4, delta_6=mu6, delta_7=J/4.    (0.1)
```

Consequently the original sequential interior saturation by
`tau,varrho,j`, followed by the boundary `tau=varrho=0` and coefficient-
irrelevant saturation, has exactly the same boundary scheme as saturation
of `(Phi_1,...,Phi_7)` by `Lambda,J`, followed by `Lambda=0` and saturation
by `(C0,...,C6)`.

This is a reduction of the exact finite-load boundary problem, not a
projection of the loads.  It does not decide whether that boundary is empty.

## 1. Frozen source

The source-typed client, its nonmutating `j!=0` erratum, and the independent
V2 compiler review have SHAs

```text
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7
5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b
b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d.
```

The exact seven tails are frozen in `tails.json` at SHA

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848,
```

with canonical all-tail digest

```text
6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8.
```

The emitted V2 two-parameter input has SHA

```text
021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c.
```

The dual AWS attempts at that input both timed out after four hours with no
mathematical sentinel; see the immutable timeout packet at SHA
`fa8ef6c68f5f48e545ac7076da846df150007d9206370e3a25dfc5422b60b708`.

## 2. Row identity

The original client defines the ordinary coefficients by

```text
C_i=R^(i mod 2) B_i
```

and evaluates the ordinary tails at the three scaled lower Faber loads

```text
tau^6 varrho^2 k10=(tau^3 varrho)^2 k10,
tau^18 varrho^6 k6=(tau^3 varrho)^6 k6,
tau^30 varrho^10 k2=(tau^3 varrho)^10 k2.
```

Every target scale likewise satisfies

```text
tau^(3(12+ell)) varrho^(12+ell)=Lambda^(12+ell).
```

For the terminal row, `gamma_7=(j/4)R=J/4`.  Thus all seven original
`Psi_ell` become exactly (0.1); no division by a coefficient variable or
load is used.  The change from `(B,j)` to `(C,J)` is an automorphism after
localizing at `R`, and `R` is a unit in the formal chart at `tau=0`.

The exact tail construction is affine-linear in `k10,k6,k2`, because
`g=F12+k10 F10+k6 F6+k2 F2`.  This linearity is a useful successor
optimization but is not needed for the base-change theorem.

## 3. Flat base change and saturation

Let

```text
A=Q[Lambda,C0,...,C6,k10,k6,k2,mu2,mu4,mu6,J]
```

and let `I0=(Phi_1,...,Phi_7)`.  After the unit coefficient change, the
two-parameter ring is obtained from the base map

```text
Q[Lambda] -> Q[tau,varrho,(1+tau)^(-1)],
Lambda |-> tau^3 varrho.                              (3.1)
```

The target of (3.1) is a domain and hence torsion-free as a module over the
PID `Q[Lambda]`; it is therefore flat.  Polynomial extension by the retained
coefficient and load variables, followed by the unit automorphism, preserves
flatness.

On this unit chart

```text
D(tau varrho j)=D(Lambda J).
```

Indeed `Lambda J=tau^3 varrho Rj` and `R` is invertible.  Principal
saturation commutes with flat extension (the ascending colon chain stabilizes
Noetherianly).  Therefore

```text
(I0:(Lambda J)^infinity) B
 = (I0 B:(tau varrho j)^infinity).                    (3.2)
```

Sequential saturation by the three factors equals saturation by their
product, so (3.2) is also the exact V2 interior saturation.

Finally, quotienting the right side by `(tau,varrho)` sends
`Lambda` to zero, `R` to one, `C_i` to `B_i`, and `J` to `j`.  Hence its
boundary fibre is canonically the quotient of the left side by `(Lambda)`.
At that fibre the coefficient-irrelevant ideals `(C0,...,C6)` and
`(B0,...,B6)` coincide, so the final irrelevant saturation also agrees.
This proves the scheme-theoretic statement of Section 0, including
nilpotents and every finite load variable.

## 4. Why load projection is forbidden

Although `Phi_2,Phi_4,Phi_6,Phi_7` solve generically for
`mu2,mu4,mu6,J`, eliminating those variables before closure is not licensed:
their quotients may acquire poles at `Lambda=0`.

The smallest exact negative control is

```text
I=(x-Lambda*m) subset Q[Lambda,m,x].
```

The finite-`m` graph is already `Lambda`-saturated and its boundary has
`x=0`.  On `D(Lambda)`, however, projecting away `m` gives the zero ideal;
closing that projection makes every boundary `x` survive.  Thus a generic-
chart projection can strictly enlarge the Rees boundary.  The one-parameter
client must retain the scaled load variables, or equivalently impose all
finite-quotient/divisibility jets before specialization.

## 5. Computational consequence and next gates

The exact client now needs one Rees parameter and two principal
localizations, with exponents at most nineteen, instead of two parameters,
three localizations, and separate exponents as high as `57` and `19`.
The first AWS race should compare exact Q and good-prime endpoints with
sentinels after the `Lambda` saturation, after the `J` saturation, and after
the irrelevant saturation.

If the one-parameter monolith remains large, exploit load linearity without
projecting: expand every row in `Lambda` and impose the finite-quotient
conditions coefficientwise.  Equivalently, use the odd-row `3 x 3` system in
`k10,k6,k2`, stratify by its determinant/minors, and retain the exact
divisibility orders `14,16,18,19` for the four target loads.  Compile both
branch-point Taylor families only on the surviving strata.

The all-lower-load-zero sub-stratum is already excluded independently by
the Hall/Shioda divisor-19 argument because `r7=(j/4)T` has divisor orders
`+1,-1`; it is a prefilter, not order-two closure.

## 6. Firewall

This theorem is conditional on the frozen source-typed strict-Rees client
and retains every finite load.  It proves equality of two algebraic boundary
schemes; it proves neither is empty or realizable.  It does not solve either
finite Taylor family, exclude the fixed `[6,2]` source, close order two,
close `(8,12)`, prove maximum twelve, or prove JC2.
