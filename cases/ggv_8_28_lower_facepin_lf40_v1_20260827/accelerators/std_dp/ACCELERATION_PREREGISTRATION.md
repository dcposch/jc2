# LF40 target-fix R1 exact `std/dp` accelerator preregistration

Date: 2026-08-27  
Lifecycle: **producer-unreviewed exact cross-check; not promoted evidence**

This lane tests the identical corrected LF40 target ideal and row order as the
literal R1 lane.  It changes only the Singular standard-basis engine calls
from `slimgb(J)` to `std(J)`; the exact ring remains `QQ` with `dp` order.
The two synthetic controls already use `std`, so the complete derived program
contains 43 `std` calls: two controls plus 41 literal replacements.

The verifier requires byte identity with

```text
base_program.replace("slimgb(", "std(")
```

and pins 41 replaced calls, zero surviving `slimgb` calls, the corrected
row-17 target exactly once, and omission/opposite-sign target mutations.  The
base compiler and its manifest are replayed from scratch before this derived
program runs.  No equation, variable, saturation factor, row order, stop
condition, target sign, or validator changes.

```text
base program SHA-256    435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7
std/dp program SHA-256  7256fcaddcdc2875ca6c31b2033f0e6950a598b8a22d3cc338c92069a89f21a5
workers                 1
nice level              5
virtual-memory cap      943718400 KiB (900 GiB)
outer wall cap          21600 seconds
inner Singular cap      21000 seconds
required swap count     0
```

Placement is the audited existing Box02 AWS node after the legacy K00 R5
lane ended and released all processes.  A unit prefix or proper row-40
fixture has exactly the base R1 mathematical meaning but remains provisional
until the raw program, hashes, output and certificate are independently
reviewed.  A resource cap is no verdict.  No family exclusion, source
landing, counterexample, or JC2 conclusion follows automatically.
