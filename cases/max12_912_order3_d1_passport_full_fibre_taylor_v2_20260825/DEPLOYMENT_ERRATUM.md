# V1 source-closure deployment erratum

The immutable V1 source/preregistration package is preserved at
`cases/max12_912_order3_d1_passport_full_fibre_taylor_20260825/`.

Its first AWS source smoke failed closed before row construction because
`SOURCE_CLOSURE.sha256` omitted two files read by the pinned parent's
`pin_inputs()`:

```text
cases/max12_partial_y_preflight_20260824/FREEZE.sha256
cases/max12_high_row_probe_20260824/FREEZE.sha256
```

This is a deployment/source-closure defect, not mathematical evidence.  No
row equality, component computation, Taylor computation, existence claim, or
exclusion claim was produced by that run.  V1 bytes are not mutated.  V2
lists both missing files explicitly, invokes the parent transitive pin check,
and requires the staged closure verifier to pass before source compilation.

Exact negative deployment custody:

```text
host: ip-172-30-0-249 / Box03 / 98.80.65.144
run_dir: /home/ubuntu/jobs/max12_912_order3_d1_rows_20260825T202325Z_box03
lane: max12_912_order3_d1_rows_20260825T202325Z_box03_compile
start=end: 2026-08-25T20:25:58Z
rc: 1
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: 5e22f45702423cec10166eb63a2759807cf343a2f7b7135253fc95b0a84d011c
error: FileNotFound at parent.pin_inputs for the preflight FREEZE file
```

After staging both omitted files, the V1 source compiler was rerun in the
same custody directory under lane suffix `_compile_v2`.  It returned rc 0,
stdout SHA-256
`3675f79c6458feb91d15d41ee43ec115897962dd4f687942fb26520717c20654`,
stderr SHA-256
`e5a2a9828d3c9391959403725ae7e13d496fe13202354eb68eb61b1b37c0418a`,
and payload SHA-256
`6ad2388a04eb4106927bde180f7d4dffd2cb1015ea787cdf9b6376508cbdd5b3`.
That is a source-only runtime control, not a component/Taylor theorem.
