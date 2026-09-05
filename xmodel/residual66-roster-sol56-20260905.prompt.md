# ROSTER lane (the all-degree program's residual at n ≤ 200 is now 66 NECESSARY ROWS — make it a concrete, attackable list): the hostile gate (frozen) CONFIRMED-WITH-FIX Astra's own-data reduction: 1,354 operative rows empty, 66 singletons (46 at u_s = 1, 20 prefix-only at u_s > 1), with ONE over-strict filter to fix — box/lib/own_v_routes.py lines 66 and 74 implement Prop 4.6(5) ("p(π) is not a power of q(π)") as "reject any single factor of multiplicity P/Q"; the correct predicate is NOT(all multiplicities equal w AND #distinct roots = deg q) — see the gate §4.1 and OPEN[RESONANCE-FILTER-EXACT-FORM]. TASK: (1) apply the fix to own_v_routes.py exactly as the gate specifies (patch in place under box/lib/, keep the old predicate behind a flag for the control), re-run the sweep (box/child-own-v-20260905/sweep.py) and CONFIRM 1,354 / 66 with the one row (168,112) M=(−112,140,160,166) V=(3,21,3) moving to singleton; run the controls (Moh's five p.207 rows + (99,66) nonempty; the 12 Moh ≤100 fibres empty) through the patched tool; (2) produce the ROSTER of the 66: for each row — source (n,m; M; d; V; s; u_s, v_s), own child data (n', m', M', d', own V', s', ℓ, δ'), the licensed descent route (D1 by Prop 6.4 at u_s = 1; the u_s > 1 prefixes flagged with their OPEN[PROP6.3-RADIUS-US>1] / [CHILD-TERMINAL-SUPPORT-US>1] dependence), the SIZE of the proved G_i-only receiver chart (17(fffffff): |G_i| depends only on (n', M_s', ℓ); count unknowns and generators via the gi-only emitter box/gi-only-20260905/) and the split-window status for the u_s ≥ 2 rows (box/lib/split_window.py: descent-forced or typed ES leaves) — write box/residual66-20260905/roster.jsonl + a human table sorted by chart size; (3) identify the CHEAPEST rows (smallest G_i charts) and, if any is ≤ 60 unknowns, run the exact-Q kill (guided_gb, 600 s) as a demonstration; (4) state what the 6 rows with n ≤ 100 are (Moh's five + (99,66)) and confirm the other 60 have 100 < n ≤ 200. FALLACY-v2 (a roster row is a necessary configuration, not a pair; sizes are chart sizes, not difficulty proofs). ≤ 150 min; no ledger edits; no jc2-lean; no ideation-*. Drivers to box/residual66-20260905/.
Report: xmodel/residual66-roster-sol56-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 150 min.
charged_input=xmodel/own-data-gate-opus5-20260905.md
charged_input=xmodel/child-own-v-astra-20260905.md
charged_input=xmodel/source-support-closeout-opus5-20260905.md
charged_input=box/lib/descend_own.py
charged_input=box/lib/own_v_routes.py
charged_input=box/lib/split_window.py
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/residual66-roster-sol56-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
3020c79b350ec46703690762b0959dcd8d0408205979f5e37796730f5ffab80f  {{LANE_INPUTS}}/own-data-gate-opus5-20260905.md
caca19dcd220758283d185415a3fdca8c131fa42fdb9a767c79bcf81d8cdf387  {{LANE_INPUTS}}/child-own-v-astra-20260905.md
a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c  {{LANE_INPUTS}}/source-support-closeout-opus5-20260905.md
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
21220b26c3485cd2f44e9b590cd53bcf5893585d8a0dae2b508331b45ceecafd  {{LANE_INPUTS}}/own_v_routes.py
be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd  {{LANE_INPUTS}}/split_window.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
