# Grade-13 V1 deployment negative

Date: 2026-08-26

The frozen V1 client (`FREEZE_G13.sha256`, SHA-256 prefix `6f29be28`)
was deployed independently at primes 32003 and 65521.  Both lanes stopped at
the preregistered affine-linearity gate before rank arithmetic:

```text
grade-13 DAG degree upper bounds in registered corrections:
[3,2,2,1,1,0,0]
```

The deployments were:

```text
max12_812_order2_p0_odd_g13_p32003_20260826T100913Z_Box03
max12_812_order2_p0_odd_g13_p65521_20260826T100913Z_r6d
```

Each returned `rc=1`, `validator=FAIL_ENGINE` after about 6.5 seconds and
about 350 MiB peak RSS.  This is a deployment-negative result, not a
mathematical failure and not proof that the source rows are genuinely
nonlinear: the DAG degree is only an upper bound until cancellations are
collected.  It does show that the V1 affine premise was not licensed by the
factor-DAG representation.  The V1 bytes and remote stderr are retained.

V2 must collect the polynomial in the eight registered corrections after
specializing predecessor parameters, cross-check polynomial values and
derivatives against an independent dual-number evaluation, and report only
modular navigation.  In particular, rows six and seven have zero structural
dependency mask in these eight corrections and are candidate next
constraints, not yet proved nonzero or globally meaningful.

