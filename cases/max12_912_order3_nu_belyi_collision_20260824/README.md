# `(9,12)` order-three `nu!=0` full B/W absorption boundary

This portable case checks the exact degree, discriminant, passport, and
scaling ledgers used to exclude the boundary on which all ramification of the
quadratic spectral Wronskian `B` lies over `beta=1`.

Run from the repository root:

```sh
shasum -a 256 -c cases/max12_912_order3_nu_belyi_collision_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_belyi_collision_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_belyi_collision_20260824/replay.json -
```

The replay is an integer/regression ledger. Hurwitz finiteness and
isotrivial descent are proved in the report, not delegated to software.
