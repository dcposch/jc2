# Registration: `r=1` / symbolic-`d=1` V6 ideal-chart root check

Date: 2026-08-26

V1--V5 all passed the complete mathematical source, row, scaling, and
recurrence sentinels but failed closed in the same nested `subst` root-chart
block.  V6 pins V5 and replaces only that diagnostic-prone implementation by
four explicit linear root-chart ideals.  It checks the same two orientations:

```text
p=-2 rtx^2,
A=aua(z-rtx), C=cvg(z+rtx), z=rtx,
A=aua(z+rtx), C=cvg(z-rtx), z=-rtx.
```

The grade-15 numerator is reduced modulo the two coefficient ideals, and the
grade-16 numerator minus `(3/2)rtx^2*cvg^2*theta^2` is reduced modulo the two
root-evaluation ideals.  No source, coefficient, grade, or claimed scope is
changed.  Q and `F_65521` run independently under 24 GiB / 600 s compile /
3600 s engine caps.  Failure remains no mathematical verdict.
