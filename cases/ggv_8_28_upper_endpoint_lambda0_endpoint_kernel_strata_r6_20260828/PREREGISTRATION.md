# Preregistration: ambient-reducer/qideal adapter repair and pilot r6

Date: 2026-08-28

R2 through r5 remain adapter `NO_VERDICT`; none reached a full receiver
kernel. The r5 pilot showed that comparing a quotient variable directly to
zero is not a reliable Singular qring selfcheck marker.

R6 changes only quotient-ring validation. Before `qring`, it reduces the
exact branch factor by the exact standard basis and requires zero remainder.
After `qring`, it records `ideal(basering)` and requires that defining ideal
to be nonempty. The tiny positive control uses the same two checks. The
reserved-name/continuation mutation remains a required negative control.

The mathematical payload is byte-identical to r2 and is pinned separately by
`MATH_PAYLOAD.sha256`; its manifest SHA-256 is
`ecd5dba798ab3157f4bf362361b630744fbadfbfe582dbc0d85523f6183f33c6`.
No equation,
factorization target, chart, matrix entry, endpoint coefficient, branch
ordering, verdict rule, or cap changes. The exact endpoint remains
`E=x14*x72+x1*x97`; every diagonal and cross term is required. A nonzero
generic pullback is `PASS`; generic zero remains
`GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING`, never whole-component death.

The counted transform of frozen r2 compiler
`53ad2aa298b499d83c593171fb3da9c1dce39bfe7f924bf461db4887a8a6f578`
must be
`a5587996f3d9de7049fe5de790d9bd16a53fa389732016bc4642e2c02a7d0d11`.
The complete patched r2 selfcheck must be
`8850f6fa2eff28731a511f52da633f949835ce4f1a8dd36365e0700081411b93`.
The runtime worker must be
`e6f3ee2772bb3f6eb3d362c134769fc179414b2d7833f9174e1ad41949e31706`.

First launch only the P lane on r6a under
`ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a`. It must pass the
complete adapter selfcheck, base build, exact P irreducibility/factor census,
and full matrix parse before the other three lanes are released. The pilot
may continue into its exact P kernel.

Retain the four pinned EC2 identities, one core, 96-GiB address-space cap,
zero swap, 7,200-second process-group cap, exact source/runtime hashes,
continuous starttime custody, and final no-orphan census. Stop on every hash,
factor, parser, reducer, quotient-ideal, replay, resource, swap, or guard
disagreement. No inference from adapter failure, no sample extrapolation,
canonical edit, HENS mutation, or access outside the authorized jc2 tree.

Frozen r6 adapter source hashes:

```text
39d5ab116d8c14238446cd86b9a6ea237f8744f3333e90a51ceb681fa495480e  aws_preflight.py
5b6a0bce34e93fa9ebbafca2095a33e06f5696b915fcd772cc9d77e08f9d5222  aws_run_remote.sh
b952b9c5b38f49aaecdc258f3be2fbac0e959b41d28adc1dd18552732819ef0b  build_compiler_r6.py
7e69ae13aaf116313d628c29fa289db65365486ec2caf85635fddae38614917f  build_worker_r6.py
4e904f354a5b108c3993a7fd395dab06645f8a654d9dde5a875fbf00f9d4854b  selfcheck_strata_r6.py
```
