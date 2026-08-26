# AWS registration: seeded order-four source projection V2

Date: 2026-08-26

Status: **preregistered; no endpoint consumed**.

## Repair and immutable V1 control

V1 is immutable and non-decisive.  Its exact-`Q` basis was passed through
`std`, but that basis was not scalar-normalized before the monicity test;
the test printed `SEEDED_Q_MONIC=0`.  Singular 4.3.2 also treated the
attempted `exit(81)` as an undefined command and continued, so every V1
endpoint is quarantined even if it later prints a `PASS` token.

V2 scalar-normalizes every nonzero member of `std(JQ)`, checks two-sided
equality with the unnormalized basis, and repeats all V1 source/dimension/
size/nonvanishing checks.  Failure branches use `quit;`.  An outer shell
validator independently requires exactly one preflight PASS, exactly one
mode-specific final PASS, no `=FAIL`, no Singular `?` diagnostic, and a
zero engine return.  Any other endpoint is no verdict.

The charged exact source and 71-element saturated basis remain the frozen
corrected V2 inputs with SHA-256
`d2fedf6c9b2b09787c7e45a00f1626ac10f7d4c68c44030102758021a55c9496`
and
`5e780dcf82d2a3ac17c3ae7957c819c8b7b8a1a1de6231f88e4f808a2b348c45`.

## Registered lanes

1. `max12_812_order4_seeded_prime_v2_20260826T025800Z_box03` on Box03,
   instance `i-0ece0b9a3b4a7512f`, IP `98.80.65.144`, expected hostname
   `ip-172-30-0-249`; directory `/home/ubuntu/jobs/` plus the tag;
   timeout 3600 s and virtual-memory cap 67108864 KiB.
2. `max12_812_order4_seeded_a6_v2_20260826T025800Z_r6d` on r6d,
   instance `i-07eeaf8ba6f0bc419`, IP `100.26.198.153`, expected hostname
   `ip-172-30-0-45`; same directory convention; timeout 3600 s and
   virtual-memory cap 33554432 KiB.

Every launch records the actual host, job directory, launcher PID, start
time, timeout, memory cap, compiler output, emitted-input hash, engine
version, resource log, raw outputs, and independent validation status.

## Scope firewall

The a6 lane tests only the exact chart equality `J:a6^infinity=J`.  The
prime lane tests the separately stated good-reduction premise.  Neither
alone proves source-component coverage, the genus obstruction, an
order-four leaf elimination, `(8,12)`, maximum twelve, or JC2.
