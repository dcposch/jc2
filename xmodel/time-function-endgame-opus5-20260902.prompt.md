# Flagship: TIME-FUNCTION ENDGAME — realisability of a pinned Moh skeleton through the polynomiality of the Jacobian time function

Reviewed (integration #17): for a Keller pair in Moh's gauge, along
every root tau_i of g - c_2, d/dx f(x, tau_i(x)) = ±1/g_y(x, tau_i(x))
(JAC-FIBRE), so f is DETERMINED on each root branch by g alone:
   f(x, tau_i(x)) = F_i(x) := ±∫ dx / g_y(x, tau_i(x)) + a_i,
a Puiseux series provided the x^{-1} coefficient of 1/g_y(tau_i) is zero
(the no-log condition, at EVERY order — Moh's search conditions are its
leading-order consequences). Since f has y-degree m = Kd < n = Ke and
g - c_2 = prod (y - tau_j) is monic of degree n, f is the Lagrange
interpolant of the values F_i + a_i at the n roots:
   f(x,y) = sum_i (F_i + a_i) prod_{j≠i} (y - tau_j)/(tau_i - tau_j),
and it must (i) have y-degree exactly m < n (n - m linear conditions on
the F_i + a_i), and (ii) have coefficients that are POLYNOMIALS in x
(every negative and every fractional power of x must cancel). These
conditions, imposed order by order on the tame coefficients of the
Puiseux roots of g, are the FULL Jacobian condition; Moh's recursion
uses their leading orders only. D1-PIN/D1-STAR give the bottom: the
a_1 = eV_2 roots of each bottom-major disc separate as a STAR at radius
delta_1 with simple leading coefficients. The pinned geometric degree is
N = sum_B V_2(B) q(B), q = (1-delta_1)de/(d+e), an integer >= 6.
YOUR TASK (flagship effort; creativity and directness):
(1) Take the smallest skeleton at D = 105 surviving the (UNI) integrality
    filter with N >= 6 (enumerate with box/d1sub-drivers-20260902/
    d1floor.py / box/moh_skeleton_N.py; print it: n, m, M_2..M_s,
    V-packet, delta_j, q, N). Write the Puiseux roots of g down the
    tower with undetermined tame coefficients (the coefficients Moh's
    recursion leaves free between characteristic exponents), organised
    by conjugacy classes, to the depth needed for the interpolation
    conditions at the FIRST TWO orders beyond Moh's leading order.
(2) Impose (i)-(ii) at those orders. Count: unknowns (tame coefficients)
    versus independent conditions; solve what is linear; report whether
    the system is (a) inconsistent — the skeleton DIES and you have the
    first exact-form Appendix-II kill; (b) consistent with a positive-
    dimensional solution set — report its dimension and the next order
    to impose; (c) determined — print the solution and go one order
    deeper.
(3) THE UNIFORM QUESTION, honestly: does the structure of the conditions
    at the bottom star (a_1 simple roots, all at the same radius) give a
    condition that can be stated for EVERY skeleton — e.g. a residue
    identity summing over the star that forces sum of the a_1 leading
    coefficients' reciprocals to vanish, or an obstruction that grows
    with V_2 — i.e. a candidate for Moh's search condition (16) that
    would kill by SKELETON, not by realisation? Derive it if it exists;
    test it on the census at D <= 120 through the d1floor framework.
(4) Controls: (y, x + y^k) must satisfy (i)-(ii) exactly with f = y;
    (y + x^2, x + (y + x^2)^2) likewise; a non-Keller two-tower row
    must FAIL polynomiality.
Discipline: desk-scale CAS (< 20 min, < 4 GB — Puiseux to the needed
order at D = 105 is structured, not brute force; if it does not fit,
run the same programme at the smallest surviving degree below 105 and
say so); PROVED-HERE/UNREVIEWED typing; state the bounded quantity of
every OPEN you raise; do not edit canonical ledgers; do not inspect
jc2-lean.
Report: xmodel/time-function-endgame-opus5-20260902.md
Seal-at-completion; bounded writes; target 30-45KB.
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/d1-subtree-review-grok46-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-synthesis.md
charged_input=box/moh_skeleton_N.py
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/d1sub-drivers-20260902/jacfibre.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c  {{LANE_INPUTS}}/d1-subtree-review-grok46-20260902.md
ad1bf4467319f98a29e50de16915ced5f5c4177f7ffe28657332aba00ad18245  {{LANE_INPUTS}}/ideation-20260902T1608Z-synthesis.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
574f2f4498be8aef0457d17bbe6da4e3d80719f0fcd0f87c470d5864e0406eea  {{LANE_INPUTS}}/jacfibre.py
```
