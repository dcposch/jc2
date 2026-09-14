# f10 mixed DAC correction: different-model static FIRST

Status: **CONDITIONALLY STATIC CONFIRMED**. This is an unexecuted source finding, not a host or runtime pass.

First action: `2026-09-13T00:08:54.964129538Z`. Every charged SHA-256 matched before body use. The exact scope is recorded in `PINS.json`; CAPRUN review was limited to its named cleanup, CPU-limit, output-open, cwd, and spawn ranges.

## Four requested determinations

1. **Diagnosis — CONFIRMED.** The dummy output directory is created for the positive child UID/GID at mode 0700. CAPRUN remains a root-side supervisor when it validates the cwd, opens/truncates its stdout, stderr, and telemetry paths, and arranges the child cwd before executing `setpriv`. UID 0 is not by itself a substitute for a retained DAC-bypass capability. With the old bounding set excluding `CAP_DAC_OVERRIDE`, those root-side accesses through a child-owned 0700 directory are not supported by the stated capability policy. The same class of issue applies when the root dispatcher must read child-owned mode-0600 candidate/receipt bytes.

2. **Minimal delta — CONFIRMED for this dummy command source.** The complete old/new diff has exactly two hunks: the nonexecuting title changes, and `CAP_DAC_OVERRIDE` is added to the root service's `CapabilityBoundingSet`. Nothing else changes. `CAP_DAC_OVERRIDE` is the narrowly relevant Linux capability for bypassing file read/write and directory traversal DAC checks; no `CAP_SYS_ADMIN`, `CAP_SYS_PTRACE`, `CAP_FOWNER`, or `CAP_SETPCAP` is needed for this diagnosed access. It does not bypass unrelated LSM, mount, immutable-file, namespace, or path-custody controls.

3. **Capability drop — CONDITIONALLY CONFIRMED.** The added capability belongs to the root systemd/CAPRUN supervisor. The unchanged child argv still crosses `setpriv --reuid=POSITIVE --regid=POSITIVE --clear-groups --no-new-privs`, has an empty ambient set, and the probe rejects unless `NoNewPrivs` is `1` and `CapEff` is exactly sixteen zero hex digits. On ordinary Linux credential transition semantics, changing from root to the nonzero identity without a keep-caps request clears effective capabilities. This remains a runtime predicate: ROOT must observe the actual unit capability configuration and the probe's exact zero `CapEff`; source bytes alone do not prove the worker's securebits/LSM/unit behavior.

4. **Preserved caps — CONFIRMED by exact diff.** CPUQuota 80%, 100 ms period, 32 GiB MemoryMax/AS, swap 0, TasksMax 64, 256 MiB FSIZE/tmpfs, RuntimeMaxSec 20, TimeoutStopSec 5, KillMode control-group, Delegate=no, namespace/realtime/control-group restrictions, CAPRUN wall 5, CPU 3, RSS 33,554,432, bounded streams, timer/cleanup predicates, and one-attempt behavior are byte-for-byte unchanged. CAPRUN's selected `cpu_preexec` code sets `(soft, hard)=(cpu_seconds,cpu_seconds+1)`, so the unchanged dummy expectation `3/4` remains exact and is compatible with a separately bounded 3300-second scientific parent hard limit.

## Remaining boundary

The correction closes only the identified dummy supervisor access defect. The future scientific dispatcher service still must be instantiated with the same root-side DAC permission and independently reviewed/observed; no dispatcher source edit is required or proposed here, but no charged unit command proves that future configuration. Actual paths, ownership, service capability sets, child credential transition, LSM/security configuration, native closure, cgroup behavior, and cleanup all remain fresh registered-worker predicates. Any mismatch is STOP.

No source, dummy, interpreter, import, test, CAS, worker, systemd unit, mount, or AWS action was executed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3714`.
- Body SHA-256:
  `cdfddb9be19643cac48750f2adca0f755e8d0cb82c4e6451de6463d08976576b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
