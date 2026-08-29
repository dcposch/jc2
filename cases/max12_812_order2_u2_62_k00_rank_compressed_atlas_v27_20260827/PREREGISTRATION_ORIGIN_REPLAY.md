# Preregistration: exact origin replay for `B+I5(A)`

Date: 2026-08-27

Lifecycle before launch: **FROZEN AUXILIARY DESIGN / UNRUN / NOT A NEW
RANK-STRATUM RESULT**.

Independently reconstruct the frozen six-variable matrix `A`, the seven
generators of `B`, and all 90 stored nonzero generators of `I5(A)`.  In two
fresh exact Singular processes, reduce every generator modulo

```text
m0 = (d0_1,d1_1,d2_1,d3_1,d4_1,d5_1).
```

The pass condition is that all 7 generators of `B`, all 90 stored generators
of `I5(A)`, and every entry of `A` have zero normal form.  Adding `1` to the
first `B` and `I5(A)` generator must make its origin normal form nonzero.
Source hashes, two-process output, zero stderr, caps, and zero swap are
fail-closed.

Use audited idle r6a, one core at nice 5, 8,388,608-KiB virtual memory,
600-second outer and 540-second inner caps.  The sole pass status is

```text
PASS_V27_AUX_ORIGIN_B_I5_EXACT_TRIVIAL_Q_POINT
```

If it passes, the useful target is explicitly **not** existence of a rational
point of the homogeneous affine ideal: the origin already supplies that.  A
meaningful downstream target must require a nonzero/projective point, a
source-open condition, or compatibility with the full prior ideal `P6`.

