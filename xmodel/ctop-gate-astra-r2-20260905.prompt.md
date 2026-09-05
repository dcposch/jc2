# RESUME (round 2 of ctop-gate-astra-20260905, which died at 14:33Z on a backend capacity error after ~25 min; its partial artifacts in box/ctop-gate-20260905/ — enum-replay.py/.json/.log (a replay of the (C-TOP) enumeration), Moh page renders child-p150/p170/p197/p207.png, moh-source.txt — may be consumed but must be re-verified; enum-replay.json is charged). Same charge as round 1, verbatim below:
# HOSTILE GATE (a 936-row kill by a NEW screen; different model from the producer): the frozen child-data report (Opus) claims (C-TOP) := "V'_{s'} ≤ d'_{s'}" — Moh Def 5.1(2) applied at i = s' to the DESCENDED datum, licensed by the child-top convention V'_{s'+1} = d'_{s'+1} which it proves at u_s = 1 via the closed form d'_{s'+1} = gcd(n', M'₁..M'_{s'}) = u_s (p.150 termination M_{h+1} = ∞ + p.174's definition of M_s dropping a terminal M_h = n−1) — kills 936 of the 1,110 u_s=1 operative census rows (16 ≤ n ≤ 200), leaving 174 live; and that the U-NEGATIVE licence u' = K'−V'₂ ≥ 0 follows in one line from Def 5.1(1) p.179 ("in D_i, g has precisely (n/d_{i+1})V_{i+1} roots") + Prop 6.3(2) p.197 (g' has exactly n' roots). ADVERSARIAL CHECKS: (1) Def 5.1(2) — quote it; is "V_{i+1} ≤ d_{i+1}" (or whatever (2) literally says) a CONDITION on admissible data (so a row violating it is impossible ⇒ kill) or a DEFINITION/normalization (so violating rows are just mislabeled)? Is it stated for the source datum only, and does it transfer to the child's own datum — i.e. is the descended pair's characteristic data (M', d', V') computed by the campaign's descend() the child's OWN Def 5.1 data (OPEN[CHILD-LEVEL2-IDENTIFICATION]: V'₂ = V₂ printed only on Moh's five u_s=1 rows p.207)? Compute ONE child's data from first principles (p.150 recipe on the child's own expansion) and compare with descend()'s labels, at a row where (C-TOP) FAILS — is the row really impossible, or is the label wrong? (2) the top convention: p.174 says the last effective pair drops M_h = n−1; the closed form d'_{s'+1} = u_s — derive it yourself; at u_s = 1 does the chain close at s' (so V'_{s'+1} = d'_{s'+1} = 1 trivially)? (3) is the p.174 drop applied consistently between the kill and the enumerator (the report says 90 rows carry M'_{s'} = n'−1)? (4) the U-NEG one-liner: does Prop 6.3(2) give g' EXACTLY n' roots in the relevant disc, and does Def 5.1(1)'s count refer to the same disc D'₁ (centre, radius) as the campaign's V'₂? (5) run the screen yourself on the frozen enumerator (box/moh_skeleton_full.py + box/child-data-20260905/) and reproduce 936/174/310 — or report the discrepancy. VERDICT: (C-TOP) CONFIRMED as a kill (⇒ promote; residual 484 rows) / CONFIRMED-WITH-FIX / REFUTED (name the row that survives from first principles); U-NEG licence CONFIRMED/REFUTED. FALLACY-v2. ≤ 120 min; no ledger edits; no jc2-lean; no ideation-*. Notes to box/ctop-gate-20260905/.
Report: xmodel/ctop-gate-astra-r2-20260905.md
Seal (<!-- BODY-END -->); 12-25KB; 120 min.
charged_input=xmodel/child-data-tests-opus5-20260905.md
charged_input=xmodel/scope-leaks-opus5-20260905.md
charged_input=box/appendix2-k16-20260903/shape.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md
charged_input=box/ctop-gate-20260905/enum-replay.json

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/ctop-gate-astra-r2-20260905.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
219faa47b435222511168ffaa1cc4f0c33be7744209a29626999f464d66c9cff  {{LANE_INPUTS}}/child-data-tests-opus5-20260905.md
c3dd95b11ea3e12ba88e813860ecab703a275f745ce429944c8aeb04a5095eda  {{LANE_INPUTS}}/scope-leaks-opus5-20260905.md
d8750d4e512645366e9e0c53153484eb5daa9c785434c1cc59658986d0ab138c  {{LANE_INPUTS}}/shape.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
3123aa9992ec170d1e38404761ade428e8bf7105c04f532c95b8fb90bf5a811e  {{LANE_INPUTS}}/enum-replay.json
```
