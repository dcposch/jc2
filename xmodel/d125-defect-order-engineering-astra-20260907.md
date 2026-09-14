# D125 defect order: actual engineering controls

Status: **TERMINAL ENGINEERING PASS**, 2026-09-07 02:04:08 UTC. All six registered capped jobs completed as expected; all seven owned process groups were freshly absent at 02:05:43. This is instrument evidence only, not a decision of the D125 ideal. No complete-client coefficient parsing/arithmetic or full solver was run.

## Authorized scope and frozen custody

Root explicitly authorized only tiny engineering on i-0da0cebfc97c9fd54, new boot `375d1a40-5988-4999-8cb7-a5427ad3b3a0`. Fresh SSH checks confirmed Linux, Amazon EC2 DMI, that exact instance/boot, `/dev/nvme0n1p1` ext4 mounted `/`, EBS serial `vol0eb6450d18ffa89f1`, and absence of the fresh destination. Before writes there were 20191297536 free disk bytes, 257467752 KiB available memory and no swap. Root supplied the fresh EC2 Owner/volume audit; this task made no EC2 state/tag changes.

Only `/home/ubuntu/d125-defect-order-solver-20260907/` and its `engineering/` subdirectory were created remotely. Frozen driver `944d5a840b6e4a81e89e5bcfa0ce6e6e54684ece70f182499735b9aa8571faec`, exact checker `f452a1f6a3dfcc534a14a0d2b1f162589fc928973aff5a91f7faaa88921039af`, helper `d5031c04fc7fdfec1fc57285b7538747b4d0aae25fae5ac140439d01dbd99ca3` and CAPRUN `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2` were deployed unchanged into fresh files. The retained Singular binary matched `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.

The registration and engineering harness were frozen **before first execution**, at hashes `4a2566914d1ea0a372387e0306988b3dd6ea22c154764ee72691a77a26f0b8f8` and `4600cddd7d5cb69cd9f1c1fb658bacaf936596c9a9a09c3efb34069f0f52bade`. Neither changed afterwards. Their manifest is `frozen-inputs.json`, SHA `8cb1f9ef04fa5f213622580a7a0ee29ac9781b6bbede007513e7e9d1c0383db8`. Every payload validated instance/boot/cwd/EBS and frozen code/registration pins before its arithmetic. The whole old terminal harness and 1198-line pinned runner were reread; no live gate artifact was accessed.

## Actual results

The single batch ran from **02:04:06.419263 to 02:04:08.103702 UTC**, 1.684446 seconds wall. Each engine/replay job had a 10-second wall and inherited per-process CPU cap, 512-MiB AS and sampled exact-group RSS, 64-MiB inherited per-stream FSIZE and core zero. The special no-CAS RSS control used a 64-MiB group threshold. No previous 161-term or file-overflow control was repeated.

| job | PID=PGID | start ticks | wall seconds | outcome |
|---|---:|---:|---:|---|
| descendant RSS | 1740 | 39964 | 0.567680 | expected RSS cap; TERM then KILL; reaped |
| three-a levels | 1760 | 40028 | 0.180206 | NORMAL_EXIT/0 |
| weighted graph | 1768 | 40052 | 0.122808 | NORMAL_EXIT/0 |
| six-column control | 1776 | 40075 | 0.066165 | NORMAL_EXIT/0 |
| actual replay normal | 1781 | 40089 | 0.066075 | NORMAL_EXIT/0 |
| actual replay -O | 1787 | 40102 | 0.236608 | NORMAL_EXIT/0 |

Controller PID=PGID1736/start39955 ran in `session-9.scope`, PID namespace `pid:[4026531836]`; the recorded RSS descendant was PID1743/start39969 in PGID1740, same cgroup/namespace. It ignored TERM and outlived the original group leader. CAPRUN revalidated the unreaped leader identity before both signals, then reaped it and observed no live group member. Its intentionally sampled RSS reached 167411712 bytes, illustrating sampling overshoot rather than an exact 64-MiB ceiling. All other jobs' maximum observed group RSS was below 22 MiB. Normal-path telemetry's default `leader_reaped=false` is not a failure: its authoritative wait completed, return status is recorded, and final exact-group absence was checked.

**Actual ordering:** Singular accepted three successive `a(...)` rows followed by dp on x,y,z,t,u with weights `(2,1,2,2,2)`, `(1,0,0,1,0)`, `(1,0,0,0,0)`. The global attribute was 1. Leaders of `x+y`, `x+z`, `x+t`, `y^2+z`, `z+u` were exactly **x,x,x,y²,z**, separating W1/W2/W3/degree/reverse-lex comparisons. Output was exactly 38 bytes, empty stderr, SHA `2f271f26e451fac773264d61ebdd4c3404e0908a47b2ec9a9bf617f63f1aa9c2`.

**Actual weighted graph:** with first weights (3,1,4), remaining rows (1,0,1),(1,0,1), the frozen footer ran one tiny slimgb on `I=(x-y^2,z-y^3)`. The complete actual indexed I and G each contained those same two polynomials; there was no T block and the terminal frame was NONUNIT. The exact weighted verifier checked all S-polynomials, NF(1) and both original equations. Output was 233 bytes, empty stderr, SHA `ef8e6a5696951f5503888638d6170ec39c9efa9046ae108284d3a4a3f808e85b`. The source/fixture digest was `6a6a15d02aca9f67e64ac2c6b1065560eb9befd8fa88d13bb2d9c90b4ac599af`; its three-variable order digest was `cbb4eea4ca46754d038a147ee07481a8bfbcfc769c419215a8abc548450bbdcf`, deliberately not the 269-variable production descriptor.

**Actual index/cofactor control:** the new driver's engineering authority executed its retained six-column fixture `I=(0,x,0,x,1-x,0)`. It printed `size(I)=3`, six indexed columns, and six cofactors `(0,0,0,1,1,0)`. Exact mapping to original indices was `(0,1,0,1,4,0)`, and the original-row identity equals 1. Output was 295 bytes, empty stderr, SHA `fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922`, identical to the previously accepted fixture output.

Both remote normal/-O replays accepted the actual graph/cofactor output. A real changed graph-header byte string substituting the dp digest was rejected. Replacing the actual parsed cofactor vector by zeros was rejected by the original-row identity check. All output/control failures would stop the batch; there was no failed job, repair, retry or enlarged run.

## Terminal harvest and replay

At **02:05:43.131928 UTC**, read-only custody confirmed the same instance/boot/EBS and absence of PGIDs **1736,1740,1760,1768,1776,1781,1787**, including all launchers in the controller group and the orphan descendant group. The final available memory was 257433836 KiB, swap zero, free disk 20190998528 bytes.

All **49 remote files, 161942 bytes**, were copied to `box/d125-defect-order-engineering-20260907/evidence/`. `remote-custody.json` records every relative path, byte count and full hash; the portable local replay verified all 49 copies normally and under -O, then replayed the actual tiny graph and index certificates. Its resource limits are 30-wall/25-CPU seconds and 512-MiB AS. Replay with:

`python3 -I -B box/d125-defect-order-engineering-20260907/root_replay.py`

and the same command with `-O`. No CAS or remote call is made by this replay.

Key custody pins:

- `remote-custody.json`: `f9a1b62d4ef67855c126d963a967693901f72e5ea499c1da95c7b464f051002b`.
- `root_replay.py`: `f388d9ec0bb2ebd3209c0eea03c78aa722c14cdec952a4aa5cd2586417e1faec`.
- `local-replay.json`: `6d521e822732994a2f7bf3d8dd4c62de8dd7512d6e3ec70a2633dcae5f43d008`.
- Read-only `harvest.py`: `00456175026c125df9373abde0b7c8416015a3ff74b84da6821565b14783ddea`.
- Remote/evidence `engineering/batch.result.json`: `0f1fd24e35998ae9cfecb75d6ba83f6fcc8b0913de833dc3310f0caf7bad902c`.
- `engineering/terminal-jobs.json`: `19263da6da781da6ac22209346482000134c3cb23cb76eb00c792c6908cdb6a3`.
- `engineering/rss.telemetry.json`: `840bec1eb8c8069b2e193deb405d5af7bd9331920b0ee7d558170e1211e806f0`.
- `engineering/post-pins.json`: `aeb0d59acd418cab09ffdf0edc1566cb309a78c4631529784fda5c1a2ca182e5`.

The original full-source files were **hashed only**, before and after: JSONL `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`, Singular `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`, unchanged. No old artifact was overwritten. No W4/W5, expanded reconstruction, alternate algorithm, source gauge, protected project, shared ledger, live independent gate or other worker was consumed/changed.

**Scope limit:** actual small-engine ordering and serializer/checker controls are now evidenced. The complete 269-variable order/client has not been imported or solved in this task; small fixtures do not certify an arbitrary complete stream or its mathematical decision. Independent code acceptance and a fresh full-solver GREEN remain root decisions. Root retains the running instance and its EBS sole complete sources; no STOP/terminate authority was exercised. **All writers terminal; STOP/IDLE.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8344`.
- Body SHA-256:
  `d2b36e7e265aeb0e7275dc69bb6edddffc9486409ad28e00cb41905464ee078e`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
