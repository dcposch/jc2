# Research lane: B3-CENSUS-DEG5-DEG6 — the Domrina–Orevkov census at N = 5, 6 with the campaign's spine data substituted

The (B3) boundary instrument (charged producer + its review: nine
bridges CONFIRMED with scopes; GAP-CANDIDATE[BI-ATTACH] REPAIRED — the
dicritical-incident object is DO's Lemma 6 constant Deg-2 block, the
transpose is the Cor-4-excluded fork; the N = 4 kill is the lemma SET
DO I §§2–7; (H-∞) is NOT promoted at N = 4) says what an all-N (B3) kill
costs: DO's local census grows as Census(N) = sum_m floor(N/m) Rows(m),
Rows(m) = [z^{m+2}] f_m(z)^3 (35 at N = 4, 86 at N = 5, 287 at N = 6),
and the affine data bound only the assembly depth (#forks <= a, BI-8),
not the census. The review declares the successor WELL-POSED in exactly
this form: run the census at Deg <= 5 and Deg <= 6 with the SPINE data
substituted from the start — BI-1 (sum Deg v~ = N split as W + a = N,
dicriticals the n >= 2 part, E-bar_X the n = 1 part), BI-8 (#forks on a
spine <= N − s_l mu_l = a for one dicritical), the degree-free
determinant package (det L = −1, det R_a = 1, pairwise-coprime branch
determinants, Prop 3, Lemmas 1–5, the edge formula) — and NOT as a
substitution of the unpromoted v_0 profile list.

Your task, computational and exact:
(1) Enumerate the raw census rows at Deg <= 5 (86) and Deg <= 6 (287)
    from the closed form's generating construction (reproduce 35 at
    N = 4 and the (4,1) sub-count 23 as controls against the charged
    replay).
(2) For every (B3) profile THEOREM PROFILE admits at N = 5 (3 types) and
    N = 6 (9 types — the review found the charged list missed one cell
    with cap 3; recompute the list yourself), substitute the spine data:
    W = N − a, the dicritical (s_l, mu_l) with 2 sum s_l <= W and
    mu_l >= 2, the fibre partitions over the cusp and the nodes as the
    cage pins them, BI-8's fork cap, and BI-1's split. Prune the rows.
(3) Assemble the surviving rows into global boundary graphs exactly as
    DO I §6 does at N = 4 (six graphs there), then apply the degree-free
    analogues of Lemmas 10–15 (state each lemma's hypotheses and whether
    it is degree-free; the checked replay's repairs — Prop 4, Lemma 7,
    Cor 5, the delta(ab) > 0 step, the three companion cases, the Lemma
    13 citation — are BINDING and must be respected). Do NOT invoke a
    general-N Corollary 4 without the split settled per the review.
(4) Outcome: either the first EMPTY window in N for (B3) — say exactly
    which lemma fires on which surviving graph at N = 5 and at N = 6 —
    or the exact list of surviving global graphs per profile with the
    boundary datum each still needs (typed OPEN with its bounded
    quantity). Controls: the N = 4 run must reproduce the (mu, corr) =
    (2,1) kill through the same pipeline; Sol's Γ curve must not be
    killed by any step that does not use a Keller-only hypothesis.
(5) Report the growth honestly: how many rows survive pruning at N = 5,
    6, and what the same pipeline would face at N = 7 (33 profiles,
    717 rows) — the number is the information.
Discipline: consume the bridges at the review's CONFIRMED scopes (BI-3
and BI-5 under (H-∞) only; do not assume (H-∞) at N = 4); DO I through
the charged replay only; no Z(G) = 1, no case (A), no A2 cells, no
(B2) rows. Pure python + sympy, exact integer arithmetic, desk-scale
(< 15 min, < 4 GB per job; larger enumerations are a job spec for the
coordinator — box01 is free). State the bounded quantity of every OPEN
you raise; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/b3-census-deg5-deg6-sol56-20260902.md
Seal-at-completion; bounded writes; target 20-35KB.
charged_input=xmodel/b3-boundary-instrument-opus5-20260902.md
charged_input=xmodel/b3-boundary-instrument-review-grok46-20260902.md
charged_input=xmodel/do1-mu2-replay-sol56-20260901.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  {{LANE_INPUTS}}/b3-boundary-instrument-opus5-20260902.md
048667793c3d34fc568269602fd8c786e9fab09ebbfb9ccd308041bb2cf6bc8f  {{LANE_INPUTS}}/b3-boundary-instrument-review-grok46-20260902.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  {{LANE_INPUTS}}/do1-mu2-replay-sol56-20260901.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
```
