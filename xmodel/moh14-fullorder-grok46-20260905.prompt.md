# STRENGTHEN + SOLVE lane (finish Moh ≤100, correcting the chart, AUDIT 17(rrrrrr)): the 12 residual ≤100 rows are u_s=1 (H2) rows — killed by theorem (T) = the DESCENDED monomial-Jacobian ORDER chart being EMPTY, NOT by split-chart pole/Jacobian/incidence rows (those are u_s≥2, 17(tttt)/(ddddd)). The s'=3 chart (free leading form + B_safe, order/D1 rows) came back NON-EMPTY (full degree-6 modular std, no 1). DIAGNOSE why, and if it is an incomplete order over-approximation, COMPLETE it to the FULL necessary Theorem-1.2 order chart (per 17(nnnnn) order-basis-full: full D1 monomial inventory + cokernel + shear audit + the δ₁'=0/zero-slope centre-support) and re-solve; if it is STILL non-empty after completion, the rows genuinely survive the order conditions (a receiver/K16-type survival) — characterize exactly

OPERATIONAL: the builder is FIXED (box/moh14-charts-20260905/builder_fix.py — unknowns in the poly ring, RSS 1.5-3.9GB; use it). Fleet workers up: c7i 172.30.0.7/.18/.28 (64GB), r7i 172.30.0.166/.254 (247GB); SSH ~/.ssh/jc2-fleet (ubuntu@IP); charts at /home/ubuntu/jc2/box/moh14-charts-20260905/ (rsync from math-hq if stale); use setsid/nohup so jobs survive disconnect; MODULAR+CRT std (fast, 19-63s per the prior lane), not exact-Q. Task: (1) for one class (start with the smallest, C_n24m16_M12_17 or Mm15_14), compare the emitted order chart's rows against the FULL Theorem-1.2 necessary D1 inventory (order_basis_full.py, 17(nnnnn)): is the emitted chart MISSING necessary order rows (a strict sub-system, like the (25,15) case 17(ggggg))? if so it CANNOT kill by emptiness regardless; (2) build the FULL necessary order over-approximation for the s'=3 descended datum (all Theorem-1.2 order rows + the δ₁'=0 zero-slope centre-support; cokernel + shear audited) and re-solve modular; (3) VERDICT per class: GG__UNIT (full order chart empty ⇒ (T) ⇒ row dead) / NON-EMPTY (extract a surviving descended monomial-Jacobian pair (P,Q), check J(P,Q) = c·γ^k exactly — if it IS a valid monomial-Jacobian pair, that row SURVIVES (T) and is a genuine open receiver instance, NOT a JC2 counterexample unless it lifts; flag it) / TIMEOUT; (4) if all 6 classes' full order charts are EMPTY ⇒ the 12 rows die ⇒ with 17(ffffff) the FULL Moh ≤100 theorem RESOLVES (MAJOR — say so); else PARTIAL: which classes survive the full order chart, and the exact surviving receiver data (this becomes a receiver/K16-type OPEN); (5) FALLACY-v2 (a NON-EMPTY chart is a real survive ONLY if it is the FULL necessary over-approximation, not a sub-system — 17(ggggg); a surviving point is a counterexample only if it lifts to a Keller pair with J∈k*). Commit chart/instrument fixes. ≤ 210 min; you MAY edit box/moh14-charts-20260905/; no other ledger edits; no jc2-lean; no ideation-*.
Report: xmodel/moh14-fullorder-grok46-20260905.md
Seal-at-completion (<!-- BODY-END -->); 15-30KB; 210 min.
charged_input=xmodel/moh14-fix-solve-opus5-20260905.md
charged_input=xmodel/moh-sprime3-compiler-grok46-20260905.md
charged_input=xmodel/order-basis-full-gpt55-20260903.md
charged_input=xmodel/row2515-order-gate-sol56-20260903.md
charged_input=box/lib/guided_gb.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md
charged_input=box/moh14-charts-20260905/builder_fix.py
charged_input=box/moh14-charts-20260905/sprime3_compiler.py
charged_input=box/moh14-charts-20260905/modular_solve.py
charged_input=box/orderbasis-20260903/order_basis_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/moh14-fullorder-grok46-20260905.run.v2` carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines; generate the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
2372687402bdb5b83a9ecd28d206f215abb834508f9a937b94c81350a54f42e2  {{LANE_INPUTS}}/moh14-fix-solve-opus5-20260905.md
1f0d61f2bfae72bbd818653c95f60ed913582c2bac4e47fb93627622c51cffe3  {{LANE_INPUTS}}/moh-sprime3-compiler-grok46-20260905.md
a8f89e2cc9060d2008375c5bb689b935ef72abdd75b96b1c10d52edf3151c2b6  {{LANE_INPUTS}}/order-basis-full-gpt55-20260903.md
f1766b7c59c03387447fa0b599d79ef05935a0a5c373ff17c8e4020592bd67fb  {{LANE_INPUTS}}/row2515-order-gate-sol56-20260903.md
501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3  {{LANE_INPUTS}}/guided_gb.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b  {{LANE_INPUTS}}/builder_fix.py
b70a5e9a6407e84b4830dc8ef8e0adddf9b593d856d7c53a2f9bae497891cef4  {{LANE_INPUTS}}/sprime3_compiler.py
febdf0bd7a3b2f422fdf5faa4b7f8eb92971cbb41bf0b697b3517b72e092ace6  {{LANE_INPUTS}}/modular_solve.py
f4e0e98e930f5b4ac9f54c8d3660fb8ca9c58dfd20a0500a456df77b47191639  {{LANE_INPUTS}}/order_basis_full.py
```
