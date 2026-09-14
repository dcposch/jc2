# F10 mixed preflight diagnostics correction — Sol

Status: **STATIC DERIVATIVE COMPLETE / UNEXECUTED / UNREVIEWED**

First action `2026-09-13T08:17:58.828764848Z`; original reserve `08:23Z`, hard stop `08:25Z`.

## Result

The owned derivative preserves the prior guards, three causal negatives, multiplicity correction, observer pin, bounds, no-overwrite output and fsyncs. It adds only the selected diagnostic/path changes:

1. Canonical `/etc/python3.12/sitecustomize.py` is the sole non-`/usr`/`/lib` exception. Before returning its identity, the source requires the exact TASK-supplied SHA `43d81125...be138b1e`, a regular file, and uid/gid 0 with no group/other write bit for `/`, `/etc`, `/etc/python3.12`, and the file. All other non-system canonical paths still fail, now naming the path.
2. `IDENTITY_BEGIN` is JSON-emitted, flushed and stdout-fsynced before each identity validation/hash; `IDENTITY_COMPLETE` with canonical path, decimal byte count and SHA is emitted only after completion. Thus a later failure preserves the offending path and completed identities without adding a logger or checkpoint file.
3. Immediately after the selected imports, a durable `DEPENDENCY_METADATA` JSON event records Python, Sympy, ground backend/dtypes, distribution version and METADATA SHA before package, loaded-module or mapping inventories.

Static diff inspection found no additional concrete blocker in the selected scope. A failure during `resolve(strict=True)` necessarily precedes the canonical-path event because no canonical path then exists; the exception will still name the unresolved input. Stdout growth remains governed by the existing regular bounded parent stream, but per-identity events increase it and must fit that external bound. An `IDENTITY_BEGIN` is progress evidence, not a completed or accepted identity.

No local source execution, import, parsing, syntax check, test, or AWS action occurred. The exception path/SHA/ownership facts are ROOT-supplied documentary metadata and remain future-worker runtime predicates. This derivative does not establish a successful preflight, dependency closure, performance, worker qualification, or science result, and grants no retry or execution authority. Different-model ROOT source review remains mandatory.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2299`.
- Body SHA-256:
  `feafb3b4067dc8ad8d9d4befdeba52f3f041b5e75672b7ef6baeeb01964e2a37`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
