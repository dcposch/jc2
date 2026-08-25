# AWS replay custody

- Host: `box02` / `ubuntu@34.203.207.55`
- Job tag: `as_residue_collision_20260825T101544Z_v2`
- Remote path:
  `/home/ubuntu/jobs/as_residue_collision_20260825T101544Z_v2`
- Source archive SHA-256:
  `e8b7fdb432d3f2359bb3025f328334210dcea79ca4c7e39cf766009d12422d8e`
- Remote archive verification: `source.tar.gz: OK`
- Replay return code: `0`
- Replay stdout SHA-256:
  `e2b2c52d2e2999de7c1143e2ff7095be0dd2ab4971639eb42b10f47a4eac0ba9`
- Replay stderr SHA-256:
  `955aa69df2bde795e2a4fe77bc2c96862e7af4d9e556c26417a3c787e09d5bd4`
- Canonical JSON payload SHA-256 (printed inside stdout):
  `af559486c32de48a2d814f69a9e338e9a0269be55d1918e11a0127714a6038e2`
- Maximum resident set size: `14516 KiB`
- Wall time: `0.02 s`
- Host stdout endpoint:
  `PASS-AS-RESIDUE-BALL-COLLISION-CONTROLS`

Exact remote command after archive verification and extraction:

```sh
/usr/bin/time -v python3 \
  source/cases/as_fonly_residue_ball_collision_20260825/replay_controls.py \
  > replay.stdout 2> replay.stderr
```

The archive emitted harmless macOS extended-header warnings during remote
extraction.  They do not alter the extracted payload; every extracted source
file hash is preserved in `SOURCE_FILES.remote.sha256`.

The earlier two-ball run at
`/home/ubuntu/jobs/as_residue_collision_20260825T101258Z` is preserved in the
files carrying the `two_ball` infix.  It was mathematically valid for the
first two balls but was superseded before freeze to include the independently
requested third `x=2` residue ball.
