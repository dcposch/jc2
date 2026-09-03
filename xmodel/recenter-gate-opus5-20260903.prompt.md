# Hostile gate (page images): does OPEN[FULL-TREE-RECENTER] close POSITIVE? — Fable's claim that a nonzero label at an intermediate disc of radius δ_j = 0 is removable by y ↦ y − c, so that Prop 5.6 kills the path and the POLY column of the whole-tree screen becomes operative

Charged claim (ideation-20260903T1200Z-fable5.md §2.1, PROVED-HERE/UNREVIEWED;
you may read that file — it is charged — but no other ideation-20260903T1200Z-*
file and no in-progress lane report): in a whole-tree sibling path from the
Lemma 5.3 top chart to a bottom major disc D₁ with all labels zero except one
nonzero label c at a level j with δ_j = 0 (radii strictly increase down the
tower so at most one intermediate level has δ_j = 0; δ = −1 only at the top),
the affine change α: y ↦ y − c (Moh p.190's y ↦ y − ax − b with a = 0)
preserves Moh's gauge (monic, deg = deg_y, degrees, J) and the tower (Def
5.1(1)–(3) intrinsic; the term c·t⁰ lies inside every disc of radius < 0 above
level j and is the label at level j), makes the path zero-typed, and then the
p.189 proof of Prop 5.6 runs verbatim ((i) pure x^l term of g at the bottom
general point, (ii) Prop 4.1(1) balance nλ + (−M₁)λ − 1 = −2 + δ₁, (iii)
δ₁ ≥ δ_{s−1} ≥ 0 ⇒ l = 1 and δ₁ ≤ (−M₁)λ < 0, contradiction); a kill needs one
centred path and different killing paths may use different constants, so the
reviewers' worry that "the automorphism must centre every sibling chart" does
not arise; a nonzero label at a NON-integral radius is NOT removable (c·t^δ,
δ ∉ Z, survives every polynomial change) and the frozen POLY implementation
applies the rule only at integral δ. MEASURED (Fable): 38 of the 52 excess
C_FULL_TREE_ODE rows at n ≤ 100 carry a δ = 0 nonzero selected edge and they
are exactly the 38 POLY kills; residue 14 rows ((90,60),(96,64),(96,72), all
s ≥ 4, u_s = 1); at s = 3 the screen is then EXACT (Moh's six). Task: (1) open
Moh pp.164–166 (Prop 4.1), 185–186 (Lemma 5.3), 189–190 (Prop 5.6 and the
p.190 recentring) as page images (pdftoppm -r 130 on the charged PDF; state
which pages you opened) and check every step of the claim against the print:
gauge preservation, tower intrinsic-ness under y ↦ y − c (in particular
whether Def 5.1's radii/labels are defined relative to a fixed chart or
intrinsically, and whether the top-chart danger flag of Lemma 5.3 is
chart-covariant), the three ingredients (i)–(iii) of the p.189 proof, and
whether Prop 5.6 as printed requires the path to be zero-typed in the
ORIGINAL chart or in any admissible chart; (2) check the claim that only
δ_j = 0 is integral among intermediate radii (from Def 5.1(3) and the
strict monotonicity) and that the frozen full_tree_partition.py POLY rule
fires only at integral δ (read the code; replay the 38/52 and the 0-mismatch
count from the charged witness JSONs); (3) verdict: CONFIRMED (then the POLY
column is promotable: state the exact operative numbers at n ≤ 100 and
D ≤ 200 from the charged audit JSONs) / GAP (name the step and its cheapest
test) / REFUTED (counter-argument or counterexample path); (4) check
whether the K = 16 ray (δ₂ = 1/4, non-integral) and Moh's six are untouched;
(5) type every claim; FALLACY-v2 applies. Desk-scale; no ledger edits; no
jc2-lean. Drivers to box/recenter-gate-20260903/.
Report: xmodel/recenter-gate-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 60 minutes.
charged_input=xmodel/ideation-20260903T1200Z-fable5.md
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json
charged_input=box/mohprog-drivers-20260903/full-tree-polynomial-ode-excess-witnesses.json
charged_input=box/mohprog-drivers-20260903/full-tree-polynomial-ode-n100-audit.json
charged_input=xmodel/whole-tree-review-opus5-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/recenter-gate-opus5-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
8d16a66112afda4aafa4b81a55a07602677d3707d60a150e3d13edb8be467e80  {{LANE_INPUTS}}/ideation-20260903T1200Z-fable5.md
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5  {{LANE_INPUTS}}/full-tree-ode-excess-witnesses.json
88e5f074b7667b537bb463e11985f80a005cc4b885c416b356bc60ed96b29ec2  {{LANE_INPUTS}}/full-tree-polynomial-ode-excess-witnesses.json
b16830edead6844380c902caf052973280bb935943a3e0b54234c27a5b31d8d4  {{LANE_INPUTS}}/full-tree-polynomial-ode-n100-audit.json
27551a88ab6ee9f62a5606010adcd9d4a1fd4411a09d97c699e13a67c84f7096  {{LANE_INPUTS}}/whole-tree-review-opus5-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
