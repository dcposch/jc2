# TRIPLE02 proper-open resume: R5 custody repair report

Date: 2026-08-28

Verdict: `REPAIRED_PACKET_FROZEN_LAUNCH_NOT_AUTHORIZED`

The launch blockers in
`xmodel/triple02-proper-open-resume-r4-hostile-review-gpt56-20260828.md`
(SHA-256
`3e55f6f334c67d4ced74651dd612f174d2ea0cde205698a98e92c2c19a7ef7b9`)
are repaired at source and no-CAS fixture level.  No AWS job was launched and
no local Singular or other CAS process was run.  The mathematical Singular
program is byte-for-byte unchanged from R4 at SHA-256
`f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a`.
This R5 packet remains blocked pending a fresh independent hostile review and a
separate coordinator `GO`.

## R5 repairs

1. `swap_violation` and `whole_timeout` are sticky supervisor latches and
   mandatory arguments to the only terminal decision.  The final clean
   `/proc/meminfo` snapshot and worker return zero cannot erase either prior
   fault.  Containment-preflight, launcher-reap, and final-systemd faults are
   also mandatory fail-closed inputs.
2. The systemd route reads and strictly parses the literal PID contents of
   `cgroup.procs`; no metadata-size test remains.  It records final unit
   state/result.  A disappeared cgroup is accepted only on the explicit
   collected-unit route after prior membership and exact bounded launcher
   reap; all other missing/malformed/nonempty routes fail closed.
3. The containment launcher is bound to its exact PID, same UID, and `/proc`
   start time.  TERM/KILL and polling revalidate that identity.  Post-kill
   polling is bounded at ten seconds; shell `wait` is entered only after that
   same process is absent or a zombie and is therefore immediate.  Identity
   drift or failure to become reapable sets a sticky failure.
4. Terminal-manifest generation return status is recorded.  The complete
   regular-file census and hashes for every included root are independently
   replayed.  The temporary archive rejects unsafe, duplicate, extra, and
   nonregular members, is extracted to a fresh private directory, and its
   embedded complete manifest is replayed before atomic archive installation.
   Generator, live replay, extracted replay, outer archive, and final
   time/swap latches are all mandatory terminal inputs.  Any late failure is
   `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.

The public terminal remains outside the terminal archive.  The worker writes
only a candidate; the supervisor alone can atomically install one allowlisted
mathematical marker, as its final successful action.

## Focused negative controls

The no-CAS suite passes all prior containment controls and newly rejects:

- observed swap followed by a final zero-swap snapshot;
- whole-job timeout with worker return zero;
- nonempty, malformed, and missing `cgroup.procs` inputs;
- launcher start-time drift and a launcher that is still live at its bound;
- terminal-manifest generator and replay failures;
- an unexpected archive member; and
- a valid outer archive whose embedded manifest no longer matches its files.

It also preserves clean-promotion, detached-child, wrong-PGID, exact-job-tag
orphan, nonzero-late-worker, missing-scope, final-systemd-fault, and late
archive failure controls.  The named result is
`preflight/R5_CUSTODY_SELFCHECK.json`, SHA-256
`7d5e13f1c5874081cd8c13f83d528efbe18c7fcd30691346734aede3ce711509`;
its SHA sidecar replays.

## Mathematical-source preservation

The deterministic no-CAS builder replay regenerated the exact 11,446-line
Singular source at SHA-256 `f5050f...`, and `cmp` found no byte difference from
`preflight/TRIPLE02_NODE1_PROPER_OPEN_RESUME.sing`.  It again reported the
full c4 matrix reconstruction and zero proper-route pure-Delta or closed-node
searches.  The generator/classifier suite again rejected all five concrete
right-transform `C` mutations, nine count mutations, c4 deletion, endpoint
cross-term and plant mutations, archive/member/ring/Delta/residual drift, and
Singular diagnostics; both scoped classifier branches passed positive
fixtures.  Frozen transcripts are:

- `preflight/R5_BUILDER_REPLAY.stdout.txt`, SHA-256
  `b10a925fa1ecde6911114c4e544b0ffef9293dcdae02b22489441146554db741`;
- `preflight/R5_GENERATOR_SELFCHECK.stdout.txt`, SHA-256
  `c6ad6c5a42978f6d354d61202bc504bc693a2468f30b407306aaa0d044eac1da`.

No mathematical Python, Singular, adapter, classifier, worker, or frozen
dependency source was changed in R5.  Only the supervisor, containment helper,
containment fixtures, preregistration/custody prose, archive-external launcher
binding, and manifests changed.

## Archive and manifest replay

The R5 source archive was built twice with normalized metadata; the two bytes
matched.  It has exactly 20 unique, safe regular members and no links.  A fresh
private extraction replayed all 19 embedded `SOURCE_MANIFEST.sha256` entries,
and every extracted source member matched its live frozen byte.  R4 remains
preserved at SHA-256
`d22774d3f6f1607cd8d29428392e5e4d900339e7e6152979290fe6b11113c7d6`
and is not rewritten or a launch candidate.

## Frozen hashes

| artifact | SHA-256 |
|---|---|
| R5 preregistration | `11ea4e805c146b0753aac3d2af2e1f4eb1dd12302ac45252fd222fce960c8c32` |
| R4 hostile review charge | `3e55f6f334c67d4ced74651dd612f174d2ea0cde205698a98e92c2c19a7ef7b9` |
| generated mathematical Singular source | `f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a` |
| source manifest | `b942527587394ca27c64822ee168c77a09732f75965c5a773048d0cc0204b684` |
| R5 source archive | `60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310` |
| source-archive sidecar | `ddf9d7fff0c80447f2cf87a5f44f6eb591e658cd02e830647f852324218d1df9` |
| preserved R4 archive | `d22774d3f6f1607cd8d29428392e5e4d900339e7e6152979290fe6b11113c7d6` |
| archive-external launch preflight | `4b5b4c641a40f12a7b873adeafd1afee156f046e5207b8e1cc7b1aa574a504a4` |
| launch manifest | `513051d9807c61d27fb92b18bff14c00b1b438201fbe3e4ac92882e6b319ceda` |
| containment contract | `99d85dd2074f89cc2a73e1c27516ac50a106acb44b018511c48b7930a00bd2d4` |
| containment selfcheck source | `c7785b727e7e6a3adc01511c5cd07a635d1e1d024ef931aef8cc3ba086600616` |
| AWS supervisor | `ba97bfd061793d220a6c16c0c8e1e0651c165dc5d4a0eda16e4812eb5b5519f2` |
| AWS worker, unchanged | `789c0995e73bc9f1a2a2a533eff75b2effcf71ed694dd1ae1f547939695330a5` |

## Scope firewall and review request

The only possible mathematical terminals remain the two TRIPLE02 node-1
proper-open markers in `AWS_PREREGISTRATION.md`.  Neither covers the chart
complement, TRIPLE02 as a whole, another component, or the ambient endpoint
problem.  Please perform a fresh independent hostile review of the exact R5
archive, archive-external launcher, terminal latches, complete-manifest replay,
and focused negative controls.  AWS launch remains prohibited until that
review passes and the coordinator separately issues `GO`.
