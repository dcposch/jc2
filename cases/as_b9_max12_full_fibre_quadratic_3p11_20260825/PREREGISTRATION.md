# Preregistration — B9 first quadratic full-family gate at `3^11`

Date: 2026-08-25

Consume the full fixed-D12 affine family modulo `3^10` from source SHA-256
`0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7`.
For

```text
F = F5 + 243*T + 3^10*W,
```

compile every one of the 276 divided determinant rows modulo three:

```text
(D5 + 243*A*T)/3^10 + det J(T) + A*W = 0 mod 3.
```

The 165-dimensional predecessor family and all 182 fresh digits are required.
First eliminate `W` by the exact rank-108 operator and its full left cokernel.
Then change predecessor coordinates so only an independent basis for
`T mod 3` carries quadratic terms; all remaining directions are exact
carry-linear spectators.  Eliminate those spectators before emitting the
reduced quadratic ANF/QF_BV system.  Preserve nil/rank-zero ambient rows.

Test only source-derived linear zero strata and zero/basis active assignments
as positive finders.  Do not enumerate `3^165`.  SAT is accepted only after
reconstructing all predecessor and fresh digits and replaying every integer
determinant coefficient modulo `3^11=177147`.  UNSAT requires an independently
checked certificate.

This covers one displayed full modulo-`3^10` family over one fixed B9
mod-243 point.  It is not an all-depth branch, characteristic-zero point,
counterexample, maximum-twelve theorem, or JC2.
