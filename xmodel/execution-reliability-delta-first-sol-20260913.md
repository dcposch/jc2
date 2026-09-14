# Execution reliability correction — STATIC DELTA FIRST

Task: `execution-reliability-delta-first-sol-20260913`  
Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`  
First action: `2026-09-13T05:07:37.681682792Z`

## Verdict

**CONDITIONAL STATIC CONFIRMED for exactly one bounded no-CAS AWS regression.** The complete old/new diffs and all four current sources were read. The prior decisive evidence-custody race and the named source/test gaps are repaired without a new static blocker. This is not a runtime pass, scientific acceptance, hostile-sandbox claim, worker allocation, or migration authority.

## Prior findings

### Admission writer custody — CONFIRMED repaired

`start` creates the no-overwrite job directory, opens `lifecycle.lock`, and takes a nonblocking exclusive flock before publishing the instance or redirecting streams. Admission now uses direct file descriptors—there are no `tee` children—and FD8 remains held through the final manager/log writes and directory sync until process exit. `collect` opens the same lock and must acquire it nonblocking *before* its manager/cgroup terminal test; it holds the descriptor through archive and hash publication. The archive excludes the lock inode.

This closes the exact old race: neither a still-running admission nor another collector can coexist with publication. The root `ExecStopPost` writer is not lock-covered, but it remains inside the target unit; collection additionally requires the unit inactive/failed and its exact cgroup absent, so that writer must already be gone. A collection arriving before `instance` exists can fail `check_existing`, never publish.

The regression removes its own tees and adds a controlled writer on the *same* job lock. It requires exact exit70/refusal while locked, waits for explicit FIFO release and the writer, collects, then compares the archived admission stream byte-for-byte to the final file. This is a meaningful mechanism control, not evidence that a real crash occurred.

### Runner and input authority — CONFIRMED for trusted-root pilot

`start` now accepts the runner digest, requires canonical absolute runner/manifest/payload paths, regular nonsymlink root-owned mode0444 files, and root-owned non-group/other-writable ancestry through `/`. It checks the runner before setup and its installed copy before that copy is used by the privileged fixed-argv `+` hook; manifest and payload copies retain exact digest checks. The test plan supplies explicit installed paths, hashes and ancestry observations.

This is sufficient for the declared trusted-root pilot. It cannot protect against a malicious root, and the source check occurs after Bash has opened the script, so ROOT's required immutable installation and prelaunch pin check remain load-bearing rather than optional.

### Credential and FSIZE predicates — CONFIRMED source-static

Before phase one, `_run` requires all four UID values and all four GID values to equal65534, `CapEff=0`, `NoNewPrivs=1`, exact cgroup path, and exact memory/swap/CPU-rate/task controls. Its tokenized single-row `/proc/PID/limits` check requires both FSIZE values to equal `file_mib*1048576` and unit `bytes`, so Linux column padding is harmless. Manager evidence now includes `LimitFSIZE`, `User`, and `Group`. Actual worker values and systemd property behavior remain runtime observations.

### Refusal causality and exit semantics — CONFIRMED source-static

The refusal helper now records the numeric exit, requires70, selects the correct caller or durable admission stderr according to whether a directory was admitted, matches the exact causal `JC2-JOB ERROR:` line, checks expected absent/admitted/unchanged directory effects, MainPID0 and absent cgroup. Bad-pin, bad-path, wrong-instance, HQ, symlink, duplicate-tag and busy-lock calls each bind a specific expected reason. The failed-collection control separately requires signal-derived153 and the C-locale file-size diagnostic before recovery.

The new `expected17` fixture changes only phase-one expected status, requires recorded17, a successful second phase and batch exit0; the existing unexpected17 case still requires absent successor/batch result. This tests mechanism, while manifest review remains responsible for never blessing a scientific failure code.

## Bounded test path and qualifications

The corrected plan declares one root driver with 600-second RuntimeMax, five-second control-group stop, 1GiB memory, swap0, CPU80%, Tasks128 and per-file64MiB; its direct logs are in the immutable stage. Each created child service independently retains at most30 seconds active plus bounded stop/receipt, 256MiB, swap0, CPU80%, Tasks32 and per-file8MiB. Terminal polls are finite; the FIFO release has a five-second foreground timeout; the controlled writer is in the outer driver cgroup. If the driver dies, children retain their independent limits and the outer cgroup owns its writer. External exact-ID retirement within15 minutes remains separately mandatory.

No aggregate disk/output quota or total CPU-time budget is created; the fixture is trusted and finitely small, and CPU remains a cgroup rate cap. The documentation phrase “last four” refusal cases is imprecise because `killed` is a service failure, but the explicit nine-name list and commands are unambiguous; this is not a source blocker.

## Remaining runtime obligations

The one regression may proceed only after ROOT binds a fresh worker, immutable installed paths/pins, actual DMI/instance identity, original deadlines and independent retirement. Acceptance still requires actual systemd/kernel values, direct nonroot identity/FSIZE gates, post-stop receipt, timeout and descendant cleanup, exact refusal causes, interrupted collection recovery, final driver exit0 plus every PASS, terminal driver/child cgroups, unchanged pins, bounded explicit archives, whole-byte transfer and worker retirement. SSH disconnect, power loss, OOM, aggregate storage, native/scientific fidelity and adversarial-root behavior remain explicitly unqualified.

No source, shared ledger, worker, process, or external system was changed or exercised in this review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6178`.
- Body SHA-256:
  `a496c3445f41c639f26e4997c3e32285717a335bad07679495ac057cd6fa1fbe`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
