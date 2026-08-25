# Independent Singular control for the F_127^2 point count

This producer is an engine-independent control for the frozen python-FLINT
point count of the pinned plane curve `H(w,v)=0`.  A small Python program only
transcribes the pinned coefficient table into Singular syntax.  All field
arithmetic, modular powering, polynomial gcds, differentiation, and degree
counts are performed by Singular 4.3.2 over

```text
F_127[a]/(a^2-a+3).
```

The first charged stage checks four fibres (`w` indices 0, 39, 71, 128)
against the frozen exact counts.  Only after that passes may a shard be run.
Shard mode compares each Singular count with the frozen FLINT `per_w` table,
but the computations are independent.  This case is a software control only;
it does not broaden the reviewed positive-genus theorem.

Every substantive computation is AWS-only.  Local work is limited to source
editing, hashing, shipping, and status inspection.

## Charged endpoints

- `q8_p127_fq2_singular_controls_r6a_v1`: harness-negative control.  The
  four counts are correct, but Singular reports the invalid final spelling
  `exit(0)` and the fail-closed wrapper rejects the run.
- `q8_p127_fq2_singular_controls_r6a_v2`: corrected four-fibre PASS.
- `q8_p127_fq2_singular_shard0000_0016_r6a_v1`: 16-fibre pilot PASS.
- `q8_p127_fq2_singular_full_r6a_v1_i00` through `i15`: full disjoint
  16,129-fibre census, all PASS.
- `q8_p127_fq2_singular_aggregate_r6a_v1`: fail-closed aggregate PASS,
  totals `16174 / 16168 / 6`.

The first background fanout did launch the charged full lanes.  A repeated
orchestration attempt used the same tags and stopped before computation at
the runner's `test ! -e "$outdir"` gate.  It created no second Singular
lane and changed none of the charged output directories.  Launcher logs are
not load-bearing; each charged directory carries its own source/output hashes
and the aggregate verifies them directly.
