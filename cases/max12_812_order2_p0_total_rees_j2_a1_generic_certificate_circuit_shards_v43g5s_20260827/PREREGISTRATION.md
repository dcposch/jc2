# V43G5S preregistration: exact 32-shard subset census

Date: 2026-08-27

This is an additive parallelization successor to immutable V43G5.  It leaves
the original exhaustive `Q(t)` lane and full-pole lane live and unchanged.

Freeze the same ordered eleven-row support and exact `Q(t)` complete-basis
predicate as V43G5.  Partition masks `0..2047` into 32 disjoint contiguous
ranges of 64 masks.  Each shard runs one-core Singular and prints exactly one
Boolean unit marker per assigned mask.  A deterministic exact aggregator must
reject missing, duplicate, out-of-range, non-Boolean, or non-monotone markers;
it accepts only the exact union `0..2047`, with mask 0 nonunit and mask 2047
unit, and serializes the full table plus all inclusion-minimal unit supports.

Pinned predecessor bytes:

```text
95910e9f93bc007029da9bc89a8a443b18dfcac5165c8a3e79744cd6aa9cde62  compile_certificate_circuit_v43g5.py
8e3c995a24bb9d91ae18adfe0cd9fee906112a2e272816cb8225cf7b532249be  run_aws.sh
43d466eed8a2feb80057cbc9ca2b37fb9ec35ec9d50c136ee941a3bfe8039745  PREREGISTRATION.md
7b01bd703c3618b65962bcbe73831d4963112d13a47a73400796dcdbe7e14f10  live V43G5 compiler_result.json
```

No modular or specialized-rho result is evidence.  This shard set decides
only the exact `Q(t)` unit table inside the fixed eleven-row support.  Per
shard cap: one core, 4 GiB RSS, one hour.  Total: 32 cores / 128 GiB on an
already running AWS host.  The original V43G5 jobs are controls and may not be
stopped or mutated by this successor.
