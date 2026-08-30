# R4-00 base-diagnostic controlled-stop receipt (Sol 5.6, 2026-08-29)

## Lifecycle and scope

**SEALED OPERATOR TERMINATION RECEIPT / NO MATHEMATICAL VERDICT.**  This
receipt records the coordinator-authorized controlled stop of the three
non-load-bearing `BASE_LIFT` diagnostics launched after the decisive R4-00
`FULL_GRADE19` jobs.  It changes only their operational lifecycle.  It does
not alter the promoted finite-jet theorem, and it does not promote a scheme,
base-properness, dimension, radical, arc, or map claim.

The stopped diagnostics were the exact-Q Rabinowitsch questions whether the
grade-18 base ideals for R2, R1+, and R1- are unit or proper.  Field-valued
R4 closure no longer depended on their answers; R1+ and R1- were conjugate
duplicate diagnostics.  Their preregistered caps were 43,200 seconds for
each job, 549,755,813,888 bytes RSS for R2, and 137,438,953,472 bytes RSS for
each R1 branch.

## Exact pre-signal identity gate

Immediately before action, `/proc` identity was re-read on the two authorized
hosts.  For every row, boot ID, PID, start tick, PPID/PGID ancestry, cwd,
executable, and argv matched the frozen launch target.  The exact packet hash
matched `LAUNCH.meta`, and `RESULT` was absent.

| host / target | launcher | CAPRUN target | worker session | Singular child | packet SHA-256 |
|---|---:|---:|---:|---:|---|
| Box02 R2 | 448323 @ 43376890 | 448356 @ 43376894 | 448357 / PGID 448357 @ 43376899 | 448359 @ 43376902 | `497e8c6bbc5b349242bf3db64a53a601fe41057f450edf9ebff47226528a8f03` |
| Box03 R1+ | 379369 @ 43377410 | 379402 @ 43377413 | 379403 / PGID 379403 @ 43377418 | 379405 @ 43377422 | `a6bbfaf7b6b7ec0a593afaa71442d587c1392d285158ef2a011d006a1429bdbc` |
| Box03 R1- | 379465 @ 43377524 | 379498 @ 43377528 | 379500 / PGID 379500 @ 43377533 | 379502 @ 43377536 | `260f93774ade8ff8d4efbbb26e2f1433490fd4e182426ad60450112205bb984f` |

Box02 boot ID was
`78106c0b-9891-4fc4-93ed-72de22449dd0`; Box03 boot ID was
`71bf27c9-5339-4e5e-b911-bca25340d281`.

## Controlled action and typed termination state

At 2026-08-29 23:21:13Z, `SIGTERM` was sent **only** to CAPRUN PIDs
448356, 379402, and 379498.  CAPRUN owned descendant cleanup.  No signal was
sent directly to a launcher, worker, Singular child, another process, or
another host.  All three launchers returned 143, and every named wrapper,
worker, Singular child, and descendant was then verified absent.

| target | CAPRUN status | wall seconds | max aggregate RSS | cleanup |
|---|---|---:|---:|---|
| R2 | `SIGNAL`, runner 143 / signal 15, child -15 | 3225.902395146 | 5,595,930,624 B | TERM sent; KILL not sent; leader reaped; group clean |
| R1+ | `SIGNAL`, runner 143 / signal 15, child -15 | 3225.325547336 | 21,885,517,824 B | TERM sent; KILL not sent; leader reaped; group clean |
| R1- | `SIGNAL`, runner 143 / signal 15, child -15 | 3224.183177563 | 21,939,331,072 B | TERM sent; KILL not sent; leader reaped; group clean |

Each `CAPRUN/v1` record says `reason=forwarded_signal`,
`term_sent=true`, `kill_sent=false`, `cleanup_complete=true`, and
`leader_reaped=true`; its `before-term` identity check is `MATCH`.  Stdout and
stderr are both zero bytes.  No `RESULT` or `ENDPOINT.sha256` exists.  The
only computational output is a partial `producer.sing` transcript/input.
Therefore these terminations are typed **NO VERDICT**, not emptiness,
nonemptiness, timeout, resource-cap, or engine evidence.

CAPRUN telemetry hashes are:

- R2: `30af94ab12bc7aec8a848ac370c416e0c37ca463a48d4a56b0596afa7de9dd58`;
- R1+: `4447fb3316316ea0aefaab8fa30e0890dc3e8ffe6965e372e1bf764cec12ed2c`;
- R1-: `ea1bd0f3cdcf7f554072bfda26d0f57d87892482c117353dc87cebe7c3977d8d`.

## Freeze and recoverability

The full terminated job directories and the pre/post host-control evidence
are frozen under
`cases/max12_812_order2_u2_62_k00_r400_exact_deciders_20260829/frozen_operator_stops/`.
The 32-file manifest is `BASE_OPERATOR_STOP_FREEZE.sha256`, SHA-256
`7fd226ebb41a53a420e9d634587b1bb57e48adc51d4fcb793935753a041c9e6c`;
all 32 entries verify.  Direct remote/local hashing matched all six files in
each terminated job directory.

The jobs have no algebra-system checkpoint and cannot resume mid-basis.
They are nevertheless reproducible: a fresh run can be launched from the
already frozen exact packets and route runner.  The partial diagnostics are
also retained both in this local freeze and on the stopped EBS roots.

## Host-role audit and EC2 stop

At 23:27:07Z, then again immediately at 23:28:32Z, the exact DMI instance IDs
and boot IDs matched.  Box02 had load `0.00,0.27,0.68`; Box03 had
`0.00,0.49,1.29`.  Neither host had a live msolve, Singular, Sage, Magma, R4,
screen, or tmux process/session, and the only `ubuntu` processes were the
audit SSH session and its transient user manager.  There was no `ubuntu`
crontab.  Historical campaign directories `res32`, `jc72108`, and `stuck7`
were on the EBS root volumes, not instance store.

The exact control-plane targets were:

- Box02: `i-010201a5da47795c4`, Name `Box02`, `x2idn.32xlarge`, 128 vCPU /
  2 TiB; sole EBS mapping `/dev/sda1` -> 150 GiB gp3
  `vol-0cebacf798eef9350`;
- Box03: `i-0ece0b9a3b4a7512f`, Name `Box03`, `r6i.16xlarge`, 64 vCPU /
  512 GiB; sole EBS mapping `/dev/sda1` -> 200 GiB gp3
  `vol-0423e17152062425a`.

Both had null IAM instance profiles and API stop protection disabled.  Box02's
two 1.7 TiB instance-store NVMe devices were unmounted, had no filesystem
signatures under read-only `wipefs --no-act`, and held no registered artifact.
Box03 had no instance-store device.  Thus no needed ephemeral artifact was at
risk.

AWS accepted only those two instance IDs at 23:28:40Z.  Both now report
`stopped` with `Client.UserInitiatedShutdown`.  Their EBS roots remain
attached and `in-use`, so all root-volume data is recoverable by starting the
same instances; the public IPs will change.  `DeleteOnTermination=true` is
irrelevant to this stop because no termination occurred.  The blank Box02
instance-store devices are the only nonpersistent storage.

The stop released 192 vCPUs and 2.5 TiB of instance-class RAM.  Using the
fleet's current approximate on-demand figures, it avoids about $17.03/hour
($408.72/day) of compute while stopped; gp3 storage charges continue.

## Firewalls

This receipt consumes no modular or char-0 msolve `[1]` output and supplies no
certificate.  It does not change the exact-Q full-grade certificates or their
hostile review.  It does not decide the base ideals, the original
nonreduced scheme, formal arcs, compatible lifting, convergence,
algebraization, Keller maps, another support/valuation, a counterexample, or
JC2.  No canonical ledger, ideation file, unrelated host/process, or separate
formalization instance was edited, inspected, signalled, stopped, or
terminated.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6826`.
- Body SHA-256:
  `e4e856149fe2cf0df1e3a2a9ec12cb04daf099a25c3c5fe37298f12622daf5b8`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
