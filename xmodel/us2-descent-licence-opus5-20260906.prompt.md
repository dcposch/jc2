# PROOF LANE (≤ 150 min): the 20 family-C residual rows (u_s ≥ 2 prefix rows in the frozen roster) are untouched by every descent-side instrument because Prop 6.3 (p.197) needs the principal-minor radius δ*_{s−1} ≥ v_s/u_s, which Prop 6.4 (pp.198–199) supplies ONLY at u_s = 1 (OPEN[PROP6.3-RADIUS-US>1]); and even with a radius, the child chain at u_s > 1 has d'_s = u_s > 1 so a further gcd drop is possible and the identified prefix has an unidentified terminal part (descend_own top_license = OPEN_CHILD_TERMINAL_IDENTIFICATION; frozen lemma gate §4). TASK — attack both licences from the print: (1) RADIUS: reconstruct Prop 6.4's proof and identify exactly where u_s = 1 is used; determine whether the argument (or a different printed argument — Lemma 6.2, the p.194–196 normalization, Prop 5.3's cluster structure, the minor-direction Def 5.1(3)) yields δ*_{s−1} ≥ v_s/u_s for u_s ≥ 2 in general, under a printed extra hypothesis, or for the specific 20 rows (their (u_s, v_s, δ*_{s−1}) data are computable from the roster — compute them and check the inequality numerically first: if it FAILS numerically on a row, the licence is impossible there and say so); (2) TERMINAL IDENTIFICATION: at u_s ≥ 2, after descent the child's characteristic sequence can continue below the copied prefix; show whether the child's terminal part is determined by finitely many printed necessary conditions (Prop 4.6 at the child's top disc; the child's own Def 5.1 radii; the Jacobian exponent ℓ = v_s − u_s − 1) — produce the finite family or prove it is unbounded; (3) if BOTH licences hold for some subset of the 20, apply the promoted LEMMA [CHILD-INTEGRALITY] machinery in outline (do not compute the sums unless cheap) and state which rows become testable; (4) VERDICT per licence: PROVED / PROVED-CONDITIONAL / OPEN with the exact printed obstruction; per row: LICENSED / NOT-LICENSED / OPEN. FALLACY-v2 (a numerical inequality is not a radius proof; a prefix is not a chain). DISK: report + JSON ≤ 1 MB; no fleet; no ledger edits; no jc2-lean; no ideation-* input. Notes to box/us2-descent-licence-20260906/.
Report: xmodel/us2-descent-licence-opus5-20260906.md
Seal (<!-- BODY-END -->); 10-18KB; 150 min.
charged_input=xmodel/child-integrality-prefixes-astra-20260906.md
charged_input=xmodel/child-integrality-lemma-gate-opus5-20260906.md
charged_input=xmodel/child-integrality-lemma-astra-20260906.md
charged_input=xmodel/descent-invariance-gate-sol56-20260906.md
charged_input=box/lib/descend_own.py
charged_input=box/residual66-20260905/roster.jsonl
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/us2-descent-licence-opus5-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
0e0fe1a8a31ac6166db47ac4c99e8373c567545bbb68e0f99ae23aa88e3ecbcf  {{LANE_INPUTS}}/child-integrality-prefixes-astra-20260906.md
ef6739224bf3d9c6601451f6f8181c93d24679ad1fce35026be958f6fcac9fb4  {{LANE_INPUTS}}/child-integrality-lemma-gate-opus5-20260906.md
694f4c9eeaaeae44b6b8b2143fa8ec53fabea283e893d708a877997b6e0f9558  {{LANE_INPUTS}}/child-integrality-lemma-astra-20260906.md
d1e04b77a39f803f34b8bd8fb258380b9f517120ff16909ad99ad16523c6793b  {{LANE_INPUTS}}/descent-invariance-gate-sol56-20260906.md
3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2  {{LANE_INPUTS}}/descend_own.py
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
