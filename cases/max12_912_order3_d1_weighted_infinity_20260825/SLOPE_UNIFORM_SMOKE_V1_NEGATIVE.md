# Slope-uniform V1 smoke: Singular API negative control

Date: 2026-08-25  
Status: **QUARANTINED; NO MATHEMATICAL EVIDENCE**

The closure-complete control-only smoke reconstructed and parsed the source
and reached all final markers, but Singular 4.3.2 emitted two diagnostics:
this `sat` implementation returns a one-entry list, so reads of `KS[2]` and
`HS[2]` were out of range.  The old wrapper admitted the zero process exit.
Those source bytes and that endpoint are rejected.  The successor removes
the invalid exponent reads and fails closed on any nonempty Singular stderr.

```text
host: ip-172-30-0-186 (Box02, Amazon EC2)
tag: max12_912_order3_d1_slope_uniform_20260825T215900Z_box02_smoke
run: /home/ubuntu/jobs/max12_912_order3_d1_slope_uniform_20260825T215900Z_box02_smoke
archive_sha256: 8c319c0082009b99fdb651bfb7630ad89fd6c841a3e2dd7fdb84b575620759de
recorded_rc: 0 (invalid because stderr was nonempty)
payload_sha256: 8ec0d48187383e69e0ba6a03bbe97c57901b50aa4f3a25fca2fc9de5165eb80c
emitted_singular_sha256: 12ecbb456c4b364cbd948b009121854144c6491027a1a210b1c9989966e6b482
singular_stdout_sha256: a75c557b6092c5b99bdf7fe1450ab5c40b21659395f2e70b6a5414e6ae8ee619
singular_stderr_sha256: 2fcc034380b338befdd7f0a98768de3500c50e3c9a621bd67513c5e1cae7bdf2
singular_time_sha256: 4b309963d1803dcfd43d0e4b672f9790704256cd6d9e757107e60ef38561bf6f
outputs_manifest_sha256: 5f9bd2a5345eff5e5212df698d01cff28550989061757b441c40e98855d622ff
```

The synthetic nonunit `H` in this run was only the registered control ideal,
not the D1 source ideal.  It is not a survivor result.
