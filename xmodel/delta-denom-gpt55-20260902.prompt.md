# Arithmetic probe: DELTA-DENOM — is Def 5.1(3) missing a denominator condition on the radii δ_i, and is it a skeleton filter?

The charged TIME-FUNCTION ENDGAME report (§7, measured anomaly, NOT
used by it) observes: by Moh Prop 5.3 (p.180, read the page image), the
radius δ_i of the major disc D_i is defined GEOMETRICALLY as a minimum
of ord_t(τ − τ′) over roots τ, τ′ of g·∏T_j (Puiseux series in t = x⁻¹
with ramification indices dividing n = deg g, resp. the degrees of the
T_j), so its reduced denominator must divide the lcm of the
ramification indices of the branches involved; Def 5.1(3)'s closed
formula δ_i = 1 − (n − M_i)∏_{j>i}[V_j(n−M_j) − d_j]/((n−M_s−1)∏_{j>i}
[V_j(n−M_{j−1}) − d_j]) does not impose this. MEASURED over the census
(box/tfe-drivers-20260902/deltadenom.py, D ∈ [48,120], 902,893
V-skeletons): denom(δ₁) | n on 0.74%; denom(δ₁) | n or | m on 0.96%;
among the 9,553 (UNI) N ≥ 6 survivors, denom(δ₁) | n on 34.19%; on
Moh's six published survivor rows 5/6 have denom(δ₁) | n and 6/6 have
denom(δ₁) | n or | m; the selected D = 105 skeleton has δ₁ = 3/4 with
4 ∤ 105 and 4 ∤ 70, δ₂ = 71/95 with 95 ∤ 105. "Six of six against 0.96%
is a signal, not a theorem."
YOUR TASK (hostile to the signal; exact arithmetic):
(1) THE THEOREM, IF ANY. From Moh's Def 1.1–1.3 (discs, logarithmic
    radius), Prop 1.2, Prop 5.3 and Def 5.1, determine exactly what
    set of orders ord_t(τ − τ′) δ_i is a minimum over, and hence the
    exact divisibility constraint on denom(δ_i): which ramification
    indices enter (of g's branches: divisors of n; of the T_j's
    branches: divisors of deg T_j = ?; of f's branches: divisors of m).
    Prove the constraint or show that Prop 5.3's minimum can have a
    denominator beyond those indices (e.g. because ord_t(τ − τ′)
    between branches of different ramification lies in (1/lcm)Z, and
    lcm can exceed both n and m — compute the true bound). State the
    THEOREM DELTA-DENOM with exact hypotheses, or REFUTE the signal.
(2) CROSS-CHECK on Moh's data: for the six published rows and Moh's
    Appendix II tables (pp.202, 207 — read the images), verify the
    constraint; for the D = 105 selected skeleton (δ₁ = 3/4) determine
    whether 4 | lcm of the admissible ramification indices (a partition
    of n = 105 into branch degrees whose lcm is divisible by 4 requires
    an even part — is that consistent with the skeleton's d_j chain
    (105, 35, 7, 1), all odd?). If the chain forces all ramification
    indices odd, δ₁ = 3/4 is IMPOSSIBLE and that skeleton DIES — state
    it as THEOREM or as GAP with the missing step.
(3) THE FILTER. If (1) yields a theorem, implement it in the d1floor
    framework and run it over D ≤ 120 (one core): kills per degree
    among all V-skeletons and among the (UNI) N ≥ 6 survivors; whether
    any degree is EMPTIED; the effect on the MOH-SHARP-2 degrees; and
    on Moh's six rows (which must SURVIVE — a filter that kills a row
    Moh realised as a skeleton candidate is wrong). If (1) refutes, run
    nothing and say what the 6/6 coincidence is.
(4) THE SAME QUESTION FOR δ_i, i ≥ 2, and for the numerators: does
    Prop 5.3 constrain anything else that Def 5.1(3) does not encode?
Discipline: PROVED-HERE/UNREVIEWED typing; quote Moh with page and
line; desk-scale; state the bounded quantity of every OPEN you raise;
do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/delta-denom-gpt55-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 15-25KB; 60 minutes.
charged_input=xmodel/time-function-endgame-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/deltadenom.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/moh_skeleton_N.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
527cd7fcafe40fcdf6f189e56a60fadf0804f358a46baecf4ee765483111c3db  {{LANE_INPUTS}}/deltadenom.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
```
