# DERIVATION lane (complete the face-level instrument): the xu71-es-leaves report (frozen) found the LEADING face ODE of Xu (7.1) solvable on all 36 family-C leaves and could not instantiate the OFFSET-ONE row (the coefficient of t^{−1+δ} in ∂(T_s(σ), g(σ))/∂(t,π) = −J·(T_s)_f(σ)·t^{−2+δ}) because Xu prints only leading coefficients and the roster stores only (ρ, λ). TASK: (1) DERIVE the offset-one coefficient symbolically from the source: Moh Prop 4.1 (the Jacobian identity along a Puiseux arc σ, pp.164–166), Xu §7 (7.1) and its proof, and Def 5.1(4) (the generic point σ = centre + πt^δ with its 1-jet) — write the full expansion of both sides of (7.1) to one order beyond the face: the unknowns are the next Puiseux coefficients of the arc (the 1-jet), the next coefficients of T_s and g along the arc (determined by the face data plus the next characteristic data of the leaf), and the face modulus; state exactly which of these the necessary datum (ρ, λ, the tower) DETERMINES and which are free; (2) instantiate the offset-one row for R012 (D=108, ρ = 3) and R015 ((99,66)) as a polynomial system in the free unknowns over exact Q with the localizer Zc·c − 1 and J = 1; decide it (Singular, small); then all 36 leaves; (3) VERDICT per leaf: DEAD (the offset-one row is inconsistent with the face data for every value of the free unknowns — typed ES_LEAF_DEAD_BY_XU71_OFFSET_ONE, with the printed lines) / survives with the residual system stated / vacuous (identically zero — say why). FALLACY-v2 (a row needs its printed line; a free unknown left unconstrained is not a kill; declare every ring map). DISK DISCIPLINE: ~1.7 GB free — report + JSON ≤ 2 MB; no CAS dumps; `df -h /` before any write > 10 MB. ≤ 200 min; no ledger edits; no jc2-lean; no ideation-* input. Drivers to box/xu71-offset-one-20260906/.
Report: xmodel/xu71-offset-one-sol56-20260906.md
Seal (<!-- BODY-END -->); 10-22KB; 200 min.
charged_input=xmodel/xu71-es-leaves-sol56-20260906.md
charged_input=box/residual66-20260905/roster.jsonl
charged_input=box/lib/split_window.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY: the receipt `xmodel/xu71-offset-one-sol56-20260906.run.v2` carries `charged_input_<i>_sha256=`/`_basename=` lines; build the manifest with awk and run `sha256sum -c`; stop only on a real content mismatch:

```text
c76be040e115dc3fab84098eef218d157948afe8717318fd2cc6f20e1aa576b9  {{LANE_INPUTS}}/xu71-es-leaves-sol56-20260906.md
cb384ecdaf41cb96288ff12184a0c22ded49c276842f136919e675e8248534bf  {{LANE_INPUTS}}/roster.jsonl
be99effafff67501f20c80d5e0366162091c3fe1c0fcd3b6672896cd3db9aedd  {{LANE_INPUTS}}/split_window.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
