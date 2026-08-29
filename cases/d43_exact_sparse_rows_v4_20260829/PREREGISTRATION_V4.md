# D43 exact a00pp row pipeline v4 preregistration

Status: **V4_REPAIRED_LAUNCH_NOT_AUTHORIZED** - review-frozen,
AWS-unregistered, and not launchable.

The review manifest has blank account, region, hostname, instance ID/type,
CPU count, instance-tag key, and tag value.  The live IMDSv2 preflight and
every compute entry point refuse it.  No AWS launch is authorized until a
fresh independent hostile review returns PASS **and** the coordinator issues
a separate GO.

## Host and registration requirements for a future launch

* Linux on Amazon EC2 only, with the exact registered account, region,
  instance ID, instance type, hostname, CPU count, and IMDSv2 instance tag.
* At most 1 TiB physical RAM (`MemTotal <= 1073741824 KiB`) with at least
  800 GiB available, at least 100 GiB free disk, and **zero swap**
  (`SwapTotal = SwapFree = 0`), continuously monitored.
* One pinned physical core per heavy side (`cpu_f=2`, `cpu_g=3`), explicit
  per-side address-space caps, and explicit whole-job aggregates:
  `MemoryMax = 962072674304`, `MemorySwapMax = 0`, `TasksMax = 512`,
  whole-job timeout 259200 s.
* `REGISTERED.json` must bind the manifest digest, operational-source-list
  digest, complete expected EC2 identity, tag key/value, run-directory tag,
  the sealed source-archive digest, and the external launcher digest.  Do
  not fill in or mutate this review manifest.

## Exclusive one-shot run protocol

1. The external hash-pinned launcher creates a fresh job namespace by
   atomic `mkdir` (the namespace lease) and acquires a nonblocking
   kernel `flock` on the host job lock, held for the whole job.
2. It verifies the sealed source archive against its pinned literal digest,
   safe-member census, embedded manifest replay in a fresh private
   extraction, then records `RUN_LEASE.json` with a 256-bit run nonce,
   launcher identity, and lock identity.
3. The supervisor is started under `setsid --wait` in **both** containment
   modes (inside the systemd user scope, or as the exact-session fallback),
   so it is the session/process-group leader in both; the sticky monitor,
   both side workers, the emitter, and all descendants run inside that one
   boundary.  The first side failure cancels and reaps its peer.
4. The sole authorized mathematical workflow is unchanged from v2/v3:
   preflight; concurrent independent f and g builds; matching-pair custody
   with same-host/different-PID/overlap proof; the literal collapsed-D21
   band-20 gate; then, inside the same process and manifest, emission of
   all 19 shards and the 184-row merge; then a non-authoritative finalize
   candidate.
5. Exactly one authoritative terminal object, `TERMINAL.json`, is published
   by atomic rename as the supervisor's last successful action, only after
   every payload, custody, orphan-census, resource, and archive-replay
   gate.  The terminal decision itself **recomputes or binds every
   payload-bearing candidate field**: it rehashes the lease, registration,
   manifest, preflight receipt, pilot gate, merge receipt, and merge
   payload on disk, cross-binds the semantic/template/inventory receipts
   under the rehashed merge receipt, contract-checks the preregistered
   `29+155=184` inventory (non-bool integers, bands `{20:10, 30:9,
   40:10}`, tail degree <= 2), validates the claim boundary against the
   rehashed manifest, resolves and rehashes the archive named by the
   sidecar, and records per-field provenance (`RECOMPUTED` vs
   `RECEIPT_CROSSBOUND`).  Every earlier artifact carries
   `terminal_authority: false`; every failure path leaves a single
   NO_VERDICT authority.
6. After the boundary exits, the launcher post-mortem census is
   **authority-bearing**: a positive terminal paired with a non-zero
   census rc or any survivor is voided by an immutable
   `TERMINAL_POSTMORTEM_FAULT.json` written beside the terminal (outside
   the sealed terminal archive, disclosed in the terminal's
   `post_boundary_contract`) and a non-zero launcher exit.  The terminal
   file itself is never modified or overwritten.

The preregistered inventory is a forecast that the pipeline **enforces**,
never measures: a run whose true inventory differs from 29 live / 155
exact-zero (bands `{20:10, 30:9, 40:10}`, tail degree <= 2) can only fail
closed to a NO_VERDICT; it cannot publish a different inventory.

No solve, candidate claim, or template claim is authorized.  A successful
future run can claim only the finite support-specialized raw-J row packet:
not a point, not the E/unit/template extension, not all-depth
compatibility, not a Keller map, and not a JC2 counterexample.
