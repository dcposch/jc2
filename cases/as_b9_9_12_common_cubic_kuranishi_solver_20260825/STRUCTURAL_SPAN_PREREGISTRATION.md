# Exact structural-span discriminator

Before execution, the source-DAG span test is fixed as follows.

- Reconstruct the complete emitted 176-coordinate Kuranishi circuit from the
  pinned source closure.
- Treat byte-identical source-DAG expressions among the 299 pre-quotient rows
  as identical formal atoms, and distinct digests as formally independent.
- Compute the exact F3 row rank of the 176 coordinates as linear forms in
  those formal atoms, emit original coordinate rows forming a basis, and emit
  an exact relation vector for every coordinate.
- A low rank proves that vanishing of the selected basis coordinates implies
  vanishing of all 176 emitted coordinates.  A high rank is only a routing
  result.  The calculation does not solve the remaining basis-coordinate
  zero locus and does not infer identities between distinct DAG atoms.

Execution is AWS-only and fails closed on platform, job tag, and source hashes.
