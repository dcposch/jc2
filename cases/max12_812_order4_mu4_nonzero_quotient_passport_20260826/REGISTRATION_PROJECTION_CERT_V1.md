# AWS registration: order-four source projection certificates V1

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

## Frozen source and method

Both lanes compile from the corrected-V2 emitted coefficient source, SHA-256
`5b401beac071a22ec9ad3fc022bf9f87a255e40fdb141359f4bdc40d8547fa47`.
The compiler must verify that hash and the unique saturation marker on AWS.

The first lane independently verifies over `Q` that saturating the already
`r7`-saturated source ideal by `a6` changes nothing.  The second computes the
reduced characteristic-zero Groebner basis, maps it to `F_32003`, requires
equality with the native saturated special fibre and equality of initial
ideals, then requires that this special fibre equal its unique
`minAssGTZ` prime.  Finally it requires a principal irreducible
one-dimensional `(a5,a6)` elimination.  The intended hand lemma is the
monic-good-reduction criterion: a monic Groebner model over `Z_(32003)` is
free over the DVR, and a domain special fibre implies a domain generic
fibre.  The computation does not by itself discharge that hand lemma or
the link to the exact candidate plane; those are theorem/review gates.

## Registered AWS lanes

1. tag
   `max12_812_order4_mu4_nonzero_a6_complement_v1_20260826T020100Z_r6d`;
   host r6d, instance `i-07eeaf8ba6f0bc419`, public IP `100.26.198.153`,
   expected hostname `ip-172-30-0-45`; remote job directory with the same
   tag under `/home/ubuntu/jobs/`; exact-Q Singular; timeout `7200 s`;
   virtual-memory cap `67108864 KiB`.
2. tag
   `max12_812_order4_mu4_nonzero_projection_primelift_v1_20260826T020100Z_r6d`;
   same host and directory convention; exact-Q plus exact `F_32003`
   Singular; timeout `7200 s`; virtual-memory cap `134217728 KiB`.

Each remote launcher must record hostname, actual PID, UTC start, caps,
source archive/input hashes, engine version, return code, and output hashes
before an endpoint is interpreted.  Any hash/source sentinel failure,
inequality, timeout, OOM, non-prime special fibre, non-principal/reducible
projection, or absent completion token is **NO VERDICT**.

## Launch record

The byte-identical source archive has SHA-256
`97c74dd91e492a05b37ee6fe82c5d7977deac4e065bc558efa8847bc4cb27f1b`.
Both remote freeze checks passed on hostname `ip-172-30-0-45` and both lanes
started at `2026-08-26T02:02:14Z`.  The exact launcher PIDs and AWS-emitted
input hashes are:

- `a6`: PID `204070`, input SHA-256
  `dfccafe4be0d0ebc2001d7792de8d25562d49f0228f593379928715b4881599a`;
- `prime-lift`: PID `204071`, input SHA-256
  `8bfca82875b686ba4a68d00411021cc04c84210d1aedff273855dbbaf5f7ceb2`.

Both lanes remain live; absent output is **NO VERDICT**.
