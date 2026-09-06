# FACE-LEVEL INSTRUMENT lane (a non-truncation kill test for the split leaves; exact Q, local CPU): the roster (charged) types the family-C rows' early-split obligations as ES_NECESSARY_LEAF records (ρ = P/Q in the window 1 < ρ < v_s/u_s, Q ≤ u_s, face polynomial p(π) of Galois shape λ); Xu 2016 p.11 (after Moh Prop 4.1) gives on each such leaf the face-Jacobian identity (7.1): ∂(T_s(σ), g(σ))/∂(t, π) = −J·(T_s)_f(σ)·t^{−2+δ}. If J is a nonzero constant the LEADING t-coefficient is the homogeneous face ODE (Xu §8 — already used by the split-window screen (G)+(L)); the coefficient of t^{−1+δ} is an INHOMOGENEOUS polynomial in the 1-jet of the arc and the face modulus (c or ρ) — the first J = 1 row on the face, at face weight, not a deep band. TASK: (1) reconcile the leaf count (roster.jsonl enumerates 36 ES leaves on the 20 family-C rows; residual65-structure prices 38 — decide which by a one-line reducer and record OPEN[ROSTER-ES-LEAF-COUNT-36-VS-38]); (2) for each leaf, in the ring k[π, c] (or ρ) with the localizer Zc·c − 1 and the (t, π) coordinates declared exactly as Xu §8, write the leading face ODE and the +1-jet inhomogeneous row of (7.1); reproduce Xu §8 as a control; (3) decide, exact Q, per leaf: UNIT (the leaf's necessary face admits no J = 1 configuration ⇒ the leaf is DEAD, typed ES_LEAF_DEAD_BY_XU71; cite (7.1) and the printed lines) / a nonzero univariate condition on the modulus whose only localized root would be c = 0 / identically vacuous (+1 jet ≡ 0 ⇒ type OPEN[XU71-PLUS-ONE-VACUOUS] and stop for that leaf); do the two cheapest rows first (R012, R015), then all family-C leaves, then the (99,66) δ=2/δ=5/2 and D=108 δ=3 branches' faces; (4) VERDICT: rows whose EVERY leaf died (they become descent-only prefixes — still necessary configurations, not pairs), leaves surviving, and the exact residual of family C. FALLACY-v2 (necessary ≠ sufficient; identical vanishing is not a kill; a floor is not attainment; declare every ring map). DISK DISCIPLINE: the host has ~3 GB free — write only the report and JSON ≤ 1 MB; no artifact trees, no CAS dumps; check `df -h /` before any write > 10 MB. ≤ 240 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/xu71-leaves-20260906/.
Report: xmodel/xu71-es-leaves-sol56-20260906.md
Seal (<!-- BODY-END -->); 10-25KB; 240 min.
charged_input=box/residual66-20260905/roster.jsonl
charged_input=xmodel/residual65-structure-fable5-20260905.md
charged_input=xmodel/split-window-gate-opus5-20260905.md
charged_input=xmodel/cone-vertex-gate-opus5-20260905.md
charged_input=box/lib/split_window.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/xu71-es-leaves-sol56-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
7d3ffbba4791a64c7c7d9e28546de67190d96edd3a47b431c116fec35394c927  {{LANE_INPUTS}}/residual65-structure-fable5-20260905.md
b72b7a3cd132f959dd7e083d10e8c1bdbd16637be3bf6066406d6c7172f707c5  {{LANE_INPUTS}}/split-window-gate-opus5-20260905.md
72dfcd371f338767e303c6da0eab02337f257ad29409a9fc6b60cd2e85c20ecd  {{LANE_INPUTS}}/cone-vertex-gate-opus5-20260905.md
be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd  {{LANE_INPUTS}}/split_window.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
