# Post-collection fingerprint dedup and voting audit — 20260824T0453Z

- Producer: OpenAI Codex, GPT-5 family, atlas audit lane
- Basis commit: dd11599b07eb05591b5c006791005eef19457d8e
- Mathematical state cutoff: 2026-08-24T04:53:35Z
- Packet: xmodel/ideation-20260824T0453Z-packet.md
- Packet SHA-256: 042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5
- Collection status: DEGRADED. Five frozen reports were complete at close. Fable missed the 60-minute cutoff, was cancelled, and supplied no report. No vote or content is imputed to it.
- Scope: post-collection comparison only. No work was launched, no network was used, no current-round prompt or missing report was inspected, and no shared ledger was edited.

The packet has one nonsemantic digest typo. Its AUDIT.md row lists
a0033b88030fbd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32,
which has 63 hexadecimal characters. The clean-basis digest consistently recorded by the frozen reports is
a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32.
The path and basis were unambiguous, the packet itself retained the packet hash above, and the packet was not mutated.

## Authorized frozen inputs

Exactly the sealed packet and the following five reports were used in this post-collection audit.

| Input | SHA-256 |
|---|---|
| xmodel/ideation-20260824T0453Z-packet.md | 042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5 |
| xmodel/ideation-20260824T0453Z-root.md | 97222d63837c4b883e94c8d667014872603b67f5663a1c86e2b1063a1435b1bc |
| xmodel/ideation-20260824T0453Z-atlas.md | 0e381be9a5f1b4d7e2976f473d3d038a3dd591789bdd9f5f4fc2368c0ce374b7 |
| xmodel/ideation-20260824T0453Z-zero-base.md | fb804efab0c2cff524512fb7f81cceb2adaea7cce299a827211310c22052ba9a |
| xmodel/ideation-20260824T0453Z-falsifier.md | 12d1fe67a1dc7be75041050be3009d8599578e10c6cb1b57d1da12ecfa800962 |
| xmodel/ideation-20260824T0453Z-grok.md | 6a7010e0d71d6bac03171e1b164a70668352d896b0da248fdb689c13494f7136 |

## Dedup rule

Each card receives a four-coordinate fingerprint:

1. target obstruction: the exact missing implication or counterexample door;
2. mechanism: the mathematical operation intended to move that obstruction;
3. object: the concrete invariant, scheme, matrix, sheaf, or certificate;
4. decisive test: the preregistered observation that would advance, stop, or repair the card.

A strict duplicate, D0, agrees on all four coordinates up to notation. An operational duplicate, D1, has the same target, mechanism family, and next experiment, but packages the invariant differently. An adjacency, A, shares a lane or obstruction while changing either the mechanism or the decisive object. Adjacencies are not merged and do not create extra votes for a common mechanism.

On this rule the 15 raw cards reduce to 12 operational candidates: one D0 pair and two D1 pairs. There are no three-way duplicates.

## Complete card map

| Card | Target obstruction | Mechanism | Concrete object | Decisive test | Dedup result |
|---|---|---|---|---|---|
| ROOT-A, DIFF-LATTICE-UNIT | Prove that the ZMT boundary is empty when the two target derivations preserve the polynomial source and form a nowhere-degenerate frame. | Saturate a finite normalization lattice under the lifted derivations; use divisorial pole orders and the determinant line to force either coherence over the target or a forbidden nonconstant unit. | A derivation-stable normalization lattice, its determinant, and the cone of boundary pole-order vectors. | One-dimensional and SNC or toroidal controls, including Laurent-boundary examples. The card survives only if the extremal-pole argument distinguishes a genuine Keller frame from an open torus. | Singleton N4; adjacent to the other global-boundary cards. |
| ROOT-B, ITERATED-LOG-VOLUME | Turn the equality F pullback of dx dy equals dx dy into a contradiction with topological degree greater than one at infinity. | Make a compactification algebraically stable under iteration; combine canonical-divisor recurrence with a nonnegative boundary pullback matrix and Perron-Frobenius growth. | Boundary divisors, discrepancy or pole vector, and the iterate pullback matrix. | Exact recurrence on automorphisms, non-Keller rational controls, and low-sheet books; stop if stability or effectivity requires the desired conclusion. | Singleton N5; adjacent to N1 and N4, not a duplicate. |
| ROOT-C, EXACT-COFRAME-K1 | Construct a characteristic-zero counterexample by finding a determinant-one polynomial coframe that integrates but cannot be the Jacobian matrix of an automorphism. | Combine unstable K1 or Mennicke-symbol non-elementarity with the closed-row integrability equations. | A matrix M in SL2(C[x,y]) whose two rows are exact one-forms and whose class is non-elementary. | Start from a Cohn-type matrix, impose both curl equations and determinant one in a bounded deformation, then certify non-elementarity independently. | Isolated singleton N6. |
| ATLAS-A, FOURIER-VERDIER NONPROPERNESS DEFECT | Detect and eliminate the nonproperness set of an étale polynomial map without choosing a boundary tree. | Six functors, characteristic cycles, Fourier-Laplace transform, and critical-point-free exponential de Rham complexes. | K_F = Cone(RF_! Q[2] to RF_* Q[2]) and the holonomic direct image F_+ O, with their conormal multiplicities. | Identity, triangular and Henon automorphisms, an affine open embedding, (x^2,xy), and a known higher-dimensional Keller counterexample; then a plane-specific positivity theorem audit. | D1 pair N1 with ZERO-A. |
| ATLAS-B, WEIGHTED-UNIT D QUOTIENT | Decide whether the first full-source D corrections close in a small source-derived state rather than by adding untyped tail variables. | Quotient the two multiplicative unit streams by their common weighted direction. | C = U_g/U_f and R = U_f^3/U_g^2; the sidecar is the first coefficient of R. | Derive the first two x-side source occurrences only. Closure must be triangular in C and R with a fixed shift; any third independent stream or missing source field stops the representation. | Singleton N7; adjacent to FALSIFIER-3 and GROK-C. |
| ATLAS-C, LOCALIZED FIXED-DEGREE COLLISION SCHEME | Decide whether the marked Artin-Schreier W2 seed lies under a bounded-degree characteristic-zero Keller collision, without following Witt levels one by one. | Local finite-type algebra, completion, cotangent and Fitting ideals, and verticality over 3. | The degree-3 Keller-collision coefficient scheme localized and completed at the seed; its generic fibre after inverting 3. | Prove the completed generic fibre is zero and extract a 3^N certificate, or exhibit a nonzero generic fibre and hence a characteristic-zero point. Tame and tower controls calibrate the local algebra. | D1 pair N3 with ZERO-C. |
| ZERO-A, TRACE-ZERO MICROLOCAL DEFECT | Show that the canonical normalization cover has no boundary inertia and therefore has degree one. | Form the trace-zero permutation local system over the finite étale locus; use middle extension, microlocal index theory, and a critical-point-free pencil to kill conormal cycles. | The trace-zero middle-extension perverse sheaf P_0 and its characteristic cycle on the target. | Deleted-point, affine-open, automorphism, Henon, and (x^2,xy) controls; compute discriminant, inertia, polar data, and characteristic-cycle multiplicities. | D1 pair N1 with ATLAS-A. Same operational mechanism, different functorial package. |
| ZERO-B, FINITE-FLAT NORMALIZATION PLUS OPEN-CHART SYNTHESIS | Either prove no ZMT boundary can coexist with the source being A2, or construct the exact global data of a counterexample. | Use finite-flat normalization, multiplication matrices, trace and codifferent constraints, affine-open epimorphisms, units, and the boundary class-group cone. | A finite normal surface X over A2 together with an open chart U = X minus D isomorphic to A2. | Analyze monogenic ranks 2 and 3 on paper, then require associativity, finite flatness, the A2 chart, unit and class-group tests, constant Jacobian, and a collision. | Strict D0 pair N2 with FALSIFIER-1. |
| ZERO-C, BOUNDED-STRATUM COMPACTNESS AND ESCAPE | Decide whether fixed-degree marked collisions persist through every p-power level, and if not prove that any compatible tower must escape every fixed degree. | Finite-branching compactness for fixed coefficient schemes, followed by Rees, tangent-cone, cotangent, and Fitting analysis. | The fixed-degree coefficient scheme Z_D and its reduction tree over Z/p^n. | At the Artin-Schreier seed, compute the associated-graded lifting equations. Either force a higher monomial at every putative lift or retain a bounded tangent direction. | D1 pair N3 with ATLAS-C. One is the local generic-fibre test; the other states its uniform escape envelope. |
| FALSIFIER-1, COMP-PAIR | Give a complete finite certificate for a characteristic-zero counterexample, or make small completion pairs fail for a stated global reason. | Reverse ZMT: construct finite covers and affine modifications, then sieve by class group, units, canonical module, and different. | A tuple (X,D,pi,j,r0,r1) with X finite normal over A2, j(A2) = X minus D, and a Keller collision on the chart. | Preregister small normal finite covers with non-Cartier boundary, require the free boundary basis in Cl(X), an exact two-chart A2 open, then test Jacobian and collision. | Strict D0 pair N2 with ZERO-B. |
| FALSIFIER-2, UNIT-INFINITY | Explain why the all-Witt Artin-Schreier tower cannot be polynomial, and decide whether mixed variables can cancel the horizontal pole. | Tate-algebra units, horizontal divisors, and pole cancellation under coupled two-variable corrections. | The class of (1-px^(p-1))^(-1) in the quotient of Tate units by polynomial units, plus its horizontal divisor. | First prove the P_y = 0 triangular no-go; then test one frozen lowest-degree coupled ansatz for cancellation. A nonzero horizontal divisor with no allowed cancellation stops the seed. | Singleton N8; adjacent to N3 and GROK-B. |
| FALSIFIER-3, X-HANKEL | Decide whether the full D source admits any finite linear representation before guessing an Ore or Spencer state. | Hankel-rank characterization of rational or finite-state series. | Source generating series U_f and U_g, including the first sidecar stream, and their block-Hankel matrices. | A source-only compiler through the first two x-side interfaces followed by exact pivot growth. Rank growth stops every fixed finite-state proposal; stable rank demands a sourced recurrence. | Singleton N9; adjacent to ATLAS-B, not a duplicate. |
| GROK-A, CONDUCTOR OF THE ZMT OPEN IMMERSION | Replace boundary emptiness by the condition that the conductor of the inclusion of the normalization into the polynomial source is the unit ideal. | Compute the ring-extension conductor and compare primitive one-forms on explicit maps. | The B-ideal f = (Abar:B) and polar divisors of f dg - x dy and g df - y dx. | Identity and triangular automorphisms versus (x^2,xy), with a stop at CONDUCTOR-TAUTOLOGY or NO-EXPLICIT-SOURCE. | Singleton N10, adjacent to N2 and N4. Not admissible as written; see the correctness audit. |
| GROK-B, P_y = 0 RIGIDITY AND MIXED-SUPPORT ESCAPE | Retire or reopen the Artin-Schreier seed by proving rigidity of the univariate slice and examining its first mixed bounded correction. | Ritt and Jung-van der Kulk factorization plus a bounded mixed W2 census. | P = x-x^p+pA(x,y), Q = y+pB(x,y), with a marked collision and a fixed degree cap. | A paper uniqueness lemma for the restricted slice and an exhaustive degree-at-most-3 search over Z/9 modulo the proposed gauges; at most one bounded W3 child after a genuinely new survivor. | Singleton N11, adjacent to N3 and N8. It is not an all-level duplicate. It needs a normalization repair. |
| GROK-C, SIDECAR LINE AND UNIT-TWIST SOFTWARE | Decide whether the first x-side D correction is a new source direction or a gauge direction attached to the origin completion. | Linear sidecar adjoint, the cube-weight line 3 alpha minus 2 beta, and a unit-twist composition factorizer. | The row-42 sidecar linear form and a factorizer for triangular multiplicative or additive twists. | Replay tame and Tate factorizations, then ask whether the sidecar form lies in the span of the six confirmed compatibility functions on an existing cell. | Singleton N12, adjacent to N7 and N9. The span test is not typed yet. |

## Duplicate verdicts

### D0: one strict duplicate

ZERO-B and FALSIFIER-1 are the same proposal at launch resolution. Both reverse the canonical ZMT factorization and seek a finite normal X over A2 containing an A2 chart whose complement freely generates the class group, followed by the same finite-flat, unit, boundary, Jacobian, and collision sieve. ZERO-B emphasizes the structural lemma and low free ranks; FALSIFIER-1 emphasizes the certificate tuple and hostile construction. These are complementary expositions of one candidate, not two votes for two mechanisms.

Merged name: COMP-PAIR / finite-flat open-chart synthesis.

### D1: two operational duplicates

ATLAS-A and ZERO-A are one microlocal proof root. The Verdier nonproperness cone and the trace-zero middle extension are not literally the same object, but both encode the finite cover over the same open target, seek the same conormal vanishing, invoke the same critical-point-free pencils and positivity, and use nearly identical controls. They should be developed as two realizations of one theorem, with comparison maps stated before either realization is treated as independent evidence.

Merged name: MICRO-DEFECT, with Verdier-cone and trace-zero variants.

ATLAS-C and ZERO-C are one fixed-stratum arithmetic root. Both replace level-by-level Witt lifting by the same fixed-degree coefficient scheme near the same marked seed and use its local or associated-graded algebra to decide verticality versus a characteristic-zero point. The local generic-fibre criterion is the sharp experiment; the compactness and escape statement is the theorem envelope.

Merged name: FIXED-STRATUM, with local-generic-fibre and uniform-escape variants.

### Important nonduplicates

- ROOT-A, ROOT-B, MICRO-DEFECT, COMP-PAIR, and GROK-A all touch the ZMT boundary, but respectively use differential stability, iterate dynamics, microlocal cycles, reverse construction, and a conductor ideal. Sharing X and D does not make them duplicate proof mechanisms.
- ATLAS-B, FALSIFIER-3, and GROK-C all address the first full-source D interface. Their tests ask, respectively, for an exponent-lattice quotient, finite Hankel rank, and first-order gauge dependence. They can share a source compiler but give logically different outcomes.
- FIXED-STRATUM, FALSIFIER-2, and GROK-B all start from the Artin-Schreier/Tate obstruction. One decides an all-level fixed-degree local scheme, one studies a horizontal unit divisor, and one examines a first mixed W2 slice. GROK-B is at most a one-sided front end to FIXED-STRATUM, not a second all-level vote.
- ROOT-C is the only exact-coframe and unstable-K1 proposal. It is independent of the normalization, D-series, and Witt clusters.

## Novelty audit: mechanisms versus renames

| Operational candidate | Novelty verdict | Reason |
|---|---|---|
| N1 MICRO-DEFECT | Genuinely new global mechanism. | It imports the six-functor or perverse-sheaf package and characteristic-cycle positivity to make nonproperness a canonical target-side defect. This is not the queued finite receiver schema, even though it still owes the boundary-vanishing theorem. |
| N2 COMP-PAIR | Genuinely new reverse-construction architecture on a known ZMT object. | The inclusion Abar in B was known, but synthesizing the finite completion and A2 open chart with class-group and different constraints is an adversarial global certificate, not another local normalization packet. |
| N3 FIXED-STRATUM | New decisive architecture for a queued obstruction, not a new obstruction. | It is the queued bounded-complexity Witt direction recast as one finite-type local generic-fibre question. The recast is materially better than another Witt level, but its vote must not be advertised as an unrelated mechanism. |
| N4 DIFF-LATTICE-UNIT | Genuinely new algebraic mechanism. | It connects target derivations, normalization lattices, divisor valuations, determinant lines, and the unit group. Its strongest feature is a plane-specific theorem with sharp toroidal controls. |
| N5 ITERATED-LOG-VOLUME | Genuinely new dynamical mechanism, with a high dependency. | It connects the invariant volume form to algebraic stability and Perron-Frobenius growth on the boundary rather than using a one-step canonical-divisor identity. |
| N6 EXACT-COFRAME-K1 | Genuinely new counterexample mechanism. | It converts a non-elementary unstable-K1 class plus polynomial Poincare exactness directly into a Keller pair. It bypasses every queued D, GGV, and Witt representation. |
| N7 WEIGHTED-UNIT D QUOTIENT | Genuinely new representation test inside the D lane. | The exponent-lattice invariants C and R are source-derived candidates, not arbitrary extra tail coordinates. It remains a D redesign, so it must pass the source-only closure test before becoming a state. |
| N8 UNIT-INFINITY | Genuinely new obstruction on the live Witt control. | The horizontal divisor of a Tate unit is a concrete algebraicity obstruction, and mixed pole cancellation is a different question from mere finite-level survival. |
| N9 X-HANKEL | Genuinely new imported mechanism. | Finite Hankel rank brings rational-series and automata theory to the source recurrence. It is a representation-independent falsifier for finite-state D claims once the source series is typed. |
| N10 ZMT-CONDUCTOR | A rename of finiteness, and geometrically defective as stated. | The unit-ideal condition is equivalent to Abar = B, but the conductor of a nonfinite open-ring extension does not generally cut out the omitted boundary. The proposed negative control is not quasi-finite. |
| N11 AS-MIXED-RIGIDITY | Mixed verdict. | The Ritt/Jung connection and transverse P_y correction are new. The finite W2 census is a refinement of the queued bounded descent, and the claimed uniqueness of the unrestricted P(x) slice is false without an added normalization or larger gauge quotient. |
| N12 SIDECAR-ADJOINT | New diagnostic and reusable factorizer, not yet a new mathematical state. | The cube-line geometry and unit-twist connection are fresh. The advertised span question still compares objects at different typed interfaces, so the adjoint cannot yet decide a source dimension. |

Thus nine operational candidates contain a genuinely new mechanism or a materially new decision architecture: N1 through N9. N11 has one new connection but needs repair. N12 is a useful diagnostic after typing. N10 does not survive dedup as a new invariant.

## Voting audit

Votes below count at most one vote per frozen submission for a theme. Raw-card counts are shown separately and never treated as independent ballots.

| Theme | Submission coverage | Raw cards | Agreement | Remaining disagreement |
|---|---:|---:|---|---|
| Canonical normalization, ZMT boundary, or global completion | 5 of 5 | 7 | Every complete report put at least one card on the global finite-versus-open boundary. No report selected a deeper GGV book or raw passport as its lead. | There is no majority mechanism: microlocal 2, completion-pair 2, differential lattice 1, iteration 1, conductor 1. The conductor vote fails its stated geometric premise. |
| Bounded polynomial lifting of a characteristic-p collision | 4 of 5 | 4 | All four cards reject unrestricted next-Witt-level work and insist on a degree or support cap. | Two choose the fixed all-level coefficient scheme; one chooses a Tate-unit obstruction; one chooses mixed W2 plus Ritt rigidity. They answer different quantifiers. |
| Full-source D redesign without new depth | 3 of 5 | 3 | All three D cards forbid band 28, an untyped Ore state, and origin-as-counterexample rhetoric. | Weighted quotient, Hankel rank, and sidecar gauge are mutually distinct models. No card has yet derived the common source functor needed to compare them. |
| Exact-coframe unstable K1 counterexample route | 1 of 5 | 1 | No duplicate or adjacent card. | High novelty, no blind corroboration, and a hard non-elementarity-preservation gate. |
| New GGV/Sigray cells, primitive-group census, raw passports, or unrestricted local-bound compute | 0 of 5 | 0 | The absence is meaningful allocation consensus: none of the 15 cards requests these stopped representations. | It is not a theorem that those avenues are false; it is a unanimous choice not to spend this round on them. |

After operational dedup, the only two-vote mechanisms are MICRO-DEFECT, COMP-PAIR, and FIXED-STRATUM. Each is a blind convergence, but not a mathematical confirmation.

The five reports are also not five independent model priors. Root, atlas, zero-base, and falsifier are Codex/GPT-5-family lanes sharing the same sealed packet and state. Grok is the only different-model report in the completed set. Blindness prevents current-round copying; it does not remove common-training, common-packet, or common-bottleneck correlation. Fable's absence further reduces model diversity. Consequently, 2-to-1 card counts are useful for detecting convergent formulations, not for estimating truth probabilities.

## Disagreement audit

### 1. What can force the boundary to vanish?

- MICRO-DEFECT says local acyclicity and positivity leave no conormal contribution.
- DIFF-LATTICE-UNIT says a stable tangent frame leaves no boundary valuation without creating a nonconstant unit.
- ITERATED-LOG-VOLUME says iteration forces spectral boundary growth incompatible with invariant volume.
- COMP-PAIR attacks the negation by trying to build an honest finite completion with an A2 chart.
- ZMT-CONDUCTOR says a unit conductor detects equality, but as written only restates equality.

These should not be averaged. They are four independent proof or falsifier interfaces to the same canonical triple. A countermodel to a proposed microlocal lemma need not affect the differential theorem, and failure of low-rank completion synthesis is not evidence that either proof theorem holds.

### 2. Which characteristic-p quantifier matters?

FIXED-STRATUM asks whether one fixed finite-type scheme has a generic fibre near the marked seed. UNIT-INFINITY asks whether an analytic unit's horizontal pole can be cancelled by any allowed polynomial coupling. AS-MIXED-RIGIDITY asks only whether a frozen W2 mixed slice is empty or contains a new first-order point. A W2 survivor does not vote against fixed-degree escape; it only supplies a tangent direction. A W2-empty fixed cap kills that cap but says nothing about larger D. Only the fixed-scheme generic fibre or a proved uniform escape statement reaches the all-level bounded question.

### 3. What is the first new D state?

WEIGHTED-UNIT predicts exactly one new weight-zero stream R. X-HANKEL refuses to posit a state and asks whether any bounded realization exists. SIDECAR-ADJOINT asks whether the first visible stream is instead gauge. These predictions are genuinely in tension:

- a new independent sidecar direction favors the quotient card;
- unbounded Hankel rank kills every fixed finite-state closure, including the quotient card;
- a typed gauge dependence kills the sidecar as a new state but does not prove a recurrence.

The common source-only compiler is therefore a dependency, not a fourth vote.

### 4. Proof-first versus counterexample-first

ROOT-A, ROOT-B, and MICRO-DEFECT seek a theorem. COMP-PAIR and EXACT-COFRAME-K1 seek an exact characteristic-zero counterexample certificate. The arithmetic cards seek either a counterexample or a finite no-lift certificate. The collection agrees on exact stopping rules but does not agree that proof-side global geometry should receive all resources.

### 5. New lane versus queued redesign

The collection did not simply return the three queued redesigns, but it did not escape them uniformly. FIXED-STRATUM is a strong reformulation of queued bounded Witt descent. WEIGHTED-UNIT and X-HANKEL are new mechanisms within queued full-source D typing. GROK-C remains a first-order D diagnostic. MICRO-DEFECT, DIFF-LATTICE-UNIT, ITERATED-LOG-VOLUME, EXACT-COFRAME-K1, COMP-PAIR, and UNIT-INFINITY are the clearest independent mechanisms.

## Hidden shared assumptions

1. The canonical normalization and ZMT open immersion are assumed to be the right common global object. This is exact for a Keller map, but accessibility of its boundary is the unsolved step, not a free input.
2. Polynomial origin is assumed to leave a functorial trace in one of the proposed objects. The failed local-normalization receiver is evidence that this information is not contained in the finite local algebra alone.
3. Low-degree automorphisms and one or two non-Keller maps are assumed to be hostile enough controls. They can detect bugs and tautologies, but they cannot establish a plane-specific vanishing theorem.
4. Several proof cards assume positivity: effective conormal multiplicities, a salient pole-order cone, or a nonnegative iterate matrix. The exact source of positivity is a central theorem dependency in each card.
5. Every bounded-search card assumes its degree, support, gauge, and marked collision define a complete finite-type stratum. An unrecorded coordinate change can turn a claimed empty or unique slice into a gauge artifact.
6. The D cards assume the first two x-side coefficients can be derived from the polynomial source without importing the untyped alpha and beta as free state. That derivation is precisely the missing interface.
7. The compactness cards assume all levels belong to one fixed coefficient scheme. This is sound only after support, degree, normalization, and reduction maps are frozen.
8. Blind convergence is assumed to indicate robustness. Four reports share a model family and all five share the packet; convergence is a reason to merge and inspect, not a confidence multiplier.

## Correctness and dependency gates

These are audit findings, not promoted claims.

### MICRO-DEFECT endgame

Vanishing of one cone Cone(RF_!Q to RF_*Q) must be proved to detect every missing end of this particular étale map; the general properness criterion quantifies over coefficients, not automatically over the constant sheaf alone. In the trace-zero variant, absence of conormal components must be connected explicitly to extension of the finite cover across the nonproper set, then to a connected finite étale cover of A2, then to degree one. Until those implications are written, the two packages are promising detectors rather than a proof.

### COMP-PAIR exact sequence

Finite normalization over the regular target is plausibly finite flat because a normal surface is Cohen-Macaulay, and a finite projective module over C[P,Q] is free. The claimed free boundary basis in Cl(X) additionally uses the localization exact sequence, pure codimension-one complement, and equality of units on X and U. Those hypotheses must be verified on every candidate; they are not optional sieve heuristics.

### FIXED-STRATUM localization

The local generic-fibre fork is exact only after the integer coefficient scheme, marked collision, degree cap, and local seed are fixed. The implication from a nonzero completed ring after inverting 3 to a characteristic-zero point should be recorded through faithful flatness and finite type. The compactness implication from points modulo every p^n to a compatible p-adic branch uses finite branching of this same fixed scheme. With those statements explicit, this is the cleanest finite decision object in the round.

### DIFF-LATTICE and ITERATED-LOG-VOLUME

DIFF-LATTICE must prove that saturation stays coherent or that an extremal boundary pole yields an actual unit of B, rather than a rational semi-invariant. Its toroidal control is decisive.

ITERATED-LOG-VOLUME must produce one model on which the needed pullbacks are stable and the boundary recurrence is effective for all iterates. Re-blowing up separately at every iterate would destroy the finite nonnegative matrix and reduce the proposal to the existing boundary problem.

### EXACT-COFRAME-K1

Three algebraic facts need separate certificates: both rows remain exact after deformation; the resulting matrix retains a nontrivial Mennicke or non-elementary class; and Jacobian matrices of all plane automorphisms lie in the elementary class after the substitutions arising in the chain rule. The last point is plausible from Jung-van der Kulk, but it should be stated with the correct unstable-K1 quotient, since E2 need not behave like a normal subgroup in every formulation.

### D quotient and Hankel

The formulas C = U_g/U_f and R = U_f^3/U_g^2 are exact formal-unit changes of variables, and the coefficient 3 alpha minus 2 beta is the first logarithmic coefficient of R. They become a state theorem only if the polynomial source derives the shifts and closes the next x-side interfaces.

For X-HANKEL, finite Hankel rank characterizes a finite linear representation only after the coefficient ordering, base field, block structure, and source series are fixed. Rank growth is then a strong falsifier; rank stability alone does not identify the nonlinear D recurrence.

### UNIT-INFINITY

The Tate factor gives an exact nonpolynomial control in the restricted slice. A horizontal divisor obstructs polynomiality of that factor, but the mixed program must prove that allowed two-variable corrections cannot cancel it. Without that stability statement, the card excludes one factorization, not the seed.

### ZMT-CONDUCTOR is false as stated

For an open immersion, the conductor of the induced nonfinite ring extension need not cut out the complement. The elementary example

A = C[t],  B = C[t,t^(-1)]

has Spec B = D(t) inside Spec A, but (A:B) is zero: multiplying any nonzero Laurent polynomial by a sufficiently negative power of t leaves A. Its vanishing set on Spec A is all of Spec A, not the omitted point.

The condition (Abar:B) = B is still equivalent to Abar = B, because it says 1 belongs to the conductor. That is exactly the finiteness/equality target and supplies no cheaper boundary invariant. Moreover, (x^2,xy) is not quasi-finite: the fibre over the origin contains the line x = 0. It is therefore not a valid negative control for the claimed ZMT open immersion. N10 should be rejected until it is replaced by a coherent boundary ideal or a finite module that exists before equality is known.

### AS-MIXED-RIGIDITY needs a gauge repair

The raw claim that the displayed F_n is the unique restricted lift when P is merely allowed to vary in R_n[x] is false without further normalization. Over Z/9, for p = 3, set

P = x - x^3 + 3x^2,

Q = y(1 - 6x + 3x^2).

Then P reduces to x-x^3, Q reduces to y, and

P_x = 1 + 6x - 3x^2.

Writing a = 6x - 3x^2, one has a^2 = 0 modulo 9, so P_x(1-a) = 1 modulo 9. Thus this is another determinant-one restricted lift, not the displayed F_2 as a literal pair. It may be equivalent under a larger lift-preserving gauge, but that equivalence must be defined and proved. Freezing P exactly, or quotienting the full nilpotent triangular gauge, is required before uniqueness or an exhaustive mixed census is meaningful.

### SIDECAR-ADJOINT is not typed

The row-42 form 3 alpha minus 2 beta and the six earlier compatibility functions do not yet live in a declared common source tangent space or common output band. Linear dependence between them is therefore undefined until a source map transports all seven forms into one vector space. The unit-twist factorizer is independently well posed; the sidecar span test is not. This is the same missing typing that stopped the full D state, not a way around it.

## Readiness and dependency tiers

These tiers rate the next discriminator, not the probability of the target theorem.

| Tier | Candidates | Readiness statement |
|---|---|---|
| T1: exact discriminator can be specified now | N1 MICRO-DEFECT, N3 FIXED-STRATUM, N4 DIFF-LATTICE-UNIT, N6 EXACT-COFRAME-K1, N8 UNIT-INFINITY | Each has a finite paper or exact-algebra gate and explicit controls. The ultimate theorem may be hard, but failure at the first gate is informative without a new campaign representation. N1 must begin with the properness endgame lemma; N3 with the exact local scheme; N4 with the toroidal lemma; N6 with the elementary-class premise; N8 with the restricted triangular theorem. |
| T2: one new explicit object or compiler is required | N2 COMP-PAIR, N5 ITERATED-LOG-VOLUME, N7 WEIGHTED-UNIT D QUOTIENT, N9 X-HANKEL | These are well-posed after, respectively, a low-rank finite cover presentation, a common algebraically stable boundary model, or a source-only x-side compiler. None should be treated as ready merely because existing banked data share its vocabulary. |
| T3: repair before experiment | N11 AS-MIXED-RIGIDITY, N12 SIDECAR-ADJOINT | N11 needs a correct normalization and gauge quotient. N12 needs a common typed source tangent map. The factorizer subcomponent of N12 is T1 software, but it does not decide the D claim by itself. |
| T4: reject as written | N10 ZMT-CONDUCTOR | Its support claim fails for the basic Laurent open immersion, its proposed negative control is not quasi-finite, and the surviving unit-ideal statement is exactly Abar = B. |

## Ranked operational candidates

Rank is by expected information per first discriminator, global reach, novelty, and dependency risk. It is not a launch order and does not promote any claim.

1. **N1 MICRO-DEFECT.** This is the strongest global proof architecture and the clearest blind operational convergence. First require the exact lemma connecting the chosen defect to properness and the trace-zero variant to degree one. If that lemma fails on an open-embedding control, stop before any D-module calculation.
2. **N4 DIFF-LATTICE-UNIT.** It is genuinely new, algebraic, plane-specific, and has sharp one-dimensional and toroidal falsifiers. It also attacks the same boundary from the source tangent frame, independently of microlocal positivity.
3. **N3 FIXED-STRATUM.** It has the most decisive finite fork: a power-of-3 no-lift certificate or a characteristic-zero point. Its two submissions are duplicates rather than independent evidence, and it remains one bounded seed rather than a proof of JC2.
4. **N2 COMP-PAIR.** It supplies the canonical adversarial testbed for every global proof card and an exact counterexample certificate if successful. Low-rank paper constraints should precede any enumeration; failure of a finite menu has no cofinal meaning.
5. **N6 EXACT-COFRAME-K1.** It is the most orthogonal and potentially revolutionary card. The elementary-class implication and a stable non-elementarity certificate are cheap enough to audit before any coefficient search.
6. **N5 ITERATED-LOG-VOLUME.** Iteration and spectral cones are a real new connection, but the existence of one effective algebraically stable model is a large dependency. A recurrence on explicit controls is useful only if it does not silently rebuild that theorem.
7. **N9 X-HANKEL.** Once a source-only coefficient stream is typed, Hankel growth is the cleanest way to falsify every finite D state at once. It should precede elaborate Ore or Spencer guesses.
8. **N7 WEIGHTED-UNIT D QUOTIENT.** The exponent-lattice variables are mathematically natural and explain the sidecar coefficient. It ranks below Hankel because closure through two source interfaces is still conjectural and representation-specific.
9. **N8 UNIT-INFINITY.** The horizontal-divisor object is exact and reusable, but its present reach is one Artin-Schreier factorization. It rises if mixed cancellation can be formulated invariantly.
10. **N11 AS-MIXED-RIGIDITY, after repair.** The Ritt link is valuable, but the raw uniqueness claim has an explicit nilpotent deformation and the W2 census requires a complete gauge quotient. It is not ready in its submitted form.
11. **N12 SIDECAR-ADJOINT, after typing.** Keep the unit-twist factorizer as software. Defer the sidecar span question until the forms share a source and codomain; otherwise it repeats NO-TYPED-STATIONARITY.
12. **N10 ZMT-CONDUCTOR.** Reject the card as submitted. A future coherent boundary module could be new, but the current conductor is either zero on a nontrivial open localization or the unit ideal exactly when finiteness is already obtained.

## Consolidated proof and falsifier architecture

The main global cards fit one architecture without being merged:

1. COMP-PAIR supplies the canonical object (X,D,pi,j) and tries to realize a nonempty boundary.
2. MICRO-DEFECT probes that boundary from the target through sheaf-theoretic singular support.
3. DIFF-LATTICE-UNIT probes it from the source through the lifted tangent frame and units.
4. ITERATED-LOG-VOLUME probes it dynamically through repeated pullback.

An explicit completion pair, even one failing the final Keller condition, is therefore a common hostile control for the three proof detectors. Conversely, three failed detector formulations do not validate the completion search. This shared testbed is the useful five-report consensus; selecting one invariant by vote is not.

Two independent bypasses should remain logically separate:

- EXACT-COFRAME-K1 seeks a characteristic-zero Keller pair without first describing its infinity.
- FIXED-STRATUM seeks a bounded characteristic-p lift whose generic fibre would itself be a characteristic-zero pair.

The D and Tate-unit cards are lower-level structural discriminators. They should not be used as premises for the global architecture unless they first produce a polynomial map or a source-derived finite object.

## Final audit verdict

- Raw cards: 15.
- Strict duplicates: one pair, COMP-PAIR.
- Operational duplicates: two further pairs, MICRO-DEFECT and FIXED-STRATUM.
- Deduplicated operational candidates: 12.
- Genuinely new or materially new decision mechanisms: N1 through N9.
- Repairable refinements: N11 and the factorizer part of N12.
- Rename or invalid as written: N10; the untyped sidecar-span part of N12 is also inadmissible until repaired.
- Strongest thematic vote: 5 of 5 reports select the canonical global normalization or boundary, but they do not agree on a mechanism.
- Strongest mechanism-level convergences: MICRO-DEFECT, COMP-PAIR, and FIXED-STRATUM, two submissions each before model-correlation discount.
- Collection caveat: DEGRADED because Fable supplied no report; no missing ballot was inferred.

Frozen. This audit launches no work, promotes no claim, and edits no shared ledger.
