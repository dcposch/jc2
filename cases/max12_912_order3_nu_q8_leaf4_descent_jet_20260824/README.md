# max12 `(9,12)` Q8 leaf-4 local descent jet

This case reconstructs the corrected second formal branch and proves that
the root-free Hurwitz discriminant, critical-value sum, invariant tail
quotient, and `S=r8^9` are etale local quotient coordinates at every Q8
contact.  It also derives `h^3*(S')^9=j^9*S^8` from the terminal row.

The replay includes the mandatory negative control showing that the parity
formula `r6=p^9*R6(v)` fails at order `t^2` off parity.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.json -
```

This is formal-local descent only.  The global quotient relation, Taylor
center, projective boundary, and punctured trajectories remain open.
