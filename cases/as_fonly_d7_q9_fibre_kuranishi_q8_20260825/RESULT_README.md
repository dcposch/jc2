# Frozen Q9-fibre Kuranishi result

Two Box02 executions of the identical source-frozen compiler produced the
same standard output and byte-identical JSON presentation.  The original
tag is `as_q9_fibre_kuranishi_q8_20260825T021044Z`; the coordinator's
independent relaunch is `as_q9_fibre_kuranishi_q8_root_20260825T0220Z`.

On the 19-dimensional Q9 affine chart over the first predecessor, the
Lyapunov--Schmidt matrix `B(t)` is identically zero.  The advertised
degree-at-most-two obstruction `kappa(t)` has no square or cross terms.  Its
only nonzero coefficients are

```text
kappa_1 = t_10,   kappa_2 = t_13,   kappa_4 = t_11,
kappa_5 = t_15,   kappa_7 = t_12,   kappa_8 = 2+t_17.
```

Thus the unreduced integral affine-lift presentation has the exact affine
zero locus

```text
t_10=t_11=t_12=t_13=t_15=0,  t_17=1,
```

with the other thirteen parameters free.  The compiler searched only 36
points, but found and directly substituted the first survivor `t=e_17`.
Its canonical Q9 vector has entries 23 and 30 equal to one and all other
entries zero; all 32 next-layer entries may be taken zero for this witness.

Two limitations are load-bearing.  First, the exact whole zero-locus
description is presently licensed in the unreduced affine-lift chart.
Canonical digit-lift compatibility was checked on all 36 searched points,
not on all `3^19` points.  Second, the six derivative-zero degree-six
`C6,D6` Frobenius spectators from Q9 are pinned to zero in this compiler.
The displayed canonical survivor is valid, but this is not a classification
of the full `3^25` fibre including those spectators.
