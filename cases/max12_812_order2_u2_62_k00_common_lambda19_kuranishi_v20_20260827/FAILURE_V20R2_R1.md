# V20R2 R1 modular-evaluator failure

Date: 2026-08-27

The registered R1 lane

```text
max12_812_order2_u2_62_k00_common_lambda19_v20r2r1_20260827T124100Z_r6b
```

failed closed after exact source reconstruction and DAG emission but before
Singular or any source/type endpoint.  Both exact-Q fixtures agreed.  The
`F_65521` DAG evaluator converted constants and inputs into the prime field
but did not reduce intermediate additions and multiplications, then compared
the resulting integer representative directly against the reduced direct
evaluator.  The first reported mismatch was row 1, `Lambda^1`; it is a
representative-normalization bug, not evidence of a polynomial discrepancy.

R1 took 3.19 seconds, used 159,252 KiB maximum RSS, and emitted no PASS.
The full evidence, including its 140-root DAG, is preserved under
`aws_r6b_r1_failed/`.  R1 is permanently nonpromotable.

The R1 mathematical compiler SHA-256 was
`13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0`;
the wrapper SHA-256 was
`7bbbf96f1de34906399dc08f85388582b41feac53472c4d23a44b4013a06e5f6`.

