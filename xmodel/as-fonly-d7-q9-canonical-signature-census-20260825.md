# AS F-only D7 Q9 canonical-signature census

Status: **PROVISIONAL PRODUCER; exact finite census, independently replayed**

## Exact statement

In the frozen 13-coordinate Q9 chart

```text
free_q9 = (0,1,2,3,4,5,6,7,8,9,14,16,18),
t10=t11=t12=t13=t15=0, t17=1,
```

the source-pinned compiler exhausts all `3^13 = 1,594,323` states.  For the
canonical RREF particular at the next stage it finds:

| exact datum | count |
|---|---:|
| Q8 rank pair `(13,13)` | 1,594,323 |
| Q7-zero-section rank pair `(9,9)` | 177,147 |
| Q7-zero-section rank pair `(9,10)` | 1,417,176 |
| full presentation signatures | 59,049 |
| size of every presentation-signature class | 27 |
| compatible labelled classes | 6,561 |
| incompatible labelled classes | 52,488 |

The compiler asserts source rows before consumption, reconstructs the exact
integer Q8/Q7 carry data, hashes the RREF matrices, right-hand sides,
particulars, kernels and reduced work matrices, and forbids a signature from
receiving two labels.  The aggregate repeats that label-homogeneity assertion
across shard boundaries.  Thus the displayed class split is exact at the
defined presentation tier.

This says that every chart state reaches a canonical Q8 particular and exactly
one ninth of those canonical particulars admits the Q7 **zero section**.  It
does **not** say that the remaining eight ninths have empty Q8 fibres.

## Independent replay

Two AWS runs used the same frozen source archive but different deterministic
shard boundaries.

| run | host/tag | shards | wall / max RSS | outcome |
|---|---|---:|---|---|
| canonical | Box02, `/home/ubuntu/jobs/as_q9_signature_census_v3_20260825T0512Z_b` | 48 | 8m39.22s / 52,144 KiB | exit 0 |
| independent | r6d, `/home/ubuntu/jobs/as_q9_signature_census_v3_independent_20260825T0510Z` | 37 | 12m51.43s / 54,720 KiB | exit 0 |

Both runs have empty per-shard stderr and zero swap.  They agree byte-for-byte
on all shard-layout-independent payloads:

```text
ordered fixed-record stream  49a563074021509150c03446b1b2257f564c1fa839d57504be12006776206a14
classes.tsv                  c42e62a1fc485874ba820912fb5ae7a3cf366f2cf6de9e261dc90d40e8acea72
representatives.tsv          cb21c2768374bb003b0b300587b8a6368c6536eb9ff25a49365dfa9435464846
```

The aggregate JSON hashes differ because `shard_count` and the shard-payload
Merkle stream are deliberately part of that file: Box02 is `6cf69216...` and
r6d is `8426f5c1...`.

## Controls and provenance

- V1 stopped before records on the stale symbol `q9_vector`; it is deployment
  negative evidence only.
- V2 stopped at state 729 because its preregistered assertion incorrectly
  required every canonical Q8 particular to admit the Q7 zero section.  This
  was a useful fail-closed negative control and motivated V3's two-label split.
- State 0 is a compatible positive control.  State 729 is the pinned
  `Q7-zero-section incompatible / full-Q8-fibre open` control.
- The running-source closure hash is
  `28f1bd2bf0e8d0d076aff2b04969d714ab1ea655c9518758364e3679d82786b6`;
  the source archive hash is
  `7288f49de272e3202f2e198f47039c32c7aa5226ed8b37fbb80266646953b1c5`.

The two portable result archives retain the aggregate, class tables, all shard
summaries and class fragments, source archive/checks, smoke controls where
present, runtime custody, and a SHA-256 manifest of the remote full outputs.
The 204 MB fixed-record payload remains at each pinned AWS job and is covered
by those manifests rather than duplicated in the repository.

## Refusal scope and next gate

No equality of presentation hashes is claimed to be a mathematical transition
equivalence.  No nonzero 19-dimensional Q8 fibre was exhausted here.  There is
no all-depth lift, no no-lift result, and no Jacobian-conjecture inference.

The nonblocking successor is two-pronged:

1. source-honest cross-tab/refinement of the 59,049 presentation classes,
   including the actual `(s15,t6,s17,t8)` canonical particulars; and
2. witness-first existential search over nonzero Q8 fibre coordinates, with
   direct integer-source replay and a full lifting-Jacobian minor test on every
   survivor.

