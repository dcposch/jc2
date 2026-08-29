# Preregistration: cutoff-four square-tail desk lane

Date: 2026-08-28  
Status: `FROZEN BEFORE EMISSION`

## Source and specialization

The sole determinant authority is

```text
../ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json
SHA256 ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
```

and the raw-slot weight inventory is

```text
../ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
SHA256 28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
```

Set every raw deformation parameter of weight below four to zero.  Rebuild
the nullspace of the literal rows `D0,...,D7` over `Q`, substitute that
nullspace into the literal rows `D8,...,D22`, and impose no `D23` equation.

## Frozen method

1. Use only Python standard-library `Fraction` arithmetic.
2. Track every compatibility row back through exact RREF operations to the
   literal determinant generator index and `(row,x_degree)` label.
3. Test the expected square-remainder pattern with
   `C=X^4-1` and `H=C^2`; do not infer a higher-cutoff identity.
4. Every passage from `P^2=0 mod C` to `C|P` is explicitly a
   characteristic-zero field-radical implication, not a scheme equality.
5. Preserve all four endpoint carriers.  A monic carrier formula may be
   used for continuation, but no carrier may be set to one or inverted.
6. Stop at the first honest residual if the next implication is not supplied
   by an exact span certificate.  Any broad Groebner computation must be
   packaged for AWS rather than run locally.

## Preregistered checks and mutations

- Pin both source hashes and the exact prefix counts/rank/nullity.
- Pin the literal `D22[X^0]-1` endpoint and carrier lifts.
- At `D8`, recover the seven-dimensional pure quadratic space and its
  one-dimensional remainder kernel; verify that the kernel is the `C` line.
- At every later divisibility step, emit the compatibility-space and literal
  source-row cofactors for each coefficient of the claimed remainder.
- Delete an essential compatibility row and require a named inclusion to
  fail.
- Reverse the half-shift in a square model and require inclusion to fail.
- Delete the quadratic term in the monic `p86` carrier formula and require a
  nonzero named difference.
- Reverse one endpoint sign and require mismatch with the literal source.

## Scope firewall

A contradiction, if found, excludes only characteristic-zero field-valued
points of this fixed cutoff-four square-tail specialization.  Radical
parameterizations do not prove a unit in the unreduced upstream scheme, and
this lane alone says nothing about the full branch-P family or JC2.
