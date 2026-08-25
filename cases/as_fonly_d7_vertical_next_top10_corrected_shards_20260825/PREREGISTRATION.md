# Source-corrected degree-ten discriminator

Consume the exact corrected-Q11 predecessor and reproduce the controls
`1085103`, `629115`, and `260847`.  Attach the full degree-ten row

```text
Q10={C7,D5}+{C6,D6}+{C5,D7}
    +({UF,D6}+{C6,VF})/3+{UF,VF}/9 mod 3.
```

Enumerate every visible predecessor state in 27 contiguous structural-base
shards.  Output exact counts, per-base histograms, leaf hashes, and an
ordered Merkle certificate.  Verify source-honestly that all six current
degree-six Frobenius spectators remain absent and contribute a fibre of
either zero or 729.

Zero corrected survivors is a finite-branch obstruction at degree ten;
nonzero survivors proceed to the lower quotient/current-next cross rows.
Any control mismatch, failed assertion/shard, timeout, OOM, or aggregate
failure is no verdict.  No lower row, recurrence, all-depth,
characteristic-zero, no-lift, counterexample, or JC2 inference is licensed.

