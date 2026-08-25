# `(9,12)` order-three `nu!=0` parity genus-five exclusion

This case reconstructs the full parity rationalization from the pinned exact
Faber compiler and verifies the cyclic genus-five curve and the `p=0`
boundary.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_genus5_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_genus5_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_genus5_20260824/replay.json -
```

No modular projection or opaque Groebner output is an input.
