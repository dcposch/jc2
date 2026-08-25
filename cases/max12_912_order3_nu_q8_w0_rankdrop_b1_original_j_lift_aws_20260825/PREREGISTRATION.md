# Preregistration: original-J cofactor over Q(c)

Date: 2026-08-25

Use exactly the pinned six-row source `(e1,e3,e5,e7,e2,e4)`, substitute
`d4=1,d2=2+u`, and form

```text
J=(phi(e1),phi(e3),phi(e5),phi(e7),phi(e2),phi(e4),
   inv*w*x5*(x3-2*x5)-1)
```

in `Q(c)[inv,w,u,x1,x3,x5]`.  Compute `lift(J,(1),U)` directly, print the
complete transformation coefficients, require the exact residual to vanish,
and require the returned scalar `U[1,1]` to be a nonzero coefficient-field
unit.  Normalize by it and verify `1-matrix(J)*H=0` exactly.

Acceptance is source regeneration, rc zero, no diagnostic, both exact
residuals zero, a nonzero degree-zero `U[1,1]`, and complete printed `H`.
This is only a source-generator membership certificate over `Q(c)` in the
frozen `d4=1` slice.  Denominators in `c`, exceptional finite values, moving
`d4`, full rank-drop/Hsrc, infinity, and trajectories remain charged.
