# Uniform full-mode continuation through `D15`

Date: 2026-08-28  
Packet: `cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/`

## Verdict

**PASS for the A-adic cascade, with new live lower-window equations.**  From
the exact prefix through D13, put

```text
Delta7=F7-T/2-Q*Z/8-R*V/16.
```

The complete D14 polar coefficient is

```text
polar(g14)=3*Delta7^2/(8*A^2)+c14/A.
```

The order-two square cannot be canceled by the order-one forced mode.  The
raw congruence

```text
D14=-3*A*A'*Delta7^2 mod A^2
```

therefore gives `Delta7=A*U`.  The sole remaining pole is `c14/A`, so raw
polynomiality forces `c14=0`.

A causal firewall is essential here.  If `c14` is provisionally retained,
g15 contains `-c14/(4*A^3)`.  Its same-row D15 contribution is
`-3*c14*A'`, but the mixed contribution from the predecessor
`g14=c14/A` is `+3*c14*A'`.  Hence

```text
(-3*c14*A')+(+3*c14*A')=0.
```

D15 does **not** independently kill `c14`; that conclusion comes only from
D14 polynomiality after the square divisibility.  The checker asserts this
exact cancellation so the invalid standalone-successor shortcut cannot
reappear.

The literal G14 same-row matrix has shape 26 by 10, rank 10, and nullity
zero; no polynomial raw kernel realizes the rational `c14/A` mode.

After `c14=0`, define

```text
Delta8=F8-T*Z/8-Q*V/16-R^2/4.
```

Then

```text
polar(g15)
 =-3*U^2/(16*A^2)
  +U*(3*Delta8/4+c8/2)/A,

D15=+(3/4)*A*A'*U^2 mod A^2.
```

Thus `U=A*Y`.  The order-one term, including `c8*U/(2A)`, becomes
polynomial; D15 does not kill `c8`.  A literal polynomial continuation with
`c8=1` satisfies D4 through D15 and is replayed against all 513 source
generators.  The combined completion is

```text
F7=T/2+Q*Z/8+R*V/16+A^2*Y,
c14=0.
```

## Positive lower-window core

Raw G13, G14, and G15 all have lower degree one.  Their constant terms give
live necessary equations.  Write lowercase letters for X=0 jets and

```text
H0=c8/2+3*F8(0)/4.
```

Then

```text
C13 = q*H0-3*q^2*v/128-3*q*r^2/16+3*t^2/16+3*t*y/4 = 0,

C14 = t*H0-3*q^2*r/16-3*q*t*v/64-3*r^2*t/16
      -3*t^2*z/64+3*y^2/8 = 0,

C15 = y*H0-q^3/16-3*q*r*t/8-3*q*v*y/64-3*r^2*y/16
      -3*t^2*v/128-3*t*y*z/32-3*y^2/16 = 0.
```

C14 and C15 are new live scalar compatibilities, not eliminated branch
claims.  The form of `H0` is forced by the exact additive gauge

```text
F8(0) -> F8(0)+lambda,
c8    -> c8-3lambda/2.
```

The checker replays this at `lambda=-1,1,2`; all raw determinant rows remain
zero.  No gauge, endpoint carrier, or unit is normalized.

All nine characteristic modes remain serialized.  Only `c14` is derived to
vanish here; `c16,c18,c20` remain mandatory and unconstrained.  The packet
proves necessary characteristic-zero field-point statements only, not
scheme divisibility, endpoint exclusion, a Keller theorem, or JC2.
