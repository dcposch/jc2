# AWS registration: exact top-boundary HN branch V5

Date: 2026-08-26

Status: completed exact diagnostic; global quotient premise still open.

- tag:
  `max12_812_order4_mu4_nonzero_tophn_v5_20260826T013800Z_box03`;
- host: Box03 / `i-0ece0b9a3b4a7512f` / `98.80.65.144`, expected
  hostname `ip-172-30-0-249`;
- remote job directory: same-named directory under `/home/ubuntu/jobs/`;
- timeout `1800 s`; virtual-memory cap `16777216 KiB`;
- engine: exact characteristic-zero Singular 4.3.2 `hnoether.lib`;
- exact input SHA-256 is recorded in `FREEZE_TOP_HN_V5.sha256` before launch.

This client replays the V4 delta, translates by the repeated weighted
tangent `w=slope*q^3`, and prints the complete Hamburger--Noether numerical
invariants.  Its purpose is to distinguish one cusp branch from multiple
tangent branches and thereby freeze the orders of `q` and `v=1/w` at the
repeated top point.  It does not assert the global normalization genus or
that the reconstructed plane is the complete invariant image.

The lane launched as PID `135507` at `2026-08-26T01:40:42Z` and completed
in 0.02 s with rc 0 and maximum RSS 12308 KiB.  It printed no Singular
error.  Exact output:

```text
TOP_QB_REPEATED_SLOPE=1/52488
TOP_QB_DELTA_REPLAY=3
TOP_QB_BRANCHES=1
TOP_QB_BETA=2,7
TOP_QB_SEMIGROUP=2,7
TOP_QB_CONDUCTOR=6
EXACT_TOP_HN_V5_COMPLETE=1
```

Retrieved stdout SHA-256 is
`59c2c35f2288f6c983925dba4a855a28e49eadc9d9db5ef84aa78b6bed2a971d`;
stderr SHA-256 is
`6f2782d1de80de75277bce7c952f4f5b820a859838e26196955f32ff232524b2`
and contains only `/usr/bin/time -v` telemetry.  Thus the repeated top
point is one `(2,7)` cusp branch.  If `tau` is its normalization parameter,
then `ord_tau(q+4/27)=2` and
`w=(1/52488)tau^6+O(tau^7)`, so `ord_tau(v)=-6` for `w=1/v`.
