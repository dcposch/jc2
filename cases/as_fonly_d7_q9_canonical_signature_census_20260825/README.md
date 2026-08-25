# AS F-only D7: canonical Q9 signature census

This case exhausts the exact `3^13` Q9 survivor chart and fingerprints the
source-honest integer carry and deterministic affine/RREF presentation at the
canonical Q8 and Q7 particulars.  It is a finite-state **classifier gate**,
not a lift, no-lift theorem, recurrence theorem, or JC2 claim.

The compiler imports the pinned corrected source through
`as_fonly_d7_q8state_next_high_samples_20260825/compile_state.py`, extracts
only its source construction and Q7 row definition, and performs direct
substitution at every state.  Each state emits a fixed 128-byte digest record:

```text
full signature | combined integer carry | Q8 RREF | Q7 RREF
```

Shard intervals are contiguous and deterministic.  The aggregate concatenates
them in shard order, verifies exactly `3^13` records, merges the exact class
counts, and emits one canonical representative index per class.

All substantive execution is AWS-only.

