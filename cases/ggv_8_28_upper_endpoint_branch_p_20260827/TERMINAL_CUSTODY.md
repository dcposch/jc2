# Terminal custody: superseded raw and reducer pilots

Date: 2026-08-27

These two terminal outputs predate the fail-closed `EXIT` evidence hook in
`run_aws.sh`.  They remain byte-untouched in their original Box03 namespaces.
This note records the independently recomputed hashes needed to preserve their
telemetry; neither terminal run returned an algebraic result.

## Exact literal raw `std/lp` pilot

Namespace:

```text
/home/ubuntu/jobs/ggv_8_28_upper_endpoint_branch_p_20260827T185111Z_compile_reduce_v1/output_exact_raw_v1
```

The frozen compiler check passed for 303 variables, 513 generators, 18
`D22` coefficients, raw system SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`,
and Singular source SHA-256
`8647c6e73c9e23dde69cbe63b264e7e9465616ca2caad2d807d380ee5ce3d02d`.
Singular terminated with `halt 14: no more memory` under the 128-GiB VM cap.
`/usr/bin/time -v` records elapsed `2:06:09`, maximum RSS `134197860` KiB,
and zero swaps.

```text
dedd9ffca463fb880bc0c71efcb724977cbebdea856b708e5b1ced2a13f43aca  METADATA.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  RUN_STARTED
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  compile_check.rc
f6e3d2b3c58e736121a0047e8b99f2f082acbb523539c0e11e1d1bf8339ff31c  compile_check.stderr
4ffe9091bda3f4661ef8e9cc570abf66d8d6dfa51eb9b43b234183717c630159  compile_check.stdout
9a92adbc0cee38ef658c71ce1b1bf8c65668f166bfb213644c895ccb1ad07a25  exact_raw.rc
0d7ff9d0badf0014af0644670f0b862e184b2f06a84ac12bec554178b29e2894  exact_raw.stderr
48cf0dede587f8c4efb176009d7c8b7454851c539693822897270601a4775b08  exact_raw.stdout
13bd6e55cb8d16213090b238ce9c3313a48635b01c4a253c22928b9ea2d7d2a6  source_check.stdout
```

## Exact triangular reducer pilot

Namespace:

```text
/home/ubuntu/jobs/ggv_8_28_upper_endpoint_branch_p_20260827T185111Z_compile_reduce_v1/output
```

This process was terminated fail-closed with `SIGTERM` after it produced no
row-progress or output bytes while its expanded exact expressions reached
`182775728` KiB maximum RSS.  `/usr/bin/time -v` records elapsed `2:11:44`
and zero swaps.  The stop is operational telemetry only, never algebraic
evidence.

```text
ffa7f130a946c90aafc4d5d0ad3b1bd0b80e4f96bbbb2f4504017853e728ca48  METADATA.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  RUN_STARTED
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  compile_check.rc
f45693348d630c001583f7727761eab1da1f2b4b31daab49c98ad1b54a77fefc  compile_check.stderr
4ffe9091bda3f4661ef8e9cc570abf66d8d6dfa51eb9b43b234183717c630159  compile_check.stdout
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  raw_parse.rc
f44780263e6e4ca6b54e22aac9504d485f803149d29309337893849fe9a44722  raw_parse.stderr
4687c607b77b9c5be47bcc2d2d20332cc6f63d5f3663c864bb6f201007ccd477  raw_parse.stdout
13bd6e55cb8d16213090b238ce9c3313a48635b01c4a253c22928b9ea2d7d2a6  source_check.stdout
9d9b18720961e9b4689fd763b85e7b6f36160ccd3a8a1c9ddc5103bb0f66c396  triangular_reduce.rc
f829c16811b603c9ebe8c842254cafe9b567a7caa470dcc9b491e6ba4658bc28  triangular_reduce.stderr
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  triangular_reduce.stdout
```

## Box02 prefix prelaunch refusal

Namespace:

```text
/home/ubuntu/jobs/ggv_8_28_upper_endpoint_branch_p_20260827T222754Z_exact_prefix_quotient_box02_r1
```

The frozen Box02 runner refused at 2026-08-27T22:28:14Z before creating
`RUN_STARTED`, metadata, or any stage output.  GNU awk reserves `load` as a
builtin and rejected that spelling in the repeated CPU gate.  The runner then
failed closed; PID 381089 exited, the output directory has zero entries, and
an independent process search found no command from this namespace and no
`prefix_quotient_q.sing` process.  No compiler, replay, or CAS stage started.
This namespace is operational non-evidence and remains byte-untouched.  The
successor changes only the awk variable name to `load_value` and must use a
fresh timestamp.

```text
b78ce6090a201c030ec4383d2750ddc4e8eef139f342b46b52da3ab54893c56f  source/source.tar.gz
1ddb68ac2381e2ee1513115531b32df3c4c53ec200b0d598a8e4310586406dbd  source/cases/ggv_8_28_upper_endpoint_branch_p_20260827/SOURCE.sha256
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  output.outer.stdout
27dfc3d7e871209d4774035fc08cd06ff0d3f867d37e944c41ca86563c18963c  output.outer.stderr
```
