# D43 exact a00pp row pipeline v3 preregistration

Status: **V3_REPAIRED_LAUNCH_NOT_AUTHORIZED** - review-frozen,
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
3. The supervisor, sticky monitor, both side workers, the emitter, and all
   descendants run inside one containment boundary (systemd user scope, or
   the exact-session `setsid` fallback with JOB_TAG census and bounded
   reap).  The first side failure cancels and reaps its peer.
4. The sole authorized mathematical workflow is unchanged from v2:
   preflight; concurrent independent f and g builds; matching-pair custody
   with same-host/different-PID/overlap proof; the literal collapsed-D21
   band-20 gate; then, inside the same process and manifest, emission of
   all 19 shards and the 184-row merge; then a non-authoritative finalize
   candidate.
5. Exactly one authoritative terminal object, `TERMINAL.json`, is published
   by atomic rename as the supervisor's last successful action, only after
   every payload, custody, orphan-census, resource, and archive-replay
   gate.  Every earlier artifact carries `terminal_authority: false`; every
   failure path leaves a single NO_VERDICT authority.

No solve, candidate claim, or template claim is authorized.  A successful
future run can claim only the finite support-specialized raw-J row packet:
not a point, not the E/unit/template extension, not all-depth
compatibility, not a Keller map, and not a JC2 counterexample.
