# Recent research progress

Dated mathematical developments across the campaign. Evidence tiers and scope remain
those recorded in [AUDIT.md](AUDIT.md) and the linked reports. Current open questions
are in [APPROACHES.md](APPROACHES.md). JC₂ remains unresolved.

## 2026-09-16

- **The running map's plane quotient has no rational-target repair.** The
  [exact quotient calculation](xmodel/running-torus-quotient-target-rigidity-swarmHQ-root-20260916T011000Z.md)
  gives Jacobian -2r^2 and image missing just(4/3,4/27). Cofinite image
  forces rational target functions with polynomial pullbacks to be polynomial,
  so they cannot remove the Jacobian zero. [Independent Sol review](xmodel/running-torus-quotient-review-swarmHQ-sol-20260916T011400Z.md)
  confirms this fixed-source exclusion: swarmHQ ROOT/Astra, MANUAL, PROMOTED.
  Arbitrary source substitutions, other quotients and JC2 remain outside scope.
- **The retained formal boundary recursion cannot algebraize.** Its fixed
  correction direction gives a [logarithmic primitive with nonzero residues](xmodel/formal-fixed-recursion-nonalgebraicity-swarmHQ-root-20260916T004300Z.md).
  The exact pair is therefore transcendental over the surface function field,
  including after any finite algebraic extension. [Independent Sol review](xmodel/formal-fixed-recursion-review-swarmHQ-sol-20260916T004600Z.md)
  confirms the recurrence identification and finite-cover obstruction.
  swarmHQ ROOT/Astra, MANUAL, PROMOTED at this fixed-algorithm scope.
  Finite jets remain valid; other formal or regular pairs and JC2 remain open.
- **Trace-pole growth returns to the integrality gap.** The
  [source-degree calculation](xmodel/source-trace-growth-swarmHQ-root-20260916T003100Z.md)
  bounds cancellation in a window of d conjugate power sums: maximal
  trace pole order is rho*n+O(1), with rho the largest normalized
  source-coordinate pole. Sublinear growth is therefore equivalent to
  local integrality. Keller derivatives supply a lower growth bound,
  not the needed upper bound. swarmHQ ROOT/Astra, MANUAL,
  PRODUCER-CHECKED, UNPROMOTED; no new integrality theorem, mixed-pole
  cutoff, degree exclusion or JC2 resolution. No growth/control farm follows.

## 2026-09-15

- **Affine target-plane sections of the fixed running triple are exhausted.**
  The [complete component classification](xmodel/affine-target-plane-sections-swarmHQ-root-20260915T235600Z.md)
  leaves only x=0 over R=0 as an A2 component; its induced map is an
  automorphism. Units and whole-fiber Euler characteristic exclude all
  other affine coefficients, levels and components, including repeated
  roots and reducible cases. swarmHQ ROOT/Astra, MANUAL,
  PRODUCER-CHECKED, UNPROMOTED; different-model review remains required
  before promotion. This classification does not classify nonlinear sections.
  Its plane-counterexample consequence is already covered more broadly by
  the September 13 [embedded-plane](xmodel/embedded-plane-transfer-root-20260913.md)
  and [finite-chain](xmodel/low-fiber-tower-transfer-root-20260913.md) transfer
  results, which allow nonlinear polynomial target maps under full
  factorization. The [right-factor theorem](xmodel/low-fiber-keller-factor-invariance-root-20260913.md)
  further preserves the initial parametrization's Keller factors at arbitrary
  generic degree. These retain their recorded accepted premises; arbitrary
  projections, other triples and JC2 remain outside those conclusions.
  No expanded section search follows. Scope pointer restored September 16;
  no new theorem or promotion.
- **Additive-symmetry descent is conditional; the first action fails.** A
  [manual derivation](xmodel/additive-quotient-descent-swarmHQ-root-20260915T232000Z.md)
  shows that a three-dimensional Keller map commuting with a primitive
  locally nilpotent derivation with full polynomial kernel C[u,v] induces
  a plane Keller map of the same geometric degree. The tested action on
  the literal running triple cannot descend: two points in one fiber give
  different pushed vectors. No compatible action or plane pair is produced.
  swarmHQ ROOT/Astra, same-model checked, MANUAL, PRODUCER-CHECKED,
  UNPROMOTED; no general symmetry exclusion, successor search, or JC2 closure.
- **One pole does not supply a rational intermediate field.** The
  [FULL2245 synthesis](xmodel/ideation-full2245-swarmHQ-synthesis-20260915T230100Z.md)
  distinguishes an already supplied rational donor field from the actual
  source fiber. The non-Keller pair P=y^2-x^5,Q=x has a unique generic-fiber
  pole but no required polynomial donor presentation. A literal two-pole
  donor separately fails the known principal-divisor obstruction. Astra
  and Sol cross-check these scopes; no new closing mechanism emerges.
  swarmHQ, MANUAL/DOCUMENTARY, PRODUCER-CHECKED, UNPROMOTED; no new
  accepted theorem, larger search, or JC2 resolution.
- **The polynomial donor filter now allows arbitrary rational base coefficients.**
  The [new local-to-global proof](xmodel/rational-coefficient-donor-swarmHQ-astra-20260915T214600Z.md)
  excludes q in C(p)[u], deg_u q=m>=2, after every finite-degree source
  substitution making p,q whole-plane polynomials with constant nonzero
  Jacobian. Either a branch curve has non-A1 normalization, or the normalized
  p-fibers are single multiple A1s and m annihilates the divisor class group.
  [Independent Sol review](xmodel/rational-coefficient-donor-review-swarmHQ-sol-20260915T215100Z.md)
  confirms both the dichotomy and the exclusion at their named-import scope.
  swarmHQ Astra/ROOT, PROMOTED / MANUAL, BOOK-relative at AUDIT's
  RATIONAL-COEFFICIENT-DONOR-1 scope. Polynomial dependence on u remains
  required; arbitrary Keller maps are not placed in this class. No JC2
  resolution, rational-in-u extension, or novelty claim.
- **An arbitrary-graph first-pair projection is excluded without a search.**
  The [degree identity](xmodel/tangent-graph-first-pair-swarmHQ-root-20260915T180230Z.md)
  rules out Keller pairs inside the first-two-output subalgebra of the
  literal tangent triple on every polynomial graph z=Z(x,y), uniformly in
  Z and the admissible donor degree. [Independent Sol review](xmodel/tangent-graph-first-pair-review-swarmHQ-sol-20260915T180600Z.md)
  confirms the self-contained argument. swarmHQ, PROMOTED / MANUAL at
  TANGENT-GRAPH-FIRST-PAIR-1 scope. Pairs involving the third output,
  other source orientations, rational changes, and JC2 remain outside it.
- **A cyclic boundary cover extends the coordinate-descent exclusion.** The
  [new proof](xmodel/tangent-cyclic-coordinate-swarmHQ-root-20260915T170800Z.md)
  excludes arbitrary target coordinates with source-coordinate pullbacks for
  the literal tangent-sweep stratum p=w^m A, q=w^(m+1) B, m>=2,
  A(0)!=0 and gcd(A,B)=1, with the full polynomiality hypotheses retained.
  A finite cyclic normalization cover and a two-sheet boundary count handle
  this additional unbounded stratum. [Independent Sol review](xmodel/tangent-cyclic-review-swarmHQ-sol-20260915T171200Z.md)
  confirms the argument relative to its named curve-theorem imports.
  swarmHQ, PROMOTED / MANUAL/BOOK-relative at AUDIT's
  TANGENT-CYCLIC-COORDINATE-DESCENT-1 scope. Common nonzero roots, other
  descent mechanisms and JC2 remain unresolved; no novelty claim.
- **Positive-genus ramification strengthens the Pinchuk donor exclusion.**
  The [original calculation](xmodel/pinchuk-donor-branch-swarmHQ-root-20260915T143100Z.md)
  found an elliptic branch obstruction for the displayed target pair. A
  [new valuation argument](xmodel/ramification-genus-birational-target-swarmHQ-root-20260915T152300Z.md)
  excludes every rational dominant target postcomposition inside that target
  field, after every finite-degree source substitution. Genuine ramification
  and positive source residue genus suffice; branch-image genus remains correct
  but is not needed by this argument. [Independent Sol review](xmodel/ramification-genus-review-swarmHQ-sol-20260915T152800Z.md)
  confirms the extension and that scope correction. swarmHQ, PROMOTED /
  MANUAL/BOOK-relative at AUDIT's POSITIVE-GENUS-RAMIFICATION-DONOR-1 scope.
  Other target fields, arbitrary Pinchuk-like maps, and all-rational ramification
  are not excluded. No novelty claim or JC2 resolution.
- **Two proposed shortcuts corrected; no new closing mechanism.** The
  [FULL1345 synthesis](xmodel/ideation-full1345-swarmHQ-synthesis-20260915T141000Z.md)
  excludes degeneration from a generic polynomial automorphism to a dominant
  nonautomorphic special fiber, by a direct inverse-coefficient pole argument.
  It also separates automatic formal idempotent lifting from the unproved
  polynomial descent. Astra and Sol cross-check both corrections; the formal
  algebraization and actual-source gaps remain. swarmHQ, MANUAL/DOCUMENTARY,
  PRODUCER-CHECKED, UNPROMOTED. All46 avenue dispositions unchanged; no
  novelty, new closing test, or JC2 resolution claimed.
- **Fixed-coefficient slices do not extract a new plane counterexample.** A
  [uniform marked-root calculation](xmodel/marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md)
  classifies these source slices for every n >= 4: a principal-open surface,
  sometimes disjoint from n-2 affine planes. The open component admits no
  dominant polynomial map from A2; the map on each plane is an affine
  automorphism. Arbitrary polynomial substitutions merely pass through the
  original JC2 problem. No claim covers other target slices or donors.
  [Independent Sol review](xmodel/marked-root-slices-review-swarmHQ-sol-20260915T125900Z.md)
  confirms the whole scheme and substitution caveat. swarmHQ, PROMOTED /
  MANUAL at AUDIT's MARKED-ROOT-FIXED-SLICES-1 scope; JC2 unresolved.
- **The translated-fiber question also has a curve formulation.** A
  [source-line Bertini corollary](xmodel/source-line-translates-swarmHQ-root-20260915T121300Z.md)
  gives geometrically integral generic fibers of F(q)-F(l(z)) for a
  general fixed complex source line l. At translation zero, connectedness
  still requires mapping degree one. No generic A1 fiber or finite set of
  bad translations is proved. [Independent Sol review](xmodel/source-line-review-swarmHQ-sol-20260915T122100Z.md)
  confirms the fixed-line quantifiers and exclusions. swarmHQ, PROMOTED /
  MANUAL/BOOK-relative at AUDIT's KELLER-SOURCE-LINE-1 scope; a routine
  dimensional reformulation, not a new closing mechanism or JC2 closure.
- **Tensor constants identify the unchanged polynomial-inverse condition.**
  A [plane constants calculation](xmodel/tensor-constants-swarmHQ-root-20260915T111600Z.md)
  uses reviewed generic translated-fiber irreducibility to show that the
  diagonal differential constants in C(p) tensor_C C[q] are precisely
  C[F(q)-F(p)]. The associated tensor map is surjective exactly when
  C[F1,F2]=C[x,y]; this does not weaken or prove the remaining inverse
  condition. No Chau no-line import or surjectivity of F is assumed.
  [Independent Sol review](xmodel/tensor-constants-review-swarmHQ-sol-20260915T112400Z.md)
  confirms the exact calculation and exclusions. swarmHQ, PROMOTED /
  MANUAL/BOOK-relative at AUDIT's KELLER-TENSOR-CONSTANTS-1 scope.
  Novelty unknown; JC2 unresolved.
- **Translated collision fibers have only finitely many possible exceptions.**
  A [branch-disjointness argument](xmodel/disjoint-branch-translates-swarmHQ-root-20260915T093700Z.md)
  gives irreducibility of \(F(p)-F(q)=t\) when the Galois branch divisor
  and its translate share no component. Purity and Chau's no-line theorem
  leave finitely many possible exceptional translations. Zero remains a
  possible exception; connectedness there and JC₂ are unresolved.
  The [independent Sol review](xmodel/disjoint-branch-review-swarmHQ-sol-20260915T094600Z.md)
  confirms the core criterion at MANUAL/BOOK-relative scope. The finite
  count is confirmed conditional on Chau's theorem, whose primary proof
  that reviewer did not audit. No novelty or uniform branch-count claim;
  see the exact accepted scope in AUDIT.
- **Rational Weyl automorphisms do not yield proper polynomial endomorphisms.**
  A [birational construction filter](xmodel/birational-weyl-dressing-swarmHQ-root-20260915T082700Z.md)
  shows that a first-Weyl endomorphism inducing a division-ring automorphism
  has a polynomial inverse of no larger Bernstein degree. The argument uses
  named positive-characteristic imports and a uniform descent bound.
  swarmHQ, MANUAL/PRODUCER-CHECKED, UNPROMOTED; no novelty claim, arbitrary
  Weyl/Keller classification, or JC₂ resolution follows.
- **New source criteria retain missing Keller hypotheses.** The
  [primary-source applicability report](xmodel/primary-source-gates-swarmHQ-root-20260915T075600Z.md)
  distinguishes finite projective dimension over the canonical graph ring from
  perfectness over its polynomial ambient ring; conductor lifting and ideal
  integral-closure bounds likewise do not supply source integrality. No new
  JC₂ closing test results. swarmHQ, DOCUMENTARY/MANUAL, PRODUCER-CHECKED,
  UNPROMOTED; source proofs were not fully audited.
- **Two donor constructions excluded at their stated scopes.** swarmHQ's
  [Laurent-polynomial donor filter](xmodel/laurent-polynomial-donor-swarmHQ-root-20260915.md)
  and [volume-neutral torus quotient filter](xmodel/volume-neutral-torus-quotient-swarmHQ-root-20260915.md)
  are PROMOTED/MANUAL after independent Fable review. These are all-degree filters
  for the named constructions, not reductions of arbitrary Keller sources to them.
- **Smooth degeneration does not supply global normality.** The
  [canonical-graph calculation](avenues/notes/smooth-graph-degeneration-20260915.md)
  retains a smooth central fiber, t-saturation, and finite total normalization.
  A non-Keller control has singularities escaping to infinity. The actual-source
  global normality/integrality gap remains. swarmHQ, MANUAL/PRODUCER-CHECKED,
  UNPROMOTED; no JC₂ proof advance.
- **An abstract strengthening of the Bass tests is insufficient.** A
  [cofinite-center cusp module](avenues/notes/cofinite-center-euler-20260915.md)
  is nonzero while passing the stated tests in every polynomial frame centered
  away from the cusp point. It is not an actual Keller source quotient. swarmHQ,
  MANUAL/PRODUCER-CHECKED, UNPROMOTED; source-specific selection remains open.
- **Finite critical values do not control behavior at infinity.** An
  [explicit polynomial control](avenues/notes/finite-critical-values-20260915.md)
  has two ordinary-node critical points at the same value, yet generic genus one
  and a further atypical value at infinity. The pair is not Keller. swarmHQ,
  MANUAL/PRODUCER-CHECKED, UNPROMOTED; this stops the proposed finite-data inference.

## Earlier work

The [complete preceding digest](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/PROGRESS.md) retains the dated developments
through the transition, including their subsequent qualifications. Its
[local archive](history/PROGRESS-through-20260915.md) preserves the original bytes.
The [historical research journal](notes.md) retains unique derivations and controls.
Operational entries in those historical records are not current swarm instructions.

## Updating this digest

Maintain one concise entry per date: what changed mathematically, exact scope and
evidence/lifecycle, producer credit, and links. Useful failed approaches belong here.
Keep machine state, routine queue polling, budgets, and internal deadlines in your
swarm workspace. Preserve corrections and link superseded claims instead of erasing them.
