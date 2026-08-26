# AWS registration: seeded order-four source projection V1

Date: 2026-08-26

Status: preregistered; no endpoint consumed.

## Purpose and charged exact seed

The corrected source-typed V2 exact-Q lane already closed cleanly with
`SOURCE_EQUIVALENCE=PASS`, `SAT_DIM=1`, and a 71-element reduced saturated
basis.  Its source input SHA-256 is
`d2fedf6c9b2b09787c7e45a00f1626ac10f7d4c68c44030102758021a55c9496`;
its stdout SHA-256 is
`5e780dcf82d2a3ac17c3ae7957c819c8b7b8a1a1de6231f88e4f808a2b348c45`.
The V2 source/freeze review is CONFIRMED at SHA-256
`252bbd07d29084952453b45546cff7e0d8ddda7a72576311d1f982ee01a66200`.

This package deterministically extracts that exact basis, verifies all
seed hashes/sentinels/punctuation, reparses it as a monic exact-Q basis, and
checks `dim=1`, size 71, source containment, and `a6` nonzero before doing
anything else.  It does not replace source saturation with an uncharged
guess; it reuses the frozen exact saturation endpoint to avoid recomputing
it at one core.

The seeded-prime lane reduces the monic basis at `p=32003`, independently
computes the native saturated special fibre from the original source rows,
requires two-sided ideal and initial-ideal equality, requires the native
fibre to equal its unique minimal prime, and checks a nonzero irreducible
one-equation `(a5,a6)` contraction.  The seeded-a6 lane independently checks
`J:a6^infinity=J` over Q.  The direct unseeded lanes remain live controls.

## Registered lanes

1. `max12_812_order4_seeded_prime_v1_20260826T025000Z_box03` on Box03,
   instance `i-0ece0b9a3b4a7512f`, IP `98.80.65.144`, expected hostname
   `ip-172-30-0-249`; same-named directory under `/home/ubuntu/jobs/`;
   timeout `3600 s`, virtual-memory cap `67108864 KiB`.
2. `max12_812_order4_seeded_a6_v1_20260826T025000Z_r6d` on r6d, instance
   `i-07eeaf8ba6f0bc419`, IP `100.26.198.153`, expected hostname
   `ip-172-30-0-45`; same directory convention; timeout `3600 s`,
   virtual-memory cap `33554432 KiB`.

Every launcher records actual host/PID/time/caps, archive and emitted-input
hashes, engine version, return code, peak memory, and output hashes.  A hash
or seed mismatch, missing/false sentinel, engine diagnostic, timeout, OOM,
nonzero return, or missing final mode-specific PASS is **NO VERDICT**.

## Scope firewall

Even a clean seeded prime endpoint is a computational premise for the
separate monic good-reduction hand lemma.  It is not by itself a loaded
order-four elimination, maximum-twelve theorem, or JC2 result.  Promotion
also charges exact residual-plane membership/geometry and the componentwise
nonconstant `(q,y)` argument.  The seeded a6 equality is an independent
chart control; after domain promotion, the weaker exact `a6`-nonzero
sentinel already implies injectivity after flat base change.
