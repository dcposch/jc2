# Calibration lane: TIME-FUNCTION method at the smallest skeleton-bearing degree (D = 48) — does polynomiality of the Jacobian time function kill, pin, or leave a family?

Same programme as the charged flagship prompt
(time-function-endgame-opus5-20260902.prompt.md — read it; it runs at
D = 105 in parallel and you must NOT read its report), at a degree where
the Puiseux computation is small: D = 48 is the smallest degree carrying
Moh skeletons in the census (50 groups; the general knapsack of
D1-SUBTREE killed 9 of them at N >= 6 — see box/d1sub-drivers-20260902/
general.log and general.py). Reviewed facts (integration #17): along
every root tau_i of g - c_2, f(x, tau_i(x)) = ±∫ dx / g_y(x, tau_i(x)) + a_i
(JAC-FIBRE; no-log condition at every order); f of y-degree m = Kd < n
is the Lagrange interpolant of these n values and must be a POLYNOMIAL
in (x, y) — these are the full Jacobian conditions on the tame
coefficients of the Puiseux roots of g; Moh's search list is their
leading order. D1-STAR: each bottom-major disc is a star of a_1 = eV_2
simple roots at radius delta_1. Pinned N = sum_B V_2(B) q(B) must be an
integer >= 6 (N <= 5 closed). NOTE: Moh proved D <= 100 impossible, so
every D = 48 skeleton is KNOWN to be unrealisable — this lane is a
CALIBRATION of the method: the question is whether the time-function
conditions detect the unrealisability, at what order, and how.
YOUR TASK:
(1) List the D = 48 groups surviving the integrality knapsack at N >= 6
    (general.py / d1floor.py); pick the one with the smallest total
    root budget u e and the fewest tame coefficients; print it (n, m,
    M_j, V-packet, delta_j, q, N, u, v, d_j chain).
(2) Write the Puiseux roots of g down the tower with undetermined tame
    coefficients organised by conjugacy class; compute 1/g_y(x, tau_i(x))
    as a Puiseux series to the order needed for (i) the y-degree
    condition (n - m linear relations among the F_i + a_i) and (ii)
    polynomiality of the interpolant's coefficients, at Moh's leading
    order and the next two orders. Impose them; solve; report
    inconsistent / positive-dimensional (dimension, next order) /
    determined.
(3) Say at which order (if any) the D = 48 skeleton dies, and whether
    the killing condition can be written as a SKELETON condition
    (depending only on (n, m, M, V, delta) — a candidate Moh condition
    (16)) or needs the coefficients. If a skeleton condition emerges,
    evaluate it on the census at D <= 120 through the d1floor framework
    and report kills per degree (do NOT claim any degree emptied at
    D > 100 without the full computation).
(4) Controls: (y, x + y^k) and (y + x^2, x + (y+x^2)^2) satisfy (i)-(ii)
    with f recovered exactly; the non-Keller two-tower rows of the
    N-ON-THE-TREE report FAIL polynomiality.
Discipline: desk-scale CAS (< 20 min, < 4 GB); PROVED-HERE/UNREVIEWED
typing; state the bounded quantity of every OPEN you raise; do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/time-function-calibration-d48-opus5-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 20-35KB.
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/time-function-endgame-opus5-20260902.prompt.md
charged_input=box/moh_skeleton_N.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/d1sub-drivers-20260902/jacfibre.py
charged_input=box/d1sub-drivers-20260902/general.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
450e4610e664c98744ec59c8a12e4361e9d64c7f92447b11feffaa14fb1e7a6c  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.prompt.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
574f2f4498be8aef0457d17bbe6da4e3d80719f0fcd0f87c470d5864e0406eea  {{LANE_INPUTS}}/jacfibre.py
e7d7d2e6f108f7a50392f530f7f561c30685dd17c8cfeed3d01e57ce97865b28  {{LANE_INPUTS}}/general.py
```
