# Hostile review lane: BRANCH-ORBITS v2 (Grok) — (UNI) is not a theorem; the orbit size |O| = ∏ A_j on (10)-levels; per-orbit (8)–(13); the exact s = 3 packing; the orbit-aware knapsack; D = 88 emptied in [6,16]; the D = 105 trio collapses to single orbits with N = 9

The charged Grok report branch-orbits-v2-grok46-20260903.md (PROVED-HERE/
UNREVIEWED + MEASURED; Moh pages read at 300 dpi) claims: (1) the u copies
of L_1 in H = L_1^u L_2^v occupy ONE disc D_{s−1} (Prop 4.5 + p.200 Theorem
(6): deg q = 2 at δ_s = −1; Lemma 6.1 makes D_{s−1} Galois-fixed), not u
conjugate discs; (2) the orbit size of a bottom-major disc is
|O|(D_1) = ∏_{j=2}^{s−1} ω_j, ω_j = A_j on a (10)-level (free multiplicative
action of the order-A_j automorphism on a ≠ 0 — the orbit is EXACTLY A_j,
not a divisor) and ω_j = 1 on the (11)-level (π fixed); (12)/(13) is the
internal condition inside D_1 (A_1 is NOT an orbit size of discs); (3) each
orbit's V-data must satisfy (8)–(13) on its own; joint constraint = packing
Σ_k |O_k| V_2^{(k)} ≤ u, EXACT at s = 3 (deg p at the unique D_2 = u on
305/305 assignments), a relaxation at s > 3 (OPEN[NESTED-PACK]); (4)
MEASURED on the (1)–(13) census D ≤ 120 (1,189 groups; census-rebase §6
reproduced to the unit): orbit-aware UNB knapsack 681 alive at N ≥ 6 / 575 in
[6,16]; s = 3 Z01 exact 173/138 of 274; D = 88 EMPTIED in [6,16] (s = 3
exact: |O| = 14, N_orb = {18} only; lives at N ≥ 6); D = 48 emptied; no
D > 100 empties; the D = 105 trio: each ONE orbit, k = 18, 13, 17, N = 9
(the UNI interval 6..12 on M = [28,103] V_s = 5 REFUTED); D = 117 Z01 drops
4 → 3 ((11)-only row: N = 9/7); D = 112 29 → 22 in [6,16]; the six Moh rows'
orbit N-sets {9},{},{10},{9},{8},{16} match integration #17 A.8 at N ≥ 6
except (84,56) M_2 = 72 loses the UNI 5; controls 336/0.
Your task, hostile: CONFIRMED / GAP / REFUTED per claim with page/line and
repair. Mandatory: (a) re-read Prop 4.4/4.5/4.6 (pp.168–171), p.173, Def
5.1 (p.179), Lemma 6.1 (p.194), the p.200 Theorem and (8)–(11) (p.201) from
the images (refs/moh1983_jram340_configurations_of_roots.pdf, page N = PDF
page N−139) and reprove (1) and (2): is the action on the π-coordinate of a
factor π − a genuinely free of order exactly A_{r−1} (what if a is a root
of unity of smaller order, or A_{r−1} shares factors with the centre's
own ramification?); can a (10)-level carry SEVERAL orbits of the same
multiplicity (the report says yes) and does that change |O|; (b) reprove
"(12)/(13) is internal to D_1" against p.188; (c) rerun
box/branch-orbits-v2-20260903/knapsack.py (charged) and confirm the totals
681/575, 173/138, the D = 88 hand check, the trio packets, and the D = 117
(11)-only kill; (d) attack the exactness claim at s = 3 (Q = u on all s = 3
assignments — prove it algebraically from u = V_s K/d_s); (e) attack the
D = 88 kill: is the only orbit-admissible N really 18 (could a second
orbit type or the (11) centre give N ∈ [6,16])?; (f) say whether (UNI)
survives in any weaker true form (e.g. one orbit when A_2 = u/V_2) and what
that does to the record's UNI N-sets. Typed verdict block; promotion
recommendation per item; bounded quantity + cheapest test of every OPEN.
Desk-scale (< 15 min one core, < 4 GB); no ledger edits; no jc2-lean; do
not read any ideation-20260903T1015Z-* file or other running lanes' reports.
Report: xmodel/branch-orbits-v2-review-gpt55-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=box/branch-orbits-v2-20260903/knapsack.py
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  {{LANE_INPUTS}}/knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
