# Source + measurement lane: the P202-10 audit — Sol's sharpest candidate gate (M_2 > n − d_2 ∧ forced-(10) at every level) leaves Moh's six rows plus four extras; reconstruct the factor data of those ten rows from Props 5.3/5.6 and Appendix II; run the (75,50,40,1) falsifier against every candidate gate

Round 20260903T1015Z produced four MEASURED candidate gates for
OPEN[MOH-PROGRAM] (bounded 652 excess rows at n ≤ 100), all keeping Moh's
six p.202 rows (charged submissions; base 658 rows / 63 classes on
box/moh_skeleton_full.py, census(n, Kmin=2, full=True)):
  Sol:   M_2 > n − d_2  (57 rows / 16 classes)  ∧  the printed nonzero
         branch (10) chosen at EVERY level j (156 / 40)  →  10 rows / 6
         classes = Moh's six + four extras: (96,64) M = (68,94) V = (2,3);
         (96,64) (76,94) (3,3); (96,64) (72,94) (2,7); (100,40) (88,98) (3,3).
         Also measured, unlicensed: A_{s−1} | (n − m) (181 rows / 29 classes,
         selects exactly the two (75,50) controls).
  Fable: M_2 > m (94 / 32; + integral N ≥ 6 → 33 rows, 28 extras).
  Opus:  MOH-INCREMENT A_j ≥ 2 ∧ NOT-ALL-(11) ∧ MAJOR-MULT V_j ≥ 2 (51 / 13).
  Sol's FALSIFIER: the (1)–(13) row (75, 50, M_2 = 40, V_2 = 1) has A_1 = 2 and
  an exact cyclic bottom solution p(π) = π³ + (3b/2)π, q(π) = π² + b,
  D(3,2,p,q) = −3b², Res = b³/4, squarefree/coprime, with the C_2 symmetry —
  so no LOCAL bottom-level filter kills it honestly.
The Moh PDF is at refs/moh1983_jram340_configurations_of_roots.pdf (page N
= PDF page N−139; render with pdftoppm -r 300 and read the images).
YOUR TASK:
(1) REPRODUCE the four gates' counts fail-closed (6/6 kept; (75,50)
    residue) and print the 2×2×2 incidence of Sol's two clauses with
    Fable's M_2 > m and Opus's MAJOR-MULT on the 658 rows: which implies
    which on the census; the exact symmetric difference between Sol's ten
    and Fable's 33.
(2) SOURCE-AUDIT Sol's two clauses: (a) "forced-(10) at every level" — is
    choosing the (10) branch (a factor π − a, a ≠ 0) at every j ≥ 2 licensed
    by Prop 5.6 (p.188–189: σ_1 = πt^{δ_1} is impossible) or by Prop 5.3's
    construction of p(π) (pp.181–185), or is it an over-reading (Prop 5.6
    forbids ALL levels taking (11), not ANY level)? Quote. (b) M_2 > n − d_2
    — find or refute a printed source (Def 5.1, Prop 5.5, the p.200
    Theorem, Lemma 6.1 δ_{s−1} ≥ 0 → an inequality on M_{s−1}?). Quote.
(3) THE TEN ROWS: for each of the six printed rows and the four extras,
    reconstruct from the page images the data Moh attaches (p.202 table
    columns: M_2, V_2, δ_2, δ_1, and the Appendix II transformed signature
    where applicable) and decide, row by row, which exact printed assertion
    kills the four extras and spares the six — or state that none does
    (then either Moh's program used an unprinted rule, or p.202 is
    incomplete: say which reading the evidence favours, typed).
(4) THE FALSIFIER: run the (75,50,40,1) row through all four gates (it is
    excluded by Sol's clause M_2 > n − d_2 = 75 − 25? — compute d_2 and say
    which clause kills it); then attempt to EXTEND Sol's exact bottom
    solution through the one remaining major level (Prop 5.3's construction
    at r = 2 with the row's V_3, δ_2) as a desk computation: does the
    two-level tower glue for some b, or does the r = 2 step fail — and is
    that failure one of the printed conditions or a genuinely global one?
Typed block per item: PROVED-IN-SOURCE / DERIVED / NOT-IN-SOURCE /
MEASURED; bounded quantity + cheapest test of every OPEN; desk-scale
(< 15 min one core); no ledger edits; no jc2-lean; do not read other
ideation-20260903T1015Z-* files than the three charged; do not read other
running lanes' reports.
Report: xmodel/p202-ten-rows-gate-audit-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 15-25KB; 90 minutes.
charged_input=xmodel/ideation-20260903T1015Z-sol56.md
charged_input=xmodel/ideation-20260903T1015Z-fable5.md
charged_input=xmodel/ideation-20260903T1015Z-opus5.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  {{LANE_INPUTS}}/ideation-20260903T1015Z-sol56.md
486b0192d6cb1f3e064e00d16b57877ed67a2360543d8ec662c837afe5fc6456  {{LANE_INPUTS}}/ideation-20260903T1015Z-fable5.md
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
