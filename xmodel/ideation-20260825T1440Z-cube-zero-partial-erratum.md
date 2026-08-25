# Custody-preserving mathematical erratum to the blind cube 1440Z note

Date: 2026-08-25  
Parent note (immutable): `xmodel/ideation-20260825T1440Z-cube.md`, SHA256
`15a057a76a9776f6b05f58286ecb1f58d2bb47c0fc842018602aa48a06788959`.

The parent note misread the producer classification `zero-partial` in its AS
discussion.  This erratum does not change the sealed blind bytes or any Q8,
TD6, allocation, or global-wall statement.

## Exact correction

`zero-partial` means that on every one of the 11,881 nonempty projected Q9
fibres, `omega` is a **nonzero/surjective affine functional** and its zero
hyperplane is nonempty (indeed one third of completions).  The producer also
contains points with `omega=1` and `omega=2`.  It does **not** mean that
`omega` vanishes in the source coordinate ring, radical, or reduced quotient.

Consequently the following parent-note proposals are withdrawn:

- testing whether `omega` belongs to the source ideal or its radical;
- interpreting uniform `zero-partial` as evidence that `omega` is a syzygy,
  nilpotent class, or source-zero primary obstruction; and
- “retiring omega” by ideal membership.

The correct inference is narrower: scalar-only sampling cannot kill this
stage because every current fibre has a nonempty `omega=0` hyperplane.  The
next exact object is the intersection of those hyperplanes with the full
Q8--Q3 restoration/next-carry correspondence.  One should first certify that
the fibrewise kernels form the claimed constructible subbundle/torsor, retain
transition functions and nilpotent strata, and then compute the next
Bockstein/Kuranishi map on that kernel.  Cross terms with varying lower-level
kernel coordinates must be included.

This correction lowers the novelty claim of the parent Card B from a new
“primary-syzygy test” to a redesign of the already-known downstream
restoration gate.  It does not turn the 11,881 projected survivors into maps,
all-depth lifts, or counterexamples.
