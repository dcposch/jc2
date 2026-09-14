# F10 mixed one-client procedure integration gate

Status: **CONDITIONAL STATIC CONFIRMED**. The consolidated procedure is a coherent, disabled one-client plan; it is not an allocation, qualification pass, enabled registration, runtime result, or launch authority.

First action: `2026-09-13T00:53:36.815772862Z`. All charged pins matched before use. The procedure, its manifest, disabled registration, authority, and dispatcher were read WHOLE; the already reviewed PREPARE and UNIT bodies were reused only after exact repinning.

## Integration findings

- Physical and time binding is ordered correctly. The worker/volume/network identity, boot/host/namespaces, canonical executables, UID/GID, native metadata, qualification receipt, and fresh clocks remain unknown until observed. Templates are bound, hashed, whole-read, transferred, and compared before use. Missed admissions and failed predicates STOP; neither clock nor allocation is recycled.
- The disabled registration has exactly the sixteen top-level fields required by the pinned dispatcher: `schema`, `enabled`, `job`, `worker`, `boot_id`, `hostname`, `not_before`, `deadline`, `uid`, `gid`, `paths`, `pins`, `native_manifest`, `library_paths`, `qualification`, and `caps`. The procedure distinguishes string bindings from the two integer identity fields, preserves fixed cap values and all unchanged nested fields, requires `enabled=true` only after qualification, then canonicalizes and independently compares the complete record.
- Initial filesystem state matches dispatcher admission: the science tmpfs mount is absent before the unit; once created, it has exactly empty `admin` and `output` siblings with the required ownership/modes. Registration, logs, and timer evidence stay outside those siblings. The copied native file projection and qualification receipt are root-owned mode 0444 beneath root-owned 0755 nonwritable ancestry, so the dropped workload can traverse and read them without exposing the assembler's 0700 directory.
- Exactly one separately bound dummy is required. Its original 25-second admission-through-cleanup envelope, whole cgroup CPU/memory/swap/task controls, AS/FSIZE limits, separate 256 MiB tmpfs, exact identity/rlimit/capability evidence, bounded streams, wait 125, TERM/KILL behavior, reaping, and final cgroup absence are all acceptance predicates rather than assumed facts.
- The science run preserves one cgroup, 80% CPU at 100 ms with zero burst, 32 GiB memory/AS, swap zero, Tasks64, 256 MiB FSIZE and shared tmpfs, and a 3540-second original wall including cleanup. The six fixed dispatcher phases and exact semantic controls are unchanged; failed controls, generic gcd failure, exceptions, time/cap failure, or incomplete cleanup remain nondecisions.
- Native and qualification evidence is described truthfully. ROOT must compare complete maps, byte counts, hashes, actual exits, package/import facts, live unit controls, and terminal cgroups before authoring the bounded qualification receipt. The receipt status is only `METADATA_AND_DUMMY_CHECKED`; pinning it supplies ROOT attestation, not a native-completeness, no-escape, API-semantic, scientific, F10, or JC2 theorem.
- Durable custody is explicit-path and outcome-independent: after stopping writers and proving terminal units/cgroups, the finite source/meta/prep/runtime/science and conditionally existing tmpfs/dummy paths are archived to the retained EBS, flushed, hashed, copied to a fresh HQ custody location, and checked by SHA plus a second whole-byte stream. Transfer failure remains incomplete custody with the nondeleted EBS as recovery; only the registered returned instance may be terminated, termination must reach `terminated`, and volume retention plus both campaign selectors are rechecked.
- Retirement ownership is finite. An exact-ID HQ timer is armed promptly after allocation; it remains authoritative until an actually live, registered science unit has a separately armed deadline-plus-five-minute retirement. Failed qualification keeps the original retirement. No broad selector termination, old host fact, retry, or larger cap is admitted.

## Runtime obligations still open

ROOT still must perform and retain the fresh allocation/quota/AMI/network/EBS checks; bind original qualification and science clocks; qualify cloud-init and all physical host/native/import facts; install and compare exact bytes; observe live metadata, dummy, and science identities and cgroups; verify every exit, stream, receipt, census, bound, deadline, and cleanup predicate; create the truthful qualification receipt and enabled registration; complete explicit archive transfer; terminate the exact worker; and verify retained EBS and fleet selectors. Any failure is STOP/nondecision.

The punctuation in the prose executable list (`/usr/bin/setpriv,/usr/bin/jq`) is contextually unambiguous and does not alter the separately named exact paths or bindings; no source reauthor is required. No blocking source/procedure mismatch was found in the charged integration scope.

No source or shared ledger was edited or executed. No AWS, worker, systemd job, setpriv, interpreter, import, AST, syntax, test, CAS, dummy, or scientific action occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5236`.
- Body SHA-256:
  `56c05fd0051945733d193cf204b21cf9783434bd1bb88fa8f6d38d6f9f74275f`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
