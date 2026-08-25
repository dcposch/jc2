# Q8 component grouping by exact localization contraction (AWS-only)

This is a distinct exact implementation of the same saturation used by the
active component-grouping lane:

```text
(I, 1-inv*f) intersect R = I:f^infinity,
f=w*x5*(x3-2*x5).
```

The ring puts `inv` alone in the first elimination block.  It computes the
localized basis, contracts by eliminating `inv`, and only then runs modular
minimal-prime/Q8-boundary grouping.  This retains closure points at `w=0`
while removing components contained in the punctured boundaries.

The package is support-learning at finite characteristic.  Even a component
with several Q8 roots modulo a prime cannot prove characteristic-zero or
geometric component grouping; it only selects the exact absolute-decomposition
successor.  No result is claimed until remote output is harvested and frozen.

Estimated guard: one core, 12 hours, at most 256 GiB RSS.  Run only on AWS.
