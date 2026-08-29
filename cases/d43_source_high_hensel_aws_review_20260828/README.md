# D43 schema-v2 corrected real-kernel diagnostic

UTC: 2026-08-28T20:23Z--20:29Z  
Lifecycle: independent diagnostic evidence; **packet verdict remains REPAIR / no target-16 launch**

This bounded AWS replay tested the defect that invalidated the schema-v1
resume state: an alternate valid `p^2` point obtained by adding `p` times a
nonzero tangent-kernel vector to the deterministic `p^2` lift while retaining
the old digit history.

The host was EC2 instance `i-02cb2b4a379ffcc64` (`r6i.4xlarge`), hostname
`ip-172-30-0-34`.  Every attempt was pinned to one core and ran with no
configured swap.  The isolated environment was Python 3.12.3 and NumPy 2.1.3.
The source tar SHA-256 was
`6c81db51fe0b6dca5ea83f97aca1e312c97851eca00e02f110cb8115fdce147f`.
This was a review diagnostic under `ops/aws_exact_lane.sh`, not a target-16
run and not a promotion-grade execution of the route-specific supervisor.

## Attempts

1. `...T2020Z`: **NO_VERDICT**, stopped before reconstruction because the
   base worker lacked NumPy.
2. `...r1_...T2024Z`: **NO_VERDICT**, after installing NumPy the fresh
   payload failed on missing `cases/directionb_core23_p105337.ms`.  That
   runtime input is absent from
   `cases/d43_source_high_hensel_aws_payload_20260828.sha256`.  Its local and
   temporarily supplied remote SHA-256 was
   `0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf`.
   This proves the sealed payload is not transitively closed.
3. `...r2_...T2025Z`: after supplying only that missing input, the packet's
   opt-in test ran the real reconstruction but failed before calling the
   validator.  Its call to `apply_digits(p2_coordinates, ..., step=p)` first
   reduces the deterministic coordinates modulo `p`; it therefore constructs
   `base + p*k`, not `deterministic_p2 + p*k`.  The inhomogeneous Newton
   correction is lost, so the asserted 184-row replay correctly fails.  This
   fixture does not test the claimed attack.
4. `...r3_...T2028Z`: independent checker
   `xmodel/d43-high-hensel-v2-real-kernel-shift-check-20260828.py`, SHA-256
   `7d58174e73e30612cfda3354dee546cb7eed108e63fd8223364321916359185d`,
   constructs the attack correctly.  Free column 67 gives 16 nonzero kernel
   digits.  The shifted point differs in 16 coordinates, satisfies all 184
   raw rows modulo `p^2`, and still passes the exact `E`/E5/E6/unit gate.
   Schema v2 rejects it specifically with
   `semantic state-chain replay mismatch`.  The run returned rc 0 in 7.45 s,
   used 210,988 KiB maximum RSS, and recorded zero swaps.

Thus the semantic-chain repair itself passes the corrected real attack.  Two
launch blockers remain: repair the packet's opt-in fixture and close/hash all
transitive runtime inputs in the AWS payload.  Neither issue invalidates the
previous finite `p^2` point, and no `p^3+` computation was attempted.

