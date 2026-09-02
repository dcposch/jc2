# Research lane: BRANCH-ORBITS — is (UNI) a theorem? How many Galois orbits of bottom-major discs can a degree-minimal Keller pair have, and what does that do to the integrality filter?

Reviewed (integration #17): N = sum_B V_2(B) q(B), q = (1-delta_1)de/(d+e),
sum_B V_2(B) <= u, over the bottom-major discs B of Moh's tree; the
per-disc contribution is pinned (D1-PIN). The (UNI) hypothesis — all
bottom-major discs carry the same lower-V datum (V_2..V_{s-1}, hence
the same q) — is CONFIRMED inside one Galois orbit of C((t)) acting on
the tree (an isometry permuting bottom discs, preserving (a_1, delta_1))
and is NOT a theorem across orbits. OPEN[BRANCH-ORBITS] (review sec.13):
bounded quantity = the number of Galois orbits of bottom-major discs, an
integer in {1, ..., u}, and the partition of sum_B V_2(B) <= u among
them. Under (UNI) the integrality filter kills 60% of groups at D <= 120
(no degree emptied); without it, the general knapsack kills ~25%.
YOUR TASK (hostile to your own conclusions; Moh 1983 in refs/, hash;
read Def 5.1 p.179, Prop 4.4/4.6, Lemma 6.1/Cor 6.1 p.194 from the
page images):
(1) STRUCTURE. In Moh's gauge the top form is l(g) = alpha H^{d_s}... with
    H = L_1^u L_2^v (two points at infinity, NU-TWO, u > v). The major
    tower D_s ⊃ ... ⊃ D_1 is built along one branch; its conjugates under
    the Puiseux monodromy (t -> zeta t) give the other bottom discs of
    the same orbit. Determine, from the skeleton data (n, m, M_j, d_j,
    V_j), how many bottom-major discs one orbit contains (in terms of the
    d_j chain: d_1 = n, d_{j+1} = gcd(d_j, M_j), and the V_j), and hence
    how many orbits are needed to reach sum_B V_2(B) = the total count of
    bottom-major roots ue (or less). Is the number of orbits FORCED to be
    1 by the tower structure (all u copies of L_1 conjugate), or can the
    u major branches at the L_1 point split into several orbits with
    DIFFERENT lower-V data? Quote Moh where he treats "the" branch.
(2) If several orbits are possible: state the exact packet structure
    (orbits O_k with multiplicities, each with its own (V_2..V_{s-1})_k in
    the windows and its own q_k; the constraint sum_k |O_k| V_2,k <= u),
    and prove or refute that each orbit's V-data must satisfy Moh's
    windows independently.
(3) COMPUTE. Implement the orbit-aware exact knapsack (Fractions; DP over
    (roots used, fractional part); state caps) in the d1floor framework
    and run it at the MOH-SHARP-2 degrees {105, 108, 112, 117, 120} and
    at D <= 100 with N an integer >= 6 (campaign frontier; N <= 5 closed).
    Report per degree groups / killed / surviving / capped; compare with
    the (UNI) numbers (105: 264/209, 108: 824/419, 112: 1163/795, 117:
    60/47, 120: 4104/2390 under H2) and with the general knapsack
    (24.7% at D in [48,79]); state whether any degree empties.
(4) If the orbit count is forced to 1 (so (UNI) is a THEOREM), say so
    with the proof and the consequence: the (UNI) kills become
    unconditional, and the surviving V-packets at D = 105 are the
    complete realisation list.
Discipline: PROVED-HERE/UNREVIEWED typing; state the bounded quantity of
every OPEN you raise; desk-scale CAS (< 30 min one core, < 4 GB); do not
edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/branch-orbits-grok46-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-opus5.md
charged_input=box/moh_skeleton_N.py
charged_input=box/d1sub-drivers-20260902/d1floor.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
0916a85a7a8090d04461fa356518fb2ffd877374d1b8452a2b808d6f77156934  {{LANE_INPUTS}}/ideation-20260902T1608Z-opus5.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
```
