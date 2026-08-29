# V20R2 R0 pre-algebra wrapper failure

Date: 2026-08-27

The first registered r6b launch

```text
max12_812_order2_u2_62_k00_common_lambda19_v20r2_20260827T123800Z_r6b
```

failed closed before source reconstruction, DAG emission, Singular, or any
mathematical calculation.  The wrapper created `$AWS_JOB/output`, while the
compiler deliberately requires its output path not to exist.  Python raised
`FileExistsError` in `Path.mkdir(exist_ok=False)`.

The failure took 0.19 seconds, used 34,880 KiB maximum RSS, and emitted no
producer stdout or mathematical endpoint.  The complete wrapper evidence is
preserved under `aws_r6b_r0_failed/`.  This lane is permanently
nonpromotable.

The frozen mathematical compiler SHA-256 was
`13342b16367b347680d6cbb4fb726798b7c1904422b10a661f31f5b7b59974b0`.
The failed wrapper SHA-256 was
`f6332a9d4535b3731b097f4b54747ba87ed52fcf2c627fc313bc0877d35819d1`.

