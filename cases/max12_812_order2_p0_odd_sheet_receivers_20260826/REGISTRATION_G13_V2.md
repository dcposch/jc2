# Registration: grade-13 polynomial/Jacobian navigation V2

Date: 2026-08-26

The V1 factor-DAG degree bound did not license affine-linear rank arithmetic.
V2 specializes all predecessor parameters at deterministic points of
`D(b*w*a1)` satisfying the raw predecessor equation `F=0`, but retains

```text
ell3,cs2,rs2,az2,ac2,ez3,ec3,k10_2
```

as an explicitly collected polynomial over `F_32003` or `F_65521`.  It
cross-checks every grade-13 polynomial value and first derivative against an
independent dual-number pass through the frozen factor DAG.  It records the
actual specialized degrees, term counts, Jacobian rank, dependency masks,
and the values of rows six and seven, whose structural masks are zero in the
eight registered corrections.

Four samples per prime are navigation.  A nonzero modular evaluation proves
only that the corresponding collected source polynomial is not identically
zero after that modular specialization.  It does not solve its vanishing
locus, prove incompatibility with the predecessor sheet, cover exceptional
divisors, establish Gate A, or give an order-two/JC2 conclusion.

Required sentinels are

```text
P0_ODD_G13_V2_SOURCE_HASHES=PASS
P0_ODD_G13_V2_POLY_DUAL_CROSSCHECK=PASS
P0_ODD_G13_V2_STATUS=PASS_MODULAR_POLYNOMIAL_NAVIGATION
```

