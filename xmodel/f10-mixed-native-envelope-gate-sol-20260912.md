# Different-model DELTA FIRST: mixed native envelope

Status: **CONDITIONAL CONFIRMED / SOURCE-ONLY / UNEXECUTED**. First action
`2026-09-12T20:30:16.641490156Z`. This review creates no worker,
registration, authority, native manifest, closure observation, runtime result,
or scalar-unit claim.

## Exact byte-diff result

Whole-file unified comparison of old and new `authority.py` contains exactly
two changed numeric literals:

- `frozen(m['path'], m['sha256'], 262144)` becomes the same call with
  `2097152`;
- `len(native['files']) <= 1500` becomes the same predicate with `8192`.

Whole-file comparison of old and new `dispatch.py` contains exactly one
changed numeric literal:

- its native-manifest `frozen(..., 262144)` call becomes the same call with
  `2097152`.

No whitespace, message, schema, keyset, algorithm, phase, argv, authority,
predicate, mutation, receipt, guard, source pin, per-file cap, scientific wire
cap, or resource-control statement changed in either source. The new source
digests necessarily require fresh installed pins; old pins cannot authenticate
these derivatives.

## Admission and compatibility

The changes are mutually compatible. Dispatcher and scientific authority now
both admit at most 2MiB for the same referenced native-manifest bytes.
Authority retains exact schema/keyset `f10-mixed-native-files/v1` plus `files`,
duplicate-key rejection through `object_pairs_hook`, a dictionary cardinality
check, and per-entry frozen path/SHA verification. The 8,192-entry bound and
2MiB byte bound apply jointly; satisfying either never bypasses the other.

As ROOT-supplied documentary input, 4,286 regular files are below 8,192 and
the 603,538-byte path-plus-70 estimate is below 2MiB. Thus the old numeric
count/estimated-size obstacle is removed prospectively. Neither number is an
actual serialization, closure, future-host observation, or runtime-fit result.
Additional native dependencies can still make the exact file count or encoded
manifest exceed a new bound, which remains STOP rather than grounds for another
automatic enlargement.

This is a metadata-admission policy expansion, not an increase to physical
science limits. The per-native-file read ceiling remains 256MiB; scientific
artifact16MiB, receipt limits, whole-batch3540s wall,80% CPU/burst0,32GiB
memory/AS,256MiB tmpfs/output and CAPRUN limits are byte-identical. More
manifest entries can add hashing time, so installed fit must be newly measured
inside those unchanged bounds.

## No implicit collector qualification

The delta admits only a parsed two-key file-map manifest. It neither parses nor
proves directory inventories, aliases, absences, default startup paths, pyc
state, import reachability, loaded native backends, immutable ancestry, or
completeness. The retained old collector has different nominated roots/raw
grammar and limits; its output is not silently admitted as a matching current
qualification. An arbitrary hash list can fit both numeric bounds and still be
incomplete. A separately reviewed actual-host collector/assembler,
qualification document, exact installed source vector, and pre/post closure
checks remain mandatory.

The accepted algebra and six-phase runtime logic were intentionally not
re-reviewed. Their existing conditional intake boundaries remain unchanged.
No old run, clock, authority, registration, retry, parameter farm or worker is
revived by these source copies.

## Verdict

**CONDITIONAL CONFIRMED** for the exact three-number source delta. It removes
the known 4,286-file documentary admission obstacle while preserving all other
source bytes and physical caps. There is no new source-static incompatibility.
Execution remains blocked pending different-model intake of this report and
fresh actual-host native/import/directory/alias/absence/pyc qualification,
exact serialization/count/size checks, new source hashes in registration and
authorities, installed runtime fit, and all previously required containment,
cleanup, custody and retirement evidence.

## Custody

`box/f10-mixed-native-envelope-gate-sol-20260912/PINS.json` records all ten
inputs. Fresh WHOLE reads covered those inputs; final WHOLE readback covers
PINS, this report and its finalizer manifest. All postpins must match before
the terminal custody write. No interpreter, import, AST, syntax, compile,
test, dummy, CAS, network, AWS, protected tree, mirror, repair or source write
occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4445`.
- Body SHA-256:
  `ee0f2c7d6efa6056c34402ed6465a4379ff9e78bfa900f3c8783b75c1d81e15a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
