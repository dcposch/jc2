# V7 deployment-negative: nonlinear leading-face finite differences

Date: 2026-08-26

Status: **FAIL-CLOSED; NO MATHEMATICAL VERDICT.**

Both exact-Q Box03 and F65521 Box02 stopped at recursion index zero on the
same control.  V7 attempted to recover the leading-face Jacobian by finite
differences from the zero vector.  The grade-48/51 leading system is
nonlinear in its simultaneous leading variables, so those finite
differences are not derivatives and the affine test correctly failed.

The failure occurs before any solve or prolongation assertion.  It does
not alter the frozen V6 grade-51 reduction.  The repaired client must fix
the exact V6 leading solution first, verify it directly, and begin the
new-coefficient affine recursion at positive index, where the standard
formal coefficient lemma applies.

Observed exact-Q mismatch:

```text
actual    = (3/2,-3/4,165/512,-131/128,-243/32,3585/128,8)
predicted = (3/2,-3/4, 21/512,-419/128,-207/32,2433/128,8).
```

The modular lane gave the coefficient reduction of the same discrepancy.
