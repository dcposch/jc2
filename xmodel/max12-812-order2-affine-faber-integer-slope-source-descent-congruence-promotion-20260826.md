# Promotion: integer-slope source-descent congruence

Date: 2026-08-26

Status: **PROMOTED AT FIXED RATIONAL-GERM / LEADING-VALUATION SCOPE.**

## Frozen theorem and review

```text
596bf3260038885c917d12203e72f3892a987d8eb324f01cffe9ca967005dde0
  xmodel/max12-812-order2-affine-faber-integer-slope-source-descent-congruence-theorem-20260826.md

c34ab2e96a9c13932816450dbad3d820002e780126174112d40da6e44e2ca69c
  xmodel/max12-812-order2-affine-faber-integer-slope-source-descent-congruence-hostile-review-grok-20260826.md
```

The independent review verdict is `CONFIRMED`.

## Promoted statement

For an actual rational coefficient germ at either unramified infinity
place, on an integer strict ray

```text
Lambda=tau^alpha*(unit),       alpha>3,
```

if the exact monic-square remainder has finite normalized order
`ord_sigma(Delta)=H` with `sigma^3=Lambda`, then

```text
3 divides alpha*H.
```

On the balanced slope-four ray this forces `3|H`; in particular the H16
and H17 normalized cells do not descend to a fixed rational germ on that
ray, while H15 and H18 pass this necessary leading-order test.

## Full-series firewall

Leading-order congruence is not sufficient.  Under
`tau=s^3,sigma=s^4`, a full normalized series descends only if it is fixed
by `s -> zeta_3*s`; equivalently every surviving exponent has the required
congruence and the series lies in the appropriate `L[[sigma^3]]` module.
Generic normalized IFT jets do not satisfy this automatically.

The reviewed H17 Gate-A composition remains a correct ramified formal
source-row point over `L((s))`; this promotion says it is not a fixed
`L((tau))` rational germ.  It does not rule out other toric slopes or
families with independent deformation constants, prove a full fixed-locus
lift, impose Taylor polynomiality, close order two, `(8,12)`, maximum
twelve, or JC2.
