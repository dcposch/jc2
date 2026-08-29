# K00 V27 auxiliary constant-kernel replay

Date: 2026-08-27

Lifecycle: **AUXILIARY PRODUCER-CHECKED / UNREVIEWED / EXPLANATORY ONLY**.

An immutable one-core AWS replay over the full frozen 33-variable rational
polynomial ring independently verified

```text
(5/1024,0,3/128,0,1/8,0,1) A = 0,
A (2,0,1,0,1,0,0)^T = 0,
A (0,1/16,0,1/2,0,1,0)^T = 0.
```

Two fresh Singular processes reconstructed `A` from the frozen atlas and
agreed exactly.  Adding `1` to the selected coefficient of each vector broke
its corresponding identity.  The run also rechecked 90 stored nonzero
`5 x 5` minors and no stored nonzero `6 x 6` minors, consistent with exact
generic rank five.

The proposed left vector does not annihilate the frozen column `b`:
`l0*b` is a nonzero polynomial with exactly 690 terms.  Both processes
serialized byte-identical output with SHA-256
`88516f87868cb27a78ac9b35d15d6aeef3ea555182710424d9520b2f9bfb565e`.
Thus the left relation of `A` does not extend to the augmented final column
`-b` without an additional equation.

These identities are merely explanatory for the global generic-rank-five
ceiling and the vanishing of `I6(A)`.  They hold before imposing `B` and do
not imply either stronger producer containment

```text
I4(A) subset B+I5(A),
I3(A) subset B+I5(A).
```

No sampled-pencil claim or sample point was consumed.

The r6a job used Singular 4.3.2, engine rc 0, 1.75 seconds wall time,
508,396 KiB maximum RSS, and zero swap.  Its lane was
`max12_812_order2_u2_62_k00_v27_kernel_replay_20260827T185700Z_r6a`.

Custody:

- source freeze: `1b397126c922d47db23c68eac15e610f554686fc0db7aa794d97fafdb47b83be`
- immutable archive: `cd1fc03284710c3f6f35fdbe92fa26fb8a34dfaa4106ecd13f7f28db8ab889e0`
- endpoint: `b9358a7dac37bfd9e8c5389e4ce9dddc02af4d35182e7957a943df0f9b2d786d`
- AWS evidence manifest: `2ca2ed27e7d2d051fc50214547483b1c417088749c6aeb6f6d9a2091153233b9`

Firewall: this auxiliary replay proves no ideal containment, rank stratum,
rational point, full-`P6` compatibility, source-open point, later-grade lift,
jet, arc, closure statement, counterexample, or JC2 result.
