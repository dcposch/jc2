# AWS registration: exact top-boundary local delta V4

Date: 2026-08-26

Status: preregistered retry; no endpoint consumed.

- tag:
  `max12_812_order4_mu4_nonzero_topdelta_v4_20260826T013100Z_box03`;
- host: Box03 / `i-0ece0b9a3b4a7512f` / `98.80.65.144`, expected
  hostname `ip-172-30-0-249`;
- same-named directory under `/home/ubuntu/jobs/`;
- timeout `1800 s`; virtual-memory cap `16777216 KiB`;
- exact input SHA-256:
  `6c8e8a0801e36f7cdd02463ddc210cfe20efe6bd03c69713129996c59f6c048c`.

The client translates the exact reconstructed residual plane to the unique
repeated top-face point `(q,w)=(-4/27,0)` and asks Singular's
`hnoether.lib` for the local delta invariant.  It is a diagnostic successor
to V3, whose weighted initial quadratic had zero discriminant.  Consume the
delta only if the AWS transcript contains no library/runtime error and both
`TOP_QB_ISOLATED=1` and `EXACT_TOP_DELTA_V4_COMPLETE=1`.  This client alone
does not certify the global normalization genus or either finite quotient.

The first launcher attempt at `2026-08-26T01:32:24Z` failed before Singular
read the input: relative `AWS_ROOT`/`AWS_RUN` arguments caused
`aws_exact_lane.sh` to look for `repo/run`.  Its empty endpoint is retained
under the original tag and is **NO VERDICT**.  The frozen input is unchanged.
The preregistered corrected retry is
`max12_812_order4_mu4_nonzero_topdelta_v4_retry1_20260826T013300Z_box03`,
in the same-named `/home/ubuntu/jobs/` directory, with the same host,
timeout, memory cap, and frozen hashes; all wrapper paths will be absolute.

The corrected retry launched as PID `134305` at
`2026-08-26T01:33:45Z` and completed in 0.02 s with rc 0 and maximum RSS
13312 KiB.  Its error-free sentinels are
`TOP_QB_DELTA=3`, `TOP_QB_ISOLATED=1`, and
`EXACT_TOP_DELTA_V4_COMPLETE=1`.  Retrieved stdout SHA-256 is
`4791594d69326fc6725e72bd15b6900988cc04f18fa7aaf050fa306c63c33a0a`;
stderr SHA-256 is
`888ace4c7bb079cf86710044a4bb699869202d7dd0b692276ec23787783f734d`
and consists only of `/usr/bin/time -v` telemetry.  Therefore the local
delta at the repeated top point is exactly three.  The global-genus and
finite-cover statements remain successor deductions.
