# V84S reverse-presentation failure classification

Date: 2026-08-26 07:11Z

V84S is a **harness-negative with no mathematical verdict**.  The registered
Box03 lane `td6_v84r2_k2_spencer_reverse_box03_20260826T062457Z` completed
with `rc=1`.  It passed source closure, rank-3470 transport, symbolic-center
typing, q-boundary singleton and omission controls, then failed before FIRST
or previous/pole output at the inherited triangular-parameterization
assertion

```text
assert other > variable and forms[other] is not None
```

in parent `parameterize` line 677.

Cause: the wrapper reversed source-row processing but still selected the
minimum base pivot and invoked the parent's descending triangular
parameterization.  Under reversed row order a pivot row can retain a smaller
unresolved variable, so that presentation no longer satisfies the parent's
triangular contract.  This is not an incompatibility or nonzero obstruction.

Custody SHAs: stdout
`3adf128bd72087127a1e4d841541761ab1c84bd2998ac8aa47b42dc2955c19b5`,
stderr
`31d6c61d27899a2182ca08fd7f56e2d5c6f8cef2f596e9df962e196d6e64c806`,
and source archive
`d6ed170d1699a3c7984f4fafa798a9c5d397f375a8d0ab5adfa4c3e2df71dcf5`.

The corrected successor must change the pivot and parameterization orders as
a matched pair, retain exact original-source replay, and run on AWS.  V84R2's
reviewed positive theorem is independent and unaffected.
