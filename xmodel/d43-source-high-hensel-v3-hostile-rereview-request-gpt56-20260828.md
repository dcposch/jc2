# Independent hostile rereview request: D43 high-Hensel v3

Date: 2026-08-28  
Producer exclusion: the reviewer must not be the producer of this v3 packet.  
Required verdict: **PASS, REPAIR, or FAIL**.  
Execution restriction for this review turn: **no AWS, no p3+, no local CAS or heavy real D43 replay; bounded light tests only**.

## Sealed review target

- packet: `cases/d43_source_high_hensel_v3_20260828/`
- source seal manifest SHA-256:
  `76fbd4f0c723ecafe7030fc9ba0186478cdcffb2678f3d0fe868a67a500b43bc`
- payload manifest SHA-256:
  `8a859fc8cdc3001c15bd762e4ffd759eaf0372e16c8a3dbcbf36ed00bf769664`
- preregistration SHA-256:
  `091a6ee2ffeed389b9fcd96ec8c82e01fcdeeb26582e05c690ff6ae50e5f2dab`
- producer report:
  `xmodel/d43-source-high-hensel-v3-repair-gpt56-20260828.md`
- producer report SHA-256:
  `e41375d8abc2bb34041aad5e57ff9869b9852697cbca40f8c489f5f17490c32e`
- repair charge:
  `xmodel/d43-source-high-hensel-hostile-review-gpt56-r2-20260828.md`
- repair-charge SHA-256:
  `e12490ff6d117c8c6baa0a6ce925aa2da291dbb165d2016c8211a8a48b4f4f8b`

Replay both packet manifests and the producer-report sidecar before reasoning.
Do not modify any producer artifact.

## Required adversarial audit

Charge every R2 blocker and the subsequent AWS attack evidence.  In particular:

1. Prove or refute that `directionb_core23_p105337.ms` is in the executable
   payload, deterministic source archive, private execution path, and semantic
   state dependency chain.  Look for any other unsealed data open in the exact
   real context call graph.  Treat the unrun real open trace as an explicit
   runtime gate, not as evidence already obtained.

2. Attack the D21 loader with `DIRECTIONB_STATE`, a pre-existing host `/tmp`
   file, symlinks, TOCTOU, persistent IDs, forbidden pickle globals, malformed
   `Fraction`/`K3` graphs, and alternate legacy loader entry points.  Determine
   whether imports can load ambient data before the v3 in-memory patches.

3. Audit the corrected real fixture line by line.  It must use
   `(deterministic_p2 + p*k) mod p^2`, first prove all 184 rows and the
   E/W/E5/E6 gate, then fail specifically at semantic replay.  Check the two
   deleted/changed history point-hash mutations.  Do not count prior v2 AWS
   evidence as a v3 run.

4. Try to self-authorize with caller-selected hashes, a forged parent marker,
   a stale/replaced EC2 tag, a different AMI/instance/job/target, a modified
   review report, or a modified manifest/prereg/supervisor/worker/source
   archive.  Verify that the immutable preregistration never changes status
   and that only a live IMDSv2 instance-tag hash of a complete external PASS
   authorization can enable p3+.

5. Attack the runtime boundary with relative/symlinked interpreters, `PATH`,
   `BASH_ENV`, shell profiles, loader variables, Python path/user site,
   runtime-manifest omission/extras, NumPy version/tree/BLAS drift, Bash drift,
   and marker-path/hash self-reference.  Check that the normalization sentinels
   do not permit two actual environments to share authority incorrectly.

6. On static and bounded synthetic fixtures, attack systemd/cgroup custody:
   duplicate supervisors, concurrent workers, setsid, double fork, reparenting,
   PID reuse, cgroup migration, namespace escape, unit replacement, delegated
   controllers, weak cgroup permissions, child survival between the main and
   validation runs, supervisor memory, task limit, RLIMIT, OOM group behavior,
   host/cgroup swap, timeout, signal, and monitor death.  Verify that the exact
   root-owned unit contract actually prevents cgroup escape and covers the
   supervisor itself.

7. Attack every terminal phase: pre-run faults, existing run-dir collision,
   partial state, worker failure, timeout/OOM/SIGKILL, containment failure,
   report parse, state semantic replay, state snapshot, telemetry stop,
   manifest creation, archive creation/replay, sidecar, and atomic authority
   promotion.  Check the systemd `ExecStopPost` semantics.  No fault may leave
   a positive authoritative terminal; provisional positive wording is
   forbidden; `TERMINAL.json` must be create-if-absent and published last.

8. Deeply compare the main report, final state envelope/payload/history,
   necessary gate, exact target, scope/claims, main marker, fresh validation
   marker/report, source archive, and terminal.  Specifically test completed
   N64 validation—the inherited v2 ordering bug must be gone.

9. Attack the separate N16-to-N64 chain.  A target-64 authorization and job
   identity must bind the exact N16 terminal authority, manifest, archive,
   state envelope/payload/history, N16 authorization, job identity, achieved
   exponent, and normalized environment.  No N16 global status or mutable
   state path may authorize N64.

10. Recheck mathematical wording.  The finite runner enforces only the 184 raw
    source rows plus the listed coefficient/template-necessary gates.  It must
    not claim the assembled 218 rows, parked/source equivalence, a full
    residue-A/template/D25 point, branch survival, indefinite lifting/formal
    smoothness, Z_p/characteristic zero, a formal germ, a Keller map, or JC2.
    Verify the 190 -> 182 census, rank 129, p2 anchor, E/E5/E6 localized
    equivalence qualification, and exact slot-42 support argument.

11. Check preregistration/implementation consistency, including exact forbidden
    claims, stop conditions, resource values, target tags, source-archive
    construction, manifest/prereg noncircular metadata handling, the inactive
    templates, and the read-only nature of `preflight_v3.py`.

## Required report

Write a new versioned hostile-rereview report under `xmodel/`, add a SHA-256
sidecar, and give one explicit verdict.  A PASS must state residual assumptions
and the **exact first authorized AWS action**—including whether the corrected
real p2 fixture/open trace must run before N16—and must retain all finite-scope
warnings.  REPAIR must identify executable counterexamples or precise missing
bindings.  No AWS launch is authorized by this request or by the producer
packet.
