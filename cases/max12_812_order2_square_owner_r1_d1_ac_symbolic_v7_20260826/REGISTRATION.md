# Registration: `r=1` / symbolic-`d=1` V7 exponent-context repair

Date: 2026-08-26

V6 replaced the nested substitutions by four linear chart ideals, but
Singular still emitted `poly ^ number` on the first ideal declaration.  V7
pins V6 and, only inside the six-line root-chart block, replaces all powers
`rtx^2`, `cv^2`, and `theta^2` by explicit products.  This avoids the
context-sensitive exponent overload without changing any polynomial.

All source rows, coefficients, validators, scope, and dual-AWS caps are
unchanged.  Failure is no mathematical verdict.
