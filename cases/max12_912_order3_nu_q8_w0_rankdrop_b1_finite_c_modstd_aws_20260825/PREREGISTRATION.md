# Preregistration — frozen-`d4` finite-`c` `modStd` mirror

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Independently mirror the direct Box02 `Q[c]` saturation using Singular's
`modStd` algorithm and an explicit Rabinowitsch localizer.  In the pinned six
rows set `d4=1,d2=2+u`, retain `c` as a polynomial variable over `Q`, and
compute

```text
J       = I + (zinv*w*x5*(x3-2*x5)-1),
C       = eliminate(modStd(J),zinv),
Landing = modStd(C) + (w,u,x1,x3,x5).
```

Acceptance requires rc0, no diagnostics, original/contraction/landing
remainders zero, and an exact printed basis.  `Landing=(1)` excludes every
finite `c` at the frozen-slice centre; it is not `C=(1)` unless separately
printed, and never covers moving `d4`, coefficient infinity, full Hsrc,
terminal/Taylor realization, trajectories, maximum twelve, or JC2.
