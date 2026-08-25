# Slope-uniform V2 control-only AWS smoke custody

Date: 2026-08-25  
Status: **PASS; SOURCE/PLACEMENT/SYNTAX/CONTROL EVIDENCE ONLY**

The exact source closure was staged on Box02 and the hardened wrapper ran in
`D1_SLOPE_CONTROL_ONLY=1` mode.  This mode reconstructed all eight reviewed
rows, checked every raw weighted-homogeneous monomial, independently rebuilt
the descended rows from the ordinary tails, verified the common-cubic
specialization, emitted and parsed every `Psi_l`, and exercised the complete
saturation/control code on the registered synthetic strict arc.

It did **not** saturate the D1 source ideal.  Its synthetic `H!=1` is the
positive control and is not a D1 survivor.

```text
host: ip-172-30-0-186 (Box02, Amazon EC2)
tag: max12_912_order3_d1_slope_uniform_20260825T220300Z_box02_smoke_v2
run: /home/ubuntu/jobs/max12_912_order3_d1_slope_uniform_20260825T220300Z_box02_smoke_v2
start_utc: 2026-08-25T22:00:57Z
end_utc: 2026-08-25T22:01:27Z
archive_sha256: e4a3cb6d566ce83098f1f18d133d071d4e8b24add3327db8ac1f173e60365a1d
source_closure_sha256: 39f43b1a078a1e07c18a3bd369a7d8f1b63a7d35a3e5015016d798b7743fd885
recorded_rc: 0
payload_file_sha256: 19412d5943adde3e530df510eee4f5b3d0f3d0d90c502323c877e70a0ce9c6cb
payload_canonical_sha256: 9eccf4be1eb8114f089b9be4af57ffd63649eeec94b57b52393ecae001f793e9
emitted_singular_sha256: c35362ef12637bc559a076c5c6605abb8b426d4d1b0ed6b930a8d40c6ae9d37c
singular_stdout_sha256: 802b434ca05296cd191a2a5aa5fd23d1f3e04bac6218b71296dfc1fe29f93b02
singular_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
payload_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
emit_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
singular_time_sha256: 0aa3ff3982b499ff2f81d6d36bf8a981a8d5296ebdd15eaa6ea6f022c32d783b
outputs_manifest_sha256: 1f22e8dbd4ab90c463e50b6994e322d9a4400ba86059329bd8c8a83db69a412e
```

Resource controls:

```text
payload: 14.90s, maxRSS 26,856 KiB
emission: 15.01s, maxRSS 25,812 KiB
Singular synthetic controls: 0.03s, maxRSS 12,552 KiB
cap: 600s / 64 GiB virtual memory
```

Required markers were present:

```text
PASS_SYNTHETIC_SATURATION_CONTROLS
CONTROL_ONLY=1
COEFFICIENT_RING=POLYNOMIAL_Q_K_MU_NU_NO_LOCALIZATION
PASS_PRODUCT_SEQUENTIAL_SATURATION_AGREEMENT
SLOPE_UNIFORM_H_IS_UNIT=0
PASS_D1_SLOPE_UNIFORM_SOURCE_AND_CONTROLS
```
