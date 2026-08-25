# TD6 V55 previous/pole source-row union — AWS custody report

## Verdict

`V55 PREVIOUS/POLE ORIGINAL-ROW AUDIT: PASS`.

Nine disjoint AWS shards replayed all 54 arbitrary-degree previous/pole
original rows for the fixed source-typed `(C,V,U), q_beta` family.  The exact
union checker proved the modulo-nine partition disjoint and exhaustive and
verified that every shard used the same source archive and ended at its
mode-specific PASS marker.

This closes the earlier **previous-row source-completeness** debt.  It does
not yet close the current-row debt or replay the combined N13/P12 source
identity.

## Exact evidence

- Source archive SHA-256:
  `afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a`.
- Union checker SHA-256:
  `4c4ef3f0178f0e9af16b293aab2435581de32aabbdf72dfca3cfe3cae9760c9b`.
- Union stdout SHA-256:
  `0a4ff0ecf052b71f914031e25a2705988312770293183c73745ce47c6a9e9855`.
- Exact stdout-union digest:
  `e0c73f462671fd57e38c10a2c4b13c5612e96d0367721f1dee3ebe74ebfe2ba4`.
- Nine shard return codes: all zero.
- Exact row coverage: indices `0..53`, each exactly once.
- Each shard: six original rows, direct replay true, genuine quadratic
  positive control true, same transport/staged pivot digests.

The complete source archive and all per-shard custody bytes are frozen in
`cases/td6_c1_c2_c3_q2_previous_source_rows_v55_aws_20260825`.

## Interpretation and next gate

V55 independently validates that no arbitrary-degree previous/pole source row
was lost by the staged linear representation.  The next exact gate is the
conjunction of:

1. V53 dependency-closed full N13/P12 source identity;
2. V56 disjoint/exhaustive replay of all 40 arbitrary-degree current rows;
3. exact denominator/support interpretation using constructible rank strata,
   never one-shot cokernel membership or multivariate gcd.

Until those gates pass, `full_source_identity_replayed=false` remains the
controlling scope line.  This report licenses no family, TD6, SP-2, or JC2
claim.
