# Research lane: B3-BOUNDARY-INSTRUMENT — the degree-free Domrina–Orevkov package at general N, fed by the affine cage (flagship effort)

State of the (B3) horn after today (charged flagship + its review, all
CONFIRMED with repairs): the affine/representation cage (B3-DEGREE,
B3-CAGE, Props 3.1–3.2, B3-N4, PERIPHERAL/MERIDIAN gates) is rigid but
cannot be empty by construction; log-BMY on the source curve E is VOID
by theorem (E-BMY-VACUITY); the numerical type of E at N = 4, k = 1 is
realised by an explicit plane quintic (no embedding obstruction);
the counting-vs-covering table never crosses (B3-E-NOCROSS) and its
only gate is OPEN[DEG-AF-VS-N] (a parallel flagship owns that). What
actually kills the object at N = 4 is Domrina–Orevkov I sections 2–7
(charged replay): a BOUNDARY argument — local census (Lemmas 8–9) →
six boundary graphs → Lemmas 10–15 — on the determinant package
(Prop 3: det R_a = 1, det D_a > 1, det L_a > 1, det L = −1, pairwise
coprime branch determinants; Lemmas 1–5; the edge formula; RH on
F|_{a~} : P^1 → P^1), whose finiteness is literally sum Deg a~ = 4. The
tools are degree-free; the kill is not. The review rejected the naive
successor (an intersection number E-bar_X · l with nothing to consume
it). THEOREM E-CHARGE is the one bridge: Orevkov's excess k_t at a
point t of the dicritical equals the same-branch contact degrees of E's
places at infinity, and a − a_p = K_p is carried entirely by those
places.

Your task: build the boundary instrument the campaign lacks.
(1) EXTRACT the degree-free part of the DO package as a standalone
    statement at general N: the dual/splice graph of X \ A^2 for a
    Keller map with one dicritical of degree s and multiplicity mu
    (the (B3) profile has one affine-image dicritical; state what the
    cage pins: W, a, the (s_l, mu_l), the cusp orbit data), the
    determinant identities that hold for EVERY N, and the fork/census
    inequality sum Deg a~ = N in the form that stays true.
(2) FEED IT THE AFFINE DATA. Use E-CHARGE (with the review's
    contracted-model repair) to convert the cage's affine numbers
    (a, a_p, K_p, the fibre partition over the cusp and the nodes) into
    boundary data on the dicritical's chain: which vertices of the
    graph carry which excess, and what the determinants of the
    resulting branches must be. This is the step nobody has written:
    the DO package with the campaign's affine ledger substituted in.
(3) CONTROL 1 (mandatory, first): at N = 4 the substituted package must
    reproduce the (mu, corr) = (2,1) kill — say exactly which lemma
    fires with the affine data in place, and whether the affine data
    shortens the DO census (fewer than 35 rows / six graphs).
(4) CONTROL 2 (Sol's Γ regression, charged submission Card 2): the
    banked curve y^2 = x^3 (x − 1)^2, parametrised (t^2, t^3(t^2 − 1)),
    has exactly one (2,3) cusp and one node — a curve-level (B3) k = 1
    datum. Any invariant you propose must reproduce its forced cusp
    preimage y_0, chi_c(E) = 1 − 4k, and the predicted genus/ends, or
    be archived.
(5) N = 5 and N = 6: run the substituted package on the (B3) profiles
    THEOREM PROFILE admits there ((B2) beta-forced is a different row —
    do not mix). Either an EMPTY window in N (the first ever for (B3))
    with the lemma that fires, or the exact residual and the datum the
    boundary side still lacks (typed OPEN).
(6) Name the uniformity obstruction precisely: what grows with N in the
    census, and whether the affine data bound it (e.g. does K_p or the
    fibre partition cap the number of forks?).
Discipline: consume the eight (B3) theorems at the review's CONFIRMED
typing WITH their repairs; DO I only through the charged replay's
assembly (its repairs are binding); no Z(G) = 1; no case (A); no A2
cells; the E_0 quintic is REPRESENTATIVE, not a preimage. Desk-scale
CAS only; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/b3-boundary-instrument-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/b3-e-geometry-opus5-20260902.md
charged_input=xmodel/b3-e-geometry-review-grok46-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/ideation-20260902T0741Z-sol56.md
charged_input=xmodel/do1-mu2-replay-sol56-20260901.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  {{LANE_INPUTS}}/b3-e-geometry-opus5-20260902.md
12dea79fc65d31dd5ac2dac9fa3faff638cd1d5a12b7c6f72a7f18658b09ba4a  {{LANE_INPUTS}}/b3-e-geometry-review-grok46-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
717134c733adc17b3b70409b018858fb1311c37608a24f0eebe65ae79aec8b11  {{LANE_INPUTS}}/ideation-20260902T0741Z-sol56.md
8607da5c6a963e459fb463125c1db83c4ee13743964f383919c95a5a300a3696  {{LANE_INPUTS}}/do1-mu2-replay-sol56-20260901.md
```
