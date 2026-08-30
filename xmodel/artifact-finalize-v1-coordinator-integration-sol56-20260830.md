# Systems integration: ARTIFACT-FINALIZE/v1

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `1c665e1f04ca47fc605484777bcfbb4d4e21c619`  
Lifecycle: **ACCEPTED SYSTEMS TOOL / NO MATHEMATICAL CLAIM**

## 0. Disposition

`ARTIFACT-FINALIZE/v1` is accepted for new locally authored campaign reports.
It replaces the error-prone convention “write a canonical path, announce a
hash, then stop editing” with an explicit transaction:

```text
begin -> write private partial -> close -> finalize -> verify.
```

The immediate failure mode was real: a running author announced hashes and
then continued strengthening and resealing the same report. Root's independent
pre-commit replay caught that instance, but downstream review could have
charged moving bytes. The new transaction makes ownership, the stable source
snapshot, publication, and release machine-checkable.

Accepted implementation:

```text
c62f35f15f56425f7ec06546e53156ea8afc6616ef5a146c0f8e15343fb12670
  ops/artifact_finalize.py

5256a36d08d416e14056f4db240df32f0be73419643d84e54b59cb0bddd85a79
  ops/test_artifact_finalize.py
```

The implementing agent's independent adversarial subreview reported no
blocker. The coordinator then read all 1,691 implementation/test lines,
checked the two hashes above, byte-compiled both modules, and reran the full
operations suite:

```text
ordinary Python: 65/65 PASS
python -O:       65/65 PASS
python -OO:      65/65 PASS
```

The focused finalizer suite contributes 15 temporary-directory tests and the
pre-existing seal suite contributes 13 tests. No campaign mathematics depends
on this acceptance.

## 1. Transaction and guarantees

`begin` takes one explicit final path, basis commit, and owner. It performs no
file discovery. An `O_EXCL` lease wins the canonical target, returns a random
capability token and private partial path, rejects occupied final/manifest/
close/release names, and probes same-directory hard-link support.

The author writes only the returned partial. `close` requires that the file
end exactly at the unique standalone `BODY-END` marker, removes write bits,
fsyncs it, and records an exact content hash plus device/inode/mode/size/time
snapshot. Repeated close is idempotent only when the frozen bytes still agree.

`finalize` refuses unsealed drift, delegates the canonical seal bytes to
`ops/seal.py`, and publishes the final report by a no-overwrite hard link. It
publishes a canonical read-only JSON manifest containing full/body hashes,
frozen basis, source custody, owner, and lifecycle times. A separate immutable
release record commits the lease/close/publication hashes before cleanup, so
interruptions after final publication, after manifest publication, or during
cleanup are recoverable by rerunning `finalize` with the same token.

`verify` checks canonical seal bytes, final and manifest hashes, basis, modes,
repeat-read snapshots, and absence of lease/close/release residue. Optional
`--staged` verification additionally requires unique stage-zero Git blobs for
both report and manifest and rereads the files after the index query. Thus a
staged commit can be bound to the bytes that passed verification.

The regression suite covers competing writers, wrong tokens, pre-existing
targets, post-close content drift, post-final content and mode drift,
noncanonical post-seal content, idempotent close/finalize, final-only and
manifest/release interruption recovery, cleanup quarantine, metadata-link
interruptions, and Git-index mismatch.

## 2. Binding campaign use

For a new report authored by a local agent or coordinator:

1. acquire the final path with `begin` before writing;
2. write only the returned partial and do not announce final hashes;
3. call `close`, then `finalize` with the private token;
4. hand off the returned final/body/manifest hashes only after the author is
   idle or completed;
5. have root run `verify`, and before commit run `verify --staged` on the
   explicitly staged report and manifest.

The manifest is tracked alongside the report. The completion handshake in
`COORDINATION.md` remains binding: this transaction prevents accidental
canonical-path drift but does not replace replay, mathematical review, or
root's independent post-author verification.

External `ops/lane.sh` reviews retain their existing immutable prompt,
sandbox, run-receipt, raw-report-hash, and root-sealing custody for now. Do not
silently insert this tool into live adapters. Adapter migration needs a
separate regression packet because the model writes a declared report path
and the lane receipt hashes the raw pre-seal report.

Legacy sealed reports need not be rewritten. Computational artifacts that
have their own atomic/certificate protocol also remain on that protocol until
an explicit adapter is reviewed.

## 3. Limits and nonclaims

The implementation requires POSIX `dir_fd` operations, same-directory hard
links, and successful directory `fsync`. Read-only modes are cooperative
workflow protection, not hostile same-user immutability; a malicious peer can
chmod or replace files, although verification detects ordinary mutation.
Capability tokens supplied on the command line can be visible in process
listings. Hash manifests provide integrity and custody evidence, not
cryptographic authorship.

Git records these files as mode `100644`, so a checkout does not preserve the
working-tree `0444` modes. The production/precommit transaction remains
useful because the manifest and staged-blob checks preserve content identity;
post-checkout seal/manifest verification remains meaningful while the mode
check applies only to the live publication workspace.

This report itself is the first self-hosted positive control: its final file
and manifest are being produced by the accepted transaction, then staged and
verified before commit. No proof theorem, avenue promotion, map,
counterexample, or JC2 conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5932`.
- Body SHA-256:
  `f6aae71f54895281f2611ed7fa22329e551a973fc4f16292b15060c9f1354ccc`.
- Frozen basis: `1c665e1f04ca47fc605484777bcfbb4d4e21c619`.
