# Result: exact K00 filtered compatibility through degree 8

Date: 2026-08-27

Status: **PROMOTED AT THE EXACT FILTERED-JET TIER AFTER OPUS5 HOSTILE REVIEW.**

At the frozen normalized K00 coefficient germ `C6=1`, let
`m=(d0,...,d5)` and let `r1,...,r7` be the unloaded ordinary tails.  The
complete cumulative degree-8 Macaulay system has

```text
2996 equations x 5544 multiplier coefficients
rank(A) = rank([A|r7]) = 2547 over Q.
```

The saved exact rational multiplier jet has 492 nonzero entries and replays
all 2,996 coefficient equations.  Therefore the producer establishes

```text
r7 in (r1,...,r6) + m^9    at C6=1.
```

Exact evidence:

```text
matrix SHA-256   15837b4e24431a61e4cc8f2498bc4cd27959b03b6150f76609b319c1dcbabc30
lift SHA-256     0b29e3cc3485b39370ed59a8833328b51d469e104eed6edcfabc3d6f5fadb360
RESULT SHA-256   cc2bed36104932b731c1408b3ab7af635cdc86a2162cf8026db0dc1c4a4b852a
```

The exact solve took 15m55s, peaked at 8,174,576 KiB RSS, and used no swap.
The registered `p=65521` software control used the byte-identical emitted
matrix, found the same rank and augmented rank 2547, and replayed a
492-entry modular lift.  It is corroboration only, not characteristic-zero
evidence.

Opus5 independently regenerated the matrix byte-for-byte from `tails.json`,
recomputed all seven exact-Q ranks through D8, and replayed both all 2,996
linear equations and the ordering-free polynomial identity.  Its review is
`xmodel/max12-812-order2-k00-d8-hostile-review-opus5-20260827.md`, SHA256
`7f0c3aea3ef9cf299b2fac00f62627d765c92e0b721efbe88248a69390a92bcd`.
It also showed by an exact degree-eight RHS mutation that D8 compatibility
is strictly stronger than D7 compatibility.

Review notes which do not weaken the theorem: the producer validator reads
the rank integers from solution metadata rather than recomputing them (the
review independently recomputed them over Q), and the modular JSON field
`characteristic_source: 0` describes the characteristic-zero tail source,
not the modular engine.  The latter lane remains control-only.

This extends the reviewed V9 compatibility from `m^8` to `m^9`.  It remains
consistent with V8 global polynomial nonmembership: a compatible finite jet
does not imply polynomial, local, or formal membership.  No conclusion is
licensed about an eventual finite obstruction, mixed `Lambda`/loads/targets,
`mu`, `Jdet`, closure-first incidence, Taylor realization, a receiver
theorem, order two, maximum twelve, or JC2.

Frozen and harvested evidence:

- `PREREGISTRATION.md`, `FREEZE.sha256`, and `AWS_REGISTRATION.md`;
- exact lane `aws_q_box01_pass/`;
- modular control `aws_p65521_box02_pass/`.
