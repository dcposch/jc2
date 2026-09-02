# Instrument lane: KELLER-CLUSTER-CENSUS codegen — enumerate numerical base clusters satisfying the full Keller ledger

Integration #12 (charged) promoted the polar ledger of a noninvertible
Keller map F of geometric degree N on the resolution X → P^2 of its
common-degree extension: Z = Phi^* L_infty = D H − sum a_i E_i over the
base cluster at infinity (base points on L_infty, with infinitely near
points and proximity), and the Keller-specific NOETHER-K equations
      sum a_i = 3D − 2N − kappa + n(W − S),      sum a_i^2 = D^2 − N,
with D = max(deg P, deg Q), kappa = sum_{C→L_inf} k_C in [1, N], n =
deg A_F-bar, W = N − a, S = sum_l s_l (dicritical degrees, 2S <= W,
mu_l >= 2, sum s_l mu_l = W), plus DEG-SPLIT D = S n + kappa + T (T the
satellite mass), the proximity inequalities of the cluster (a_i >= sum
of the a_j proximate to i), Z nef with Z^2 = N, and the reviewed floors
(MERIDIAN-FLOOR+: n >= ceil((N−1)/(W−S)) + 1; SHARP-CHAU: D >= Sn + 1;
Moh: D >= 101 for an actual counterexample). The ceiling lane's small
forest model (blow-up forests with r <= 5 points, multiplicities <= 4 at
N = 8) found NO solution of the FULL Keller ledger, and 40 monomial maps
none — but that was tiny. NO-CEILING[LATTICE-LEDGER] says the lattice
part alone cannot bound D; whether NOETHER-K (the Keller part) does is
OPEN[ANTICANON-DEFECT]. A census of the ledger's numerical solutions is
the cheapest way to see where a counterexample could numerically live
below and above Moh's 101, and whether the Keller equations already
exclude everything small.
Deliver a fail-closed enumerator (python 3, integers only; no CAS) and a
box01 job spec:
(1) INPUT: N in 2..8 (and a switch for any N), D <= D_max (declare;
    default 40 for the desk run, 200 for the box run), and the profile
    data ranges the promoted ledger allows: a in (N/2, N−2] (THEOREM
    PROFILE's counting window; also allow the reducible/other windows
    as a flag), W = N − a, dicritical multisets (s_l, mu_l) with
    mu_l >= 2, 2 sum s_l <= W, sum s_l mu_l = W, kappa in [1, N], n in
    [floor from MERIDIAN-FLOOR+, (3N + f)/(W − S) with f a declared cap
    or unbounded], T >= 0 with D = S n + kappa + T.
(2) OBJECT: a base cluster at infinity = a rooted forest of infinitely
    near points on L_infty (roots = the points of L_infty hit; children =
    infinitely near; proximity = parent and, for satellites, the
    earlier point they are proximate to) with integer multiplicities
    a_i >= 1 satisfying the proximity inequalities; the polar divisor
    Z = D H − sum a_i E_i; Z^2 = D^2 − sum a_i^2 = N; the second NOETHER-K
    equation sum a_i = 3D − 2N − kappa + n(W − S); and the dicritical
    structure: the dicriticals are the (n >= 2)-part of the boundary
    over L_infty per BI-1 [P3] (W + a = N) — encode at least that the
    cluster's "L_infty-sheets" account for kappa and the dicritical
    multiplicities for W (the charged reports define these; if a datum
    is not pinned by the promoted ledger, expose it as a free parameter
    and say so, never guess).
(3) CONTROLS (mandatory, fail-closed): N = 1 must reproduce the Cremona
    clusters (Noether's equations sum a_i = 3D − 3, sum a_i^2 = D^2 − 1,
    e.g. the quadratic transformation D = 2, three simple points; the
    elementary map (x, y + x^k) clusters); the NEG-GEN family
    (x, x^c y^N), which is NOT Keller, must be REJECTED by the Keller
    form (its ledger carries the extra affine ramification term — show
    the enumerator would only accept it with that term added); the
    ceiling lane's 41 exactly resolved maps (their clusters are listed
    in box/nvm-drivers-20260902/) must be accepted or rejected exactly
    as the lane's engine did.
(4) OUTPUT per (N, D): the number of admissible clusters, and for each
    the tuple (D, n, S, kappa, T, W, a, forest shape, multiplicities);
    a summary table "smallest D admitting a full-ledger solution at
    each N" — with the honest statement that a numerical cluster is
    NOT a map (typing: NUMERICAL_PROFILE / NECESSARY per the PREFLIGHT
    two-field scheme).
(5) JOB SPEC for box01 (64 vCPU, python 3.12): parallelise over (N, D);
    estimate row counts; a 12h cap; outputs to ~/cluster_census/.
Run the desk census yourself for N <= 4, D <= 40 (< 15 min, < 4 GB) and
report its result. Do not edit canonical ledgers; do not inspect
jc2-lean. State the bounded quantity of any OPEN you raise.
Report: xmodel/keller-cluster-census-codegen-sol56-20260902.md (+ the
enumerator as box/keller_cluster_census.py with its tests).
Seal-at-completion; bounded writes; target 12-20KB; 90 minutes.
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-review-gpt55-20260902.md
charged_input=xmodel/integration12-coordinator-fable51-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  {{LANE_INPUTS}}/n-vs-mapdeg-review-gpt55-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  {{LANE_INPUTS}}/integration12-coordinator-fable51-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
```
