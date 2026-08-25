# Bounded source-delta audit: `jacobian-collision-geometry`

## Verdict

`REUSABLE_SCOPED_DELTA`

Audited public source: `what-social-construct/jacobian-collision-geometry` at
`9a3d6caa7fa465a9b81dde2140e269655911858d` (commit time
`2026-08-24T09:35:06Z`).  I cloned it outside this repository, detached at
that SHA, compared it with the last Aug-14 commit
`e1ea8e546a6b5b66fce06c2acb8eaa22f7a3322e` (2026-08-14T18:24:26Z), read
`README.md`, `paper/paper2.tex`, `SEMANTIC-PARITY.md`, the detailed theorem
inventory, and the Lean sources named below.  A clean `lake build` fetched the
pinned Lean/Mathlib dependencies and compiled 763 of 2,838 targets without an
error before I stopped the dependency rebuild; this audit therefore does not
claim an independently completed clean build.  Lean acceptance is evidence only that the encoded terms typecheck
relative to their hypotheses and axioms; it is not evidence that those
hypotheses hold or that the manuscript's geometric arguments are correct.

The delta is reusable because the source now constructs an actual conjugate
Galois collision-map pair and its planar off-diagonal evaluation, and because
the nonnormal cubic branch is more completely internalized.  It is not an
actionable JC2 delta: Paper II is principally an extraction/reframing of
material already present on Aug 14, and every route from its boundary or
conductor language to unrestricted planar vanishing still crosses an
unproved universal assertion or an absent geometric landing construction.

## 1. Genuine post-Aug-14 content

The large apparent delta is mostly organizational.  Commits `97d05e2` and
`598ad29` split/reorganized the papers and modules; `991ef8a` rebranded the
repository; `67d28d8` extracted standalone `paper/paper2.tex`.  The Aug-14
tree already had the planar secant/colon theorem, boundary ideals and
valuation containment, rigidity targets, finite denominator lemmas,
monogenic order, Tate reconstruction, trace-dual/conductor identities, and
the conductor-landing API.  Renamed files with 94--100% similarity and the
new umbrella import files are not mathematical deltas.

The genuine Lean-certified, non-literature-interface additions are scoped:

1. `CollisionIdeals/General/Galois/PolynomialCollisionPair.lean` constructs
   `polynomialConjugateSourceMapOverImage`, proves agreement on the image
   coordinates and right-coset invariance, proves
   `polynomialConjugateSourceMapOverImage_ne_of_not_mem_conjugateFixingSubgroup`,
   and packages `polynomialGaloisCollisionPair`.  Thus an ordered moved pair
   `(g, sigma*g)` is now an actual map pair out of the polynomial source, not
   just sheet notation.
2. `CollisionIdeals/Planar/GaloisCollisionPair.lean` specializes that
   construction and defines `galoisOffDiagonalLiftOfNotMem`: under an
   explicitly supplied normal-closure datum and the Keller hypothesis, a
   group element outside `gHg^-1` gives a map from `OffDiagonalRing F` into
   the normal-closure field.  This closes a real interface gap, but proves no
   coverage, boundary separation, or vanishing.
3. `CollisionIdeals/ComplexThree/Cubic/Branch.lean` proves
   `irreducible_minpolyDiv_of_cubic_of_not_normal`, the residual rank-two
   calculation, and constructs
   `cubicResidualEquivNormalClosureOfNotNormal`.  Consequently the revised
   `complexThreeCubicS3Collision` no longer needs a caller-supplied residual
   equivalence in the nonnormal separable cubic branch.  This is a genuine
   conditional cubic theorem, not a planar theorem and not a concrete Keller
   counterexample.
4. `CollisionIdeals/Planar/Secant/Projector.lean` gives a chosen concrete
   `planarCollisionIdempotent` and convenient kernel/projector theorems.  It
   repackages the pre-existing existence theorem; it is an API improvement,
   not a stronger secant or collision theorem.

The following are not new mathematical advances: the Paper II split;
`Statements`/`Equivalences`/`Interfaces` ownership modules; the renamed
normalization, boundary, secant, and endgame files; the three standard
literature interfaces; and restatements that make an unproved proposition an
explicit theorem argument.

## 2. Universal implication and the first missing arrow

There is no unconditional universal implication narrowing unrestricted JC2.
The dependency audit is:

| Input/language | What Lean proves | What is still supplied or absent |
|---|---|---|
| `PlanarBoundaryCoherence F` | `planarVanishing_of_boundaryCoherence` composes it to vanishing | Requires `BoundaryCoherenceBridge`, whose conclusion is that the whole intermediate boundary is empty.  Neither the coherence proposition nor the bridge is proved. |
| `PlanarRamificationRigidity` | `planarVanishing_of_ramificationRigidity` composes finite-length differentials to vanishing | Requires `RamificationRigidityBridge` to no codimension-one ramification, plus purity and finite-etale rigidity.  Rigidity and its bridge are not proved. |
| moving-sheet coverage | `noCodimensionOneRamification_of_movingSheetCoverage`, then `planarVanishing_of_movingSheetCoverage` | `PlanarMovingSheetCoverage M.diagram` is an argument.  Lean constructs the boundary ideals but does not establish universal coverage. |
| boundary separation | `BoundaryIdealData.noCodimensionOneRamification`, then `planarVanishing_of_boundarySeparation` | `PlanarBoundarySeparation M.diagram` is an argument.  The missing candidate landing is intended to produce it but does not. |
| no hidden inertia | `planarVanishing_of` and `planarVanishing_assuming_standardGeometry` | `PlanarNoHiddenInertia M.diagram` is an argument.  `noHiddenInertia_of_movingSheetCoverage` only changes the hypothesis language. |
| conductor landing | `boundarySeparation_of_monogenicConductorLanding` and `planarVanishing_of_monogenicConductorLanding` | Both require a nonzero candidate, candidate containment in the landing ideal, and the pointwise pole hypothesis.  No actual secant-frame specialization supplies these arguments. |
| local cohomology / DVR pole | only abstract principal-parts objects and generic torsion lemmas exist | The localization to `Frac(T_p)/T_p`, common ambient quotient map, and pointwise pole theorem are missing from Lean. |
| downstream bridges | no codimension-one ramification implies the finite-etale and field-trivial endgame | The convenience wrappers use the axioms `branchPurityA2` and `affinePlaneFiniteEtaleRigidity`; automorphism additionally uses `axGrothendieckA2`.  A `PlanarKellerCollisionModel F`, including normalization and Keller-to-etale/flat interfaces, is supplied rather than universally constructed in the endgame theorem. |

For the manuscript's proposed conductor route, the first absent typed arrow
is earlier than the advertised ideal containment: it has not constructed the
actual evaluated `(g,sigma*g)` overlap coefficient family and the common map
from fixed-moving principal parts and the trace-dual quotient into one
ambient `N/T`.  Without those objects there is no source-level morphism on
which to state the claimed geometric landing square.  After those typing
arrows, the first unproved mathematical arrow is the DVR/local-cohomology
pole statement; after that comes the uniform containment

`d.sf_(C,1) <= c.tr_C`

(or a finite-jet/prescribed-scalar substitute).  `README.md` and
`SEMANTIC-PARITY.md` explicitly list all of these omissions.

As a universal assertion over all planar Keller maps, boundary separation
(and hence an unqualified universal landing assertion that implies it) is not
a strict narrowing of JC2.  The manuscript itself notes that nonzero
intersection is equivalent to separation, and its standard endgame makes
universal separation imply `PlanarVanishing`; `Planar.Equivalences` makes
that, with Ax--Grothendieck, the planar Jacobian conjecture.  Thus the first
*universal endpoint* still owed is equivalent in strength to all of JC2 in
this framework, not a theorem for a smaller degree/support class.  Individual
map-specific coverage, pole, or landing statements are strictly weaker and
could kill a named client, but none is supplied for any campaign client.

`PlanarRamificationRigidity` by itself is merely a named finite-length
condition; the missing `RamificationRigidityBridge` is needed even to reach
no codimension-one ramification.  Likewise `PlanarBoundaryCoherence` is not a
proved global properness theorem merely because the normalization algebra is
finite over the image algebra.

## 3. Secant/colon crosswalk

Let `S=k[x,y,u,v]`, `I=(F(x,y)-F(u,v))`, and
`Delta=(x-u,y-v)`.  For a polynomial secant matrix `A` with
`A*(x-u,y-v)^t=F(x,y)-F(u,v)` and constant nonzero Jacobian `c`, our reviewed
idempotent is `e=c^-1 det(A)`.  Their notation is

`delta_F=det(A)`, `q_F=1-delta_F/c=1-e`.

Their proved identities in `Planar/Secant/Algebra.lean`,
`Planar/Secant/Ideal.lean`, and `Planar/Secant/Projector.lean` say exactly:

- `delta_F*Delta <= I` and `delta_F = c mod Delta`;
- `q_F` is the complementary idempotent and generates the obstruction/off
  factor;
- `I:Delta = I+(delta_F)`;
- clopenness makes the first colon equal the saturation, so
  `I:Delta = I:Delta^infinity = I+(det A)`;
- the diagonal and off factors give the corresponding product/CRT
  decomposition.

This exactly duplicates the mathematical result confirmed in
`xmodel/secant-idempotent-review-grok-20260824.md` and recorded in approach
32, `AUDIT.md`, and `PROGRESS.md`.  Their chosen explicit divided-difference
secant is one secant convention; our review proves convention independence
modulo `I` for any polynomial secant matrix.  The public source's concrete
projector wrapper is convenient, but no stronger degree, support, height,
boundary, or unit-ideal theorem follows.  In particular,
`I+(det A)=S` for every characteristic-zero Keller map is still injectivity
and hence JC2.  The hypotheses matter: the idempotent normalization uses
`c` a unit/`IsPlanarKeller`; the bare adjugate containment does not.

## 4. Tate/conductor and first-jet audit

There is no concrete source-defined containment or computable invariant that
can presently be tested on the maximum-12 order-three fibre, the TD6 center
family, or the AS branch without adding the missing universal/geometric
construction.

What is actually source-defined and proved is generic:

- `powerBasis_tate_reconstruction` and the two
  `traceDual_monogenic_iff_*` theorems in
  `Research/TateReconstruction.lean`;
- monogenic and overorder trace-dual/conductor identities in
  `Research/MonogenicTraceDual.lean`;
- `finiteCoefficientDenominatorIdeal` and
  `finiteCoefficientDenominatorIdeal_ne_bot` for an already supplied finite
  family in a fraction field;
- `monogenicConductorBoundedStage` and
  `monogenicConductorLandingIdeal`, plus conditional implications from a
  supplied nonzero landing candidate and supplied pointwise pole test.

The first-jet label does not denote a constructed campaign-ready ideal.  The
source says explicitly that the actual evaluated overlap family is missing,
the Keller frame has not been extended to the relevant fields/conjugate
rings, the geometric trace dual has not been specialized, and the open-section
algebra `R_C` and common quotient maps are absent.  Consequently the generic
denominator ideal could be computed only after inventing precisely the data
the source has not defined.  Computing arbitrary denominators for arbitrary
chosen coefficients would merely test denominator clearing, not conductor
landing.

The named clients also mismatch the present API.  The maximum-12 and TD6
objects are boundary-book/finite-family artifacts without a supplied
`PolynomialNormalClosureData`, subgroup `C`, normalization ring `T`,
primitive `alpha_sec`, evaluated secant-frame coefficient list, section
module `R_C`, and conductor/trace embeddings.  The AS branch is additionally
positive-characteristic or Witt-local, whereas Paper II's specialization is
over `C`.  There is therefore no honest “cheapest exact experiment” yet.
The circular/absent landing map is the map into a common `N/T` followed by
the unproved uniform trace/conductor containment; choosing an existential
nonzero intersection is, by the manuscript's own argument, just boundary
separation in disguise.

## 5. Semantic and trust audit

No `sorry` or `admit` occurs in the Lean sources.  There are exactly three
declared project axioms, all in
`CollisionIdeals/Planar/External/Assumptions.lean`:

- `branchPurityA2`;
- `affinePlaneFiniteEtaleRigidity`;
- `axGrothendieckA2`.

The README discloses these.  The convenience theorems
`planarVanishing_assuming_standardGeometry`,
`planarVanishing_of_movingSheetCoverage`,
`planarVanishing_of_boundarySeparation`, and the automorphism wrappers inherit
some or all of them even when the theorem statement does not list them as
arguments; source-level `#print axioms`, not the surface signature, is the
right trust check.

Other apparent progress is carried as propositions or supplied structures:
`BoundaryCoherenceBridge`, `RamificationRigidityBridge`,
`PlanarMovingSheetCoverage`, `PlanarBoundarySeparation`,
`PlanarNoHiddenInertia`, and `PlanarKellerCollisionModel`.  The latter stores
normal-closure/normalization data plus Keller-to-etale, Keller-to-flat, and
ramification-realization interfaces.  Theorems consuming such a value do not
construct it for every Keller map.

The source is unusually explicit about most manuscript/Lean mismatches in
`SEMANTIC-PARITY.md`: prime-order reduction, the converse fixed-locus
containment, local-cohomology localization, geometric trace-dual finiteness,
common ambient maps, actual overlap coefficients, landing containment, and
the open-section specialization remain missing.  The potentially misleading
phrases are “proved finite Tate--conductor reduction” and “first-jet ideal.”
They are accurate only at the generic algebraic layer: the concrete planar
normalization specialization and first-jet family are not wired.  Paper II's
prose proofs of the DVR pole and boundary statements therefore outrun Lean;
the parity file acknowledges this.  The detailed README inventory is broadly
honest, but readers who inspect only exported consequence names could mistake
explicit inputs or inherited axioms for proved universal geometry.

## Smallest missing implication and allocation

Smallest missing implication on the proposed active route:

`actual evaluated secant-frame overlap data + common N/T landing map`
`=> d.sf_(C,1) <= c.tr_C` (together with the unformalized pointwise DVR pole
test) `=> PlanarBoundarySeparation`.

The universal form reaches an endpoint equivalent to JC2 rather than a
strictly smaller unrestricted theorem.  The newly constructed
`galoisOffDiagonalLiftOfNotMem` stops before this implication.

**Allocation recommendation:** allocate no compute and no client search.
Retain the new conjugate collision-pair/off-diagonal API as a scoped reusable
interface.  Revisit with one bounded algebra task only when a named client
comes with all of: a characteristic-zero polynomial map, explicit finite
normal closure and normalization order, subgroup/sheet data, a primitive
monogenic element, and the actual evaluated overlap coefficients.  The first
gate should be construction of the common `N/T` landing map; do not spend on
denominator or conductor calculations before that map typechecks.
