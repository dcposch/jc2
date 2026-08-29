# V1 fail-closed result: wrong lower-load tail alignment

Date: 2026-08-26

Status: **DUAL-AWS FAIL-CLOSED NEGATIVE CONTROL; NO MATHEMATICAL VERDICT.**

Both exact-Q and `F_65521` runs compiled and returned Singular `rc=0`, but
the fail-closed validator rejected `A6_ROW_IDENTITIES_24=0`.  The exact-Q
row remainders are

```text
row 1: -(3/4)c0*k60 +(3/4)c1*k60
row 2:  (3/8)p*c1*k60 +(3/4)c0*k60
row 3:  (3/16)p*c0*k60 -(3/16)p*c1*k60
row 5:  (3/128)p^2*c0*k60 -(3/128)p^2*c1*k60
row 7:  (3/512)p^3*c0*k60 -(3/512)p^3*c1*k60.
```

All source quotient/support markers and the grade-23 row bridge passed.
The failure isolates the analytic generating-series encoding of the new
`k6*C/L` term: V1 used `t*C*Inv1`, but the exact source rows begin

```text
g1=(3/4)k60*c1,  g2=(3/4)k60*c0,
```

which is the lower-unitriangular image of `t^2*C*Inv1`.  This is a tail-row
alignment error in the new analytic comparator, not evidence for or against
the D1 contact.  V1 remains immutable and supplies no theorem.

Exact stdout SHAs are

```text
ffb45c2802d57037bc20d25ed7c3f86ff34baaa922ec11d593d61aa5f335d984  Q
d2cb6b8a0d3ed46d1e8dd6f36f7660abd696376e6d836a6af62ba0f42584f652  F_65521
```

Both validation files have SHA
`5b8530e6476f1395043e0ff7e6988a1feedce02ab55bf95e94316440ec89b3ba`
and end with
`validator=FAIL_MISSING_OR_NONUNIQUE:A6_ROW_IDENTITIES_24=1`.

