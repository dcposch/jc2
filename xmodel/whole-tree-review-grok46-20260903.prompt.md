# Hostile review lane (source + reimplementation, decisive): WHOLE-MAJOR-TREE NECESSITY — is Moh's construction really universal over sibling factors; the orbit partition and q-root capacity; the recursion's soundness; the ODE consequence (3.7); the passport inequality (3.8); the recentring rule

The charged Sol report moh-program-review-sol56-20260903.md (§3.1, §3.3,
§5.1; drivers box/mohprog-drivers-20260903/) claims PROVED-IN-SOURCE (as a
local obligation) and MEASURED: at a major disc D_j with common leading
polynomial p_j (Prop 4.6, deg P_j = V_{j+1}d_j/d_{j+1}) and squarefree q_j
(deg Q_j = V_{j+1}(n − M_j)/d_{j+1}, containing every root of p_j, p_j not a
power of q_j), EVERY factor of p_j of multiplicity u > d_j/(n − M_j) defines
another major disc which must satisfy the same construction at the next
level (Prop 5.3 pp.180–183 applies to any factor above threshold; the p.200
Theorem (4): every subdisc with more than n/(n − M_j) roots of g extends the
tower); the p.201 conjugation makes an actual factorisation
P_j = b + A_j Σ_ℓ u_ℓ (b = multiplicity at the fixed root 0 ≡ P_j mod A_j;
u_ℓ per-root multiplicities of nonzero A_j-orbits), within the q-root
capacity A_j | Q_j − 1 (Lemma 5.2); minor factors stop (p.200(5)); at j = 2
every major child obeys (12)/(13); Prop 5.6 forbids the TYPED all-zero
continuation (the source-safe projection: if the mandatory residue
b = P mod A is positive and above threshold, an actual zero major sibling
exists; follow it recursively; if it reaches the bottom still major the
skeleton dies — C_ZERO_PATH). The finite consequence C_FULL_TREE: enumerate
every (3.3), embed the selected V_j as b or some u_ℓ, recursively check
every above-threshold b/u_ℓ. MEASURED: 658 → 60 rows / 12 classes at n ≤ 100
keeping Moh's six and giving exactly the (75,50) residue {M₂ = 55, V₂ ∈
{2,3}}; two independent recursions agree row-for-row. Sharpenings: (3.7)
from Appendix I Prop A.3's equation D(P,Q,p,q) = Ppq' − Qqp' = cp: at a
simple q-root a with u = mult_a p, (P − Qu)q_a(a) = c ⇒ P − Qu ≠ 0 at every
p-root (kills a minor sibling of multiplicity exactly P/Q) → 58 rows;
(3.8) a cyclic-quotient passport inequality d₊/g ≥ S from the logarithmic
derivative of p^Q/q^P (Davenport–Zannier; NOT in Moh) → 55; the exploratory
edgewise recentring (Prop 5.4's polynomial translation at every integral
nonpositive-radius sibling; Moh proves it only at the globally selected
disc) → 20 (OPEN[FULL-TREE-RECENTER]). On the campaign space: D = 105 and
D = 117 have NO survivor under bare C_FULL_TREE; D ≤ 200: 14,016 → 1,261
groups (passport screen).
Your task, hostile — SOURCE-FIRST and REIMPLEMENTATION-FIRST: re-transcribe Props 4.6, 5.2, 5.3, 5.4, 5.6, Lemma 5.2, the p.200 Theorem and Prop A.3 from the images BEFORE reading the charged §3; write your OWN whole-tree recursion from scratch (do not read tree-independent.py until yours runs) and diff survivors row-for-row against candidate-results.json; then answer, from the page images (refs/moh1983_jram340_
configurations_of_roots.pdf, page N = PDF page N−139; pdftoppm -r 300):
(a) THE UNIVERSAL QUANTIFIER. Does Prop 5.3 (pp.180–183) apply to ANY
factor π − C_r of multiplicity above threshold, or only to a chosen one
whose existence is asserted (Prop 5.2 "any subdisc can be used as D_{s−1}
if it contains more than the average number of roots")? Quote the exact
hypothesis; decide whether "every above-threshold sibling extends" is
Moh's statement, a consequence of his proof (the proof constructs D_{r−1}
from the chosen factor — does it use anything special about the choice?),
or an over-reading. Check the p.200 Theorem (4) quantifier ("if the number
of roots of g in E_i is > n/(n − M_r) then …") — is it "for every i"?
(b) THE PARTITION (3.3) and CAPACITY (3.4). Re-derive from the p.201 orbit
action and Prop 4.6: are the nonzero-orbit sizes exactly A_j (delta 17(j)
says yes); is b ≡ P_j mod A_j forced; is A_j | Q_j − 1 Lemma 5.2's content
(re-derive); can q have several fixed roots (q squarefree, roots of p ⊂
roots of q — what fixes the zero root count)? Are the "unused slots"
(q-roots with p-multiplicity 0) correctly allowed?
(c) THE RECURSION. When a sibling factor of multiplicity u becomes the next
major disc, what are ITS (M, d, V) data — is the child's Q_{j−1} determined
by u alone (as the DP assumes) and are the radii δ recomputed per branch
(Def 5.1(3) depends on the whole V-path down that branch)? Is the DP's
state (level, multiplicity) sufficient or does it forget the branch's own
δ-sequence / A-sequence? Construct a small worked example by hand (one of
Moh's six) and one excess row killed by the tree, tracing the sibling that
kills it.
(d) THE ODE STEP (3.7): re-derive (P − Qu)q_a(a) = c from D(P,Q,p,q) = cp
(Prop A.3 p.205 — is the right-hand side cp or c? quote) and check the
hypotheses (simple q-root; u ≥ 1); confirm it is exact and not the
strict-window restated.
(e) THE PASSPORT (3.8): is d₊/g ≥ S a correct necessary condition for
p^Q/q^P (the cyclic quotient of the Belyi map) — derive it or refute it;
type it (external, not Moh).
(f) THE RECENTRING RULE: exactly what Prop 5.4 proves, and whether the
edgewise extrapolation changes a quantifier (the report says it does).
(g) INDEPENDENT REPLAY: rerun candidate_eval.py / tree-independent.py
(charged drivers) and confirm 60/58/55/20 and the (75,50) residue; then
evaluate the screens on the D = 105 trio and D = 117 (trace WHICH sibling
kills each), and on the first four members of the A₂ = 6 ray
(n = 9(7t+6), t = 0..3) and of Sol's L = 8a+5 ray (a = 0..3) — do the rays
survive the sourced tree? Type each verdict. Typed block: PROVED-IN-SOURCE /
DERIVED / OVER-READING / EXTERNAL per component; promotion recommendation
(the campaign will move its frontier on this); bounded quantity + cheapest
test of every OPEN. Desk-scale (< 20 min one core, < 4 GB); no ledger
edits; no jc2-lean; do not read ideation-20260903T1015Z-* files or other
running lanes' reports.
Report: xmodel/whole-tree-review-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 25-40KB; 150 minutes.
charged_input=xmodel/moh-program-review-sol56-20260903.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=xmodel/branch-orbits-v2-review-gpt55-20260903.md
charged_input=xmodel/n6-family-review-grok46-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=box/mohprog-drivers-20260903/candidate_eval.py
charged_input=box/mohprog-drivers-20260903/tree-independent.py
charged_input=box/mohprog-drivers-20260903/candidate-results.json
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  {{LANE_INPUTS}}/moh-program-review-sol56-20260903.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
c61bb15528b25587578ac10101cb18267e83150fa6ea541e250f606e648d5418  {{LANE_INPUTS}}/branch-orbits-v2-review-gpt55-20260903.md
982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896  {{LANE_INPUTS}}/n6-family-review-grok46-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553  {{LANE_INPUTS}}/candidate_eval.py
c2a27632d54576abbca54b9f268a7fa5d2b144497a1e364c93102450a066baf9  {{LANE_INPUTS}}/tree-independent.py
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  {{LANE_INPUTS}}/candidate-results.json
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
