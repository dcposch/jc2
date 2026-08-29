# V82QSS2 typed q11/q16 CURRENT-symbol split

V82QSS2 is the minimal typed-constructor repair of V82QSS.  The old dual-host
run reached exact transport, FIRST, PREVIOUS/POLE, and an identical affine
`f3[0]` dump, then failed before its symbol assertions because it passed the
bare FLINT polynomial `U^6` directly to `E3`.  Those four `rc=1` streams are
software/deployment negatives and have no q11/q16 verdict.

The only mathematical-code change is

```text
E3(U^6)  ->  E3(Rat3(U^6)).
```

The rerun retains the reviewed parent, exact source keys, direct-q-prime
omission, full versus omission pivot replay, q11 and q16 post-elimination maps,
and the q15 lower-target-shear marker.  It runs independently on Box03 and r6d,
with 4 GiB and 10,800 seconds per lane.

Expected discriminators:

- q11: verify the raw direct coefficient from `3 q' f3`, then determine whether
  its post-CURRENT class is exactly the observed singleton;
- q16: verify a nonzero raw direct term and determine whether its exact
  post-CURRENT class vanishes by source-row/pivot reduction;
- q15 is not promoted to a free q axis: it remains only the combined
  lower-target-shear marker `(delta q, delta g)=(p,f)`.

Fail closed on any typed mismatch, source-parent mismatch, omission mismatch,
pivot mismatch, denominator change, or host disagreement.  Scope is the fixed
source-typed A3 square-zero generic section.  No q-neighborhood, family, TD6,
SP-2, landing, or JC2 inference is licensed.
