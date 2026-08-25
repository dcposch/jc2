# Exact characteristic-zero double-B saturation basis

This package preserves the corrected `msolve 0.10.1` characteristic-zero
run for the normalized `(9,12)` order-three double-`B` leaf, saturated at
`p`.  The input begins with the required nine-variable declaration; the
earlier malformed one-variable trials are not part of this package.

`result.out.gz` is the byte-for-byte gzip of the 23,172,493-byte output.
Run

```sh
python3 verify_result.py
```

to check all frozen hashes, parse the complete 1,246-element basis, recompute
every leading monomial in graded reverse lexicographic order, and verify that
the initial ideal contains a pure power of every declared variable.  The
script validates the output as recorded evidence; the claim that the list is
indeed the reduced Groebner basis of the input still rests on the exact
characteristic-zero `msolve` computation and is being checked independently.

