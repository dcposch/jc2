# Byte-readable source snapshot for the TD6 `B3=0` cover

This directory is a review-custody supplement for the immutable AWS
archives in
`../td6_c1_c2_c3_b3_raw_divisor_aws_20260825/`.  It exposes the exact V22,
V26, and V27 payload bytes without requiring a reviewer to invoke a shell or
extract a tarball:

- `v22/`: the exact `t^2-4t+2=0` raw-curve producer;
- `v26/`: the exact `t=1/2` raw-curve producer;
- `v27/`: the strengthened generic birational producer with per-slot
  denominator clearing.

Each subtree is a direct extraction of its correspondingly named archive,
with the archive's top directory stripped.  Each embedded `SOURCE.sha256`
was checked after extraction and every entry returned `OK`.  No source file
was edited, and no `__pycache__`, `.pyc`, AppleDouble, or `.DS_Store` file is
present.

This supplement is source custody only.  The theorem-producing AWS stdout,
run metadata, resource reports, archives, dependencies, and scope statement
remain in the primary evidence package.  Heavy replay remains AWS-only.
