# Research lane: MERIDIAN-FLOOR-SHARPEN — raise the only N-monotone bound with the group data (flagship effort)

DEG-AF-VS-N (charged, reviewed: PROMOTE with repairs) proved
MERIDIAN-FLOOR: for a noninvertible Keller map of geometric degree N
under H2, the Aut-minimal degree of A_F-bar satisfies
n_min >= ceil((N-1)/(W - S)) >= ceil((N-1)/(W-1)), W = N - a,
S = sum_l s_l, using ONLY the generic meridian cycle type
1^a · prod_l (mu_l)^{s_l} and transitivity. It is the first N-monotone
statement in the record. Its price is exact: a cell (N, W) is EMPTY as
soon as an upper bound n_min <= C holds with C < ceil((N-1)/(W-S)); at
W = 2 any C < N-1 kills the column at every N. The reviewer confirmed the
floor and its compatibility with CUSP-PARITY and ORBIFOLD-CAGE, and
named the successor: feed the floor the rest of the group data.

Your task: sharpen the floor as far as the reviewed group theory allows,
and price every cell.
(1) Reprove MERIDIAN-FLOOR in your own words (state exactly which
    property of the parametrisation degree the meridian argument
    bounds), then add, one at a time, the reviewed relations on the
    same representation rho: CENTRAL-RANK (r = j - 1), CUSP-PARITY,
    ORBIFOLD-CAGE (s + s' = M + 2 - j), PERIPHERAL-RANK and
    MERIDIAN-SPAN (kappa*j <= a, under the cage window F1), the
    point-stabiliser structure at the cusp (rho(Loc_{p_0}) with the
    fibre partition, a_{p_0} = #size-1 parts), and the (B3)-specific
    B3-DEGREE / B3-CAGE (SCOPE[B3-QH]). For each: does it raise the
    denominator's effective value (W - S -> smaller) or the numerator
    (N - 1 -> larger), and by how much? Produce the sharpest floor
    n_min >= Phi(N, a, profile) you can prove, with its hypotheses.
(2) PRICE TABLE: for N = 4..20 and every counting-admissible (a, W,
    profile) under THEOREM PROFILE, tabulate the sharpened floor and the
    threshold C(N, W) below which an upper bound would kill the cell.
    Identify the cells where the floor already exceeds the CEILING
    n <= 3 delta_aff for every profile-admissible delta_aff (those cells
    are EMPTY outright — check whether any exist; the reviewed
    DEG-DELTA(b) is the ceiling).
(3) (B2) at 5 <= N <= 16: the reviewed death condition is
    delta_aff <= 3 (N <= 10) / <= 1 (11..16). Use the floor plus the
    ceiling (delta_aff >= (n_min - 1)/3 roughly) to give a LOWER bound
    on delta_aff per (N, W); if it exceeds the death threshold at some
    cell the cell is inconsistent — say which, if any.
(4) Name exactly what a matching UPPER bound would have to be
    (n_min <= C(N)) for the column W = 2 to die at all N, and whether
    any reviewed statement supplies a bound of that shape for ANY
    profile (the reviewer says none does; confirm or refute).
Discipline: consume DEG-AF-VS-N at the review's PROMOTE typing WITH its
repairs (SG-INV reparametrisation, b_1 | b_0 escape, family = affine
representatives); the cusp/homology set and THEOREM PROFILE at banked
typing; no Z(G) = 1; no case (A) (it is EMPTY, integration #9); no A2
cells. Desk-scale CAS only; state the bounded quantity of every OPEN you
raise; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/meridian-floor-sharpen-opus5-20260902.md
Seal-at-completion; bounded writes; target 20-30KB.
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-review-gpt55-20260902.md
charged_input=xmodel/homcover-transfer-opus5-20260902.md
charged_input=xmodel/cusp-a-n8-gate-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
50f62fae3d6265f93781185e62979925471063676cbeb0d1fe67c8dfc170e056  {{LANE_INPUTS}}/deg-af-vs-n-review-gpt55-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
2a1717aec9999608b13e3de9432d841d5746152e0b5590a87430d6a69215c459  {{LANE_INPUTS}}/cusp-a-n8-gate-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
```
