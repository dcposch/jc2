# F10 mixed preflight path-order correction — Sol

Status: **STATIC MINIMAL DELTA COMPLETE / UNEXECUTED / UNREVIEWED**

First action `2026-09-13T08:27:06.322153762Z`; original reserve `08:33Z`, hard stop `08:35Z`.

The new derivative makes only the requested ordering correction inside `identity()`:

- After canonical resolution and durable `IDENTITY_BEGIN`, an ordinary path must be below `/usr` or `/lib` before `stat`, open, or hashing.
- The sole exact `/etc/python3.12/sitecustomize.py` exception must pass regular-file and root-owned, non-group/other-writable ancestry checks before open or hashing. Its exact pinned SHA remains checked immediately after hashing.
- Size validation precedes open; `IDENTITY_COMPLETE` remains after all applicable admission, size, hashing, and special-SHA checks.

This restores the predecessor read boundary: an arbitrary resolved unadmitted path is named and rejected without a file metadata read beyond resolution and without opening or hashing it. The exact exception necessarily receives its selected metadata checks before its content read. Static whole-diff inspection found no other changed behavior or concrete blocker in this narrow correction.

All imports, guards, causal negative controls, progress/metadata events, pins, limits, output semantics and fsyncs remain otherwise byte-identical. No source was parsed, imported, syntax-checked, tested, or executed; no AWS action occurred. The artifact is inert and grants no worker, retry, preflight, observer, or scientific authority. ROOT different-model review remains mandatory.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `1601`.
- Body SHA-256:
  `b95b2952de08ca958b9dd4c972727517748bfac5abb4589dbfac6fdf08ffc95b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
