# AS F-only `D=7`: Q9 rank is not a sufficient Q8 transition state

**Status: PRODUCER EXACT AT SAMPLED-CANONICAL SCOPE; PROVISIONAL PENDING
DIFFERENT-MODEL REVIEW.**

Twenty-seven deterministic Box02 shards traversed all 33,225 states accepted
by the corrected Q10 source.  Within each structural shard, the compiler
retained at most four canonical representatives of each exact Q9 rank pair
and reconstructed their Q9 witnesses and Q8 transition matrices.  The
resulting sample counts are

```text
Q9 rank pair    sampled    Q8 compatible
(13,13)              4          0
(13,14)              4     Q9-incompatible control
(15,15)              4          4
(16,16)             84          4
(16,17)             36     Q9-incompatible control
(17,18)             36     Q9-incompatible control.
```

For every compatible Q9 witness the top Q8 block has rank 13.  The rank-13
sample has full Q8 rank pair `(13,14)` and Kuranishi rank zero, so all four
sampled witnesses are obstructed.  The rank-15 sample has full pair `(14,14)`
and Kuranishi rank one, so all four extend.  Most importantly, the 84
rank-16 witnesses split: four have full pair `(15,15)` and extend, while 80
have `(15,16)` and do not.

Those 84 rank-16 records have fifteen distinct exact Q8 matrix/RREF
signatures.  Therefore the scalar Q9 rank pair—even together with the fact
that its affine fibre is nonempty—is not a sufficient state for the Q8
transition.  Canonical coefficient/Bockstein data inside the rank stratum
must be retained.  The next compression problem is to cluster the fifteen
signatures by explicit coefficient invariants rather than opaque hashes.

The AWS run used tag `as_q9_rankclass_q8_samples_20260825T022400Z` on
Box02 from 02:21:56Z to 02:26:10Z, with all 27 shard sentinels present,
return code zero, and empty stderr files.  Aggregate JSON SHA-256 is
`492a70d7145578bf35730b0a48dc54687f8de3c7168dc1a23b7f0f4c0404b967`;
the ordered shard Merkle digest is
`20d2dd31b184e44ea7ffca36df82a5435e60b8b901e0449b56fb469890b5694d`.

This is a deterministic sample, not a rank-class census.  The fractions
above are not population rates, and no conclusion applies to unsampled
witnesses, whole fibres, fixed-cap/all-depth lifting, counterexamples, or
JC2.
