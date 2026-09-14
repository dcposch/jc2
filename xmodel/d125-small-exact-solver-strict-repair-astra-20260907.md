# D125 strict-stream parser — two-check versioned repair

Status: **PRODUCER-CHECKED NARROW REPAIR / PENDING DIFFERENT-MODEL DELTA GATE.** Author `/root/model_productivity`, 2026-09-07. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

The terminal Sol gate `xmodel/d125-small-exact-solver-code-gate-sol56-20260907.md` was read whole and its SHA verified as `84770876aaa2c3ac57e241f4ca4aa4957a46d4d5a16da32e47e9eff27d763a84`. It refuted two strict-stream checks, not a demonstrated mathematical unit/properness certificate. The arithmetic, certificate criteria, source/serializer and static caller were separately confirmed at the gate's stated scope.

## Exact repair and preservation

New version is in `box/d125-small-exact-solver-strict-repair-20260907/`. Relative to the old `exact.py`, **only two executable lines changed**:

```diff
-    need(not stderr.strip(), 'nonempty stderr')
+    need(stderr == b'', 'nonempty stderr')
-    need(0 <= engine_size <= len(engine), 'engine size outside indexed columns')
+    need(engine_size == sum(bool(row) for row in engine), 'engine size/nonzero count mismatch')
```

The complete unified diff is `exact-two-checks.patch`, SHA `1cccb1738f7d27cf20ea181099c4105baa434189786703480e538164edf39b3e`. No arithmetic, source parsing, serialization, mapping, certificate, authority, limit or command logic changed.

- Old `exact.py` remains unchanged: `ca7630e39cb8c5b4aec671b2a83132502abd716c6826c30a4bbc03014ffdb6b3`.
- New `exact.py`: `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`.
- Copied `driver.py` is byte-identical: `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`.
- Copied `test_exact.py` is byte-identical: `e1f0d6d0c0a930d8f1a2dc17709c98fd1bb37669564c1d09b2be6251a87dd588`.
- Copied `run_tests.py` is byte-identical: `90f3ae5e24c51a893af232b911d9baafb9b8f60ece1a5349807fa3332b94cd04`.

## Actual changed-object controls

The pinned actual engineering stdout is read only as295-byte data, SHA `fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922`. Its observed `I_SIZE 3`, six engine columns and six cofactor rows license the exact nonzero-entry count on this pinned Singular behavior; all zero/duplicate slots remain independently indexed.

Normal and `-O` delta controls both established:

- Original actual stdout plus `b" \n\t"` stderr: old parser **accepts**, repaired parser **rejects**.
- Actual stdout with `I_SIZE 3` replaced by `I_SIZE 0`: old **accepts**, repaired **rejects**.
- A two-nonzero-row `(x,1-x)` stream with `I_SIZE 2` replaced by0: old **accepts**, repaired **rejects**.
- The unchanged actual six-column zero/duplicate control remains **accepted** by both versions, with exact six-row cofactor identity and map `[0,1,0,1,4,0]`.

All17 unchanged producer methods also passed normally and under `-O`. The four new delta methods passed in both modes. Entire bounded local batch:1.024083 wall seconds,1.026256 child CPU seconds, peak29,648KiB RSS, within30 wall/25 inherited CPU/512MiB limits. No enforcement relies on removable language assertions.

New test/evidence pins:

- `delta_tests.py`: `65fc880d4343c318d75399bc6cc29b404dc3267f49df195cad0338947f550fb2`.
- `run_delta.py`: `e04c0e4e1760cd0be0016b8387dae795b463a09642e5aa76a2a4908bb15d1b75`.
- `delta-results.json`: `0237429bacc82126eb02311e2d3586b9566caa5489827d37283273b499905aed`.
- `producer-tests.json`: `e45a7806a1168f2e31bd4169e600bdae1b4a548fcce2c2eca8ad3f270920902a`.

Read-only replay commands from the new directory: `python3 -B -m unittest -v test_exact`, the same with `-O`, and `python3 -B delta_tests.py` / `python3 -B -O delta_tests.py`. The batch runner's named outputs are exclusive; do not rerun it into occupied evidence paths.

No AWS/SSH/CAS, full-source parsing, remote deployment, source-stream change or solver action occurred. All older code/evidence and the installed worker version remain untouched. The repair needs the scoped different-model gate and an explicit root deployment/solver GREEN; this report supplies neither. All local test children and artifact writers are terminal after sealing. **STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4153`.
- Body SHA-256:
  `77aef6610e25f5f7b5c9210a1c981e62d588ed6a6a3729fb4fb1c98a31e09abd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
