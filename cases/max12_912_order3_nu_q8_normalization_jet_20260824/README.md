# max12 `(9,12)` order-three Q8 normalization jet

This case computes the lowest nonzero formal jet of the corrected Q8
non-parity branch over `Q[v]/(Q8)`, pulls back `r8`, and types the branch in
the reviewed root-free critical-value norm.  It reconstructs all `10+13`
original Taylor coefficients at the true center `r=A/9`; it does not replace
them by evaluations at the spectral center `z=0`.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_normalization_jet_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.json -
```

The exact local discriminator is `E=e1*t+O(t^3)` with `e1` a unit: the node
is in equal-value leaf 3, while the punctured branch enters generic leaf 4.
This remains a local formal jet, not a global normalization or a rational
Keller trajectory.
