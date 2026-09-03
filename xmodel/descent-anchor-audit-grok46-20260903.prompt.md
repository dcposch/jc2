# Source + arithmetic lane (decisive, 4 h cap): DESCENT-ANCHOR AUDIT — is Moh's Prop 6.3/6.4 descent, and the promoted radii rule δ' = (k+1)·Def 5.1(3)(descended data), defined when M_{s−1} = n − d_s (the Def 5.1(3) anchor n' − M'_{s'} − 1 = 0)?

From the blind Opus submission of round 20260903T1200Z (charged, §0 H1, §8,
§13): Def 5.1(3) as transcribed (census-rebase §1; box/moh_skeleton_full.py
Skel._delta) carries the factor 1/(n − M_s − 1), identically 1 for a Keller
pair (M_s = n − 2) and therefore never exercised in the source; after descent
M'_{s'} = M_{s−1}/d_s and the anchor n' − M'_{s'} − 1 vanishes exactly when
M_{s−1} = n − d_s. MEASURED (Opus): this holds on 38 of the 57 descendable
(u_s = 1) C_FULL_TREE_ODE survivors at n ≤ 100, on 12 of the 20 n = 108
screened survivors, and on THREE of Moh's printed six — the (84,56) rows
M = [−56, 42, 77, 82] and [−56, 70, 77, 82] with d_s = 7 (descending to (12,8)
with M₃' = 11 = n' − 1); Moh's p.207 table prints only d_s = 4 rows of
(84,56) and excludes (99,66). The δ' rule (AUDIT delta 17(t): 10/10 printed
rationals) is therefore confirmed on a proper subfamily; dropping the factor
breaks the match (δ₂' = −3 instead of −1/3 on (15,10)). Consequence: theorem
(T) (delta 17(q)) can currently be posed on only 19 of 57 screened rows.
YOUR TASK (source open: refs/moh1983_jram340_configurations_of_roots.pdf,
page N = PDF page N−139, pdftoppm -r 300; read pp.176–185 (Props 5.1–5.4,
Lemma 5.2, Def 5.1 at p.179 — the DISPLAYED formula (3)), 196–199 (Prop
6.3/6.4, the p.198 substitution and the last display), 207–208 (the descent
table and its d_s)):
(a) Is the factor 1/(n − M_s − 1) present in Def 5.1(3) as PRINTED at p.179
    (transcribe the display exactly), and what is its role in the proof of
    Prop 5.3 (pp.181–183) and Lemma 5.2 — is it the radius-order identity
    "c = n − M_s − 1" (RADIUS-ORDER, moh_skeleton_N.py:191–195) that D1-PIN
    consumes at c = 1? Under what hypothesis does Moh assert M_s = n − 2
    (Prop 5.4 / Lemma 5.3 / search (2))? Does the descended pair (Jacobian
    cγ^k) satisfy M'_{s'} = n' − 2 — compute it on all five p.207 rows and on
    the two (84,56) d_s = 7 rows; if not, what IS its top characteristic
    exponent and does Prop 5.3 still apply to it?
(b) Does Moh's p.207 descent table contain any anchor-degenerate row
    (prediction: no)? Read pp.207–208 and say why the (84,56) d_s = 7 rows are
    absent — did Moh treat them elsewhere (Appendix II says "similar
    arguments" for (84,56); which data does it use?), or does his descent
    require d_s = 4 there (the (84,56) row has TWO printed data sets [64]/[72]
    — are the d_s = 7 rows in the campaign's census but not in Moh's table
    because of a census/transcription difference? Check box/moh_skeleton_full
    's (84,56) rows against p.202).
(c) THE THREE OUTCOMES (Opus §8): (i) anchor-degenerate rows do not descend
    (Prop 6.3's hypothesis fails — say which) ⇒ OPEN[MINOR-DICHOTOMY] is
    much larger than 1/58 and (T) is incomplete; (ii) the descent is defined
    under a different normalisation (repair the δ' rule; it must still give
    10/10 printed rationals — negative control); (iii) the anchor-zero limit
    is a degeneration (δ' = −∞ / the descended disc collapses) ⇒ a KILL
    candidate for the 38 rows — state exactly what Moh's construction says
    happens when the top characteristic exponent is n' − 1 (this is the
    "M_i ≤ n − 1" note on p.151: M_i = n − 1 means f_{n−1}(x) is the x-linear
    coefficient — Lemma 2.1 — i.e. the descended pair's characteristic
    sequence reaches the Jacobian term itself; derive what that forces).
(d) MEASURE: reproduce Opus's 38/57 and 12/20 counts (box/mohprog-drivers-
    20260903/full_tree_partition.py + the descent map n' = n/d_s, m' = m/d_s,
    M_i' = M_i/d_s, V_i' = V_i, k = V_s − u_s − 1); list the anchor-zero rows
    with their (n, m, M, V, d_s); and under whichever of (i)–(iii) the source
    supports, restate the domain of theorem (T) (how many of the 57 / 20 it
    covers) and the corrected size of the u_s > 1 ∪ anchor-zero residue.
Typed block: PROVED-IN-SOURCE / DERIVED / MEASURED per item; bounded quantity
+ cheapest test of every OPEN. Desk-scale (< 10 min CAS); no ledger edits; no
jc2-lean; do not read ideation-20260903T1200Z-* files other than the charged
Opus one, nor other running lanes' reports. Drivers to
box/anchor-audit-20260903/.
Report: xmodel/descent-anchor-audit-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 12-20KB; 90 minutes.
charged_input=xmodel/ideation-20260903T1200Z-opus5.md
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=box/moh_skeleton_full.py
charged_input=box/moh_skeleton_N.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
2e4e817267cbfdba97607a41df0433b11f3d4542dbb5418226aa48982830accd  {{LANE_INPUTS}}/ideation-20260903T1200Z-opus5.md
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
