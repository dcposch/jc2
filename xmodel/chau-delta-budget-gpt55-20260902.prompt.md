# Desk lane: CHAU-DELTA — the Chau degree cap, delta_infty in closed form, and CLAIM [D]

A blind ideation submission (Opus 5, charged, its sections 3 and 9 Card 1)
observes that OPEN[DEG-AF-VS-N] — ranked first by both H2 flagships — is
answered in the form the delta-budget needs by the Chau clauses banked on
the reducible branch (COMPANION-CURVE-ALLN C6/C7/C8 and its derived
M <= K = deg P/d): under H2, A_F is the image of a parametrisation of
bidegree (Md, Me), gcd(d,e)=1, with ONE place at infinity,
deg A_F = M max(d,e) <= max(deg P, deg Q). It then raises CLAIM [D]
(UNREVIEWED): at the (9,6) row the cap sum deg D_i <= max(deg P, deg Q) = 9
is saturated by the realised component D_1 alone (deg D_1 = 9, leading
form (u^2 - v^3)^3, m_1 = 3), so NO companion of any degree fits and
OPEN[COMPANION-R0-REALISATION] is NEGATIVE at (9,6,2) by substitution.
Three checks are named there: (a) additivity M = sum a_i m_i >= sum m_i
from the weighted-leading form of R_0 = c prod f_i^(a_i); (b) m_1 = 3 as a
property of the numerical type, not the realisation; (c) Chau's
normalisation and deg_x Res = N at his typing.

Your tasks, desk-scale, exact:
(1) Verify or refute the transfer: do Chau Thm 1 / Cor 1 / Cor 2 (as
    banked, with COMPANION's machine-verified corrections) apply under H2
    to give n = deg A_F = M max(d,e), bidegree (Md,Me), one place at
    infinity, and M <= K? State every hypothesis (P,Q monic in y; generic
    linear change; the relation of Chau's degree data to N).
(2) Compute delta_infty(M,d,e) — the delta-invariant of the unique place
    at infinity of such a curve — in closed form if it is a function of
    (M,d,e) alone; if it needs further Puiseux data, say exactly what and
    type OPEN[DELTA-INFTY-NOT-NUMERICAL]. Control: reconcile on the
    realised (9,6,2) curve (n = 9, four nodes; sum of delta over the affine
    singularities plus delta_infty must equal (n-1)(n-2)/2 = 28).
(3) Substitute into the (B2) budget: does it give a beta-bound at
    5 <= N <= 16 for each admissible (M,d,e), and is the set of admissible
    (M,d,e) finite at fixed N (it is not, unless something bounds
    max(deg P, deg Q) in N — say so plainly; the honest output may be a
    per-(M,d,e) finite list rather than a closure).
(4) Decide CLAIM [D] with checks (a)-(c). If it stands, state the general
    razor sum deg D_i <= max(deg P, deg Q) as a prefilter on numerical
    types, with its exact hypotheses.
(5) For (B3) at N = 4: with HF Prop 3.2's cusp congruences and the budget,
    list the admissible (M,d,e,p,q,k) with n = M max(d,e) <= 8; the Opus
    submission claims n >= 4 is forced (n = 3 is case (A)); confirm.
Deliver CONFIRMED / GAP / REFUTED per item with the computation shown.
No CAS beyond sympy; do not edit canonical ledgers; do not inspect
jc2-lean. The Chau PDF is at refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
if you need the primary text.
Report: xmodel/chau-delta-budget-gpt55-20260902.md
Seal-at-completion; bounded writes; target 12-20KB; 75 minutes.
charged_input=xmodel/ideation-20260902T0741Z-opus5.md
charged_input=xmodel/companion-curve-alln-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  {{LANE_INPUTS}}/ideation-20260902T0741Z-opus5.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  {{LANE_INPUTS}}/companion-curve-alln-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
```
