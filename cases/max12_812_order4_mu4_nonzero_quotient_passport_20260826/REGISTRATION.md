# AWS registration: order-four invariant quotient/passport graph V1

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

## Frozen source

- specification SHA-256:
  `d315cfd6b0c52bb704705ed9d3e3e991efaa07775cafddccabc4407614e7aed1`;
- compiler SHA-256:
  `9b2c9dc586b8ba25c2ff150dcc79118fbf3c1aec1f3ae9f2722133bcf9b0fe0d`;
- corrected-V2 emitted input SHA-256:
  `5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`.

`FREEZE.sha256` contains every charged source and must verify on AWS before
compilation.

## Compile and exact graph launch

- registered tag:
  `max12_812_order4_mu4_nonzero_quotient_graph_v1_20260826T004212Z_box03`;
- instance: Box03, `i-0ece0b9a3b4a7512f`, public IP `98.80.65.144`,
  expected hostname `ip-172-30-0-249`;
- remote job directory:
  `/home/ubuntu/jobs/max12_812_order4_mu4_nonzero_quotient_graph_v1_20260826T004212Z_box03`;
- timeout: `21600 s`;
- virtual-memory cap: `402653184 KiB`;
- engine: exact characteristic-zero Singular `modStd`/`modSat` with installed
  final exact tests, followed by exact elimination;
- preregistered endpoints: corrected source equivalence, exact `r_7` and
  `a_6` saturations, deck graph `(q,y,rho)`, residual graph `(q,v,R16)`, and
  their curve images.

The host, PID, UTC start, archive/input hashes, engine version, caps, return
code, and output hashes must be recorded before any endpoint is interpreted.
`A6_CHART_LOSS=1`, timeout, OOM, failed exact reconstruction, or missing
sentinel is **NO VERDICT**.  Genus and passport degree are successor gates on
the complete normalizations; this graph job does not use affine genus.

The frozen archive was transferred and verified on hostname
`ip-172-30-0-249` with SHA-256
`bcb504a3bb40924cda9bf6050ed364fb979eafbe4d528259a3690d408f11b60a`.
All lines of `FREEZE.sha256` passed there.  The AWS-only compiler emitted
input SHA-256
`9061aab76ceac34e5b7df0204110d0b54434d83444c145fc089cfcf735f84d53`.
The exact graph lane began at `2026-08-26T00:43:30Z`; launcher PID `126184`
and all descendants run on Box03.  No local CAS or symbolic Python process
was used.
