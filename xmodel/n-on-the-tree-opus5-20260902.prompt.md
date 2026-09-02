# Research lane: N-ON-THE-TREE — express the geometric degree on a Moh skeleton and run the N <= 16 filter (flagship effort; instrument + decision)

The DEPTH-CEILING report (charged as a PROPOSAL — its review runs in
parallel; RE-DERIVE what you use) recovered Moh's tower recursion
(Def 5.1(1)–(4), Prop 5.3; validated by reproducing his published delta
columns and his "25 possible values for M_2" at (75,50)), proved that
the number of characteristic pairs at infinity of a degree-minimal
Jacobian counterexample is <= log_2 K (K = gcd(deg P, deg Q) >= 16), and
located the geometric degree N inside Moh's tree: with t = x^{-1}, the
n roots tau_i of g − c_2 and the m roots phi_j of f − c_1 (generic c's,
deg = deg_y gauge, leading form with exactly two distinct linear
factors), N = deg_x Res_y(f − c_1, g − c_2) = − sum_{i,j} ord_t(tau_i −
phi_j) = 2deuv − sum_{same-slope} ord_t (CONTACT-DEFICIENCY). Every
constraint Moh and GGV derive constrains radii and counts along ONE
major tower; none forms this pairing sum. Its OPEN[N-ON-THE-TREE] is
the one finite instrument in the record whose outcome can PROVE the
ceiling on a range.
Your task:
(1) RE-DERIVE CONTACT-DEFICIENCY: why deg_x Res_y(f − c_1, g − c_2) is
    the geometric degree N (the number of solutions of f = c_1, g = c_2
    for generic c), and why the resultant's x-degree equals the
    negative sum of t-adic contact orders of the two root towers; make
    the gauge and the generic-c hypotheses explicit; controls: an
    automorphism (N = 1), (x, x y^m) (N = m), a non-Keller two-tower
    example, and (if the pairing is computable there) Moh's (75,50)
    survivor data.
(2) BUILD N(skeleton): from a Moh skeleton (n, m, the major tower data
    M_*, d_*, V_*, delta_*, plus the minor-disc distribution of Moh §6 /
    Prop 6.1 — state exactly what additional data the pairing needs and
    whether Moh's §6 supplies it or whether it must be enumerated as a
    further free datum with its exact size), compute the contact orders
    ord_t(tau_i − phi_j) for all pairs (the two towers share the
    major structure by the Jacobian condition — say precisely how) and
    hence N. Deliver box/moh_skeleton_N.py (standard library + sympy at
    most), fail-closed, with the controls of (1) as tests.
(3) EVALUATE on Moh's four n <= 100 survivors ((64,48), (84,56), (75,50),
    (99,66) per the depth lane's corrected reading — verify the list
    against Moh's text in refs/): what N does each carry (or what
    range, if the minor data is free)?
(4) RUN THE FILTER: on the skeleton census of the depth lane
    (box/depth-drivers-20260902/, census2.py; re-run or extend it to
    D <= 200 within desk limits, else write a box01 job spec) apply
    "N <= 16" together with the campaign's promoted profile ledger
    (W = N − a with the counting window, 2S <= W, mu_l >= 2, kappa <= N,
    the meridian floor n >= ceil((N−1)/(W−S)) + 1) and report per D: the
    number of skeletons surviving. If NONE survive at every D <= 200 for
    N <= 16, state the theorem exactly (hypotheses: degree-minimal,
    Jacobian, the recovered recursion's completeness — say what the
    recursion's completeness rests on) and price it against MOH-CROSS;
    if some survive, list the smallest ones with their full data — they
    are the exact objects a realisability/endgame lane must attack.
(5) CONTROLS on the filter: N = 1 skeletons (automorphisms) must be
    accepted by the pairing and rejected by non-invertibility; the
    non-Keller families must be rejected at the Jacobian steps of the
    recursion.
Discipline: the depth lane is a PROPOSAL; Moh 1983 and GGV from refs/
(hash); integrations #12–#14 at their scopes; no case (A), no A2, no
Z(G) = 1. Desk-scale CAS (< 15 min, < 4 GB per job; larger runs as a
box01 job spec — the box is running the cluster census on 48 of 64
cores, so a spec should use <= 14 workers or wait). State the bounded
quantity of every OPEN you raise; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/n-on-the-tree-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/depth-ceiling-opus5-20260902.md
charged_input=xmodel/minimal-keller-shape-opus5-20260902.md
charged_input=xmodel/integration14-coordinator-fable51-20260902.md
charged_input=xmodel/keller-cluster-census-codegen-sol56-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
863b05dbbd425035a09265cacdf6c418a2a3a1a7fadbeb303571bb5ccba618d6  {{LANE_INPUTS}}/depth-ceiling-opus5-20260902.md
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  {{LANE_INPUTS}}/minimal-keller-shape-opus5-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  {{LANE_INPUTS}}/integration14-coordinator-fable51-20260902.md
489e9ba2618482d572e1e424680bf8227f5850c001d4fc1d74c5d7c63dba117b  {{LANE_INPUTS}}/keller-cluster-census-codegen-sol56-20260902.md
```
