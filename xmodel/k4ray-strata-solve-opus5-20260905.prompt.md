# COMPUTE lane (finish the k=4-ray β-strata by brute force with real watchdogs; the charts exist): the frozen beta-strata report built per-stratum I_light charts for the residual band b_min < b ≤ b_max (K=8: b = 7..15, nine charts; K=9: b = 8..17, ten; K=7: b = 6..13, eight) with the LEVEL-4 top band parametrized by two scalars and the lower β-block the exact box (no unknown dropped), but could only run 10-minute exact-Q solves — all INCONCLUSIVE_TIMEOUT. A UNIT on every K=8 stratum restores "D=108 no-split arm DEAD for all deg β"; on every K=9 stratum, "(99,66) configuration (A) DEAD for all deg β". TASK: (1) take the charts from box/k4ray-beta-strata-20260905/ (verify each chart's construction against the report §2–3 and pinned_chart.py; confirm no weight-floor drop of unknowns; record sizes); (2) launch 4 fleet workers (`bash ops/fleet/fleet.sh launch 4 r7i.8xlarge`; Owner tag is automatic) and dispatch ALL 27 strata (K=8 first, then K=9, then K=7) detached via ops/fleet/dispatch.sh with 150-minute watchdogs: for each stratum run guided_gb exact-Q (box/lib/guided_gb.py: Hilbert-hinted modular+CRT std, control battery) AND msolve modular (screen) in parallel; poll every 10 minutes; (3) any modular UNIT ⇒ exact-Q confirmation (or the rational identity) before it is called a kill; record custody per stratum (chart SHA, variables, generators, order, solver, rc, wall, RSS); a NONUNIT basis ⇒ dimension + a sample point (the stratum SURVIVES the necessary chart — report loudly, typed as survivor of a necessary chart, not a counterexample); (4) at the end TERMINATE the four workers and report the per-K verdict: DEAD for all deg β (all strata UNIT, exact-Q) / list of surviving or timed-out strata. FALLACY-v2. ≤ 220 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/k4ray-strata-solve-20260905/.
Report: xmodel/k4ray-strata-solve-opus5-20260905.md
Seal (<!-- BODY-END -->); 10-20KB; 220 min.
charged_input=xmodel/k4ray-beta-strata-grok46-20260905.md
charged_input=xmodel/support-regression-gate-opus5-20260905.md
charged_input=box/k4raypinned-20260903/pinned_chart.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/k4ray-strata-solve-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
689e3ed80af53c683a38c47ba666ca49151dbea2d6b451787fd74cb310d508ae  {{LANE_INPUTS}}/k4ray-beta-strata-grok46-20260905.md
e08f6e40f817e5bf354073e0fb685b4e6b3625c6a7442b1d90ac6ef4dffa0990  {{LANE_INPUTS}}/support-regression-gate-opus5-20260905.md
eed2cdf5cc5b85e3358013416bca7f6f6bd272138533ff0c065a86afb4c47e43  {{LANE_INPUTS}}/pinned_chart.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
