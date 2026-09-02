# Desk lane: POLAR-CHAIN at N = 4 — is the polar tree of the (B3) N = 4 object a chain, and is E_0 a leaf?

Reviewed (charged review of KELLER-PENCIL-GENUS): on the resolution of
the net <P, Q, 1> of a noninvertible Keller map with polar subtree
T_+ = supp Z, FORK-GENUS gives 2 g_L − 2 = N − kappa − Lambda + Psi
(Lambda the leaf mass, Psi the fork mass), and the conditional
translations CH1 (Psi = 0 ⇒ n(W − S) <= 2N − 2) and CH2 ("E_0 a leaf of
T_+" ⇒ nW <= 2N − 2, which at N = 2W conflicts with the floor n >= 4 ⇒
the cell is EMPTY). OPEN[POLAR-CHAIN] (bounded quantity: the number of
valency >= 3 vertices of T_+, in [0, #L~ − 2]) was raised with the
N = 4 (B3) data in hand: Lambda − Psi = 4 there, and Psi >= 3 if E_0 is
a leaf. The live N = 4 (B3) cell has (promoted) a = 2, W = 2, one
dicritical (s, mu) = (1, 2), n >= 4 (MERIDIAN-FLOOR+), kappa <= N,
rho(G) = S_4, the cusp type (2|p, 3|q) or (3|p, 2|q), and E's structure
from B3-N4; the boundary instrument (charged) gives the DO boundary
ledger for the same object with BI-8 (#forks <= a = 2 on the spine).
Task, exact and finite: (1) From the promoted N = 4 data compute every
admissible polar tree T_+ (vertices over L_infty with their m_C and k_C,
the dicritical with m = s n, the leaf/fork structure) consistent with
FORK-GENUS, MF-EXACT (n(W − S) = N − 2 + 2 g_L + theta_inf with
theta_inf = kappa), the boundary instrument's BI-1/BI-8, the (H-∞)
scope (not assumed), and the determinant identity det = ±1; list the
solutions by (n, kappa, g_L, Lambda, Psi, shape). (2) Decide, for each,
whether T_+ is a chain (Psi = 0) and whether E_0 is a leaf; if every
admissible tree has E_0 a leaf, CH2 fires and the N = 4 (B3) cell is
EMPTY — say so with the exact chain of consumed statements (this would
be the first EMPTY window for (B3) and must be typed CONDITIONAL on
every unreviewed input it uses); if some admissible tree has a fork,
exhibit it and say what datum would exclude it. (3) Cross-check against
Domrina–Orevkov's six global graphs at N = 4 (the charged boundary
instrument reproduces them): which of the six is the polar tree of the
surviving (mu, corr) = (2,1) profile, and does DO's own kill of it
translate into Psi > 0 or into a determinant obstruction? (4) State
what survives at N = 5, 6 under the same computation if it is cheap
(the boundary instrument's N = 5, 6 profile lists are in the charged
report); otherwise type the OPEN with its size. Discipline: consume
FORK-GENUS, ESCAPE-KAPPA, CH1/CH2 at the review's CONFIRMED typing
(conditionals stay conditional); B3-N4 and the cage at HR's typing;
the boundary instrument at its review's scopes; SAT-MASS as a proposal
only for its T definition; no Z(G) = 1; no case (A); no A2. Desk
(python/sympy) only; state the bounded quantity of every OPEN you
raise; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/polar-chain-n4-grok46-20260902.md
Seal-at-completion; bounded writes; target 12-20KB; 75 minutes.
charged_input=xmodel/keller-pencil-genus-opus5-20260902.md
charged_input=xmodel/keller-pencil-genus-review-grok46-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/b3-boundary-instrument-opus5-20260902.md
charged_input=xmodel/sat-mass-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  {{LANE_INPUTS}}/keller-pencil-genus-opus5-20260902.md
d57d17f8eb6e776013d283e6796bef0db256088011dae2b73d1383c1e40cc56a  {{LANE_INPUTS}}/keller-pencil-genus-review-grok46-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  {{LANE_INPUTS}}/b3-boundary-instrument-opus5-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  {{LANE_INPUTS}}/sat-mass-opus5-20260902.md
```
