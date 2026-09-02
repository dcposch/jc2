# Research lane: SAT-MASS — bound the satellite mass of a degree-minimal Keller pair (flagship effort)

The reviewed ceiling flagship (charged with its review) established, on
the resolution X → P^2 of a noninvertible Keller map F of geometric
degree N (common-degree rational map, boundary base points on L_infty
blown up, Z = Phi^*L_infty = D H − sum a_i E_i): DEG-SPLIT
D = sum_l s_l n + kappa + T, where D = max(deg P, deg Q), n = deg A_F-bar,
s_l the dicritical degrees, kappa = sum_{C→L_inf} k_C <= N, and T = the
SATELLITE MASS (the sum of the satellite base-point multiplicities a_i —
the boundary avatar of Jung–van der Kulk word length); and MOH-CROSS:
Moh 1983 proves D_min >= 101 for every noninvertible Keller map
(max(deg f, deg g) <= 100 is impossible), so ANY proved bound
D_min <= C(N) with C(N) <= 100 kills geometric degree N outright. The
n-half of the price (bounding n, equivalently delta_aff or the genus of
the generic pencil member) is owned by a parallel flagship. YOUR half:
carry n to D — bound T (and kappa, and S n) for a DEGREE-MINIMAL
representative of the Aut × Aut orbit, so that n <= C'(N) implies
D_min <= C(N).
Tasks:
(1) Define T precisely on the resolution (which base points are
    satellites — proximate to two earlier points — and why their
    multiplicities are exactly the part of D not accounted for by the
    dicriticals and the L_infty-sheets); re-derive DEG-SPLIT; state the
    proximity inequalities of the base cluster at infinity of the
    pencil/net (a_i >= sum of the a_j proximate to i) and the NOETHER-K
    equations sum a_i = 3D − 2N − kappa + n(W − S), sum a_i^2 = D^2 − N.
(2) DEGREE-MINIMALITY. For a representative of minimal D in its
    Aut(C^2) × Aut(C^2) orbit, what does Jung–van der Kulk say about the
    boundary cluster? (An elementary automorphism reduces D exactly when
    the top form of one coordinate is a power of the other's leading
    form; Abhyankar–Moh: for a Keller pair the leading forms are powers
    of a common form and deg P | deg Q or vice versa can be arranged
    only in the invertible case — state the exact theorems: Abhyankar–
    Moh 1975 (the leading-form theorem for Keller pairs), Nagata's and
    Appelgate–Onishi's degree results, Heitmann / GGV gcd(deg P, deg Q)
    >= 16 as banked.) Translate "no further degree-lowering
    automorphism exists" into a statement about the satellite cluster:
    the satellites are the resolution of the Newton-polygon / Puiseux
    structure of the leading forms; a minimal representative has a
    cluster with no "free tail" that an elementary automorphism would
    remove. Make this precise and prove what you can: is T bounded by a
    function of (n, S, kappa, N) for a minimal representative, or by a
    function of the Puiseux characteristic of the place of A_F-bar at
    infinity?
(3) The dicritical side: D = sum_l s_l n + kappa + T with the first term
    the degree of the pullback of L_infty along the dicriticals and
    kappa the transverse sheets; T is what remains. For a minimal
    representative, use the (reviewed) MERIDIAN-FLOOR+ and SHARP-CHAU
    (D >= n S + 1) as controls and find the FIRST case where T > 0 is
    forced (T = 0 means D = Sn + kappa: does the Keller condition allow
    it? test on the N = 4 (B3) profile data: S = 1, n >= 4, kappa <= 4).
(4) NEGATIVE ROUTE: the ceiling flagship's family (x, x^c y^N) has all
    its growth in T at fixed N but is NOT Keller; find where Keller +
    degree-minimality stops T from growing, or exhibit a Keller-
    compatible cluster family (satisfying NOETHER-K and the proximity
    inequalities) with T → ∞ at fixed N, n, S, kappa — that would type
    OPEN[SAT-MASS] as undecidable from the ledger and name the missing
    datum.
(5) CONSEQUENCES: for any bound T <= tau(N, n) you prove, the price of
    MOH-CROSS per (N, W): n <= (100 − kappa − tau)/S closes the cell;
    tabulate for N = 4..16 with the reviewed floors on n.
Discipline: consume the ceiling set at the review's typing WITH its
repairs (NO-CEILING as [LATTICE-LEDGER]; NEG-GEN as a lower-bound
refutation; Moh's normalisation = both coordinates <= 100); DEG-AF, the
Chau lane and the boundary instrument at their reviewed typings; no
case (A), no A2 cells, no Z(G) = 1. Literature from refs/ only (Moh 1983
is there; hash anything you read). Desk-scale CAS (< 15 min, < 4 GB);
state the bounded quantity of every OPEN you raise; do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/sat-mass-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-review-gpt55-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md
charged_input=xmodel/b3-boundary-instrument-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  {{LANE_INPUTS}}/n-vs-mapdeg-review-gpt55-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
e9f26dde675665febdedd2b2555d2c35d02b0719df10cde56637e23b0a71887f  {{LANE_INPUTS}}/b3-boundary-instrument-opus5-20260902.md
```
