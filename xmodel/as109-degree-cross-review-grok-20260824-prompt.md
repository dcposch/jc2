# Hostile different-model review — AS109 HENSEL TO GLOBAL DEGREE

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer/review artifacts on top.

Read in full:

- `xmodel/as109-hensel-global-degree-cross-gate-20260824.md`
- every file under `cases/as109_degree_cross_20260824/`
- the dual-confirmed AS109 Hensel producer/review and carry erratum/review
- the confirmed secant-idempotent materials and cited sheet-ledger statements
  only where the producer uses them

Frozen hashes:

- report: `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133`
- replay: `c0587c220cc9ca0e92bf8cd57fab466787ca6caa88fb61c8aceb7affb806f7b7`

Independently rerun the replay and attack exactly:

1. Under the conditional exact-lift hypothesis, prove or refute algebraic
   independence of `P,Q`, finiteness and separability of
   `L=Q_109(x,y)` over `M=Q_109(P,Q)`, and interpretation of its degree as
   generic mapping degree.
2. Audit parameter Hensel over `R=Z_109[[S,T]]` at all 109 points `(a,b)`.
   Check completeness hypotheses, target substitution, uniqueness, pairwise
   distinct residues, and that evaluation really gives 109 distinct
   **M-embeddings of the field L into E=Frac(R)** rather than only maps of a
   polynomial ring. Attack the kernel-height argument and every denominator.
3. Derive `d>=109` from separability without assuming `E` algebraically
   closed. Then prove or refute the finite-etale algebra decomposition
   `L tensor_M E ~= E^109 x A_infinity`, its rank statement, and the exact
   meaning of the residual factor. Check whether more than 109 split factors
   or non-field factors affect any wording.
4. Audit descent to a finitely generated coefficient field `k0` and scalar
   extension to `Q_109` and `C`. In particular, rule out a degree drop or
   tensor-product splitting under constant-field extension; justify that the
   complex map after an abstract embedding has the same generic/topological
   degree and still has constant Jacobian one.
5. Attack every monodromy statement. Distinguish automorphisms of the split
   `E^109` factor from `M`-automorphisms of `L`; check the conditional
   implications `deck C_109 => 109|d` and
   `A_infinity=0 + deck descent => cyclic Galois degree 109`. Verify no
   inertia, divisibility, congruence, or global monodromy element is smuggled
   in.
6. Recompute the controls
   `G_N=(x-x^109+109*x^N,y)` for every `N>=109`: residue-ball Hensel,
   integral unit Jacobian, nonconstant-Jacobian status, and generic degree N.
   Decide exactly what they disprove and what they do not say under the
   Keller hypothesis.
7. Audit the stated interactions with td6/TDU, secant ranks, Bezout/leading
   degree, and bounded-y no-gos. Mark any restatement as such and quarantine
   unreviewed prime-degree claims. Identify the smallest genuinely global
   missing bridge to eliminate `A_infinity` or descend deck permutations.
8. Enforce scope: this is conditional on a lift, constructs none, and at most
   proves a degree lower bound/formal split. It must not become a lift
   obstruction, degree congruence, properness theorem, or JC2 decision.

Try hard to find a field-theoretic or completion error. Do not edit producer
or canonical files, attempt the successor infinity gate, or launch AWS.

Write exactly one file:

`xmodel/as109-degree-cross-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
full hashes, independent algebra/replay, dependency and scalar-extension
caveats, exact scope exclusions, and promotion advice.
