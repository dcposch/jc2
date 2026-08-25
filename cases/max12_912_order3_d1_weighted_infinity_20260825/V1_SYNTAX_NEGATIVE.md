# V1 exceptional-compiler AWS syntax negative

The immutable V1 source freeze passed its full source-closure check on Box03,
then failed closed before any algebra because `compile_exceptional.py` opened
`lines.extend([` and closed only the list (`]`) rather than the call (`])`).

```text
host: ip-172-30-0-249 (Box03)
archive_sha256: c709292f6dc4fc3d9c51827677a3b7d9b22ceb91fb615367bd7eba81460e08a2
run_dir: /home/ubuntu/jobs/max12_912_order3_d1_infty_exceptional_20260825T212744Z_box03_smoke
rc: 1
elapsed: 0.09s
max_rss: 31,456 KiB
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: 00185ac59edfdfc38f771833d7f70b6c9ceb8a0013bfcfbbfe6e34e710b7aa3e
time_sha256: dda6bae284fd358efb1bc0d12a6fa52a75f90515e2eb50778b5e09756aa19f00
closure_stdout_sha256: af94c15adc7de733c9cce0247f4972f6fac00a69908e9d601ecb0a6bfd557b39
closure_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

No Singular process started and no exceptional ideal, component, rank,
containment, deformation, Taylor, or D1 evidence was produced.  V2 preserves
and hashes the V1 bytes, applies exactly one in-memory syntax patch, and must
run under a fresh tag.

