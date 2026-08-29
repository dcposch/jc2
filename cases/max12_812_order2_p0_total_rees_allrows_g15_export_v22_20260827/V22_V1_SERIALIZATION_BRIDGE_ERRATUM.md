# V22 V1 serialization-bridge erratum

Date: 2026-08-27

The dual V1 jobs failed closed before exporting or accepting any grade-15
polynomial:

```text
Q host/root:
  Box02
  /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827T031143Z_q
  compiler.stderr 82a2e39dcb095259f5a6f05441f4a5bdc18735f45c1168a95dfdbef2e582ee8c

F65521 host/root:
  r6d
  /home/ubuntu/jobs/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827T031143Z_p65521
  compiler.stderr 90773104847100b2fee905c0971643dd1f56e66492edff2bf28c14065f111623

shared source archive:
  9075246165a26ee361eb22b686e570afdcd4dc803eb16dd55132eb2c33c8657c
```

Both failed at the first V9 historical bridge because V1 compared polynomial
**text**, despite the preregistration's mathematical obligation being exact
polynomial equality.  The two strings were

```text
V22 reconstruction:
(3/8)*a0*c1+(3/8)*a1*c0+(15/256)*cs*k*rs^2+(5/16)*cs^3*k*rho^2

V9 reference:
5/16*rho^2*cs^3*k+15/256*cs*rs^2*k+3/8*a0*c1+3/8*a1*c0
```

They are the same polynomial; only term/factor order and rational-parenthesis
format differ.  No mathematical discrepancy was observed.  V1's later
ordinary-Singular control already tests the correct semantic equality for all
35 historical coefficients, but the premature string gate prevented that
control from running.

R1 preserves every V1 source byte and wraps its compiler so that only this
named text-order failure is deferred to the mandatory 35-polynomial Singular
equality gate.  Every other fail-closed check remains fatal.  R1 reports the
number and labels of serialization deferrals and changes the result field
from `byte_bridges` to `exact_polynomial_bridges`.

