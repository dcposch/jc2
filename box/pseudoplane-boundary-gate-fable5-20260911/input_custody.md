# Input custody: pseudoplane-boundary-gate-fable5-20260911

Lane: Fable5.1 FIRST static review of two all-degree critical-point obstructions.
Actual first action 2026-09-11 08:44:54 UTC (date -u). At that instant the owned
report xmodel/pseudoplane-boundary-gate-fable5-20260911.md and the owned box were
ABSENT (ls: No such file or directory). ROOT prep 08:42:40 UTC; latest launch
08:48; original reserve 08:58 / HARD 09:01 UTC, never reset.

## Prepins 08:44:54 UTC (sha256sum, /tmp/jc2-lane.q7WBvV/inputs, mode 0400)

Exact match to the charged manifest, verified BEFORE any body was read:

```
d9bb20f83678cde429f04a1f4a175b013d31be2b92ccdb87d6b98ad3edc24265  pseudoplane-boundary-submersion-test-astra-20260911.md
41a6621fa7a94cad2e87e1706215b2468f459e989417c23d831b2ebc8b553132  pseudoplane-boundary-submersion-test-astra-20260911.md.artifact.json
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```

Sizes 9853 / 710 / 9204 / 681 bytes; 97 and 197 lines for the two reports.

## Fresh WHOLE reads

Both reports read FRESH_WHOLE through EOF including the Seal (last line 97 and
197 respectively, one clipping-free read each); both artifact JSONs read whole.
JSON body_sha256/body_bytes equal the Seal lines: ad29886d…2162c / 9521 for the
Astra report, 5b902bf2…690b2 / 8872 for the ROOT report; frozen_basis
0d39df3c9fd69c939a8420c54d03228b9077777d on all four. FALLACY-v2 guardrail was
supplied in the assignment text. No linked reports, mutable ledgers, live author
bytes, network, git, other agents or any subprocess were consumed.

## Postpins and own readback

Postpins 08:50:36 UTC (sha256sum output, byte-identical to the prepins):

```
d9bb20f83678cde429f04a1f4a175b013d31be2b92ccdb87d6b98ad3edc24265  pseudoplane-boundary-submersion-test-astra-20260911.md
41a6621fa7a94cad2e87e1706215b2468f459e989417c23d831b2ebc8b553132  pseudoplane-boundary-submersion-test-astra-20260911.md.artifact.json
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```

Own WHOLE readback 08:50:36 UTC, BEFORE the marker (report complete, 48 lines,
10667 bytes, grep count of BODY-END = 0; read whole via cat, no clipping):

```
d1e34bb0e582113f30da921eca321c669a0b119ded29f7c9f6f0f7aa4e9a18ed  xmodel/pseudoplane-boundary-gate-fable5-20260911.md (pre-marker)
c43bbfff3ff9ff1fe312d2a843e74e45bcd4c7bfd226574e77c6d09935c8293a  box/pseudoplane-boundary-gate-fable5-20260911/input_custody.md (before this section)
```

Writes: four apply_patch transactions (custody add, report add 822 words, report
append about 690 words, this custody update), each under 1500 words; the fifth
and last write is the single standalone marker line appended to the report.
No author Seal, charge_basis or artifact transaction; the adapter seals.
Own-only COLLISIONS: NONE. ALL WRITERS IDLE after the marker.
