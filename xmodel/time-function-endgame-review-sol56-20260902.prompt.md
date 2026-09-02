# Hostile review lane: TIME-FUNCTION ENDGAME — LOCAL-KELLER, BOTTOM-ODE, STAR-SIMPLE/RESIDUE/SUM, STAR-ABC (dessin), STAR-EIGEN, the resonance structure at D = 105, the Nullstellensatz existence table, the controls

The charged Opus flagship claims (integration #17 reviewed inputs:
JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR): (1) LOCAL-KELLER: the
charge's interpolation conditions (f of y-degree m < n as the Lagrange
interpolant of F_i = ±∫dx/g_y(τ_i) + a_i, with polynomial coefficients)
transported to one bottom-major disc are exact at all orders; (2)
THEOREM BOTTOM-ODE: at Moh's leading order they are d·p_f·p_g′ −
e·p_g·p_f′ = κ ∈ C*, deg p_g = eV₂, deg p_f = dV₂, κ = c·d·e/q; (3)
STAR-SIMPLE (p_f, p_g squarefree and coprime — strengthens D1-STAR to
the f-roots), STAR-RESIDUE, STAR-SUM (Σ c_i^k/p_g′(c_i)² = 0 for
k ≤ (e−d)V₂ − 2); (4) THEOREM STAR-ABC: BOTTOM-ODE ⟺ p_f^e − ρ p_g^d
attains the Mason–Stothers bound with equality ⟺ p_f^e/p_g^d is a
three-point Belyi map with profiles [e^{dV₂}], [d^{eV₂}], [(d+e)V₂−1,1^*];
(5) STAR-EIGEN; (6) at the declared smallest D = 105 skeleton (n = 105,
m = 70, (d,e) = (2,3), M = (−70,−63,103), V = (1,4,1), δ = (3/4, 71/95,
−1), q = 3/10, N = 6): order 0 determined (single orbit), orders 1–2
governed by L_ε with resonances exactly at ε ∈ μZ, μ = 1/20; non-resonant
orders 7 unknowns / 5 conditions / cokernel 0; resonant orders kernel 3 /
cokernel 1; positive-dimensional, no kill; (7) Nullstellensatz existence
(Gröbner over Q saturated at κ ≠ 0): 15/15 (d,e,V₂) triples REALISABLE
with explicit witnesses; (8) controls 78/0 incl. the non-Keller
(y, x^j + y^k) failing (ii) with a hypergeometric obstruction; (9) the
DELTA-DENOM measured anomaly (do NOT adjudicate it as a filter; a
separate lane does; only check the measurement is right).
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per
item with line and repair. Mandatory: (a) reprove LOCAL-KELLER and
BOTTOM-ODE from JAC-FIBRE — is the "one-variable Keller equation" the
leading-order bracket in the disc coordinate π, and is κ's value
c·d·e/q right (recompute on (y, x + y^k))?; (b) reprove STAR-ABC (the
Mason–Stothers equality step: degree count of p_f^e − ρ p_g^d and the
squarefreeness of all three factors; the passport of the Belyi map);
(c) rerun the Nullstellensatz table (box/tfe-drivers-20260902; one
core) for the 15 triples and decide TWO more with b₁ ∈ {7, 8} if they
fit in 15 min; (d) recompute the D = 105 resonance analysis at orders
1 and 2 (the operator L_ε, its rank drop at μZ, kernel/cokernel) from
the delivered driver and by your own sympy at order 1; (e) rerun three
of the 78 controls including one two-tower row; (f) the selection of
the "smallest" D = 105 skeleton: is (105, 70, (−70,−63,103), V=(1,4,1))
(UNI)-surviving with N = 6 (cross-check against d1floor.py), and is the
declared count "63 with an integer N ≥ 6 under (UNI), 49 in [6,16]"
consistent with D1-SUBTREE's 264/209 (55 surviving groups)? Reconcile
V-skeletons vs groups exactly. Typed verdict block; promotion
recommendation per item; CAN/CANNOT; bounded quantity of any OPEN.
Desk-scale CAS; no ledger edits; no jc2-lean.
Report: xmodel/time-function-endgame-review-sol56-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 25-35KB; 90 minutes.
charged_input=xmodel/time-function-endgame-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=box/d1sub-drivers-20260902/d1floor.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
```
