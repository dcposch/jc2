# Hostile review lane (fast): Sol's explicit unbounded (1)–(13) family with pinned N = 6 — verify the algebra symbolically in L, the census membership, and the orbit-admissible packets

Charged claim (blind Sol submission of round 20260903T1015Z, §2.3,
PROVED-HERE/UNREVIEWED): for every a ≥ 0 and L = 8a + 5, the skeleton
n = 21L, m = 14L, M_1 = −14L, M_2 = 7(3L+1)/4, M_3 = 21L − 2, s = 3, V_2 = 1,
V_3 = 5 satisfies Moh's printed (1)–(13) (as implemented in
box/moh_skeleton_full.py, census-rebase §1): d_2 = 7L, d_3 = 7, d_4 = 1; the
windows 7/2 < 5 ≤ 7 and 4L/(9L−1) < 1 ≤ 5L; δ_3 = −1, δ_2 = 2(3L−1)/(3(5L−1)),
δ_1 = 7/12; since L ≡ 5 (mod 8), A_2 = 3(5L−1)/4 and with Q = V_3 d_2/d_3 = 5L
condition (10) admits V_2 = 1; A_1 = den(A_2·7/12) ∈ {1, 2} and (12)/(13)
holds; q = (1 − δ_1)de/(d + e) = 1/2, u = V_3 K/d_3 = 5L; the formal (UNI)
packet k = 12 gives N = 6 exactly; degrees 105, 273, 441, …; the first 21
members pass the census implementation. Consequence claimed: "(1)–(13) +
integral pinned N" is cofinally nonempty, so a uniform theorem must use a
datum outside the scalar skeleton. Also relevant (charged): branch-orbits
v2's orbit-size law |O| = ∏_{j=2}^{s−1} ω_j (ω_j = A_j on (10), 1 on (11)),
exact s = 3 packing, under which the family's admissible packets are
k ∈ A_2·Z (if the D_2 → D_1 split is (10)-only) — at L = 5 this is the D = 105
group A with k = 18, N = 9, NOT k = 12.
Your task, hostile: (1) re-derive every displayed quantity symbolically in
L (sympy, exact) — d_j, the windows, δ_j from Def 5.1(3) as printed in
census-rebase §1, A_2, A_1 (which of {1,2}, as a function of a), (12)/(13),
(10)/(11) at j = 2, q, u — and state whether (1)–(13) hold for ALL a ≥ 0 or
only measured ones; check M_2 = 7(3L+1)/4 is an integer with d_3 = gcd(n,
M_1, M_2) = 7 exactly (not larger) and gcd(d_2, M_2) = d_3; check condition
(2) m ∤ n and (3)/(4)/(5)/(6) (3 ≤ s ≤ 5, d_s ≥ 4); check s ≤ 5 is not
consumed (it fails at D = 192 in general — irrelevant here since s = 3, but
say so). (2) Run box/moh_skeleton_full.py's census on n = 21L for
L = 5, 13, 21, 29, 37, 45 (K_min as appropriate) and confirm the family row
appears with full_ok; report wall-clock. (3) Under branch-orbits v2's law:
compute A_2 and the orbit-admissible N-set of the family per L (is k = 12
ever orbit-admissible? what is the smallest orbit-admissible N per L? does
the family stay alive at N ≥ 6 in the orbit-aware knapsack?), and say
whether Sol's consequence (cofinal nonemptiness) survives the orbit
correction — if the orbit-admissible N grows with L, the family does NOT
show fixed-N cofinality and the claim must be retyped; if it stays bounded,
state the bound. (4) Is there a second, orbit-consistent family with N
bounded in L (search the census for s = 3, q = 1/2 rows with A_2 | small k,
D ≤ 500 if cheap)? Typed verdict block (CONFIRMED / GAP / REFUTED per
item), bounded quantity + cheapest test of every OPEN. Desk-scale (< 10 min
one core); no ledger edits; no jc2-lean; do not read other
ideation-20260903T1015Z-* files than the charged Sol one; do not read other
running lanes' reports.
Report: xmodel/n6-family-review-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 10-18KB; 45 minutes.
charged_input=xmodel/ideation-20260903T1015Z-sol56.md
charged_input=xmodel/branch-orbits-v2-grok46-20260903.md
charged_input=box/branch-orbits-v2-20260903/knapsack.py
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/moh_skeleton_full.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  {{LANE_INPUTS}}/ideation-20260903T1015Z-sol56.md
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  {{LANE_INPUTS}}/branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  {{LANE_INPUTS}}/knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
```
