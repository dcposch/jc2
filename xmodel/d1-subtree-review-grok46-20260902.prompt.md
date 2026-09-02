# Hostile review lane: D1-SUBTREE — JAC-FIBRE, FRONTIER-EXACT, D1-PIN, D1-STAR, PIN-NOT-CEILING, the integrality filter, condition (15)

The charged producer report (Opus, flagship) claims, for a degree-minimal
Keller pair in Moh's gauge (NU-TWO): (1) THEOREM JAC-FIBRE: on every
Puiseux branch tau of a generic fibre {g = c_2}, ord_t f(tau) + ord_t
g_y(tau) = -1 (general law -1 + ord_t J); (2) FRONTIER-EXACT: N = sum_rho
(1 - delta^0_rho)^+ over the roots of g, delta^0 the g-frontier, with
lambda_f(delta^0) = delta^0 - 1 exactly and delta^0 >= 1 iff non-proper;
(3) THEOREM D1-PIN: floor(r) - ceiling(r) = (1-delta_r)(-M_r - m)/(n-M_r),
zero iff r = 1, so at the bottom major disc c_rho = m(1-delta_1)/(n+m)
exactly and N = sum_B V_2(B) q(B), q = (1-delta_1)de/(d+e) = deK
prod_{j>=2} P_j/Q_j, sum_B V_2(B) <= u; (4) THEOREM D1-STAR: below
delta_1 the slope of lambda_g is exactly 1, lambda_f is constant, the
a_1 = eV_2 roots separate pairwise at exactly delta_1 (Moh's p(pi) has
a_1 simple roots); (5) RADIUS-ORDER is Moh's Lemma 5.2; (6) THEOREM
PIN-NOT-CEILING (measured): min over branch data of V_2 q is 3/64 at
D <= 120 and 3/112 at D <= 200 with no growth in D, so no D <= C(N)
follows; (7) the integrality filter: under (UNI) at D <= 120, 98.98% of
V-assignments and 60.0% of groups die under H2 (55% unconditionally);
per degree 105: 264/209, 108: 824/419, 112: 1163/795, 117: 60/47, 120:
4104/2390; without (UNI), exact knapsack at D in [48,79]: 24.7% of
groups killed; NO degree emptied; Moh's six survivor rows all admit an
integer N; (8) new Moh search condition (15); (9) PLACE LAW m_gamma =
nu_gamma (1-delta_1) d/(d+e). The same squeeze was derived
independently by Sol (charged, sec.2, SD1-SD6) and by Grok's dictionary;
you are the DIFFERENT-MODEL review required for promotion.
Your task, hostile and computational (Moh 1983 in refs/, hash; read
the page images for Lemma 2.1 p.151, Lemma 5.2 p.178, Def 5.1 p.179,
Prop 5.3 p.180, Prop 6.1 p.190-191): CONFIRMED / GAP / REFUTED per item
with the exact line and repair. Mandatory: (a) reprove JAC-FIBRE from
implicit differentiation and monicity, including the no-log integration
step and the non-proper case; (b) reprove FRONTIER-EXACT and the
shifted-tree contact formula sum_{j != i} ord_t(tau_i - tau_j) =
-delta^0_i; (c) D1-PIN: recompute floor(r) - ceiling(r) in closed form
from Lemma 5.2 and Def 5.1(1); confirm it vanishes only at r = 1; state
exactly which Moh inputs the CEILING half uses (Def 5.1(1) at level 1)
and whether the FLOOR half is Moh-free; (d) D1-STAR: is the star forced
for BOTH root families, and does it contradict anything in Moh (e.g.
his statement that the recursion "stops" — quote him); (e) rerun the
producer's controls (box/d1sub-drivers-20260902: jacfibre.py,
treecheck.py) and three of the nine genuine Keller pairs by your own
sympy; (f) recompute the six Moh survivor rows' achievable N sets and
the (UNI) filter at D <= 120 (d1floor.py / runall.py; one core,
~25 min) — confirm the per-degree kills and that NO degree empties;
run the general knapsack at D in [80, 100] if it fits in 15 min;
(g) PIN-NOT-CEILING: confirm min V_2 q at D <= 200 and say whether a
lower bound on V_j or on the number of bottom discs (OPEN[V-FLOOR]) is
available from anything in Moh (1)-(13) or Prop 4.4/4.6/5.3; (h) the
(UNI) hypothesis: is branch uniformity within a Galois orbit correctly
argued, and what is the bounded quantity of OPEN[BRANCH-ORBITS];
(i) condition (15) versus NOTT's (14): containment; (j) the PLACE LAW.
Deliver a typed verdict block with a promotion recommendation per item,
an explicit statement of what the pinned formula CAN and CANNOT decide,
and the bounded quantity of any OPEN you raise. Desk-scale CAS only; do
not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/d1-subtree-review-grok46-20260902.md
Seal-at-completion; bounded writes; target 25-35KB; 90 minutes.
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/n-on-the-tree-opus5-20260902.md
charged_input=xmodel/n-on-the-tree-review-grok46-20260902.md
charged_input=xmodel/integration16-coordinator-fable51-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-sol56.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  {{LANE_INPUTS}}/n-on-the-tree-opus5-20260902.md
481d71bfdb9f5237405c671234c751b7c9a3d5339a23f676aa947b7fc69c5ba9  {{LANE_INPUTS}}/n-on-the-tree-review-grok46-20260902.md
6b8a712344397e1248e4efe230f5fcbeb41ae8b64423de272a77e98ae6b1a241  {{LANE_INPUTS}}/integration16-coordinator-fable51-20260902.md
3a4744ddb23e6659ad1ab752e7d7b531c8a325f041971b7d72ec1179f11155e1  {{LANE_INPUTS}}/ideation-20260902T1608Z-sol56.md
```
