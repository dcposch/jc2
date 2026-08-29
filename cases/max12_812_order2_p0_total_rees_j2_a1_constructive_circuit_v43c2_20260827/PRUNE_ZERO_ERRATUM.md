# V43C2 exact-zero pruning erratum

Date: 2026-08-27

This additive erratum supersedes only the claim in
`PRUNE_ZERO_ADDENDUM.md` that the intermediate node `Z=170` is zero.  That
note and the separately frozen v4 source bytes remain immutable historical
artifacts.

The frozen v4 AWS producer expanded node 170 exactly over `Q` with its
memory-bounded sparse evaluator.  It found:

```text
expanded_term_count = 24429
expanded_sha256 = 3c4dcc5f62f3c501f08581369525ca088b15a4ec3d3fa6f56251da288e229a72
peak_sparse_terms = 24429
visited_nodes = 61
evaluated_node_calls = 92
```

Therefore node 170 is nonzero and may not be pruned after the `a1^18`
checkpoint.  V4 correctly failed closed before performing any branch
combination.

The actual final crossed coefficient has root 642 and factorization

```text
root642 = a1^2 * node170 * a1 * node619.
```

Since `Q[X19_rho0]` is a domain and node170 is nonzero, any exact zero of
root642 must come from node619.  The v5 successor removes the invalid early
prune, retains the exact low-memory evaluator, and again invokes
`PruneZeroTerms` only at the final crossed-label boundary.  It must accept
only if the complete root642 expansion is literally zero (with serialized
telemetry independently replayed); otherwise it fails closed.  The strict
`CombineBranches` guard is unchanged.

