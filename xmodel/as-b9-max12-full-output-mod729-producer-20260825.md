# AS B9 complete fixed-D12 output digit survives modulo 729

Status: **producer-exact / dual-AWS same-implementation replay / hostile
review pending**.

The frozen B9 branch through modulo 243 was extended using the complete fresh
fixed-D12 output cone, rather than its earlier structured primitives.  For
the literal parent `(P5,Q5)`, the producer introduced all 91 monomials of
total degree at most twelve in each order-243 correction `(R,S)` and imposed
all 276 determinant rows of total degree at most 22:

```text
(det J(P5,Q5)-1)/243 + L_G(R,S) = 0 mod 3.
```

The exact `276 x 182` system has rank 108 and is consistent, with affine
kernel dimension 74.  The uncorrected parent fails modulo 729.  The selected
solution reconstructs an integer pair with determinant one modulo 729 in
every coefficient; its actual total degrees are `(11,12)` and its actual
partial `y`-degrees are `(9,12)`.  Thus the maximum-twelve support cap is
preserved.

## Exact custody

- solver source SHA-256:
  `4deb7fe07acef4f37bb14735493b0d20b6c7ac66bb10633f81b7bc1a48264bd4`;
- source-closure SHA-256:
  `c9ea6b8c321f911a4291167e454064683fb2ae5a229bed87afc70dadfb58a00f`;
- affine matrix SHA-256:
  `f99150e22eefb3d71fbb170e66fac01caf925cb4855cfd52ea8f70ff0cf04d0f`;
- RHS SHA-256:
  `1522a8874f86b81e268840237e7632409924563aea59c2bb764528626b2a71a6`;
- result JSON SHA-256:
  `d267a2b5f4d7f6fd8d0535857923cd8f842322aa59d1a4b5bbd520f3a13a52dc`;
- determinant payload SHA-256:
  `3532f443ce53b2784162077332f6ec347278b167762183a910eeb67e229f17b5`;
- byte-identical stdout SHA-256:
  `102c1666f85d35db129fa4bad230697050ee26ceeb88a8e1c8a99b367730cbbe`.

The same source and result bytes ran on:

- Box02, `/home/ubuntu/jobs/as_b9_d12_full_output_mod729_20260825T1620Z`,
  `rc=0`, 17,656 KiB maximum RSS, 0.08 seconds;
- Box03, `/home/ubuntu/jobs/as_b9_d12_full_output_mod729_20260825T1620Z`,
  `rc=0`, 18,852 KiB maximum RSS, 0.08 seconds.

These are independent executions of one implementation, not independent
implementations.

## Scope firewall and successor

The complete claim is only the fresh order-243 output digit over one explicit
B9 mod-243 point.  It is not the complete mod-243 fibre, a compatible
all-depth tower, a `Z_3` or characteristic-zero polynomial map, a
counterexample, a maximum-twelve theorem, TD6, or JC2.

The immediate successor recomputes the divided residual of this literal
mod-729 point and the same complete 182-column operator for modulo 2187.
Continuation of one point remains witness-first; any exclusion of its full
74-dimensional fibre requires the next Bockstein/Kuranishi projection rather
than failure of a stored particular.
