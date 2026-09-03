# Minor-dichotomy source desk

This directory contains the bounded artifacts for
`OPEN[MINOR-DICHOTOMY]`.  The inputs are the frozen copies under
`/tmp/jc2-lane.7KOQB3/inputs`; nothing here edits those copies.

- `census_usgt1.py` verifies the nine receipt hashes, reruns
  `C_FULL_TREE_POLYNOMIAL_ODE`, groups by
  `(n,m,(M_2,...,M_s),V_s)`, and emits the complete `u_s>1` result as JSON.
- `client_arithmetic.py` checks the exact gcd towers, Definition 5.1 major
  radii, thresholds, and typed conditional detector profiles for `(99,66)`
  and `(108,72)`.
- `pages/` contains 200-dpi PNG renderings made with `pdftoppm`.  Printed
  page `p` is PDF page `p-139` (one-based).  The requested pages are
  `moh-pp196-199-{57..60}.png` and `moh-pp207-209-{68..70}.png`.
  Supporting pages 146--147, 150--152, 161, 168--171, 179--180, 190--195,
  202, and the continuation 210--211 are also present.

Important type boundary: Definition 5.1's `delta_i` are major-disc radii.
They are not the actual-root minor radius `delta*_{s-1}`.  The latter is
absent from a skeleton.  On p.209 Moh displays a radius-2 pi-root of `g`
while discussing roots inside `D_2*`; he does not identify its disc as the
combined-product minor disc.  Thus the probe is source data but `delta_2*`
remains open until the combined root contacts are supplied.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 box/minordich-20260903/client_arithmetic.py
PYTHONDONTWRITEBYTECODE=1 python3 box/minordich-20260903/census_usgt1.py \
  | jq '{counts,controls,skeleton_level_decision,focus}'
```

Measured on the lane host: the census command exited zero in 18.12 seconds
with maximum RSS 150396 KiB.  Both drivers use only the Python standard
library; the `jq` command only selects display fields.
