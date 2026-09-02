# Hostile review lane: SAT-MASS — SAT-WEIGHT, the T definition repair, LEDGER-BLIND, HALF-CAP, and the Moh price

The charged producer report (Opus 5, flagship) claims (PROVED-HERE /
UNREVIEWED): THEOREM SAT-WEIGHT (74 maps, 0 fails): with nu_C = ord_C
sigma^*L_infty (source polar multiplicity), m_C = ord_C Phi^*L_infty
(target), c_C = Z·C (the proximity excess of the base cluster, c_{E_i} =
a_i − sum_{j→i} a_j): D = sum nu_C c_C, N = sum m_C c_C, D − T = sum c_C,
T = sum (nu_C − 1) c_C; at most kappa + #dicriticals of the cluster points
have positive excess; DEFINITION REPAIR: DEG-SPLIT's T is the mass of
points proximate to two members of the EXTENDED cluster {L_infty, p_1..
p_r} (T = T_class + (D − sum_{level 1} a_i); witness (x, y + x^4): T = 3,
T_class = 2); THEOREM LEDGER-BLIND (every boundary-ledger entry is
invariant under source composition F ↦ F∘chi while D and T diverge;
(x, y + x^k) has T = k − 1); THEOREM HALF-CAP (if D > N and F has exactly
ONE dicritical — forced by 7.B' whenever W <= 3 — then D <= 2(T + kappa),
S n = Lambda <= D/2, T >= D/2 − kappa; sharp on (x, xy), (x, x^2 y^2);
refuted for two or more dicriticals by three witnesses); its
consequences (Chau's cap halved at W <= 3; T > 0 forced; any bound
T <= tau on a degree-minimal representative gives D_min <= 2(tau + N),
so tau <= 50 − N closes the cell outright via Moh — tau <= 46 at N = 4,
tau <= 34 at N = 16); the degree-minimality translation (the tail an
elementary automorphism removes) and the exact theorems it cites
(Abhyankar–Moh, Nagata, Appelgate–Onishi, Heitmann/GGV).
Your task, hostile and computational: CONFIRMED / GAP / REFUTED per
item with the exact line and repair. Mandatory: (a) SAT-WEIGHT — reprove
from the definitions (why D = sum nu_C c_C with c_C the excess; why
D − T = sum c_C); recompute on at least eight maps including
automorphisms, (x, xy), (x, x^2 y^2), (x, x^c y^N), and one two-
dicritical map; (b) the T definition repair against DEG-SPLIT as
promoted in integration #12 (is #12's T the extended-cluster mass? if
not, state the binding correction); (c) LEDGER-BLIND — confirm the
invariance list and the divergence; (d) HALF-CAP — reprove; check the
one-dicritical hypothesis, the D > N hypothesis, the sharpness
witnesses and the three refuting witnesses; is "7.B' forces one
dicritical whenever W <= 3" correct (2 sum s_l <= W with mu_l >= 2)?;
(e) the price: confirm D_min <= 2(tau + N) from T <= tau on a
degree-minimal representative and the Moh crossing thresholds per N;
(f) the degree-minimality section: are the cited classical theorems
stated correctly and do they give the claimed cluster translation? Say
exactly what is proved about the boundary tree of a degree-minimal
Keller pair and what is not. Deliver a typed verdict block with a
promotion recommendation per item; state the bounded quantity of any
OPEN you raise. Desk-scale CAS only; do not edit canonical ledgers; do
not inspect jc2-lean.
Report: xmodel/sat-mass-review-gpt55-20260902.md
Seal-at-completion; bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/sat-mass-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-review-gpt55-20260902.md
charged_input=xmodel/integration12-coordinator-fable51-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  {{LANE_INPUTS}}/sat-mass-opus5-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  {{LANE_INPUTS}}/n-vs-mapdeg-review-gpt55-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  {{LANE_INPUTS}}/integration12-coordinator-fable51-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
```
