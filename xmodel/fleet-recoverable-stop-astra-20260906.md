# Recoverable stop of the two terminal JC2 workers

2026-09-06; owner `/root/model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Outcome

**Both authorized instances are STOPPED**, confirmed by EC2 at
`2026-09-06T12:47:38.588675Z`. One explicit `StopInstances` call was recorded
at `12:46:49.533497Z`. No instance was terminated; no tags, volumes or
DeleteOnTermination settings were changed. No other worker was contacted.
There is no mathematical promotion or solver retry.

| Former endpoint | Instance | Retained root EBS | Unchanged Owner tag |
|---|---|---|---|
| 172.30.0.63 | i-07e1212591a6acae9 | vol-09c6e3133f3442e56 | t2t3-longsolve-sol56-20260906 |
| 172.30.0.56 | i-0da0cebfc97c9fd54 | vol-0eb6450d18ffa89f1 | coordinator-factored-jacobian-20260906 |

Both volumes are 100 GiB gp3 in us-east-1a and remain attached/in-use.
Both still have **DeleteOnTermination=true**: sole retained data copies
must not be treated as safe to terminate. STOP was chosen explicitly to
retain these volumes and their contents. No EBS snapshot was created.

## Process/ownership gates and one resolved exception

Read-only whole-machine process/storage snapshots were captured on both
workers at 12:41:28Z, followed by fresh readiness snapshots at 12:45:02Z.
The latter contained only the individually inspected system services,
user-session infrastructure and this audit's SSH/Python ancestry: no live
solver, builder, replay, model client or other compute owner remained.
Boot identities stayed unchanged, and a fresh EC2 describe immediately
before STOP rechecked exact IDs, private IPs, Owner tags and EBS mappings.
The stop driver fails closed on a changed owner, unexpected process,
unexpected disk, incomplete archive or stale readiness snapshot.

The first `.63` audit found orphan PID/PGID 24286, start ticks 197859:
a bash loop waiting for nonempty msolve stdout and Singular `BEGIN_STD`
from the already stopped two-job batch. No instance action occurred while
this exception was unresolved. Root explicitly authorized its cleanup.
Exact argv, start ticks, group, session-91 cgroup and namespaces were
revalidated; PIDFD SIGTERM was sent only to bash PID 24286 and its validated
`sleep 15` descendant PID 289098. No members remained. No unrelated
process was signaled. The two original solvers' earlier stop/result custody
remains in `xmodel/degree99-longsolve-stop-astra-20260906.md`.

No campaign artifacts were found in the inspected shared-memory location;
`/dev/shm` contained only the system EC2-connect directory and reported
zero used bytes. `/tmp` had the two `.63` msolve trees plus normal system
temporary directories; `.56` had no campaign build/input tree in `/tmp`.
No local instance-store disk was present. Repository contents outside the
specified campaign artifacts were not inspected or changed.

## Exact preservation of the .63 temporary trees

Before STOP, `cp -a` made new, non-overwriting copies:

```text
/tmp/msolve-src-0101
  -> /home/ubuntu/fleet-recoverable-stop-20260906/msolve-src-0101
/tmp/msolve-patched
  -> /home/ubuntu/fleet-recoverable-stop-20260906/msolve-patched
```

The source tree contains 557 entries / 33,169,729 regular-file bytes;
the install tree contains 40 entries / 7,299,894 regular-file bytes.
Every regular file hash, symlink target, directory/file type and permission
mode matched the destination and a second read of the original. Both
originals remain in place. The installed executable also matched its
existing custody hash before copying. This is a faithful file-tree archive,
not a claim that the copied binaries' embedded library paths are relocatable;
restore required original paths or rebuild before reuse if `/tmp` is cleaned.

The source inputs and both terminal run directories remain under
`/home/ubuntu/t2t3-longsolve/`. The previous task already harvested and
hash-verified every terminal run file. No input/output/source file was
deleted, moved, overwritten or truncated by this housekeeping task.

## .56 full-J and instrument retention

All nine declared pilot/review/replay directories were checked on the
EBS-backed root filesystem. In particular, these key file hashes match
their prior custody exactly:

```text
factored-jacobian-pilot-20260906/complete_checked.sing
  50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091
factored-jacobian-pilot-20260906/complete_export.generators.jsonl
  39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f
full-j-solver-pilot-20260906/complete.slimgb.sing
  f87c0718b7df56c2b421a9d145e0e30d4e337ac2dca4a4c73d036033a55487cb
full-j-solver-pilot-20260906/complete.p1073741827.ms
  5a7f674325e9e8cb483234bd8b510f54bff387032498ed49ba76e084748517e2
msolve-allocation-repair-20260906/msolve-source/.libs/msolve
  175575870bf76a3c3a21c1660e1f6c7b8604a256fc4123643ce9711589326434
```

All paths above are relative to `/home/ubuntu/` on `.56`. Each key file
also has the root filesystem's device ID 66305; none is stored in tmpfs or
on instance-local ephemeral media. Large complete-J streams remain there,
not on the coordinator host. The entire corresponding source, library,
output and replay directories remain retained; they were not rewritten.

On both workers, EC2 `/dev/sda1` maps to the guest NVMe root disk and ext4
partition `/dev/nvme0n1p1` mounted at `/`. Both `/home/ubuntu` and `/tmp`
were on that EBS-backed filesystem. Remaining root free space after archive
work was approximately 22.81 GB on `.63`, 20.30 GB on `.56`.

## Restart and custody handoff

Root retains both instances and volumes. On restart, re-resolve addresses
from the exact instance IDs; treat cached/public endpoints as stale because
public IPs can change. Recheck mounts, hashes, runtime library paths and
task ownership before launching anything. This report grants no new solve
authority; characteristic-zero msolve `-g` output still needs the usual
exact-Q evidence discipline.

The compact custody package is
`box/fleet-recoverable-stop-astra-20260906/`. It includes both process
snapshots per worker, storage/ownership metadata, complete archive manifests,
monitor signal identities, readiness gates, the STOP API response, final
STOPPED states and retained-volume response. All archive/audit/cleanup
payloads had ended before the API stop. There are no remaining task writers.

SHA-256 anchors:

```text
custody.json       813eaa6735ccc771df19c690550d39f29ba11a25fcdbfc2957c3fc354b95be88
archive63.json     b029e2ce4acd3f0e7e2a2698572b7d396d7d232994c7f79e3a14c50428364bc2
archive56.json     60e3f33c2f7fe9644b1854e2563174e25b77b29093dbddab81baa4927ddef475
monitor-cleanup.json 837f7ae9ee943900f81771b31d34ecc31a8f166b618638bea5679258bc75c6e5
stop-response.json 52e9980ef3b852f9bcfb1770f36bcf517a0599d32838caa447badbfcad619271
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6797`.
- Body SHA-256:
  `3b490ec8cd5373b195221052cb85ede55a7216d4aa69f43d911708117d48e1b0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
