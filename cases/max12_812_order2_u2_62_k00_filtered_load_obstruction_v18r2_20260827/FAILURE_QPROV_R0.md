# Provisional exact-Q V18R2 R0 implementation failure

The first registered lane
`max12_812_order2_u2_62_k00_filtered_load_v18r2_qprov_20260827T113627Z_box01`
verified its complete freeze and then failed before compiling or running any
Singular algebra.  The runner pre-created `compiled/`, while the frozen
extractor correctly required its output parent not to exist.  Python raised
`FileExistsError` before writing the extracted script.

The immutable failed packet is `aws_qprov_box01_failed_output_parent/`.
`run/extractor.stderr` has SHA-256
`8bf79840cbb408667834c760479374ffccff273bd4c2e32684778e810b45652d`.
This is a path-allocation implementation failure and carries no mathematical
result.

R1 changes only the additive runner's output path to the previously absent
subdirectory `compiled/extracted/`; the frozen extractor, emitter, exact rank
engine, validator, dependencies, target cutoffs, caps, and firewalls are
unchanged.
