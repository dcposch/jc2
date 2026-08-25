# AWS replay custody

- Host: `box02` / `ubuntu@34.203.207.55`
- Job tag: `as_residue_collision_20260825T101258Z`
- Remote path:
  `/home/ubuntu/jobs/as_residue_collision_20260825T101258Z`
- Source archive SHA-256:
  `ff87503b1a994b2c1a1c996c74f6812391665a49625e03b8995bd0f91a0a465b`
- Remote archive verification: `source.tar.gz: OK`
- Replay return code: `0`
- Replay stdout SHA-256:
  `494d325782b0f1402e1cd440dda090d6e5da2f36164c19628935083ae14519d4`
- Replay stderr SHA-256:
  `8ce63bec9a93b4f11bdf37f9ffe0650d7c93b0d899b343af31dbfd417e008f55`
- Canonical JSON payload SHA-256 (printed inside stdout):
  `4ec692abf2ccc5e6c19d443b15054a1cae0c7a05de0faf741867846b8973ea73`
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
