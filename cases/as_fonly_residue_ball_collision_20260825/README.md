# AS residue-ball collision controls

This portable case is the finite-ring regression payload for
`xmodel/as-fonly-residue-ball-collision-compactness-theorem-20260825.md`.

Run on AWS:

```sh
/usr/bin/time -v python3 replay_controls.py \
  > replay.stdout 2> replay.stderr
```

The replay expands the complete determinant of the frozen cap-seven
triangular map, performs the digit-by-digit Hensel lift in all three source
residue balls at moduli `9` and `27`, checks the image equations and unit
separation equation, and runs a singular-Jacobian negative control.

The case is a positive control.  It neither constructs nor excludes an
all-depth fixed-support lift.
