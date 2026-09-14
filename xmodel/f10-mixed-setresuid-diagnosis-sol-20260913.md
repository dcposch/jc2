# F10 mixed setresuid failure diagnosis

Status: **NARROW CAUSE CONFIRMED; DEEPER ORIGIN UNOBSERVED**. Diagnosis only—no implementation, test, service, worker, retry, or scientific authority.

First action: `2026-09-13T01:54:59.161785333Z`. All three local inputs matched before use. `COMMANDS.md` was read WHOLE; the pinned CAPRUN launch/preexec sections were read selectively. Primary util-linux 2.39.3, libcap-ng 0.8.4, and Linux capability/setresuid documentation were inspected at the URLs recorded in PINS.

## What is definite

The exact util-linux 2.39.3 source maps `setpriv: setresuid failed: Operation not permitted` to its direct `setresuid(ruid,euid,euid)` call. Earlier failures have different messages: setting no-new-privileges, `PR_SET_KEEPCAPS`, and the first `capng_apply(CAPNG_SELECT_CAPS)` would respectively report their own errors. The later `setresgid` and `setgroups` calls were not reached. Thus the source-level failing operation is the UID change returning `EPERM`; the observed exit 127 is setpriv's privilege-error exit.

The command requests UID/GID 65534 from a root/root service. Linux documents `CAP_SETUID` as the capability for arbitrary UID changes and `setresuid(2)` documents `EPERM` when the caller lacks the necessary capability in its user namespace. The unit's `CapabilityBoundingSet` containing `CAP_SETUID` proves only the ceiling, not that the short-lived setpriv process actually had it in its effective/permitted sets. No live CapEff/CapPrm snapshot or syscall/audit trace was captured. The empty kernel-journal window is not proof against an unlogged LSM/seccomp denial. Therefore the immediate failure is confirmed, while the mechanism that removed/denied effective `CAP_SETUID` remains unobserved.

CAPRUN does not alter credentials or capability sets: its preexec function changes only RLIMIT_CPU, and `Popen` adds a new session before executing the supplied setpriv argv. V5's normal-exit-127 telemetry, zero probe output, exact 51-byte setpriv stderr, and absent later PID/PGID/cgroup are consistent with failure before probe execution; they do not demonstrate RSS/TERM/KILL behavior.

## CAP_SETPCAP hypothesis — refuted

This util-linux version does **not** use `capng_change_id` for these flags. It calls `PR_SET_KEEPCAPS`, opportunistically calls `bump_cap` for SETPCAP/SETUID/SETGID only when each is already permitted, applies the cap state, then directly calls `setresuid`. The command requests no setpriv bounding-set, inheritable-capability, ambient-capability, or securebits mutation. The libcap-ng `capng_change_id` caveat about CAP_SETPCAP belongs to a different API path. Adding CAP_SETPCAP does not satisfy the kernel's CAP_SETUID check and would broaden privilege without primary-source support as the repair.

## Minimal proposed delta

Prefer eliminating the nested privileged transition for this dummy: run the transient service itself as the already registered UID/GID 65534 (`User=`, `Group=`, empty supplementary groups), retain `NoNewPrivileges=yes`, use an empty capability bounding/ambient set, and make CAPRUN's child argv begin directly with the pinned Python/probe command. The output directory is already owned by 65534 and CAPRUN needs no root operation to supervise and signal its same-UID process group. This requires recomputing the registered child argv count/hash and changing the telemetry executable expectation from setpriv to Python; every cap, timer, cgroup, tmpfs, output, and semantic predicate otherwise stays fixed.

If ROOT instead retains nested setpriv, the minimal proven prerequisite is not CAP_SETPCAP: it must establish and capture CAP_SETUID and CAP_SETGID in setpriv's permitted/effective sets at exec and show the relevant syscalls are not denied. Granting ambient SETUID/SETGID is one possible systemd mechanism, but it exposes those privileges to CAPRUN and is not endorsed without a fresh source/security review. No retry is authorized by this diagnosis.

Primary references: [util-linux v2.39.3 setpriv source](https://raw.githubusercontent.com/util-linux/util-linux/v2.39.3/sys-utils/setpriv.c), [libcap-ng source](https://raw.githubusercontent.com/stevegrubb/libcap-ng/v0.8.4/src/cap-ng.c), [Linux capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html), and [setresuid(2)](https://man7.org/linux/man-pages/man2/setresuid.2.html).

No source, command, shared ledger, or runtime state was changed. No local privilege/dummy/service/scientific execution, AWS/SSH action, or protected-tree inspection occurred.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4563`.
- Body SHA-256:
  `c67b941aaa24285718a0b1a5da638704902fddd04c57f5843fecb84f0dafcb71`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
