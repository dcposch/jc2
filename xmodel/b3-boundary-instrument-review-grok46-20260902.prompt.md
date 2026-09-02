# Hostile review lane: B3-BOUNDARY-INSTRUMENT — nine bridges, two controls, the census, and GAP-CANDIDATE[BI-ATTACH]

The charged producer report (Opus 5, flagship) extracts the degree-free
part of the Domrina–Orevkov determinant/transfer package at general N and
feeds it the campaign's affine (B3) ledger. Claims (all PROVED-HERE /
UNREVIEWED): BI-1 (DO's formula (9) at the target curve is [P3]:
W + a = N with dicriticals the n >= 2 part and E-bar_X the n = 1 part);
BI-2 (transverse degree at a mark over p = ramification index e_y of that
place of E over infinity); BI-3 (fibre-at-p local-degree ledger
(s_l mu_l) ∪ (e_y) summing to N under (H-∞)); BI-4 (E-CHARGE transported
to the boundary: affine excess r_p[(r_p−1)W + K_p], at most K_p charged to
the k_t); BI-5 (mark saturation at v_0; ramification profile of the
compactified normalisation of E over ∞ is {n(v~)^{m(v~)}}); BI-6 (unit
lifts of E transport target determinants; DO's coprimality kills are
kills of the multiplicity of E's sheets); BI-7 (the disconnected reading
of B3-E-GENUS can never contradict j <= a — route closed negative); BI-8
(spine-depth cap #forks <= N − s_l mu_l); BI-MERIDIAN (generic meridian
cycle type 1^a · prod (mu_l)^{s_l}); EXTRACTION-1 (which DO ingredients
are degree-free, with MI Lemma A supplying the single-point-at-infinity
hypothesis at every N); the CENSUS closed form Census(N) = sum_m
floor(N/m) Rows(m), Rows(m) = [z^{m+2}] f_m(z)^3 with Census(4) = 35
matching DO; CONTROL 1 (N = 4: reproduces (mu,corr) = (2,1) and
identifies DO's "the other two sheets"); CONTROL 2 (Sol's Γ curve
y^2 = x^3(x−1)^2 passes every item); the N = 5, 6 runs (no empty window;
the N = 6, a = 4 three-cusps-plus-node cell forced to j >= 2).
And one GAP-CANDIDATE[BI-ATTACH]: the (m,n) split of the dicritical-
incident boundary block B_l is not fixed by the frozen DO replay; the
lane's local computation gives (m,n)(B_l) = (mu_l, s_l), the TRANSPOSE of
what the replay's §6 assembly presupposes ((s_l, mu_l)); in an explicit
resolved model the component l meets at p~ is CONTRACTED, so the naive
identification of B_l is unlicensed. Only Deg B_l = s_l mu_l is safe.

Your task, hostile and computational, with ONE mandatory item first:
(0) BI-ATTACH versus the CHECKED N = 4 CHAIN. The campaign's
    N=4-CHECKED-CLOSED rests on the Domrina–Orevkov I replay (charged).
    Decide, against that replay's text: (a) does DO's §6 assembly or any
    of Lemmas 10–15 consume the (m,n) split of the dicritical-incident
    block in a load-bearing way, or only its Deg? (b) if the split is
    consumed, is the lane's transpose right (recompute the local model:
    monomial F at a transverse crossing of l with a single L~_∞-
    component; n(B_l) = ord_{B_l} F^*(v_0), m(B_l) = degree of F on B_l)
    and does the N = 4 kill survive with the corrected split (it is the
    SET §§2–7, per the lane)? (c) what exactly is the contracted-
    component subtlety, and does it change any determinant DO uses?
    Type the outcome: NO-GAP (split not load-bearing) / GAP-REPAIRED /
    GAP-OPEN with the exact lemma affected. This is the only item that
    can touch the checked ledger; do it before anything else.
(1) BI-1..BI-8, BI-MERIDIAN, EXTRACTION-1: CONFIRMED / GAP / REFUTED
    per item with the exact line and the repair; state each item's
    hypotheses ((H-∞), H2, SCOPE[B3-QH]).
(2) The census closed form: recompute Rows(m) for m <= 6 and Census(4),
    Census(5), Census(6) independently; confirm Census(4) = 35 and the
    (4,1) sub-count 23 against the replay.
(3) CONTROL 1 and CONTROL 2: replay the substituted package at N = 4 and
    on Γ (its singularity data, y_0, chi_c = 1 − 4k, genus/ends, the two
    index-1 marks, the three E-bar_X branches of degrees 1; 2, 2).
(4) The N = 5, 6 runs: recompute the (B3) profile lists (3 and 8) and the
    boundary ledgers; confirm no empty window and the j >= 2 constraint
    at the non-generic N = 6 cell.
(5) Assess the successor (OPEN[BI-CENSUS-DEG5-DEG6] with BI-1/5/8
    substituted; settle BI-ATTACH first) for well-posedness.
Deliver a typed verdict block with a promotion recommendation per item
and the BI-ATTACH outcome on its own line. Desk-scale CAS only; state
the bounded quantity of any OPEN you raise; do not edit canonical
ledgers; do not inspect jc2-lean.
Report: xmodel/b3-boundary-instrument-review-grok46-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/b3-boundary-instrument-opus5-20260902.md
charged_input=xmodel/do1-mu2-replay-sol56-20260901.md
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-review-grok46-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  {{LANE_INPUTS}}/b3-boundary-instrument-opus5-20260902.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  {{LANE_INPUTS}}/do1-mu2-replay-sol56-20260901.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  {{LANE_INPUTS}}/b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  {{LANE_INPUTS}}/b3-e-geometry-review-grok46-20260902.md
```
