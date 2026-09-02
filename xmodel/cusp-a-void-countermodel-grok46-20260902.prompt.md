# Paired review lane: CUSP-A-VOID — countermodel hunt and hidden-assumption audit

The charged producer report (Opus 5, cusp-a-n8-gate) proves, it says,
that MPRIME case (A) is EMPTY at every degree: THEOREM NO-CUSP-PREIMAGE
(the cusp of a cone-type non-properness curve x^p = y^q has no preimage
under an étale map that is proper over the complement) and THEOREM
CUSP-A-VOID (chi(E) = 1 forces an A^1 component mapping into C^*). A
line-by-line gate runs in parallel; YOUR job is adversarial: break it.
(1) Hidden assumptions: list every fact the two proofs consume
    (properness over the complement, surjectivity, smoothness of E,
    disjointness of components, chi additivity, the C^*-retraction) and
    for each try to build a model where it fails while the stated
    hypotheses hold. Note that any étale polynomial self-map of C^2 is
    Keller, so countermodels must live on other surfaces: e.g. the
    N-fold covering Y of C^2 minus a cone curve classified by a transitive
    representation (E empty, chi(Y) = 0) — show where the argument
    correctly refuses to let Y be an open subset of C^2 with curve
    complement, or find a case where it does not.
(2) Test the C^*-retraction step on a NON-quasihomogeneous unicuspidal
    curve homeomorphic to C (there are none by Lin–Zaidenberg — confirm
    that dependence and its exact statement/scope over C).
(3) Try to defeat "A^1 -> C^* is constant" by exhibiting a component that
    is A^1 but whose image is NOT in C^*: is it really impossible for a
    component of E to pass over the cusp? (This is NO-CUSP-PREIMAGE
    again — attack it from the topology of the fibre over c: étale,
    finite fibre, section of a connected covering.)
(4) Cross-examine the FLAGGED conflict with MPRIME Prop 6.1
    ("a_p = 1, K_p = a-1"): construct the two readings and say which one
    the charged MPRIME text supports.
(5) Attack Chain II (PERIPHERAL-RANK, MERIDIAN-SPAN) with explicit small
    representations: search transitive reps of torus-knot groups
    <alpha,beta | alpha^p = beta^q> into S_N for N <= 9 that violate
    kappa*j <= a or the genus-0 claim; report any violator with its data.
Deliver: REFUTED (with the countermodel) / SURVIVES (with the exact list
of hypotheses that carry it) per theorem, plus any scope narrowing.
Desk-scale computation only (python/sympy, < 15 min per job); do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/cusp-a-void-countermodel-grok46-20260902.md
Seal-at-completion; bounded writes; target 15-25KB; 90 minutes.
charged_input=xmodel/cusp-a-n8-gate-opus5-20260902.md
charged_input=xmodel/case-a-sweep-grok46-20260902.md
charged_input=xmodel/homcover-transfer-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
2a1717aec9999608b13e3de9432d841d5746152e0b5590a87430d6a69215c459  {{LANE_INPUTS}}/cusp-a-n8-gate-opus5-20260902.md
6fa3447c0bdbc28347f287820bd95ea11c2fec37b3310d20adc8da3a75c87ea1  {{LANE_INPUTS}}/case-a-sweep-grok46-20260902.md
fa52e816869fc689db23d5dfb6354be0cf88cb361f365dd9ff16f51c01d97883  {{LANE_INPUTS}}/homcover-transfer-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
```
