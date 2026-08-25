# Registration — AS `B9` fixed-D12 successor through `Z/243`

- Registered UTC: `2026-08-25T16:14Z`, before execution.
- Parent: frozen producer-exact
  `cases/as_b9_max12_w3_survivor_aws_20260825/`.
- Execution: AWS only, dependency-free exact integer polynomial replay.

Put `u=x+y^3`.  First retain the parent `Z/27` pair and its `Z/81`
continuation

```text
P4 = u-u^3+18*u*y,
Q4 = y+u^4+3*u^2*y+72*y^2.
```

The registered `Z/243` candidate is

```text
P5 = P4 + 81*(2*u*y+x*y^2),
Q5 = Q4 + 81*(y^2+x^4*y^2+x*y^11).
```

The replay must verify every coefficient of both determinant congruences,
actual total and partial `y`-degrees at most twelve, reduction to `B9`, and
failure after omitting the whole new `81`-digit.  It must also verify the
mod-three linearized identities

```text
D(2*u*y,y^2)=u^4+y,
D(x*y^2,x^4*y^2+x*y^11)=y^2,
D(R,S)=R_x-u^3*R_y+S_y.
```

Scope is one explicit branch through `Z/243`, not the complete W2 fibre, a
compatible all-depth tower, a `Z_3`/characteristic-zero map, a counterexample,
a maximum-twelve theorem, TD6, or JC2.
