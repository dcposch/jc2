# AWS custody

- Job tag: `ggv_endpoint_root_triple03_plants_r1_20260828T182118Z_i0f089`
- Remote namespace:
  `/home/ubuntu/jobs/ggv_endpoint_root_triple03_plants_r1_20260828T182118Z_i0f089`
- Host: `54.224.45.13`, hostname `ip-172-30-0-106`
- Instance: `i-0f089e64c378f5da3`, `r6i.4xlarge`, 16 vCPU, 128 GiB
- Assigned CPU: `7`; supervisor PID/PGID/SID: `20315`
- Supervisor start: `2026-08-28T18:22:41Z`
- Overall wall time: `8.89 s`; maximum RSS: `32,460 KiB`
- Singular wall time: `7.50 s`; maximum RSS: `12,408 KiB`
- Worker return code: `0`; supervisor swap-violation flag: `0`
- Swap total/free at preflight and final: `0/0 KiB`
- Post-terminal audit at `2026-08-28T18:26:30Z`: supervisor absent, PGID
  empty, swap total/free `0/0 KiB`

## Frozen source

- preregistration SHA:
  `ec00c47be59b9c0203e1bdabff96e15fe746d9ca5e58623488d7d4cd33652708`;
- source manifest SHA:
  `18a93ca0f261314b0a20d45299085eaedea450433407d5c67267ddf0d993996f`;
- source archive SHA:
  `d1edd4a2c4732b29e47ceea682fc0571b077155b6f8dd8485ba9df519805b9e4`;
- original root terminal input SHA:
  `1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787`;
- patch builder SHA:
  `7951eb67b9a858556b7f78e4bc2f304ce85c5783fd513eb27f2d2115dc736b50`.

The source tree was made read-only before execution. The producer ran under the
30-minute supervisor and 15-minute Singular hard caps, one pinned CPU, 96 GiB
virtual-memory and 32 GiB file limits, Linux/Amazon-EC2/IMDS/instance/hostname/job
tag gates, a hostile-diagnostic control, a clean reducer/saturation selfcheck, and
continuous zero-swap telemetry. The terminal archive was checksum-verified on AWS,
fetched intact, expanded, and replayed locally with hash/text checks only.

## Terminal custody

- terminal archive SHA:
  `db522621095ca392e65280fe18044924d8566de3e1f30acd0b9e419e0798419d`;
- remote checksum sidecar local SHA:
  `6693094c4cf9eefff3fdd99dafe3ab9c9b64e66ee2c9ed53ba527b0de42200e5`;
- post-terminal no-orphan/swap audit SHA:
  `96f06d0ac0a46c9856041ff7b4e61e113507488532d93430b3bd99f6fa77cf77`.
