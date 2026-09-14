# Input custody: pseudoplane-homogeneous-gate-fable5-20260911

Lane: Fable 5.1 hostile proof review of the exact homogeneous pseudo-plane
obstruction. Reviewer model claude-fable-5-1. Owned files: this record and
`xmodel/pseudoplane-homogeneous-gate-fable5-20260911.md` only.

## Pre-pins (measured 07:51:28 UTC, before any body was read)

Inputs at `/tmp/jc2-lane.LM8wRa/inputs`, mode 0400, sizes 9204 and 681 bytes.
```
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```
Both matched the charged pins exactly. Both owned targets were absent at
07:51:28 UTC (ls returned no such file for the report and the box dir).

## Whole read

Root report read whole, lines 1-197 through EOF, in two contiguous sed
ranges (1-60, 60-197) with the final bytes shown by od; last line is the
Seal frozen-basis line ending in a newline. Artifact JSON read whole (one
line). FALLACY-v2 guardrail read from the adapter-supplied prompt. No
other file was opened; the four older linked reports were not opened.

## Administrative seal cross-check (sha256sum/head only)

`head -c 8872` of the root file hashes to
`5b902bf2160b41b52f7dbef72cecd1a1ddfb99daa0d83190151ab4cf6aa690b2`
and ends with the root's standalone body-end marker line plus newline.
This equals the
Seal body SHA-256 and the artifact JSON body_sha256 / source_sha256;
body_bytes 8872 and file_bytes 9204 agree with wc. Frozen basis
`0d39df3c9fd69c939a8420c54d03228b9077777d` is recorded, not verified
against git (git access not permitted in this lane).

## Post-pins

Measured 07:58:23 UTC after the report body sections 1-8 were written,
before section 9 and before the marker:
```
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```
Identical to the pre-pins; input files unchanged (mode 0400, same sizes).
Own whole readback of both owned files was performed by cat immediately
after this line was written and before the marker append. COLLISIONS
(own-only): none; both owned targets were absent at 07:51:28 UTC and no
other path was created or modified by this lane.

## Method statement

Static text and manual mathematics only. No subprocess, CAS, code, test,
network, git, AWS, SSH, or process control. Writes only through the
sanctioned apply_patch binary, each under 1500 words. The adapter owns the
Seal, charge_basis, and artifact transaction; none were authored here.
