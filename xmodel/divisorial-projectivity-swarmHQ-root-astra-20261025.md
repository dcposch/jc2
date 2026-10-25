# Projectivity of the actual divisorial compactification

Producer: swarmHQ coordinator and primary co-research lane, configured gpt-6-astra; actual hosted identity unmeasured.
Date: 2026-10-25 UTC
Basis: 8b1fb2c39449ccaeb8f3399c22b6ddb96c7acf52
Evidence tier: MANUAL / conditional; desk proof, independently reviewed internally.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending final public-artifact review.

## Statement and scope

Under the attached actual-divisorial package, the compact normal analytic target Y is projective.
There is an ample generator L of Pic(Y), with rho*L=L_E and n=L_E² a positive integer.
As Weil divisor classes L~nB, nB is Cartier ample, Cl(Y)=Z[B], and B²=1/n.
For each actual finite h_j:W_j→Y of degree e=N^j, W_j is projective and h_j,k_j are algebraic;
C_j is Q-ample with C_j²=1/(ne). No uniform index or degree bound is asserted.
Inputs: X is smooth projective rational, obtained by boundary blowups of P²;
E+D is an integral Picard basis, D has negative-definite connected blocks each attached to E,
and L_E.E=1, L_E.D_i=0, L_E²>0. The analytic contraction rho contracts precisely those blocks.
Also Y has rational singularities, Y\B is the marked whole A², and E→B is a normalization/homeomorphism with B topologically S².
These are retained published inputs, not re-proved or extended to the infinitely singular branch here.

## Dependencies and prior work

The [actual divisorial attachment](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md)
supplies these hypotheses under its adopted dynamical inputs and a divisorial eigenvaluation.
We retain the exact scopes of the [finite Stein factor theorem](finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md)
and [singular-ambient boundary theorem](singular-ambient-cusp-local-index-swarmHQ-root-astra-20261024T223151Z.md).
Their earlier correction and source-scope qualifications remain binding; no dynamical input is re-audited here.
Named standard imports are Leray, compact-support cohomology, the analytic exponential sequence,
GAGA, finite normalization, projective intersection theory, and Kodaira vanishing on smooth projective X.
For Kodaira's exact canonical-bundle factor, see [Vakil, The Rising Sea, July 27 2024, Theorem 21.5.8, p.625](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
That theorem statement was visually checked; its proof was not audited. No stopped Artin source or classification theorem is imported.
No novelty claim is made; this is a direct proof of the intermediate projectivity implication.
The generated EMPTY collision status is not a novelty certificate.

## Argument

### 1. A line bundle on the analytic target
Rational singularities give R^i rho_*O_X=0 for i>0, and normality gives rho_*O_X=O_Y.
Leray and rationality of smooth projective X yield H¹(Y,O_Y)=H²(Y,O_Y)=0.
For the open U=Y\B≅C², H_c²(U,Z)=H_c³(U,Z)=0.
The compact-support exact sequence therefore identifies H²(Y,Z)→H²(B,Z)≅Z.
This also follows from Y/B≅S⁴, but the exact sequence avoids an unstated quotient-cofibration step.
The exponential sequence now gives c₁:Pic_an(Y)≅H²(Y,Z).
Choose L corresponding to the generator of degree+1 on B; hence deg_E(rho*L)=1.
Set L_X=rho*L. Its degree on each D_i is zero because rho(D_i) is a point.
GAGA on projective X algebraizes L_X. Its intersections with the boundary basis identify c₁(L_X)=L_E.
On this rational boundary-blowup surface Pic(X) is free with unimodular intersection form;
H¹(X,O_X)=H²(X,O_X)=0, so numerical equality here is actual linear equivalence.
Thus L_X is the line bundle represented by the integral divisor class L_E, not merely a numerical surrogate.

### 2. Positive coefficients and the null locus
Write L_E=nE+Σb_iD_i in the integral boundary basis. Intersecting with L_E gives n=L_E²>0.
For each D block with matrix M and vector v_i=E.D_i≥0, the equations are M b=−n v.
The vector v is nonzero on every block. The inverse −M^{-1} is strictly positive on a connected block.
For completeness, −M is positive definite with nonpositive off-diagonal entries;
after a sufficiently large scalar rescaling, its inverse is a convergent nonnegative Neumann series,
and connectedness makes the needed entries strictly positive. Hence every b_i>0.
The coefficients n,b_i are integers because the boundary is an integral Picard basis.
If an irreducible complete curve T is outside the boundary, it must meet E+D: affine A² contains no complete curve.
All intersections of T with distinct boundary components are nonnegative and some are positive,
so L_E.T>0 by the positive coefficients. Also L_E.E=1 and L_E.D_i=0.
Thus L_X is nef, has positive square (hence is big), and its null curves are exactly the D_i.

### 3. An integral exceptional cycle and Kodaira vanishing
Choose an ample divisor H_0 on X. Put a_0=(H_0.L_E)/n>0.
Then H_0−a_0 L_E lies in the span of D; write H_0=a_0 L_E−Z_0.
Its block equations are M z=−(H_0.D_i), so Z_0 has strictly positive rational coefficients on ALL D_i.
Scale H_0 sufficiently, clearing denominators, to obtain
  H~aL_X−Z,
where a is a positive integer, Z is effective integral with support exactly D,
H is very ample, and H−K_X is ample. The class identity is linear equivalence by step2.
If D is empty, rho is already an isomorphism and projectivity is immediate; the rest treats D nonempty.
The visually checked Kodaira statement is H^i(X,K_X+A)=0 for i>0 and A ample, in characteristic zero.
Apply it with A=H−K_X. This gives H¹(X,H)=H¹(X,aL_X−Z)=0.
Consequently the exact sequence for the Cartier divisor Z gives a surjection
  H⁰(X,aL_X)→H⁰(Z,(aL_X)|Z).
Thus m=a suffices; no vanishing theorem on analytic or singular Y is invoked.

### 4. Fat components and section lifting
Write Z as the disjoint union of its fat connected components Z_t, supported over p_t=rho(D_t).
Choose disjoint neighborhoods of the distinct p_t on which the holomorphic line bundle L is trivial.
Pullback trivializes L_X on neighborhoods of the entire Z_t, including their nonreduced structures.
This does not assume the morphism Z_t→Y factors scheme-theoretically through the reduced point p_t.
All cohomology/section comparisons on X and its closed subscheme Z use GAGA.
Independent constant tuples (1 on Z_t, 0 on all other Z_s) are therefore sections on Z and lift by step4.
They remove base points on D and distinguish different connected contracted components.
The subsystem s_Z·H⁰(X,H)⊂H⁰(X,aL_X) removes every base point outside D.
On X\D, the factor s_Z is nonzero and this subsystem gives the very ample embedding |H|.
It therefore separates points and tangent directions there. Its coordinates all vanish on D,
so it also separates every point outside D from every image of a D component.
All global sections of aL_X descend: projection formula and rho_*O_X=O_Y give
  H⁰(X,aL_X)=H⁰(Y,L^a).
They are constant along each rho-fiber in local pulled-back trivializations.
The complete linear system |aL_X| is consequently basepoint-free and its fibers are exactly rho's fibers.

### 5. Projective normalization
The algebraic morphism f:X→P^r defined by |aL_X| has an integral projective image T.
By the section equality, L^a is basepoint-free on analytic Y and defines a holomorphic g:Y→T^an with f=g rho.
Step5 makes every g-fiber a singleton. Compactness makes g proper, hence finite; it is birational off the contracted points.
Normality of Y identifies it with the analytic normalization of T^an.
The finite algebraic normalization T^nu is projective and analytifies to that normalization.
Thus Y≅(T^nu)^an is projective. This is a finite-normalization argument, not an assumed contraction-uniqueness theorem.
Now GAGA algebraizes L; L^a=g*O_T(1) is ample by finite pullback, so L is ample.
Ample line bundles on Y have only been used AFTER this projective realization.

### 6. Boundary and Picard arithmetic
The morphism rho between projective varieties is algebraic by its graph/GAGA.
In particular the marked open Y\B is algebraically the original A², not just an unspecified analytic copy.
Push forward L_X~nE+Σb_iD_i, using a rational section of the now-algebraic L.
Exceptional terms disappear, and principal divisors push to the same rational functions; hence L~nB as Weil classes.
It follows that nB is Cartier and ample. Its degree against B is L.B=1, giving B²=1/n and L²=n.
The localization sequence and Cl(A²)=0 show Cl(Y) is generated by [B].
If mB is principal, its rational function restricts to an algebraic unit on A², hence a nonzero constant;
it is constant on dense U, so m=0. Therefore Cl(Y)=Z[B], and GAGA gives Pic(Y)=Z[L].
The Cartier subgroup is nZ[B]; n is the least positive global Cartier multiple of B, with no bound proved here.

### 7. Finite-iterate corollary
For actual finite analytic h_j, the finite coherent O_Y-algebra h_{j*}O_{W_j}, its unit and multiplication
algebraize by GAGA. Its relative Spec is finite/projective over Y and analytifies to W_j.
Thus W_j and h_j are algebraic/projective; the holomorphic k_j is algebraic by its projective graph.
With e=N^j, unique boundary ramification gives h_j*(nB)=ne C_j as Cartier divisors.
Finite pullback makes ne C_j ample, so C_j is Q-ample. The finite intersection formula gives
  (ne C_j)²=e(nB)²=en, hence C_j²=1/(ne).
This proves a Cartier multiple ne, not that ne is the exact index of C_j or a uniform index bound.
No R_j=0, R_j Cartier, W_j\C_j=U, finite self-germ, target descent, or properness of F follows from this proof.

## Replay and negative controls

Desk-only. The proof uses no computation or finite search. The fat-cycle step requires triviality
on a neighborhood of the entire nonreduced cycle, not merely on its reduced support.
Kodaira is applied only on the already projective smooth X. Numerical equivalence is upgraded
to linear equivalence using the rational boundary-blowup lattice, not for an arbitrary surface.
The construction and its exact hypotheses received independent configured Sol5.6 hostile review;
final artifact review and any promotion are recorded in [AUDIT.md](../AUDIT.md).

## Limitations and next test

The result applies to the attached divisorial package. The infinitely singular eigenvaluation branch remains open.
The ample Cartier multiple ne C_j is not asserted to be its exact Cartier index. There is no uniform bound on n or e.
No Gorenstein, klt, E8, R_j Cartier/zero, target-map descent, finite self-germ, properness of F,
or equality W_j-C_j=U follows. A further argument must constrain the actual joint global maps;
projectivity alone is not that argument. This is neither a proof nor a counterexample to JC2.

## OPENS RAISED

None. Existing omitted-boundary, descent, uniform-degree and infinitely singular gaps remain.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `8b1fb2c39449ccaeb8f3399c22b6ddb96c7acf52` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10993`.
- Body SHA-256:
  `290fd3f580993300dabae6ec5c9978122b59275e6368583e4e4be97ebc3efc1b`.
- Frozen basis: `8b1fb2c39449ccaeb8f3399c22b6ddb96c7acf52`.
