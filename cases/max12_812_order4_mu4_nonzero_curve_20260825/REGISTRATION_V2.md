# Registration V2: normalized `(8,12)` order-four `mu_4 != 0` curve

Date: 2026-08-26

Status: preregistered after hostile-review repair; endpoints not yet consumed.

## V1 quarantine

The V1 producer, compiler, and all V1 AWS outputs are immutable controls and
are **NON-PROMOTABLE**.  Hostile-review SHA-256
`0877fc072583c3a484ad7740e0abc6a0a981be6ad4b17e4002765f21e97cd57b`
found three wrong full parent hashes in V1 §1.  It found no wrong mathematical
identity or compiler formula.  V2 changes only those pins and the resulting
client/compiler hashes.

## V2 freeze

- client SHA-256:
  `c1aa88b40104205f327240dd33a4e674983577ce6d9dfafc82b8547959312621`;
- compiler SHA-256:
  `b000ed1557bd307dc37b92fd1ff3fbe1e075cec169721d346a28599374890e1b`;
- freeze-manifest SHA-256:
  `d4a5c584a792d38d74c09b607da4777ba83715d0d092c590b99f15083b35e31b`.

The exact actual parent hashes are included in `FREEZE_V2.sha256` and must all
verify on AWS before compilation.

## V2 compile prelaunch

- tag: `max12_812_order4_mu4_nonzero_curve_v2_compile_20260826T002224Z_box02`;
- Box02 instance `i-010201a5da47795c4`, current IP `34.203.207.55`, expected
  hostname `ip-172-30-0-186`;
- remote job directory:
  `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_curve_v2_compile_20260826T002224Z_box02`;
- timeout `7200 s`, memory cap `134217728 KiB`;
- the remote launcher records its actual PID, host, caps, UTC time, and input
  hashes before invoking the AWS-only compiler.

No V1 endpoint is inherited.  The emitted V2 Singular input must be hashed
and preregistered anew before exact-Q replay.

The V2 compile completed `rc=0` on hostname `ip-172-30-0-186`.  Its emitted
Singular input SHA-256 is
`5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`;
byte identity with the V1 emitted input is expected because the repair changed
only documentary source pins, but no V1 result is inherited.

## V2 exact-Q prelaunch records

All three lanes below were registered before their V2 payloads began and use
that emitted input.

1. `max12_812_order4_mu4_nonzero_curve_v2_modsatQ_20260826T002334Z_box02`;
   Box02; same-named `/home/ubuntu/jobs/` directory; exact `modStd` plus
   `modSat` with installed final exact tests; timeout `21600 s`, cap
   `402653184 KiB`.
2. `max12_812_order4_mu4_nonzero_curve_v2_directQ_20260826T002334Z_box02`;
   Box02; same-named job directory; unmodified direct characteristic-zero
   Singular input; timeout `21600 s`, cap `402653184 KiB`.
3. `max12_812_order4_mu4_nonzero_curve_v2_directQ_20260826T002334Z_box03`;
   Box03 instance `i-0ece0b9a3b4a7512f`, current IP `98.80.65.144`;
   same-named job directory; byte-identical direct-Q replay; timeout `21600
   s`, cap `402653184 KiB`.

Every launcher records actual hostname, PID, caps, input hash, UTC time,
engine version, return code, and output hashes.  Promotion requires the V2
source-equivalence sentinels and agreement of the reconstructed endpoint;
timeouts or disagreement are **NO VERDICT**.

## V2 exact plane-model prelaunch

Without waiting on the background direct-Q controls, tag
`max12_812_order4_mu4_nonzero_curve_v2_planeQ_20260826T002619Z_box02` was
preregistered on Box02 in the same-named `/home/ubuntu/jobs/` directory,
with timeout `21600 s` and cap `402653184 KiB`.  It uses the V2 emitted
equations, exact `modStd`/`modSat`, and block order
`(dp(a0,...,a4),dp(a5,a6))`; it prints and factors the exact Q elimination
ideal in `(a5,a6)`.  It inherits no V1 endpoint.  Birationality, deck
quotient, and terminal-passport interpretation remain separate gates.

The V2 plane lane launched on hostname `ip-172-30-0-186` at
`2026-08-26T00:30:37Z`, launcher PID `258732`, with exact input SHA-256
`a9628edc67aedef93c084c48516be4ad365c6e7cb94a12e81a65c942eddac05d`.
It remains live; an absent output is **NO VERDICT**.

## V2 delta hostile review

The unique-output V2 delta review is

```text
xmodel/max12-812-order4-mu4-nonzero-coefficient-curve-review-grok-v2-20260825.md
```

with SHA-256
`252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200`
and overall verdict **CONFIRMED**.  It used no live AWS endpoint.  The exact
modular-Q endpoint and both direct-Q controls remain computational gates
separate from that source/freeze confirmation.
