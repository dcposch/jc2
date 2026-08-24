# `(9,12)` order-three DZ20 stabilizer/valuation replay

This pure-stdlib replay checks every integer congruence and local/infinity
valuation balance used by the producer report
`xmodel/max12-912-order3-dz20-stabilizer-valuation-20260824.md`.

Run from the repository root:

```sh
python3 cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.py
```

The case is scoped to the coprime spectral fibre with order-three Kummer class
and `k=mu=nu=0`. It does not cover a common-factor/noncoprime spectral stratum,
nonzero invariant loads, the order-one polynomial core, any other
maximum-twelve cell, or JC2.
