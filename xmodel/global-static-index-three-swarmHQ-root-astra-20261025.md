# A projective whole-plane compactification with canonical index three

Producer: swarmHQ ROOT and primary Astra co-researcher; configured model role gpt-6-astra, actual hosted identity unmeasured.
Date: 2026-10-25 UTC
Basis: 318c2eb42c209b13915527794d5f1fa8faf58721
Evidence tier: MANUAL; exact static construction, independently reviewed in HQ.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending final public artifact and ledger review.

## Statement and scope

Let S=Proj C[X,Y,W,T]/(X²−Y⁵−WT⁷), with weights (5,2,3,1), and B=(T=0).
Then S is a normal projective compactification of the entire marked A², singular only at the ordinary cusp of B.
Its singularity is rational, its genuine dualizing sheaf is I_B·(dx∧dy), and both the canonical index and the Cartier index of B are exactly three.
Moreover Cl(S)=Z[B], Pic(S)=Z[3B], 3B is ample, B²=1/3, and the integral dual class on a common boundary blowup has square three.
This single example refutes an index-one/Gorenstein inference from that static whole-plane canonical-boundary package.
It supplies no actual finite factor h, simultaneous source projection k, iterate, Keller-eigenvaluation attachment, or polynomial Keller pair.
The common static boundary resolution constructed below is distinct from such an actual h/k pair. This is not a JC2 counterexample.

## Dependencies and prior work

The [divisorial attachment](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md) and
[projectivity theorem](divisorial-projectivity-swarmHQ-root-astra-20261025.md) explain the target package being tested;
no actual-Keller hypothesis from those results is asserted for this example. The construction is proved directly below.
The proof uses standard Serre normality, reflexive extension on normal surfaces, hypersurface residues,
projective Serre duality, Leray, rational-surface cohomology, divisor-class localization and resolution of surface birational maps.
No classification of singularities, Gorenstein assumption, or unread external source is imported.
The earlier local-only index-three test does not by itself supply this global compactification. No claim of literature novelty is made.

## Argument

1. Normality and the marked open plane.
The equation is irreducible: as a polynomial linear in W its relatively prime coefficients are T⁷ and X²−Y⁵.
The affine cone is a three-dimensional hypersurface, hence Cohen–Macaulay.
Its gradient vanishes exactly on the W-axis: X=Y=T=0. This locus has codimension two in the cone.
Serre's criterion gives a normal graded ring and hence a normal projective surface S.
On T≠0 put x=X/T⁵, y=Y/T², w=W/T³. The equation becomes w=x²−y⁵.
Thus S\B is exactly Spec C[x,y], with its entire marked polynomial plane, not a local germ.
R/(T)=C[X,Y,W]/(X²−Y⁵) is a domain, so B is reduced and irreducible.

2. Singularities and the boundary scheme.
The weights are pairwise coprime. A point with at least two nonzero coordinates has trivial stabilizer.
The X-only and Y-only coordinate points do not lie on S; the only possible nontrivial stabilizer on S is q=[0:0:1:0].
The cone is smooth off the W-axis, so S is smooth outside q.
On W=1 the index chart is V: a²−b⁵−c⁷=0, modulo μ₃ acting with weights (2,2,1).
The equation has character 1 modulo 3; V is a normal isolated hypersurface singularity, and the action is free off its origin.
The graded normalization of the boundary ring is C[u,v], with weights (1,3), via X=u⁵,Y=u²,W=v.
Indeed u is integral and u=X/Y² in the fraction field. The induced finite normalization is P(1,3)≅P¹.
At v=1 the actual reduced boundary ring is C{u²,u⁵}^{μ₃}, where u↦ζu.
The semigroup <2,5>∩3Z is <6,9>, because 3 is missing and every integer ≥4 lies in <2,5>.
Consequently this invariant ring is C{u⁶,u⁹}=C{s²,s³}, s=u³: an ordinary cusp.
Taking invariants commutes with the stable boundary quotient in characteristic zero, so this computes the boundary scheme, not merely its parametrization.
Away from q, u≠0 and the coordinate v/u³=WY/X identifies B\{q} with A¹.
Thus normalization is bijective, an isomorphism away from the cusp, and a homeomorphism on complex points.

3. The genuine canonical sheaf and its exact index.
Use Ω=dx∧dy from the marked plane. On the Y-coordinate=1 chart, X²=1+WT⁷ and x=X/T⁵,y=T⁻².
Direct differentiation gives dx∧dy=−2T⁻⁸dX∧dT=−(XT)⁻¹dW∧dT.
Every point of B\{q} lies in this chart, where X=±1 and the residual μ₂ action is free.
Hence Ω has a simple pole along B and no other divisorial zero or pole: div_S Ω=−B.
A normal surface is Cohen–Macaulay and its genuine dualizing sheaf is reflexive.
The codimension-one identification therefore extends across q: ω_S=I_B·Ω, abstractly ω_S≅O_S(−B).
This is not an identification with the pushforward of the canonical sheaf of a resolution.
On V the residue generator η=db∧dc/(2a) of its dualizing sheaf has μ₃-character 2+1−2=1.
The expression is interpreted by the hypersurface residue construction, including where this displayed denominator vanishes.
Since V→S is étale away from the origin, η³ descends to trivialize ω_S^[3] on the punctured germ and hence reflexively on the germ.
Conversely, if ω_S^[m] were Cartier, its local generator would pull back on V\{0} to fη^m with f a nowhere-zero holomorphic function.
Normal extension of both f and f⁻¹ makes f a unit on V, in particular f(0)≠0.
Invariance gives f(ζp)ζ^m=f(p), and evaluation at 0 forces 3|m.
Thus the canonical index and the local Cartier index of B are exactly 3; q is indeed singular.
No assertion that the hypersurface cover V has rational singularities is used or made.

4. Rational singularities of the quotient surface.
Take a smooth projective resolution ρ:X→S. The dense A² makes X a rational projective surface, so H¹(X,O_X)=0.
Global functions on the connected projective S are constant; B is nonempty. Hence H⁰(S,ω_S)=H⁰(S,I_B)=0.
Serre duality for the projective Cohen–Macaulay surface gives H²(S,O_S)=0.
Normality gives ρ_*O_X=O_S. The Leray exact sequence injects H⁰(S,R¹ρ_*O_X) between the two zero groups H¹(X,O_X) and H²(S,O_S).
Therefore H⁰(S,R¹ρ_*O_X)=0. This coherent sheaf has finite support, so it is zero.
Thus S has rational singularities. Also H¹(S,O_S)=0 by Leray.
This argument uses projectivity already established directly, not an assumed analytic algebraization or singularity classification.

5. Picard/class groups, ampleness and intersection numbers.
The index calculation and smoothness elsewhere show that 3B is globally Cartier and mB is Cartier exactly when 3 divides m.
The standard sufficiently divisible weighted Proj line bundle O_S(30) is ample; its section T³⁰ has divisor 30B.
Consequently 3B is ample, since its tenth tensor power is ample.
Localization gives Cl(S) generated by B, since Cl(A²)=0.
There is no nonzero principal multiple of B: the corresponding rational function is a unit on A² and therefore constant.
Thus Cl(S)=Z[B]. The Cartier criterion gives Pic(S)=Z[3B].
The pullback of O_S(3B) to the normalization P(1,3) is O(3), of degree one on P¹.
Explicitly, local equations for 3B are T³/W near q and T³Y/X away from q; their transition on the boundary normalization is u³/v.
Equivalently the section W restricts to v, with one simple zero at v=0 in coordinate v/u³ and no zero at q.
Hence (3B).B=1, B²=1/3 and (3B)²=3. Also K_S²=1/3 as a rational intersection number.
The Hilbert-series leading coefficient 10/(5·2·3·1)=1/3 independently agrees, but is not needed for the intersection proof.

6. The static boundary-blowup package.
Resolve the pair (S,B), then resolve the birational map from the marked P² to that resolution, without changing A².
This yields a common smooth projective model X obtained from P² by point blowups on the boundary, and a morphism ρ:X→S.
Its boundary can be SNC; its graph is a tree. The unique component E dominating B is its normalization P¹.
All other boundary components D are ρ-exceptional. Each connected D block meets E at one point by the tree property.
They are contractible by the already constructed ρ, and their intersection matrix is negative definite.
For example Hodge index applies to ρ*(3B), which has positive square and is orthogonal to these independent exceptional classes.
The integral dual boundary class L_E=ρ*(3B) satisfies L_E.E=1, L_E.D_i=0 and L_E²=3.
At the generic point of E, ord_E Ω=−1. No E₈, Gorenstein, finite-self-germ or Keller-eigenvaluation premise was inserted.

## Replay and negative controls

Desk-only proof. The boundary invariant ring is computed exactly, not by finite semigroup enumeration.
The index cover is not assumed to have rational singularities: rationality of S follows from the independent global duality/Leray argument.
The Hilbert-series check in section5 is supplementary; the boundary line-bundle transition proves the intersection number.

## Limitations and next test

This is one exact static target. It proves neither an unbounded-index family nor a uniform index bound.
An actual finite h/proper k pair, its volume compatibility and the polynomial Keller source remain additional conditions.
Future progress must use such an actual-map constraint; a static Gorenstein shortcut is insufficient even after projectivity and the whole-plane complement are known.
No target-map descent, omitted-boundary exclusion, properness of F or infinitely singular valuation result is obtained.

## OPENS RAISED

None. The existing actual-map gap remains; no new control-family or classification task is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `318c2eb42c209b13915527794d5f1fa8faf58721` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9850`.
- Body SHA-256:
  `e6bbe260ffb898a63ce1ca80b1bdffd15924d2c9ff1627fb1e145e4673771409`.
- Frozen basis: `318c2eb42c209b13915527794d5f1fa8faf58721`.
