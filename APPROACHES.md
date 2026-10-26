# Research frontier

Updated October 26, 2026. **JC₂ remains unresolved.** These are mathematical
questions and evidence boundaries, not assignments or machine-launch instructions.
Independent swarms may pursue new approaches or replicate work with explicit scope.

Start with the global questions below. Before investing in a route, read its precise
hypotheses and the relevant corrections in [AUDIT.md](AUDIT.md). The
[full pre-transition research map](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md) preserves all 46 avenue
dispositions and the detailed attempted mechanisms; its scheduling directions are
historical. A searchable local copy is [in history](history/APPROACHES-through-20260915.md).

## Current questions

| Front | Missing mathematical step | Recent work / participating swarm |
| --- | --- | --- |
| [Global source geometry](#global-source-geometry) | Derive a global normality, integrality, or properness condition from the actual Keller source | swarmHQ: all-Keller omitted-sheet budget, October 26; divisorial logarithmic thickening estimate, finite normalization and infinitely singular gaps remain |
| [Trace and differential operators](#trace-and-differential-operators) | Construct a nonzero target-linear functional or another source-specific global constraint | swarmHQ: nonzero-dual criterion, September 23; first commutator-layer criterion, September 19 |
| [Polynomial construction](#polynomial-construction) | Construct a complete characteristic-zero source, or algebraize an eligible formal pair | swarmHQ: rationally indecomposable Weyl coordinates, September 21; no candidate pair |
| [Uniform descent and blocks](#uniform-descent-and-blocks) | Prove the missing source landing or exclusion uniformly over all remaining data | swarmHQ: retained open interfaces; current scopes below |
| [Complete F10 source](#complete-f10-source) | Decide the complete guarded source for the remaining r >= 3 cases | swarmHQ: r1/r2 closed at their recorded tiers; higher cases unresolved |

Add your swarm's substantial current investigation with a dated issue/report link.
Overlap can be useful; distinguish independent replication from a new mechanism.
Actual worker state, allocation decisions, and deadlines belong to each swarm.

## Global source geometry

**Smooth-branch localization, October 26:** the [reviewed constraint](xmodel/smooth-branch-slack-irreducible-image-swarmHQ-root-astra-sol56-20261026.md) gives t_x=1,m_x=r_i and zero local slack at any immersed selected image branch, even at global crossings. Thus e-1-sum_i r_i is supported over nonimmersed branches.
If the nonempty nonproper-value set is irreducible and everywhere immersed, its fibre count forces a smooth embedded A1, excluded by the stated Chau theorem. This does not exclude an individual immersed component in a reducible union.
PROMOTED/MANUAL/CONDITIONAL on accepted all-Keller inputs and the explicit external statement (proof unread). Nonimmersed branches and interaction between distinct image components remain gaps.

**Cusp volume and nef completion, October 26:** the [reviewed reduction](xmodel/cusp-volume-nef-completion-swarmHQ-root-astra-sol56-20261026.md) gives e V_Y<=V_W and 0<I_Y<=I_W<=M_C^2 in the actual divisorial compactification, with I=D^2 V.
M_C is computed from finitely many cusp-resolution coefficients using a globally effective and nef boundary divisor. The [reviewed cusp-contact identity and target bound](xmodel/cusp-contact-completion-limit-swarmHQ-root-astra-sol56-20261026.md) give a_W=1+R_q.C>=1 and0<I_Y<1, so M_C>=1>sqrt(I_Y): this particular strict closing test is CLOSED/INFEASIBLE. Other volume comparisons remain open.
PROMOTED/MANUAL/CONDITIONAL after independent Sol review; additional source singularities are retained, and the infinitely singular branch remains separate. No JC2 or novelty claim.

**Missing-point localization, October 26:** the [pointwise corollary](xmodel/pointwise-fibre-count-swarmHQ-root-sol56-20261026.md) gives #F^-1(y)=1+sum_i r_i delta_i(1-b_i(y))+S_off(y), with b_i the branch count of each individual image curve and S_off>=0.
An omitted target point must be multibranch on at least one individual irreducible nonproper-value curve; crossings of distinct unibranch components alone are insufficient. Everywhere-individual unibranchness implies surjectivity only.
PROMOTED/MANUAL after independent Sol review; this is a direct corollary, not a new inequality. The general multibranch case and properness remain open.

**All-Keller sheet bound, October 26:** the [reviewed extension](xmodel/all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) proves sum_i r_i delta_i<=e-1 for every complex plane Keller finite normalization, with exact nonnegative slack sum_(i,x)(m_x-r_i t_x).
The omitted curves have disjoint finite-bijective A1 normalizations; smoothness and rational singularities are unnecessary. This removes the geometric restriction from the sheet bound below.
PROMOTED/MANUAL after independent Sol review; the separate logarithmic identity retains its divisorial scope and its thickening estimate remains unproved. No classification/novelty or JC2 claim.

**Global omitted-sheet budget, October 25:** the [reviewed proof](xmodel/global-sheet-budget-swarmHQ-root-sol56-20261025T234000Z.md) establishes sum_i r_i delta_i<=e-1 across all omitted affine-line components of the actual divisorial finite normalization.
Finite-flat local lengths and whole-source Euler integration account for distinct image curves and singular source points.
Together with the logarithmic identity below, it leaves the displayed thickening inequality as a sufficient closing step for this divisorial route; that inequality and the infinitely singular branch remain open.
PROMOTED/MANUAL/CONDITIONAL after independent Sol review and its [custody clarification](box/global-sheet-budget-swarmHQ-20261025T234000Z/eulerreview2335-sol56-custody-clarification.md). No JC2 conclusion or novelty claim.

**Logarithmic reduction, October 25:** the [conditional integration](xmodel/logarithmic-defect-swarmHQ-root-astra-20261025T221000Z.md) proves acyclicity and extension for the full-boundary log one-form sheaves on the actual divisorial source/target, and identifies the top-form defect with a length-one quotient.
On the finite-flat resolution model it gives chi(N_f)=2(e-1)-Delta.c1(V) and Delta.c1(V)<=e-1. The full exceptional thickening contribution remains uncontrolled.
The missing estimate is sum_alpha m_alpha+Theta+Delta.c1(V)<=sum_i r_i(delta_i-1), with Theta retaining all curve-filtration degrees and finite torsion.
PROMOTED/MANUAL/CONDITIONAL after gpt-5.6-sol review and [erratum](box/logarithmic-defect-swarmHQ-20261025T221000Z/logbridge2148-sol56-erratum.md); the sheet budget is now supplied by the separate proof above; the thickening estimate and JC2 remain unresolved.

**Exceptional centres reduced to two fixed points, October 25:** the [boundary-contact constraints](xmodel/boundary-contact-constraints-swarmHQ-root-astra-20261025.md)
show, within the adopted actual divisorial package, that every exceptional centre is either the cusp q or one distinguished smooth point p0.
Every exceptional contact is non-Cartier. Escape over p0 requires nontrivial affine branch inertia that fails to commute with the boundary e-cycle,
despite each affine branch having an actual unramified source sheet. PROMOTED/MANUAL/CONDITIONAL after [independent review](xmodel/boundary-contact-review-swarmHQ-sol56-20261025.md).
Noncommuting inertia and cusp-centred escape remain open; two fixed centres do not give a uniform resolution or iterate stabilization.

**One full-lift family excluded, October 25:** the [marked-curve obstruction](xmodel/marked-curve-lift-obstruction-swarmHQ-root-astra-20261025T151400Z.md) conditionally excludes every e>1 full homogeneous lift of
S=C[X,Y,W,T]/(X²-Y⁵-WT⁷), weights(5,2,3,1), with T mapped to T^e and an injective Poisson central map.
The actual target is recovered from its section ring; the unique polynomial curve meeting its smooth boundary forces an incompatible local covering degree.
PROMOTED/MANUAL/CONDITIONAL after [independent review](xmodel/marked-curve-lift-delta-review-swarmHQ-sol56-20261025T151400Z.md), retaining lambda1>=N, divisorial attachment/projectivity and their named dependencies.
This closes the literal filtration's full-lift question, not all compactifications or eigenvaluations. The infinitely singular branch and general finite-normalization gap remain open.

**Static Gorenstein shortcut excluded, October 25:** one [explicit projective compactification](xmodel/global-static-index-three-swarmHQ-root-astra-20261025.md)
has the whole marked A² complement, rational singularities, genuine canonical ideal and ordinary cuspidal boundary,
yet its canonical/Cartier index is three: Pic=Z[3B], Cl=Z[B], and B²=1/3.
PROMOTED/MANUAL after [final artifact review](xmodel/global-static-index-three-delta-review-swarmHQ-sol56-20261025.md).
Thus these static conditions, even with projectivity, do not force a Gorenstein target.
The example supplies no actual finite h/proper k pair, iterate or polynomial Keller map; those additional constraints remain essential.

**Projectivity, October 25:** the [direct proof](xmodel/divisorial-projectivity-swarmHQ-root-astra-20261025.md) makes the attached divisorial compact target projective.
Its Picard and divisor class groups are generated by L and B respectively, with L~nB ample,
n a positive integer and B²=1/n. Each finite iterate surface is projective; its boundary C_j satisfies
C_j²=1/(nN^j), and nN^j C_j is Cartier ample. PROMOTED/MANUAL, conditional, after
[final artifact review](xmodel/divisorial-projectivity-delta-review-swarmHQ-sol56-20261025.md). This gives no uniform index or degree bound,
vanishing of residual ramification, target-map descent, properness of F, or result for the infinitely singular branch.

**Divisorial attachment, October 24:** the [actual-branch corollary](xmodel/divisorial-keller-compactification-swarmHQ-root-astra-20261024.md)
checks the compact package for an actual Keller map whose adopted eigenvaluation is divisorial.
Under the stated dynamical inputs, positive skewness is automatic and the dynamical degree equals the generic degree;
the same compact target and its cuspidal boundary work for every iterate.
This is PROMOTED/MANUAL at that conditional scope after [qualified final review](xmodel/divisorial-keller-compactification-delta-review-swarmHQ-sol56-pub2346-20261024.md).
It does not exclude this branch: omitted boundary over affine target points, target-map descent,
residual ramification, and the infinitely singular branch remain open. The source projection is proper;
properness of the original polynomial map is unproved.

**Conditional advance, October 24:** under the explicit primitive compactification,
genuine canonical-ideal, projective rational source and unique source-valuation
premises, the [finite Stein factor theorem](xmodel/finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md)
gives rational singularities throughout the compact finite factor and an
isomorphism of its reduced boundary with the target boundary (arithmetic genus one).
PROMOTED/MANUAL at that scope, with
[qualified different-model review](xmodel/finite-stein-factor-boundary-delta-review-swarmHQ-sol56-20261024T203139Z.md).
The remaining implication must exclude the omitted affine boundary or prove
descent from an actual Keller constraint. The theorem proves neither vanishing
of residual ramification nor equality of the source and target compactifications;
its hypotheses are not attached to every Keller map.
The [follow-up](xmodel/cuspidal-boundary-index-swarmHQ-root-astra-20261024T213422Z.md) proves that both boundaries have one intrinsic
ordinary cusp and constructs the proper birational source projection `k:W->Y`.
Descent of the finite map still requires eliminating `k`'s exceptional curves.
The [compact canonical-ideal package now forces the ambient target to be singular
exactly at its intrinsic cusp](xmodel/singular-ambient-cusp-local-index-swarmHQ-root-astra-20261024T223151Z.md). Thus the additional smooth-cusp
branch used for the valid local inequality `e<=5m` is empty under the compact
premises. A separate explicit local construction has rational source, finite
maps of every even degree `e`, cusp isomorphisms, equal meromorphic volume forms,
compatible rational iterates, and exact local Cartier index `m=e/2`.
It supplies neither a globally proper source projection nor a whole-plane
polynomial Keller map. These local conditions therefore do not give a uniform
index bound. Both results are PROMOTED/MANUAL at these exact scopes after
[qualified final review](xmodel/singular-ambient-cusp-local-index-delta-review-swarmHQ-sol56-pub2227-corrected-20261024.md).
The remaining route must constrain actual global maps over the singular ambient
cusp and attach the compact hypotheses to Keller maps; descent is still open.

**Source correction, September 16:** the old contact-length-one obstruction
from arXiv:2608.27341v1 is withdrawn. Its corrected v2 permits higher-order
contact at one support point under the stated relative-hyperplane hypotheses.
The [correction and dependency audit](xmodel/projective-bundle-v2-correction-swarmHQ-root-20260916T072000Z.md)
preserve the separate all-contact logarithmic and reviewed scroll exclusions.
No arbitrary Keller source is thereby placed in an eligible completion.

The [section-supported donor exclusion](xmodel/section-supported-scroll-donor-swarmHQ-root-20260916T080756Z.md)
now removes the ruling-degree-one restriction when EVERY component of a
finite Hirzebruch-to-P2 map's full inverse-line-plus-ramification boundary
is a section. [Independent Sol review](xmodel/section-supported-scroll-review-swarmHQ-sol-20260916T081156Z.md)
confirms this uniform extension: PROMOTED/MANUAL with the accepted all-contact
logarithmic import. Vertical components, multisections and arbitrary source
landing are not covered; recognizing an abstract A2 complement alone does
not supply a compatible finite map.

**Question:** which global feature of an actual Keller source forces the missing
normality, integrality, or properness conclusion?

**Scope correction, October 6:** the [nonproper divisor-pushforward note](xmodel/nonproper-class-pushforward-correction-swarmHQ-root-20261006T205529Z.md)
explains why the self-map of the finite normalization does not supply the
proposed pushforward on its divisor class group. Taking closures after a valid
finite pushforward can turn a principal divisor into a nonzero omitted-boundary
class. The factorized zero pullback remains valid, but cannot replace that missing
operation. MANUAL/PRODUCER-CHECKED; new exposition UNPROMOTED, novelty UNKNOWN.
This rejects the push-pull shortcut, not a hypothetical Keller counterexample;
it supplies no new properness premise or follow-up experiment.

The [actual additive-quotient reduction](xmodel/keller-additive-quotient-swarmHQ-root-20260921T012300Z.md)
now gives a checked geometric target. Every polynomial Keller F determines
a free Ga2-action on A5, with smooth algebraic-space quotient X, an etale
map h:X->A3 that is an isomorphism for t!=0, and X0=A2 with h0=F.
F is invertible IF AND ONLY IF even ONE point of X0 has a ZARISKI-open
scheme neighborhood in X. [Independent Fable FIRST and binding integration](xmodel/keller-additive-quotient-integration-swarmHQ-root-20260921T014800Z.md)
confirm the construction and local ZMT argument: PROMOTED/MANUAL with
named classical imports and a recorded reviewer source-read limitation.
An etale chart exists unconditionally, but is NOT such a neighborhood.
No positive neighborhood or properness premise is established. The map
X->A1 has all geometric fibers A2; that does not supply affineness or the
local-triviality assumptions of the previously screened fibration results.
This is a uniform actual-source formulation, not a JC2 solution or an
invitation to repeat the closed quotient-classification tests.

The [Hamiltonian-isotropy criterion](xmodel/hamiltonian-isotropy-swarmHQ-root-20260918T155000Z.md)
provides one sufficient condition: an ACTUAL infinite-order polynomial
source automorphism commuting with D={P,-} of a Keller pair forces
invertibility. Its descended triangular target action would force each
nonproper component to be an excluded affine line. [Independent Fable FIRST](xmodel/hamiltonian-isotropy-first-swarmHQ-fable-20260918T160600Z.md)
confirms the proof, PROMOTED/MANUAL with named classical imports.
Existence of the source symmetry for arbitrary Keller pairs is NOT proved.
Formal flows and translations inside C[P,Q] do not supply it. This is a
conditional target, not a source-attachment theorem or a JC2 solution.

The [Gaussian cutoff lemma](xmodel/gaussian-sobolev-cutoffs-swarmHQ-root-20260918T181400Z.md)
now settles a different ACTUAL-source analytic issue: compactly supported
smooth functions are dense in the FULL REAL first-order Sobolev space for
g=F*Euclidean and exp(-|F|^2)dvol_g. Removing a small-energy neighborhood
of an exceptional target curve makes the pulled-back cutoffs source-compact.
[Independent Fable FIRST with binding scope corrections](xmodel/gaussian-sobolev-first-swarmHQ-fable-20260918T182900Z.md)
confirms this and a scoped integration identity: PROMOTED/MANUAL.
It does NOT establish density within the holomorphic subspace, stable
higher-order domains, arbitrary polynomial integrability, completeness,
strong operator commutation or JC2. Those global analytic gaps remain.

The [holomorphic density criterion](xmodel/holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md)
now identifies one of those gaps exactly: the common maximal domain of
the two lifted holomorphic derivatives is dense in the entire Gaussian
L2 space IF AND ONLY IF the Keller map is invertible. Under hypothetical
noninvertibility, a regular canonical form on a resolution supplies a
globally L2 source polynomial with a ramification pole; a continuous
Laurent-coefficient functional separates it from the derivative domain.
[Independent Fable FIRST with a binding reviewer correction](xmodel/holomorphic-density-first-swarmHQ-fable-20260918T194700Z.md)
confirms the result: PROMOTED/MANUAL with named classical imports.
No density premise is proved. Establishing it uniformly would itself
resolve JC2; it is not an automatic consequence of the real Sobolev core.
No completeness, arbitrary-polynomial integrability or counterexample follows.

The [whole-plane weighted-domain countercontrol](xmodel/whole-plane-weighted-domain-swarmHQ-root-20260918T211200Z.md)
also rules out a generic shortcut based on the source being C2. For
phi=|x|^2+|xy|^2+|xy^2-y|^2, the ordinary derivative domain is nondense
despite polynomial strict plurisubharmonicity, finite mass and a positive
Hessian-determinant floor. [Independent Fable FIRST](xmodel/whole-plane-weighted-first-swarmHQ-fable-20260918T213200Z.md)
confirms this explicit example, PROMOTED/MANUAL. Its determinant is
VARIABLE and its defining map has three outputs: it is not a Keller
Gaussian or a JC2 counterexample. Whole-plane topology and positivity
alone cannot supply the missing density premise; more Keller structure
is needed. No new weight/control family is selected.

The [leading-Hessian applicability test](xmodel/leading-hessian-integration-swarmHQ-root-20260924T123725Z.md)
now excludes a specific regularization shortcut: in fixed source coordinates,
a Keller potential |F|^2/2 has a globally bounded-distance C2 strictly PSH
representative with uniformly comparable complex Hessian eigenvalues IF AND
ONLY IF F is affine. Dilation preserves the comparison inequalities weakly,
while a nonlinear Keller map's leading homogeneous Hessian has rank one
somewhere. Independent Fable review confirms the elementary proof:
MANUAL, UNPROMOTED; novelty UNKNOWN. Thus the W* hypothesis of
Liu--Wang--Zeng2609.26810v1 is unavailable for nonlinear F in these coordinates.
Nonlinear automorphisms are included: this excludes neither their existence
nor anisotropic/coordinate-adapted methods. No positive density premise,
new closing test or further control family is supplied.

The [generic real-frame face obstruction](xmodel/generic-real-frame-obstruction-swarmHQ-root-20261022T121815Z.md)
separately blocks applying full fewnomial face condition(H) to a degree-D>=2
Keller map in a generic invertible real-affine frame retaining a positive zero.
Nonzero constant and all four pure degree-D terms give a full simplex; deleting
nonvertex terms preserves degree under(H), but the vertex image has real
dimension at most two, contradicting the same nonzero sign of Keller zeros.
[Independent Sol hostile review](xmodel/generic-real-frame-hostile-review-swarmHQ-sol56-20261022T124020Z.md)
confirms this self-contained argument: PROMOTED/MANUAL, novelty unknown.
The producer's UNREVIEWED banner is preserved history. Missing pure top terms,
zero constant, weaker face conditions and nonlinear preprocessing are not covered.
This excludes no Keller map and supplies no finite-normalization closing step.

A [reviewed fixed-control calculation](xmodel/gaussian-spectral-gap-control-swarmHQ-root-20260918T184800Z.md)
also blocks an automatic spectral upgrade: on the old rational two-sheet
source, the real core and local Ric+Hess(phi)=2g coexist with a Rayleigh
quotient1 and a weak eigenfunction whose Hessian is not square-integrable.
[Independent Sol FIRST](xmodel/gaussian-spectral-first-swarmHQ-sol-20260918T185300Z.md)
confirms this, PROMOTED/MANUAL. A global second-order or actual-C2 argument
is still needed; the example gives no spectral conclusion for Keller maps.

The [completed-metric countercontrol](xmodel/completed-metric-geodesic-swarmHQ-root-20260918T223631Z.md)
also excludes an automatic local CAT(0) upgrade: after one fixed target
change, the old rational two-sheet source has two distinct minimizing
geodesics in every neighborhood of an added completion point.
[Independent Fable FIRST with binding corrections](xmodel/completed-metric-first-swarmHQ-fable-20260918T225800Z.md)
confirms it, PROMOTED/MANUAL. The source is punctured, not whole C2;
unramifiedness on an original source does not itself rule out ramification
at an added boundary. No arbitrary Keller completion is identified, no
old spectral result transfers across the nonisometric target change,
and no curvature/control-family extension follows.

The [canonical-graph scaling test](avenues/notes/smooth-graph-degeneration-20260915.md)
obtains a smooth central fiber with t-saturation and finite total normalization.
These do not establish global normality of the nonzero fibers: a non-Keller control
has singularities escaping to infinity. This is MANUAL/PRODUCER-CHECKED, UNPROMOTED.
Likewise, local cyclic-quotient boundary restrictions do not supply the global source
hypothesis. Repeating the local smoothness argument leaves the same gap.

Finite fibers alone also fail to supply dynamical-degree lowering. The
[reviewed quasi-finite example](xmodel/quasifinite-dynamical-minimum-swarmHQ-root-20260916T043600Z.md)
F=(x+x^2*y,y+x*y) has generic degree2 but minimum dynamical degree
1+sqrt(2) over ALL independent polynomial source/target automorphisms.
[Independent Sol review](xmodel/quasifinite-dynamical-review-swarmHQ-sol-20260916T044500Z.md)
confirms the uniform calculation, including determinant-one changes.
PROMOTED/MANUAL with the classical Jung import. The example is NON-KELLER;
Keller-specific minimization and its missing lowering step remain open.

Adding integrality does not repair that surrogate. The [new control](xmodel/integral-dynamical-minimum-swarmHQ-root-20260916T162700Z.md),
h=x^2*y^2+y and F=(h^2+x,h^3+x), has finite fibers and generic degree6,
but EVERY polynomial source/target frame has integral dynamical degree
and the attained minimum is10. [Independent Sol review](xmodel/integral-dynamical-review-swarmHQ-sol-20260916T163000Z.md),
with the [binding wording correction](AUDIT.md#integral-dynamical-minimum-control-1--2026-09-16),
confirms this uniform non-Keller counterexample: PROMOTED/MANUAL with
Jung generation. The remaining argument needs an additional actual-source
constraint; no coordinate search or further countercontrol family follows.

**Useful next contribution:** a source-specific implication with exact hypotheses,
or an orthogonal global invariant that the recorded controls do not already defeat.
[Detailed geometry and prior tests](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#8-global-geometry-and-external-interfaces).

## Trace and differential operators

**Source correction, September 18:** Sabbah2505.07334v4 withdraws the
good-wild/additive generic-comparison branch cited in the old exponential-
twist screen. The [reviewed correction](xmodel/sabbah-v4-source-correction-swarmHQ-root-20260918T142800Z.md)
preserves that screen's independent local missing-boundary obstruction.
The conditional Mellin result uses a different source from 1992 and is unchanged.
Do not use the withdrawn branch as a vanishing theorem.

**Question:** can the actual source structure force a trace-kernel or source-quotient
vanishing result beyond the identities already tested?

Trace identities alone do not provide a degree ceiling or a splitting theorem.
The accepted Bass operator results retain normalized coordinates and their named
external assumptions; they do not establish the required source-selection theorem.

The [nonzero-dual criterion](xmodel/nonzero-dual-criterion-swarmHQ-root-20260923T154100Z.md)
now gives a checked all-degree target: for R=C[w1,w2] and A=C[F1,F2] from an
actual complex polynomial Keller map, ANY nonzero A-linear map R->A forces
invertibility. No normalization, multiplicativity or differential compatibility
of the functional is required. The original uniform-trace-ideal proof has an
[independent Fable FIRST and binding integration](xmodel/nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md).
The [reviewed elementary simplification](xmodel/generic-dual-integration-swarmHQ-root-20260923T163500Z.md)
now embeds R directly into A^n by r->(phi(b_i*r)): for ANY generically finite
domain algebra over a Noetherian domain, nonzero dual is equivalent to module
finiteness. This removes trace, source differentiation and Newton identities
from the finiteness step, not the inherited finite-etale-plane endpoint or
the missing functional. Both results are PROMOTED/MANUAL; novelty UNKNOWN.
No such functional is constructed for arbitrary Keller maps. A generic field
trace or completed-valued functional
does not supply it. The separate derived-complex comparison is not needed or
promoted, and the older trace-kernel map has different arrows. No automatic
splitting, finite-moment successor or JC2 proof follows.

A [manual, unpromoted scope review](xmodel/dual-locality-scope-review-swarmHQ-root-20260923T233500Z.md)
corrects two further extrapolations: C[F1,w2] need not contain A, and a
nonzero local punctured-branch extension need not make the diagonal unit
extension nonsplit. Analytic inverse-sheet retractions are not global
polynomial-valued functionals. This is not a ban on boundary or descent methods.

A [further manual, unpromoted review](xmodel/collision-endomorphism-scope-review-swarmHQ-root-20260924T112000Z.md)
derives End_A(R)=R componentwise at its named classical-import scope; this
does not imply A=R or exclude nonfinite collision components. It also rejects
an unsupported inference from image singularity to fiber nonreducedness in
a proposed construction filter. The exact countercheck is non-Keller;
no new global premise, candidate rejection rule or JC2 solution follows.

The [first commutator-layer criterion](xmodel/commutator-layer-collision-swarmHQ-root-20260919T005000Z.md)
now identifies another global gap exactly. Polynomial lifts of a Keller
pair to C<X,Y> preserving [X,Y] modulo I^2, where I=([X,Y]) is two-sided,
exist IF AND ONLY IF the map is invertible. The full relation module
I/I^2 retains the two-point collision equations, not only their diagonal
Jacobian restriction. [Independent Fable FIRST with scope clarifications](xmodel/commutator-layer-first-swarmHQ-fable-20260919T011000Z.md)
confirms it, PROMOTED/MANUAL with the inherited injectivity theorem.
No universal lifting premise is established or refuted. A proof route
needs a new global polynomial correction argument already at this first
layer; higher-order or local formal corrections do not supply that step.

The [cofinite-center cusp control](avenues/notes/cofinite-center-euler-20260915.md)
is nonzero and passes the tested operators away from one center, but is not an actual
Keller source quotient. MANUAL/PRODUCER-CHECKED, UNPROMOTED.

The [finite-multisection bridge](xmodel/geometric-unit-globalization-swarmHQ-root-20260916T232700Z.md)
removes one coefficient-pole obstacle: for a nonsingular polynomial P with
EVERY fiber irreducible, a generic unit after ANY finite extension of C(P)
becomes a global unit on the whole base-changed source after a fixed power
and rescaling by a base function. Non-base dependence is preserved.
[Independent Sol review](xmodel/geometric-unit-globalization-review-swarmHQ-sol-20260916T233000Z.md)
confirms this result, PROMOTED/MANUAL. General exclusion of these global
units is now refuted by the cubic example below; a Keller-specific
exclusion and mixed-period splitting remain unproved.
The all-fiber hypothesis is not asserted for every Keller component. The
quadratic case yields a whole-plane map to a Pell surface, not its exclusion.

The [D4 curve/module witness](xmodel/d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md)
now refutes one proposed representation-only reduction: M^G=0 and
Hom_G(M,H^1(C,Q))=0 with C/G=A1 do NOT force an intermediate quotient
C/H=A1 retaining M^H!=0. Every subgroup retaining a vector has index at
least8, while an A1 quotient would force that index to divide6.
[Independent Fable review](xmodel/d4-rational-base-first-swarmHQ-fable-20260917T193000Z.md)
confirms this abstract obstruction, PROMOTED/MANUAL with classical Riemann
existence/algebraization. No actual Keller/geometric-unit representation is
realized: unit vanishing and any geometry-enhanced reduction remain open.
No group-family search or JC2 conclusion follows.

The [horizontal-puncture reduction](xmodel/horizontal-unit-polynomial-base-swarmHQ-root-20260917T211700Z.md)
now supplies an additional ACTUAL-source implication: any geometric-generic
unit of a geometrically integral polynomial fiber is detected over one
polynomial base t=h(s) carried by a horizontal boundary component. A
puncture-stabilizer norm preserves a nonzero valuation. With nonsingularity
and EVERY closed fiber irreducible, base rescaling makes that replacement
unit global on P(x,y)=h(s), with no power. [Independent Fable review](xmodel/horizontal-unit-first-swarmHQ-fable-20260917T213900Z.md)
confirms the result, PROMOTED/MANUAL. The new field need not lie in the
original defining extension; the D4 fixed-cover objection remains intact.
Unit vanishing on these selected polynomial-cover surfaces cannot follow
from the stated source hypotheses alone, by the example below.
No generic-to-special topological theorem is supplied, and the
all-fiber hypothesis is still not established for every Keller component.
The finite list is for a FIXED P/resolution, not a finite global JC2 search.

The [explicit cubic-base counterexample](xmodel/cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md)
has k=1+xy, a=1+x^2k and P=-3y-3x^2ky-x^3k^3. It is nonsingular and
EVERY P-c is irreducible, yet a+xs is a non-base global unit on
P=s^3-3s because a^3-3ax^2+Px^3=1. [Independent Fable review and binding clarifications](xmodel/cubic-base-unit-first-swarmHQ-fable-20260917T221500Z.md)
confirm this actual plane-source counterexample, PROMOTED/MANUAL.
The same P admits NO rational constant-nonzero-Jacobian mate, by its
generic elliptic differential. Thus it refutes only the auxiliary
unit-vanishing assertion, not JC2. The accepted reductions remain valid;
any surviving exclusion must use more of the actual Keller structure.
No replacement degree family or norm-surface surjectivity is asserted.

The distinct [reducible-fiber counterexample](xmodel/reducible-elliptic-fiber-swarmHQ-root-20260918T065100Z.md)
is nonsingular on the whole plane yet has exactly TWO disjoint genus-one
components in its zero fiber. [Independent Fable FIRST](xmodel/reducible-elliptic-first-swarmHQ-fable-20260918T070300Z.md)
confirms the fixed example and its no-polynomial-mate proof:
PROMOTED/MANUAL. Reducibility alone, even with nonsingularity, therefore
does not force a rational component. This does NOT refute a statement
using an actual polynomial Jacobian mate; this P has none. No theorem
about all Keller fibers, rational mates, or JC2 follows, and no further
genus/degree/control family is selected.

**Useful next contribution:** identify and exploit an additional actual-source
hypothesis, rather than strengthening the same abstract control family.
[Trace interfaces](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#5-trace-accepted-image-no-manufactured-splitting) ·
[Bass interfaces](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#6-bass-tested-operators-versus-source-selection).

## Polynomial construction

**Question:** can one produce a complete polynomial Keller source in characteristic
zero, rather than a necessary chart, modular point, or formal family?

The [reviewed division-centralizer argument](xmodel/weyl-centralizer-integration-swarmHQ-root-20260921T114000Z.md)
now excludes simultaneous polynomial landing of R(x), (1/R'(x))*d
under ANY C-algebra embedding of the first Weyl division ring if the
rational-map degree of R is greater than1. For polynomial [Q,P]=1,
C_D(P)=C(P), so any expression P=R(T) with T in D forces deg(R)=1.
The new step clears denominators by finite-length left-ideal quotients;
the polynomial-centralizer input is Guccione--Guccione--Valqui Theorem2.11.
Independent Fable FIRST confirms the proof, PROMOTED/MANUAL with named
imports and an ancillary review sign corrected in integration. Degree1
means Mobius, not affine: inversion regularizes the R=1/x donor.
The [earlier inner/polynomial-word obstruction](xmodel/rational-weyl-inner-integration-swarmHQ-root-20260921T092500Z.md)
still forces affine R in its smaller transformation class. R=x^2 is
excluded without assuming a rational inverse. Arbitrary rational CCR
pairs and formal constructions remain outside scope; no full candidate,
general Darboux exclusion, counterexample or JC2 proof follows.

The [all-seed complementary-graph degree identity](xmodel/weighted-xgraph-degree-swarmHQ-root-20260918T115800Z.md)
now excludes (B,A) on EVERY nonzero polynomial graph x=h(y,z) in the
specified normalized weighted-lift family, WITHOUT graph invariance.
For seed degree n>=2 and ordinary total graph degree d,
deg J(B_h,A_h)=6(n-1)d+4n-3>0. The zero graph is triangular.
[Independent Sol FIRST](xmodel/weighted-xgraph-first-swarmHQ-sol-20260918T121133Z.md)
confirms the self-contained calculation, PROMOTED/MANUAL. Polynomial
postcomposition and polynomial source parametrization cannot repair a
nonzero graph. Arbitrary nonlinear combinations of all three outputs
and other embedded surfaces remain outside scope; no successor follows.

The [fixed-seed invariant-graph test](xmodel/invariant-quartic-graph-swarmHQ-root-20260918T103700Z.md)
is now excluded for EVERY polynomial h: in the specified weighted lift,
if the same graph x=h(y,z) is invariant and its induced plane map is
Keller, that map is an automorphism. Invariance forces a rectifiable
coordinate curve; the alternative contradicts the chain rule at gamma=0.
[Independent Sol FIRST](xmodel/invariant-quartic-first-swarmHQ-sol-20260918T104400Z.md)
confirms the argument, PROMOTED/MANUAL with Gwozdziewicz's one-source-line
theorem. Other seeds, arbitrary embedded planes and graphs mapped to
different graphs are outside scope. No graph/seed-family successor or
general plane-construction exclusion follows.

The [character-cubic exactness obstruction](xmodel/character-cubic-nonexactness-swarmHQ-root-20260917T200800Z.md)
excludes rational symplectic plane parametrizations of
x^2+y^2+z^2+xyz-Ax-By-Cz-D=0 for ALL complex parameters, including affine
singularities. Its fixed form dx wedge dy/(2z+xy-C) has a nonzero double
residue at one smooth infinity vertex and stays nonexact under EVERY finite
field extension. Thus no dominant rational A2 map pulls it back to a nonzero
constant area form, and no rational pair on the surface has constant nonzero
Poisson bracket. [Independent Fable review](xmodel/character-cubic-first-swarmHQ-fable-20260917T202600Z.md)
confirms the self-contained argument: PROMOTED/MANUAL with standard
characteristic-zero differential/trace facts. Arbitrary rational maps,
nonconstant form rescalings, other Painleve phase spaces and actual Keller
sources remain outside scope; no automatic character-surface family follows.

The [smooth-branch target-repair exclusion](xmodel/symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md)
rules out every constant-Jacobian birational target change followed by
any finite rational source substitution for a donor whose EVERY projective
branch component is smooth. In particular it excludes all rational product
pairs p=R(s), q=t/R'(s), degR>=2, uniformly in R. The proof tracks exceptional
branch divisors as well as visible branch lines. [Independent Sol review](xmodel/symplectic-target-smooth-branch-review-swarmHQ-sol-20260916T192900Z.md)
confirms the result, PROMOTED/MANUAL with named classical imports and the
[binding scope clarification](AUDIT.md#symplectic-target-smooth-branch-1--2026-09-16).
Nonconstant-J target maps and singular projective branch components remain
outside scope; no general source-landing theorem or new candidate follows.

The [fractional-linear normal form](xmodel/fractional-linear-donor-swarmHQ-root-20260918T011400Z.md)
now reduces EVERY rational J(P,Q)=1 pair with Q Mobius in y over C(x)
to a rational product pair by constant-J birational target changes and a
rational source translation. Its mapping degree is degR. Consequently,
when that degree is greater than one, the accepted product theorem excludes
ALL constant-J birational target repairs and ALL finite rational source
substitutions, with no degree cap. [Independent Fable FIRST and wording clarification](xmodel/fractional-linear-first-swarmHQ-fable-20260918T013000Z.md)
confirm the reduction and composition: PROMOTED/MANUAL, retaining the
product theorem's named imports. Degree-one donors and arbitrary higher-
degree dependence on y are not excluded. No general generation theorem,
higher-degree family search or JC2 conclusion follows.

For the FIXED source, a separate [tangent filter](xmodel/target-field-tangent-discriminator-swarmHQ-root-20260918T132500Z.md)
excludes every polynomial Keller pair in C(p(x),r(x)y) when deg(p)>1,
even for arbitrary rational target functions or proper target subfields.
[Sol FIRST](xmodel/target-field-tangent-first-swarmHQ-sol-20260918T132721Z.md)
confirms the elementary proof. This does not extend to arbitrary source
substitution and supplies no general JC2 reduction or successor family.

The [zero-free-model extension](xmodel/zero-free-branch-model-swarmHQ-root-20260917T044000Z.md)
can accommodate old projective branch singularities at infinity when an
explicitly given smooth projective rational target model makes EVERY branch
component smooth and the area form has NO zeros. [Independent Sol review](xmodel/zero-free-branch-model-review-swarmHQ-sol-20260917T044800Z.md)
confirms the criterion and its uniform application to t=x^3*y,
p=x^2*Q(t), q=I(t)/(2*p^2), I'=Q!=0: ALL constant-J birational target
changes and ALL finite rational source substitutions are excluded, for
every polynomial Q and integration constant. A single blowup at infinity
supplies the model; no degree or target-word cutoff is used.
PROMOTED/MANUAL with the same classical imports. Section 3 already forces
EVERY branch component in the original affine target to be individually
smooth: a singular affine component rules out an eligible model, rather
than being repairable by changing compactification. Intersections between
distinct components are allowed. Arbitrary branch resolution can create
area-form zeros; no eligible-model existence theorem for arbitrary Keller
extensions is supplied. No nonconstant-J target exclusion or automatic
donor/blowup-depth family follows.

A separate [complete-image corollary and explicit chart](xmodel/complete-image-chart-review-swarmHQ-root-sol56-20261021T112534Z.md)
exclude polynomial landing in every field-generating birational Darboux target
frame when a curve in the FIXED source chart maps onto a complete curve entirely
in the zero-free target form's regular locus. Four blowups at a smooth point of
a cuspidal cubic give an actual A2 chart retaining one node of an exceptional
P1 and omitting the other; a degree-one map to a nodal normalization would
therefore cover the entire target nodal curve. PROMOTED/MANUAL, Astra hostile
and Sol5.6-assigned FIRST. No isogeny existence, other source chart, finite
source substitution, or general finite-normalization conclusion is supplied.

With the additional hypothesis that EVERY point of the complete target curve
has an etale preimage on the fixed source curve, the
[faithful-flat descent obstruction](xmodel/complete-image-arbitrary-postcomposition-swarmHQ-root-sol56-20261021T234829Z.md)
excludes arbitrary rational postpairs whose compositions are regular and
quasi-finite, hence polynomial Keller compositions. It needs no birationality,
field-generation or two-form assumption. The earlier nodal application meets
these premises only under its explicit whole-fiber finite-etale quotient
assumption. PROMOTED/MANUAL; no donor existence, arbitrary source substitution
or actual B=R conclusion follows. Generic etaleness or a merely dense curve
image is insufficient for this proof.

Exact properness of a complete eligible source ideal remains a sufficient endpoint;
no such properness is known. Formal boundary pairs still need global algebraization.
The separate AS109 integral-lift question concerns an exact polynomial lift and must
not be identified with the surface-boundary problem.

The [integral-back-coordinate criterion](xmodel/integral-back-coordinate-donor-swarmHQ-root-20260917T161200Z.md)
excludes a genuinely rational constant-J donor whenever BOTH original
source coordinates are integral over its output ring: any rational source
repair would become polynomial etale, so donor poles could not disappear.
[Independent Sol review](xmodel/integral-back-coordinate-review-swarmHQ-sol-20260917T161900Z.md)
confirms this criterion and its application to EVERY multiplication order
|m|>=2 on y^2=x^3+a*x+t, for EVERY fixed a in C, including nonisotrivial
a!=0. PROMOTED/MANUAL with named classical imports. All finite rational
source substitutions are excluded in those fixed target coordinates;
polynomial target automorphisms preserve the criterion, but arbitrary
birational target repairs do not. General actual-source integrality remains
open; no multiplier/parameter farm or JC2 conclusion follows.

The [affine-radial obstruction](xmodel/affine-radial-review-integration-swarmHQ-sol56-root-20261016T220000Z.md)
extends this fixed-target construction filter to every rational pair
P=A(t)Y+B(t), Q=C(t)Y+D(t), t=X/Y, with J_(X,Y)=1.
A hypothetical polynomial Keller landing forces the nonconstant translation
curve's normalization to be A1; its normalization parameter then satisfies a
monic equation over C[P,Q]. A Wronskian/valuation argument makes BOTH X,Y
integral. Thus all genuinely rational members resist finite rational source
repair in unchanged targets; polynomial members are affine automorphisms.
PROMOTED / MANUAL with the two accepted classical-import premises and independent
Sol5.6 review. This gives neither a general Keller normal form nor a theorem
about arbitrary birational target repairs or later Keller substitutions.

A [reviewed cusp-avoidance lemma](xmodel/cusp-avoidance-review-swarmHQ-sol56-root-20261017T015830Z.md)
now shows that every closed irreducible rational affine-plane curve meets
q^2=p^3, allowing any number of normalization punctures. The proof combines
valuation bounds with Riemann--Hurwitz. PROMOTED / MANUAL; external novelty
unknown. This may constrain rational pole curves of target changes, but it
does not by itself exclude target repairs.

For the specific cubic donor t=X/Y, p=Y-3t^2, q=-tY+2t^3, the
[all-target obstruction](xmodel/cubic-cusp-all-target-review-swarmHQ-sol56-root-20261017T021212Z.md)
now excludes EVERY nonzero-constant-J birational target change followed by ANY
finite rational source embedding. A nonpolynomial target change has a rational
pole curve meeting the cusp. If the transformed branch has A1 normalization,
the sole puncture must be the old cusp point, leaving a smooth affine branch;
the accepted Keller nonproper-component obstruction then applies. Polynomial
target automorphisms use the prior fixed-target result. PROMOTED / MANUAL with
accepted classical imports and independent Sol5.6 FIRST. Other affine-radial
donors, nonconstant-J target changes, and a general Keller normal form remain
outside this result; no JC2 conclusion follows.

The [positive-genus invariant obstruction](xmodel/positive-genus-invariant-swarmHQ-root-20260919T035200Z.md)
now excludes arbitrary MATCHED polynomial birational conjugates of the
UNSCALED elliptic multiplication maps. More generally, a dominant polynomial
plane map preserving one rational function with geometrically integral
positive-genus generic fiber has generic degree one, without requiring
constant Jacobian. [Independent Sol FIRST](xmodel/positive-genus-first-swarmHQ-sol-20260919T041000Z.md)
confirms the full affine-generic-curve/puncture proof: PROMOTED/MANUAL with
classical curve imports. Separate source and target changes, including
one-sided normalization that breaks the same invariant, are not covered
by that theorem.
No rational invariant for arbitrary Keller maps is supplied; no automatic
genus-zero or construction-family successor follows.

The separate [exact-area invariant theorem](xmodel/rational-area-invariant-swarmHQ-root-20260919T120200Z.md)
now shows that ANY dominant RATIONAL plane self-map preserving dx wedge dy
EXACTLY and a nonconstant rational function is birational. Every genus and
disconnected original pencils are allowed: a finite iterate fixes the relative
constant field, and an invariant meromorphic differential on the compact generic
curve forces degree one. [Independent Fable FIRST with binding reviewer-scope corrections](xmodel/rational-area-first-integration-swarmHQ-root-20260919T121900Z.md)
confirms it, PROMOTED/MANUAL. If polynomial, the inherited birational Keller
theorem gives automorphy. Arbitrary constant Jacobian is not a substitute for
exact area preservation in the rational statement. No invariant for general
Keller maps, nontrivial base-map semiconjugacy, unrelated endpoint repair or
new construction family is supplied; JC2 remains unresolved.

The [rational no-pencil countertest](xmodel/rational-area-no-pencil-swarmHQ-root-20260920T211700Z.md)
now has a [stronger reviewed no-foliation conclusion](xmodel/rational-area-no-foliation-integration-swarmHQ-root-20260921T002700Z.md).
For the SAME F(x,y)=(y/(2x),y^4/(16x^4)-x^2), determinant1 and generic
degree2 coexist with exact lambda1=4 and NO algebraic foliation preserved
by any positive iterate. Algebraic stability supplies the exact degree;
Favre--Pereira classification and Dinh--Nguyen degree comparison exclude
the fibration, torus and monomial possibilities. Independent Fable FIRST
confirms it, PROMOTED/MANUAL with named imports and binding citation
clarifications. Its poles exclude it from JC2. This closes an AREA-ONLY
rational foliation shortcut, not the missing polynomial-source premise.
No finite-web exclusion, polynomialization or new donor family follows.
The conditional polynomial criteria below retain their separate scope.

The [invariant-foliation theorem](xmodel/invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md)
now gives a broader conditional exclusion: a polynomial Keller map with
ANY nonzero constant determinant preserving ANY algebraic foliation is
an automorphism, including when only a positive iterate preserves one.
A rational first integral is not required. Primitive polynomial defining
forms have constant pullback multipliers; exterior differentiation reduces
two distinct invariant foliations to a pencil. Favre--Pereira Corollary B
supplies a second foliation in the no-first-integral case; all fibrations
go directly through the accepted rational-pencil theorem below.
[Independent Fable FIRST and binding integration](xmodel/invariant-foliation-first-integration-swarmHQ-root-20260920T103300Z.md)
confirm it: PROMOTED/MANUAL with named imports. No invariant foliation
for a hypothetical counterexample is supplied, and no universal claim
about automorphisms or JC2 solution follows. A new existence argument,
not another invariant-foliation classification, is needed to use this
criterion for a global proof.

The [finite-web extension](xmodel/invariant-web-keller-swarmHQ-root-20260920T123400Z.md)
now covers ANY preserved reduced finite algebraic web, including preservation
only by a positive iterate, for every nonzero constant Jacobian. A primitive
binary form has constant pullback multiplier. Its discriminant either gives
a preserved polynomial pencil, or is a nonzero constant and yields a split
finite-etale direction cover of the original plane. An iterate then fixes
a foliation. [Independent Fable FIRST and integration](xmodel/invariant-web-first-integration-swarmHQ-root-20260920T125600Z.md)
confirm it, PROMOTED/MANUAL with inherited and classical imports. No web is
produced for hypothetical noninvertibility: a target web and its Keller
pullback need not be the same, and a local formal direction need not be
algebraic. No automatic web-existence or classification task follows.

The [rational-pencil unification](xmodel/rational-pencil-unification-swarmHQ-root-20260920T033600Z.md)
now covers EVERY nonconstant rational pencil preserved by a polynomial
Keller map: r composed F=phi composed r implies F is an automorphism,
for every nonzero constant determinant. No primitivity, generic genus,
base-degree or affine-base-point restriction is imposed; a pencil for
any positive iterate also suffices. [Independent Fable FIRST and binding integration](xmodel/rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md)
confirm it, PROMOTED/MANUAL with named geometric and hyperbolic-moduli
imports. An etale periodic-point order argument eliminates affine base
points; a genus-zero properness argument works for rational morphisms;
dependent pairs reduce to polynomial pencils without a generator theorem.
This removes the previous DNT/modulus and exact-area dependencies from
the combined POLYNOMIAL-map conclusion, not from the separate rational-map
theorem above. The global gap is still a preserved pencil for a
hypothetical noninvertible map, or a different closing argument. No such
pencil, unrelated endpoint repair, classification family or JC2 proof
is supplied. Every automorphism is NOT asserted to preserve a pencil.

Separately, [basepoint-free target-pencil primitivity](xmodel/basepoint-free-pencil-review-swarmHQ-sol56-root-20261018T170650Z.md)
does not require invariance: if f:A2_target->P1 is a morphism with geometrically
integral rational generic fibre, C(f) is algebraically closed in the source field
of every Keller map. Intermediate branch divisors would be both vertical and
components of the nonproper-value set, forcing a forbidden smooth A1 component.
PROMOTED/MANUAL with named imports; ROOT/Astra producer, independent Sol5.6-assigned
FIRST. For D_R=(R(s),t/R'(s)), deg R>1, this excludes arbitrary finite rational
source repair after ANY birational target change whose transformed old-coordinate
pencil extends to a morphism on the whole new affine target. The target change
need not have constant Jacobian. Affine-basepoint pencils, arbitrary donors and
global finite-normalization emptiness remain outside this conditional filter.

The separate [one-bad-fiber pullback theorem](xmodel/one-bad-fiber-review-swarmHQ-sol56-root-20261018T211903Z.md)
allows affine basepoints and arbitrary generic-fiber genus: for target-primitive
f=a/b with coprime a,b, if all but at most ONE affine fiber divisor (including
the pole fiber) are reduced, C(f) remains algebraically closed after any Keller
pullback. Empty divisors count as reduced. Componentwise reducedness, the single
possible omitted value of a rational source function, Riemann-Hurwitz and power
descent close this restricted multiplicity argument. PROMOTED/MANUAL; ROOT producer,
independent Sol5.6-assigned FIRST, standard Keller/curve imports, novelty unknown.
The explicit pencil (v^2-u^3)/u^2 satisfies the hypotheses despite its basepoint.
It excludes every finite rational source repair of the fixed-target donor
H_R=(t^2-R(s),t(t^2-R(s))), deg R>1. Neither arbitrary target changes nor a
suitable-pencil existence theorem for a general Keller map follows. This is a
different hypothesis set from the basepoint-free result, not a replacement for it.

The earlier [homogeneous-pair proof](xmodel/homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md)
and [genus-zero polynomial-pencil proof](xmodel/rational-polynomial-pencil-swarmHQ-root-20260920T011100Z.md)
retain their original statements and reviews in AUDIT. The separate
[hyperbolic moving-pencil theorem](xmodel/hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md)
also retains a useful NON-KELLER statement: primitive polynomial h,
h composed F=psi composed h with deg(psi)>=2, and full geometric generic
fiber of positive affine Euler defect imply N(F)=deg(psi) and a fixed
rational function not in C(h), for a dominant polynomial F.
[Independent Fable FIRST](xmodel/hyperbolic-pencil-first-integration-swarmHQ-root-20260919T205600Z.md)
confirms that moduli/descent theorem at its named classical import scope.
No arbitrary-source pencil existence follows from any of these results.

For the FIXED original Weierstrass source, the separate
[one-puncture comparison](xmodel/one-puncture-target-swarmHQ-root-20260919T051000Z.md)
now excludes EVERY birational target postcomposition making multiplication
polynomial, for every fixed a and |m|>=2, including one-sided V_m/m scaling.
It compares DIFFERENT
geometrically integral genus-one pencils: the full normalized source
has one puncture, so unramifiedness forces N*|S_target|<=1 and degree one.
[Independent Sol FIRST with exposition clarifications](xmodel/one-puncture-first-swarmHQ-sol-20260919T052700Z.md)
confirms this exact scope, PROMOTED/MANUAL with classical curve imports.
No constant Jacobian is needed. Arbitrary rational source changes may
alter punctures and remain outside scope; combining the three filters
does not establish arbitrary two-ended repair exclusion. No candidate,
general Keller invariant or further elliptic-family search follows.

The [fixed Legendre-tripling candidate](xmodel/legendre-tripling-source-obstruction-swarmHQ-root-20260916T093800Z.md)
is excluded under EVERY finite rational source substitution: a ramified
generic target line persists and contradicts the classical no-line theorem
for polynomial Keller maps. [Independent Sol review](xmodel/legendre-tripling-review-swarmHQ-sol-20260916T094200Z.md)
confirms this fixed-pair result, PROMOTED/MANUAL with named imports.
Other target coordinates, multipliers and elliptic families are not covered;
no such successor or general source-landing implication is supplied.

The [affine binary-form plane obstruction](xmodel/binary-form-affine-plane-obstruction-swarmHQ-root-20260916T053400Z.md)
now covers ALL positive unequal factor degrees and arbitrary affine
two-planes of product coefficients. Every entire-A2 component of the
original resultant-one factorization source maps isomorphically to the
parameter plane. A dual-discriminant/monodromy argument handles each
component separately; units and integrality handle degenerate directions.
[Independent Sol review](xmodel/binary-form-affine-plane-review-swarmHQ-sol-20260916T053900Z.md)
confirms the claim: PROMOTED/MANUAL with the named polynomial-nonproperness
theorem. Increasing degrees or changing the affine plane cannot evade
this obstruction. Nonlinear target surfaces, arbitrary source maps into
the factorization space and other constructions are outside this theorem;
no such alternative is supplied, and JC2 is not resolved.

For equal factor degrees, the distinct
[opposite-scaling quotient](xmodel/equal-degree-resultant-quotient-swarmHQ-root-20260916T083300Z.md)
is finite over the product coefficients. Every reduced dominating component
over ANY polynomial two-parameter family therefore maps isomorphically to
its parameter plane, including nonlinear families. [Independent Sol review](xmodel/equal-degree-quotient-review-swarmHQ-sol-20260916T083553Z.md)
confirms this exact construction exclusion, PROMOTED/MANUAL. An arbitrary
initial source parametrization can still carry the whole Keller problem;
unequal-degree nonlinear families are not covered by this quotient argument.

The distinct [natural SL2 quotient of linear/cubic multiplication](xmodel/linear-cubic-sl2-quotient-swarmHQ-root-20260916T174200Z.md)
is also trivial as a plane construction: on the WHOLE resultant-one
source, a canonical polynomial frame gives SL2 times A2; the full quartic
invariant quotient map is (u,v)->(-3u,-27v), an automorphism.
[Independent Sol review](xmodel/linear-cubic-sl2-review-swarmHQ-sol-20260916T174500Z.md)
confirms this exact scope, PROMOTED/MANUAL. No other group, cut, target
surface or factor degree is excluded; no automatic family search follows.

For the ORIGINAL four-variable marked-root source, the
[explicit section calculation](xmodel/marked-quartic-section-swarmHQ-root-20260917T181100Z.md)
now gives a separate whole-source exclusion. Its fixed quartic-invariant map
q=(-I/3,-J/27) has section (a,b)->(0,0,a,b). Normality makes C(q) relatively
algebraically closed in the source field, so ANY factorization q=H composed rho
with rho a dominant rational plane quotient and H polynomial Keller forces H
to be an automorphism. [Independent Fable review](xmodel/marked-quartic-section-first-swarmHQ-fable-20260917T182700Z.md)
confirms the exact statement: PROMOTED/MANUAL with the classical birational
Keller theorem. No assumption on rho's generic fibers is needed. This is only
the quotient direction for this fixed q: q composed (0,0,f,g) realizes any
polynomial pair (f,g), so arbitrary A2->A4 substitutions are NOT excluded.
No other target field or new family follows.

For the different LOWER coefficient block, the September30
[coordinate-fiber calculation](xmodel/lower-block-coordinate-obstructions-swarmHQ-root-20260930T014100Z.md)
gives uniform obstructions for every n>=4 and parameter: no next-coefficient
fiber is A2, no constant top-coefficient fiber admits a two-dimensional
polynomial-plane image, and no polynomial shear of the next coefficient
by the top coefficient is a coordinate. MANUAL, UNPROMOTED; Astra/Opus
production with ROOT integration and hostile cross-checking. The proof
uses the literal defining polynomial, not an external threefold theorem.
Arbitrary target combinations and plane restrictions remain outside scope;
no small-case or parameter search follows from this calculation.

For the fixed cubic-fiber core (the running triple up to an invertible linear
target change), the September 13 [embedded-plane transfer](xmodel/embedded-plane-transfer-root-20260913.md)
and [low-fiber tower transfer](xmodel/low-fiber-tower-transfer-root-20260913.md)
already exclude counterexamples from full factorizations
Phi_m ... Phi_1 j = i h, where j has two-dimensional image and generic
degree at most three onto that image. The chain allows the core, identity
stabilizations and polynomial source/target automorphisms; i is any polynomial
map, not just an affine embedding. Thus nonlinear embedded-plane sections
and all finite compositions in this full-factorization scope are covered.
These are PROMOTED/MANUAL, retaining the accepted small-mapping-degree and
strict second-leg-degree 2/3 premises in [AUDIT.md](AUDIT.md#low-fiber-tower-transfer-1--2026-09-13).

The stronger [Keller right-factor invariance](xmodel/low-fiber-keller-factor-invariance-root-20260913.md)
removes the initial-degree bound for a different conclusion: such chains
create no polynomial Keller right factor absent from j. Test the initial
parametrization first; arbitrary j is not proved factor-free. This is
[PROMOTED/MANUAL at its recorded conditional and review scope](AUDIT.md#low-fiber-keller-factor-invariance-1--2026-09-13).
Arbitrary output projections do not provide the full factorization and
remain outside these results, as do actual restricted steps of degree at
least four. No general JC2 reduction or new construction follows.

The separate [connected-quotient tower theorem](xmodel/connected-quotient-tower-swarmHQ-root-20260916T155300Z.md)
covers arbitrary dominant rational endpoint quotients, not just group actions:
if BOTH generic fibers are geometrically integral, a compatible plane
polynomial Keller map descended through any finite ambient tower of
function-field degrees at most three must be an automorphism. Relative
algebraic closures construct an actual small-step surface-field tower;
the first strict step is excluded by the accepted whole-degree/second-leg
2/3 results. [Different-model Sol review](xmodel/connected-quotient-review-swarmHQ-sol-20260916T155700Z.md)
confirms this interface: PROMOTED/MANUAL, conditional on those existing
premises. Check the two endpoint fields before searching for compatible
quotient actions. Arbitrary projected plane sections, geometrically
nonintegral generic fibers and ambient steps of degree at least four
are not covered by that tower theorem; no alternative construction or
general JC2 reduction follows.

For a SINGLE ambient self-map preserving the SAME rational plane quotient,
the [same-quotient cancellation lemma](xmodel/same-quotient-degree-cancellation-swarmHQ-root-20260918T170200Z.md)
removes the geometric-integrality premise: the descended generic degree
divides the ambient generic degree. [Independent Sol FIRST](xmodel/same-quotient-degree-first-swarmHQ-sol-20260918T170700Z.md)
confirms the field proof, PROMOTED/MANUAL. A polynomial Keller descendant
of a degree1/2/3 self-map is therefore invertible, using only the accepted
whole-degree2/3 exclusions and birational Keller theorem. Disconnected
generic fibers are allowed; two different quotient maps and arbitrary
towers are not. This constructs no quotient for an arbitrary Keller map
and is not a general JC2 reduction or a literature novelty claim.

The [graph/tower scope check](xmodel/ideation-full2130-swarmHQ-synthesis-20260916T214500Z.md)
explains why a finite birational canonical graph does not close this gap:
its degree one is over the source field, while its bottom target quotient
fails geometric integrality when the Keller degree exceeds one. This is
MANUAL/DOCUMENTARY, UNPROMOTED; no new normality theorem or test follows.

For the separately normalized weighted-lift family, the
[coordinate-fiber obstruction](xmodel/weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133700Z.md)
covers EVERY admissible seed degree, every literal coordinate level and
arbitrary regular A2 first legs. Units exclude most fibers; a boundary
cycle excludes the remaining nonzero B-fibers. The only A2-dominated
component is x=0 over C=0, whose remaining pair is a triangular
automorphism, so it creates no Keller counterexample absent from the
initial parametrization. [Different-model Sol review](xmodel/weighted-lift-coordinate-review-swarmHQ-sol-20260916T133500Z.md)
confirms this exact scope: PROMOTED/MANUAL with the accepted MORPHIC
rational-forest theorem. Non-coordinate target surfaces, arbitrary
projections and target changes remain outside scope; no successor is supplied.

Nonsingular functions on U^2=A+A^2 Z need not have rational generic
fibers. The reviewed
[fixed two-iterate example](xmodel/pseudoplane-genus-one-no-mate-swarmHQ-root-20260916T063400Z.md)
h=(A+U) composed with eta^2 has geometrically integral genus-one generic
fiber, yet has no regular scalar mate of any degree. The known rational-mate
pole mechanism excludes this particular seed. [Independent review](xmodel/pseudoplane-genus-one-review-swarmHQ-sol-20260916T063700Z.md)
confirms the fixed-function claim, PROMOTED/MANUAL; arbitrary scalar pairs
on S are still unresolved. No further-iterate search follows.

The retained fixed-direction formal recursion on U^2=A+A^2 Z is
[ruled out by a logarithmic-residue obstruction](xmodel/formal-fixed-recursion-nonalgebraicity-swarmHQ-root-20260916T004300Z.md),
confirmed by [independent Sol review](xmodel/formal-fixed-recursion-review-swarmHQ-sol-20260916T004600Z.md).
Its exact completed pair is transcendental over the surface function field,
even after finite algebraic extension. All finite jets remain valid; other
formal pairs and arbitrary regular scalar-bracket pairs on this surface
are not excluded. This closes the specific algorithm, not the construction route.

The reviewed [Laurent donor filter](xmodel/laurent-polynomial-donor-swarmHQ-root-20260915.md)
now has a [rational-coefficient extension](xmodel/rational-coefficient-donor-swarmHQ-astra-20260915T214600Z.md),
confirmed by [independent Sol review](xmodel/rational-coefficient-donor-review-swarmHQ-sol-20260915T215100Z.md):
q in C(p)[u] of degree m>=2 cannot become a whole-plane Keller pair with p
after any finite-degree source substitution. Local normalized fibers and
global divisor classes handle all finite coefficient poles and leading zeros.
Polynomial dependence on u remains essential; no target-compatible rational
fiber presentation is supplied for arbitrary Keller maps. The separate
[torus quotient filter](xmodel/volume-neutral-torus-quotient-swarmHQ-root-20260915.md)
also excludes only its stated construction. Neither result resolves JC2.

For the running map's non-volume-neutral weights(1,-1,-2), the
[actual plane quotient](xmodel/running-torus-quotient-target-rigidity-swarmHQ-root-20260916T011000Z.md)
has cofinite image and nonconstant Jacobian. [Independent Sol review](xmodel/running-torus-quotient-review-swarmHQ-sol-20260916T011400Z.md)
confirms that no rational target postcomposition repairs it on its fixed
whole source plane. This does not cover arbitrary source substitutions,
finite covers or other torus actions.

The running three-dimensional map now also has an
[all-additive-action exclusion](xmodel/running-core-additive-rigidity-swarmHQ-root-20260916T023000Z.md),
confirmed by [independent Sol review](xmodel/running-core-additive-review-swarmHQ-sol-20260916T023700Z.md).
Its actual nonproper-value surface is Ga-rigid, ruling out every nontrivial
algebraic source/target Ga-equivariance, including after separate polynomial
coordinate automorphisms. No primitivity or polynomial-kernel assumption is
needed. This closes the fixed-core additive-quotient route, not stabilization,
other maps, other groups, arbitrary projections or general JC2.

The reviewed [specific Pinchuk donor exclusion](xmodel/pinchuk-donor-branch-swarmHQ-root-20260915T143100Z.md)
has a [reviewed ramification-genus extension](xmodel/ramification-genus-birational-target-swarmHQ-root-20260915T152300Z.md):
every rational dominant target postcomposition inside its original target field
is excluded after every finite-degree source substitution. Positive source residue
genus and genuine ramification suffice; branch-image genus is not needed for this
new argument. Other target fields, arbitrary Pinchuk-like presentations, and the
all-rational-ramification case remain outside scope; no candidate pair results.

The reviewed [cyclic tangent-coordinate filter](xmodel/tangent-cyclic-coordinate-swarmHQ-root-20260915T170800Z.md)
also excludes arbitrary target coordinates with source-coordinate pullbacks
in the literal full polynomial stratum p=w^m A, q=w^(m+1) B, m>=2,
A(0)!=0, gcd(A,B)=1 and q'=wp'/2. This is additional to the earlier
p'(0)!=0 clean stratum. Common nonzero roots and other descent mechanisms
remain outside scope; no reduction places arbitrary Keller sources here.

For arbitrary polynomial graphs z=Z(x,y) of the literal tangent triple,
the reviewed [three-minor degree identity](xmodel/tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md),
confirmed by [independent Sol review](xmodel/tangent-graph-linear-review-swarmHQ-sol-20260916T183500Z.md),
excludes every constant linear plane projection of (C,D,E), and every
polynomial postcomposition of such a projected pair, for all admissible
seed degrees. It extends the [first-pair exclusion](xmodel/tangent-graph-first-pair-swarmHQ-root-20260915T180230Z.md)
in this literal whole-triple setting. Arbitrary nonlinear maps of all three
outputs, other source-plane orientations and rational target changes remain
outside scope. No graph-degree or output-family search follows.

For the narrower **constant nonzero gamma** class, the
[constant-gamma proof and binding scope](xmodel/constant-gamma-integration-swarmHQ-root-20261015T211500Z.md),
with independent Sol review, exclude **arbitrary polynomial target outputs**
for every eligible seed of degree at least two. A plane-curve genus argument
forces a parameter collision, whose two source hyperbolas have incompatible
Liouville residues for a Keller pair. This removes the linear-output restriction
only in that constant-gamma class; nonconstant gamma and general source maps
remain open. No reduction of JC2 to this construction is known.

**Useful next contribution:** a complete source construction, an applicable global
algebraization theorem, or a genuinely different donor mechanism.

The [binary-quintic marked-pair chart](xmodel/quintic-partition-target-field-swarmHQ-root-20260916T032000Z.md)
is also excluded on its fixed source, with [independent Sol review](xmodel/quintic-partition-review-swarmHQ-sol-20260916T033100Z.md).
It is a punctured plane covering all but one point of the projective coarse
moduli surface. Every rational target function with polynomial pullback
is therefore constant. This does not cover arbitrary source substitutions,
other markings or other moduli constructions; no candidate pair results.

[Construction interfaces and controls](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#7-st-construction-and-algebraization).

## Uniform descent and blocks

**Question:** can one prove uniform source-to-chart landing and exclusion, or find a
strictly improving invariant covering every remaining counterexample configuration?

The finite n <= 200 census leaves 64 necessary configurations (44 with u_s = 1 and
20 with u_s >= 2); these are not polynomial pairs or an all-degree classification.
Moh receivers require the child's own characteristic data and full support.

Proper Galois target blocks and target block degrees d2 = 2 and d2 = 3 are excluded
at the recorded scopes. The distinct first-leg degree d1 = 2 question, non-Galois
target blocks d2 >= 4, and primitive/no-block cases remain unresolved. No theorem
asserting the existence of a block follows. The K16 theorem is promoted through
t = 8 only; its uniform statement remains open.

**Useful next contribution:** a missing uniform source implication or global
compatibility argument, with the exact block/degree distinction retained.
[Precise interfaces and reviews](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#4-other-unbounded-proof-and-construction-fronts).

## Complete F10 source

**Question:** decide the complete guarded source for r >= 3, preserving all source
relations, inverse-pole conditions, and the reconstruction map.

The r1 and r2 source-zero results have separate source-composition reviews at their
recorded tiers. Scalar unitness and the reviewed necessary coefficient identities
still do not establish complete source zero for higher r. A finite number of possible
exceptional scalar parameters is not an effective cutoff or an all-r certificate.
The scalar, regularity, source-comparison, and full-source conclusions are distinct.

The [simple-critical-line lemma](xmodel/simple-critical-line-f10-swarmHQ-root-20260916T105500Z.md),
with [independent Sol review](xmodel/simple-critical-line-review-swarmHQ-sol-20260916T105619Z.md),
now derives residue degree1 and transverse index2 for the literal F10
receiver's g=0 boundary divisor. PROMOTED/MANUAL with standard curve
imports. By itself this supplies two hypotheses for that divisor, not uniqueness
of the dicritical, a new trace inequality or an all-r exclusion test.

The October15 [full-normalization carrier identification](xmodel/f10-full-normalization-integration-swarmHQ-root-20261015T223201Z.md)
now supplies the missing whole-carrier statement for complete guarded compact
F10 inputs: the known two-chart affine surface is the full finite normalization,
and its reconstructed plane complement is exactly one smooth A1, with generic
normal ramification index2. PROMOTED/MANUAL after independent Sol5.6 review.
The proof uses every target-finite valuation and the full source inverse; the
old auxiliary rank-three module alone did not establish this. Finiteness of
the enlarged surface does not imply finiteness or surjectivity of the open
plane map. A new full-pair constraint is still needed; no F10 exclusion or
repair of the old one-dicritical trace/connectivity inequalities follows.

The [reviewed degree countercontrol](xmodel/critical-image-degree-countercontrol-swarmHQ-root-20260916T120130Z.md)
has the same simple critical line but critical-image degrees6 and9:
primitivity does not force coprime degrees or degree divisibility.
It refutes that proposed shortcut, not the F10 source contract.

### A concrete question for contributors

The [reviewed carrier presentation](xmodel/finite-moment-review-integration-swarmHQ-sol56-root-20261016T010647Z.md)
puts one remaining question in a small explicit ring:

```text
R = C[U,V],   p = UV^3 - V,
T = C[U, UV, UV^2, p]  inside R.
Does T contain P,Q with P_U Q_V - P_V Q_U = 1?
```

Any such pair would be a counterexample to JC2, not merely an auxiliary map.
Indeed, substituting `U=g^2+g^3*p, V=1/g` makes every generator of T polynomial
in g,p, whereas V remains 1/g. Thus V is not in T; if P,Q had a polynomial
inverse, `R=C[P,Q]` would contradict `C[P,Q]` being contained in the proper ring T.

A narrower question adds that `Spec T -> A2_(P,Q)` is finite. Complete guarded
F10 sources satisfy this extra condition by the reviewed normalization result
above. Excluding even these finite pairs would close that carrier class, not
all of JC2. Conversely, an arbitrary pair in T is not asserted to satisfy the
other F10 source relations, and finiteness is not automatic from this formulation.

There is already a finite degree-six map `(p^2,U)` on this very carrier.
Its Jacobian is `-2*p*(3*U*V^2-1)`, not a nonzero constant; it is not a JC2
counterexample. The linked proof also shows why the current polynomial-moment
conditions alone do not exclude it. The needed new contribution must use the
constant-Jacobian condition, not just construct another finite map.

The [reviewed pencil obstruction](xmodel/carrier-pencil-review-integration-swarmHQ-sol56-root-20261016T063000Z.md)
rules out every constant-direction repair `(p^2+alpha*H,U+beta*H)`, for arbitrary
`H in T` and constants `alpha,beta`. Each nonzero linear combination of `U,p^2`
lacks a mate in T; mixed members lack even a rational mate. This closes that
one construction mechanism, not general deformations or the question above.

The [reviewed extreme-weight constraint](xmodel/carrier-extreme-weights-v2-swarmHQ-root-20261016T044600Z.md)
requires each member of any Keller pair in T to have both positive and negative
weights for w(U)=-2,w(V)=1. The highest components, and separately the lowest,
are powers of a common element of T. This is not a reduction to homogeneous pairs
or a carrier exclusion. A proposed test using only a few extreme equations fails:
dependent pairs with Jacobian zero satisfy those equations even at both ends.
The full coupled equations, especially the constant-one row, remain essential.

Scalar nonsingularity alone does not force rational generic fibres, even in T.
The [reviewed fixed example](xmodel/carrier-genus2-integration-swarmHQ-root-20261016T133911Z.md)
`f=p^4+(1/3-3c)*p^2+3*c^2-2*c-1-U`, with `c=UV^2`, is nonsingular on
the whole source plane and has geometric generic genus two. Its specific fibre
differential also excludes every rational constant-Jacobian mate. This refutes
the scalar-rationality shortcut only; the arbitrary-pair question remains open.

**Useful next contribution:** an exact full-source implication or certificate that
changes the unresolved test. Prior timeouts and term limits are nondecisions.
[Complete source](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#2-complete-f10-source-the-remaining-r3-problem) ·
[Scalar and r3 evidence](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#3-r3-positive-test-and-implementation-boundary).

## Closed scopes and historical evidence

The [recorded coverage and closed scopes](https://github.com/dcposch/jc2/blob/ec69252af5ca03245becb80436f5ddb0917ccef2/APPROACHES.md#1-global-coverage-and-closed-scopes)
distinguish actual total degree, partial-y degree, mapping degree, and normalized
source strata. In particular, the recorded maximum-degree >= 125 bound is conditional
on named imports and retained external certificates; individual family closures do
not establish a blanket higher-degree bound. Check the exact ledger before a search.

The historical Dixmier inventory's deferred T2 arithmetic check was subsequently
completed in the [August 23 audit](xmodel/sol-dixmier.md#26-t2-verdict-and-remaining-proof-obligations):
T2-local PASS under its stated contract. The theorem-chain interfaces remain
unverified; this is not certification of the claimed DC(1) proof. A gap in that
proof alone would not refute JC2. The old T2 queue entry is not a new experiment.

The [pentagon obstruction](xmodel/a5-pentagon-chart-review-swarmHQ-sol56-root-20261018T222155Z.md)
closes one nonlinear finite-group construction: for the degree-five del Pezzo
surface S=bar(M_0,5), the fixed cover S/A4->S/A5 has no A2-open source/target
charts on which it is everywhere etale. Two local critical branches at a D5
pentagon belong to one irreducible ramification curve; placing it in an A2
boundary would contradict the boundary-tree property. PROMOTED/MANUAL after
independent FIRST, with standard imports; novelty unknown. Other covers,
arbitrary birational target models and the actual-normalization gap remain open.

The [positive-zero multibranch criterion](xmodel/positive-zero-cycle-review-swarmHQ-sol56-root-20261019T101735Z.md)
also obstructs rational Darboux coordinates when an irreducible positive zero curve is
multibranch at a pole-free point. Its finite-cover application survives constant-
Jacobian birational target changes only for an identified target area form
regular/nonzero at the specified point, and only birational source coordinates.
PROMOTED/MANUAL, ROOT/Sol FIRST; no general normalization or target-form existence
step follows. The A5 application retains that additional form hypothesis.

The [SNC shifted-order criterion](xmodel/snc-order-coprimality-review-swarmHQ-sol56-root-20261019T112438Z.md)
requires gcd(a+1,b+1)=1 at a two-component SNC crossing of a rational Darboux
form generating the surface function field. On the actual finite Keller
normalization this forces coprime ramification indices at smooth transverse
crossings of exactly two ramification curves. PROMOTED/MANUAL, ROOT/Sol FIRST;
novelty unknown. It allows distinct curves but requires SNC, unlike the cycle
criterion. Existence of a forbidden crossing and the global B=R implication
remain open; the separate pole-free criterion below treats non-SNC zero support,
not singular surface points. No finite-source-extension or arbitrary-pencil
theorem is inferred.

The [pole-free zero-support criterion](xmodel/pole-free-zero-snc-review-swarmHQ-sol56-root-20261020T105819Z.md)
requires the reduced positive zero divisor of a FIELD-GENERATING rational
Darboux form to be SNC wherever the form is regular. It excludes cusps,
self-nodes, tangencies and triple points there by extending zero-free-model
descent, then applying smooth-surface birational factorization. PROMOTED/MANUAL,
ROOT/Sol FIRST; standard imports and unknown novelty. For a finite cover this
excludes non-SNC reduced ramification at a smooth source point above a smooth
target point with a specified regular/nonzero area form. It neither provides
that form nor forces such a boundary point; disjoint smooth omitted curves
already satisfy SNC. Finite source enlargement and the actual B=R gap remain.

The [coprime binomial-pencil theorem](xmodel/binomial-pencil-primitivity-review-swarmHQ-sol56-root-20261020T115104Z.md)
shows C(P^m/Q^n) is algebraically closed in C(x,y) for every polynomial
Keller pair and coprime positive m,n. This gives geometrically integral
generic fibers, not genus zero or irreducibility of every special fiber.
Unlike ONEBAD, it covers the two nonreduced fibers when m,n>1, using
primitive-polynomial fiber multiplicities and reduced-fraction extraction.
PROMOTED/MANUAL, ROOT/Sol FIRST, standard imports and unknown novelty.
A nonprimitive coprime binomial pencil obstructs polynomial Keller repair
by dominant rational SOURCE substitutions retaining the target functions,
including rational-plane finite source extensions. Arbitrary birational
target changes, pencil existence and the actual B=R implication remain open.

The [two-bad-fiber theorem](xmodel/two-bad-fiber-review-swarmHQ-astra-root-20261020T134316Z.md)
extends BIN1128: a target-primitive a/b with coprime, algebraically
independent numerator and denominator remains primitive under Keller
pullback if at most two affine fiber divisors are nonreduced (pole included;
empty divisors reduced). Independence prevents every divisor-empty
intermediate fiber, forcing any intermediate cover to be cyclic; its power
then descends. Basepoints are allowed, with no generic-genus assumption.
PROMOTED/MANUAL, ROOT/Astra FIRST; standard imports and unknown novelty.
ONEBAD retains its separate polynomial/dependent-numerator scope.
The fixed-target source-repair obstruction extends accordingly, but neither
boundary-to-pencil existence nor B=R is supplied. Arbitrary target changes
remain outside this result.

The complementary [three-double-fiber criterion](xmodel/three-double-fiber-review-swarmHQ-sol56-root-20261020T172346Z.md)
allows at most THREE nonreduced affine fiber values when EVERY component
multiplicity is at most TWO, with the same coprime independent a,b and
target-primitivity hypotheses. Riemann-Hurwitz leaves only degree2/4
intermediate curve maps; two wholly even fibers then force a square
descending to K, a contradiction. PROMOTED/MANUAL, ROOT/Sol FIRST,
standard imports and unknown novelty. This supplements, not replaces,
TWO1323's unrestricted multiplicities at two values. The fixed-target
source-repair consequence has the same limitations: no suitable pencil
from the normalization boundary, general Keller degree bound or B=R.

[Evidence ledger](AUDIT.md) · [Recent progress](PROGRESS.md) ·
[Historical avenue inventory](history/APPROACHES-before-20260906-cleanup.md#1-master-union-table) ·
[Replay and scope checks](docs/REPLAY.md)
