# AWS custody

- Host: `box02` / `ubuntu@34.203.207.55`
- Tag: `as_residue_collision_repaired_20260825T103915Z`
- Remote path:
  `/home/ubuntu/jobs/as_residue_collision_repaired_20260825T103915Z`
- Source archive SHA-256:
  `25661c847fa80dfbec331e7a177ac32809a587b382d68bb406f6bd8f9c1a9696`
- Remote archive check: `OK`
- Return code: `0`
- Stdout SHA-256:
  `e2b2c52d2e2999de7c1143e2ff7095be0dd2ab4971639eb42b10f47a4eac0ba9`
- Stderr SHA-256:
  `aa5e98ea35862131c53dec7a13816efed3f73b9f3e925cd56a2e6c1e71946119`
- Maximum RSS: `15584 KiB`
- Endpoint: `PASS-AS-RESIDUE-BALL-COLLISION-CONTROLS`

Exact command:

```sh
/usr/bin/time -v env JC2_ROOT="$JOB/source" python3 \
  "$JOB/source/cases/as_fonly_residue_ball_collision_repaired_20260825/replay_repaired.py" \
  > replay.stdout 2> replay.stderr
```
