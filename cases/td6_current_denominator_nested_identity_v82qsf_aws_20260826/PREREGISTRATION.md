# V82QSF nested CURRENT-denominator identity preregistration

V82QSD exposed three common foreign factors `F,G,L` on q2 through q10.  This
source-light exact check tests whether they form a nested algebraic chain rather
than three unrelated divisor debts.

Over `Q[C,V,U]` it must verify

```text
G = V^4 + 4 F^2,
L = 4 U^3 G^2 + V^4 (V^2+4U^3) (V^2+2F)^2,
```

and the corresponding normalized identity on `D(U)`, with
`x=V^2/U^3`, `s=F/U^3`.  It also emits exact principal-ideal quotient controls
for `F=0` and the elementary certificate collapsing the apparent
`V^2+2F=0` branch inside `G=0` to `V=F=0` set-theoretically.

Run independently on two registered AWS hosts with a 1 GiB cap and a ten-minute
timeout.  This is a denominator/divisor diagnostic only.  It does not source-
lift a CURRENT coefficient, rebuild any raw fibre, or establish a cover,
obstruction, family, TD6, SP-2, landing, or JC2 statement.
