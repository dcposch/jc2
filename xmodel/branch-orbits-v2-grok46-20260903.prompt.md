# Research lane: BRANCH-ORBITS v2 — is (UNI) a theorem? Galois orbits of bottom-major discs, and the orbit-aware exact knapsack on the TRUE (1)–(13) census

Relaunch of the stuck-and-killed branch-orbits-grok46-20260902 lane
(NO-REPORT), now on the rebased census. Reviewed (integration #17 and
delta (h)): N = Σ_B V_2(B) q(B), q = (1−δ_1)de/(d+e), Σ_B V_2(B) ≤ u,
over the bottom-major discs B of Moh's tree; the per-disc contribution
is pinned (D1-PIN). The (UNI) hypothesis — all bottom-major discs carry
the same lower-V datum (V_2..V_{s−1}, hence the same q) — is CONFIRMED
inside one Galois orbit of C((t)) acting on the tree and is NOT a theorem
across orbits. OPEN[BRANCH-ORBITS]: bounded quantity = the number of
Galois orbits of bottom-major discs, an integer in {1, …, u}, and the
partition of Σ_B V_2(B) ≤ u among them. The admissible space is now Moh's
(1)–(13) (box/moh_skeleton_full.py, charged; census-rebase §1 for the
verbatim conditions): 1,189 groups at 48 ≤ D ≤ 120, 670 alive at N ≥ 6
under the pinned-N knapsack, 589 (UNI) / 648 mixed in [6,16]; D = 105 → 3
groups (m = 70, K = 35, (d,e) = (2,3); M = [28,103] V_s ∈ {5,6},
M = [40,103] V_s = 4). The Moh 1983 PDF is available at
refs/moh1983_jram340_configurations_of_roots.pdf (sha256 6c8847a8…;
journal p.N = PDF page N−139); render pages with pdftoppm -r 300 -png and
read the images (pdftotext drops display formulas): Def 5.1 p.179,
Props 4.4/4.6, Lemma 6.1/Cor 6.1 p.194, the search pp.200–202.
YOUR TASK (hostile to your own conclusions):
(1) STRUCTURE. In Moh's gauge l(g) = αH^{d_s}…, H = L_1^u L_2^v (NU-TWO,
    u > v). The major tower D_s ⊃ … ⊃ D_1 is built along one branch; its
    conjugates under t ↦ ζt give the other bottom discs of the SAME orbit.
    Determine from the skeleton data (n, m, M_j, d_j, V_j) how many
    bottom-major discs one orbit contains, hence how many orbits are
    needed to reach Σ_B V_2(B) = the total count of bottom-major roots
    (ue or less). Is the orbit count FORCED to be 1 by the tower
    structure (all u copies of L_1 conjugate), or can the u major
    branches at the L_1 point split into several orbits with DIFFERENT
    lower-V data? Quote Moh where he treats "the" branch, and where
    Def 5.1 / Prop 4.4 fix the count of discs at each level.
(2) If several orbits are possible: the exact packet structure (orbits
    O_k with multiplicities, each with its own (V_2..V_{s−1})_k in Moh's
    windows AND satisfying (8)–(13) independently — prove or refute that
    each orbit's V-data must satisfy (8)–(13) on its own; note (12)/(13)
    is a condition at r = 2 on A_1, which depends on the orbit's δ_1).
(3) COMPUTE. Implement the orbit-aware exact knapsack on the (1)–(13)
    space (Fractions; DP over (roots used, fractional part); state caps)
    using box/moh_skeleton_full.py's enumeration, and run it at
    48 ≤ D ≤ 120 and at D ∈ {105, 108, 112, 117, 120} with N an integer
    ≥ 6 (campaign frontier) and separately N ∈ [6,16]. Report per degree
    groups / killed / surviving / capped; compare with census-rebase §6
    (uni>=6, uni6-16, mix6-16 columns); state whether any degree empties;
    list the D = 105 survivors with their full packet structure.
(4) If the orbit count is forced to 1 ((UNI) is a THEOREM): say so with
    the proof; then the (UNI) kills are unconditional and the D = 105
    (UNI) survivors are the complete realisation list — give it.
Discipline: PROVED-HERE/UNREVIEWED typing; state the bounded quantity of
every OPEN you raise; desk-scale CAS (< 30 min one core, < 4 GB); do not
edit canonical ledgers; do not inspect jc2-lean; do not read any
ideation-20260903T* file or other lanes' in-progress reports.
Report: xmodel/branch-orbits-v2-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; the skeleton you
write first must NOT contain it); bounded writes; target 20-30KB;
120 minutes.
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/censusrebase-drivers-20260902/survivors-D48-120.txt
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1  {{LANE_INPUTS}}/survivors-D48-120.txt
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
