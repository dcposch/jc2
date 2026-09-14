# Corrected-flow administrative placement delta — Sol

- First action: `2026-09-12T06:40:28.933997979Z`.
- Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
- Lifecycle: source-static, unreviewed, unbound, unexecuted.

## Status

**MISMATCH_CONFIRMED; bounded constants-only placement repair required.** This is an inert source-static finding, not launch authority. No host, paths, batch, or clocks are selected.

## Literal trace

The retained setup creates the science base and its `admin` child as root:root `0755`, installs all regular files there root:root `0444`, and installs only `holder.py` in `admin`. It creates one channel object, `release.fifo`, root:root `0600` beneath a root:root `0700` channel. It neither installs nor qualifies the corrected admission, observer, receiver, release-check, or FIFO-writer programs.

The retained security check requires every directory recursively below the science base to be exactly root:root `0755` and every regular file exactly root:root `0444`, with no symlinks. Corrected FLOW directly places `remote.admission`, `remote.observe`, `remote.receiver`, and `remote.release_check` as the first remote argv word. The charged Fable review records that release-check in turn directly executes the fixed FIFO writer. Consequently these five shell roles require execute permission. Putting them at `0555` inside the base fails the unchanged recursive guard; putting them there at `0444` fails direct execution. `holder.py` is not this problem: it is interpreter-opened and may remain `0444`. The installed/native manifests are data and may remain `0444`. The staged final installer is explicitly invoked through `/bin/bash`.

The remote fixed-role census is exactly eight: five executable programs (`admission`, `observe`, `receiver`, `release_check`, `fifo_writer`) plus `holder`, installed manifest, and native list. Their manifest digests and eventual physical paths must agree exactly with the frozen configuration; source-static membership is not evidence that any physical copy exists.

## Minimal constants-only resolution

A separate, batch-specific immutable administrative tree outside the science base resolves the mode conflict without changing the science inventory, recursive base guard, or phase authority. Before holder start, a reviewed setup derivative (or an equivalently reviewed supplemental administrative placement step) must:

1. Bind one absolute canonical admin-tree path; require the target absent and non-symlink; create only root-owned directories at `0755`. Qualify every ancestor through `/opt` (or the selected root) as canonical, root-owned, and not group/world writable.
2. Install exactly the five fixed program bytes as root:root `0555`, with no symlinks and no extra directory entries. Match each physical path and SHA-256 to the frozen eight-role remote manifest/configuration. Freeze and hash-read back before admission.
3. Extend the preholder qualification, without weakening its existing base checks, to require the admin tree's exact directory/file census, root ownership, `0755`/`0555` modes, canonical ancestry, no symlinks, and exact manifest hashes. Recheck unchanged identity/hashes at every phase's existing fixed-file check.

If the two retained templates are the complete deployment path, these setup and security derivatives are mandatory administrative source edits. No FLOW, caller, binder, stage, installer, dispatcher, science source, cap, predicate, or authority edit is required. Allowing `0555` exceptions inside the science base would weaken/change the existing guard and is rejected. Rewriting every invocation through an interpreter would be broader and would still leave installation/qualification absent.

## FIFO inventory and qualification

There is exactly one FIFO: `<channel>/release.fifo`; receiver transport is stdin, not another FIFO. The constants-only qualification must bind one canonical root:root `0700` channel and one canonical, non-symlink FIFO child root:root `0600`; require the channel's immediate-child census to be exactly `{release.fifo}` and record its device/inode after creation. The same path/identity must bind holder, observer, release-check, and FIFO writer, with no replacement and no concurrent writer through the separately authorized release. Nothing is prewritten. The retained scripts check type/mode/ownership but do not establish the full child census and stable object identity, so that check belongs in the setup/security derivative.

## Controls, scope, and verdict

No worker, physical path, old clock, or enabling value was invented. No program was run, parsed, imported, compiled, or tested. Whole reads covered the two newly charged templates and the corrected contract/config/FLOW/manifests; the exact-current Fable report, intake, and COORDINATION whole reads were reused. All input hashes were unchanged at post-pin.

One exploratory text lookup inadvertently named three uncharged administrative sources and returned matching role lines. No whole read or executable action was performed, and no finding here depends on that output: the charged FLOW and Fable review independently establish the invocation facts. No further uncharged input was accessed.

Verdict: **GAP until the external admin-tree placement and qualification are concretely reviewed and bound.** Static source compatibility is established only under the requirements above; it is not physical deployment evidence or release authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5484`.
- Body SHA-256:
  `d4e7fb66c5e76813afe21941422f08b6fb5cd658e0c88dd943ec4611ecf529fc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
