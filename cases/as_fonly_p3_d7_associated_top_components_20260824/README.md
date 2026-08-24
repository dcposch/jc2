# F-only D7 associated top-component checkpoint

This case reconstructs the exact `F_3` first-digit schemes covering:

- homogeneous degree-seven divergence and carry degree 12;
- homogeneous degree-six divergence and carry degree 11;
- minimal and primary components, including the embedded Frobenius-supported
  layer-`7/6` component; and
- incidence of the frozen triangular point's zero top projection.

Replay:

```sh
python3 replay_rows_and_incidence.py
M=7 DO_PRIMARY=1 python3 generate_top_gate.py | Singular -q
TOP=7 LOW=6 DO_PRIMARY=1 python3 generate_layers76_gate.py | Singular -q
shasum -a 256 -c MANIFEST.sha256
```

Scope stops before carry degrees 10 through 7, the Cartier row, or any full
depth-seven conclusion.

