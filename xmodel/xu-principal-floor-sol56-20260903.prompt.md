# Derivation + census lane: sharpen the Xu screen's principal-minor floor for u_s > 1 rows from 0 to V_s/u_s − 1 (Fable's gate §2 "distance-only rederivation"), PROVE it from Xu Lemma 4.1 / Theorem 4.7 and Moh's minor-disc results, and rerun the promoted screen — the only lever that bites the u_s > 1 stratum (170 groups) and possibly (99,66)

Context (banked, AUDIT deltas 17(ccc), (eee)): the promoted screen XU = Cor. 5.3
(Theorem 4.7(ii) + Theorem 5.1) kills a skeleton iff IM_max < Im_min, with Im_min
charging nonprincipal minor children by the first zero-order floor and the
PRINCIPAL minor roots of a u_s > 1 row by 0 (a deliberately weak floor: Xu §7.3
gives the principal-minor multiplicities and non-splitting at order 1 but not
the final count/orders). Fable's gate (charged) re-derived the minor floor
from Lemma 4.1 (the distance argument, λ^f_σ = 0) and states that the same
argument gives a principal floor V_s/u_s − 1, expected to add +5 rows / +4
groups at D ≤ 200, "requires its own gate of the distance argument". Task:
(1) SOURCE-READ Xu Lemma 4.1, Lemma 4.4, Definition 4.6, Theorem 4.7 and its
proof (pp.4–6), §7.3 and Prop 7.3 (pp.10–11), and Moh Props 6.1–6.4 (pp.196–199:
minor roots do not split before order 1; the minor radius bound) as page
images (name pages); (2) DERIVE the principal-minor contribution to Im for a
u_s > 1 skeleton: the principal minor roots are the u_s·(something) roots of
f_ξ near the second point at infinity with multiplicity data from §7.3; using
Lemma 4.1 (contact orders) and the fact that they do not split before order 1
(Moh 6.1 / Xu Prop 7.3), give the sharpest LOWER bound on Σ_{P_m principal}
(|D_σ| − 1)(δ_σ − 1) that depends only on the skeleton — is it V_s/u_s − 1 as
Fable states? derive it carefully (state exactly which quantity is bounded and
why it is a floor, i.e. holds for every possible split tree), or correct it;
also derive the best UPPER bound on the principal contribution to IM if the
principal roots can be final major (they cannot — they are minor by
definition; check); (3) implement the sharpened floor in a copy of the
promoted driver (box/xuscreen-20260903/xu_screen.py, charged), keep the
promoted floor as a column, and rerun the D ≤ 200 census: report the new kills
(rows/groups; which u_s > 1 groups; does (99,66) or the D = 108 u_s = 2 row
(108,72; (−72,81,106); V = (7,7)) die? does anything on the two-point list or
the K = 16 ray change (must not)); calibration: Xu's three cases must
reproduce; (4) the gate-quality argument: write the floor as a typed lemma
with proof (SOURCE-READ hypotheses named), so that a different-model gate can
confirm it; (5) verdict + bounded quantity + cheapest test per OPEN; FALLACY-v2
applies (a floor must hold for EVERY split tree; if the derivation needs an
assumption on the split, say so and do not promote). ≤ 90 min; no ledger
edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(k16-middle-spine, moh9966-B-lift, bigrows-preprocess, strata-rerun-corrected,
r3-preprocess). Drivers to box/xufloor-20260903/.
Report: xmodel/xu-principal-floor-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 90 minutes.
charged_input=xmodel/xu-screen-gate-fable5-20260903.md
charged_input=box/xuscreen-gate-20260903/hand_check.py
charged_input=xmodel/xu-inequality-screen-gpt55-20260903.md
charged_input=box/xuscreen-20260903/xu_screen.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=xmodel/minor-dichotomy-sol56-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/xu-principal-floor-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
73810445b86518097594ce95d478a4f96000c74c7ad0455e376eccdc5f23218b  {{LANE_INPUTS}}/xu-screen-gate-fable5-20260903.md
9fbc168353e65645e7d0f028d213d372573c89d10ac9a7d604745d48800606ae  {{LANE_INPUTS}}/hand_check.py
86ca820edb793853d6d725713edd6208d1b9f484a19f5416ef81dbc4391e5230  {{LANE_INPUTS}}/xu-inequality-screen-gpt55-20260903.md
5b71f196ce433333bd860aa74d8dc897f1729d02f246445fb41e971b60b26495  {{LANE_INPUTS}}/xu_screen.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
184a689f3cd63405d922b8118632c7e17f96f471a0bc71f9a50cd161b8a87ad1  {{LANE_INPUTS}}/minor-dichotomy-sol56-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
