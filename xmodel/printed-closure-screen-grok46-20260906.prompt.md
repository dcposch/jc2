# BOUNDED DATA SCREEN (≤ 50 min): the corrected integrality table (frozen) enumerated, for the 66 roster rows, the Galois-valid COMPLETE configurations under the PRINTED fixed-list closure (Moh Def 5.1(4) p.179 + Prop 5.3 p.180: every above-threshold factor continues along the same global M-list with the actual centre stabilizer L; at r = 1 Prop 4.6 forces squarefree coprime leading polynomials; D₁ residue/Galois checks) and found exactly one row with N = 0 complete configurations: R063 (a parent-level kill candidate, under gate). TASK: run the SAME enumeration (box/integrality-table-20260906/integrality_table.py reusing the gate scripts box/exact-contact-gate-20260906/census_replay.py and closure_fixed.py — do not rewrite the identities; parametrize only the row source) on ALL 1,420 operative rows (box/child-own-v-20260905/enumerated-source-rows.json or the operative census; the roster's 66 must reproduce the frozen table exactly as a control): for every row report N (complete configurations), the number integral, the number with I_M ≥ I_m, and list EVERY row with N = 0 and every row with 0 survivors — these are DATA (kill candidates under the printed closure, typed exactly as the table typed R063: DEAD-mod-[printed fixed-list + D₁ residues], NOT promoted). Cross-tabulate against the own-data partition (1,354 empty / 66 singleton): how many of the 66 singletons have N = 0; how many of the 1,354 already-empty rows have N > 0 (the two necessary-tree notions differ — say how). FALLACY-v2 (a missing configuration is not a pair; N = 0 is a kill only if the closure is a proved necessity — leave that to the gate). DISK DISCIPLINE: report + JSON ≤ 2 MB; no fleet. ≤ 55 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/printed-closure-screen-20260906/.
Report: xmodel/printed-closure-screen-grok46-20260906.md
Seal (<!-- BODY-END -->); 5-12KB; 55 min.
charged_input=xmodel/integrality-table-grok46-20260906.md
charged_input=xmodel/r063-child-pattern-grok46-20260906.md
charged_input=xmodel/own-data-gate-opus5-20260905.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/printed-closure-screen-grok46-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
a6ff5bb912937b0eebbc74ed92949fffe9571150d33834c153605b6e4510110b  {{LANE_INPUTS}}/integrality-table-grok46-20260906.md
c6b7d613e83f82bb928a27010e7bfacefc1e26980e97b2e46fa7cf5ddb782f6c  {{LANE_INPUTS}}/r063-child-pattern-grok46-20260906.md
3020c79b350ec46703690762b0959dcd8d0408205979f5e37796730f5ffab80f  {{LANE_INPUTS}}/own-data-gate-opus5-20260905.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
