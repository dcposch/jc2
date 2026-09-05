# SWEEP lane (harvest every cheap kill in the OPERATIVE residual with the certified pipeline; produce the explicit hard-row list): box/lib/census_sweep.py (frozen census-sweep report: exact-Q only, source-complete charts through the fixed builder, negative control passes, wall ≈ 67 unknowns for real order charts) has so far been run on 19 census classes. TASK: run it on the OPERATIVE rows only — the 1,420 rows with C_FULL_TREE_POLYNOMIAL_ODE ∧ XU (16 ≤ n ≤ 200; the partitions in box/child-data-20260905/ and box/scopeleaks-20260905/: 174 live u_s=1 rows + 310 u_s ≥ 2 rows after (C-TOP) and the U-NEG kills; also include the 936 (C-TOP)-killed rows as a SEPARATE tier since (C-TOP) is still under gate) — grouped into source-complete classes, sorted by unknown count. (1) For every class with nunk ≤ 100: emit + solve exact-Q with a 300 s watchdog per fibre, on the fleet in parallel (launch up to 6 c7i.4xlarge workers via fleet.sh; dispatch.sh; TERMINATE them before sealing); msolve modular first as a screen, exact-Q confirmation for any unit; (2) for split (mixed) classes, only the unsplit fibres can die by the order chart — record split fibres as OPEN with their (ρ,λ) leaf count from box/split-window-20260905/ (tool box/lib/split_window.py) rather than pretending; (3) TALLY: per tier (174 live u_s=1 / 310 u_s≥2 / 936 C-TOP-killed), classes DEAD (exact-Q) / OPEN-compute (nunk, equations, wall time) / OPEN-split; the hard-row list = every operative class not dead, with nunk and the reason; (4) SANITY: re-run the tame-automorphism negative control and the two J≡0 controls through the same code path in this run. Certificates to box/operative-sweep-20260905/ in the census-sweep-class-certificate-v1 format. FALLACY-v2 (a modular unit is a screen; a class is DEAD only if every fibre is exact-Q UNIT on the full necessary chart; never transport an old-chart unit). ≤ 200 min; no ledger edits; no jc2-lean; no ideation-*.
Report: xmodel/operative-sweep-grok46-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 200 min.
charged_input=xmodel/census-sweep-grok46-20260905.md
charged_input=xmodel/child-data-tests-opus5-20260905.md
charged_input=xmodel/scope-leaks-opus5-20260905.md
charged_input=box/lib/census_sweep.py
charged_input=box/lib/split_window.py
charged_input=box/lib/guided_gb.py
charged_input=ops/fleet/fleet.sh
charged_input=ops/fleet/dispatch.sh
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/operative-sweep-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
58146fdb40740b9491b7d0390f8f8b38b164bfffba83b81d00e0f5972fc1e404  {{LANE_INPUTS}}/census-sweep-grok46-20260905.md
219faa47b435222511168ffaa1cc4f0c33be7744209a29626999f464d66c9cff  {{LANE_INPUTS}}/child-data-tests-opus5-20260905.md
c3dd95b11ea3e12ba88e813860ecab703a275f745ce429944c8aeb04a5095eda  {{LANE_INPUTS}}/scope-leaks-opus5-20260905.md
700bfeb07ceb84d9afcaa7504f7007c5a285a9f78bae0623e5ff2c790f7af206  {{LANE_INPUTS}}/census_sweep.py
be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd  {{LANE_INPUTS}}/split_window.py
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
c0ea96034bf12b7445aa123f00cf600baaca81751f36a91855987f44fd6311e3  {{LANE_INPUTS}}/fleet.sh
dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599  {{LANE_INPUTS}}/dispatch.sh
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
