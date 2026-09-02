# Hostile review lane: N-VS-MAPDEG — the polar ledger, NO-CEILING, NOETHER-K, MERIDIAN-FLOOR+, and the Moh crossing

The charged producer report (Opus 5, flagship) claims (all
PROVED-HERE/UNREVIEWED unless marked machine-verified): (1) the invariant
D_min(F) = min over BOTH Aut factors (psi o F o chi) of max(deg G_1,
deg G_2); right composition fixes A_F, N, a, W, (s_l, mu_l), delta_aff,
Gamma, (d,e) and R_0 (Chau) and moves only K = gcd(deg P, deg Q), so
D_min = min_psi [max(d,e) · K_min]; THEOREM NEG-GEN — for general
dominant maps the bound is FALSE ((x, x^c y^N): geometric degree N,
n_min = 1, D_min >= (c+N+1)/2), the families spending deg Jac; for
Keller maps the question is neither proved nor refuted and absent from
refs/. (2) On the resolution with Z = Phi^*(L_infty) = sum m_C C:
m_{E_0} = D and s_l n = m_{C_l}; DEG-SPLIT: D = sum_l s_l n_{c(l)} + kappa
+ T (T the satellite mass), sharpening Chau's cap to deg A_F-bar <=
D − 1; NOETHER-K: sum a_i = 3D − 2N − kappa + n(W − S) and
sum a_i^2 = D^2 − N (machine-verified on 41 maps); DICRITICAL-NEIGHBOUR;
"sum Deg a~ = N" bounds only the non-contracted boundary; det(boundary
matrix) = ±1 for every compactification of A^2. (3) MERIDIAN-FLOOR+:
p(W − S) >= N − 1 with p = min deg_t l(a,b) <= n − 1, hence
n >= ceil((N−1)/(W−S)) + 1 — one unit sharper than the promoted floor at
every cell; re-derives n >= 4 at N = 4 from group theory. (4) THEOREM
NO-CEILING: no intersection-theoretic boundary instrument can bound D at
fixed N; two machine-verified families realise it; the free datum is the
satellite mass T (the boundary avatar of Jung–van der Kulk word length);
the one identity that bites is NOETHER-K = the Keller condition, which
reduces the ceiling question to ONE integer, Z·K_X = sum a_i − 3D = −2N
− kappa + n(W − S): any bound Z·K_X <= f(N) closes OPEN[DELTA-AFF-VS-N]
(OPEN[ANTICANON-DEFECT]); Z·K_X is unbounded above for general dominant
maps; for automorphisms Z·K_X = −3. (5) Crossing: (N, W) is EMPTY once
D_min <= C with C <= ceil((N−1)/(W−1)) + 1; at W = 2, D_min >= N + 1; and
via Moh 1983 (D_min >= 101, verified in refs/) ANY proof of C(N) <= 100
closes that N outright — the whole (B2) 5..16 and (B3) 4..8 ranges.
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per
claim with the exact line and repair. Mandatory: (a) NEG-GEN's family
(compute A_F, N, n_min, D_min for (x, x^c y^N); confirm it is NOT Keller
and where deg Jac is spent); (b) DEG-SPLIT and NOETHER-K — re-derive
from Noether's formula on a resolution of the map's boundary (state the
compactification, the definition of kappa and T, the polar divisor Z,
and why sum a_i^2 = D^2 − N); recompute on at least six maps including
automorphisms, (x, x y^N), and a Keller-like control; (c) MERIDIAN-
FLOOR+ — reprove (why is the generator count p, not n; is p <= n − 1
always?) and check it against the promoted MF-EXACT (integration #11):
is "+1 at every cell" consistent with MF-EXACT's g_L = 0, theta_inf = 1
attainment case, or does it prove OPEN[MF-DEFECT] (2 g_L + theta_inf >=
2 always)? Say which; (d) NO-CEILING — is it a theorem (with a precise
class of "intersection-theoretic boundary instruments") or a heuristic
backed by two families? (e) the one-integer reduction: confirm that
Z·K_X <= f(N) implies a bound on n(W − S) hence on delta_aff, and state
what is known about Z·K_X for Keller maps beyond automorphisms; (f) the
Moh crossing — verify the exact statement of Moh 1983 in refs/ (which
degree, which normalisation, both coordinates or the max?), and confirm
that a proof of D_min <= 100 for geometric degree N would indeed kill N
(no gap between Moh's degree notion and D_min). Deliver a typed verdict
block with a promotion recommendation per item; state the bounded
quantity of every OPEN you raise. Desk-scale CAS only; do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/n-vs-mapdeg-review-gpt55-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-review-gpt55-20260902.md
charged_input=xmodel/meridian-floor-sharpen-opus5-20260902.md
charged_input=xmodel/b3-boundary-instrument-opus5-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
50f62fae3d6265f93781185e62979925471063676cbeb0d1fe67c8dfc170e056  {{LANE_INPUTS}}/deg-af-vs-n-review-gpt55-20260902.md
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  {{LANE_INPUTS}}/meridian-floor-sharpen-opus5-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  {{LANE_INPUTS}}/b3-boundary-instrument-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
```
