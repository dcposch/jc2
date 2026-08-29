# Ordered-`a1` constructive-cascade invalidation (V43C2)

Date: 2026-08-27

The proposed V43C1/V43C2 constructive tree does **not** currently prove
`a1^104` in the raw ordered-`a1`, `rho=0`, grade-through-19 ideal.  The final
right branch, advertised as modulo `G=e1-4*a1*ell1`, retains a nonzero
multiplier of the old assumption `e1`; the strict branch-combination rule
correctly rejects it.

The exact obstruction is replayed and fully scoped in
`cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION.md`.
Its smallest inherited factor (DAG root 170) expands over `Q` to 24,429
nonzero terms with polynomial SHA-256
`3c4dcc5f62f3c501f08581369525ca088b15a4ec3d3fa6f56251da288e229a72`.
The remaining geometric factor is nonzero because its `ell1=0`
specialization is `a1^36`.  Hence the complete crossed multiplier is nonzero
in the polynomial domain.

This withdraws only the explicit special exponent `M=104` and its conditional
total exponent `628` **from the uncorrected derivation**.  It does not touch
the reviewed V42 radical result or the exact generic identity
`5*t^6*a1^4 in J`.

The clean repair is an exact change of assumption basis before the second
branch clears `ell1`:

```text
e1=G+4*a1*ell1,       ee0=Q0-4*aa0*ell1.
```

This converts the inherited `(e1,ee0,ell1)` multiplier triple to
`(G,Q0,ell1)` exactly.  It must be implemented as a typed, serialized,
independently replayed rule with both signed-`4` mutations rejected; no
`M=104` claim resumes until the complete successor passes and is hostile
reviewed.

