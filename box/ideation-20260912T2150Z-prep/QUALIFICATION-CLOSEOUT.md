# Mixed-scalar qualification: metadata obtained; attempt CLOSED

ROOT administrative closeout, 2026-09-12 21:41 UTC. This is an execution and
custody record, not a promoted mathematical result or a qualified science run.
The original qualification cutoff was 21:20 UTC and was not extended.
No live dummy, CAPRUN regression, scientific import, algebra, enabled science
authority or six-phase registration ran. JC2 remains unresolved.

## Actual worker and retirement

- One personal/us-east-1 r7i.2xlarge, 8 vCPU/64 GiB:
  i-0ffb0b24da98f32a8, launched 21:00:16 UTC, private 172.30.0.113,
  hostname ip-172-30-0-113, boot afb5ad54-af6a-45ee-99b2-a0a24aa94d9e,
  PID namespace pid:[4026531836]. Exact owner was
  f10-mixed-qualification-root-20260912. No successor was allocated.
- AMI ami-066263bf15bd856de; root vol-08866d1c6bd6b386e, 100 GiB,
  explicitly DeleteOnTermination=false. Minimal cloud config disabled package
  updating/upgrading. Full Sympy/mpmath package copies were installed, not
  pruned. Their original combined census was 3092 regular files.
- The independent HQ timer jc2-mixed-qual-retire-20260912.timer was armed
  at 21:00:43 for the original 21:25 retirement. No transfer to a 22:30
  science retirement occurred. ROOT requested exact-ID termination at
  21:22:38.505340559 after local custody; AWS returned shutting-down.
- The timer fired at 21:25 and its API call returned both previous/current
  state terminated. It was NOT stopped by ROOT before firing. Direct checks
  at 21:25:28 and again in the 21:40:06 check confirmed TERMINATED; the
  retained root volume was AVAILABLE/unattached, 100 GiB.
- Both nonterminal regional campaign selectors were empty at 21:31:01 and
  again in the successful check begun 21:40:43. The retirement timer/service
  were not-found/inactive/dead with blank InvocationID and service MainPID=0.
  Retained EBS incurs storage independently of terminated instance compute;
  no price, exact billing duration, all-region or historical-volume audit is
  claimed. No evidence volume or local evidence was deleted.

## Metadata actually executed

Installed layout: /opt/jc2-mixed-20260912/{science,runtime,lib,meta,prep}.
The source/runtime directories had their exact three files, root-owned0444;
lib contained full Sympy and mpmath trees. Preparation output was a separate
256 MiB tmpfs. No science-output or dummy tmpfs was created.

The collector's only source change was substituting this physical instance
for its placeholder. Its systemd service used Type=exec, Restart=no,
RuntimeMaxSec=595, TimeoutStopSec=5, KillMode=control-group, CPUQuota=80%,
period100ms, MemoryMax=1 GiB, swap0, TasksMax64 and FSIZE4 MiB. Absolute TERM
and KILL timers for 21:19:55/21:20 were armed before launch. Its actual live
cpu.max was `80000 100000`, burst0, memory.max1073741824 and swap.max0.
The timers were stopped after collection and independently inactive by21:17.

| Phase | Actual execution and retained outcome |
|---|---|
| Native collector | 21:08:31.033921408--21:09:09.798021000; MainPID1622; invocation3d8d58f059d144879fdb7422463ea655. Complete NATIVE_END, 4330 files/419 directories/35 aliases; exact-invocation journal says deactivated successfully. |
| Record assembler | 21:17:09; invocationeb37ca776d4941709807a9ec8e9f82d1. `systemd-run --wait` returned actual exit0, success, runtime187ms/CPU172ms. Receipt says ASSEMBLED_METADATA_ONLY_UNQUALIFIED, science NONE. |
| Administrative inspector | 21:18:40; invocation1fa26e56f5b34db5adc1cc0f4fc85977. `systemd-run --wait` returned actual exit0, success, runtime455ms/CPU386ms. Metadata-only checks passed. |

The assembler used isolated Python `-I -S -B`, its pinned native_records.py,
authenticated raw/facts inputs and fresh private output, under115+5 seconds,
80% CPU,1 GiB/swap0,4 MiB FSIZE and bounded preparation storage. The inspector
used the same isolated metadata startup under25+5 seconds and the same small
resource envelope; neither imported CAS or scientific source.

The inspector rehashed every manifest file and every private package file
against its original apt copy; checked root ownership, absence of group/other
write bits and POSIX ACL xattrs on inventoried paths and their ancestors;
checked exact source/runtime/lib directory names, the three isolated base
Python paths and absent /etc/ld.so.preload. Actual Python was3.12.3,
package3.12.3-1ubuntu0.16; kernel7.0.0-1011-aws, systemd255.4-1ubuntu8.17.
These checks do not establish complete dynamic-loader/import closure or
science API/startup compatibility.

## Evidence and limits of custody

All SHA-256 values below were rechecked locally at closeout. ROOT read the
complete assembly receipt, inspector source/output and ten exact-unit journal
records. The 13839-line collector raw was read only at header/end: its body is
HASH_ONLY to ROOT, and was fully machine-parsed by the executed assembler.
The four large assembly outputs are byte-count/hash checked, not a ROOT
whole-body semantic review. Every stderr was empty.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| retained/prep/native.stdout | 1346913 | 40d4371062f60107c8c5b1f11ca3e9a1353a8bb638d7725a72cb0ac8efadda44 |
| retained/prep/assembled/assembly-receipt.json | 1103 | 94f1e57279b9b980da7c51bb09d14c6e3622d863b214ea747f45b4ee1923239e |
| retained/prep/assembled/native-manifest.json | 728824 | 6a8ba6098d73e6fc2dd3bfc4bb57734e2885aee6df8d00d316d01b88c7ea3b97 |
| retained/prep/assembled/native-stat-records.json | 439833 | ed98cf47e285938ef87c7bef2d752d7b78f1f8794c783bc339c9a39028f500d8 |
| retained/prep/assembled/native.sha256 | 586034 | bbaee127fb681ef6f3a953cd82c36c28138015215cc1f2c95f5b5574d828c642 |
| retained/prep/assembled/source-native-manifest.json | 599073 | 38e6947d80127cd120cf873b549f514f52129fe5d498320ee150a97a8deb2e10 |
| retained/prep/assembly.stdout | 163 | f6f7549c9aa9873c7e378bba6bdd2ad34515c1eb0dd9cf256f4f78405d62bfab |
| retained/prep/inspect.stdout | 572 | 76a4e264cb6a5d27c50c6b8dc5d3f0e0765bc86b0685161ef7976d92c5a155c7 |

Other binding retained files:

- REGISTRATION.md:2b95614bccbb1fb9b493e7aa8f2a0b2160f0453683978389dce598da613c4c4a.
- native-metadata.actual.sh:644cc39e5cf5f4b74b34e63aef6dc1ba988b5b51ab68b586404867c535e817e8.
- facts.json:6b0db3a628dbd440b521a074b59b2e9aef23233638bfce62eea2948bda7c5419.
- retained/meta/native_records.py:63178c8aeab6d2f81bfddf4cdcc732ee00204c73f68f43c5f04761a2dfe4be9a.
- inspect_native.py:b0ea56644448c310f34a4dbb4db33ad4ba5be6c5ac380adee6ca8eafce0b9d7a.
- worker-journal.jsonl:2ff2d0914fdd8a6038deb9f0fd9af756a178dbab0db977c877653ecfe8b41008.
- stage.tar:a4d86ef52ed2d203bd62298a747870c3dde0c1555003d2b86bc2679f91ad5db3.
- qualification-evidence.tar:987971b264de4b34ead949295d6233249a8ad9a77202c40900a36841e6dfc81f.

The evidence tar was made remotely, synced and tar-compared before SCP;
remote/local hashes matched. It contains meta and prep, not the complete
installed science/runtime/lib trees. Those trees remain on the retained root
EBS; the staged source packet is also local. Safe relative archive names were
inspected before extraction to fresh retained/. The original and retained
registration/facts/collector/inspector/stage-manifest copies compare identical.

Qualifications that must not be erased:

- The collector's actual command line and PID namespace were not independently
  captured while it remained live. The check at21:10:36 found its PID/cgroup
  already absent, not a within60second command confirmation.
- Its numeric terminal exit code was not retained. A subsequently unloaded
  transient unit's default Result=success/ExecMainStatus=0 with blank
  InvocationID is NOT actual exit evidence. The retained evidence is the
  exact-invocation clean-deactivation journal and complete raw output.
  The assembler/inspector instead have actual `--wait` exit0 observations.
- The new administrative inspector had no separate FIRST; its first recorded
  source SHA was post-execution, not a pre-execution pin. Its source and output
  are observational evidence, not promoted software or full qualification.
- The collector journal reports29295887000 ns CPU and2043904-byte memory peak.
  Reported memory is not an independently established true peak/RSS bound.
- Initial sed/stat display mistakes were corrected before charging the missing
  boot/DMI and cgroup-filesystem facts. A multi-unit stop command returned
  nonzero for absent services; subsequent checks established inactive timers.
  No metadata program was rerun to erase a failed execution.

## Decision

PROGRESS at the engineering-evidence level: this actual installation fits all
joint metadata limits; the full file projection is599073 bytes, not an assumed
future-host estimate. Qualification nevertheless STOPPED at its original
cutoff. Metadata routines were fast; ROOT coordination consumed the window.
No resource exhaustion, algebraic failure, user-authority blocker or JC2
progress is inferred from that scheduling failure.

Before any separately authorized future attempt, prewrite the finite operator
commands, including actual dummy identity/RSS/TERM/KILL/cgroup observations and
durable numeric exit capture. Delegate routine execution where useful. Do not
allocate a paid worker while designing that procedure; do not reopen this
registration, reuse its host facts, enlarge caps or launch a successor
automatically. The original mandatory dummy and actual science qualification
remain unmet. Mathematical scope and global ranking are unchanged.
