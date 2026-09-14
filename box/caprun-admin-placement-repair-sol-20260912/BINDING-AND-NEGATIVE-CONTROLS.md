# Disabled binding and negative-control contract

These two derivatives are administrative SOURCE changes. They remain disabled until every `JC2_*_PLACEHOLDER` is replaced, the complete resulting bytes and manifests are pinned, and a different model accepts them. They do not select a worker, batch, path, clock, or release.

## Exact five-role binding

For each row, ROOT first binds the charged template's placeholders to the already frozen early constants, then hashes the resulting program bytes. The resulting bound hash—not the charged unbound-template pin—is used everywhere below.

| Role | bound stage name | installed path |
|---|---|---|
| admission | `outer-admission.sh` | `<admin-tree>/outer-admission.sh` |
| observer | `observe-and-leaves.sh` | `<admin-tree>/observe-and-leaves.sh` |
| receiver | `receive.sh` | `<admin-tree>/receive.sh` |
| release check | `release-check.sh` | `<admin-tree>/release-check.sh` |
| FIFO writer | `fifo-write.sh` | `<admin-tree>/fifo-write.sh` |

`ADMIN-PROGRAMS-STAGE.sha256` is exactly five LF-terminated rows in table order, each `BOUND_SHA256__two_spaces__stage-name`. `ADMIN-PROGRAMS-INSTALLED.sha256` is the same five hashes and order with the exact absolute installed paths. Their exact file hashes bind `JC2_ADMIN_STAGE_MANIFEST_SHA_PLACEHOLDER` and `JC2_ADMIN_INSTALLED_MANIFEST_SHA_PLACEHOLDER`. The setup derivative checks both exact text and file hash, checks the stage bytes, installs each named role explicitly, then checks the installed manifest.

The corrected eight-row remote preholder manifest and frozen configuration must use the same five installed paths and bound hashes. Its holder path/hash and installed/native data rows remain unchanged. The five programs stay outside the science base and outside every science/source/native inventory; `PRE-ADMISSION-STAGE.sha256`, `PRE-ADMISSION-INSTALLED.sha256`, source contract, science files, holder `0444`, and data-manifest `0444` roles retain their prior meaning.

The external admin tree is one direct child of `/opt`, distinct from and neither ancestor nor descendant of the science base. `/` and `/opt` are canonical, root-owned, and not group/world writable. The tree is root:root `0755`, contains exactly the five regular non-symlink files above at root:root `0555`, and has no other entry or subtree.

## FIFO binding

Setup creates only `<channel>/release.fifo`, verifies the exact one-child census/type/mode, and emits `FIFO_CREATED_ACTUAL device inode uid gid mode path`. While still preholder, ROOT freezes that observed positive device/inode into a fully bound preholder-security derivative. Security must match those expected values, the canonical path, root:root `0600`, non-symlink FIFO type, and the exact channel census before holder admission. The channel stays root:root `0700`.

The existing observer, release check, and FIFO writer check path/type/mode but do not compare this device/inode. This derivative therefore relies on the already required exclusive ROOT/no-concurrent-writer/no-replacement custody from security completion through release. Repeated mechanical identity checks in later phases remain an explicit GAP requiring separately selected edits to those helpers; they are outside this two-file authorization.

## Negative controls

Binding or qualification must stop on any unresolved placeholder; wrong authorization phrase; changed host/namespace/deadline; existing or symlink target; admin tree outside a single `/opt` child, equal to, inside, or containing the science base; unsafe ancestry; extra/missing/nonregular admin entry; wrong owner/mode/hash/path/manifest row; use of an unbound template hash as a bound-program hash; registration already present; worker cgroup already present; extra channel child/subtree; wrong FIFO type/link/owner/mode/device/inode; or any changed original science/runtime/native/holder guard.

No nine authority output is preinstalled. Neither derivative starts the holder, launches a worker, writes the FIFO, installs final registration, alters caps/phases, or authorizes release.
