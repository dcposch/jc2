# Preregistration: K00 V27 R2 exact `B+I3(A)` recursion

Date: 2026-08-27

Lifecycle before launch: **FROZEN DESIGN / UNRUN / SPECULATIVE ROLLBACK TAG
ON UNREVIEWED BASE4 R1 / NOT EVIDENCE**.

## Purpose and dependency discipline

BASE4 R1 producer endpoint `f886f17c...` reports, without independent review,
that

```text
B + I5(A) + I4(A) = B + I5(A)
```

and that this proper ideal has affine dimension three.  Its producer report
is frozen at `19c87955...` and its review packet at `41d11075...`.

R2 consumes that result **only to schedule the next cheap recursion**.  The
new runner independently rebuilds `A`, `B`, `I5(A)`, and `I4(A)`, recomputes
the BASE4 equality and dimension, and then decides

```text
J2base = B + I5(A) + I4(A) + I3(A).
```

By determinantal containment this is equivalently `B+I3(A)`.  No R1 prose
claim substitutes for the fresh exact checks.  Nevertheless every R2 artifact
remains rollback-tagged until R1 and R2 each receive independent hostile
review.

- If `J2base=(1)`, no rank-`<=2` geometric point survives in the provisional
  rank-`<=3` base scheme, so that scheme is rank-pure of rank exactly three,
  subject to both reviews.
- If `J2base` is proper, rank-`<=2` survives.  If all `I3(A)` generators
  already lie in the freshly rechecked BASE4 ideal, record equality and stop;
  no `I2(A)` job may launch until this endpoint has its own frozen producer
  report, source, evidence, and review packet.
- A cap, warning, source mismatch, missing byte, or failed replay is no
  verdict.

## Frozen inputs

R2 pins the V26 atlas/compiler/result, V26R1F producer and hostile review,
V24R6R1 audits, V27 design, all R1 source/replay/report bytes, and this
preregistration.  Load-bearing new R1 pins are:

```text
7ffc61ba3aa1286205f3fc6e9f8b77792e3eff6f6790d91b737beb8d0f18d060  R1 source freeze
f886f17ca2c626ec476e695418002185d2223d556721759900f6cdbe89635073  R1 endpoint
3e7fac6cd993c8afa581fa037d6f69df757a6a8db08ccdeda6c5770d1d7e8d9c  R1 AWS evidence manifest
279bdc80febfe7a309bcd279f30caeb25d58e74476aa7bcf62dd13557bbbe2f4  R1 portable harvest
19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c  R1 producer report
41d1107589f33b7f7fab4ec5cac6e47ffc72368dfeeb93981ae2e921a9eb0205  R1 review packet
```

The full literal rank-three label set has 1,225 row/column subsets.  Frozen
V26 comparison telemetry says 412 determinants are zero and 813 are nonzero,
with 725 distinct nonzero exact polynomials.  R2 recomputes `minor(A,3)` from
`A`; frozen census bytes are comparison controls only.

## Exact replay and mutations

1. Refuse non-EC2 Linux and malformed/unregistered lane tags; verify the
   immutable archive, source-freeze hash, every source entry, and endpoint
   metadata before algebra.
2. Retain every rank-3/4/5/6 row/column source label.  Recompute the stored
   nonzero censuses `813/594/90/0` and the combinatorial totals
   `1225/1225/441/49`.
3. Freshly prove `B+I5(A)` proper of dimension three, reduce every `I4(A)`
   generator to zero against its fresh standard basis, and require the rebuilt
   `B+I5(A)+I4(A)` ideal proper of dimension three.
4. Decide `J2base` by exact `slimgb`.  A unit endpoint gets a serialized
   Bezout coefficient vector and second-process entrywise replay.  A proper
   endpoint gets `Graw,T`, entrywise `matrix(J2base)T=matrix(Graw)`, fresh
   `std(Graw)`, and reverse reductions of every literal generator of `B`,
   `I5(A)`, `I4(A)`, and `I3(A)`.
5. Delete the first nonzero `I3(A)` stored entry; delete and add a nonzero
   certificate/transform coefficient; force a unit by adjoining `1`; preserve
   `(d0_1)` as a proper control; and require omission of `I3(A)` to recover
   the freshly rebuilt proper BASE4 ideal.
6. Fail closed on caps, empty required output, nonempty Singular stderr,
   diagnostics/warnings, nonzero swap, missing telemetry, or any replay/hash
   mismatch.

The `b`-sign, restored `k6_0`, and MAX5CLASS representative mutations remain
out of scope because this recursion consumes only `A` and `B`.

## AWS envelope

Use idle AWS r6a only after a fresh process/memory/swap audit.  One process at
nice level 5; outer wall cap 21,600 seconds; per-Singular cap 21,000 seconds;
virtual-memory cap 402,653,184 KiB; required swap count zero.  Do not touch
Box02 R2/R5 or any other lane.

## Allowed outcomes

```text
PASS_V27_R2_EXACT_RANK3_PURE_PRODUCER_UNREVIEWED_ROLLBACK_R1
PASS_V27_R2_EXACT_RANK_LE2_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1
RESOURCE_CAP_NO_VERDICT
DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE
```

## Firewall

R2 decides only the intrinsic six-variable rank filtration.  It asserts no
rational point, full-`P6` point, grade-seven compatibility, rank-five chart,
later grade, jet, arc, source reachability, closure incidence, counterexample,
or JC2 result.
