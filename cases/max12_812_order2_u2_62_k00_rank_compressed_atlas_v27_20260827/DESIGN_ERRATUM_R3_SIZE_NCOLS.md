# Design erratum: V27 R3 per-slot `size()` bounds

Date: 2026-08-27

Lifecycle: **ADDITIVE CORRECTION / HISTORICAL PRODUCER BYTES RETAINED /
SUCCESSOR REPAIR REQUIRED**.

The frozen R3 producer endpoint remains exact evidence for properness,
dimension two, and the strict ideal cut, but its numerical marker
`I2OUTSIDE=237` is not a complete slot census.  Singular 4.3.2 retains 441
literal columns in `I2A` and `reduce(I2A,SJ2)`, while `size()` returns the
number of nonzero entries.  Bounding a positional scan by `size()` therefore
does not visit every column.

The different-model review at
`xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md`, SHA-256
`738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a`,
establishes the corrected exact census:

```text
ncols(I2A) = ncols(I2MOD) = 441,
size(I2A) = 351,
size(I2MOD) = 291,
true nonzero normal forms over all 441 slots = 291,
zero normal forms among the 351 nonzero determinants = 60.
```

The original R3 report hash
`5f9700c7e67eaa5255ef642ff4e784983d71da9f8c5394d6cb01245c9c0a873d`,
endpoint JSON, scripts, source archive, transforms, streams, and evidence
manifests remain historical and must not be rewritten.  The report carries
an additive correction; a repaired review packet binds it to the immutable
producer endpoint and hostile review.

For every successor, `size()` may be used only when the intended quantity is
explicitly the count of nonzero entries.  Every positional loop, entrywise
zero test, first-slot selection, reverse-inclusion replay, origin replay,
standard-basis column scan, and matrix-shape comparison must use `ncols()`
(and `nrows()` for rows).  A source grep finding `<=size(` in a generated
Singular loop is a prelaunch failure.  The R1/R2 conclusions survive because
the hostile reviewer independently checked all 594 and 813 relevant minors;
the defective guards are nevertheless forbidden in new source.

The corrected dimension comparison `dim(R/J2base)=3` and
`dim(R/J1base)=2` proves distinct radicals and a nonempty rank-exact-two
stratum over an algebraic closure.  It gives no explicit or rational point
and no full-`P6` or later compatibility.
