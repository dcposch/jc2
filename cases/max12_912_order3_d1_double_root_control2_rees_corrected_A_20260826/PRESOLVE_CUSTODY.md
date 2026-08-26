# Pre-solve custody

Both independent AWS compilers completed rc zero with empty stderr and the
unique compiler PASS.  After replacing only the embedded AWS tag, both hosts
emitted identical sources for each order:

```text
21edd6daf0a2ea7b290ad440c3ebbca076ff197f001559ecb0dd2693cd41f359  corrected_A_lpdp.sing.normalized
83ddc95f52fd34ed5c6b5498b0acdfd6dc4b026069937c3dd122943197ea72b4  corrected_A_dp.sing.normalized
```

Frozen solve inputs:

```text
0e92f2d1c418d1710ef20b5dd288912e8b820c8d8d66dd6faa678ebf99c42e02  Box03 corrected_A_lpdp.sing
a15555873395ed2cfedfedef35ee954dcbe4ed390c29791d5c9bbfff72b92131  r6d corrected_A_dp.sing
```

Each remote `solve_source.sha256` verified before GO_SOLVE.
