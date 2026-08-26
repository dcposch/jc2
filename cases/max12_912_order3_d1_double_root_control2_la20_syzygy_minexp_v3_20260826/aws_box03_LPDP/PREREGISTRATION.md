# Preregistration: minimum-individual-exponent witness race

- Fixed source/support/weight and nine Rees generators are identical to V2.
- Reconstruct and hash-match the exact repaired LPDP V2 source.
- Preserve the checked global saturation and `(C,s)` lift. A positive endpoint
  additionally requires exactly one used `C` generator, as observed but not
  inferred from both still-running V2 orders.
- Compute `std(I)` and search `m=0,...,N` in increasing order by literal exact
  reduction for the first `s^m*g in I`. Print `m`, lift `s^m*g` to the original
  nine generators, and replace the final exponent-`N` Rees identity by the
  corresponding exponent-`m` identity. Check it as a literal zero polynomial.
- Any parser diagnostic, failed source hash/anchor, missing `m`, lift failure,
  rc/timeout/memory failure, or nonempty stderr gives no verdict.
- This races certificate size and time only. It is neither evidence against
  V2 nor a cone claim. The dehomogenized witness must be separately enumerated
  and checked before any weight-neighborhood statement.
