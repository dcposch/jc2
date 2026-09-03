# Software lane: the APPENDIX-II COMPILER — descend (Prop 6.3/6.4), assign the descended radii by the rule Φ, evaluate (8)–(13) on the descended pair, apply Moh's shape reduction, and exactly solve the resulting small systems over the screened residue

Now available (charged, all reviewed today): the Prop 6.3 descent as a
machine (box/mohsieve/descent.py: n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s,
d_i' = d_i/d_s, V_i' = V_i, J = cγ^{v_s−u_s−1}; p.207 to the unit);
OPEN[DESCENT-RADII] CLOSED: δ_i' = (k + 1)·Def 5.1(3)(n', m', M₂', V₂'; s' = 2)
with k the Jacobian exponent (10/10 printed rationals; measured on Moh's
shapes); the Appendix-II (15,10; M₂ = 11, V₂ = 3) reduction and kill
reproduced mechanically (box/m2descent-drivers-20260903/moh_1510_control2.py;
erratum in Moh's γ; SATURATED-EMPTY one step later); the normal form for a
descended pair with monomial Jacobian (charged m2-descent §4.3: h the d'-th
approximate root, f = h^{d'} + …, g = h^{e'} + G_{e'−2}h^{e'−2} + … + G₀;
the monomial Lemma 2.1: g_j ∈ k for j < m' − 1 and deg_x g_{m'−1} = k + 1;
exponent dictionary M₂ = N + (n' − m')); the whole-tree screen (delta
17(r); the 52 excess C_FULL_TREE_ODE rows at n ≤ 100 in box/mohprog-drivers-
20260903/full-tree-ode-excess-witnesses.json; the D = 108 screened
survivors in candidate-results.json).
YOUR TASK (fail-closed; Moh's six rows are the calibration set — p.207
signatures and, for (15,10; V₂ = 3), the pp.210–211 reduction and kill
must be reproduced before any new row is trusted):
(1) box/appendix2/compile.py: for a (1)–(13) row with u_s = 1, emit the
    descended datum, its radii by Φ, the descended (8)–(13) evaluation
    (A_j', (10)/(11), (12)/(13) on the descended tower — state what s' = 2
    means for (8)–(11): is only the r = 2 endpoint (12)/(13) active?), and
    Moh's SHAPE reduction: from δ₁' and the subdisc split (Def 5.1(1) on
    the descended data: the number of f- and g-roots per bottom disc), the
    forced forms of h and β (as on p.210: "the datum δ₁ = 1/2 implies that h
    and β must be of the following form") — derive the general rule
    (which monomials of h, β survive given δ₁', V₂', d₂'), gate it on Moh's
    (15,10) shapes (5)–(6) and (16,12) shapes (p.208) reproducing his
    coefficient counts (22 [15 or 13]; 17 → 10), then emit the polynomial
    system (Jacobian = cx^k in h-adic components + the monomial Lemma 2.1
    + the M₂' vanishing pattern) with its unknown count.
(2) SOLVE exactly every emitted system with ≤ 30 unknowns (Gröbner over
    Q; Rabinowitsch saturation at unit leaders and c ≠ 0; positive control:
    a planted descended automorphism must SURVIVE — construct one by
    descending a genuine automorphism in Moh's gauge with u_s = 1 if any
    exists in the autoscan population, else state none; negative control:
    Moh's (15,10; 11; 3) must be SATURATED-EMPTY): verdict per row
    SATURATED-EMPTY / SURVIVES (print the solution family) / COUNTING-BOUND
    (> 30 unknowns: emit and stop).
(3) RUN over: Moh's six (calibration); the 52 C_FULL_TREE_ODE excess rows at
    n ≤ 100 (how many have u_s = 1; verdict per row); the D = 108 screened
    survivors with u_s = 1; the D = 105 descended G2/G3 as a cross-check
    (expected COUNTING-BOUND at 42 unknowns per the descent-radii lane —
    does your shape rule agree?). Report the totals: how many of the 52
    die by the compiler (a coefficient-level kill beyond the tree), how many
    survive to a positive-dimensional family, how many are out of budget.
(4) READING: does the compiler's kill mechanism look uniform (e.g. always
    the same h-adic component / the same degree contradiction), i.e. a
    candidate theorem (T)-shape; what is the cheapest next experiment.
Typed block; bounded quantity + cheapest test of every OPEN. Desk-scale
(< 30 min one core, < 6 GB total; per-system cap 3 min); python3 -O replay
with an assert scan; no ledger edits; no jc2-lean; do not read
ideation-* files or other running lanes' reports. Drivers to box/appendix2/.
Report: xmodel/appendix2-compiler-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 150 minutes.
charged_input=xmodel/descent-radii-grok46-20260903.md
charged_input=xmodel/m2-descent-opus5-20260903.md
charged_input=xmodel/whole-tree-review-grok46-20260903.md
charged_input=box/mohsieve/descent.py
charged_input=box/descentradii-drivers-20260903/phi_delta.py
charged_input=box/m2descent-drivers-20260903/moh_1510_control2.py
charged_input=box/m2descent-drivers-20260903/moh_1510_controls_pm.py
charged_input=box/m2descent-drivers-20260903/descent_table.py
charged_input=box/m2descent-drivers-20260903/autoscan2.py
charged_input=box/mohprog-drivers-20260903/full-tree-ode-excess-witnesses.json
charged_input=box/mohprog-drivers-20260903/candidate-results.json
charged_input=box/moh_skeleton_full.py
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
2482ae1e8550cbaf6042a59ff20ca990eef78d7b77c590c1958a816c66a4e512  {{LANE_INPUTS}}/descent-radii-grok46-20260903.md
8aa3ba20567cb810cb6f540ef451e7fb4cadb8ad89f77418837f5d65fae55668  {{LANE_INPUTS}}/m2-descent-opus5-20260903.md
9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d  {{LANE_INPUTS}}/whole-tree-review-grok46-20260903.md
dfb81ffef2050c582451b1e096c8ae20b6ff0c15b61c1be0aaf5be530c10948b  {{LANE_INPUTS}}/descent.py
4bcb512d47cf9f935c6a2c0c7b8251ae16b3e4f73b4794abbef2d1702846c7c1  {{LANE_INPUTS}}/phi_delta.py
5ea3845b6e6f7022a59b0620b22f017c632ef08e6e5d0675f9c3d0274032566b  {{LANE_INPUTS}}/moh_1510_control2.py
add00ccc08951cc356891e3198bb39bf8ae5b55ffd182354ace7ba8a8ef3aa8a  {{LANE_INPUTS}}/moh_1510_controls_pm.py
aad83d39a8830f2eb3ff888997394bbc9cbf58e1074fe61f3695f3e797764c87  {{LANE_INPUTS}}/descent_table.py
e84fa92ff380f90558ace924d924b777f723f845cd1809534390fa3268a1328f  {{LANE_INPUTS}}/autoscan2.py
334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5  {{LANE_INPUTS}}/full-tree-ode-excess-witnesses.json
01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2  {{LANE_INPUTS}}/candidate-results.json
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
