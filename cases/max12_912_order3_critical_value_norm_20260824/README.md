# Root-free critical-value norm

This case constructs the exact unordered two-critical-value stratifier on the
normalized `(9,12)` order-three `k=mu=0, nu=1` coefficient fibre.  It works
in the quadratic algebra defined by the reviewed Wronskian `B`, so neither
root is selected and the expanded roughly 200,000-term resultant is avoided.

Replay:

```sh
python3 cases/max12_912_order3_critical_value_norm_20260824/replay.py \
  | diff -u cases/max12_912_order3_critical_value_norm_20260824/replay.json -
```

The output is a stratification identity, not an exclusion.
