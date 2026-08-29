# Deployment-negative V1 custody

Date: 2026-08-26

V1 was stopped manually on both AWS lanes before any mathematical endpoint.
The generated Singular ring used `k0,...,k6` for moving `K10` jets while
also retaining the frozen source generators named `k2,k6,k10`.  Singular
printed the explicit conflicts

```text
name conflict ... `k6`, rename to `@k6`
name conflict ... `k2`, rename to `@k2`
```

so subsequent `subst(P,k6,...)` and `subst(P,k2,...)` were not source-safe.
No V1 row, ideal, or endpoint is evidence.  The process was terminated
fail-closed.  The only custody value is the exact input archive:

```text
source archive SHA256:
  393c666d4b2218c7e18b0bae16ce9989ffebafc2bfd6d842813bf74bc8165a81
V1 FREEZE.sha256 file SHA256:
  1c41a99212726f89be30a575b00747c85cdef3bd7c0da3b8ffb81bc5d92cee81

Box03 tag:
  max12_812_order2_affine_faber_a_h16_q6_a4_g48_20260826T1805Z_q_v1
r6d tag:
  max12_812_order2_affine_faber_a_h16_q6_a4_g48_20260826T1805Z_p65521_v1
```

V2 changes only the moving-`K10` jet names to `kk0,...,kk6`, leaving the
mathematical substitutions, valuation window, targets, and validators
unchanged.
