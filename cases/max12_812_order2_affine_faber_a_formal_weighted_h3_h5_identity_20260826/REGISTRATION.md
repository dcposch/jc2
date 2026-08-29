# Formal weighted affine-Faber `A` `H3/H5` identity

Date: 2026-08-26

Status: preregistered exact-Q producer; no result is assumed.

This is the controlling repair for the moving-center truncation identified
by the hostile review of the literal `q=6` jet producer.  It substitutes
independent formal variables into all seven frozen complete ordinary-Faber
tails, rather than setting `a=s^5*a5` with no later center jets.

Put `A=z-a`, `B=4a`, `D=A^2+B*A+E`.  In weighted form the exact coefficient
map is

```text
Q=A^2*D + X*A + R1*A + R0,
N=lambda*(M*A*D + Y*A + M*X/2 + S1*A + S0),
```

with weights

```text
a:5, X:Y:6, R1:R0:S1:S0:12, lambda:15,
k10:k6:k2:mu2:42, E:M:0.
```

Here `lambda` means the full normal scale, implemented as `t^15*lam`; the
symbols `lam,E,M,a,X,Y,R,S` are algebraically independent.  The compiler
forms the exact inverse-Faber `H3,H5` rows and checks modulo `t^46`

```text
H3=-(3/8)t^42*lam^2*M*X*Y-(1/16)t^45*lam^3*M^3,
H5= (3/8)t^42*E*lam^2*M*X*Y.
```

It also checks `[t^45](E*H3+H5)=-lam^3*E*M^3/16`.  This is an identity
before imposing any predecessor source row.  Because the congruence is
polynomial in every displayed symbol, substitution of arbitrary power
series for the symbols preserves it and includes every later moving-center
jet (including the omitted `a6`), tangent jet, kernel jet, and complement
jet that can meet weight 45.  Raising the weights of `X,Y` covers every
`q>=6` after common ramification.

The exact coefficient map/two-sided source chart and the separate `q<6`
homogeneous face remain theorem gates.  Exact Q is mathematical evidence;
F65521 is only a software control.  No claim is made for `m=0`, another
load slope, terminal/Taylor, total fan, order two, or JC2.
