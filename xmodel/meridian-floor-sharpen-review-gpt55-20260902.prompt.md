# Hostile review lane: MERIDIAN-FLOOR-SHARPEN — the exact identity, the group audit, LOC-MULT, the price table

The charged producer report (Opus 5) sharpens the promoted MERIDIAN-FLOOR
(integration #10). Claims (PROVED-HERE/UNREVIEWED): (1) MF-EXACT — the
floor is an IDENTITY: for the degree-N cover C_L = F^{-1}(L) -> L over a
generic line L, Riemann–Hurwitz gives n (W − S) = N − 2 + 2 g_L + theta_inf
(g_L the genus of C_L, theta_inf its number of target-escaping places at
infinity), the banked floor being g_L = 0, theta_inf = 1; and what the
meridian argument bounds is the MERIDIONAL RANK of pi_1(C^2 \ A_F), so no
upper bound on n can ever come out of that apparatus (the only bridge
mrk(G) <= n points the wrong way); (2) the group audit — CENTRAL-RANK,
CUSP-PARITY/B3-DEGREE, ORBIFOLD-CAGE/B3-CAGE, PERIPHERAL-RANK,
MERIDIAN-SPAN raise neither numerator nor denominator; 7.B' caps the
S-route at ceil(2(N−1)/W) and at W = 2 forces S = 1, so n_min >= N − 1 is
optimal in S; (3) THEOREM LOC-MULT — mult_P >= r_P + ceil(K_P/(W − S)) at
every singular point of A_F, fed through Bezout and DEG-DELTA(a);
control: at N = 4 it returns n >= 4, reproducing the Chau lane's (B3)
value; (4) the PRICE TABLE over N = 4..20 and every counting-admissible
cell: the sharpened floor Phi beats the banked floor at 39 of 81 cells by
exactly +1; no cell is empty outright (no profile bounds delta_aff
above); (5) (B2) at 5 <= N <= 16: delta_aff >= 6..39 is FORCED against the
death thresholds 3 and 1 — no inconsistency, the beta-route priced at a
factor 2 to 39; (6) item (4) of its charge CONFIRMED: the W = 2 column
dies at all N only under n_min <= C(N) with C(N) <= N − 2, and no
reviewed statement has that shape; (7) NEW: n <= (D_F − theta_inf)/S and
D_F >= n S + 1, sharpening Chau's cap n <= D_F = max(deg P, deg Q).
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per item
with the exact line and repair. Mandatory: (a) MF-EXACT — reprove it;
state exactly what C_L is (the generic member of the affine pencil
alpha P + beta Q = gamma), its smoothness, the ramification of
C_L -> L (only over L ∩ A_F, with the generic meridian cycle type), and
the bookkeeping of the places at infinity; check the identity on an
explicit non-Keller control where all quantities are computable (e.g.
a proper map or the identity), and on the promoted N = 4 profile data;
(b) the meridional-rank reading and the "no upper bound from this
apparatus" claim — is it a theorem or a heuristic?; (c) LOC-MULT —
reprove from the point-stabiliser structure (rho(Loc_P), the fibre
partition, a_P = #size-1 parts, K_P) and check the Bezout step; (d)
recompute the price table at N = 4, 5, 6, 8, 12 for every admissible
cell; (e) the (B2) forced delta_aff values at N = 5, 6, 10, 11, 16;
(f) the Chau-cap sharpening D_F >= n S + 1 (exact hypotheses).
Deliver a typed verdict block with a promotion recommendation per item;
state the bounded quantity of any OPEN you raise. Desk-scale CAS only;
do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/meridian-floor-sharpen-review-gpt55-20260902.md
Seal-at-completion; bounded writes; target 15-25KB; 75 minutes.
charged_input=xmodel/meridian-floor-sharpen-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-review-gpt55-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/homcover-transfer-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  {{LANE_INPUTS}}/meridian-floor-sharpen-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
50f62fae3d6265f93781185e62979925471063676cbeb0d1fe67c8dfc170e056  {{LANE_INPUTS}}/deg-af-vs-n-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
```
