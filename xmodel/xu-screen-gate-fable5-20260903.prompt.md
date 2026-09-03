# Hostile gate (page images): the Xu IM ≥ Im skeleton screen (AUDIT delta 17(ccc), PROVISIONAL) — are Theorems 3.4 / 4.7 / 5.1 transcribed correctly, is the fail-closed policy (IM maximised over full-tree embeddings; Im floored; principal u_s > 1 floor 0) sound, and are the 29 kills theorems about skeletons?

Charged claim (xu-inequality-screen-gpt55-20260903.md; box/xuscreen-20260903/
xu_screen.py): from Xu, arXiv:1604.07683v4 (charged PDF) — Theorem 3.4 (exact
formula I(f_ξ, f_y) = −Σ_σ (e(f_σ) − 1)λ_σ over split π-roots of f_ξ, no Jacobian
condition used), Theorem 4.7 (final-minor inequalities), Theorem 5.1 / Cor. 5.3
(I(f_ξ, g) expressed by final major roots) — the lane derives, for a Jacobian
pair whose skeleton is (n, m, M_i, V_i, d_i, δ_i), an upper bound IM_max on the
final-major side (maximised over all whole-tree embeddings) and a lower bound
Im_min on the final-minor side (charging nonprincipal minor children by the
first zero-order floor δ_j + (d_j/(n − M_j))(1 − δ_j)/v − 1, and the principal
minor roots of a u_s > 1 row by 0), and kills a skeleton iff IM_max < Im_min. It
reproduces Xu's three printed numbers exactly ((75,50) split (ii): 4 < 6; (84,56;
64; 2): 4 < 5; (84,56; 72; 5): 10 ≥ 4) and kills 43 rows / 29 groups of the
operative D ≤ 200 census, including 7 u_s > 1 groups and (84,56; M = (64,82);
V_s = 3), (90,60; (45,80,88); V_s = 4) at n ≤ 100. Task: (1) open Xu pp.3–9 and 10–
12 as page images (pdftoppm -r 200; name pages) and check each theorem
statement and hypothesis as transcribed in the report §Source Read and in
xu_screen.py: in particular (a) whether Theorem 4.7's inequality direction and
its hypotheses (final minor roots; "not split before order 1"; the role of ξ
generic) are as used; (b) whether I(f_ξ, g) and I(f_ξ, f_y) are related by the
Jacobian condition in the way the screen's IM ≥ Im comparison requires (which
of Xu's displayed relations gives IM ≥ Im, and is it stated for Jacobian pairs
only?); (c) whether the "first zero-order floor" for nonprincipal minor
children is a theorem of Xu (or of Moh: minor roots do not split before order 1)
and correctly evaluated from the skeleton; (d) whether maximising IM over all
whole-tree embeddings is fail-closed (is IM monotone in the choices? could a
non-maximal embedding be the only actual one, and would that matter?); (2)
replay: run xu_screen.py on the frozen census and reproduce the calibration
and the counts; independently recompute IM/Im by hand from Xu's formulas for
two killed groups ((84,56; (64,82); 3) and one u_s > 1 group, e.g. (144,108;
(126,135,142); V_s = 6; u_s = 3)) and for two survivors ((64,48) and (99,66));
(3) verdict: CONFIRMED (promotable as the screen C_FULL_TREE_POLYNOMIAL_ODE ∧
XU, with scope) / GAP (which step; cheapest test) / REFUTED; also state whether
the principal u_s > 1 floor could be sharpened from Xu §7.3 alone. Type every
claim; FALLACY-v2 applies (a screen is necessary, never attainment). ≤ 75 min;
no ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports
(bigrows-preprocess, k16-t4-normalizer-gate, strata-rerun-corrected, k16-
middle-spine, moh9966-B-lift). Drivers to box/xuscreen-gate-20260903/.
Report: xmodel/xu-screen-gate-fable5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 8-16KB; 75 minutes.
charged_input=xmodel/xu-inequality-screen-gpt55-20260903.md
charged_input=box/xuscreen-20260903/xu_screen.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=xmodel/xu9966-read-gpt55-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/xu-screen-gate-fable5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
86ca820edb793853d6d725713edd6208d1b9f484a19f5416ef81dbc4391e5230  {{LANE_INPUTS}}/xu-inequality-screen-gpt55-20260903.md
5b71f196ce433333bd860aa74d8dc897f1729d02f246445fb41e971b60b26495  {{LANE_INPUTS}}/xu_screen.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
aabc19a04839c1337fefea5ecd369f54654c4d0359f4ddd341ed1b73df4d4773  {{LANE_INPUTS}}/xu9966-read-gpt55-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
