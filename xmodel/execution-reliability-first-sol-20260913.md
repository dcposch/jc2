# Execution reliability pilot — different-model STATIC FIRST

Task: `execution-reliability-first-sol-20260913`  
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`  
First action: `2026-09-13T04:46:32.203038883Z`

## Overall verdict

**REFUTED as ready for the proposed AWS regression.** The one-service design removes the prior model-roundtrip timing interface and most core controls are coherent, but one evidence-custody race is load-bearing and currently untested. Two further runtime predicates and several negative controls remain GAP. These findings do not authorize a patch, regression, worker, or migration.

This is a trusted, root-prepared job pilot, not a hostile-code sandbox. `MemoryMax` and `CPUQuota` are cgroup-wide configured controls; CPU is a rate, not total CPU time. `LimitFSIZE` is per file. There is no aggregate output/disk quota, and the documentation already disclaims one.

## Load-bearing claims

### 1. Terminal collection / immutable evidence — REFUTED

`start()` redirects both streams through asynchronous process substitutions (`job.sh:102`). Those `tee` children belong to the caller/driver cgroup, not `jc2-job-TAG.service`; their PIDs are neither retained nor waited. Bash completion of the `start` shell does not establish that process-substitution children have drained and exited. A fast job can therefore be inactive with its service cgroup absent while an admission `tee` still holds and writes `admission.stdout` or `admission.stderr`.

`collect()` tests only service state/cgroup absence (`51-55,243-249`) and then archives the directory. Its collector lock serializes collectors, not admission writers. Thus the claimed `writers/unit/cgroup terminal` precondition is false: a tar may capture a prefix while a late tee append remains outside the published archive. The regression driver has analogous tees, but its outer bounded service can cover them; that does not cure each child job's collection race.

**Smallest correction:** remove the admission process substitutions; use direct append files, and hold a per-job admission lock from redirection through the last `start` write. `collect` must acquire that same lock nonblocking (otherwise STOP as admission still live) before its terminal test and retain it through archive publication. If console mirroring is required, it must be synchronous or its exact PIDs must be closed and waited before releasing the lock. Add a fast-terminal/concurrent-collect negative control that proves refusal until the admission writer is gone and exact log bytes are stable.

### 2. Identity, host and no-overwrite admission — CONDITIONAL STATIC CONFIRMED

The Linux/Amazon DMI, exact 17-hex instance, explicit HQ deny, board-asset equality, tag grammar, cgroup-v2, absent directory/unit/cgroup, and saved-instance checks are literal (`18-27,39-54,89-101`). Manifest keys/types/counts, unique phase names, bounded argv strings, NUL rejection, registered `@payload/` substitution, array execution, and post-copy hashes avoid eval and ordinary shell interpolation (`63-88,106-118,187-201`). Duplicate tags cannot overwrite prior evidence.

The intended pilot's external plan requires the runner, bundle and payloads to be root-owned `0444` under a root-owned stage and compares pins. The runner itself checks neither bundle/file ownership nor immutable ancestry, and accepts its own `$0` without an expected runner digest before installing the copy later used by the privileged `+` post-stop hook. For the trusted pilot this is a **GAP to be discharged by exact installed-path qualification**; absent that external fact, the report's “pinned root-owned bundle” is not source-enforced. A hostile or mutable source path is out of scope and unsafe.

### 3. Privilege drop and post-stop receipt — GAP pending actual qualification

Systemd is asked to create the main service directly as `nobody:nogroup`, with empty capability/ambient sets and NNP; `_run` rejects an effective UID other than 65534 and checks `CapEff=0` and `NoNewPrivs=1` before payload (`129-147,159-185`). The root-only `_finish` is a narrow, fixed-argv `+` hook and writes the manager-provided result atomically (`218-231`). With a physically immutable runner this is a coherent authority split.

However `_run` does not verify the four real/effective/saved/fs UID and GID values, and it records `/proc/PID/limits` without checking the requested FSIZE. `manager_state` also omits `LimitFSIZE`. Before runtime acceptance, compare exact UID/GID vectors and the padded `Max file size` soft/hard values against `file_mib*1048576`, and record the manager property. Actual `+` behavior, hook receipt, NNP/capability state and worker systemd semantics remain UNRUN.

### 4. Sequential phases, descendants, deadlines and failures — CONDITIONAL STATIC CONFIRMED

Each argv executes as one array; actual wait status and start/end files are flushed before comparison. Unexpected exit blocks the successor, and a successful phase must leave only the controller in `cgroup.procs` (`187-216`). Runtime, memory, swap, CPU-rate, tasks, control-group kill, no restart and five-second stop settings are all placed on the one service (`129-147`). The post-stop receipt plus absent-cgroup collection criterion correctly avoids interpreting missing phase exits or killed controllers as success. These are sound source intentions, not kernel/runtime facts; external absolute retirement and retained EBS remain mandatory.

### 5. Regression's positive paths — CONDITIONAL; refusals — REFUTED as exact controls

The success, unexpected-17, exec-127, timeout/TERM-ignore/new-session, controller-KILL, partial-evidence and repeat-archive checks inspect meaningful outcome artifacts. Yet `refusal()` accepts every nonzero status and never authenticates the intended error (`job-regression.sh:59-68`). Consequently bad-pin, bad-path, wrong-instance, HQ and symlink cases can PASS after an unrelated early failure. Require the exact corresponding `JC2-JOB ERROR:` line for each case, preserve the captured exit, and verify the expected directory/unit side effects. Also add a registered expected-nonzero phase followed by a successor if nonzero `expected_exit` remains a supported mechanism; current tests exercise only unexpected nonzero exits. A manifest review—not this runner—must still prevent a scientific failure code from being declared expected.

## Disposition

The architecture is promising but remains `RUNTIME-UNTESTED` and must not run its proposed pilot until the admission-writer/collection race is corrected and independently reviewed. Exact source installation, full credentials/FSIZE, refusal causality, actual cgroup limits/descendant cleanup, interrupted collection, systemd post-stop behavior, external deadline/retirement and archive transfer all remain runtime obligations. No automatic migration to scientific clients follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6910`.
- Body SHA-256:
  `b1ccf1f37f0698ce938a85d9ffcbae7241a95b20ce1c101270e24c747bcbe1f0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
