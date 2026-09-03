# Research lane: OPEN[SIBLING-COEFFICIENTS] — the coefficient-level obstruction beyond the whole-major-tree: can the sibling polynomials (p_j, q_j) at adjacent nodes of Moh's tree be realised simultaneously over one coefficient field with the Appendix-I ODE, the common leading terms, and the Galois action?

Promoted today (AUDIT delta 17(r), charged): the whole-major-tree obligation
(every above-threshold factor of p_j at every major disc extends — Prop 5.3
universal, p.200 Thm (4)) and the finite screen C_FULL_TREE (658 → 60 / 58
with the ODE (3.7) at n ≤ 100, keeping Moh's six; the (75,50) residue exact;
D = 105 and 117 empty). What the tree constrains: multiplicities, orbit
sizes, radii. What it does NOT constrain (the residual named by the second
reader §5.2 and by Moh's introduction p.143 last paragraph — the unresolved
interaction of the two polynomials): the SIMULTANEOUS existence of the
polynomials p_j(π), q_j(π) at every node with a common coefficient field,
matching leading terms between parent and child (the child's chart is the
parent's factor recentred and rescaled: σ_{j−1} = σ_j-data + π t^{δ_{j−1}}),
the Appendix-I ODE D(P_j, Q_j, p_j, q_j) = c_j p_j (Prop A.3, RHS = cp) at
EVERY node including minor siblings, and the Galois action π ↦ ζπ of order
A_j (the nonzero orbits are ζ-orbits, so p_j, q_j ∈ k[π^{A_j}]·π^{b}-form).
The 49 excess rows after the passport (52 after ODE only) at n ≤ 100 are the
bounded target; Moh's six are the positive controls (Appendix II kills them
only by coefficient computation).
YOUR TASK:
(1) FORMALISE the two-node gluing problem exactly from the source (Prop 4.6
    pp.170–171, Prop 5.3 pp.180–183 — the construction of the next general
    point from a factor; Prop A.3/A.4 pp.205–206; the p.201 orbit action;
    Moh's own worked gluing on pp.208–211 for (16,12) and (15,10)): given a
    parent node with (P, Q, A, b, {u_ℓ}) and its p, q, what are the exact
    constraints on the child's (p', q') at the factor of multiplicity u —
    which coefficients of (p', q') are determined by (p, q) (the leading
    terms / the "outer" data) and which are free; write the system as
    polynomial equations over Q in the free coefficients with the ODE at
    both nodes, the Galois symmetry, squarefreeness/coprimality (Prop 4.6
    (3)–(5)) as inequations.
(2) CALIBRATE on Moh's six: for (64,48) (tree 1 core + k bottoms, s = 3)
    and (75,50) V₂ = 3, set up the parent D₂ node (P = 12/20, Q = 9/16,
    A₂ = 4/5) and its bottom children, and SOLVE the two-node system exactly
    (Gröbner over Q, saturate at the unit leaders and the ODE constants;
    positive/negative controls on the saturation): does a solution exist
    (it must, up to Appendix II's deeper computation — if the two-node
    system is already EMPTY on a printed row, your formalisation is wrong:
    fail closed).
(3) ATTACK one excess C_FULL_TREE_ODE survivor at n ≤ 100 that Moh's table
    omits — take the lexicographically first (90,60) row from
    box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json — and
    one D = 108 screened survivor (from candidate-results.json / the
    survivors listing; state which): set up and solve the two-node system;
    verdict SATURATED-EMPTY (a new coefficient-level kill — say whether the
    mechanism is uniform) / SURVIVES (print the solution family and its
    dimension) / COUNTING-BOUND.
(4) READING: is a uniform "sibling-coefficient" theorem plausible — what
    quantity would it bound — and is this the same computation as the
    tree-decorated moment engine (the whole tree supplies exactly the
    decoration the framework needs: state the dictionary tree-node ↔
    decoration datum)? Single cheapest next experiment.
Discipline: PROVED-HERE/UNREVIEWED; SOURCE-READ per citation (refs/moh1983_
jram340_configurations_of_roots.pdf, page N = PDF page N−139, pdftoppm -r 300);
bounded quantity + cheapest test of every OPEN; desk-scale CAS (< 30 min
one core, < 6 GB); no ledger edits; no jc2-lean; do not read
ideation-20260903T1015Z-* files or other running lanes' reports. Drivers to
box/siblingcoef-drivers-20260903/.
Report: xmodel/sibling-coefficients-sol56-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 25-40KB; 180 minutes.
charged_input=xmodel/moh-program-review-sol56-20260903.md
charged_input=xmodel/whole-tree-review-grok46-20260903.md
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=box/mohprog-drivers-20260903/full_tree_partition.py
charged_input=box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json
charged_input=box/mohprog-drivers-20260903/candidate-results.json
charged_input=box/m2descent-drivers-20260903/moh_1510_control2.py
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45  {{LANE_INPUTS}}/moh-program-review-sol56-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  {{LANE_INPUTS}}/whole-tree-review-grok46-20260903.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8  {{LANE_INPUTS}}/full_tree_partition.py
334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5  {{LANE_INPUTS}}/full-tree-ode-excess-witnesses.json
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  {{LANE_INPUTS}}/candidate-results.json
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  {{LANE_INPUTS}}/moh_1510_control2.py
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
