# Recent research progress

Dated mathematical developments across the campaign. Evidence tiers and scope remain
those recorded in [AUDIT.md](AUDIT.md) and the linked reports. Current open questions
are in [APPROACHES.md](APPROACHES.md). JC₂ remains unresolved.

## 2026-10-26

- **An infinitely singular value-group constraint is now reviewed.** The [conditional argument](xmodel/infinitely-singular-value-group-swarmHQ-root-astra-sol56-20261026.md) gives lambda-divisibility, eigen ramification/residue indices one, and ramification prime to lambda for all other existing extensions. The local Keller form also fixes integral kappa and mu=1/lambda.
  PROMOTED/MANUAL/CONDITIONAL after independent Sol review, with essential-prefix classification explicitly imported and unaudited. Counting or excluding the other extensions remains the global gap; JC2 is unresolved.

- **Smooth image branches carry no local slack.** The [reviewed argument](xmodel/smooth-branch-slack-irreducible-image-swarmHQ-root-astra-sol56-20261026.md) localizes all finite-normalization excess to nonimmersed branches. If the nonproper-value set is irreducible, the fibre identity and an external embedded-A1 exclusion force at least one nonimmersed branch.
  PROMOTED/MANUAL/CONDITIONAL after independent review; the external theorem statement was checked, its proof was not audited. Reducible image unions, nonimmersed branches and JC2 remain open; no novelty claim.

- **The proposed strict completion test is now ruled out.** The [cusp-contact analysis](xmodel/cusp-contact-completion-limit-swarmHQ-root-astra-sol56-20261026.md) proves a_W=1+R_q.C>=1 and0<I_Y<1, so its threshold cannot satisfy M_C<sqrt(I_Y).
  This reviewed conditional result retires that particular test and preserves the earlier valid volume inequalities. Other volume comparisons and JC2 remain unresolved; the optional static n=3 diagnostic is not adopted.

- **A cusp-volume comparison is now reviewed.** The [reduction](xmodel/cusp-volume-nef-completion-swarmHQ-root-astra-sol56-20261026.md) proves finite degree growth e V_Y<=V_W and a finite-boundary upper bound 0<I_Y<=I_W<=M_C^2 in the adopted divisorial package.
  The remaining sufficient step is the strict coefficient estimate M_C<sqrt(I_Y); it is unproved. PROMOTED/MANUAL/CONDITIONAL after independent Sol review, with all source singular blocks retained. The infinitely singular branch and JC2 remain unresolved.

- **Missing values are confined to individual multibranch points.** The [pointwise fibre identity](xmodel/pointwise-fibre-count-swarmHQ-root-sol56-20261026.md) shows that a target point with only unibranch individual nonproper-value components has a source preimage; crossings between distinct components alone cannot cause omission.
  This is a reviewed corollary of the sheet budget, PROMOTED/MANUAL (swarmHQ coordinator and independent Sol 5.6 review). The general multibranch case, properness and JC2 remain unresolved; no novelty claim.

- **The sheet bound now applies to every plane Keller map.** The [extension](xmodel/all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) gives sum_i r_i delta_i<=e-1 and an exact nonnegative slack identity for every complex Keller finite normalization.
  A boundary-tree argument supplies disjoint omitted curves with finite-bijective A1 normalizations; neither smoothness nor rational singularities is assumed.
  swarmHQ ROOT/Astra co-research, PROMOTED/MANUAL after independent configured gpt-5.6-sol review. The logarithmic thickening estimate and infinitely singular branch remain open; JC2 is unresolved.

## 2026-10-25

- **A global omitted-sheet bound is now reviewed.** The [proof](xmodel/global-sheet-budget-swarmHQ-root-sol56-20261025T234000Z.md) gives sum_i r_i delta_i<=e-1 for the actual divisorial finite normalization, simultaneously across all omitted affine lines and their possibly different images.
  The proof uses finite-flat local fibre lengths and whole-source Euler integration; no affine sheet over every target point is assumed.
  PROMOTED/MANUAL/CONDITIONAL after independent Sol review and a separate custody clarification. The logarithmic thickening inequality and infinitely singular branch remain open; JC2 is unresolved.

- **The actual divisorial log defect is now explicit.** The [reviewed reductions](xmodel/logarithmic-defect-swarmHQ-root-astra-20261025T221000Z.md) establish full-boundary logarithmic acyclicity, a length-one top-form defect and the one-sided bound Delta.c1(V)<=e-1.
  The differential quotient retains its exceptional thickening terms; the estimate needed to compare them with missing sheets remains unproved.
  Producer swarmHQ (gpt-6-astra), PROMOTED/MANUAL/CONDITIONAL after gpt-5.6-sol review with its [mandatory erratum](box/logarithmic-defect-swarmHQ-20261025T221000Z/logbridge2148-sol56-erratum.md). The sheet budget is supplied by the newer entry above; the infinitely singular branch remains unresolved.

- **Exceptional centres lie at two fixed boundary points, conditionally.** The [new constraints](xmodel/boundary-contact-constraints-swarmHQ-root-astra-20261025.md)
  force every exceptional contact to be non-Cartier and locate its centre at the cusp or one distinguished smooth point.
  At the smooth point, whole-source unramified sheets leave noncommuting branch inertia as the precise local obstruction.
  PROMOTED/MANUAL/CONDITIONAL after [independent review](xmodel/boundary-contact-review-swarmHQ-sol56-20261025.md); cusp escape and uniform stabilization remain open. JC2 is unresolved.

- **All full lifts of one explicit cusp filtration are conditionally excluded.** A [marked-curve argument](xmodel/marked-curve-lift-obstruction-swarmHQ-root-astra-20261025T151400Z.md) rules out every e>1 full homogeneous lift of
  C[X,Y,W,T]/(X²-Y⁵-WT⁷), weights(5,2,3,1), with an injective Poisson central map and T mapped to T^e.
  The proof uses the unique polynomial curve at the smooth boundary and local covering monodromy, uniformly in e.
  swarmHQ ROOT/Astra, PROMOTED/MANUAL/CONDITIONAL after [independent review](xmodel/marked-curve-lift-delta-review-swarmHQ-sol56-20261025T151400Z.md);
  the adopted lambda1>=N and divisorial attachment/projectivity inputs remain explicit assumptions. Other targets and the infinitely singular branch remain open; JC2 is unresolved.

- **The static compactification conditions do not force index one.** An [explicit whole-plane compactification](xmodel/global-static-index-three-swarmHQ-root-astra-20261025.md)
  is projective, has rational singularities and an ordinary cuspidal boundary, and satisfies the genuine canonical-ideal identity,
  but its canonical/Cartier index is three. Its boundary has B²=1/3 and 3B is ample.
  PROMOTED/MANUAL after [final artifact review](xmodel/global-static-index-three-delta-review-swarmHQ-sol56-20261025.md).
  This rules out the static Gorenstein shortcut. It supplies no actual finite h/proper k pair, iterate or Keller map, and does not settle JC2.

- **The divisorial compact target is projective.** A [direct proof](xmodel/divisorial-projectivity-swarmHQ-root-astra-20261025.md)
  constructs a line bundle using topology and the exponential sequence, then lifts sections across the
  contracted boundary using Kodaira vanishing on the smooth projective resolution. It also gives
  Picard/divisor-class arithmetic and projectivity of the finite iterate surfaces, with
  C_j²=1/(nN^j) and nN^j C_j Cartier ample. PROMOTED/MANUAL, conditional, after
  [final artifact review](xmodel/divisorial-projectivity-delta-review-swarmHQ-sol56-20261025.md). No uniform degree/index bound, target-map descent,
  properness of F, or treatment of the infinitely singular branch follows; JC2 remains unresolved.

## 2026-10-24

- **The compact package now attaches to the actual divisorial branch.** The
  [corollary](xmodel/divisorial-keller-compactification-swarmHQ-root-astra-20261024.md) checks the compactification and finite-factor hypotheses for every iterate,
  under the adopted dynamical inputs and a divisorial eigenvaluation. Positive skewness follows automatically;
  the dynamical degree equals the generic degree. The source projection is proper, while properness of the
  original polynomial map, omitted-boundary exclusion and target-map descent remain open.
  The infinitely singular branch is outside the result. PROMOTED/MANUAL, conditional, after
  [qualified final review](xmodel/divisorial-keller-compactification-delta-review-swarmHQ-sol56-pub2346-20261024.md); no JC2 proof or counterexample.

- **A conditional compact finite-factor theorem closes two intermediate gaps.**
  The [proof](xmodel/finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md)
  shows that the actual finite Stein factor has rational singularities, including
  at infinity, and that its reduced boundary maps isomorphically to the target
  boundary; both boundary curves have arithmetic genus one. This requires the
  stated primitive compactification, genuine canonical ideal, projective rational
  source and unique source-valuation hypotheses. swarmHQ coordinator;
  PROMOTED/MANUAL, conditional, after
  [Sol5.6-assigned review of the frozen public artifact](xmodel/finite-stein-factor-boundary-delta-review-swarmHQ-sol56-20261024T203139Z.md).
  The review was not fully blind; its qualifications are retained in the report
  and audit. Omitted boundary, descent and attachment to all Keller maps remain
  open. No properness or JC2 conclusion follows.

- **The same conditional boundary is intrinsically cuspidal; a further local bound isolates the Cartier-index gap.**
  The [follow-up proofs](xmodel/cuspidal-boundary-index-swarmHQ-root-astra-20261024T213422Z.md) give one ordinary cusp on each boundary
  curve and construct a proper birational source projection `k:W->Y`.
  If the target surface is additionally smooth at its cusp, ramification satisfies
  `e<=5m`, where `m` is the source boundary's local Cartier index. The construction
  of `k` does not prove descent, and the index is not uniformly bounded.
  A local example shows why rationality alone cannot supply that bound; it has
  no required finite Keller map. Coordinator/Astra; PROMOTED/MANUAL, conditional,
  after the [qualified Sol5.6-assigned final review](xmodel/cuspidal-boundary-index-delta-review-swarmHQ-sol56-pub2127-20261024.md).
  The compact ambient-location question is resolved below; actual global-map
  control and all-Keller attachment remain open.

- **Singular ambient cusp and a stronger local countertest.** Under the explicit
  compact canonical-ideal premises, the target is singular exactly at its
  intrinsic cusp. This closes the ambient-location question and makes the
  extra smooth-cusp branch empty in that compact setting.
  Separately, finite local maps of every even degree `e` have rational source,
  cusp isomorphisms, equal forms, compatible rational iterates, and exact
  Cartier index `m=e/2`. Thus these local data alone cannot bound the index.
  The construction does not supply a globally proper source projection or a
  whole-plane polynomial Keller map. Global attachment and descent remain open.
  [Proofs and exact scope](xmodel/singular-ambient-cusp-local-index-swarmHQ-root-astra-20261024T223151Z.md);
  [qualified hostile review](xmodel/singular-ambient-cusp-local-index-delta-review-swarmHQ-sol56-pub2227-corrected-20261024.md).
  PROMOTED/MANUAL; no JC2 proof or counterexample.

## 2026-10-22

- **A fewnomial face condition is unavailable in generic real-affine Keller frames retaining a positive zero.**
  The [frozen proof](xmodel/generic-real-frame-obstruction-swarmHQ-root-20261022T121815Z.md)
  uses a self-contained vertex homotopy and the rank-one complex leading image.
  For degree D>=2, four nonzero pure top terms and a nonzero constant, full face
  condition(H) would force degree zero, contradicting same-sign Keller zeros.
  [Independent Sol5.6-assigned hostile review](xmodel/generic-real-frame-hostile-review-swarmHQ-sol56-20261022T124020Z.md)
  confirms the exact claim: PROMOTED/MANUAL; the frozen producer banner is historical.
  Exceptional frames, zero constant and weaker face conditions remain outside scope.
  This includes nonlinear automorphisms and excludes no Keller map; JC2 is unchanged.

## 2026-10-21

- **Complete-image obstruction now allows arbitrary rational postmaps, under an added hypothesis.**
  The [faithful-flat descent proof](xmodel/complete-image-arbitrary-postcomposition-swarmHQ-root-sol56-20261021T234829Z.md)
  excludes every rational postpair yielding a regular quasi-finite composition
  when every point of a complete target curve has an etale preimage on the
  fixed source curve. It applies to the earlier nodal setup only conditionally.
  ROOT producer, Astra hostile and Sol5.6-assigned FIRST; PROMOTED/MANUAL.
  No donor is constructed, and the actual finite-normalization gap is unchanged.

- **A complete target curve can obstruct polynomial chart landing.** The
  [corollary and explicit four-blowup chart](xmodel/complete-image-chart-review-swarmHQ-root-sol56-20261021T112534Z.md)
  use the accepted zero-free-form extension to rule out every birational
  Darboux target frame for a fixed source chart whose image contains a complete
  curve in the target's regular-area locus. An affine line retaining one of
  two cycle nodes gives this obstruction conditionally for a nodal quotient.
  ROOT producer, Astra hostile and Sol5.6-assigned FIRST; PROMOTED/MANUAL.
  No isogeny is constructed; other source charts and the normalization gap remain open.

## 2026-10-20

- **Three double-fiber values also preserve primitivity.** The
  [proof and independent review](xmodel/three-double-fiber-review-swarmHQ-sol56-root-20261020T172346Z.md)
  add the case of at most three nonreduced affine fiber divisors, with every
  component multiplicity at most two, for target-primitive a/b with coprime,
  algebraically independent a,b. Basepoints and the pole fiber are included.
  Ramification counting leaves only quadratic or quartic intermediate maps;
  both force a square that descends to the target, contradicting primitivity.
  TWO1323 separately allows arbitrary multiplicities at two bad values.
  No suitable boundary pencil, general degree bound or B=R is supplied.
  ROOT producer, independent Sol5.6-assigned FIRST; PROMOTED/MANUAL,
  standard imports, external novelty unknown.
- **Two bad fibers suffice with independent numerator and denominator.** The
  [theorem and independent review](xmodel/two-bad-fiber-review-swarmHQ-astra-root-20261020T134316Z.md)
  extend the binomial result to any target-primitive a/b with coprime,
  algebraically independent a,b and at most two nonreduced affine fiber
  divisors (including the pole fiber; empty divisors count as reduced).
  Independence excludes every divisor-empty intermediate fiber; the
  resulting two-branch-value cover is cyclic, and powers descend by
  unramified prime detection. Affine basepoints are allowed. This does not
  supply a suitable pencil from a normalization boundary or prove B=R.
  ROOT producer, independent Astra-assigned FIRST; PROMOTED/MANUAL,
  standard imports, external novelty unknown.
- **Coprime binomial pencils remain primitive.** The
  [proof and independent review](xmodel/binomial-pencil-primitivity-review-swarmHQ-sol56-root-20261020T115104Z.md)
  show that C(P^m/Q^n) is algebraically closed in C(x,y) for a polynomial
  Keller pair and coprime positive m,n. Primitive-polynomial multiplicities
  and reduced-fraction extraction handle two nonreduced target fibers,
  beyond the retained ONEBAD scope. This obstructs fixed-target donor
  repair by dominant rational source substitutions, but supplies no
  generic-genus bound, arbitrary-target exclusion or B=R conclusion.
  ROOT producer, independent Sol5.6-assigned FIRST; PROMOTED/MANUAL,
  standard imports, external novelty unknown.
- **Pole-free zero support must be simple normal crossing.** The
  [proof and independent review](xmodel/pole-free-zero-snc-review-swarmHQ-sol56-root-20261020T105819Z.md)
  show that a rational two-form with Darboux coordinates generating the
  surface function field has SNC reduced zero support wherever the form is
  regular. This excludes cusps, self-nodes, tangencies and triple points there.
  The proof extends the retained zero-free-model descent argument.
  Conditional finite-cover use requires smooth source/target points and a
  target area form regular and nonzero at the image; finite source-field
  enlargement is not covered. ROOT producer, independent Sol5.6-assigned
  FIRST; PROMOTED/MANUAL with standard imports, novelty unknown.
  No forbidden configuration in an actual Keller normalization is forced,
  so the global B=R gap remains.

## 2026-10-19

- **Ramification crossings have a coprimality constraint.** The
  [proof and independent review](xmodel/snc-order-coprimality-review-swarmHQ-sol56-root-20261019T112438Z.md)
  show that at an SNC crossing of a rational constant-area form, the two
  divisor orders plus one are coprime. On the actual finite Keller
  normalization this forces coprime ramification indices at smooth crossings
  of exactly two ramification components. No forbidden crossing is forced
  to exist; singular/non-SNC points and B=R remain gaps. ROOT producer,
  independent Sol5.6-assigned FIRST; PROMOTED/MANUAL, novelty unknown.
- **A multibranch zero curve obstructs rational constant-area coordinates.**
  The [proof and independent review](xmodel/positive-zero-cycle-review-swarmHQ-sol56-root-20261019T101735Z.md)
  show that an irreducible positive zero curve, multibranch at a pole-free point, forces a
  cycle incompatible with the exceptional fibers of a birational plane model.
  The finite-cover consequence survives constant-Jacobian birational target changes for
  a specified area form, with birational source coordinates only. Its A5
  application still requires a suitable global target area form. ROOT producer,
  independent Sol5.6-assigned FIRST; PROMOTED/MANUAL with standard imports,
  novelty unknown. No finite source enlargement or general B=R conclusion.

## 2026-10-18

- **One nonlinear degree-five cover cannot supply Keller charts.** The
  [pentagon proof and independent review](xmodel/a5-pentagon-chart-review-swarmHQ-sol56-root-20261018T222155Z.md)
  exclude A2-open etale charts for S/A4->S/A5, where S is the degree-five del
  Pezzo surface. One global ramification curve has two tangent branches at a
  smooth source point; it cannot be hidden in an affine-plane boundary.
  ROOT producer, independent Sol5.6-assigned FIRST; PROMOTED/MANUAL with stated
  imports, novelty unknown. This rules out only this fixed cover, not arbitrary
  birational models, other constructions or a general Keller map.
- **A one-bad-fiber criterion permits affine-basepoint pencils.** The
  [proof and independent review](xmodel/one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md)
  show that a target-primitive rational pencil remains primitive under any Keller
  pullback if at most one affine fiber divisor, including the pole fiber, is
  nonreduced. Componentwise reducedness avoids the earlier whole-fiber-gcd gap.
  The basepoint pencil (v^2-u^3)/u^2 supplies an explicit client, excluding finite
  rational source repairs of H_R=(t^2-R(s),t(t^2-R(s))), deg R>1, at fixed target
  functions. ROOT producer, independent Sol5.6-assigned FIRST; PROMOTED/MANUAL
  with standard imports, novelty unknown. General pencil selection, arbitrary
  target changes and JC2 remain open.
- **Basepoint-free rational target pencils stay primitive under Keller pullback.**
  The [proof and independent review](xmodel/basepoint-free-pencil-review-swarmHQ-sol56-root-20261018T170650Z.md)
  show that C(f) is algebraically closed in the source field when f is a morphism
  from the target plane to P1 with geometrically integral rational generic fibre.
  This excludes finite rational source repairs of D_R=(R(s),t/R'(s)), deg R>1,
  even after nonconstant-J birational target changes, PROVIDED the transformed
  old-coordinate pencil has no affine basepoints. ROOT/Astra producer, independent
  Sol5.6-assigned FIRST; PROMOTED/MANUAL with named imports, external novelty unknown.
  General affine-basepoint pencils and the missing-boundary problem remain open;
  the separate reduced-fiber criterion above addresses only its stated subclass.

## 2026-10-17

- **The cubic-cusp donor is excluded under all constant-J birational target changes.**
  The [proof and independent review](xmodel/cubic-cusp-all-target-review-swarmHQ-sol56-root-20261017T021212Z.md)
  rule out every such target change followed by any finite rational source
  embedding for t=X/Y, p=Y-3t^2, q=-tY+2t^3. A key
  [reviewed lemma](xmodel/cusp-avoidance-review-swarmHQ-sol56-root-20261017T015830Z.md)
  says every closed rational affine-plane curve meets the cusp, with no puncture
  bound. Pole geometry and the behavior at infinity then force a forbidden
  nonproperness component. Other donors, nonconstant-J target changes, and a
  general Keller normal form remain open. Producer swarmHQ ROOT/Astra;
  independent Sol5.6 FIRST; PROMOTED / MANUAL with accepted classical imports,
  external novelty unknown. This does not resolve JC2.

## 2026-10-16

- **An all-degree rational construction family is excluded in fixed targets.**
  The [affine-radial proof and independent review](xmodel/affine-radial-review-integration-swarmHQ-sol56-root-20261016T220000Z.md)
  rule out finite rational source repairs of genuinely rational constant-J pairs
  affine in the radial variable. The proof combines branch-curve normalization,
  a monic parameter equation and integrality of both original source coordinates.
  Polynomial members are affine automorphisms. This is a construction filter,
  not a general Keller normal form or JC2 proof; arbitrary birational target
  repair remains outside scope. PROMOTED / MANUAL with accepted classical imports.

- **Nonsingularity does not force rational fibres in the carrier ring.** A
  [fixed polynomial and independent review](xmodel/carrier-genus2-integration-swarmHQ-root-20261016T133911Z.md)
  give a whole-plane submersion in the marked carrier ring with geometric generic
  genus two. Its specific differential has no rational primitive, so this scalar
  has no rational constant-Jacobian mate. This closes the scalar-rationality
  shortcut, not the arbitrary-pair question or JC2. Producer swarmHQ ROOT;
  independent Sol5.6 review; PROVED / PROMOTED, external novelty UNKNOWN.

- **A simple repair of the finite-map control is excluded in every degree.**
  The [pencil proof and independent review](xmodel/carrier-pencil-review-integration-swarmHQ-sol56-root-20261016T063000Z.md)
  rule out `(p^2+alpha*H,U+beta*H)` for arbitrary H in the marked carrier ring.
  Mixed pencil members also have no rational Jacobian mate. This closes only
  constant-direction perturbations, not all deformations or carrier pairs.
  Producer swarmHQ ROOT; independent Sol5.6 review. PROVED / PROMOTED at this
  scope; external novelty UNKNOWN.

- **Carrier weight constraint survives review; selected-row test fails.** For an
  arbitrary nonzero constant-Jacobian pair in the explicit carrier ring, each polynomial
  must have both signs of weight, with common-power highest and lowest components.
  The [corrected proof and test refutation](xmodel/carrier-extreme-weights-v2-swarmHQ-root-20261016T044600Z.md)
  also give dependent zero-Jacobian pairs passing the proposed extreme-row test.
  This is a necessary condition, not a carrier exclusion or a new closing test.
  Producer swarmHQ Fable5.1; independent review Astra. PROVED / PROMOTED at this
  scope; external novelty not asserted.

- **Finiteness does not repair the moment shortcut.** A fixed finite degree-six
  map on the marked two-chart surface has every polynomial two-form moment
  zero but a nonconstant Jacobian. The [proof and independent review](xmodel/finite-moment-review-integration-swarmHQ-sol56-root-20261016T010647Z.md)
  rule out this sufficiency inference only; they do not solve or exclude the
  complete F10 equations or produce a Keller counterexample. MANUAL / PROMOTED;
  external novelty UNKNOWN.

## 2026-10-15

- **Complete F10 inputs: full finite-normalization carrier identified.**
  A [proof and independent review](xmodel/f10-full-normalization-integration-swarmHQ-root-20261015T223201Z.md)
  identify the known two-chart surface with the full normalization over the
  actual target, and its source complement with one smooth affine line of
  generic ramification index2. MANUAL / PROMOTED, conditional on every complete
  compact-source equation and guard. This removes a carrier-identification gap,
  not the missing full-pair exclusion; no source point, F10 exclusion, source
  surjectivity or general JC2 conclusion is obtained. Producer swarmHQ ROOT;
  independent reviewer Sol5.6. External novelty UNKNOWN.

- **Constant-gamma tangent constructions: all polynomial outputs excluded.**
  A [proof and independent review](xmodel/constant-gamma-integration-swarmHQ-root-20261015T211500Z.md)
  exclude every polynomial plane projection of the specified whole-plane triple,
  for all eligible seeds of degree at least two and constant nonzero gamma.
  Plane-curve genus forces a collision; unequal source residues obstruct a Keller
  pair. MANUAL / PROMOTED at this exact scope. This extends the earlier linear-output
  exclusion within this class, not to nonconstant gamma or arbitrary Keller maps.
  External novelty UNKNOWN; JC2 and the finite-normalization gap remain unresolved.

## 2026-10-06

- **Nonproper divisor pushforward does not descend to classes.** A
  [self-contained correction](xmodel/nonproper-class-pushforward-correction-swarmHQ-root-20261006T205529Z.md)
  locates the omitted-boundary term that invalidates a proposed class-group
  push-pull argument on the finite normalization. The finite norm identity and
  factorized zero pullback remain valid. ROOT/Astra supplied the argument with
  an Astra hostile check; the new exposition is MANUAL/PRODUCER-CHECKED and
  UNPROMOTED, novelty UNKNOWN. This corrects the operation, not JC2, and admits
  no new experiment or theorem promotion.

## 2026-10-05

- **A scoped branch-geometry criterion.** A
  [short generic-fiber proof](xmodel/normalization-branch-coordinate-criterion-swarmHQ-root-20261005T172000Z.md)
  shows that a plane Keller map is invertible if the branch curve of its finite
  normalization lies in finitely many fibers of one target polynomial coordinate.
  Opus supplied the criterion; ROOT/Astra shortened the proof, with an Astra
  hostile scope check. MANUAL; exposition PRODUCER-CHECKED and UNPROMOTED;
  novelty UNKNOWN. No argument puts arbitrary branch curves in that configuration,
  so this does not resolve JC2 or authorize another branch-family search.

- **A real-Jacobian lower-bound converse fails.** The
  [explicit polynomial and proof](xmodel/positive-jacobian-bound-converse-swarmHQ-root-20261005T054620Z.md)
  give a positive Jacobian with infimum zero whose prescribed transform has
  infimum one, contradicting the converse in Peretz, arXiv:2610.02961v1,
  Theorem 6.1(2), at its stated real-polynomial scope. ROOT/Astra produced the
  calculation; Opus and Fable independently checked it, and an Astra hostile
  review checked the original source scope. MANUAL; new exposition UNPROMOTED;
  novelty UNKNOWN. The forward implication survives. This is neither a
  constant-Jacobian example nor a JC2 counterexample or whole-paper refutation.

## 2026-09-30

- **The next marked-root coordinate step has a uniform obstruction.** A
  [manual, unpromoted integration](xmodel/lower-block-coordinate-obstructions-swarmHQ-root-20260930T014100Z.md)
  analyzes the LOWER coefficient block for every n>=4 and every parameter.
  All next-coefficient fibers fail to be affine planes; constant top-coefficient
  fibers admit no two-dimensional polynomial-plane image; and arbitrary
  polynomial shears of the next coefficient by the top coefficient still
  cannot be coordinates. A separate plane restriction is an isomorphism,
  providing a positive control. Producer Astra/Opus with ROOT integration
  and hostile cross-checking; MANUAL, UNPROMOTED, novelty UNKNOWN. These
  specified reductions are excluded without a parameter scan. Arbitrary
  sections and the global JC2 problem remain open.

## 2026-09-24

- **A fixed-coordinate analytic shortcut is excluded.** The
  [reviewed leading-Hessian argument](xmodel/leading-hessian-integration-swarmHQ-root-20260924T123725Z.md)
  shows that a polynomial Keller weight admits bounded-distance isotropic
  complex-Hessian regularization iff its map is affine. This blocks direct
  use of the inspected weighted-Fock class for nonlinear maps, including
  nonlinear automorphisms. Producer ROOT/Astra; independent Fable review;
  MANUAL, UNPROMOTED, novelty UNKNOWN. No actual Keller map is ruled out,
  and the positive holomorphic-density premise remains open.

- **Collision-component duals and a construction-filter correction.** A
  [manual, unpromoted integration](xmodel/collision-endomorphism-scope-review-swarmHQ-root-20260924T112000Z.md)
  justifies End_A(R)=R for a polynomial Keller source at its named classical-
  import scope, without proving A=R or collision emptiness. Hostile review
  also rejects an inference from singular image points to nonreduced fibers;
  an exact non-Keller control exposes the gap. No new closing test or
  polynomial counterexample is supplied. Producer Fable; ROOT/Astra review
  and integration; novelty UNKNOWN.

## 2026-09-23

- **Two functional-route scope corrections.** A [manual, unpromoted review](xmodel/dual-locality-scope-review-swarmHQ-root-20260923T233500Z.md)
  exhibits an actual Keller automorphism for which a proposed intermediate
  ring fails to contain the target ring. It also separates a local
  punctured-branch extension from the diagonal unit extension: retained
  inverse sheets give analytic local retractions, not a global polynomial-valued
  functional. These corrections reject an overbroad exclusion of boundary
  methods; they provide no new closing mechanism or JC2 solution.

- **One nonzero target-linear functional suffices for Keller invertibility.**
  The [reviewed nonzero-dual criterion](xmodel/nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md)
  proves Hom_A(R,A)!=0 iff F is an automorphism, for R=C[w1,w2] and
  A=C[F1,F2] from any complex polynomial Keller map. The functional need
  not be normalized, multiplicative or differentially compatible. Independent
  Fable FIRST checks the trace-ideal, differential-simplicity and integrality
  proof: swarmHQ ROOT/Codex, PROMOTED/MANUAL with the classical finite-etale
  endpoint; novelty UNKNOWN. Existence of the functional remains unproved;
  no derived splitting or JC2 solution is supplied.
  A subsequent [reviewed elementary proof](xmodel/generic-dual-integration-swarmHQ-root-20260923T163500Z.md)
  shows nonzero dual iff module finiteness for any generically finite domain
  algebra over a Noetherian domain. Multiplication embeds the source in A^n,
  removing trace, differential simplicity and Newton identities from this
  step. This simplifies the same criterion; it does not advance its existence premise.

## 2026-09-21

- **Polynomial Weyl commutator coordinates are rationally indecomposable.**
  The [reviewed centralizer argument](xmodel/weyl-centralizer-integration-swarmHQ-root-20260921T114000Z.md)
  proves C_D(P)=C(P) for polynomial [Q,P]=1 in the first Weyl algebra
  over C. Consequently P=R(T), T in D, forces rational-map degree1.
  This excludes simultaneous polynomial landing of R(x), (1/R'(x))*d
  under any division-ring embedding when deg(R)>1. Independent Fable
  FIRST confirms the denominator-module proof and exact classical imports:
  swarmHQ ROOT/Codex, PROMOTED/MANUAL; novelty UNKNOWN. A review shift-sign
  typo is corrected in integration. Mobius R can land; the
  [earlier inner/polynomial-word filter](xmodel/rational-weyl-inner-integration-swarmHQ-root-20260921T092500Z.md)
  forces affine R only in its smaller transformation class. Arbitrary
  rational pairs remain outside scope; no counterexample or JC2 solution.
- **An actual quotient reduces invertibility to one scheme neighborhood.**
  The [reviewed additive-quotient construction](xmodel/keller-additive-quotient-integration-swarmHQ-root-20260921T014800Z.md)
  attaches a free Ga2-action on A5 to every polynomial Keller F. Its
  algebraic-space quotient has special fiber A2, and F is invertible
  exactly when one special-fiber point has a Zariski-open scheme
  neighborhood. Independent Fable FIRST confirms the exact reduction,
  with source-read limits and reviewer wording corrected in integration:
  swarmHQ ROOT/Codex, PROMOTED/MANUAL with named imports. An etale chart
  is not the required neighborhood; no positive premise or JC2 proof
  is supplied.
- **Exact rational area preservation does not force an invariant foliation.**
  The [reviewed extension of the fixed countertest](xmodel/rational-area-no-foliation-integration-swarmHQ-root-20260921T002700Z.md)
  proves exact dynamical degree4 and no algebraic foliation preserved by
  any positive iterate of F=(y/(2x),y^4/(16x^4)-x^2). Independent Fable
  FIRST confirms the algebraic-stability and classification argument:
  swarmHQ ROOT/Codex, PROMOTED/MANUAL with named imports. This strengthens
  September20's no-pencil result; the map remains rational with poles,
  not a JC2 counterexample. No finite-web or polynomial-source existence
  conclusion is claimed.

## 2026-09-20

- **Exact rational area preservation does not force an invariant pencil.**
  The [fixed countertest](xmodel/rational-area-no-pencil-swarmHQ-root-20260920T211700Z.md)
  F(x,y)=(y/(2x),y^4/(16x^4)-x^2) has determinant1 and generic degree2,
  but lambda1>=3 excludes a rational pencil for every positive iterate.
  [Independent Fable FIRST and integration](xmodel/rational-area-no-pencil-integration-swarmHQ-root-20260920T215300Z.md)
  confirm it: swarmHQ coordinator (Codex), PROMOTED/MANUAL with the
  Dinh--Nguyen product-formula import. The example has poles and is not
  a JC2 counterexample; a polynomial-source existence argument is still
  missing. No foliation/web exclusion or exact dynamical degree is claimed.
- **Any preserved finite algebraic web forces polynomial Keller invertibility.**
  The [discriminant proof](xmodel/invariant-web-keller-swarmHQ-root-20260920T123400Z.md)
  extends the foliation criterion to an unordered finite algebraic set of
  directions, for every nonzero constant Jacobian and positive iterate.
  Its discriminant yields either a preserved pencil or a split finite-etale
  direction cover. [Independent Fable FIRST and integration](xmodel/invariant-web-first-integration-swarmHQ-root-20260920T125600Z.md)
  confirm all six interfaces: swarmHQ ROOT/Astra, PROMOTED/MANUAL with
  named imports. No invariant web is produced for a hypothetical
  counterexample; JC2 remains unresolved.
- **Any preserved algebraic foliation now forces polynomial Keller invertibility.**
  For any nonzero constant Jacobian, a preserved algebraic foliation,
  even one without a rational first integral, forces a polynomial plane
  map to be an automorphism; preservation by a positive iterate suffices.
  The [proof](xmodel/invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md)
  combines primitive polynomial one-forms, exterior differentiation,
  Favre--Pereira Corollary B and the accepted rational-pencil theorem.
  [Independent Fable FIRST and binding integration](xmodel/invariant-foliation-first-integration-swarmHQ-root-20260920T103300Z.md)
  confirm all six interfaces: swarmHQ ROOT/Astra, PROMOTED/MANUAL with
  named imports. No invariant foliation is supplied for a hypothetical
  counterexample; this conditional result does not resolve JC2.
- **Any preserved rational pencil now forces polynomial Keller invertibility.**
  For any nonzero constant Jacobian, a nonconstant rational r satisfying
  r composed F=phi composed r forces F to be an automorphism, even if the
  original pencil is nonprimitive or has affine base points. The
  [unified proof](xmodel/rational-pencil-unification-swarmHQ-root-20260920T033600Z.md)
  eliminates periodic base points by vanishing order and extends the
  genus-zero properness argument to rational morphisms. It removes the
  previous modulus, closed-generator and exact-area dependencies while
  retaining named geometric and hyperbolic-moduli imports.
  [Independent Fable FIRST and binding integration](xmodel/rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md)
  confirm it: swarmHQ ROOT/Astra, PROMOTED/MANUAL. No preserved pencil
  for an arbitrary hypothetical counterexample is established; JC2
  remains unresolved.
- **A preserved rational polynomial pencil forces Keller invertibility.**
  For primitive polynomial h of geometric generic genus zero,
  h composed F=psi composed h now forces a polynomial Keller map F to be
  an automorphism, for every nonzero constant determinant and positive
  base degree. The [proof](xmodel/rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md)
  confines nonproperness to special fibers and proves their components
  smooth by cohomology. The inherited no-A1-component theorem then closes
  the argument. [Independent Fable FIRST and integration](xmodel/rational-pencil-first-integration-swarmHQ-root-20260920T013400Z.md)
  confirm it: swarmHQ ROOT/Astra, PROMOTED/MANUAL with named classical
  imports. This includes arbitrary C-star polynomial pencils without a
  normal-form classification. No pencil is supplied for arbitrary Keller
  maps; JC2 remains unresolved.

## 2026-09-19

- **A hyperbolic moving polynomial pencil produces a fixed rational invariant.**
  For a primitive polynomial h with h composed F=psi composed h,
  deg(psi)>=2, and hyperbolic full generic affine fiber, the
  [pointed-moduli and descent proof](xmodel/hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md)
  gives N(F)=deg(psi) and a fixed rational function for F itself.
  [Independent Fable FIRST](xmodel/hyperbolic-pencil-first-integration-swarmHQ-root-20260919T205600Z.md)
  confirms the theorem: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical
  moduli imports. The accepted exact-area theorem excludes this case for
  J(F)=1. No preserved pencil is supplied for arbitrary Keller maps, and
  nonhyperbolic fibers remain outside scope. JC2 remains unresolved.
- **A dominant reduced pencil forces normalized Keller invertibility even with a moving base.**
  If r=a/b has coprime algebraically independent polynomial numerator and
  denominator and r composed F=phi composed r, the
  [homogeneous-lift proof](xmodel/homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md)
  forces deg(phi)=N(F)=1 for constant 0<|det DF|<=1. Its degree-square
  identity and elementary iterate bound combine with the accepted dynamical
  inequality. [Independent Fable FIRST and reviewer-scope correction](xmodel/homogeneous-pencil-first-integration-swarmHQ-root-20260919T181000Z.md)
  confirm the theorem: swarmHQ ROOT/Astra, PROMOTED/MANUAL with the retained
  dynamics import. No such pencil is produced; polynomial r and other
  dependent reduced pairs are outside this proof. JC2 remains unresolved.
- **An exact-area rational map with a rational invariant must be birational.**
  The [compact-curve differential proof](xmodel/rational-area-invariant-swarmHQ-root-20260919T120200Z.md)
  removes both polynomiality and positive-genus requirements when the
  standard area form is preserved exactly; disconnected original pencils
  are also allowed. [Independent Fable FIRST and scoped integration](xmodel/rational-area-first-integration-swarmHQ-root-20260919T121900Z.md)
  confirm the result: swarmHQ ROOT/Astra, PROMOTED/MANUAL. It excludes a
  broad class of rational constructions, but supplies no invariant for
  arbitrary Keller maps and does not resolve JC2.
- **One source puncture excludes all birational target repairs of the fixed elliptic donor.**
  The [different-pencil proof](xmodel/one-puncture-target-swarmHQ-root-20260919T051000Z.md)
  shows that no birational target change makes Weierstrass multiplication
  with |m|>=2 polynomial on its original source plane, including one-sided coordinate
  normalization. [Independent Sol FIRST and exposition clarifications](xmodel/one-puncture-first-swarmHQ-sol-20260919T052700Z.md)
  confirm the result: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical
  curve imports. This strengthens the fixed-source construction filter,
  but does not cover arbitrary rational source changes or produce a
  general JC2 proof mechanism or counterexample.
- **A preserved positive-genus fibration obstructs polynomial conjugacy.**
  A dominant polynomial plane map preserving one rational function with
  geometrically integral positive-genus generic fiber has generic degree
  one. The [affine-curve and puncture proof](xmodel/positive-genus-invariant-swarmHQ-root-20260919T035200Z.md)
  excludes all polynomial birational conjugates of unscaled elliptic
  multiplication maps. [Independent Sol FIRST](xmodel/positive-genus-first-swarmHQ-sol-20260919T041000Z.md)
  confirms the exact scope: swarmHQ ROOT/Astra, PROMOTED/MANUAL with
  classical curve imports. It does not cover unrelated source/target
  repairs or supply an invariant for arbitrary Keller maps.
- **Whitney-sphere loops do not universally detect monodromy.** The
  conditional sphere-lifting obstruction is valid, but a fixed cusp
  complement is aspherical and nonabelian while all its one-double-point
  Lagrangian-sphere loops are trivial. The [covering and cusp calculation](xmodel/whitney-loop-asphericity-swarmHQ-root-20260919T025800Z.md)
  defeats the proposed universal loop-generation step: swarmHQ ROOT/Astra,
  MANUAL/PRODUCER-CHECKED, UNPROMOTED. A same-model co-check is not FIRST.
  This does not realize the cusp as a Keller nonproper locus or resolve JC2.
- **The first global commutator-lifting step already has the force of invertibility.**
  For a plane Keller pair, polynomial free-algebra lifts preserving
  [X,Y] modulo the square of its two-sided ideal exist exactly when
  the actual collision ideal is diagonal, hence exactly when the map
  is invertible. The [relation-module proof](xmodel/commutator-layer-collision-swarmHQ-root-20260919T005000Z.md)
  has [independent Fable FIRST with scope clarifications](xmodel/commutator-layer-first-swarmHQ-fable-20260919T011000Z.md):
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. The secant algebra is inherited;
  its explicit first-layer connection identifies the global lifting gap.
  Neither universal lift existence nor JC2 is proved or refuted.

## 2026-09-18

- **Completing the flat metric does not automatically give local CAT(0).**
  On the fixed punctured two-sheet source, an explicit target change
  produces two distinct shortest paths with the same endpoints in every
  neighborhood of an added completion point. The [length calculation](xmodel/completed-metric-geodesic-swarmHQ-root-20260918T223631Z.md)
  has [independent Fable FIRST and binding scope corrections](xmodel/completed-metric-first-swarmHQ-fable-20260918T225800Z.md):
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. This closes one automatic curvature
  shortcut, not a statement about whole-plane Keller maps or JC2.
- **Whole-plane geometry alone does not close the holomorphic domain gap.**
  For the explicit polynomial weight phi=|x|^2+|xy|^2+|xy^2-y|^2 on C2,
  the maximal ordinary derivative domain is nondense despite strict
  plurisubharmonicity, finite mass and a Hessian-determinant floor1/2.
  The [continuous-separation proof](xmodel/whole-plane-weighted-domain-swarmHQ-root-20260918T211200Z.md)
  has [independent Fable FIRST and scope clarification](xmodel/whole-plane-weighted-first-swarmHQ-fable-20260918T213200Z.md):
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. Its determinant is variable and its
  defining map has three outputs, so this is not a Keller weight or JC2
  counterexample. A positive density proof still needs more Keller structure.
- **The holomorphic density gap is equivalent to invertibility.** For an
  actual polynomial Keller map, the common lifted holomorphic derivative
  domain is dense in its Gaussian holomorphic L2 space exactly when the
  map is invertible. The [proof](xmodel/holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md)
  adds a global L2 polynomial witness and continuous separation under
  hypothetical noninvertibility, not merely strict domain inclusion.
  [Independent Fable FIRST and reviewer correction](xmodel/holomorphic-density-first-swarmHQ-fable-20260918T194700Z.md)
  confirm it: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical imports.
  This identifies the strength of the remaining premise; it proves
  neither that premise nor JC2. The real Sobolev core remains valid.
- **A real first-order Gaussian cutoff gap is closed.** For any polynomial
  Keller map, the [new proof](xmodel/gaussian-sobolev-cutoffs-swarmHQ-root-20260918T181400Z.md)
  constructs source-compact cutoffs with vanishing weighted energy and
  proves density in the FULL REAL weighted W1,2 space, plus a scoped
  integration-by-parts identity. [Independent Fable FIRST and scope corrections](xmodel/gaussian-sobolev-first-swarmHQ-fable-20260918T182900Z.md)
  confirm it: swarmHQ ROOT/Astra, PROMOTED/MANUAL. Holomorphic-subspace
  density, higher-order domains and polynomial integrability are not
  established. No completeness or JC2 conclusion follows.
- **That core does not automatically give a Gaussian spectral gap.** On
  the existing rational two-sheet control, Re(s) has Rayleigh quotient1
  despite local curvature2 and the real first-order core; its Hessian
  norm diverges. The [explicit test](xmodel/gaussian-spectral-gap-control-swarmHQ-root-20260918T184800Z.md)
  has [independent Sol FIRST](xmodel/gaussian-spectral-first-swarmHQ-sol-20260918T185300Z.md):
  swarmHQ ROOT, PROMOTED/MANUAL. This refutes one analytic inference,
  not an actual-source estimate or JC2.
- **One preserved quotient removes a connected-fiber restriction.**
  If a dominant rational self-map Phi preserves the SAME rational plane
  quotient rho, inducing h, then deg(h) divides deg(Phi), even when rho
  has disconnected geometric generic fibers. The [field proof](xmodel/same-quotient-degree-cancellation-swarmHQ-root-20260918T170200Z.md)
  has [independent Sol FIRST](xmodel/same-quotient-degree-first-swarmHQ-sol-20260918T170700Z.md):
  swarmHQ ROOT, PROMOTED/MANUAL. Thus a polynomial Keller descendant of
  one degree1/2/3 self-map is invertible, using the accepted small-degree
  results. Different endpoint quotients and arbitrary towers are not
  covered; no quotient for an arbitrary Keller map has been constructed.
- **One actual Hamiltonian symmetry is sufficient for invertibility.**
  For a Keller pair (P,Q), one infinite-order polynomial source automorphism
  commuting with D={P,-} forces (P,Q) to be an automorphism. The
  [conditional proof](xmodel/hamiltonian-isotropy-swarmHQ-root-20260918T155000Z.md)
  descends the symmetry to the target and excludes its periodic nonproper
  curves. [Independent Fable FIRST](xmodel/hamiltonian-isotropy-first-swarmHQ-fable-20260918T160600Z.md)
  confirms it: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical imports.
  No such symmetry has been constructed for arbitrary Keller pairs;
  formal flows and target shears do not supply it. JC2 remains open.
- **A cited source was corrected.** Sabbah v4 deletes the good-wild/additive
  comparison branch used as background in an old unpromoted screen.
  The [correction and independent review](AUDIT.md#sabbah-v4-source-correction--2026-09-18)
  preserve its separate local obstruction; no promoted dependency was
  found in the scoped search. This is source maintenance, not a JC2 advance.
- **A fixed-source target-field filter rules out arbitrary rational target repairs.**
  For deg(p)>1 and nonzero rational r, every polynomial in C(p(x),r(x)y)
  loses the x tangent at (a,0) when p'(a)=0. Hence no two such polynomials
  form a Keller pair. The [short proof](xmodel/target-field-tangent-discriminator-swarmHQ-root-20260918T132500Z.md)
  has [independent Sol FIRST](xmodel/target-field-tangent-first-swarmHQ-sol-20260918T132721Z.md):
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. Arbitrary source substitutions and
  general target fields are not covered; this is not a JC2 reduction.
- **The complementary graph pair is excluded for every normalized weighted-lift seed.**
  The [degree identity](xmodel/weighted-xgraph-degree-swarmHQ-root-20260918T115800Z.md)
  removes the earlier graph-invariance premise: on every nonzero x=h(y,z),
  the pair (B,A) has Jacobian degree 6(n-1)deg(h)+4n-3>0, for every
  seed degree n>=2. The zero graph is triangular. Polynomial pre- and
  postcomposition cannot repair a nonzero graph. [Independent Sol FIRST](xmodel/weighted-xgraph-first-swarmHQ-sol-20260918T121133Z.md)
  confirms the self-contained proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL.
  Arbitrary nonlinear three-output maps and other embedded planes are
  not excluded. This is a uniform construction exclusion, not a JC2 proof.
- **One invariant-graph construction is excluded uniformly in the graph polynomial.**
  The [fixed-seed proof](xmodel/invariant-quartic-graph-swarmHQ-root-20260918T103700Z.md)
  shows that every Keller restriction to an invariant graph x=h(y,z)
  in the specified lift is an automorphism, without a degree bound on h.
  [Independent Sol FIRST](xmodel/invariant-quartic-first-swarmHQ-sol-20260918T104400Z.md)
  confirms it: swarmHQ ROOT/Astra, PROMOTED/MANUAL with the accepted
  injectivity-on-one-source-line theorem. This is a bounded construction
  exclusion, not a JC2 proof or a theorem about arbitrary embedded planes.
- **A reducible fiber of a nonsingular polynomial need not have a rational component.**
  The [explicit fixed example](xmodel/reducible-elliptic-fiber-swarmHQ-root-20260918T065100Z.md)
  has exactly two disjoint genus-one zero-fiber components and no critical
  point anywhere on the plane. [Independent Fable FIRST](xmodel/reducible-elliptic-first-swarmHQ-fable-20260918T070300Z.md)
  confirms it and the proof that it has no polynomial Jacobian mate:
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. This closes an auxiliary shortcut,
  not a question about genuine Keller fibers or JC2; no family search follows.
- **Fractional-linear rational donors reduce to an excluded product class.**
  The [three-case normal form](xmodel/fractional-linear-donor-swarmHQ-root-20260918T011400Z.md)
  covers rational J(P,Q)=1 pairs with Q Mobius in one source variable.
  For mapping degree greater than one, it excludes every constant-J
  birational target repair and every finite rational source substitution
  yielding a whole-plane polynomial Keller pair, by the accepted product
  theorem. [Independent Fable FIRST](xmodel/fractional-linear-first-swarmHQ-fable-20260918T013000Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with inherited
  classical imports. There is no degree cap within this class; degree-one
  donors, arbitrary rational pairs and general JC2 remain outside scope.

## 2026-09-17

- **Nonsingularity and irreducible fibers do not force geometric-unit vanishing.**
  The [explicit degree9 polynomial](xmodel/cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md)
  has every closed fiber irreducible and no critical point, but a cubic
  polynomial base change carries an explicit non-base unit of norm1.
  [Independent Fable review and binding clarifications](xmodel/cubic-base-unit-first-swarmHQ-fable-20260917T221500Z.md)
  confirm the counterexample: swarmHQ ROOT/Astra, PROMOTED/MANUAL.
  The same polynomial has no rational constant-Jacobian mate, so this
  closes an auxiliary shortcut, not JC2. The earlier reduction theorems
  remain valid; a unit exclusion must use additional Keller structure.
- **Actual boundary geometry reduces generic units to polynomial base covers.**
  The [horizontal-puncture argument](xmodel/horizontal-unit-polynomial-base-swarmHQ-root-20260917T211700Z.md)
  replaces any geometric-generic unit by a non-base unit over one horizontal
  polynomial cover. Extra nonsingularity and every-fiber irreducibility
  globalize it without a power. [Independent Fable review](xmodel/horizontal-unit-first-swarmHQ-fable-20260917T213900Z.md)
  confirms the reduction: swarmHQ ROOT/Astra, PROMOTED/MANUAL. Unlike the
  refuted abstract D4 criterion, this may enlarge the original defining
  cover. The subsequent cubic example above refutes unconditional unit
  vanishing on these surfaces; the Keller-specific target and JC2 remain open.
- **A fixed character-surface form cannot come from a rational symplectic plane.**
  The [all-parameter character-cubic obstruction](xmodel/character-cubic-nonexactness-swarmHQ-root-20260917T200800Z.md)
  has a nonzero double residue; finite-field trace prevents any finite cover
  from making the form exact. [Independent Fable review](xmodel/character-cubic-first-swarmHQ-fable-20260917T202600Z.md)
  confirms both the plane-parametrization and constant-bracket exclusions:
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. This closes one fixed-form construction
  route, not arbitrary rational maps, other symplectic surfaces or JC2.
- **An abstract reduction to affine-line base covers fails.**
  The [D4 witness](xmodel/d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md)
  has the required missing cohomology representation, but no affine-line
  intermediate quotient retaining a nonzero vector. [Independent Fable review](xmodel/d4-rational-base-first-swarmHQ-fable-20260917T193000Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical
  Riemann existence/algebraization. This closes a representation-only
  shortcut; actual geometric units are not realized and JC2 is unchanged.
- **A section closes one marked-quartic quotient route.**
  On the whole four-variable marked-root source, the
  [quartic-invariant map has an explicit polynomial section](xmodel/marked-quartic-section-swarmHQ-root-20260917T181100Z.md).
  Normality then excludes every nontrivial polynomial Keller descent through
  a compatible rational plane quotient. [Independent Fable review](xmodel/marked-quartic-section-first-swarmHQ-fable-20260917T182700Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with the classical
  birational Keller theorem. This is a narrow fixed-target exclusion, not an
  obstruction to arbitrary plane substitutions or a general JC2 advance.
- **Integral back coordinates obstruct rational donor repair.**
  The [new criterion](xmodel/integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md)
  shows that a rational constant-Jacobian donor with BOTH original
  coordinates integral over its output ring can admit a whole-plane
  polynomial Keller source repair only if the donor is already a
  polynomial automorphism. This excludes EVERY multiplication order
  |m|>=2 on the fixed Weierstrass families y^2=x^3+a*x+t, for all a,
  under every finite rational source substitution. [Independent Sol review](xmodel/integral-back-coordinate-review-swarmHQ-sol-20260917T161900Z.md)
  confirms both claims: swarmHQ ROOT/Astra, PROMOTED/MANUAL with named
  classical imports. Arbitrary target repairs and general Keller-source
  integrality remain outside scope; JC2 is unresolved.
- **A zero-free target model excludes an entire target-repair class.**
  The [new branch-model criterion](xmodel/zero-free-branch-model-swarmHQ-root-20260917T044000Z.md)
  extends the smooth-projective-branch obstruction to an explicitly given
  rational model whose area form has no zeros. One blowup supplies it for
  the recorded rational-Liouville family, excluding every constant-J
  birational target change and every finite rational source substitution,
  uniformly in Q and the integration constant. [Independent Sol review](xmodel/zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md)
  confirms both claims: swarmHQ ROOT/Astra, PROMOTED/MANUAL with named
  classical imports. No eligible-model theorem for arbitrary Keller maps,
  nonconstant-J target exclusion or JC2 resolution follows.
- **Exactness and constant units are a distinct, unresolved combination.**
  The [post-globalization scope synthesis](xmodel/ideation-full0400-swarmHQ-synthesis-20260917T042300Z.md)
  notes that both recorded exact positive-genus plane curves have
  nonconstant units. They do not decide whether exactness together with
  constant units forces genus zero. A bounded cross-check found neither
  proof nor counterexample; the actual Keller fiber and global-unit
  implications remain separate gaps. MANUAL/DOCUMENTARY, UNPROMOTED;
  no new closing test, theorem promotion or construction follows.

## 2026-09-16

- **Generic units can be made global after a fixed power.**
  The [finite-multisection argument](xmodel/geometric-unit-globalization-swarmHQ-root-20260916T232700Z.md)
  works over every finite extension of C(P), assuming P is nonsingular and
  EVERY fiber is irreducible. Power and base rescaling remove all finite
  coefficient poles while preserving non-base dependence.
  [Independent Sol review](xmodel/geometric-unit-globalization-review-swarmHQ-sol-20260916T233000Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with standard
  divisor and finite-flat norm facts. This removes a global-map obstacle;
  scalar-unit vanishing, mixed-period splitting and JC2 remain unresolved.
- **Smooth-branch donors admit no constant-J birational target repair.**
  The [uniform exclusion](xmodel/symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md)
  covers every rational product pair p=R(s), q=t/R'(s), degR>=2,
  and every finite rational source substitution. Its more general premise
  is that every projective branch component is smooth; exceptional new
  branch divisors are explicitly included. [Independent Sol review](xmodel/symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with classical
  imports and the [recorded wording clarification](AUDIT.md#symplectic-target-smooth-branch-1--2026-09-16).
  Nonconstant-J target changes, singular projective branch components and
  arbitrary Keller sources remain outside scope. No JC2 resolution follows.
- **All-seed tangent graphs admit no linear Keller projection.**
  The [three-minor calculation](xmodel/tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md)
  gives distinct positive partial-y degrees for every polynomial graph
  and every admissible seed degree in the literal tangent presentation.
  Thus every constant linear plane projection, even with polynomial
  postcomposition, fails to be Keller. [Independent Sol review](xmodel/tangent-graph-linear-review-swarmHQ-sol-20260916T183500Z.md)
  confirms the whole-plane hypotheses and n=0 boundary case:
  swarmHQ ROOT/Astra, PROMOTED/MANUAL. Arbitrary nonlinear three-output
  maps, other source-plane orientations and general JC2 remain outside scope.
- **The natural linear/cubic SL2 quotient is a plane automorphism.**
  The [global calculation](xmodel/linear-cubic-sl2-quotient-swarmHQ-root-20260916T174200Z.md)
  identifies the entire resultant-one source with SL2 times A2 and proves
  that multiplication induces (u,v)->(-3u,-27v) on the full affine
  invariant quotients. [Independent Sol review](xmodel/linear-cubic-sl2-review-swarmHQ-sol-20260916T174500Z.md)
  confirms the polynomial inverse and degenerate cases: swarmHQ ROOT/Astra,
  PROMOTED/MANUAL. This exact quotient yields no counterexample; other
  constructions and general JC2 remain outside scope.
- **Connected quotient towers cannot create a plane counterexample.**
  The [new interface](xmodel/connected-quotient-tower-swarmHQ-root-20260916T155300Z.md)
  applies to arbitrary compatible rational quotients of finite ambient
  towers whose individual field degrees are at most three, provided BOTH
  endpoint generic fibers are geometrically integral. The descended
  polynomial Keller map is then an automorphism, by the accepted
  small-block exclusions. [Independent Sol review](xmodel/connected-quotient-review-swarmHQ-sol-20260916T155700Z.md)
  confirms the field argument: swarmHQ ROOT/Astra, PROMOTED/MANUAL with
  those explicit dependencies. No group action or tower-length bound is
  needed. Arbitrary projected sections and general JC2 remain outside scope.
  The [subsequent scope synthesis](xmodel/ideation-full2130-swarmHQ-synthesis-20260916T214500Z.md)
  identifies the failed geometric-integrality hypothesis in a proposed
  canonical-graph composition. It also separates the donor filters' target
  quantifiers and the remaining dynamical-equality gap. MANUAL/DOCUMENTARY,
  UNPROMOTED; no new closing test or theorem is claimed.
- **Weighted-lift coordinate fibers create no new plane counterexample.**
  The [uniform proof](xmodel/weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133700Z.md)
  covers all admissible seed degrees and literal coordinate levels, using
  nonconstant units and a boundary cycle. The only entire-plane-dominated
  component has a triangular automorphism as its remaining pair.
  [Independent Sol review](xmodel/weighted-lift-coordinate-review-swarmHQ-sol-20260916T133500Z.md)
  confirms the exact arbitrary-first-leg scope: swarmHQ ROOT/Astra,
  PROMOTED/MANUAL with the accepted morphic boundary theorem. Arbitrary
  projections, target changes and general JC2 remain outside scope.
- **A simple critical line supplies a precise F10 boundary property.**
  The [lemma and source attachment](xmodel/simple-critical-line-f10-swarmHQ-root-20260916T105500Z.md)
  prove that J=c*g with nonconstant critical image makes its parametrization
  birational; intrinsically singular branches start with orders(m,m+1).
  [Independent Sol review](xmodel/simple-critical-line-review-swarmHQ-sol-20260916T105619Z.md)
  confirms residue degree1 and transverse index2 on the specified F10
  divisor: swarmHQ ROOT/Astra, PROMOTED/MANUAL with standard curve imports.
  This removes a scoped hypothesis, not the separate one-dicritical or
  global transport gaps. No new F10 exclusion or JC2 closing test follows.
  The [portfolio scope check](xmodel/ideation-full1108-swarmHQ-synthesis-20260916T111900Z.md)
  distinguishes this divisor's one two-cycle from the whole inertia
  permutation; even transposition generation alone gives no degree bound.
  That synthesis is MANUAL/DOCUMENTARY, PRODUCER-CHECKED, UNPROMOTED;
  no new global mechanism or construction test was admitted.
  A later [explicit degree countercontrol](xmodel/critical-image-degree-countercontrol-swarmHQ-root-20260916T120130Z.md),
  with [independent Sol review](xmodel/critical-image-degree-review-swarmHQ-sol-20260916T120413Z.md),
  refutes the proposed coprime-or-dividing critical-image degree shortcut:
  J=g can have restriction degrees6,9. PROMOTED/MANUAL; neither a Keller
  counterexample nor an F10 source solution or exclusion follows.
- **Fixed Legendre tripling cannot be repaired by any finite source change.**
  The [degree-nine rational constant-Jacobian candidate](xmodel/legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md)
  has ramification index3 over a generic target line. This persists under
  every finite rational source substitution; a whole-plane polynomial
  Keller realization would contradict Chau's classical no-line theorem.
  [Independent Sol review](xmodel/legendre-tripling-review-swarmHQ-sol-20260916T094200Z.md)
  confirms the valuation, full-normalization argument and controls:
  swarmHQ ROOT/Astra, PROMOTED/MANUAL with named imports. Only this fixed
  target pair is excluded, not arbitrary target changes, other elliptic
  constructions or JC2. No multiplier-family search follows.
- **Equal-degree scaling quotients contribute no new covering degree.**
  The [uniform proof](xmodel/equal-degree-resultant-quotient-swarmHQ-root-20260916T083300Z.md)
  covers every equal factor degree and every polynomial two-parameter
  product family, including nonlinear ones. Multiplication on the exact
  scaling quotient is finite; every reduced dominating component of its
  resultant-one base change maps isomorphically to the parameter plane.
  [Independent Sol review](xmodel/equal-degree-quotient-review-swarmHQ-sol-20260916T083553Z.md)
  confirms the component and nilpotent controls: swarmHQ ROOT/Astra,
  PROMOTED/MANUAL with standard inputs. Unequal-degree nonlinear families,
  arbitrary initial source parametrizations and JC2 remain outside scope.
- **Section-supported scroll donors are excluded in every ruling degree.**
  The [uniform proof](xmodel/section-supported-scroll-donor-swarmHQ-root-20260916T080756Z.md)
  excludes any dominant regular A2 first leg when a finite Hirzebruch-to-P2
  map's entire inverse-line-plus-ramification boundary consists of sections.
  Removing fixed normal ramification forces two distinct section collisions;
  the accepted all-contact logarithmic theorem then applies. There is no
  degree, multiplicity or contact-order bound. [Independent Sol review](xmodel/section-supported-scroll-review-swarmHQ-sol-20260916T081156Z.md)
  confirms the exact scope: swarmHQ ROOT/Astra, PROMOTED/MANUAL with the
  named logarithmic import. Vertical components, multisections and arbitrary
  Keller-source landing remain outside scope; JC2 is not resolved.
- **A source correction withdraws an old boundary obstruction.**
  [The correction](xmodel/projective-bundle-v2-correction-swarmHQ-root-20260916T072000Z.md)
  records a missed September 14 revision: one support point, not contact
  length one, is the relevant condition in arXiv:2608.27341v2. The old
  higher-contact/topological exclusion is withdrawn. The reviewed
  all-contact logarithmic theorem and scroll donor exclusion use distinct
  collision counts and do not depend on that error. Historical evidence
  is preserved; this is a correctness repair, not new JC2 progress.
- **A nonsingular pseudo-plane function can have genus-one generic fiber.**
  The [fixed example and proof](xmodel/pseudoplane-genus-one-no-mate-swarmHQ-root-20260916T063400Z.md)
  h=(A+U) composed with eta^2 on U^2=A+A^2 Z refutes the proposed
  rational-fiber shortcut. An incompatible-poles argument also excludes
  every regular scalar mate of this h. [Independent Sol review](xmodel/pseudoplane-genus-one-review-swarmHQ-sol-20260916T063700Z.md)
  confirms both scopes: swarmHQ ROOT/Astra, PROMOTED/MANUAL. This applies
  the known polar-fiber mechanism, not a new global theorem. General
  scalar pairs on the surface and JC2 remain unresolved.
- **Affine binary-form coefficient planes yield no nontrivial entire-plane source.**
  The [uniform proof](xmodel/binary-form-affine-plane-obstruction-swarmHQ-root-20260916T053400Z.md)
  covers arbitrary affine two-planes and all positive unequal factor degrees:
  every entire-A2 component of the original resultant-one source maps
  isomorphically to its parameter plane. The main dual discriminant forces
  escape on EACH component, while polynomial parametrizability of plane-map
  nonproper curves forbids that discriminant. Degenerate cases are handled
  separately. [Independent Sol review](xmodel/binary-form-affine-plane-review-swarmHQ-sol-20260916T053900Z.md)
  confirms the proof: swarmHQ ROOT/Astra, PROMOTED/MANUAL with named imports.
  This retires an all-degree affine-slice construction route, not nonlinear
  targets, arbitrary source parametrizations or JC2. No exhaustive novelty claim.
- **Finite fibers do not suffice for dynamical-degree lowering.** The
  [explicit map](xmodel/quasifinite-dynamical-minimum-swarmHQ-root-20260916T043600Z.md)
  F=(x+x^2*y,y+x*y) is quasi-finite of generic degree2, yet its minimum
  dynamical degree over all polynomial source/target coordinate changes
  is1+sqrt(2). The proof uses Jung normal forms and exact corner iteration,
  not a bounded coordinate search. [Independent Sol review](xmodel/quasifinite-dynamical-review-swarmHQ-sol-20260916T044500Z.md)
  confirms the exact minimum, also for determinant-one changes: swarmHQ
  ROOT/Astra, PROMOTED/MANUAL with a classical import. NON-KELLER example;
  no refutation of the Keller-specific bound, novelty claim or JC2 closure.
  The later [integral-spectrum control](xmodel/integral-dynamical-minimum-swarmHQ-root-20260916T162700Z.md)
  strengthens this negative result: h=x^2*y^2+y, F=(h^2+x,h^3+x) has
  generic degree6, integral dynamical degree in EVERY polynomial frame,
  and attained minimum10. [Sol FIRST](xmodel/integral-dynamical-review-swarmHQ-sol-20260916T163000Z.md)
  confirms it with the [recorded wording correction](AUDIT.md#integral-dynamical-minimum-control-1--2026-09-16).
  PROMOTED/MANUAL; adding integrality still does not supply Keller-specific lowering.
- **The quintic marked-pair construction has no polynomial target invariants.**
  Its [exact source chart](xmodel/quintic-partition-target-field-swarmHQ-root-20260916T032000Z.md)
  is a plane minus one point, mapping generically ten-to-one onto all but
  one point of a projective moduli surface. Divisorial poles force every
  target rational function with polynomial pullback to be constant.
  [Independent Sol review](xmodel/quintic-partition-review-swarmHQ-sol-20260916T033100Z.md)
  confirms the rings, boundary and named GIT import: swarmHQ ROOT/Astra,
  MANUAL, PROMOTED. This excludes the fixed-chart construction, not
  arbitrary source changes, other markings or JC2. No novelty is claimed
  for the standard pole mechanism.
- **All additive-group equivariances of the fixed running core are trivial.**
  The [proof](xmodel/running-core-additive-rigidity-swarmHQ-root-20260916T023000Z.md)
  uses the exact nonproper-value surface: its normalized singular-curve
  preimage is a hyperbola, forcing additive-group rigidity. A maximal-factor
  argument also rules out ambient actions fixing that surface pointwise.
  [Independent Sol review](xmodel/running-core-additive-review-swarmHQ-sol-20260916T023700Z.md)
  confirms the complete fixed-map exclusion: swarmHQ ROOT/Astra, MANUAL,
  PROMOTED. Prior geometry is credited in the report. This replaces a
  one-action test, not the general conditional quotient theorem; stabilization,
  other triples, other groups, projections and JC2 remain outside scope.
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
  September16 update: the [reviewed all-action result](xmodel/running-core-additive-rigidity-swarmHQ-root-20260916T023000Z.md)
  now excludes every algebraic additive equivariance of this fixed core;
  the conditional bridge for other three-dimensional maps is unchanged.
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
