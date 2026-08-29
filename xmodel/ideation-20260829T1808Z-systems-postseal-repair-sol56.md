# Round 1808 systems post-seal repair: anchored BODY-END integrity helper

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `POST-SYNTHESIS SYSTEMS REPAIR / OPT-IN / NO MATHEMATICAL CLIENT`

## Reason for the addendum

The sealed round synthesis recorded `ops/seal.py` and its test file before
the final internal hostile diff review returned. That review found two
commit-blocking custody defects:

1. after an atomic replacement and successful byte verification, failure to
   open the parent directory for `fsync` would be reported as ordinary
   `INVALID`, even though the seal was already installed; and
2. resolving the parent pathname did not anchor it. Every later temp, read,
   replace, verification, and sync operation re-traversed the path, so a
   rename/recreation of the canonical parent could redirect the operation.

The pre-review hashes printed in synthesis Section 5 are therefore
superseded by this report. No sealed mathematical report or claim depended on
the helper, and no lane caller had been migrated.

## Repair

The final implementation opens the resolved parent exactly once with
`O_DIRECTORY` and `O_NOFOLLOW` where available, compares its `fstat` identity
with pre/post path observations, and retains that descriptor for the complete
operation. Target inspection/open/read, unique temp creation, cleanup, and
atomic `os.replace` are all `dir_fd`-relative. The parent pathname identity is
checked again immediately before and after replacement. A pre-replacement
change fails without installing; a post-replacement detachment or directory
`fsync` failure returns typed `DURABILITY_WARNING` after the installed bytes
have verified. There is no second directory open after replacement.

The earlier hardening remains: pre-open nonregular/FIFO refusal,
`O_NONBLOCK`, final-component no-follow plus inode checks, same-inode
content/metadata rewrite detection, post-install exact byte and body-seal
verification, explicit `--expected-basis`/`--expect-basis`, CRLF-normalized
post-body metadata, attributed multi-file failures, mode preservation, and
temporary-file cleanup. A body seal is integrity metadata, not
authentication; full-file hashes and run receipts remain separate.

Final hashes are

```text
7649bcbaf45ceaa8bc8dd6113615db588a5d641af030570384ea8e604c9cbaa1  ops/seal.py
0c160fe6df7ad95d312dd054f2195f8b704a9656957a2cf801e94092b87b6376  ops/test_seal.py
```

## Acceptance

The final suite passes 13/13 under ordinary Python and 13/13 under `python
-O`, plus byte compilation. New deterministic fixtures rename and recreate
the parent between staged reads and confirm that neither the decoy path nor
the anchored original is replaced; they also force directory `fsync` failure
and confirm a typed warning plus a subsequently valid installed seal.
Final internal hostile re-review returns `PASS`: both prior blockers are
closed and all ordinary/optimized fixtures reproduce independently.

The original fixtures continue to cover body mutation, wrong length/hash/
basis, missing and duplicate markers or metadata, inline marker text, CRLF,
symlinks, FIFO refusal without blocking, same-inode rewrites, mode/temp
cleanup, multi-file error attribution, restamp refusal, and optimized
equivalence. The final helper also stamped and verified this addendum through
its own anchored path.

The tool remains opt-in. `ops/lane.sh` is unchanged; no automatic hook, map,
theorem, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3530`.
- Body SHA-256:
  `32c48c828e7ef6c6780b51d1ac121b816a2c080a12a5136a6f117425d31c0ead`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
