# BOUNDED REPLAY (≤ 45 min; a cross-check dataset for the running descent-partition theorem lane): under the printed fixed-list closure the parent row R063 has ONE actual-L complete configuration with I_M = 19 (corrected integrality table, frozen), while the earlier replay (frozen) computed a licensed-child value I'_M = 71/4 using the exact-contact child calculus. TASK: (1) using box/lib/descend_own.py (licensed descent, own child data) and the gate's printed-closure scripts (box/exact-contact-gate-20260906/: census_replay.py, closure_fixed.py) — do NOT rewrite the calculus — enumerate the CHILD's complete configurations under the same printed closure (actual centre stabilizer L', the child's own M'-list) for R063, and separately for R009 and R050; (2) for each child configuration compute I'_M and I'_m in BOTH conventions — unshifted, and with the ℓ-shift (ℓ = v_s − u_s − 1; Lemma 4.1's −c·t^{−ℓ−2}; Prop 4.6(3)*) — tabulating the two; (3) report: the number of child configurations, the values, whether the unshifted or shifted child value equals the parent's I_M (19 for R063; 8 for R009/R050), and whether 71/4 reappears in either convention; (4) type the result as DATA (a replay, not a theorem). FALLACY-v2. DISK DISCIPLINE: report + JSON ≤ 1 MB; no fleet. ≤ 50 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/r063-child-20260906/.
Report: xmodel/r063-child-pattern-grok46-20260906.md
Seal (<!-- BODY-END -->); 4-10KB; 50 min.
charged_input=xmodel/integrality-table-grok46-20260906.md
charged_input=xmodel/im-descent-replay-grok46-20260906.md
charged_input=xmodel/exact-contact-gate-astra-20260906.md
charged_input=box/lib/descend_own.py
charged_input=box/residual66-20260905/roster.jsonl
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/r063-child-pattern-grok46-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a6ff5bb912937b0eebbc74ed92949fffe9571150d33834c153605b6e4510110b  {{LANE_INPUTS}}/integrality-table-grok46-20260906.md
81dda41bebc3c88782eb94a3238ccf72ee982f18bf39e2edf0946104f3c8b473  {{LANE_INPUTS}}/im-descent-replay-grok46-20260906.md
cd0880f0a7c4122118f59e330f60830f9b2d772762ec346a970138858a62cedf  {{LANE_INPUTS}}/exact-contact-gate-astra-20260906.md
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
