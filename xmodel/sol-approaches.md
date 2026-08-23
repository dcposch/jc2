# The JC2 approach landscape

**Status date:** 2026-08-21  
**Question:** for $F=(P,Q):\mathbb A^2_{\mathbb C}\to\mathbb A^2_{\mathbb C}$, does
$J(P,Q)\in\mathbb C^\times$ imply that $F$ is a polynomial automorphism?

## Scope and ground rules

This is an operationally complete map of the *top-level* proof and disproof programs I can identify. It deliberately includes overlapping formulations when the missing theorem is genuinely different, and includes bad routes when their failure teaches us something. It does not attempt to list every named lemma or every possible implementation of Gröbner elimination.

Two status boundaries control the survey.

1. **JC2 remains open.** A dated 2026 preprint gives an explicit counterexample in dimension $3$, hence in every dimension $n\geq3$ by adjoining identity coordinates [Gao 2026](https://arxiv.org/abs/2608.00222). Thus “prove the Jacobian conjecture in all dimensions and specialize” is no longer a viable program. BCW/Drużkowski, stable Dixmier, and unrestricted vanishing programs remain relevant to JC2 only after one characterizes the special stable image of maps originating in two variables.
2. **This repository has no end-to-end reduction of JC2.** The controlling audit is [REDUCTION.md](../REDUCTION.md): there is no theorem landing every plane Keller pair in the enumerated sheet books, no GGV-chain-to-Eggers–Wall data transport, no complete off-axis/post-jump sector coverage, and no uniform bound on topological degree or type. Older optimistic summaries must be read through that audit.

Campaign labels below mean:

- **Yes:** the repository executed a substantive calculation or proved/audited a scoped theorem.
- **Partial:** it executed only a restricted client, or did nearby work without testing the central implication.
- **No:** I found no executed test; a proposal note alone does not count.

For every **No**, and normally every **Partial**, I give the cheapest useful new experiment. The score is **expected research information from that first experiment**, not the probability that the route will solve JC2: 1 is nearly category-error; 5 is a worthwhile discriminator; 10 would be the obvious first priority.

The three best live clusters, in my judgment, are:

- **HC4 $\Rightarrow$ JC2**, starting with the degree-five Hessian case: **9/10**.
- The integrated plane-at-infinity pipeline—Newton corners $\to$ Puiseux/key valuations $\to$ resolved boundary/nonproper set $\to$ coupled $\mu=6$ monodromy: **8/10**.
- For disproof, a genuinely two-dimensional version of the new tangent-sweep mechanism or descent of its three-dimensional example: **6–7/10**, with a severe ramification obstruction.

---

## I. Direct algebra and geometry in the plane

### 1. Jung–van der Kulk / elementary degree descent

- **Essence.** Normalize a minimal Keller pair and imitate the affine/triangular reductions of a plane automorphism until one component degree drops.
- **Campaign:** **No.** [TRANSPORT.md](../TRANSPORT.md) proves a useful simultaneous coordinate normalization, but not a Jung-style descent for a hypothetical nonautomorphism; [AM-CHECK.md](../AM-CHECK.md) tests a different one-place criterion.
- **Precise obstruction.** For an *already invertible* pair, Jung–van der Kulk supplies degree divisibility and hence a lowering shear. A normalized counterexample is expected precisely in the nondivisibility regime, and the Keller equation alone has not been shown to force a permissible elementary reduction.
- **Cheapest experiment — 4/10.** On the smallest unresolved GGV corner families, enumerate all weight-lowering affine/triangular shears and test whether the bracket equations force one of their divisibility conditions. A negative result would sharply delimit the route.

### 2. Weighted Newton polygons, initial forms, and the GGV reduction

- **Essence.** For every exposed weight, $[P,Q]=1$ forces the leading forms to be algebraically dependent/common powers; combine compatible faces until no Newton polygon can occur.
- **Campaign:** **Yes, heavily and conditionally.** The $(72,108)$ Laurent clients were attacked in [CAMPAIGN.md](../CAMPAIGN.md), [LEMMA.md](../LEMMA.md), [AUDIT.md](../AUDIT.md), and independently replayed in [CROSSCHECK.md](../CROSSCHECK.md). The broad implementation is documented in [SECTION4-AUTOMATION.md](../SECTION4-AUTOMATION.md).
- **Precise obstruction.** Facewise common-power information does not glue automatically across adjacent faces or lower coefficients. The exact $(72,108)$ exclusions concern the two *transcribed Laurent systems* $[P,Q]=x^2$, conditional on the cited GGV proposition and transcription; they do not exclude arbitrary Keller pairs. Globally there are unboundedly many possible chains, and no degree/type bound makes the census finite.

### 3. Finite degree, corner, or support exhaustion

- **Essence.** Fix a degree/type bound $B$, enumerate every admissible Newton configuration below $B$, and kill every leaf exactly.
- **Campaign:** **Yes.** The farm in [SECTION4-AUTOMATION.md](../SECTION4-AUTOMATION.md), [REDUCE4-REVIEW.md](../REDUCE4-REVIEW.md), [REDUCE4-CUT-REVIEW.md](../REDUCE4-CUT-REVIEW.md), and [lib/farm.py](../lib/farm.py) covers 34 recorded families/62 systems, with some immediate deaths and many unresolved algebraic cores.
- **Precise obstruction.** A bounded census proves only a bounded theorem. No uniform degree, corner, topological-degree, or chain-length bound is known; moreover, completeness of the reduction generator is a deeper issue than certifying individual leaves. Above the regression range, parts of the implementation remain unvalidated, and large leaves time out or exhaust memory.

### 4. Newton–Puiseux expansions, approximate roots, and key valuations

- **Essence.** Follow branches at infinity, their characteristic pairs and contacts, and use the constant Jacobian to constrain every split, merge, and approximate root.
- **Campaign:** **Yes, but without a universal landing theorem.** This is the mathematical engine of [SHEET6.md](../SHEET6.md), [SHEET6-CAMPAIGN.md](../SHEET6-CAMPAIGN.md), the `SHEET6-*`, `BOOK-*`, and `TOWER-*` files, with coordinate normalization in [TRANSPORT.md](../TRANSPORT.md).
- **Precise obstruction.** Characteristic chains and dicritical families can be arbitrarily long; lower-order cancellations retain unbounded ordered coefficient data. Most importantly, the repository does not transport an arbitrary GGV admissible chain into a fiber-tagged Eggers–Wall/pole tree. The enumerator therefore explores conditional books, not all Keller pairs.
- **Cheapest untried extension — 8/10.** For one nontrivial GGV chain, build and formally verify a *paired Newton-cut/Eggers–Wall functor* that transports weights, denominators, fiber labels, contacts, and all charts—not just the coordinate rectangle. Failure on one example would identify the exact missing datum; success would attack the main bridge.

### 5. Sparse vertex-gap / unit-pivot obstructions

- **Essence.** Order bracket equations by a face valuation so unsupported columns force coefficients in sequence and leave an impossible unit monomial.
- **Campaign:** **Yes.** [LEMMA.md](../LEMMA.md), [LEMMA-REVIEW.md](../LEMMA-REVIEW.md), [SURPLUS.md](../SURPLUS.md), [SURPLUS-EXT.md](../SURPLUS-EXT.md), and [FACE-ISOLATION.md](../FACE-ISOLATION.md) establish exact scoped collapses; Lean checks two core identities in [lean/README.md](../lean/README.md).
- **Precise obstruction.** The clean gap occurs only in special thin strips. The general TL1 claim was refuted outside its valid scope; $k=1$, $y$-axis/pentagon supports, $d_1\ge2$, short strips, and deeper Minkowski columns introduce coupled terms that absorb the would-be culprit.

### 6. Residues, constant terms, Koszul cokernels, and weighted ODE rigidity

- **Essence.** Interpret the last bracket equation as a toric-boundary residue or cokernel functional and prove its nonvanishing by a one-variable logarithmic-derivative/ODE theorem.
- **Campaign:** **Yes, with a real local theorem.** [RESIDUE.md](../RESIDUE.md), [MATHIEU.md](../MATHIEU.md), [MATHIEU-REVIEW.md](../MATHIEU-REVIEW.md), and [paper2/PRIORITY.md](../paper2/PRIORITY.md) prove the full depth-two strip statement in characteristic zero. The initial form $dP\wedge dQ/P^{k+2}$ itself had zero residue; the useful functional is subtler.
- **Precise obstruction.** The proof requires the strip/gap, $d_1=1$, no $y$-axis, and depth two. Extra columns give simultaneous residue conditions rather than a single ODE. No theorem puts every JC2 candidate in this local geometry.
- **Cheapest untried extension — 6/10.** Eliminate the first depth-three column with an Ore/differential resultant and ask whether a second independent residue appears or a generic solution survives.

### 7. Generic fiber curves, exact differentials, Gauss–Manin, and adjoints

- **Essence.** On $P=c$, exploit that $Q$ is unramified and $dx/P_y$ is an exact/nonvanishing differential; force the compactified fiber to be rational with one puncture.
- **Campaign:** **Partial.** [SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md) and [TEMPLATE-ATTACK.md](../TEMPLATE-ATTACK.md) test genus, Euler, and differential budgets on residue A, but do not run a pencil-wide Gauss–Manin, Rosenlicht-adjoint, or Mittag–Leffler argument. The latter was only proposed in [sol-avenues2.md](sol-avenues2.md).
- **Precise obstruction.** Higher-genus, many-punctured affine curves can carry exact/nonvanishing differentials with all poles and cancellations at infinity. One must control the whole pencil and variation of punctures, not a single formal fiber; current residue-A data leave resolution tails unpinned.
- **Cheapest untried experiment — 7/10.** Compute the Rosenlicht dualizing module and residue pairing for the first fully specified residue-A truncation, including all punctures, and test whether the required exact differential lies in the image of $d$ after the allowed tail parameters are restored.

### 8. Coordinate recognition: Abhyankar–Moh–Suzuki, rational fibers, retracts, and an injective line

- **Essence.** Prove one component is a coordinate—or find one affine line on which $F$ is injective—then finish by known plane results.
- **Campaign:** **Partial and negative on the present template.** [AM-CHECK.md](../AM-CHECK.md) shows that the forced sequence passes local dual axioms but is a finite-center/multiplace object, so the one-place theorem does not apply. [TRANSPORT.md](../TRANSPORT.md) handles coordinate normalization, not coordinate recognition; the multibranch Gorenstein-semigroup extension in [sol-avenues2.md](sol-avenues2.md) was proposed but not run.
- **Precise obstruction.** Keller fibers are smooth, but need not be rational or one-place; nonsingular non-coordinate polynomials exist. The correct one-place objects would be components of the nonproper set, whose degrees and cross-fiber place correspondence are not pinned. Square-free preservation is far weaker than irreducible preservation or existence of a retract/fixed polynomial.
- **Cheapest untried experiment — 6/10.** Derive the components of the asymptotic set for the simplest surviving two-pole book, compute each component’s actual place semigroup, and only then apply the Abhyankar–Moh inequalities.

### 9. The nonproper/asymptotic-value set $S_F$

- **Essence.** JC2 is equivalent to $S_F=\varnothing$; classify polynomially parametrized components of $S_F$ and show none can support an étale Keller map.
- **Campaign:** **Partial.** Jelonek/nonproperness checks are part of [SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md) and [TEMPLATE-ATTACK.md](../TEMPLATE-ATTACK.md); the current template passes them. There is no campaign-wide construction of $S_F$ from the sheet books.
- **Precise obstruction.** Smooth or especially simple components are strongly constrained, but the unknown $S_F$ may be singular, reducible, self-intersecting, and reached by several escaping sheets. Local pole data do not yet determine its global component degrees, intersections, or cross-fiber correspondence.
- **Cheapest untried experiment — 8/10.** For the smallest live $\mu=6$ book, compute the elimination/valuation data for the full set of asymptotic values, not one source branch, and test the resulting component against known degree and singularity restrictions.

### 10. Blowups, dicritical divisors, Eggers–Wall trees, and boundary frameworks

- **Essence.** Resolve $\mathbb P^2\dashrightarrow\mathbb P^2$, label the boundary tree by multiplicities, discrepancies, and ramification, and prove no complete labeled tree satisfies all identities.
- **Campaign:** **Yes, extensively but conditionally.** See [SIGRAY-AUDIT.md](../SIGRAY-AUDIT.md), [SHEET6-CAMPAIGN.md](../SHEET6-CAMPAIGN.md), [TDBOUND.md](../TDBOUND.md), and the consolidated failures in [REDUCTION.md](../REDUCTION.md).
- **Precise obstruction.** Large numerical frameworks survive; necessary label identities do not guarantee local or global realizability. There is no complete entry/endpoint theorem, off-axis $b\ge2$ and mixed post-jump continuations remain, composite/on-axis books survive, and the state space is unbounded.

### 11. Links at infinity, splice diagrams, plumbing, and knot theory

- **Essence.** Encode generic fibers and their monodromy by links/splice diagrams and exclude every diagram compatible with a Keller map.
- **Campaign:** **Yes on residue A.** [SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md) runs splice, genus, pole-valuation, and Euler tests; the template passes most of them and one $x$-side $\pi_G=4$ branch dies.
- **Precise obstruction.** The method is sharp for rational, one-place, or low-sheet/simple links, but non-simple multiplace diagrams and their moduli proliferate. A topologically admissible splice diagram need not be algebraically realizable, yet topology alone has not contradicted the survivors.

### 12. Cover-complement monodromy, Hurwitz spaces, and low geometric degree

- **Essence.** Over $\mathbb A^2\setminus S_F$, regard $F$ as a finite unramified $\mu$-sheeted cover and constrain inertia, $\pi_1$, and transitive branch-cycle factorizations.
- **Campaign:** **Yes, for the degree-six one-cover data.** [GROK-MONODROMY.md](../GROK-MONODROMY.md) finds explicit transitive identity factorizations for all 169 geometrically allowed passports, so that test does not kill the template. The sheet books also recover known low-$\mu$ exclusions conditionally.
- **Precise obstruction.** Curve-complement groups can be large, the branch curve is unknown, and abstract Riemann-existence data do not produce—or contradict—a polynomial Keller pair. A passport for one coordinate ignores compatibility with the second coordinate and the Jacobian contacts.
- **Cheapest untried experiment — 7/10.** Encode *both* coordinate fibrations, all infinity contacts, and the Jacobian pairing as one finite branch-cycle CSP for the $\mu=6$ residue-A data. This is more discriminating than enumerating another single-cover passport.

### 13. Bézout/BKK intersection, proximity inequalities, and a topological-degree bound

- **Essence.** Bound the number of sheets by polynomial degrees or boundary intersection mass—e.g. $\operatorname{td}F\le mn$—and reduce the infinite sheet census to a finite one.
- **Campaign:** **Yes, but conjectural.** [TDBOUND.md](../TDBOUND.md), [sol-tdbound-review.md](sol-tdbound-review.md), [sol-pcc-orbits.md](sol-pcc-orbits.md), [sol-wtc1.md](sol-wtc1.md), and [sol-g5-emission.md](sol-g5-emission.md) test pole-mass/PCC formulations. Apparent numerical support was downgraded when most coincidences proved census-forced.
- **Precise obstruction.** The earliest missing theorem, WTC-1, must transport a Laurent common-power packet and its denominators to named ordinary or infinitely-near pencil base centers with mobile multiplicities and proximity parents. Coverage and non-double-counting are unproved. Even $\operatorname{td}\le mn$ is not an absolute bound while $m,n$ remain unbounded.
- **Cheapest untried extension — 8/10.** Prove or refute WTC-1 on one explicit nontrivial GGV chain by constructing the complete base-point/proximity graph and comparing its squared mass with the Laurent packet.

### 14. Log surfaces, log-BMY, adjunction, and surface MMP

- **Essence.** Apply canonical-divisor, log-Chern, negativity, and fibration inequalities on a compactification to rule out the boundary configuration of a nonproper étale map.
- **Campaign:** **Partial.** [SHEET6-CLASSICAL.md](../SHEET6-CLASSICAL.md) and [TEMPLATE-ATTACK.md](../TEMPLATE-ATTACK.md) set up the classical invariant battery, but explicitly mark BMY as **NEEDS-DATA** because the $B/x$-resolution tails are unpinned.
- **Precise obstruction.** Numerical boundary labels are incomplete, while BMY needs the full normal-crossings divisor, self-intersections, discrepancies, and singularity corrections. Known frameworks leave large admissible trees; inequalities alone do not settle realizability.
- **Cheapest untried experiment — 6/10.** Complete one smallest survivor to every minimal compatible tail, compute the log-Chern pair for each completion, and test whether BMY kills the entire finite completion set or merely selects realizable tails.

### 15. Function-field degree, birationality, and Galois/normal extensions

- **Essence.** Force $\mathbb C(x,y)/\mathbb C(P,Q)$ to have degree one, or at least to be normal/Galois, where strong automorphy theorems apply.
- **Campaign:** **Partial.** [TEMPLATE-ATTACK.md](../TEMPLATE-ATTACK.md) tests Galois descent on the residue-A coefficient field; conjugation merely exchanges the two poles and preserves the constraints. [GROK-MONODROMY.md](../GROK-MONODROMY.md) explores the associated non-Galois cover data.
- **Precise obstruction.** Keller implies a finite separable extension of function fields, not a normal one. All branching can live at infinity, and higher non-Galois transitive monodromy survives. Arithmetic Galois symmetry of template coefficients is not normality of the geometric function-field extension.
- **Cheapest untried experiment — 5/10.** Compute the Galois closure/inertia subgroups forced by the coupled $\mu=6$ boundary data and test whether the Jacobian contact pairing forces an impossible normal subgroup—not merely conjugation of coefficients.

### 16. Integrality, properness, Zariski Main, and étale fundamental groups

- **Essence.** Prove $x,y$ integral over $\mathbb C[P,Q]$; then $F$ is finite étale, and affine space has no nontrivial connected finite étale cover.
- **Campaign:** **No direct attempt.** Properness appears only as the target of the asymptotic-set and classical tests above; no repository argument establishes integral dependence.
- **Precise obstruction.** A Keller map is étale and quasi-finite, but *finiteness is exactly the missing global assertion*. Zariski Main completes the source by adding a boundary divisor mapping into $S_F$, not by removing it. The dimension-three counterexample rules out any dimension-free local-Jacobian-to-finiteness lemma.
- **Cheapest experiment — 6/10.** For one complete boundary book, compute the Rees valuations of $\mathbb C[P,Q]\subset\mathbb C[x,y]$ and test integral dependence directly. This is the concrete local version of the proposed multi-Rees/b-divisor idea in [sol-ideas-0821.md](sol-ideas-0821.md).

### 17. Resultants, discriminants, Bézoutians, and the off-diagonal fiber product

- **Essence.** Show the residual ideal
  $$(P(x,y)-P(u,v),Q(x,y)-Q(u,v)):(x-u,y-v)^\infty$$
  is empty, or force a unit leading coefficient in an eliminant.
- **Campaign:** **Partial.** Resultants, Macaulay matrices, branch products, and $Q$-linear elimination are used throughout [CAMPAIGN.md](../CAMPAIGN.md), [SHEET6-R1.md](../SHEET6-R1.md), and [SOL-ALGEBRAIZATION.md](../SOL-ALGEBRAIZATION.md), but the general saturated off-diagonal ideal has not been attacked.
- **Precise obstruction.** A collision component is disjoint from the diagonal and closes only at infinity, precisely where eliminant leading coefficients vanish. The local Jacobian excludes diagonal multiplicity but says little about this residual component; direct elimination doubles variables and explodes.
- **Cheapest untried experiment — 7/10.** On **open_8_28_c2**, exploit linearity in the $Q$-coefficients: compute the generic left-kernel/Fitting consistency ideal in the $P$-variables, clear denominators chartwise, and compare its first generators with the known cascade culprit.

### 18. Jacobian derivations, locally nilpotent derivations, and complete flows

- **Essence.** The Hamiltonian derivation $D_P=P_y\partial_x-P_x\partial_y$ has the slice $D_P(Q)=1$; prove $D_P$ locally nilpotent or complete, making $P$ a coordinate.
- **Campaign:** **No direct global attempt.** The ODE in [MATHIEU.md](../MATHIEU.md) is a one-variable face equation, not a proof that the global Hamiltonian derivation is locally nilpotent.
- **Precise obstruction.** A polynomial derivation with a slice need not be locally nilpotent merely from the displayed identity. Complex polynomial flows can escape to infinity in finite time; proving completeness/LND here is essentially another form of the conjecture.
- **Cheapest experiment — 6/10.** For each smallest unresolved Newton family, compute Darboux polynomials and pole orders of $D_P$ on a resolved compactification; test whether Keller plus that boundary type forces or refutes local nilpotence.

### 19. Commuting frames, foliations, and polynomial $\mathbb G_a^2$-actions

- **Essence.** The vector fields dual to $dP,dQ$ commute and form a polynomial/rational frame; prove they integrate to a transitive algebraic $\mathbb G_a^2$-action.
- **Campaign:** **No.** The campaign has local coefficient ODEs and topology of fibers, but no classification of the global commuting frame.
- **Precise obstruction.** Commutativity is local differential information. Completeness and algebraicity of both flows are not automatic, and denominators/poles of the dual frame encode the same nonproper escape. Existing classifications contain a branch equivalent to proving the original derivations are LND.
- **Cheapest experiment — 5/10.** Write the dual fields for a finite boundary template in the resolved charts and compute their pole divisors; check whether commutativity forces cancellation at every horizontal divisor.

### 20. Global reciprocity, $K_2$ tame symbols, and Jacobian-matrix factorization

- **Essence.** Package $dP\wedge dQ$, symbols $\{P,Q\}$, or the $2\times2$ Jacobian matrix into a reciprocity/factorization invariant that must vanish for a global polynomial map but not for a counterexample boundary.
- **Campaign:** **No.** $K_2$ tame symbols were proposed, not executed, in [sol-lateral.md](sol-lateral.md); local residues were pursued instead. No unstable $GL_2$ factorization program appears in the run record.
- **Precise obstruction.** Stable elementary factorization of polynomial matrices loses the integrability conditions needed to recover $P,Q$; size two is unstable, and the residual group is poorly controlled. Ordinary residue reciprocity tends to restate local étaleness while the missing contribution sits on the unknown boundary.
- **Cheapest experiment — 3/10.** Compute all tame symbols of $\{P,Q\}$ on a fully specified small boundary tree and see whether reciprocity gives an independent equation rather than the already-known valuation budgets.

### 21. Tropical and non-Archimedean geometry of the coefficient variety

- **Essence.** Tropicalize the *coefficient ideal*, not just $P,Q$, and seek a weight whose initial ideal is inconsistent or whose tropical branches force a forbidden valuation pattern.
- **Campaign:** **No direct tropical computation.** Newton weights and valuations are ubiquitous, but I found no **gfan**/tropical-variety run on an unresolved saturated coefficient system. A $p$-adic escape-mass idea was only proposed in [sol-lateral.md](sol-lateral.md).
- **Precise obstruction.** A tropical prevariety usually overapproximates the variety; nonemptiness is weak, and full fan enumeration can be as hard as Gröbner elimination. Initial degenerations can also lose the saturation and chart conditions where the contradiction lives.
- **Cheapest experiment — 5/10.** Tropicalize one unresolved 12–27-variable saturated chart, explicitly retaining saturation variables, and test whether every tropical cone lifts or whether a finite set of monomial/unit initial ideals covers it.

### 22. Graded/equivariant maps, GIT, and symmetry of a minimal counterexample

- **Essence.** Classify weighted-homogeneous Keller maps, or force a minimal counterexample into a torus/finite-group fixed stratum where that classification applies.
- **Campaign:** **Partial only at the normalization level.** Torus gauges are used in [CAMPAIGN.md](../CAMPAIGN.md), and [TEMPLATE-ATTACK.md](../TEMPLATE-ATTACK.md) tests Galois/symmetry “shields”; the campaign never proves that a counterexample specializes equivariantly.
- **Precise obstruction.** The exactly graded plane class is already automorphic, but a generic candidate’s lower terms destroy the action. Orbit closure can lose nonproperness or change degree, so GIT degeneration to a symmetric initial map does not preserve the property one needs to contradict.
- **Cheapest untried experiment — 4/10.** Compute stabilizers and one-parameter orbit limits of the smallest live boundary coefficient variety, and test whether any limit retains the collision/nonproper branch and the saturated Keller equations.

---

## II. Reductions and reformulations

### 23. The four-variable Hessian conjecture bridge

- **Essence.** Apply the standard doubling/gradient construction: proving the Hessian conjecture in four variables (HC4) implies JC2.
- **Campaign:** **No executed attack.** [RECON.md](../RECON.md) tracks the literature, but the repository has not tried the Hessian equations. The bridge is stated in [Meng–Yang 2026](https://arxiv.org/abs/2607.22198); the quartic HC4 case is reported proved in [Ni 2026](https://arxiv.org/abs/2608.14217), leaving degree at least five.
- **Precise obstruction.** Nilpotence of the Hessian controls homogeneous layers, but in degree five and above different layers can cancel; the top form being a cone is not yet enough to force the inverse/Legendre series to terminate.
- **Cheapest experiment — 9/10.** Reproduce the quartic cone/Schur argument symbolically, formulate the exact quintic obstruction module, and decompose its first uncancelled term under $GL_4$. This is the strongest adjacent live conjecture with a clean implication to JC2.

### 24. BCW cubic-homogeneous, Drużkowski, and symmetric/gradient stable reductions

- **Essence.** Stabilize a plane Keller map into a cubic homogeneous, cubic-linear, or symmetric gradient map and prove all maps in the target normal form invertible.
- **Campaign:** **No direct proof program.** The corpus uses many normal forms but does not classify the stable BCW image of plane maps; [RECON.md](../RECON.md) is reconnaissance rather than an execution.
- **Precise obstruction.** The unrestricted higher-dimensional target class now contains genuine counterexamples. A proof for *all* cubic/Drużkowski maps is therefore impossible. What may survive is a theorem for the narrow subclass produced from plane maps, but the reductions have not been augmented with invariants that recognize that subclass.
- **Cheapest experiment — 5/10.** Apply the explicit BCW reduction to several normalized plane maps and to the new three-dimensional counterexample, then compute stable invariants—rank flags, syzygies, isotropic subspaces, and grading data—that separate the plane-origin images.

### 25. Yagzhev algebras and Engel/nilpotence identities

- **Essence.** Translate a cubic homogeneous Keller map into a finite-dimensional nonassociative algebra; prove the relevant Engel identities force weak nilpotence and hence invertibility.
- **Campaign:** **No.** No Yagzhev-algebra computation or identity search appears in the executed campaign.
- **Precise obstruction.** Engel-type identities do not in general imply the required nilpotence in nonassociative algebras, and unrestricted higher-dimensional formulations inherit actual counterexamples. The plane-origin stable subclass would again need extra identities.
- **Cheapest experiment — 4/10.** Compute the Yagzhev algebras of BCW stabilizations of generic plane Keller jets and search, by low-degree PI linear algebra, for identities absent in the three-dimensional counterexample’s algebra.

### 26. Formal inverse, rooted trees, Feynman graphs, and coefficient cancellation

- **Essence.** Keller gives a formal inverse; express its coefficients as rooted-tree sums and prove all sufficiently large sums vanish or lie in the radical of the Jacobian relations.
- **Campaign:** **Partial.** [conjectureE-plan.md](../conjectureE-plan.md) and [lib/conjE.py](../lib/conjE.py) study a Magnus/remainder truncation, but the repository has not attacked the full rooted-tree expansion or a uniform termination ideal.
- **Precise obstruction.** Nilpotent-Jacobian identities do not kill every large tree, cancellations are global across many tree shapes, and no uniform truncation bound is known. Any unrestricted all-dimensional vanishing statement strong enough to imply general JC is now false; a plane-origin restriction must be isolated.
- **Cheapest untried experiment — 5/10.** Generate the first tree degrees for the four-variable gradient image of a generic plane map and compare their representation content with a generic Hessian-nilpotent map; look for a plane-specific ideal that kills the first otherwise surviving trees.

### 27. Hessian-nilpotent vanishing, Image/Mathieu conjectures, and Gaussian moments

- **Essence.** Translate inverse polynomiality into eventual vanishing of Laplacian powers, images of differential operators, or moments of a polynomial.
- **Campaign:** **Partial.** [MATHIEU.md](../MATHIEU.md), [MATHIEU-REVIEW.md](../MATHIEU-REVIEW.md), and [FACE-ISOLATION.md](../FACE-ISOLATION.md) test local Mathieu/constant-term and Wilson/Gaussian face isolation. The useful strip theorem was ultimately elementary; the hoped-for infinite moment tower is absent.
- **Precise obstruction.** The Keller bracket supplies a finite bilinear identity, not Wilson’s all-moment tower. Strong unrestricted versions that would imply JC in every dimension cannot survive the dimension-three counterexample. No demonstrably easier HC4/plane-doubling subspace of the vanishing problem is known.
- **Cheapest untried experiment — 5/10.** Derive the exact moment/Laplacian constraints on the four-variable doubled image of a plane quintic and test whether its special polarization removes the first general HC4 obstruction.

### 28. Generalized Magnus / Conjecture E remainder vanishing

- **Essence.** Prove a uniform sparse remainder-vanishing statement; in the repository’s implication chain, $E\Rightarrow D\Rightarrow C\Rightarrow B\Rightarrow A\Leftrightarrow\mathrm{JC2}$.
- **Campaign:** **Yes, at the smallest cap only.** [conjectureE-plan.md](../conjectureE-plan.md), [runs/conjE_results.txt](../runs/conjE_results.txt), [AUDIT.md](../AUDIT.md), and [CERT-UPGRADE.md](../CERT-UPGRADE.md) record six genuine exact characteristic-zero holds, one degenerate case, no failure, and a short two-row certificate.
- **Precise obstruction.** Only one minimal parameter tuple and bounded strata were checked. The quantification over all parameters, all $B$-subsets, and all degree tiers is the theorem; small Gröbner success supplies a motif, not an induction.
- **Cheapest untried extension — 7/10.** Use sparse $L^1$-style cofactor minimization to extract short identities in the next parameter tuple, then compare their supports with the two-row certificate to conjecture a uniform recurrence.

### 29. Dixmier, Weyl algebras, Poisson quantization, and spectral surfaces

- **Essence.** Quantize $\{P,Q\}=1$ to canonical commutator relations and prove the resulting Weyl endomorphism is onto; conversely exploit stable JC/DC correspondences.
- **Campaign:** **Yes in bounded DC(2) slices.** [DC2-PROGRAM.md](../DC2-PROGRAM.md), [DC2-REVIEW.md](../DC2-REVIEW.md), [cases/dc2_slice.py](../cases/dc2_slice.py), and [cases/dc2_deg3.py](../cases/dc2_deg3.py) classify degree $\le2$ points as automorphisms and expose genuine degree-three quantum/classical scheme divergence; degree four is already large. A defensive audit of a claimed DC1 proof in [ZHEGLOV-SCOPE.md](../ZHEGLOV-SCOPE.md) and [ZHEGLOV-LTEST.md](../ZHEGLOV-LTEST.md) found no small ODE counterexample but left expert-gated endgame gaps.
- **Precise obstruction.** The stable all-rank equivalence cannot prove a now-false generalized JC. For the still-relevant $\mathrm{DC}(2)\Rightarrow\mathrm{JC2}$ lane, the DC1 Schur-centralizer argument fails at step zero: $A_2$ has no comparable two-dimensional Schur normal form and has large noncommutative centralizers. Bounded slices neither cover arbitrary endomorphisms nor turn scheme divergence into a nonautomorphic point; even a valid DC1 proof would not itself prove JC2.
- **Cheapest untried extension — 5/10.** Decompose the degree-three and first degree-four quantum correction maps into $Sp_4$-irreducibles and compute them on highest-weight vectors before attempting another 1,000-equation brute-force solve.

### 30. Free-associative / noncommutative Jacobians

- **Essence.** Lift $P,Q$ to free words, invoke the much stronger free Jacobian theorem, and abelianize the inverse.
- **Campaign:** **No.** I found no noncommutative lift or free Gröbner experiment.
- **Precise obstruction.** A commutative determinant-one identity does *not* imply invertibility of the free Jacobian matrix; choosing commutator corrections that make it invertible is the entire missing problem. The free theorem assumes a condition strictly stronger than JC2.
- **Cheapest experiment — 2/10.** For the smallest unresolved commutative support, solve degree-by-degree for commutator corrections making the free Jacobian left-invertible. Expect failure at very low degree; that would document the gap cleanly.

---

## III. Arithmetic, analytic, and constructive/disproof routes

### 31. Positive characteristic counterexamples, Cartier theory, and Witt lifting

- **Essence.** Start from a separable noninjective plane Keller map in characteristic $p$, then construct compatible $W_n$-lifts and descend a fixed-support limit to characteristic zero.
- **Campaign:** **Yes.** [MONDELLO-CHECK.md](../MONDELLO-CHECK.md), [sol-witt.md](sol-witt.md), its review, and [AUDIT.md](../AUDIT.md) verify Mondello’s characteristic-two collision and compute the first Witt/Bockstein obstruction. On the registered hull-plus-one-shell stratum, all 1,152 cases have nonzero $W_2$ obstruction; 48 relaxed controls vanish but lose the guarded odd-degree geometry.
- **Precise obstruction.** Frobenius terms make characteristic $p$ radically different. A $W_2$ lift is already absent on the natural stratum; even one would still require compatible fixed-support lifts through every Witt level, a $\mathbb Z_p$-polynomial limit, and characteristic-zero descent. The three-dimensional datum lifting mod $4$ does not descend to a plane map.
- **Cheapest untried extension — 5/10.** Search low-support separable collisions over $\mathbb F_3$ and $\mathbb F_5$, compute their first Witt obstruction immediately, and retain only odd-characteristic $W_2$-survivors.

### 32. $p$-adic injectivity, Hensel lifting, adelic escape, and model theory

- **Essence.** Prove uniform $p$-adic bijectivity/injectivity for almost all primes, or transfer a first-order finite-field statement back to characteristic zero.
- **Campaign:** **Partial but not on the global implication.** The repository uses modular fibers and Hensel/Tougeron ideas in [SHEET6-DIRECTIONB.md](../SHEET6-DIRECTIONB.md), [cases/valuation_e.py](../cases/valuation_e.py), and [cases/eplus_certify.py](../cases/eplus_certify.py); a $p$-adic escape-mass route is only proposed in [sol-lateral.md](sol-lateral.md).
- **Precise obstruction.** Reduction mod $p$ can collide for purely arithmetic/Frobenius reasons, and good behavior at finitely many primes says little. Transfer needs a uniform degree/support bound, essentially the missing global compactness. Hensel lifting a solution of a truncated jet system would prove only that truncated system survives.
- **Cheapest untried experiment — 4/10.** Extract certified $\mathbb F_{p^2}$ or $\mathbb F_{p^3}$ smooth points on a D25 component, Hensel-lift them, and measure exactly which compatibility equation first fails; do not infer a Keller germ from the truncated lift.

### 33. Diophantine integral points, heights, and thin sets

- **Essence.** Spread a Keller pair over a number field and use integral points on fibers, height bounds, or Hilbert irreducibility to force multiple preimages or properness.
- **Campaign:** **No.** No arithmetic-geometry computation on integral points or heights appears in the corpus.
- **Precise obstruction.** Siegel-type theorems classify curves that *can have infinitely many* integral points; they do not guarantee even the two points needed by relevant reformulations. Uniformity across an unknown polynomial pencil and control of bad reduction are inaccessible without already controlling infinity.
- **Cheapest experiment — 3/10.** On one explicit surviving formal fiber model, compute genus, punctures, and the effective $S$-unit equation governing integral points; see whether the arithmetic condition adds anything beyond the existing place count.

### 34. Analytic global inverse theorems, coercivity, and pullback metrics

- **Essence.** Prove $F$ is proper, path lifting is complete, or the pullback Euclidean metric is complete; then use Hadamard/covering theory.
- **Campaign:** **No direct attempt.** Escape-to-infinity is studied algebraically, but no quantitative least-singular-value or metric-completeness estimate is attempted.
- **Precise obstruction.** Constant determinant controls volume distortion, not the smallest singular value. Large singular-value anisotropy and polynomial cancellation can carry an escaping path to a finite target. The explicit dimension-three counterexample demonstrates that no dimension-free metric slogan can work.
- **Cheapest experiment — 4/10.** For the simplest live two-pole formal route, compute asymptotic singular values of $DF$ along the branch and test whether the Keller/degree constraints force infinite or finite pullback length.

### 35. Real-plane methods, Pinchuk phenomena, dynamics, and SOS/CAD

- **Essence.** Seek a real constant-Jacobian collision to disprove JC2, or use real foliations, half-Reeb components, positivity, and global inverse criteria to prove injectivity.
- **Campaign:** **No.** Sparse rational SOS/Positivstellensatz was only proposed in [sol-lateral.md](sol-lateral.md); no real CAD or dynamical run was executed.
- **Precise obstruction.** Pinchuk maps have nowhere-zero but nonconstant Jacobian, so they are not counterexamples. Complex collisions need not have real points, so real positivity cannot prove complex JC2. SOS over the real locus is almost orthogonal to emptiness of a complex coefficient variety and scales terribly.
- **Cheapest experiment — 1/10 for proof, 3/10 for disproof reconnaissance.** Impose the simplest real-symmetric boundary ansatz, solve numerically for a collision, and exact-check any hit. Do not invest in global CAD unless a very small rigid ansatz first survives.

### 36. Symplectic/Lagrangian geometry and a two-dimensional tangent-sweep construction

- **Essence.** Regard $\{P,Q\}=1$ as an exact algebraic symplectic map; for disproof, adapt the 2026 tangent-line sweep/polynomialization mechanism while canceling its ramification in only two coordinates.
- **Campaign:** **No executed plane construction.** Related quotient/descent ideas occur only as proposals in [sol-lateral.md](sol-lateral.md) and literature reconnaissance in [RECON.md](../RECON.md).
- **Precise obstruction.** Noncompact symplectic local isomorphisms need not be proper, so symplecticity alone proves little. More concretely, the known sweep hides/polynomializes the bad divisor using a third coordinate; in two dimensions the ramification divisor has nowhere to go, and graded plane Keller maps are already automorphisms.
- **Cheapest experiment — 7/10.** Write the lowest-degree plane tangent-sweep ansatz with one controlled pole, impose polynomiality and determinant one as divisibility equations, and compute the saturation. Either a survivor reveals a new mechanism or a short unit identity exposes the two-dimensional no-go.

### 37. Restriction, quotient, or invariant-surface descent of the three-dimensional counterexample

- **Essence.** Find an invariant graph/surface, a one-LND quotient, or two target combinations on which the known $3$-fold Keller collision induces a plane Keller collision.
- **Campaign:** **No execution; explicitly proposed.** The one-LND quotient is listed in [sol-lateral.md](sol-lateral.md). The campaign’s Witt work notes that the literal three-dimensional datum can lift mod $4$, but that is not a descent.
- **Precise obstruction.** A constant $3\times3$ determinant gives no constant $2\times2$ minor after restriction or quotient. Natural quotients acquire a factor such as $\kappa L^2$, and arbitrary invariant surfaces destroy étaleness; a collision may disappear under the two target coordinates.
- **Cheapest experiment — 6/10.** Compute all low-degree polynomial invariants/semi-invariants of the counterexample’s evident vector fields and test every rank-two target combination for a constant induced Jacobian on an invariant graph.

### 38. Rational constant-Jacobian maps and pole removal (Vitushkin-type)

- **Essence.** Begin with a noninjective rational étale plane map and remove its poles by birational shears or blowdowns without introducing a third coordinate.
- **Campaign:** **No.** I found no rational-map construction or pole-cancellation solve in the repository.
- **Precise obstruction.** Clearing a pole changes the Jacobian or leaves base points; the simple Vitushkin covering shape is incompatible with known polynomial Keller geometry. Two dimensions offer no spare coordinate in which to absorb a denominator.
- **Cheapest experiment — 6/10.** Classify one-pole rational maps with constant rational Jacobian up to triangular birational changes, then solve the exact divisibility conditions for polynomial output and a retained collision.

### 39. Naive scaling/deformation to the linear part

- **Essence.** Use $F_t=t^{-1}F(tx)$ to connect a Keller map to its invertible linear part and argue invertibility cannot change with $t$.
- **Campaign:** **No—and it should not be pursued in this form.** No such proof appears in the corpus.
- **Precise obstruction.** Properness is not uniform in $t$; sheets can enter from or escape to infinity. The dimension-three counterexample deforms to its linear part, directly falsifying the naive deformation principle.
- **Cheapest experiment — 1/10.** None beyond documenting the escape divisor in the known counterexample. A viable deformation program would first need a new invariant controlling infinity uniformly, which makes it a different route.

### 40. Exotic affine surfaces, cancellation, and étale covers of pseudo-planes

- **Essence.** Construct a nontrivial quasi-finite étale map on a $\mathbb Q$-homology plane or exotic $\mathbb A^2$, then identify, cancel, or descend the source to the actual affine plane.
- **Campaign:** **No.** No exotic-surface construction appears in the campaign.
- **Precise obstruction.** Log Kodaira dimension, boundary graphs, Makar-Limanov invariants, and cancellation data usually distinguish these surfaces from $\mathbb A^2$. Stabilization or abstract diffeomorphism does not preserve a two-variable polynomial Keller presentation.
- **Cheapest experiment — 2/10.** Take the simplest known étale pseudo-plane cover and compute its boundary/Makar-Limanov invariants before and after one stabilization; test whether descent to $\mathbb A^2$ is already formally impossible.

### 41. Homology at infinity, intersection homology, motivic/$\mathbb A^1$ degree

- **Essence.** Attach a compactified or semialgebraic variety $N_F$, motivic degree, or local $\mathbb A^1$-degree whose nontriviality detects nonproperness, then force it to vanish from $J(F)=1$.
- **Campaign:** **No.** A local $\mathbb A^1$-degree idea is only listed in [sol-lateral.md](sol-lateral.md); no motivic or intersection-homology calculation was run.
- **Precise obstruction.** These invariants readily *encode* the unknown asymptotic set but the determinant condition supplies no known vanishing theorem for them. Local degree is already $+1$ at every point and does not prevent several separated sheets; global nonproper boundary terms are the missing information.
- **Cheapest experiment — 3/10.** Compute the local/global $\mathbb A^1$-degree balance and intersection homology for one explicit low-sheet nonproper model, checking whether it yields a constraint not already equivalent to sheet counting.

---

## IV. Computational proof and counterexample strategies

### 42. Direct coefficient ideals, Gröbner bases, saturation, and Nullstellensatz certificates

- **Essence.** Choose a finite support, impose $J(P,Q)=1$, normalize the torus, split all saturation charts, and certify that the coefficient ideal is the unit ideal—or extract an exact point.
- **Campaign:** **Yes, at very large scale.** [CAMPAIGN.md](../CAMPAIGN.md), [lib/reduce.py](../lib/reduce.py), [lib/reduce2.py](../lib/reduce2.py), [lib/reduce3.py](../lib/reduce3.py), [lib/chartelim.py](../lib/chartelim.py), [AUDIT.md](../AUDIT.md), and [CERT-UPGRADE.md](../CERT-UPGRADE.md) document the cascade and certificate work. Exact characteristic-zero certificates exist for the two transcribed $(72,108)$ systems. The rigid residue-A attack in [SHEET6-TEMPLATE.md](../SHEET6-TEMPLATE.md), [SHEET6-R1.md](../SHEET6-R1.md), and [SHEET6-R6.md](../SHEET6-R6.md) found a formal coefficient candidate and killed several strata before the surviving monoliths forced the move to jets.
- **Precise obstruction.** Variables and degrees explode, chart/saturation omissions manufacture false deaths, and solver truncation has manufactured false survivors. Modular $[1]$ is not a characteristic-zero proof. Naive CRT/rational reconstruction is defeated by prime-dependent normal forms and astronomical height bounds; direct cofactor lifts already stall around 27 variables. Above all, an exact leaf certificate does not prove the leaf census exhaustive.
- **Best next computational discriminator — 7/10.** Mine minimum-support human identities from modular Macaulay traces and replay them over $\mathbb Q$; in parallel, try a proof-producing fixed-support modular F4 trace rather than reconstructing arbitrary Gröbner bases.

### 43. Formal arcs, jet prolongation, finite determinacy, and Hensel–Tougeron lifting

- **Essence.** Prolong $J=1$ to increasing Puiseux depth, seeking either finite-window emptiness or a compatible formal germ via a uniformly invertible filtered Jacobian.
- **Campaign:** **Yes, deeply.** See [SHEET6-DIRECTIONB.md](../SHEET6-DIRECTIONB.md), [sol-newton-lemma.md](sol-newton-lemma.md), [sol-conjecture-k.md](sol-conjecture-k.md), [sol-h29-dichotomy.md](sol-h29-dichotomy.md), [AUDIT.md](../AUDIT.md), [cases/d25_certificate_replay.json](../cases/d25_certificate_replay.json), and [cases/d43_slices.py](../cases/d43_slices.py). D25 is modularly nonempty: each fiber has 16 disjoint $\mathbb A^{14}$ cells, 576 in the union. Sampled D43 points/slices die, but the symbolic family verdict is pending.
- **Precise obstruction.** Every extra depth adds equations *and fresh tail absorbers*. Finite jets do not imply an inverse limit, characteristic-zero point, algebraic series, or polynomial map. The abstract filtered Newton lemma is valid, but there is no live square block, finite loss $e^+$, causal all-depth right section, or proved CYCLIC/BRIDGE/FILTER/PARAM package; current lower bounds $e^+\ge37$ certify no Hensel conclusion.
- **Best next discriminator — 7/10.** Compute a characteristic-zero comprehensive triangular decomposition of the uniform D25 family and verify every raw row through the emission back-map; only then attack family-wide D43 elimination rather than sampling more points.

### 44. Finite-state and normal-form compilers for the sheet books

- **Essence.** Quotient arbitrarily long neutral words, coefficient histories, and merge records to a finite Markov state space on which every continuation can be decided.
- **Campaign:** **Yes, with several failed and scoped quotients.** [sol-normalform.md](sol-normalform.md), [NF-Z.md](../NF-Z.md), [NF-P.md](../NF-P.md), [NF-M.md](../NF-M.md), and [NF-D.md](../NF-D.md) build exact “fat” states and smaller candidate normal forms. The fat record is Markov but infinite; NF-M/P have scoped cores, NF-Z was repeatedly refuted, and NF-D closes only a bounded mechanism-A/td7 regime.
- **Precise obstruction.** Neutral cylinders retain unbounded ordered arithmetic and coefficient history. Any quotient coarse enough to be finite can merge states with different legal futures; the exact enumerator semidecides **ALIVE** configurations but cannot certify **DEAD** without a uniform kill or depth bound.
- **Best next discriminator — 6/10.** Implement the proposed Hall-deficiency dual from [sol-lateral.md](sol-lateral.md) on the first live neutral cylinder and test whether its certificate is invariant under arbitrary neutral extension. A single depth-dependent counterexample would retire that quotient cleanly.

### 45. Algebraization, Hermite–Padé, coefficient gluing, and toric-circuit closure

- **Essence.** Turn a compatible formal branch into bounded polynomial $P,Q$ by Padé rank conditions, synchronize coefficients across charts, and restore all monomial relations lost in linear relaxation.
- **Campaign:** **Yes, in three separate pilots.** [SOL-ALGEBRAIZATION.md](../SOL-ALGEBRAIZATION.md) kills one named completion but not the template; [sol-algkill.md](sol-algkill.md) shows separate bounded algebraic relations are too weak; [sol-gluing-design.md](sol-gluing-design.md) obtains a leading SAT pilot but exposes route-provenance loss; [sol-toric.md](sol-toric.md) finds no Tier-1 kill and a Tier-2 matrix with about 6.94 million columns.
- **Precise obstruction.** A shallow prefix cannot control a matrix consuming thousands of deeper coefficients; exceptional rank-drop loci may survive. Separate algebraicity of branches does not impose their *joint* Keller compatibility. Stored completion records discard alternate chart routes, while full toric closure reconstructs the original nonlinear problem at prohibitive scale.
- **Best next discriminator — 6/10.** Restore exact route/window provenance for one two-chart family and compute the smallest *joint* $P,Q,J=1$ Fitting ideal. Do not repeat a fixed-completion Padé rank test without quantifying the entire parameter locus.

### 46. Modular random slices, point counting, numerical homotopy, and finite-field reconnaissance

- **Essence.** Probe large varieties by random lines/planes, extension-field points, sparse ranks, witness sets, or point counts; reconstruct and certify any promising component.
- **Campaign:** **Yes as diagnostics.** [CAMPAIGN.md](../CAMPAIGN.md), [lib/linprobe.py](../lib/linprobe.py), [lib/lineprobe.py](../lib/lineprobe.py), [lib/planeprobe.py](../lib/planeprobe.py), and [runs/planeprobe_results.txt](../runs/planeprobe_results.txt) record zero-hit slices and resultant candidates. The campaign correctly retracted apparent nonempty outputs caused by killed/truncated processes.
- **Precise obstruction.** Zero hits cannot distinguish empty from thin positive-codimension or extension-field loci; numerical path failure is not emptiness. Modular components may be bad-prime artifacts, and even a smooth $p$-adic lift of a truncated system is not a polynomial Keller pair.
- **Cheapest untried extensions — 4/10.** Numerically decompose one 27-variable unresolved chart to learn component dimensions, then use exact modular associated-prime guesses and certified primary decomposition over $\mathbb Q$. Exact $\mathbb F_{p^2}$ extraction is useful only as falsification/reconnaissance.

### 47. Support-first exact counterexample search, SAT/SMT, symmetry, and ML-guided discovery

- **Essence.** Impose both $J=1$ and an explicit collision in a boundary-compatible sparse ansatz, use symmetry/graph structure or learning to propose supports, then rationally reconstruct and exactly verify a hit.
- **Campaign:** **Partial.** The coefficient templates, residue-A systems, finite-field probes, and Witt searches are structured searches, but there has been no systematic boundary-first plane collision search coupled to the currently minimal live $\mu=6$ data. Dense raw systems already reach hundreds to thousands of variables and OOM.
- **Precise obstruction.** Any counterexample has very high known lower bounds, while dense coefficient space is enormous and overwhelmingly populated by inconsistent points or known automorphisms. Exact counterexamples form an extremely thin algebraic locus; generic numerical optimization and evolutionary search are ill-conditioned. A bounded failure says nothing globally.
- **Cheapest untried experiment — 6/10 for sparse algebra, 1/10 for generic ML.** Build the smallest $\mu=6$, two-pole support with an explicit off-diagonal collision, quotient all torus/affine symmetries, inspect equation-variable treewidth, and run sparse block elimination. ML may rank supports, but every proposed hit must pass exact arithmetic.

### 48. Machine-exhausted finite universes, independently replayable certificates, and formal proof

- **Essence.** Separate and formally certify (i) completeness of the case generator, (ii) soundness of every reduction/chart/saturation step, and (iii) exact death of every leaf.
- **Campaign:** **Yes only at the leaf/identity layer.** [CROSSCHECK.md](../CROSSCHECK.md) independently replays the $(72,108)$ clients; [CERT-UPGRADE.md](../CERT-UPGRADE.md) records certificate limits and retractions; [lean/README.md](../lean/README.md) and [lean/Jc/Culprit.lean](../lean/Jc/Culprit.lean) verify two local identities without `sorry`.
- **Precise obstruction.** Formalization cannot manufacture a finite universe. The Lean files do not prove bracket provenance, elimination or saturation preservation, census completeness, GGV-to-sheet landing, or any Gröbner basis. A flawlessly checked leaf is irrelevant if a sector is omitted. Full formalization has high trust value but low discovery value.
- **Cheapest untried extension — 5/10 for rigor, 1/10 for solving JC2.** Formalize one `SystemA` bracket derivation, one Cascade M1/M2/M3 preservation theorem, and one exhaustive `INV/ZERO` chart split, then attach the existing culprit identity. In parallel, formalize the *next corner generator*, not another isolated endpoint.

---

## Comparative verdict

The approaches are not independent. The most credible direct proof architecture is a pipeline:


```text
arbitrary plane Keller pair
        |
        v
complete Newton/corner data
        |
        v
fiber-tagged Puiseux + resolved boundary tree
        |
        +----> proximity/log-surface inequalities
        |
        +----> nonproper-set components
        |
        v
coupled low-sheet monodromy / exact leaf obstruction
```

The campaign has strong pieces below the first arrow and many exact leaf obstructions at the bottom. It does **not** have the two global bridges that make the diagram a proof: universal landing/coverage and a finite bound. More brute force inside an already filed sector will not repair either gap.

The best adjacent proof experiment is HC4 in degree five. The best direct-plane experiment is one fully faithful GGV-chain-to-boundary-tree transport followed by a coupled two-coordinate $\mu=6$ test. The best disproof experiment is the lowest-degree two-dimensional tangent-sweep/pole-cancellation system, with descent of the explicit three-dimensional mechanism as a second lane.

Routes I would actively deprioritize unless a new invariant appears are naive scaling deformation, generic ML search, real SOS/CAD as a complex proof, free-associative lifting, and exotic-surface cancellation. Their obstruction is structural, not merely lack of compute.

## Selected field anchors

- Bass–Connell–Wright stable cubic reduction: [AMS article](https://www.ams.org/bull/1982-07-02/S0273-0979-1982-15032-7/S0273-0979-1982-15032-7.pdf).
- GGV Newton polygon algorithms and approximate roots: [algorithms](https://arxiv.org/abs/1708.07936), [approximate roots](https://arxiv.org/abs/1708.09367), [degree-frontier preprint](https://arxiv.org/abs/2204.14178).
- Generic fibers and coordinate criteria: [exact-differential formulation](https://doi.org/10.1016/0022-4049(90)90005-3), [injectivity on one line](https://arxiv.org/abs/alg-geom/9305008), [rational/simple fibers](https://arxiv.org/abs/0711.3894).
- Low topological degree and topology at infinity: [Orevkov](https://www.mathnet.ru/eng/im1571), [Neumann–Norbury](https://arxiv.org/abs/math/9805093), [Żołądek](https://doi.org/10.1016/j.top.2008.04.001).
- Nonproperness geometry: [Jelonek](https://arxiv.org/abs/2011.03472), [Valette–Valette](https://aif.centre-mersenne.org/article/AIF_2014__64_5_2147_0.pdf).
- Algebraic and arithmetic reformulations: [D-resultants](https://doi.org/10.1016/0022-4049(95)00116-E), [retracts](https://arxiv.org/abs/math/9701210), [$p$-adic formulation](https://doi.org/10.1016/j.jpaa.2014.09.018), [integral-points formulation](https://arxiv.org/abs/1709.03664).
- Hessian/vanishing and stable Dixmier routes: [Hessian-nilpotent vanishing](https://arxiv.org/abs/math/0409534), [Image/Mathieu](https://arxiv.org/abs/1006.5801), [stable Dixmier](https://arxiv.org/abs/math/0512171).
- Current dated boundary: [three-dimensional counterexample preprint](https://arxiv.org/abs/2608.00222), [graded plane maps](https://arxiv.org/abs/2607.20210), [HC4 $\Rightarrow$ JC2](https://arxiv.org/abs/2607.22198), [quartic HC4 preprint](https://arxiv.org/abs/2608.14217).
