# Input custody: pseudoplane-linear-u-gate-fable5-20260911

Lane inputs dir: `/tmp/jc2-lane.y7sd28/inputs` (four files, mode 0400).
First action 2026-09-11 08:27:49 UTC. Both owned targets absent at that time.

## Pre-pins (measured 08:27:49 UTC, before any body was read)

```
86741d44fb280d0e0498bae7fb18ce01505b2d75814f50ce3f14aaf507b0f3bd  pseudoplane-linear-u-submersions-astra-20260911.md
29298c37d2f1b4f487fbaa624069ea2dee5fa0b0fd52a001da08a22f87df02aa  pseudoplane-linear-u-submersions-astra-20260911.md.artifact.json
e042b696f3dce19fe116fddc4fed328bb066dee86ef539fd2f13f9055a0f87b7  pseudoplane-homogeneous-gate-fable5-20260911.md
347b7e38435237c8e2ca77d830bdac82ae2d702898c50786b928bbf2adc1b9ad  pseudoplane-homogeneous-gate-fable5-20260911.run.v2
```
All four matched the charged pins in the lane prompt before any body was
read. FALLACY-v2.md at the lane root hashed
`e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`, equal
to the fallacy_sha256 recorded in the parent run.v2.

## Administrative body check

`head -c 10042` of the Astra report hashes to
`4fc13293aa49b8c4444c4624c2d892ce837441500c76870ab19d15e765baf8fd`, equal
to the body SHA-256 in its Seal (body bytes 10042) and in the artifact
JSON (body_bytes 10042, body_sha256, source_sha256, full_sha256 86741d...,
file_bytes 10375, frozen basis 0d39df3c...). The 10042-byte prefix ends
with the standalone `<!-- BODY-END -->` line plus newline; each of the two
.md inputs contains exactly one such standalone line. The parent run.v2
records report_sha256 e042b6..., equal to the frozen parent file, with
report_state BODY_SEALED and seal_boundary CLEAN. The parent report itself
ends at its marker (no author Seal), as its lane contract declares. Byte
lengths: 106, 1, 273, 58 lines respectively; all read whole to EOF.

## Post-pins

Measured 08:33:39 UTC after report sections 0-8 were written:
```
86741d44fb280d0e0498bae7fb18ce01505b2d75814f50ce3f14aaf507b0f3bd  pseudoplane-linear-u-submersions-astra-20260911.md
29298c37d2f1b4f487fbaa624069ea2dee5fa0b0fd52a001da08a22f87df02aa  pseudoplane-linear-u-submersions-astra-20260911.md.artifact.json
e042b696f3dce19fe116fddc4fed328bb066dee86ef539fd2f13f9055a0f87b7  pseudoplane-homogeneous-gate-fable5-20260911.md
347b7e38435237c8e2ca77d830bdac82ae2d702898c50786b928bbf2adc1b9ad  pseudoplane-homogeneous-gate-fable5-20260911.run.v2
```
Identical to the pre-pins. The inputs directory is unchanged.

## Whole-read record

All four inputs were read whole by `cat -n` through EOF at 08:28 UTC with
no clipping (largest 273 lines). Only sha256sum, date, head, tail, od, wc,
grep, ls and cat were used; writes only via the designated apply_patch to
the two owned paths. No linked report, ledger, history, git, network,
subprocess, CAS or process control. Owned targets were absent at 08:27:49.
