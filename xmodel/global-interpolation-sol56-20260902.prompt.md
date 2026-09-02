# Framework lane: GLOBAL-INTERPOLATION — the exact global Jacobian conditions on g alone, across all bottom discs and levels, as an algorithm (target-independent)

Reviewed (integration #17 + delta (f)): for a Keller pair in Moh's gauge,
f(x, τ_i(x)) = F_i(x) := ±∫dx/g_y(x, τ_i(x)) + a_i along every root τ_i of
g − c₂ (JAC-FIBRE); f has y-degree m < n, so f is IDENTICALLY the Lagrange
interpolant of the n values F_i + a_i at the n roots τ_j of g − c₂:
   f(x,y) = Σ_i (F_i + a_i)·∏_{j≠i}(y − τ_j)/(τ_i − τ_j).
The endgame review (charged) found that working in the completed chart
of ONE bottom disc ("LOCAL-KELLER") captures a necessary local identity
(whose leading order is BOTTOM-ODE — reviewed, promoted: the bottom
star is a dessin) but is NOT the global condition: the y-degree
condition (n − m linear relations among the F_i + a_i) and the
polynomiality of every coefficient of the interpolant in x mix ALL
discs and all levels of the tree. The stopped DISC-COUPLING lane was
charged on a refuted resonance structure; you are writing the correct
framework that its relaunch will use on a rebased Moh survivor (the
census-rebase lane runs in parallel; do not wait for it; do not read
it).
YOUR TASK (mathematics + an algorithm; target-independent):
(1) THE GLOBAL CONDITIONS, EXACTLY. With the n roots τ_j of g − c₂
    organised by Moh's tree (levels δ_s > … > δ₁, major/minor discs,
    Galois orbits under t ↦ ζt), write the coefficients of the Lagrange
    interpolant as symmetric functions of the τ_j and the F_i; state
    precisely (a) the n − m conditions that kill the y-degrees m+1..n−1,
    and (b) the conditions that the remaining m + 1 coefficients are
    POLYNOMIALS in x (no negative or fractional powers). Express both in
    terms of the Puiseux data: which conditions are local to one disc
    (and reproduce BOTTOM-ODE at leading order), which couple the discs
    of one Galois orbit (automatic by symmetry — say exactly what
    symmetry gives for free), and which couple DIFFERENT orbits / levels
    (the genuinely global ones).
(2) THE NO-LOG CONDITION AT ALL ORDERS. NO-RESIDUE (reviewed): [x⁻¹] of
    1/g_y(x, τ_i) = 0 on every branch. Show how it sits inside (1) and
    whether it is implied by (b) or independent.
(3) THE ALGORITHM. Given a Moh skeleton (n, m, M_*, V_*, δ_*, u, v) and
    the tame coefficients as unknowns, order the conditions by
    t-order; give the count of unknowns and conditions accumulated to
    each order and to each level junction, as closed-form functions of
    the skeleton data; identify the first order at which the number of
    conditions can exceed the number of unknowns (a counting bound —
    typed as such) and state what a "kill by counting" would need.
(4) CONTROLS. Run the framework on (y, x + y^k) (k = 3, 5), on
    (y + x², x + (y + x²)²), and on the composition (x + y⁵, y + (x + y⁵)³)
    (five bottom discs, ν = 1 — outside NU-TWO, but the global
    conditions apply to every Keller pair in the monic gauge): recover f
    exactly from g through the interpolant, confirm every condition of
    (1)–(2) holds identically, and exhibit that a non-Keller g (e.g.
    y² − x² − x, or the two-tower rows) FAILS at a stated order.
(5) Deliver a driver (box/globalinterp-drivers-20260902/globalinterp.py)
    that takes a skeleton + unknown tame coefficients to a stated order
    and emits the linear/quadratic system, with the controls as tests.
Discipline: PROVED-HERE/UNREVIEWED typing; desk-scale CAS (< 20 min,
< 4 GB); state the bounded quantity of every OPEN you raise; do not
edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/global-interpolation-sol56-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 25-40KB; 120 minutes.
charged_input=xmodel/time-function-endgame-review-sol56-20260902.md
charged_input=xmodel/time-function-endgame-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/time-function-calibration-d48-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=box/tfcal-drivers-20260902/bottom_star.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  {{LANE_INPUTS}}/time-function-endgame-review-sol56-20260902.md
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
db8a10c986a8a8a7b83c285585e299d887c72e52417b76ea7fca8c4fd0dbff2a  {{LANE_INPUTS}}/time-function-calibration-d48-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
437c5b45facf61e8e24d5399da50d131310b360f8184667a25c7388c6941c09e  {{LANE_INPUTS}}/bottom_star.py
```
