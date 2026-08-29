# V1 deployment-negative custody

Both V1 AWS lanes compiled, but Singular parsed the unparenthesized
substitution `p^2/4-D` as a nonintegral exponent and emitted
``poly ^ number failed``.  The process exit code was zero, but the diagnostic
validator correctly rejected each lane.  Every displayed zero and endpoint
after that parse error is inadmissible and has no mathematical status.

V2 changes only Singular parenthesization of powers followed by rational
division.  It preserves all rows, variables, faces, and endpoint tests.

```text
exact-Q tag:
  max12_812_order2_affine_faber_exceptional_p3_20260826T131842Z_q
F65521 tag:
  max12_812_order2_affine_faber_exceptional_p3_20260826T131842Z_p65521
```
