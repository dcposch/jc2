# Post-run custody supplement

The six registered lanes completed on 2026-08-25 at the following immutable
AWS endpoints:

- r6d (`ip-172-30-0-45`):
  `/home/ubuntu/jobs/max12_912_order1_cubic_bands_v1_r6d_20260825T1745Z`;
- Box02 (`ip-172-30-0-186`):
  `/home/ubuntu/jobs/max12_912_order1_cubic_bands_v1_box02_20260825T1745Z`.

The harvested bytes are under `evidence/{r6d,box02}/{triple,double,squarefree}`.
For each stratum the two hosts have byte-identical `compiler.stdout`,
`singular.stdout`, `result.json`, and `obstruction.sing`.  The squarefree
hosts also have byte-identical `sat_interface.stdout` and
`sat_interface_result.json`.  They are two executions of one implementation,
not independent mathematical implementations.

## Stale self-hash quarantine

Each remote `OUTPUT.sha256` was generated inside `run_aws.sh` immediately
before the final shell line wrote `PASS <stratum>` to `launcher.stdout`.
Consequently its entry for `launcher.stdout` records the empty-file hash even
though the final harvested file contains the PASS line.  No algebraic output
is affected.  The stale `OUTPUT.sha256` files are preserved unchanged as
negative custody controls and MUST NOT be used as final manifests.

`MANIFEST.postrun.sha256` was generated only after harvest and is the active
byte manifest.  `FREEZE.sha256` pins that manifest, this supplement, the
producer report, and the hostile-review prompt.

