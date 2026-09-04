# STRUCTURAL/census lane (Opus's (H1) new lead, round §5.2; re-prices the whole flagship in one lane): test the skeleton predicate NONRES(S) :≡ d_s ∤ u_s·j for all 1 ≤ j ≤ v_s (⟺ u_s > (g−1)·v_s, g = gcd(u_s, v_s)) — derived from the banked ladder closed form 9(99 − 3n − 11i) = (n/d_s)(n − u_s·j − d_s·i) (17(hhhhh)) — across the full D ≤ 200 u_s ≥ 2 census, and decide whether NONRES(S) is (a) TRUE for every genuine-split skeleton (⇒ the ladder pivot is nonzero ⇒ an inhomogeneous Jacobian row always survives elimination ⇒ a uniform arithmetic kill mechanism for (H1), the shape 17(ooooo) said was missing), (b) FALSE for some, pinpointing exactly which skeletons the ladder does NOT kill (they need a different row), or (c) NECESSARY-BUT-NOT-SUFFICIENT (the predicate holds but does not by itself give the unit ideal)

OPERATIONAL: skeleton first; foreground, ≤ 30 min per job; ≤ 3 cores. The
predicate is arithmetic — this is mostly enumeration + a few exact checks, not
heavy CAS. Task: (1) enumerate the D ≤ 200 census of u_s ≥ 2 skeletons from
box/moh_skeleton_full.py (the 166 groups / ~274 reduced pairs; state the exact
count and how you generate it) and compute NONRES(S) for each — tabulate the
TRUE/FALSE split and the u_s > (g−1)v_s form; (2) VERIFY the predicate's
derivation: confirm 9(99−3n−11i) = (n/d_s)(n − u_s·j − d_s·i) on the banked
(99,66) ladder (d_s=11, u_s=3, v_s=8: the 66 δ=5/2 and 31/35 δ=2 pivots) and on
D=108 (d_s?, u_s=2, v_s=7) — does the same closed form reproduce the D=108
incidence residues? if not, the predicate is (99,66)-specific — say so; (3) for
the skeletons where NONRES(S) is TRUE, is the ladder row actually IN the joint
ideal (a necessary Jacobian row of the chart), making its non-vanishing a real
kill? check on (99,66) (yes, 6264/64) and on ≥ 2 other census skeletons by
building just the ladder rows (not the full chart); (4) for NONRES(S) FALSE
skeletons, exhibit the smallest and state what row family must kill it instead;
(5) verdict: NONRES(S) is a SUFFICIENT uniform kill / NECESSARY-not-sufficient
/ (99,66)-specific — and the fraction of the census it covers (re-pricing the
flagship: how many of the 274 pairs does the arithmetic predicate kill for
free?); FALLACY-v2 applies (a predicate holding is not a kill unless the row is
sourced-necessary AND its non-vanishing gives the unit ideal). ≤ 150 min; no
ledger edits; no jc2-lean; no ideation-* files; no in-progress lane reports.
Drivers to box/h1nonres-20260903/.
Report: xmodel/h1-nonres-census-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-30KB; 150 minutes.
charged_input=xmodel/ideation-20260904T1200Z-opus5.md
charged_input=xmodel/g9966-chart-necessity-opus5-20260903.md
charged_input=xmodel/two-place-obstruction-core-sol56-20260903.md
charged_input=xmodel/minor-residue-formula-opus5-20260903.md
charged_input=xmodel/minor-empty-disc-sol56-20260903.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf
charged_input=FALLACY-v2.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first, MECHANICALLY and without retyping any digit: the lane receipt `xmodel/h1-nonres-census-sol56-20260903.run.v2` (readable in your sandbox) carries `charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines that reproduce this block; generate the manifest from it with awk and run `sha256sum -c`; stop only on a real content mismatch, not on a transcription slip of your own — recheck once before stopping:

```text
a32a3eb996435facabb7a39baf3972178e289009967e29f45be2500960633aa0  {{LANE_INPUTS}}/ideation-20260904T1200Z-opus5.md
37beed7ace5aafced312725fcca2e43aa316c19cecc387ef5aafa1c0809bb628  {{LANE_INPUTS}}/g9966-chart-necessity-opus5-20260903.md
3f16d1f776a6bd37525302f4a9c15639db5bee03f3b4bc3cd29063c2fa252a11  {{LANE_INPUTS}}/two-place-obstruction-core-sol56-20260903.md
b009dee9b3aee4c48ab97a4c0a4f61d41c3430923461b7fce22077fb9eb2547f  {{LANE_INPUTS}}/minor-residue-formula-opus5-20260903.md
ee001adf67c83b9d53a05bd3da3a12b3186c278f600c9448809dc577cc41aa54  {{LANE_INPUTS}}/minor-empty-disc-sol56-20260903.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  {{LANE_INPUTS}}/FALLACY-v2.md
```
