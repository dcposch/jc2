# V18R1 r6a environment failure

The registered `p=65521` V18R1 preflight

```text
max12_812_order2_u2_62_k00_filtered_load_v18r1_p65521_20260827T111842Z_r6a
```

verified the frozen source and completed the repaired source audit and all
fifteen matrix emissions.  It then failed closed before any rank computation
because `g++` is absent on host `ip-172-30-0-34`:

```text
run_filtered_load_v18_aws.sh: line 42: g++: command not found
```

The immutable harvest is `aws_p65521_r6a_failed_no_gxx/`.  In particular,
`output/emitted/SOURCE_AUDIT.json` has SHA-256
`ab0cd9296bd19a6a6dfe862ed607f67ed1f6303337805da3cff48b75f689d93e`
and the compiler diagnostic has SHA-256
`4d3497475adefb728b5d9980bf55bca5e184d0932bc24df4fa230ad8b57c0153`.

This is an AWS software-environment failure, not a mathematical outcome.
It yields no rank, no filtered obstruction, and no characteristic-zero
inference.  The same frozen V18R1 bytes will be rerun on a host with the
required FLINT C++ toolchain; no algorithm or monomial order changes.
