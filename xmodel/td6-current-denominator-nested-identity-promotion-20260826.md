# Promotion: nested TD6 CURRENT-denominator identities

Date: 2026-08-26

Status: **HOSTILE-REVIEW CONFIRMED AS DENOMINATOR-DIVISOR ALGEBRA ONLY.**

Let

```text
F=C*U-V^2+U^3
```

and let `G,L` be the literal foreign factors printed by the reviewed V82QSD
CURRENT denominator diagnostic.  In `Q[C,V,U]` one has exactly

```text
G = V^4+4F^2,
L = 4U^3G^2+V^4(V^2+4U^3)(V^2+2F)^2.
```

On `D(U)`, put `x=V^2/U^3`, `s=F/U^3`, and `g=x^2+4s^2`.  Then

```text
L/U^15
 = 64s^4+4x^2(x+12)s^2+4x^3(x+4)s+x^4(x+8)
 = 4g^2+x^2(x+4)(x+2s)^2.
```

The exact specializations are:

```text
F=0:  L=V^8(V^2+8U^3),
G=0:  L=V^4(V^2+4U^3)(V^2+2F)^2.
```

For `A=V^2+2F`, the identity

```text
G-A^2+2*A*V^2=2V^4
```

shows set-theoretically in characteristic zero that `G=A=0` forces
`V=F=0`.  The exact normalized radical of the `G=L=0` intersection is

```text
rad(g,L/U^15)=(x,s) intersect (x+4,s^2+4).
```

Thus the earlier shorthand `x=0_or_x=-4` records only the `x`-support:
`s=0` at `x=0`, while `s^2=-4` at `x=-4`.

Producer report/manifest/freeze SHAs are `ef88290d...`, `1c2a1070...`, and
`a5dabcd1...`.  The independent hostile-review SHA is `a3e13150...`, verdict
`TD6_CURRENT_DENOMINATOR_NESTED_IDENTITY_CONFIRMED`.

These identities turn the exceptional denominator geometry into a recursive
atlas, but they do not factor `L` as a product globally.  The generic
`L=0,D(UVFG)` hypersurface remains a genuine debt.  Nothing here establishes
a CURRENT coefficient, numerator cancellation, alternate-minor cover,
source-fibre theorem, rank, family, Kuranishi map, TD6, SP-2, landing, or JC2.
The live successor is the fraction-free/alternate-pivot CURRENT conormal
calculation followed only as needed by original-source factor-stratum clients.
