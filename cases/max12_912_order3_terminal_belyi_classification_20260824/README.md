# Selected-Q8 terminal Belyi classification

This case classifies rational solutions of the selected-Q8 descended terminal
identity with polynomial `h`.  At the noncube, `3|deg(h)` scope, the only
survivors are balanced three-value Belyi passports.  This is a necessary
classification, not a coefficient-fibre realization or trajectory
exclusion.

```sh
python3 cases/max12_912_order3_terminal_belyi_classification_20260824/replay.py \
  | diff -u cases/max12_912_order3_terminal_belyi_classification_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_terminal_belyi_classification_20260824/MANIFEST.sha256
```
