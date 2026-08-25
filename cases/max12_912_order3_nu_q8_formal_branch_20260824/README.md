# max12 `(9,12)` order-three Q8 formal branch

This case freshly verifies the equivariant formal-node hypotheses at the
corrected `Q8` rank boundary.  It imports no conclusion or code from the
quarantined `Q12` formal-branch case.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q8_formal_branch_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_formal_branch_20260824/replay.json -
```

The result is formal seven-row coefficient-fibre geometry only.  It does not
impose the terminal row or certify a Keller trajectory.
