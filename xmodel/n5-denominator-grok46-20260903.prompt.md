# Derivation lane (one page): prove or refute N5 — the denominator of the principal-minor split order δ is at most u_s (Xu p.13 asserts den(δ) ≤ u_s = 3 for (99,66) without an exhibited proof); the completeness of the split-order classification δ ∈ {2, 5/2} (AUDIT delta 17(nnn)) rests on it

Context (banked): at (99,66) the principal minor roots of f_ξ are the u_s·m/d_s =
18 roots near the second point at infinity (leading form y − a₁x); they do not
split before order 1 (Moh Prop 6.1 / Xu Prop 7.3); Moh's Prop 6.1 proof gives
ord g(σ) = (n/d_s)(u_sδ − v_s) = 9(3δ − 8) for a π-root σ of split order δ, so
the detector exists iff δ < v_s/u_s = 8/3; Xu's §8 classification of admissible
δ uses "the denominator of δ is at most u_s = 3" — asserted, not proved in the
print (Grok gate 17(nnn)). If a split order with denominator > 3 in (1, 8/3)
were possible (e.g. 5/4, 7/4, 9/4, 7/5, 11/5, 13/6 …), it would fall outside
both surviving branches and the (99,66) decider would be incomplete. Task:
(1) SOURCE-READ Moh pp.190–194 (Prop 6.1 and its proof: the structure of the
principal-minor cluster, the u_s conjugate factors of the leading polynomial
at the top disc, the ramification of t at the second point) and Xu pp.10–13
(§7.3: quasi-approximate roots and the characteristic δ-sequence; Prop 7.3;
§8's sentence about the denominator) as page images (name pages); (2) DERIVE:
the principal minor roots at the second point at infinity are the roots of
the u_s-fold factor; their Puiseux expansions in t = x⁻¹ have exponents in
(1/e)Z where e is the ramification index of the principal place — show that e
divides u_s (or equals u_s, or is bounded by it) from the multiplicity data of
§7.3 (the u_s conjugate roots at the top disc under the Galois action of the
principal place's ramification), hence every split order δ of these roots
has den(δ) | e ≤ u_s; handle the case where the principal cluster itself
splits into sub-clusters with smaller ramification (does the bound still hold
per sub-cluster?); if the argument needs a hypothesis Xu does not state, name
it and say whether the (99,66) skeleton satisfies it; (3) sanity: at Moh's
(64,48) (u_s = 1) the principal minor roots are unramified (den = 1) — check
against the known tree; at (75,50) V₂ = 3 with the 2,2,6 split (u = 2) —
check; (4) if N5 is PROVED, the split-order classification is complete and
the (99,66) decider is exhaustive over branches {2 [2,1], 5/2 [1,1,1]}; if
N5 fails, list the additional admissible δ with denominator ≤ some bound you
CAN prove and run Xu's ODE exclusion (the q = p^{13}(π − c) argument; sympy)
on each — report which survive; (5) verdict + typed scope; FALLACY-v2
applies. Desk-scale (≤ 60 min); no ledger edits; no jc2-lean; no ideation-*
files; no in-progress lane reports (g9966-delta52-joint, g9966-global-design,
k16-*, emitter-native). Drivers to box/n5-20260903/.
Report: xmodel/n5-denominator-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 6-12KB; 60 minutes.
charged_input=xmodel/g9966-review-gate-grok46-20260903.md
charged_input=xmodel/g9966-source-review-opus5-20260903.md
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=xmodel/xu-principal-floor-sol56-20260903.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/n5-denominator-grok46-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
dc2355a81dd472993c9af0fb0f03eb5b6f3c087c3a2ed00120615b76bcf91be8  {{LANE_INPUTS}}/g9966-review-gate-grok46-20260903.md
47ca21fa9a633a4d2ffeff8380d2c33abf36076e96f8a1d078399576c500825a  {{LANE_INPUTS}}/g9966-source-review-opus5-20260903.md
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
759d54a7c346c0a063f88421d4bdf94dec438f4a7df219c5403b3770afc271e2  {{LANE_INPUTS}}/xu-principal-floor-sol56-20260903.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
