# Affine-Faber `A` half-weight tau-90 replay V2

Date: 2026-08-26

V2 is the deployment-only repair of the frozen V1 half-weight client.
V1 failed before source substitution because Singular did not accept
power-followed-by-division coefficient syntax in the independent Faber
connection control.  V2 rewrites only those finitely listed expressions
from forms such as `cb^2/32` to `(1/32)*cb^2`.

The ramification, all source substitutions, retained correction and load
jets, seven rows, coefficient windows, inverse `H3,H5` connection,
preregistered identities, localization, endpoint, and scope are byte-for-
byte inherited from the V1 emitter after this spelling repair.  The V2
compiler requires each bad spelling exactly once and refuses any drift.

Preregistered endpoint:

```text
A_HW90_H3_G90 = -(3/8)*m*x*y-(1/16)*m^3,
A_HW90_H5_G90 =  (3/8)*p*m*x*y,
A_HW90_UNIT=1,
A_HW90_ENDPOINT=PASS_COMPLETE_SOURCE_HALFWEIGHT_UNIT.
```

Exact Q is mathematical evidence.  Characteristic 65521 is a software
control.  V1 remains deployment-negative and supplies no evidence.

Scope is exactly the V1 `q=15/2`, `D(p*m*kk)`, through-tau-90 scope.  No
`q>15/2`, terminal, Taylor, order-two, or JC2 statement is registered.
