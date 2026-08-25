# max12 (9,12) order-three parity-normal Q12 checkpoint

This case replays the exact first-order normal-Jacobian calculation along the
reviewed `nu != 0`, `k=mu=0` parity fibre.  It pins both exact dependencies by
SHA-256 and uses only the Python standard library.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_normal_q12_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.json -
```

The result is deliberately not a Q12 exclusion or a formal-trajectory
classification.  It isolates the one residual normal-rank boundary on the
generic parity chart.
