# V3 to v4 supersession record

V1 remains frozen at
`cases/d43_exact_sparse_rows_20260828/SOURCE.sha256`, digest
`9b851ede56986fe3154cf962f336fda6185fb7a4a00d07888c93e9b78a06848d`.
V2 remains frozen at
`cases/d43_exact_sparse_rows_v2_20260828/SOURCE_V2.sha256`, digest
`83635fe45e6f3a9e19d3c93ef963de769f2721653a7bb5333002dd100172fa73`.
V3 remains frozen at
`cases/d43_exact_sparse_rows_v3_20260828/SOURCE_V3.sha256`, digest
`5423bd88328c338c54072b056d3f64251dc57de6f5112646f9d157f991ab5271`.
No prior packet was modified or resealed by v4, and none may be launched.

The Opus 5 v3 hostile review
(`xmodel/d43-exact-sparse-rows-v3-hostile-review-opus5-20260829.md`,
SHA-256 `6e01e5d7e7852d094559ab57cd7a256c41390fca99e38a6c55fbea8f12209bd9`)
confirmed the v3 mathematical source fidelity within its boundary and
returned REPAIR_REQUIRED on custody: the terminal copied its
payload-binding candidate fields (blocking), directory members passed the
archive census, the pgid/cgroup orphan gates were vacuous or copied in one
mode each, and the launcher post-mortem census gated nothing.  It also
disclosed the v2->v3 mathematical byte-diff as UNADJUDICATED.

V4 preserves the v3 mathematics **byte-for-byte at the function level**
(machine-checked by `math_function_diff_v4.py`; the only producer diffs
are the module docstring, the `.v3`->`.v4` schema strings, and the
optimized-Python refusal message) and repairs all five findings: a
value-binding terminal with per-field provenance, sidecar archive
resolution and rehash, full-member-set archive census refusing directory
members, setsid session leadership plus real pgid censuses in both
containment modes with a `NOT_APPLICABLE` (never copied) fallback cgroup
gate, and an authority-bearing launcher post-mortem that voids a positive
terminal via an immutable fault object.  The unadjudicated v2->v3 diff is
closed by the pinned diff tool and its sealed report
`V2_V4_MATH_FUNCTION_DIFF.md`.

The v3 files `run_conditional_pipeline_aws_v3.sh`, `aws_launch_v3.sh`,
`aws_preflight_v3.py`, `job_contract_v3.py`, and `selected_rows_v3.py` are
superseded for launch purposes.  No claim is promoted: no D43 v4 jet, row,
inventory, point, or verdict exists.
