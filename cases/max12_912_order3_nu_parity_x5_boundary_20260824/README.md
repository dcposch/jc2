# `(9,12)` order-three `nu!=0` parity `x5=0` boundary

The replay imports the pinned approximate-cubic compiler, applies the exact
odd/even specialization, verifies the `x5=0` triangular solve and terminal
contradiction, and certifies that `A=x3-2*p*x5` cannot vanish when `nu!=0`.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_x5_boundary_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_x5_boundary_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_x5_boundary_20260824/replay.json -
```
