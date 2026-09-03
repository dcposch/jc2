# Hostile review lane: GLOBAL-INTERPOLATION framework (Sol) — the exact global conditions, the n−m−1 count, the Galois-descent statement, the log-block implication, the impossibility of a bare-skeleton count, the driver and its controls

The charged Sol report global-interpolation-sol56-20260902.md (20d554a0;
PROVED-HERE/UNREVIEWED) claims: (1) the Lagrange coefficients A_q =
(−1)^{n−1−q} Σ_i H_i e^{(i)}_{n−1−q}/D_i (1.3) and the moment form
M_r = Σ_i H_i τ_i^r/D_i with L/G = Σ M_r y^{−r−1} and the triangular
conversion (1.6); (2) the degree conditions are exactly n − m − 1 homogeneous
identities M_0 = … = M_{n−m−2} = 0 plus the monic normalisation
M_{n−m−1} = 1 (DEG) — "n − m degrees to kill" is false; (3) polynomiality is
the support test (1.9)/(1.10), reducing after Galois descent to [t^h]A_q = 0
for h ≥ 1 (1.11); (4) the exact tree factorisation (2.1)–(2.2) and that
BOTTOM-ODE is the leading local block; (5) Galois symmetry gives exactly:
one free integration constant per orbit (2.4), automatic cancellation of
non-invariant fractional powers (2.5), the support congruences (2.6) — and
NOT the vanishing of invariant integer-order coefficients nor any relation
between distinct orbits; (6) NO-RESIDUE is the logarithmic block; (DEG) +
(POLY) in K[log x] imply it (3.2), but it is computationally independent in
the Puiseux-field implementation; (7) IMPOSSIBILITY: no unknown count
U_Q(n, m, M_*, V_*, δ_*, u, v) exists on the bare tuple (§4.1); the exact
counts (4.7)–(4.16) on a DECORATED skeleton; (8) the quadratic lift (4.17) is
existentially equivalent; (9) controls: (y, x + y^k) k = 3, 5;
(y + x², x + (y + x²)²); the five-bottom-disc composition (x + y⁵, y + (x + y⁵)³)
with (5.4)–(5.5); the g-alone negative control y² − x² − x with residues
±1/2 (5.6); the corrected two-tower λ table (bracket degrees 2,3,4,2,2,5,2);
driver controls 40/0, selftest 50/0, example rank 26 with 36 lifted
equations (raw excess is not a kill).
Your task, hostile: CONFIRMED / GAP / REFUTED per numbered item with line
and repair. Mandatory: (a) re-derive (1.3), (1.5)–(1.6), (1.8) and the (DEG)
count from scratch; (b) re-derive (2.4)–(2.6) and find the exact hypothesis
under which "one constant per orbit" holds (does it need NO-RESIDUE first,
as claimed, and is the averaging argument valid when the orbit is not the
full μ_R?); (c) reprove (3.2) and decide whether the log-aware (DEG) is a
legitimate condition or circular; (d) attack the impossibility claim §4.1 —
is it an information obstruction or merely "the tuple does not fix k and
the orbit partition" (in which case a count as a function of the tuple PLUS
(k, orbit partition) may exist — state it if so); (e) rerun the driver's
controls/selftest/example (charged) and construct ONE additional control
the author did not run: a Keller pair with two DISTINCT Galois orbits of
bottom branches, verifying that invariant integer-order coefficients from
different orbits genuinely couple (item 5); (f) check the composition
control's branch structure (5.4) by direct reversion; (g) the corrected
two-tower λ table: recompute the seven rows. Typed verdict block; promotion
recommendation per item; bounded quantity of every OPEN you raise.
Desk-scale CAS (< 20 min one core, < 4 GB); no ledger edits; no jc2-lean;
do not read any ideation-20260903T1015Z-* file or other running lanes'
reports.
Report: xmodel/global-interpolation-review-grok46-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 20-30KB; 90 minutes.
charged_input=xmodel/global-interpolation-sol56-20260902.md
charged_input=box/globalinterp-drivers-20260902/globalinterp.py
charged_input=xmodel/time-function-endgame-review-sol56-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/exact-n-rigidity-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  {{LANE_INPUTS}}/global-interpolation-sol56-20260902.md
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588  {{LANE_INPUTS}}/globalinterp.py
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  {{LANE_INPUTS}}/time-function-endgame-review-sol56-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  {{LANE_INPUTS}}/exact-n-rigidity-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
```
