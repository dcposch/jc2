# max12 `(9,12)` order-three `Q12` formal branch

This producer case reconstructs all eight coefficient-tail rows and verifies
the exact rank and transversality hypotheses for the equivariant formal
implicit-function argument at `Q12=0`.

```sh
shasum -a 256 -c cases/max12_912_order3_nu_q12_formal_branch_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q12_formal_branch_20260824/replay.json -
```

The resulting second component is only a formal component of the seven-row
constant-invariant coefficient fibre.  The case does not impose the terminal
differential row or certify any polynomial/rational Keller trajectory.
