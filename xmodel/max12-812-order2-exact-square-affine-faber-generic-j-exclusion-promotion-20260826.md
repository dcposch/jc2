# Promotion: generic affine-Faber complete-local `J` exclusion

Date: 2026-08-26

Status: **PROMOTED, NORMALIZED ORDINARY-FABER COMPLETE-LOCAL SCOPE ONLY.**

## Charged theorem and review

```text
fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md

08a6bec022613a1d26ac64a5685e6408e875423b609c50fee604326fbb5a15dc
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-hostile-review-grok-20260826.md
```

The different-model hostile review independently reconstructs the centered
octic square-division coordinates, parity argument, ordinary-Faber
differential, the full odd Jacobian block, its determinant, and the formal
implicit-function argument.  Its verdict is `CONFIRMED`.

## Promoted statement

On the corrected non-square exact-square affine-Faber graph, put

```text
D=(p^2-4*r)/4,                  s=5*D-4*beta.
```

In the completed centered ordinary-Faber coefficient chart with `k10=1`,
on

```text
U=D(D*(5*D+2*s)*(5*D-2*s)),
```

the zero-target odd rows `(R1,R3,R5)` generate the full odd-coordinate
ideal `(c,u,n3)`.  Parity then gives `R7=0`, so after adjoining
`J-4*R7`, saturation by `J` is the unit ideal.  No `J`-nonzero formal,
ramified, or nilpotent arc in this normalized completion specializes to a
point of `U`.

The determinant is exactly

```text
-25*D^3*(5*D+2*s)*(5*D-2*s)^2/2^17.
```

Thus, on `D(D)`, normalized `J` accessibility is confined to the disjoint
resonances

```text
A: 5*D+2*s=0,                  K: 5*D-2*s=0.
```

Both first-order kernel spaces are `R7`-null; neither exceptional face is
classified by this promotion.

## Firewall

This promotion does not identify the normalized completion with a literal
source/total-Rees chart.  It does not supply a two-sided `k10`
normalization, retain arbitrary moving-center directions, classify `A` or
`K`, treat `D=0` or `k10=0`, impose terminal `[6,2]` or either Taylor
family, or close the square branch, order two, `(8,12)`, maximum twelve,
or JC2.
