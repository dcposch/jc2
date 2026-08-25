# Box02 custody: pinned base-513 Q4 obstruction

Canonical exact run:

- host: Box02, `ip-10-0-2-143`;
- SMT/compiler job: `/home/ubuntu/jobs/as_global_q4_h5_20260825T103745Z_v3`;
- affine/literal replay job: `/home/ubuntu/jobs/as_q4_affine_20260825T1058Z_v5`;
- result archive SHA-256:
  `3f952888d46e88b26e857220601fa2b3b7cbe26fad172bf3f5345ec61325e389`.

The archive contains the compiler metadata, the SMT hash (the 13 MB formula
itself is hash-pinned but omitted), both solver endpoints, and the complete
affine/literal replay.  Boolector and Z3 both returned UNSAT for the same
pinned formula.  The independently checkable mathematical payload is the
68-by-12 affine matrix and the one-row left-cokernel certificate emitted by
`analyze_pinned_q4_affine.py`.

Two prior deployments are negative controls only:

- `as_global_q4_h5_20260825T103522Z` failed at Python syntax parsing;
- `as_global_q4_h5_20260825T103634Z_v2` failed with `NameError`.

They are not evidence.  The first two affine-replay deployments likewise
failed closed on an incomplete source closure and on use of the superseded
Q5 V1 replay.  The consumed run is V5, which pins the Q5 V2 erratum replay.

