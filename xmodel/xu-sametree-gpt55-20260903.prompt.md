# Census lane: strengthen the promoted Xu screen by the SAME-TREE optimisation of IM − Im (one full split tree at a time, instead of independent max(IM) and min(Im)) and by adding Xu Theorem 3.4's EXACT formula for I(f_ξ, f_y) as an equality constraint — the cheapest strengthening every gate named

Context (banked, AUDIT deltas 17(eee), (fff)): the operative screen is
C_FULL_TREE_POLYNOMIAL_ODE ∧ XU with XU = Cor. 5.3 (IM ≥ Im), evaluated fail-closed
as IM_max (over all full-tree embeddings) ≥ Im_min (floors: nonprincipal minor
children by S_out/N; principal by V_s/u_s − 1); 653 groups survive at 48 ≤ D ≤
200 (166 with u_s > 1). Fable's gate (charged) proved from Lemma 4.1 that for
every root α of f_ξ, S(α) := −ord f_y(α) = −Σ_{j≠i} ord(α − α_j) is a function of
the ultrametric root tree alone; IM = Σ_{major α}(1 − S(α)) EXACTLY and every
final minor root has δ_σ = S(α) EXACTLY. So for a GIVEN full split tree T of the
roots of f_ξ, both IM(T) and Im(T) are exact, and Cor. 5.3 says IM(T) ≥ Im(T)
must hold for the actual tree; moreover Theorem 3.4 gives I(f_ξ, f_y)(T) =
−Σ_σ (e(f_σ) − 1)λ_σ exactly, and I(f_ξ, f_y) is ALSO expressible from the
skeleton (degrees: I(f_ξ, f_y) = deg_x Res_y(f_ξ, f_y) — is it determined by
(n, m, M, V, d)? — check: for a Keller pair, Theorem 4.7(i)/(ii) bound it; is
there an exact skeleton formula, e.g. via the Milnor number / genus of the
generic fibre?). Task: (1) SOURCE-READ Xu pp.4–8 (page images; name pages):
state exactly which quantities are exact functions of the full split tree T
(IM, Im, I(f_ξ, f_y)) and which constraints Xu proves among them for Jacobian
pairs (Cor. 5.3; Theorem 4.7(i),(ii); Cor. 4.8; anything relating I(f_ξ, f_y)
to deg_y f − 1 or to the genus); (2) implement the SAME-TREE test: for each
operative row enumerate the finite set of full split trees under the
operative model (the charged driver's embedding enumerator; reuse it), and
for each tree T compute IM(T), Im(T), I(f_ξ,f_y)(T); kill the row iff EVERY
tree violates at least one of Xu's constraints (fail-closed: a row survives if
some tree satisfies all); record which constraint kills; (3) report: counts
killed under (a) the promoted independent-extrema policy (must reproduce
48/33 with the sharpened floor), (b) same-tree Cor. 5.3 only, (c) same-tree
with all constraints; by u_s class; the new kills at D ≤ 120; whether (99,66),
(108,72; V = (7,7)), the two-point list or the K = 16 entries change (K = 16
must not die — if it does, that is a REFUTATION of something: stop and
report); calibration on Xu's three cases; (4) type the same-tree policy as a
lemma (why the actual tree is in the enumerated set; why each constraint is
necessary) so a gate can confirm; (5) verdict + bounded quantity + cheapest
test per OPEN; FALLACY-v2 applies. ≤ 90 min; 2 cores; no ledger edits; no
jc2-lean; no ideation-* files; no in-progress lane reports (k16-middle-spine,
moh9966-B-lift, bigrows-preprocess, strata-rerun-corrected, r3-preprocess).
Drivers to box/xusametree-20260903/.
Report: xmodel/xu-sametree-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 90 minutes.
charged_input=xmodel/xu-principal-floor-sol56-20260903.md
charged_input=xmodel/xu-screen-gate-fable5-20260903.md
charged_input=box/xuscreen-gate-20260903/hand_trees.py
charged_input=box/xuscreen-gate-20260903/hand_check.py
charged_input=xmodel/xu-inequality-screen-gpt55-20260903.md
charged_input=box/xuscreen-20260903/xu_screen.py
charged_input=refs/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=FALLACY-v2.md
charged_input=box/xufloor-20260903/xu_screen_candidate.py
charged_input=box/xufloor-20260903/audit_results.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/xu-sametree-gpt55-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
759d54a7c346c0a063f88421d4bdf94dec438f4a7df219c5403b3770afc271e2  {{LANE_INPUTS}}/xu-principal-floor-sol56-20260903.md
73810445b86518097594ce95d478a4f96000c74c7ad0455e376eccdc5f23218b  {{LANE_INPUTS}}/xu-screen-gate-fable5-20260903.md
8169199b78917c2d9d33c38d6af10d2d258a6adffd029c5d2ae096b92b9379cc  {{LANE_INPUTS}}/hand_trees.py
9fbc168353e65645e7d0f028d213d372573c89d10ac9a7d604745d48800606ae  {{LANE_INPUTS}}/hand_check.py
86ca820edb793853d6d725713edd6208d1b9f484a19f5416ef81dbc4391e5230  {{LANE_INPUTS}}/xu-inequality-screen-gpt55-20260903.md
5b71f196ce433333bd860aa74d8dc897f1729d02f246445fb41e971b60b26495  {{LANE_INPUTS}}/xu_screen.py
00fecb1614c98b6e7496097ab2d6b7496c3027feca66a8c30642aa7f5812de21  {{LANE_INPUTS}}/xu2016_intersection_numbers_split_minor_roots_arxiv1604.07683v4.pdf
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
aef7059080a7fe0e8f54358b2d10c7a81a6c833796497693bbe3234ae779c87b  {{LANE_INPUTS}}/xu_screen_candidate.py
8161c7f1b64792e50ab16d09c9b86ba9ea889d3623e5dfbafc0c993305cf33f1  {{LANE_INPUTS}}/audit_results.py
```
