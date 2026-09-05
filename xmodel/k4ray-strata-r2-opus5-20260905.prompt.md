# COMPUTE lane, round 2 (finish the K=8 and K=9 β strata with the engine that works): round 1 (frozen) built all 27 strata charts (54 covers), found that msolve decides these ideals (4–900 s mod 32003; over Q on the smaller ones) where Singular std never finished, and closed K=7 b = 9..13 exact-Q; K=8 (b = 7..15, nine strata) and K=9 (b = 8..17, ten) are ALL open — every entry a named memory or wall-clock limit (b = 11 at K=8 has a q0-cover modular unit only); no NONUNIT anywhere. A K=8 sweep restores the D=108 no-split arm for all deg β; a K=9 sweep restores (99,66) configuration (A). TASK: (1) reuse round 1's charts and emitter (box/k4ray-strata-solve-20260905/: integral denominator-cleared generators, both covers per stratum); (2) launch 3 × r7i.16xlarge (512 GB) via `bash ops/fleet/fleet.sh launch 3 r7i.16xlarge` (wait installs msolve 0.10.1; TERMINATE all three before sealing) and dispatch, detached with 160-minute watchdogs and 400 GB address-space limits: msolve -t 32 modular F4 on every K=8 stratum first (both covers), then K=9, smallest first; for any modular UNIT run msolve over Q (-g 2) on the same integral generators immediately as the exact certificate; record for each run: input SHA, rows, variables, F4 degree reached, peak RSS, wall, rc; (3) also run the three open K=7 strata (b = 6, 7, 8) if capacity allows; (4) poll every 15 min; (5) VERDICT per K: DEAD for all deg β (all strata exact-Q unit, both covers) / the surviving list with the exact resource cause; any NONUNIT basis ⇒ dimension + sample point, reported loudly (necessary-chart survivor). FALLACY-v2 (a modular unit is a screen; the exact-Q [1] over the same generators is the certificate; I_light drops rows only). ≤ 200 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/k4ray-strata-r2-20260905/.
Report: xmodel/k4ray-strata-r2-opus5-20260905.md
Seal (<!-- BODY-END -->); 8-18KB; 200 min.
charged_input=xmodel/k4ray-strata-solve-opus5-20260905.md
charged_input=xmodel/k4ray-beta-strata-grok46-20260905.md
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k4ray-strata-r2-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
2af3e012dd4157669308f3855a22582967e2fffdc25cad3bf825b1050f25be4c  {{LANE_INPUTS}}/k4ray-strata-solve-opus5-20260905.md
689e3ed80af53c683a38c47ba666ca49151dbea2d6b451787fd74cb310d508ae  {{LANE_INPUTS}}/k4ray-beta-strata-grok46-20260905.md
a9da94d341a691942e9d6a6a6d90d97008b2d7baa1cadb2592481cf6b9c11c4c  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
