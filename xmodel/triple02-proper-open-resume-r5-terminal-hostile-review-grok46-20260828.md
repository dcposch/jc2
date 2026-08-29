# Hostile terminal review: TRIPLE02 proper-open resume R5

Date: 2026-08-28
Reviewer: Grok 4.6, equal-standing adversarial mathematical and custody referee
Charge: independent review of the completed AWS terminal, not of coordinator prose

Verdict: **PASS**

This PASS authorizes campaign promotion only of the literal claim
`EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` for TRIPLE02 node 1 on
`D(Delta)` in `Spec(R/I)` over `R=Q[q0,q2,c4,c6]` with `dp` order.  It does
not authorize any inference about the closed successor `V(I,Delta)`, a later
recursive node, the whole TRIPLE02 component, the geometric ambient endpoint
locus, or JC2.

No AWS job, no Singular or other CAS process, and no `jc2-lean` access
occurred in this review.  The producer packet was not modified.  This report
is the only repository file written.

## 0. Charged inputs, all independently hashed before any extraction

| object | charged SHA-256 | live recomputation |
|---|---|---|
| terminal archive | `4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e` | match |
| source review `xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md` | `b886d8bb516f04f3ca6683b17e8f1502c9b4e40eff55a9aab52dd922d48df10b` | match |
| frozen R5 source archive | `60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310` | match |
| frozen generated Singular program | `f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a` | match |

Local sidecar (repo-relative path) and remote-custody sidecar (AWS job-root
path `/home/ubuntu/jobs/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d/ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d.terminal.tar.gz`)
both carry that same outer digest.  Independent recomputation of the archive
bytes matches both sidecars.  The controlling preregistration hashes to
`11ea4e805c146b0753aac3d2af2e1f4eb1dd12302ac45252fd222fce960c8c32`, which is
the pin in `runtime_expectations.env`.

The passing source review is treated only as a launch-authorization record.
Every mathematical and custody claim below is taken from extracted evidence.

## 1. Archive inventory, extraction, and replay

The gzip tar was inventoried **before** extraction.  Census:

- 574 unique members (574 total; no duplicate names)
- 84 directories, 490 regular files
- no symlinks, hardlinks, FIFOs, devices, absolute paths, or `..` traversal
- owners numeric-normalized as `ubuntu:ubuntu` (uid/gid 1000)
- regular files are `0444` under `source/` and `0600` under `work/`,
  `custody/`, and `output/`

Extraction was into a fresh private `0700` directory under `/tmp` that did not
pre-exist.  Extracted regular-file census equals the tar regular-file census
exactly (490/490).  Top-level members are exactly `source/`,
`source_archive.tar.gz`, `work/`, `custody/`, and `output/`.

Embedded `custody/TERMINAL_MANIFEST.sha256` has 489 entries, excludes itself,
contains no duplicates, and names a set equal to the extracted regular files
minus the manifest.  Independent SHA-256 replay: **489/489 OK**.  The one
regular file not in the manifest is the manifest itself, which is the
reviewed include-root contract (roots `source`, `source_archive.tar.gz`,
`work`, `custody`, `output`).  Worker artifact manifest independently
replays **16/16 OK**.

`source_archive.tar.gz` inside the terminal is byte-identical to the frozen
R5 source archive `60f83a1d...`.  Extracted `SOURCE_MANIFEST.sha256` replays
**19/19 OK**.  The generated production script
`work/generated/TRIPLE02_NODE1_PROPER_OPEN_RESUME.sing` is byte-identical
(`cmp`) to the live frozen preflight copy at `f5050f12...`.

## 2. Attack 1 — candidate and output classification

Exact bytes, including the trailing newline:

```text
custody/CANDIDATE_MATHEMATICAL_VERDICT.txt
output/VERDICT.txt
```

both equal `EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY\n`
(SHA-256 `75645210fa8d7a9cebada5680b6608dfeb1ebada23e8e1cebaba49bf9fc63a05`).

`output/SUMMARY.json` records the same classification, with
`endpoint_coefficient_nf_nonzero_count: 0`,
`endpoint_quadratic: "x14*x72+x1*x97"`,
`scope: "TRIPLE02_NODE1_D_DELTA_ONLY"`,
`proper_open_only: true`,
`whole_component_or_closed_successor_inference: false`,
`saturation_certificate: "SELF_CONTAINED_TWO_CONTAINMENT"`,
`node: 1`.

`custody/classifier.stdout.txt` is exactly

```text
CLASSIFICATION=EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY
TRIPLE02_PROPER_OPEN_RESULT_CLASSIFIER_PASS=1
```

with empty stderr.  Production stdout contains exactly one
`CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA` and exactly one
`ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=0`, and zero copies of the survivor
marker.

I re-ran the **extracted** `classify_resume.py` against the extracted
stdout, stderr, result JSON, generated script, transcript gate, production
artifact root, and archived pivot/residual files, writing into a throwaway
directory.  Exit 0.  The replayed `SUMMARY.json` and `VERDICT.txt` are
byte-identical to the archived output pair.  That is not coordinator prose;
it is an independent consumption of the complete expected outputs.

Inherited R3 chart files under `work/prepared/work/base/output/` still say
`ROOT_CHARTS_COMPLETE_COMPLEMENTS_COMPONENTWISE` and
`ENDPOINT_DEAD_ONLY_ON_D_DELTA`.  Those strings are provenance inside the
frozen R3 terminal; the R5 classifier does not read them, and they are not
the candidate.  The archived R3 timeout remains `NO_VERDICT`
(`ARCHIVED_TIMEOUT_REMAINS_NO_VERDICT=1` in prepare stdout).  That is the
correct refusal to promote a timed-out saturation prefix.

## 3. Attack 2 — scope is TRIPLE02 node 1 on `D(Delta)` only

From production stdout, each of the following appears exactly once:

- `NODE_INDEX=1`
- `RING_ORDER=Q[q0,q2,c4,c6]_dp`
- `PROPER_OPEN_IDEAL_CERTIFICATE=1`
- `PROPER_OPEN_ROUTING_PASS=1`
- `CLOSED_SUCCESSOR_ENTERED=0`
- `PURE_DELTA_POWER_SEARCH_ENTERED=0`
- `NODE_SATURATION_RECOMPUTATION_ENTERED=0`
- `SCOPE_FIREWALL.marker` bytes
  `OPEN_RESULT_BANKED_WITHOUT_CLOSED_SUCCESSOR_OR_WHOLE_STRATUM_PROMOTION\n`

Builder stdout, independently of Singular execution, records

```text
NODE_SATURATION_RECOMPUTATION_CENSUS=0
PROPER_PATH_PURE_DELTA_POWER_SEARCH_CENSUS=0
PROPER_PATH_CLOSED_SUCCESSOR_CENSUS=0
```

and `build.json` has `"proper_open_resume_only": true` and
`"whole_stratum_inference_authorized": false`.  The worker allowlist and
the contract `MATH_TERMINALS` set contain only the two preregistered
node-1 proper-open markers.  Nothing in the extracted evidence reaches a
closed-node, whole-component, ambient-locus, or JC2 claim.

## 4. Attack 3 — return codes, hashes, timeout, classifier inputs

**Singular subprocess vs wrapper.**  `run_singular_stage.py` writes
`production.result.json` from `Popen.wait()` of `/usr/bin/Singular` and
returns that same integer as the Python process exit.  `aws_job_worker.sh`
then wraps that Python process in `/usr/bin/time -v` and records the wrapper
exit in `production.rc`.  Those two numbers are not the same object.

| record | meaning | value |
|---|---|---|
| `custody/production.result.json` `returncode` | Singular subprocess | `0` |
| `custody/production.result.json` `timed_out` | stage-runner timeout flag | `false` |
| `custody/production.result.json` `elapsed_seconds` | stage-runner clock | `8.824917` |
| `custody/production.runner.stdout.txt` | stage-runner report of the subprocess | `SINGULAR_STAGE_RETURNCODE=0`, `SINGULAR_STAGE_TIMED_OUT=0` |
| `custody/production.time` `Exit status` | GNU `time` wrapper around the Python runner | `0` |
| `custody/production.rc` | worker `run_stage` wrapper exit | `0` |
| `custody/worker_exit_code.txt` | worker bash EXIT trap | `0` |
| `custody/supervisor_worker_returncode.txt` | supervisor `wait` of the launcher | `0` |

The classifier binds the **subprocess** record: it requires
`timed_out is False`, `returncode == 0`, and byte hashes of stdout, stderr,
and the generated script.  All three hashes match the extracted files,
including empty stderr at the empty-file SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Wrapper `production.rc=0` is consistent here, but it is not what the
classifier consumes.  A truncated or swapped stdout with a lucky wrapper
zero would fail the result-JSON hash gate.

The hostile diagnostic is the opposite illustration: Singular subprocess
`returncode` is also `0`, but stdout contains three `?` diagnostics.  The
transcript gate accepted it only because `--expect diagnostic` matched
those three lines.  Production was gated `--expect clean` with
`diagnostic_count: 0`.  Return code zero is not a transcript.

**Pinned hashes, all matching the preregistration / `runtime_expectations.env`:**

| pin | value |
|---|---|
| generated script | `f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a` |
| source archive | `60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310` |
| preregistration | `11ea4e805c146b0753aac3d2af2e1f4eb1dd12302ac45252fd222fce960c8c32` |
| normalized Singular version | `f16fa01f3d3bdb83ac08dc7dbc25ebd84ba147bf3433779a0f5c695cee9ad9ec` |
| `elim.lib` | `cb39b70a6cff9f1bf6b6397b9de3a597f6bb9d91dad468243bed9bfb2552fcd1` |
| frozen R3 terminal | `e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1` |
| R5 recursor `recurse_component.py` | `d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90` |
| transcript gate | `0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316` |
| archived saturation prefix stdout | `4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418` |
| inherited rank-six archive / member | `b947a2d3...` / `cc6dc1c4...` |

Production cap is 1200 s against 8.82 s elapsed.  GNU time wall clock is
`0:08.98`.  Whole supervisor window is 21 s (`23:40:50Z`–`23:41:11Z`)
against the 1800 s latch.  `sys_vendor` is `Amazon EC2`, instance
`i-07eeaf8ba6f0bc419` (`r6i.8xlarge`), hostname `ip-172-30-0-45`, and the
IMDS `CodexJob` tag equals `JOB_TAG`
`ggv_triple02_proper_open_resume_r5_20260828T233745Z_r6d`.

All 65 `REQUIRED_LINES` of the extracted classifier occur exactly once in
production stdout (71 lines total).  Zero `FATAL_*` lines.  Zero forbidden
proper-route markers.  Artifact censuses used by the classifier:

| file | header | records |
|---|---|---|
| `NODE_001_CHART_PIVOTS.tsv` | `step\|source_row\|source_col\|pivot` | 95, byte-identical to archived pivots `2edaa006...` |
| `NODE_001_CHART_RESIDUAL.tsv` | `rows\|11\|cols\|10` | 110, byte-identical to archived residual `f24a4a23...` |
| `NODE_001_CHART_BASE_CHANGED_RESIDUAL.tsv` | `rows\|11\|cols\|10` | 110 |
| `NODE_001_BASE_CHANGED_RIGHT_TRANSFORM.tsv` | `row\|col\|normal_form` | 11025 unique `(row,col)` pairs, 0 duplicates |
| `NODE_001_BORDERED_IDENTITIES.tsv` | `basis\|free_col\|residual_row\|normal_form` | 44, all NF `0` |
| `NODE_001_ADJUGATE_KERNEL_105.tsv` | `coordinate\|basis\|normal_form` | 420 |
| `NODE_001_ENDPOINT_DELTA2_CLEARED_NF.tsv` | `basis_i\|basis_j\|normal_form` | 10 |
| `NODE_001_REVERSE_CONTAINMENT_ATTEMPTS.tsv` | `basis_generator\|exponent\|normal_form` | 4 |
| `NODE_001_REVERSE_CONTAINMENT_WITNESSES.tsv` | `basis_generator\|found\|exponent\|normal_form` | 2 |

## 5. Attack 4 — two-containment certificate and the ten coefficients

Let `B` be the ideal generated by the resumed active basis.  That file is
byte-identical to the preregistered archived OPEN_SB
`e2d240e369e516ad8e3fb3ac221061abe465a241ce91ceeef96a4e7c0947493c`, with
literal generators

```text
9*q0-80
159432300*q2^4*c6 + 20503125*q2^4 - 391820820480*q2^2*c6^2
  + 75582720000*q2^2*c6 + 240734712102912*c6^3
  - 3240000000*q2^2 - 61917364224000*c6^2 + 995328000000*c6 + 128000000000
```

`NODE_001_STANDARD_BASIS.txt` is a **different** polynomial list
(`84872c7a...`): the node ideal `I`, not `B`.  The classifier hashes the
resumed active basis, not this file.  That distinction is load-bearing; a
swap would break the OPEN_SB pin.

**Forward containment `I ⊂ B` and stability `B:Delta^∞ = B`.**  Production
stdout has `RESUME_NODE_INCLUSION_FAILURES=0`,
`RESUME_OPEN_BASIS_REPLAY_FAILURES=0`,
`RESUME_CANDIDATE_STABILITY_FAILURES=0`,
`CANDIDATE_STABILITY_SATURATION_ENTERED=1`, and
`NODE_SATURATION_RECOMPUTATION_ENTERED=0`.  The archived saturation object
is bound as provenance only.  The program did not re-enter `sat(I,Delta)`.

**Reverse containment `B ⊂ I:Delta^∞`.**  The attempts TSV is the actual
search trace, not a summary bit:

```text
basis_generator|exponent|normal_form
1|0|9*q0-80
1|1|0
2|0|<the second B generator, nonzero>
2|1|0
```

So `NF_I(b_i)` equals `b_i` itself (the generators of `B` are not in `I`),
and `NF_I(Delta * b_i) = 0` at exponent 1 for both generators.  The
witnesses TSV records `found=1`, `exponent=1`, `normal_form=0` for
generators 1 and 2.  Stdout has
`REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT=2`,
`REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT=4` (inside the classifier
range `[2,130]`), and
`SELF_CONTAINED_TWO_CONTAINMENT_SATURATION_CERTIFICATE=1`.
Together with `I ⊂ B` and `B:Delta^∞ = B`, this is `B = I:Delta^∞` on the
declared ring.  Exhaustion did not occur.

**Right transform, adjugate, endpoint.**  Stdout has
`FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1`,
`RIGHT_TRANSFORM_ENTRY_COUNT=11025` matching 11025 unique recorded
`(row,col)` pairs, `CHART_BASE_CHANGE_REDUCTION_COUNT=11135`,
`NF_RATIONAL_UNIT_PIVOT_COUNT=95` with `NF_PIVOT_INVARIANT_FAILURES=0`,
`ADJUGATE_KERNEL_VECTOR_COUNT=4`, `LIFTED_KERNEL_ENTRY_COUNT=420`,
`COMPLETE_BORDERED_IDENTITY_COUNT=44` with zero failures (artifact: every
row ends in `|0`), `FULL_106_ROW_KERNEL_REPLAY_COUNT=424` with zero
failures, `C4_SOURCE_TOKEN_CENSUS=30`, and
`NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1`.  Selected minor
`1,2,4,7,9,11` × `1,2,3,5,6,7` is the preregistered SHA-256
`84b4c2c4...`.  Chart `Delta` is a nonzero rational polynomial; the
bordered plant equals that same `Delta`.

The ten symmetric coefficients of `E = x14*x72+x1*x97` after
`Delta^2`-cleared pullback are the complete upper triangle of a 4-vector
basis:

```text
1|1|0
1|2|0
1|3|0
1|4|0
2|2|0
2|3|0
2|4|0
3|3|0
3|4|0
4|4|0
```

Zero nonzero rows.  Shift plants: `endpoint_nf|0|plus_one_nf|1|plus_two_nf|2`
with both affine-replay failure flags 0, so the zero of `E` is not an
innocent `e = -1` artefact.  Classification marker and nonzero-count agree.

I did not re-execute Singular.  The certificate is the bound trace plus the
artifact censuses the already-reviewed generated program is required to
emit, consumed again here by the extracted classifier.

## 6. Attack 5 — sticky latches, censuses, stale/partial promotion

Custody latch files, each the single character `0` plus newline:

- `supervisor_swap_violation.txt`
- `supervisor_whole_timeout.txt`
- `supervisor_containment_preflight_failure.txt`
- `supervisor_launcher_reap_failure.txt`
- `supervisor_systemd_final_fault.txt`

`CONTAINMENT_EMPTY.marker` is `CONTAINMENT_EMPTY_PASS=1\n`.
`WORKER_FINAL_GATE.marker` is `WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1\n`.
Final censuses:

```text
custody/no_orphan_pgid_census.json  -> []
custody/no_orphan_job_tag_census.json -> []
```

`containment_cleanup.stdout.txt` is `CONTAINMENT_CENSUS_EMPTY=1`.
Launcher reap JSON is `ready_to_reap: true`, `terminal_state: "ABSENT"`.

Swap is `0/0` in preflight, worker-final, worker-prepromotion,
supervisor-final, and both telemetry samples.  GNU time records `Swaps: 0`.
`MemTotal` is 259751808 kB on `r6i.8xlarge`, under the 1 TiB cap.
Containment selfcheck on the AWS host printed every required `PASS=1` line
including the sticky-swap/whole-timeout, complete-manifest, late-worker-exit,
and late-archive negative controls.

**Containment mode is `pgid`, not `systemd_scope`.**  The preregistration
makes systemd a probe, not a requirement: the exact-PGID fallback is used
when the delegated user manager probe fails.  Evidence of that fallback,
not of a silent skip after a successful probe:

- `containment_mode.txt` is `pgid`
- `worker_identity.json` is `pid=pgid=sid=9005`, `mode=pgid`
- `validate-worker` wrote `WORKER_IDENTITY_CONTAINMENT_PASS=1`
- `scope_membership_gate.txt` is `1` (the pgid branch sets this on identity
  pass; it does not fake a cgroup membership)
- there is no `systemd_scope_cgroup.txt`, no
  `systemd_cgroup_procs_final.json`, and no
  `systemd_scope_collected.marker`
- `systemd_scope_unit.txt` is always written (the prospective unit name)
  and is not evidence the unit ran
- `supervisor_systemd_final_fault.txt` remains `0` because the systemd
  emptiness block is skipped in pgid mode, which is the reviewed control
  flow

The documented **collected-scope** cgroup-empty route is systemd-only.  This
job never entered it, so a missing cgroup census is required, not a hole.
The applicable emptiness obligation is the pgid/JOB_TAG pair, both `[]`.
Worker cgroup text `0::/user.slice/user-1000.slice/session-176.scope` is the
login session of the pgid fallback, not a job transient scope.

Process snapshots confirm the pgid boundary rather than contradict it.
At worker start, PID 9005 is `bash aws_job_worker.sh` with PPID 8971 (the
supervisor), PGID=SID=9005.  Stage identities record Singular children
inheriting that exact PGID/SID (production Singular PID 9132, runner 9131).
At worker end, 9005 is still the worker writing its own snapshot; the
supervisor `sleep 10` (PID 9148) is in PGID 8969, not 9005.  At supervisor
final, PGID 9005 is gone: only the supervisor and its `ps` child remain.
No Singular process survives.  Recorded launcher PID/starttime equal the
worker session leader; `setsid --wait` here exec'd into that leader rather
than leaving a distinct waiter.  Reap of that identity as `ABSENT` after
worker exit 0 is then a reap of the session leader, which is the fail-closed
direction.

`FINALIZATION_LATCHES.txt` is **not** in the archive.  The supervisor writes
it at `$JOB_ROOT` after the archive is frozen, then decides the public
marker.  That is the reviewed order.  The archive therefore cannot contain
the post-archive latch refresh; the in-archive latch files can only
understate a later raise.  Elapsed 21 s and swap 0/0 through supervisor
final make a post-archive raise implausible, and a raise would publish
`CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT` without deleting the already-frozen
candidate archive.  This review therefore refuses to treat the archive as
containing the public marker, which is the next section.

No contradictory positive-looking mathematical marker survives a failed
gate inside the archive: there is no second candidate, no `NO_VERDICT`
candidate, and no `TERMINAL.marker`.  The only `NO_VERDICT` / `TIMEOUT`
strings in custody stdout are the required provenance line
`ARCHIVED_TIMEOUT_REMAINS_NO_VERDICT=1` and the containment-selfcheck
negative-control names.

## 7. Attack 6 — candidate present, public marker absent

A recursive search of the extraction for `TERMINAL.marker` returns empty.
The archive contains `CANDIDATE_MATHEMATICAL_VERDICT.txt` and the
classifier output pair, and does not contain the supervisor's public
terminal.  The on-disk terminals directory next to the archive holds only
the tar and the two sidecars.

That is exactly the reviewed rule: the worker may write only the candidate;
the supervisor's last successful action is the atomic rename of
`TERMINAL.marker` **outside** the archive.  Promotion of the literal
proper-open claim is therefore a supervisor-side act witnessed by this
archive's candidate and by the independently replayed outer digest, not by
a marker smuggled into the tarball.

## 8. Stale / partial / post-fault promotion attacks

Checked and rejected from evidence:

1. **Timed-out R3 saturation prefix promoted as a certificate.**  Prepare
   stdout binds the prefix as provenance and keeps the archived timeout as
   `NO_VERDICT`.  Production entered candidate-stability saturation of `B`,
   not `sat(I,Delta)`, and produced fresh reverse witnesses.
2. **Wrapper rc 0 with a failed Singular subprocess.**  Result JSON
   `returncode` is the subprocess; classifier requires it.  Both 0 here.
   GNU time exit also 0.  The hostile stage shows subprocess 0 is still
   insufficient without the transcript gate.
3. **Partial stdout with complete artifacts.**  Result JSON stdout hash
   matches the 71-line file; every required marker has census 1; independent
   classifier replay is byte-identical.
4. **Archived pivot/residual swapped for a later chart.**  Exact byte match
   to the frozen R3 members pinned in the preregistration.
5. **Active basis swapped for `I`.**  Active SB pin is the OPEN_SB hash;
   `NODE_001_STANDARD_BASIS.txt` is a different object and is not the
   classifier's `active_standard_basis`.
6. **Nested R3 component classifications promoted.**  Different strings,
   different paths, not in the worker artifact manifest's output pair.
7. **Post-fault clean snapshot.**  Sticky latch files are 0; selfcheck on
   the host rejected the R4 “observed swap then final zero” and
   “whole-timeout with worker rc 0” fixtures.  Those latches are mandatory
   `decide_terminal` inputs in the extracted contract.
8. **Manifest/archive replay skipped.**  Independent inventory, census
   equality, 489/489 hash replay, and matching outer/local/remote sidecars
   are this review's replay of that gate.

## 9. Verdict

**PASS.**  The completed R5 terminal archive is custody-replayable and
mathematically coherent at the literal proper-open scope.  Campaign
promotion is authorized only for

```text
EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY
```

on TRIPLE02 node 1 on `D(Delta)`.  It is not a closed-successor theorem, not
a whole-component theorem, not an ambient geometric emptiness statement,
and not a JC2 statement.

## Hashes independently recomputed in this review

```text
4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e  terminal archive (outer, local sidecar, remote sidecar)
b886d8bb516f04f3ca6683b17e8f1502c9b4e40eff55a9aab52dd922d48df10b  xmodel/triple02-proper-open-resume-r5-hostile-review-fable5-20260828.md
60f83a1d4e2eae0f974027059bc1cb1e6de8c3fc687b6cce4af4072ab18c2310  frozen R5 source archive / embedded source_archive.tar.gz
f5050f1204f3d990be64f18c5776eb7204f2587273a64a533e6d56d37b49132a  generated TRIPLE02_NODE1_PROPER_OPEN_RESUME.sing
11ea4e805c146b0753aac3d2af2e1f4eb1dd12302ac45252fd222fce960c8c32  AWS_PREREGISTRATION.md
f16fa01f3d3bdb83ac08dc7dbc25ebd84ba147bf3433779a0f5c695cee9ad9ec  Singular.version.normalized
cb39b70a6cff9f1bf6b6397b9de3a597f6bb9d91dad468243bed9bfb2552fcd1  elim.lib
e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1  frozen R3 TRIPLE02 terminal
bbd28fe58d12a8f48312a552737bf0585fd4719883eb435457d6e6dedfa8796f  production.stdout.txt
75645210fa8d7a9cebada5680b6608dfeb1ebada23e8e1cebaba49bf9fc63a05  CANDIDATE and output/VERDICT.txt
e2d240e369e516ad8e3fb3ac221061abe465a241ce91ceeef96a4e7c0947493c  resumed active OPEN_SB
e638be10d42160fbba456a8c9de3b108cd1ea702abb352ffdde57b93eb68d815  NODE_001_ENDPOINT_DELTA2_CLEARED_NF.tsv
779e74dc5c7e6ddbef811c06037cdc297e9cd37a77e4b001c2684a74ab4fcf25  NODE_001_BASE_CHANGED_RIGHT_TRANSFORM.tsv
```

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/triple02-proper-open-resume-r5-terminal-hostile-review-grok46-20260828.md
```

computed after the final write, recorded immediately below.
<!-- self-hash -->
c5a1b3a64b79f6567fc8978869a8c1b0787e382eed96ab8d84f737888276f1c7  report body above this delimiter
