# LF40 target-fix R1 exact `std/dp` Box02 launch

Lifecycle: **live producer cross-check; unreviewed and not promoted evidence**

The exact engine-substitution lane launched at `2026-08-27T21:24:42Z` on
Box02 (`ip-172-30-0-186`):

```text
tag        = ggv_8_28_lf40_targetfix_r1_std_dp_20260827T212404Z_box02
wrapper    = 379764
Singular   = 379803 (initial process; subject to timeout-wrapper lifecycle)
algorithm  = std
order      = dp
workers    = 1
VM cap     = 943718400 KiB
wall caps  = 21600 / 21000 seconds
```

Immutable pins:

```text
source freeze  336a5295394dc3d84aebf268e720ac4ec0b7906a282f9ac527cff3b33e80992f
source archive a5fc34dca5898c6e2d4c990f541ce3ddef4f3d90cd2e524ecdc283b0b5773b65
program        7256fcaddcdc2875ca6c31b2033f0e6950a598b8a22d3cc338c92069a89f21a5
```

The remote runner replayed the complete source freeze, desk gate and patched
LF40 compiler, then regenerated and byte-compared the derived program.  The
independent verifier found exactly 41 `slimgb`-to-`std` substitutions, the
row-17 target exactly once, and rejected omission/opposite-sign mutations.
Synthetic controls and row 0 passed before Singular entered row 1.  At launch
the host had about 1.9 TiB available and zero swap.  This lane changes no
mathematical input and remains a cross-check until its output is independently
reviewed.
