# Corrected-Q8 unordered-Hurwitz support gate

This case reconstructs `tau` and `Delta` on the selected corrected-Q8 branch
through `w^47`, verifies their even descent from `t^2=w`, and excludes all
plane relations in 53 stated rectangles for each of four Hurwitz/tail pairs.
It also records the triangular Taylor-coordinate freeness lemma.

```sh
python3 cases/max12_912_order3_nu_q8_hurwitz_support_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_hurwitz_support_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_hurwitz_support_20260824/MANIFEST.sha256
```

No relation outside the finite boxes, global normalization, projective
boundary, genus, or trajectory conclusion is claimed.
