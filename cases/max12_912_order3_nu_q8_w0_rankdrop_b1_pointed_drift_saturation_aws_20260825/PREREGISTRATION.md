# Preregistration: pointed moving-d4 selected saturation

Date: 2026-08-25

Use the pinned six-row source `(e1,e3,e5,e7,e2,e4)` and the pointed chart

```text
d4=1+v,   d2=2+v+u,
```

so the landing centre is `(v,u,w,x1,x3,x5)=0` while both `d4` drift and the
transverse rank-drop coordinate `u=d2-d4-1` remain in the ring.  Form

```text
J=I+(inv*w*x5*(x3-2*x5)-1).
```

Run two exact characteristic-zero variants:

1. `Q(c)` routing with `c` in the coefficient field;
2. `Q[c]` with `c` a polynomial variable, retaining every finite coefficient
   value and printing the landing basis/eliminant in `c`.

Both must use an `inv` elimination block, exact `std` or `slimgb`, print full
bases, return rc zero, and contain no diagnostics.  A unit in the `Q(c)` lane
is generic only.  A unit in the `Q[c]` selected-localizer ideal is an exact
all-finite-`c` result for this pointed affine chart, still not coefficient
infinity, the rest of the rank-drop line, full Hsrc, Taylor/terminal
realization, trajectories, `(9,12)`, maximum twelve, or JC2.
