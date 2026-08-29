# Adjudication: V24R6R1 exact leading-base D(W) certificate

Date: 2026-08-27

Verdict: **ACCEPT HOSTILE-REVIEW PASS AT THE NARROW EXACT SCOPE.**

The hostile review
`xmodel/max12-812-order2-k00-v24r6r1-leading-base-dw-hostile-review-sol-ultra-20260827.md`
(SHA-256
`f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9`)
independently rederived both the global syzygy and the full-ring embedding.
All cited source/result hashes were rechecked after review.  The producer
source freeze replays 14/14 entries, the rebased producer evidence manifest
replays 26/26, the additive syzygy freeze replays 13/13, and fresh small/full
replays reproduce their marker bytes.

The two producer-tree files omitted from its non-exhaustive evidence manifest
are `outer.stdout` and `outer.stderr`; both are empty and have SHA-256
`e3b0c442...b855`.  They are now pinned together with the producer report,
review, producer result, additive result, extracted `A1,A3,A4`, and fresh
replay markers in `REVIEWED_BUNDLE_R6R1.sha256`.  This is additive custody;
it does not rewrite or pretend to predate the producer manifest.

Accepted exact statements:

```text
W = A1*Q1 + A3*Q3 + A4*Q4 in Q[x0,...,x5].
(Q1,...,Q5,F10,zW-1) = (1).
```

Under `x_i -> d_i_1` and `z -> zinv*k10_0`, the full 36-generator exact-Q
V24 prior/localizer ideal is also the unit ideal.  Therefore the normalized
prefix has no source point on `D(k10_0*W)`; every possible survivor lies on
`W=0`.

No broader inference is accepted: the review does not decide other rank-five
minor charts, rank at most four, grades 7--19 on `W=0`, a full jet, an arc,
K00 closure incidence, order two, maximum twelve, or JC2.
