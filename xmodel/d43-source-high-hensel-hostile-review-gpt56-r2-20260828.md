# D43 source high-Hensel schema-v2 hostile review R2

Date: 2026-08-28

Reviewer role: independent hostile reviewer; I did not produce or mutate the
reviewed packet.

## Verdict

**REPAIR — AWS LAUNCH BLOCKED.**  The schema-v2 semantic replay is materially
better than the obsolete v1 packet, and the pinned p2 arithmetic replays, but
the sealed packet is not a closed or authenticated executable object.  A real
AWS reconstruction has already exposed an omitted runtime input.  After that
input was supplied diagnostically, the opt-in real stale-kernel test failed
before it reached the validator because its mutation discards the deterministic
p2 correction.  Independent static attacks also find an unsealed scratch/env
input path, a self-authorizing route, and process/terminal-custody gaps.

No p3+, target-16, or target-64 mathematical conclusion is licensed.  The
coordinator-reported AWS diagnostic attempts are all **NO_VERDICT**.

## Bytes reviewed

The following hashes were replayed from the workspace immediately before this
report:

| Artifact | SHA-256 |
|---|---|
| `cases/d43_source_high_hensel.py` | `eaa40faa998a79761aed6f020fbf2c72155a0aa9944b1b78e37e618479abbd66` |
| `cases/d43_source_high_hensel_aws_supervisor.py` | `d56a2e1d81fee1abae56922003ddf4f2a3ba41cc82d5c4e1f91bf30de1b3b251` |
| `cases/d43_source_high_hensel_aws_worker.sh` | `310b9be0d7f7e244d3b361d1997522b90a68109cfc410ce3107b2d6a9662d0a6` |
| `cases/test_d43_source_high_hensel.py` | `16a250bb501bdf87d34269179bce70868947b073282c428a9167b1649ff83034` |
| `cases/test_d43_source_high_hensel_aws_supervisor.py` | `7da073c628a4a0ab5753cbcf9162bc5ab0927d1541cd6af0edb08d27da1bb378` |
| `cases/d43_source_high_hensel_prereg_20260828.json` | `946c2de23ac23d5163fee05abc4ff584be09f91352f75ea588025f801a72ad8b` |
| `cases/d43_source_high_hensel_p2_replay_20260828.json` | `43d317e60b264171d7181c18469601d32ce81a761586fe453cb32cf54030c3a2` |
| `xmodel/d43-source-high-hensel-preflight-gpt56-20260828.md` | `06035799a0acfe7ffa72084faf624fb6c84f7af64a23df0ea610b9602e723564` |
| `cases/d43_source_high_hensel_aws_payload_20260828.sha256` | `5204aeef58226fb4485e17cde52dd3b80a9836802548b3ad061497f89d94ea10` |
| `cases/d43_source_high_hensel_preflight_20260828.sha256` | `e783bb856e50daee0aff4c7f1bee9e4e9b44f1bd9dd08a4af474f8c956bcc89b` |
| obsolete v1 hostile review (read as a repair charge, not a PASS) | `17cab0b49c80ff3eb5382edfaeea2cf98207a7e0aa67db00f9f7b3b6d928a5ce` |

Both supplied SHA manifests verify exactly against their listed files.

## Launch-blocking findings

### R2-1. The executable payload/dependency closure omits a required 1.52 MB row file

The real preparation path is
`prepare_d43_context` -> `d43_graph_witness.build_operator_point` ->
`d25_eplus.reconstruct_point` -> `band22_system` ->
`valuation_e.row22_rows`.  The last function reads
`cases/directionb_core23_p105337.ms` (`valuation_e.py:422-446`).  Its hash is:

`0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf`.

That file is absent from all three places that claim closure:

- `_dependency_hashes()` in `d43_source_high_hensel.py:578-605`;
- `d43_source_high_hensel_aws_payload_20260828.sha256`;
- `aws_route.payload_files` and `inputs` in the preregistration.

This is not hypothetical.  The subsequently harvested evidence packet
`cases/d43_source_high_hensel_aws_review_20260828/README.md`, SHA-256
`47d09920579b020a9f5fe59f12e3557a9d4d1b61f4de88cec18496c7b6f82249`,
records: the first lane stopped NO_VERDICT because NumPy was absent; after an
isolated NumPy 2.1.3 install, reconstruction reached the real path and stopped
on the missing `directionb_core23_p105337.ms`.  The failed run directory was
`/home/ubuntu/d43-high-review-87w9m0/run/`, with tags ending `T2020Z` and
`r1_T2024Z`; swap remained zero.  Its evidence manifest has SHA-256
`bd8a83ef22d2143e5ed44321e94fc2c9455a511d418b24494be4a127bbd45f51`
and replayed exactly in this review.

Required repair: include this file in the payload manifest, preregistered file
set, source archive, and semantic dependency fingerprint.  Then run an audited
file-open trace of the complete real context construction and fail on every
read outside the sealed source archive and explicitly created run scratch.

### R2-2. A listed input can be bypassed by inherited scratch or environment

Even `directionb_tails_D21.pkl`, which is listed and hashed, is not necessarily
the pickle executed.  `valuation_e.raw_rows21()` only copies the sealed repo
file if `/tmp/directionb_tails_D21.pkl` does not already exist
(`valuation_e.py:369-380`).  It then calls
`directionb_compress.load_nolog_rows()`, which calls
`directionb_window.load()`.  At module import,
`directionb_window.py:61-70` selects either inherited `DIRECTIONB_STATE` or an
existing `/tmp` pickle and unpickles it.  `directionb_residual32_emit.py:48,63-66`
also loads the scratch copy directly.

The supervisor inherits the caller environment and does not delete
`DIRECTIONB_STATE` (`supervisor.py:589-598`).  Consequently a stale scratch
file can change the mathematics, while a hostile pickle can also execute code,
without violating the repo-file manifest.  This is a custody and containment
failure.

Required repair: clear/reject all relevant inherited path/config variables;
copy the sealed pickle into a job-private directory with exclusive creation;
hash it after copy; bind the exact private path explicitly; reject pre-existing
scratch; and never unpickle an ambient `/tmp` or caller-selected file.

### R2-3. The opt-in real stale-kernel mutation does not test its stated attack

The test at `test_d43_source_high_hensel.py:303-332` computes a genuine mod-p
kernel vector, but then calls:

`apply_digits(p2_coordinates, ..., kernel, step=p, modulus=p^2)`.

`apply_digits` first reduces **every existing coordinate modulo `step`**
(`d43_source_high_hensel.py:330-339`).  Applied to a p2 point, this discards the
deterministic p2 correction before adding `p*kernel`.  A homogeneous kernel
vector need not solve the inhomogeneous p2 Newton right-hand side, so the next
assertion that all 184 rows vanish is not a validator test.

Again this is experimentally decisive: after the omitted row file was supplied
for diagnosis, the sealed AWS evidence records 7.49 s, 214,360 KiB maximum
RSS, zero swaps, and a failure at `self.assertEqual(rows, [0]*184)` before
`validate_resume_payload` was called (tag ending `r2_T2025Z`, complete stderr
SHA-256
`8df243c94406fd3e0985cc00401c0ebb64434558e11ebb299080eab66f38337e`).
This is a test defect, not a source-lift verdict.

An independent corrected checker,
`xmodel/d43-high-hensel-v2-real-kernel-shift-check-20260828.py`, SHA-256
`7d58174e73e30612cfda3354dee546cb7eed108e63fd8223364321916359185d`,
was also harvested.  Its AWS lane used free column 67, obtained 16 nonzero
kernel digits, changed 16 p2 coordinates, retained all 184 raw rows and the
E/E5/E6/unit gate, and was rejected specifically by
`semantic state-chain replay mismatch`.  The run returned rc 0 in 7.45 s,
used 210,988 KiB maximum RSS, and recorded zero swaps.  Thus the **core
schema-v2 semantic replay passes the correctly constructed attack**; the
producer's own required fixture and payload closure still fail.

Required repair: form every mutated coordinate as
`(p2_coordinate + p*kernel_digit) mod p^2`, applying the exact HW/fixed collapse
semantics, first prove all 184 rows still vanish, and only then require semantic
history replay to reject it.  Add a mutation that deletes/changes the history
point hash to ensure the rejection is not accidentally caused by an unrelated
shape field.

### R2-4. The preregistration and route marker are self-authorizing

The preregistration currently says
`PREREGISTERED_REREVIEW_REQUIRED_NO_AWS_LAUNCH`; the supervisor requires a
magic authorized status.  But the only root hash used is caller-provided
`--expected-prereg-sha256` (`supervisor.py:193-248,480-490,757-768`).  A caller
can change the status, compute its new hash, and provide that hash.  No sealed
review decision, coordinator authorization sidecar, signature, or immutable
launch record anchors the transition.

Similarly, `job_id`, expected hostname/instance ID, and lane tag are supplied
by the caller.  IMDS authenticates that the machine is some EC2 instance, but
there is no AWS tag/API check binding that instance to the registered job.

The runner's p3+ marker is just an unkeyed JSON envelope created by its parent.
The runner checks Linux, DMI, hostname, parent PID, runner hash, and the syntax
of several arbitrary hashes (`d43_source_high_hensel.py:1214-1271`), but it does
not independently verify the supervisor/worker hash, IMDS identity, manifest
or prereg bytes, an EC2 job tag, or a reviewer/coordinator trust root.  A light
mocked negative control constructed a custom-parent marker and obtained:

`FORGED_SELF_ATTESTED_MARKER_ACCEPTED forged i-forged`.

Required repair: authorize launch with a separate immutable review/coordinator
sidecar whose digest is compiled or otherwise independently pinned; bind the
reviewed prereg, payload manifest, supervisor, worker, target, job ID, live IMDS
identity, and verified EC2 job tag.  The runner must validate that binding, not
merely trust values written by its current parent.

### R2-5. The verified worker can be substituted through inherited process environment

The worker starts with `#!/usr/bin/env bash`.  The supervisor clones the ambient
environment wholesale and clears only a few numerical/Python variables
(`supervisor.py:589-598`).  It preserves at least `PATH`, `BASH_ENV`,
`LD_PRELOAD`, and related loader/shell configuration.  `PATH` chooses which
`bash` `/usr/bin/env` executes; noninteractive Bash evaluates `BASH_ENV` before
the sealed script body; loader variables can alter `/usr/bin/env`, Bash, or
Python.  All of this occurs after the input hashes and source archive were
created.  Therefore manifest verification does not imply that the reviewed
worker/runner semantics execute.

Required repair: use absolute, preregistered executable paths; construct a
small allowlisted environment from scratch; reject shell/loader/Python path
injection variables; hash the exact interpreter/environment closure; and add
positive and hostile `BASH_ENV`/`PATH`/loader fixtures.

### R2-6. Python/NumPy execution semantics are recorded after selection, not pinned

The real path imports NumPy.  The supervisor accepts any importable version and
only records `numpy.__version__` and the Python executable hash after launch
(`supervisor.py:506,555-571`).  No Python distribution, NumPy wheel/version/hash,
or BLAS implementation is preregistered.  The first AWS diagnostic actually
failed because NumPy was absent; the next used an ad hoc NumPy 2.1.3 install.

Required repair: preregister a small immutable environment closure (or a sealed
image hash) and refuse version/build drift before source construction.  Since
the Jacobian engine deliberately uses float64 under an exactness bound, the
NumPy/BLAS execution environment is part of the audited implementation even
though mathematical values are meant to be exact.

### R2-7. Process containment can miss reparented/session-escaped children

The supervisor becomes a subreaper, but samples only descendants of the payload
root and members of the original process group (`supervisor.py:296-347`).  A
child can create a new session and exit/reparent between 0.1-second samples; as
an adopted child of the supervisor it is no longer reachable from the exited
payload root.  Adopted children are neither globally enumerated by
supervisor-parent identity nor reaped.  On termination, only the original
group plus previously sampled raw PIDs are killed (`350-383`); those PIDs have
no start-time identity, creating both escape and PID-reuse risks.  The success
path's final topology snapshot has the same root-based blind spot
(`637-647`).

Required repair: run the whole job in a verifiable cgroup/systemd scope and
gate terminal promotion on empty parsed membership, or maintain a complete
PID+start-time registry of every child/subreaper adoption with bounded reap and
kill loops.  Add a real setsid/double-fork escape fixture and a PID-reuse/start-
time fixture.

### R2-8. Late state/report/archive checks do not close terminal custody

After the process exits, the supervisor checks selected report fields but does
not independently load and semantically replay the copied state snapshot, or
compare the report's `state_payload_sha256`/history to that snapshot.  It does
not require the report's `aws_lane` to equal the authorization marker.  A
finite result is not required to have achieved the requested exponent.
Target-64 accepts an existing semantic p16 state, but that input state is not
pre-run snapshotted and hashed into the immutable job identity/source archive
before it is overwritten (`supervisor.py:500-545,656-705`; runner
`1304-1317`).

The 1200-second timer begins only after source archive creation and other
preflight work, so it is a worker timeout rather than the preregistered whole-
job cap.  Swap/orphan checks stop with the worker loop; report parsing,
snapshotting, manifest creation, archive creation, and terminal promotion have
no final swap/containment/resource gate.  `terminal_bundle()` generates a
manifest and archive but never independently replays either before returning
success (`406-426,686-710`).

Required repair: make the timeout and sticky swap/resource/orphan latches cover
the whole supervisor lifecycle; pre-seal any target-64 input state; parse and
semantically replay the final snapshot; cross-bind report/state/marker/target;
independently replay the complete terminal manifest and archive; and downgrade
every late failure to NO_VERDICT.

Additionally, job/tag/target/run-directory checks and run-directory creation
occur before the protected `try` (`supervisor.py:434-461`).  Those faults are
printed by `main` but do not receive an atomic terminal bundle.  A failure
bundle also does not preserve the external durable state's last committed
snapshot.  Move every gate into a durable fail-closed lifecycle and require a
terminal packet for every attempted job identity.

### R2-9. Target 16 -> 64 needs a separately sealed authorization and state handoff

The preregistration text says target 64 is a separate authorization, but the
same magic global status unlocks both target choices.  The runner requires an
existing finite exponent-16 state, which is good as a mathematical precondition,
but the supervisor does not require a distinct reviewed target-64 sidecar or a
registered hash for the p16 input state.

Required repair: target 64 must have a new immutable prereg/review authorization
binding the exact target-16 terminal archive, state envelope hash, history hash,
environment, payload, and new job identity.  It must never be unlocked merely
by reusing the target-16 status string.

## What did pass

These positive findings do not override the launch blockers:

1. Both SHA manifests replay against their listed bytes.
2. `python3 -m unittest -v cases/test_d43_source_high_hensel.py
   cases/test_d43_source_high_hensel_aws_supervisor.py` completed 23 tests:
   22 PASS, the opt-in real reconstruction skipped, zero failures, about 0.15 s
   and 31.8 MB RSS in the observed light run.
3. `py_compile` of the runner, supervisor, and both test modules passed;
   `bash -n` of the worker passed.
4. The runner's stdlib-only `--selftest` passed and reproduced necessary p2
   gate hash
   `39702f29d6e1a0b6f45864eca343b555620b41d8cb747b60bca057b3799804e3`.
5. The schema-v2 replay algorithm reconstructs the registered initial state and
   every transition, then exact-compares the entire payload.  An obstruction is
   accepted only after a fresh extra transition reproduces it.  The light
   synthetic stale-state and forged-obstruction fixtures exercise that logic.
6. Direct p3+ invocation refuses targets other than 16/64 and requires a route
   marker before expensive context construction.  This is useful defense in
   depth once the marker receives an external trust anchor.
7. The stated claim scope is appropriately narrow: finite raw 184-row source
   truncation plus necessary eliminated E/E5/E6 and unit conditions only.  It
   explicitly excludes parked/source equivalence, D25/template reconstruction,
   formal smoothness, a Z_p point, characteristic zero, and JC2 conclusions.

## Independent p2 arithmetic replay

A separate stdlib integer calculation from the pinned replay JSON, without
calling the runner's gate function, obtained:

- modulus `11095883569`;
- E terms `4315102731`, `6780780838`, sum `0`;
- HM values `5143408652`, `5143408652`, common and a unit;
- corrected-243 E5 residues `[0,0]`;
- `s1F = 9120266557`, a unit;
- cube E6 residue `0`;
- W1 and W2 both units.

The canonical JSON summary hash is
`b98e32f539a8d8a459215162e00c4de2a806c76e64629b477f52cc6663634fc6`,
and every value matched the pinned replay JSON.  This verifies the finite
arithmetic implemented by the stated formulas.  It does **not** replay the
unshipped derivation of E5/E6, parked/source equivalence, the raw-to-NF bridge,
or any p3+ state.

## Mandatory repair and rereview gate

Before target 16, the producer must at minimum:

1. close and hash the actual runtime file and environment graph, including
   `directionb_core23_p105337.ms`, private sealed D21 scratch, and pinned NumPy;
2. repair the real kernel-shift fixture so it preserves the deterministic p2
   base correction and actually reaches the schema-v2 validator;
3. replace self-attested prereg/route authorization with a separately sealed
   review/coordinator and AWS-tag binding;
4. use whole-job containment and late fail-closed terminal replay;
5. make target 64 a separately reviewed continuation binding an exact p16
   terminal/state input;
6. reseal all source, tests, preregistration, manifests, and reports, then obtain
   a new independent hostile review.

## Is another AWS real-kernel diagnostic required before target 16?

**A corrected diagnostic has now passed for the present core validator, but a
post-repair execution of the producer's sealed fixture is still required.**
The independent AWS checker already records, in order: exact p2 construction;
nonzero kernel with `J*k=0`; 16-coordinate `p2+p*k (mod p2)` mutation; all 184
rows zero; E/E5/E6/unit gate PASS; and rejection specifically for semantic
state-chain drift.  That is strong evidence that the schema-v2 replay repair is
mathematically effective.

It does not make the producer packet launchable: the packet's own opt-in test is
wrong, the execution-input closure is open, and the independent checker is not
part of the current sealed payload.  After repairing and resealing those bytes,
run the corrected packet fixture (or the byte-identical checker newly included
in the sealed tests) once in an isolated zero-swap AWS lane and bind its archive
to the new review.  Only then may a fresh hostile review consider target-16
authorization.
