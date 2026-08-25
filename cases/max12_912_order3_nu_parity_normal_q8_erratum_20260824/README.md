# max12 `(9,12)` order-three parity-normal Q8 erratum

This case replaces the refuted off-fibre `Q12` determinant with the exact
`Q8` determinant on the reviewed `r2=r4=0` parity chart.  It contains an
explicit dual control: the quarantined wrong substitution still reproduces
`Q12`, while the correct substitution kills `r2,r4`, fails `Q12`, and yields
`Q8`.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.json -
```

The result is first-order only.  No formal branch or trajectory at `Q8=0`
is registered here.
