# AWS registration: seeded order-four source projection V3 raw-reduction control

Date: 2026-08-26

Status: **preregistered; no endpoint consumed**.

## Purpose and immutable predecessors

V1 remains immutable and non-decisive because its monicity preflight failed
and its attempted nonzero exit did not stop Singular 4.3.2.  V2 is a precise
near-pass: it proves the exact normalized basis, native special-fibre prime,
one-dimensionality, plane contraction, and the `a6` chart statement, but its
prime lane compares the standard basis of the coefficientwise reduction with
the native special fibre rather than explicitly certifying that the raw
coefficientwise reduction is itself a standard basis.

V3 consumes the exact V2 emitted prime input with SHA-256
`28721c66a0838487dc9490f1a33cd4b3d95324ffe80aaef9dcedabed3c10645a`.
It adds the missing two-sided equality between the leading-term ideal of the
raw reduction and the initial ideal computed from its standard basis.  Since
both lists generate the same ideal, that equality is the charged standard-
basis certificate.  Only after this equality is proved does V3 set the
special-fibre `isSB` attribute and require the computed standard basis to
reduce to zero.  Separately, V3 explicitly marks the characteristic-zero
scalar-normalized basis as standard only after its elementwise nonzero-scalar
normalization; this is valid because such scaling preserves a standard basis
and prevents the benign V2 `GQ is no standard basis` warnings.

## Registered independent lanes

1. `max12_812_order4_seeded_prime_v3_rawgb_20260826T031500Z_box03` on
   Box03, instance `i-0ece0b9a3b4a7512f`, IP `98.80.65.144`, expected
   hostname `ip-172-30-0-249`; directory `/home/ubuntu/jobs/` plus the tag;
   timeout 3600 s and virtual-memory cap 67108864 KiB.
2. `max12_812_order4_seeded_prime_v3_rawgb_20260826T031500Z_r6d` on r6d,
   instance `i-07eeaf8ba6f0bc419`, IP `100.26.198.153`, expected hostname
   `ip-172-30-0-45`; same directory convention; timeout 3600 s and
   virtual-memory cap 67108864 KiB.

Every launch records host, exact job directory, launcher PID, start, timeout,
memory cap, V2 and V3 compiler outputs, emitted hashes, engine version,
resource log, raw outputs, the `rc=0` field in the exact-lane `.meta` file,
and an outer validation file.  The validator requires zero engine return,
unique exact PASS sentinels, no `=FAIL`, no Singular `?` diagnostic, and zero
`GQ is no standard basis` warnings.

## Scope firewall

V3 tests only the missing raw-reduction standard-basis premise in the seeded
good-reduction lane, while replaying its V2 controls.  It does not by itself
prove source-component coverage, nonconstancy, the genus obstruction, an
order-four leaf elimination, `(8,12)`, maximum twelve, or JC2.
