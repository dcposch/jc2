# INSTRUMENT-FIX + SOLVE lane (unblock the Moh ≤100 finish; AUDIT 17(qqqqqq)): the s'=3 chart builders (emitted by box/moh14-charts-20260905/order_basis_full.py / sprime3_compiler.py — the "full D1 native builder") have a Singular TYPE BUG in proc native_append_coeffs (line ~29: `string(xp)+"|"+string(yp)+"|"+string(cc)` → "wrong type declaration" when the coefficient `cc` is a type string() can't render), so several stems silently extract ZERO generators (NATIVE_DONE equations=0) and the guided std then reports GG__DIM=full (a VACUOUS non-kill, NOT a survive). FIX the bug, RE-VALIDATE that ALL 18 stems (6 classes) produce non-empty generators, and SOLVE the 6 classes via a fast method — then report which of the 12 Moh ≤100 rows / 6 descended classes DIE

This is the residual of the FULL Moh ≤100 theorem (the published (99,66) case is closed degree-wide, 17(ffffff)). OPERATIONAL: fix + validate LOCALLY on math-hq first (small charts), then run the batch on the FLEET (workers exist; see below). Task: (1) FIND + FIX the native_append_coeffs type bug in the builder emitter (the `string(cc)` — cc is likely a `number`/`poly` matrix entry; use the correct Singular idiom, e.g. cast via `string(cc)` after ensuring cc is a poly/number, or `sprintf`/`nc` handling; TEST that the fixed builder for stem V2_1 (which errored) now writes non-empty rows.tsv, and that V3_2 (which worked) still matches its prior 514 generators — a regression check); (2) RE-VALIDATE all 18 stems: for each, run the fixed builder and confirm rows.tsv has > 0 data rows; report any stem still empty (those are genuinely degenerate — flag); (3) SOLVE fast: switch the guided std from exact-Q Singular (too slow: ~53 min unfinished on 176/514-eqn systems) to MODULAR + CRT (guided_gb.py supports mod-p + reconstruction) OR msolve via qqideal/msolveio (installed on workers) — pick the faster; for each of the 6 classes, decide GG__UNIT (all its V-stems empty ⇒ class DEAD) / GG__DIM (a stem survives — extract a point, test J=const, it is NOT a counterexample unless J is a nonzero constant) / TIMEOUT; (4) FLEET: workers are up — c7i (64GB): 172.30.0.7, .18, .28; r7i (247GB): 172.30.0.166, .254; SSH key ~/.ssh/jc2-fleet (ubuntu@IP); the charts are at /home/ubuntu/jc2/box/moh14-charts-20260905/ on each (rsync from math-hq if stale via `rsync -az -e "ssh -i ~/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes" box/moh14-charts-20260905 ubuntu@IP:/home/ubuntu/jc2/box/`); use ops/fleet/dispatch.sh or direct ssh with `setsid`/nohup so jobs survive disconnect; route stems ≥140 unknowns to the r7i workers; (5) VERDICT: k of 6 classes DEAD; if all 6 DEAD ⇒ with 17(ffffff) the FULL Moh ≤100 theorem is RESOLVED (a MAJOR milestone — say so prominently); else PARTIAL with the exact surviving classes + the fastest next step. FALLACY-v2 (a GG__DIM is a real survive ONLY if the builder produced non-empty generators — always check rows>0 first; modular unit → char0 via properness for homogeneous, else exact-Q confirm the small residual). Commit the builder fix. ≤ 210 min; you MAY edit box/moh14-charts-20260905/ code (the instrument); no other ledger edits; no jc2-lean; no ideation-*.
Report: xmodel/moh14-fix-solve-opus5-20260905.md
Seal-at-completion (<!-- BODY-END -->); 15-30KB; 210 min.
charged_input=xmodel/moh-sprime3-compiler-grok46-20260905.md
charged_input=xmodel/moh100-14rows-opus5-20260905.md
charged_input=xmodel/sys-guided-gb-gpt55-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/moh14-charts-20260905/sprime3_compiler.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/moh14-fix-solve-opus5-20260905.run.v2` carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines; generate the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
1f0d61f2bfae72bbd818653c95f60ed913582c2bac4e47fb93627622c51cffe3  {{LANE_INPUTS}}/moh-sprime3-compiler-grok46-20260905.md
034e568d48572d69f809ca8fe02a909b120d6fb79e66a56381dd0c0b0348bc14  {{LANE_INPUTS}}/moh100-14rows-opus5-20260905.md
3256f9599f92f5f7e2129d4164237296f2adbce8bcda8fd61f56474ecdd55e6c  {{LANE_INPUTS}}/sys-guided-gb-gpt55-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
b70a5e9a6407e84b4830dc8ef8e0adddf9b593d856d7c53a2f9bae497891cef4  {{LANE_INPUTS}}/sprime3_compiler.py
```
