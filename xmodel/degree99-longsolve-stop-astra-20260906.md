# Degree-99 long solves: scoped operator stop and retained custody

2026-09-06; owner `/root/model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Outcome

Both authorized solvers on `172.30.0.63` are stopped; their untouched
wrappers finalized telemetry, exit-code files and output hashes. Neither
solver produced a completed mathematical result. Classification:
**METHOD_ONLY / OPERATOR_STOP / NO_COMPLETED_RESULT**. This is neither unit
nor properness evidence.

Root authorized this stop because actual degree 99 was externally closed
and no named open client justified the remaining approximately 16 hours.
That is the operator's recorded reason, not a theorem re-audited here.
No solver retry, instance stop/termination, retag, package change, deletion,
or interaction with another worker occurred. All existing source, input,
output and instrument files remain in place.

## Exact signal custody

The first read-only snapshot was communicated to root at 12:29Z. The frozen
pre-stop snapshot is timestamped `12:32:05.856614Z`. The inherited custody
is `box/t2t3-longsolve-20260906/custody.json`, SHA-256
`64c74a0d5251d864419ef738a24972fddd07d58bf4fd4f43dc13d73abc0ec3f8`.

| Solver | Solver PID / PGID | Linux start ticks | Derived start UTC | TERM sent UTC |
|---|---|---:|---|---|
| msolve | 20597 / 20596 | 178713 | 08:25:46.130 | 12:33:03.180828 |
| Singular | 20637 / 20636 | 179018 | 08:25:49.180 | 12:33:03.184264 |

Worker hostname is `ip-172-30-0-63`; boot ID
`749752a4-f5b1-4d56-9500-72793f580440`. Exact solver argv, input paths,
live executable hashes, parent/group relationships, start ticks, cgroup and
namespaces were checked. Both solvers remained direct children of their
recorded `/usr/bin/time` group leaders. Their cgroup was
`0::/user.slice/user-1000.slice/session-87.scope`; PID and mount namespaces
were `pid:[4026531836]` and `mnt:[4026531832]`. User/cgroup/network namespace
identities are also frozen in the pre-stop and signal-plan records.

The original JSON did not record raw start ticks or namespaces: these were
anchored in the new read-only snapshot. Derived process starts match its
08:25:46/08:25:49 preflight times to less than a second. The subsequently
finalized CAPRUN files independently preserve the same boot/start-tick
identities for both group leaders.

Only solver PIDs 20597 and 20637 received SIGTERM, via
`pidfd_send_signal`, with identity revalidation after opening each process
handle and immediately before signaling. No group-wide signal was sent;
no escalation was needed. The shell, time and CAPRUN wrappers were left to
finish. Both process groups were completely empty at `12:33:33.215801Z`.
A later read-only check at `12:35:55Z` also found solver PIDs, time leaders
and known CAPRUN PIDs 20595/20635 absent. This audit covers these two jobs,
not every possible workload on the instance.

## Terminal results and resource release

| Job | Wrapper rc | CAPRUN terminal UTC / elapsed | Result |
|---|---:|---|---|
| `d2-z55-msolve` | 143 | 12:33:10.228919 / 14843.114 s | `basis.ms` and stdout both empty; partial F4 trace only. GNU time records termination by signal 15. |
| `d2-z55-singular` | 1 | 12:33:07.095622 / 14836.926 s | stdout is exactly `ALL_ROWS_PARSED`, `BEGIN_STD`, blank line, `halt 1`; no completed basis/result markers. |

CAPRUN reports `NORMAL_EXIT` because its registered `/usr/bin/time` process
returned 143 or 1. This lifecycle label is **not** successful solver
completion. Singular's `halt 1` is a termination message, not the unit ideal.
The msolve trace names first prime 1,073,741,827; even a characteristic-zero
`-g` header with `[1]` would not establish an exact Q proof without an
independent rational certificate. No such output exists here.

At the pre-stop snapshot, solver RSS was 245,901,262,848 bytes (msolve) and
116,445,462,528 bytes (Singular), approximately 337.46 GiB combined. Recorded
peak group RSS was 245,902,925,824 and 116,466,679,808 bytes respectively.
Host MemAvailable increased from 164,243,431,424 to 527,312,035,840 bytes
(approximately 152.96 to 491.10 GiB). Both solver VmSwap values and host
SwapTotal were zero; `pswpin` and `pswpout` remained zero. There was no swap
activity hidden by the stop. Full pre/post memory snapshots are retained.

## Source/output preservation and verification

All seven charged input/instrument hashes match both before and after:
the `.ms`, original `.sing`, derived `-slimgb.sing`, label map, msolve wrapper,
long-run wrapper and CAPRUN script. The two solver executable hashes also
matched inherited custody before the signal. The large input files remain
on the worker; they were not copied or rewritten. In particular:

```text
99-delta2.ms           7f593b87e40f02dbdb91f9b22aace6989f4a4d2092d9903276675b3265c7b572
99-delta2.sing         a604ed314ced1a33ff46e43081c2222430f24bde96a10405a3a8562ec6dccbbc
99-delta2-slimgb.sing   354b9293d065035f4e3b7ca2c918eb27cb5dc2ac3407eea2f02e9e467ba3ab7c
msolve caprun.json     ea7486561362a75ac723cd3fddede1be811d6e0bede74290322a58880c9f974d
Singular caprun.json   df585b272fd403c370dd15a448b84ed9cca92255505fd7c9c95bcbe520cdab37
msolve solver.stderr  dc511dfd1a060d1abb819aeb1f811b84f8655fbd2736afef42b88e5a91152d4b
Singular solver.stdout 9bc32e61a392947091e82fb8fe307804618d023894b40eb5d95f864bba4c8160
```

Every terminal regular file in the two run directories was copied into
`box/degree99-longsolve-stop-astra-20260906/evidence/<job>/` and checked
against its remote hash and the wrapper's postflight hash list. This
includes raw logs, basis file, timing, limits where present, custody,
CAPRUN, postflight hashes and `runner.rc`. No file was removed.

## Storage and stop-versus-termination handoff

Read-only EC2/EBS metadata at `12:33:31Z`:

- Instance `i-07e1212591a6acae9`, `r7i.16xlarge`, us-east-1a, still
  **running**. Owner tag remains `t2t3-longsolve-sol56-20260906`;
  Name remains `jc2-worker-20260906T075549Z`.
- One attached root EBS volume: `vol-09c6e3133f3442e56`, 100 GiB gp3,
  3000 IOPS / 125 MiB/s, unencrypted. EC2 device `/dev/sda1`; guest disk
  `/dev/nvme0n1`, serial `vol09c6e3133f3442e56`; root ext4 partition
  `/dev/nvme0n1p1` mounted at `/`.
- **DeleteOnTermination is true.** Termination would endanger this retained
  root volume. No termination or flag change was performed.
- `/home/ubuntu/t2t3-longsolve`, both run directories, their TMPDIRs,
  `/tmp/msolve-src-0101`, `/tmp/msolve-patched`, and the new custody directory
  are on that same EBS-backed root, not a separate tmpfs/instance-store
  mount. Root had 22,848,786,432 available bytes after the stop.

These two jobs no longer block a coordinator decision to stop the instance.
No blanket host-idle assertion is made. The `/tmp` source/install remain
in place, but boot/age-based temporary-file cleanup policy was not audited;
preserve those trees outside `/tmp` before relying on a later restart to
retain them. This task did not authorize instance control or a storage move.

Retained paths:

```text
/home/ubuntu/t2t3-longsolve/presentations/d2-z55-source/
/home/ubuntu/t2t3-longsolve/runs/d2-z55-msolve/
/home/ubuntu/t2t3-longsolve/runs/d2-z55-singular/
/tmp/msolve-src-0101/
/tmp/msolve-patched/
/home/ubuntu/degree99-longsolve-stop-astra-20260906/
```

## Charged stop artifacts

The compact final custody is
`box/degree99-longsolve-stop-astra-20260906/custody.json`, SHA-256
`256e06593ad876b130c29a665455c1c33429968069a243543d7083aef2c16e70`.
It records memory deltas, complete terminal hashes, signals, EC2/EBS metadata
and all retained locations. Supporting hashes:

```text
pre.json             ceef58df7ef723bd65822b245d536bfe38bdcec9b666d8c26ce01b7802ae8018
post.json            6dcdad1f83aca5d4dff828415e8eb5ccc10fd62c165633388267f79193c85e64
signal-actions.jsonl 2fe07d49a6361c8340f5bce5121cd554a0a97fdd7496d0e46a492febcaa199e9
storage.json         b9af388fb8600c43051870fdb0de5e2f642cd783dfcae2bfa66f1fa44ee2596d
stop_worker-v2.py    7539ed365aa5b39a96c77dc2b68a6feac856426c48a3dd03572146a131e9f91c
```

Both versions of the stop script are retained: the first produced the
read-only snapshot; the second adds an explicit start-UTC check for future
snapshots and narrows the post-stop source inventory. The signal path and
identity/PIDFD checks did not change. All scoped solver/finalizer work is
terminal; the instance remains under root custody.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8398`.
- Body SHA-256:
  `0847b18c0df6077bd431fc1642017f2d180ce445dc20ae7f1ae27fc13bcd9b94`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
