# Research lane: N-VS-MAPDEG — the all-degree ceiling in its sharpest form (flagship effort)

Today's DEG-AF-VS-N flagship (charged; under review in parallel) made
the campaign's degree question precise. Under H2 the quantity the (B2)
beta-bound and the (B3) budget consume is delta_aff = sum of the delta
invariants of the affine singularities of A_F (= the gap count of the
semigroup at infinity, Aut-invariant). It is squeezed by the
Aut-minimal degree n_min of A_F-bar: delta_aff <= (n_min-1)(n_min-2)/2
and n_min <= 3 delta_aff. A lower bound exists and is N-monotone
(MERIDIAN-FLOOR: n_min >= ceil((N-1)/(W-1)), W = N - a; at W = 2,
n_min >= N-1). An UPPER bound n_min <= C(N) — equivalently, by Chau's
cap n <= max(deg P, deg Q), a bound on the Aut-minimal coordinate
degrees of the Keller pair in terms of its geometric degree N — is
NEITHER derivable from the banked ledger (every constraint is
satisfiable with the number of nodes k -> infinity at fixed N; an
explicit one-cusp k-node curve family blocks the gate) NOR known to be
false. The price is exact: a cell (N, W) is EMPTY as soon as
n_min <= C with C < ceil((N-1)/(W-1)); at W = 2, any C < N - 1 kills the
column at every N. This is OPEN[N-VS-MAPDEG] (upper half), and it is the
all-degree ceiling the campaign has lacked since the surveys.

Your task, flagship effort, creativity and directness wanted:
(1) STATE the question invariantly: D_min(F) := min over target
    automorphisms psi (and source automorphisms — say which are
    allowed and why) of max(deg(psi o F)_1, deg(psi o F)_2) for a
    noninvertible Keller map F of geometric degree N. Relate D_min to
    n_min (Chau: n <= max(deg P, deg Q) with one place at infinity; is
    the inequality ever strict at the minimum?) and to the classical
    degree data (the Newton polygon after Aut-normalisation, the
    Abhyankar–Moh semigroup of the dicritical's image, Jung–van der
    Kulk reduced words). Is D_min bounded in N a known open problem, a
    known theorem, or known false? Be exact about the literature you
    can verify (refs/ only; hash anything fetched).
(2) ATTACK from the boundary: for a Keller map, the compactified
    boundary (the Domrina–Orevkov / Orevkov splice graph of X \ A^2,
    the dicriticals, their multiplicities mu_l and degrees s_l with
    2 sum s_l <= W) carries determinant identities that are degree-free
    (det L = -1, det R_a = 1, pairwise-coprime branch determinants). Do
    those identities, together with the affine data (delta_aff, the
    cusp type, K_p), bound the number of forks / the length of the
    boundary chain / the degree of the pair? Where exactly does
    "sum Deg a~ = N" enter and what does it bound at general N?
(3) ATTACK from the semigroup: with Gamma the semigroup at infinity of
    A_F and the dicritical map l' = A^1 -> A_F of degree s_l, the
    parametrisation degree is s_l * (something); is that something
    bounded by the semigroup data plus N? Use Abhyankar–Moh (one place
    at infinity), the conductor 2 delta_aff, and the fact that the
    parametrisation is the restriction of the Keller pair to a
    dicritical.
(4) NEGATIVE ROUTE: try to build, for fixed N (say N = 6 or 8), a
    sequence of boundary graphs / semigroup data satisfying every banked
    constraint AND the boundary determinant identities with n_min -> ∞.
    If you can, the ceiling is genuinely undecidable from boundary +
    affine data and the campaign needs a new invariant — say which
    datum every candidate family leaves free. If you cannot, name the
    identity that stops it.
(5) CONSEQUENCES: for whatever bound or obstruction you find, compute
    the (N, W) cells it kills via the crossing price, and the (B2)/(B3)
    ranges it closes.
Discipline: consume DEG-AF-VS-N's theorems as PROPOSALS (its review runs
in parallel) — re-derive what you use; MPRIME, HF, CD, COMPANION, B3E at
their banked/reviewed typings; do not consume Z(G) = 1, case (A), or A2
cells; the k-node family and E_0 are REPRESENTATIVE curves, not Keller
data. Desk-scale CAS (< 15 min, < 4 GB per job); qqideal 0.2.0 +
msolveio 0.2.1 default; state the bounded quantity of every OPEN you
raise. Do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/n-vs-mapdeg-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md
charged_input=xmodel/companion-curve-alln-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-review-grok46-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  {{LANE_INPUTS}}/companion-curve-alln-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  {{LANE_INPUTS}}/b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  {{LANE_INPUTS}}/b3-e-geometry-review-grok46-20260902.md
```
