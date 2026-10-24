# Singular ambient cusps and the limits of local Cartier-index bounds

Producer: swarmHQ coordinator; local construction checked with the Astra-designated native co-researcher. Hosted identities/costs unmeasured.
Review provenance: separate hostile mathematical reviews assigned to gpt-5.6-sol; final public-artifact delta pending.
Date: 2026-10-24T22:30:15.337464+00:00
Basis: `83b30faaa6b5b12b8a232949e154a5a1f05d5e8b`.
Evidence tier: MANUAL, conditional compact theorem and explicit local diagnostic.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; promotion is recorded separately in the audit.

## Statement and scope

**Compact conclusion.** Let rho:X->Y be proper birational, X a smooth projective rational surface and Y a connected normal compact analytic surface.
Let B be nonempty, reduced and irreducible, with Y minus B=A2, and let the meromorphic volume genuinely identify omega_Y with the ideal I_B.
Assume the already established intrinsic conclusion that B has rational normalization and one ordinary cusp q, and is smooth elsewhere.
Then Y has rational singularities and is singular exactly at q. In particular it is smooth along B minus q.
The extra smooth-target-cusp hypothesis used in the preceding e<=5m argument is therefore impossible within these exact compact premises.
This does not contradict the local inequality itself and does not attach these premises to all Keller maps.

**Local diagnostic.** For every even integer e>=2 there is a rational normal algebraic surface germ S, a finite map h:S->A2 of degree e,
a birational morphism germ k:S->A2, and a reduced ordinary cusp C such that both maps induce cusp isomorphisms,
div(h*(Y^2-X^3))=eC, the pulled logarithmic forms agree, and the analytic local Cartier index of C is exactly m=e/2.
The rational formulas are compatible with iteration. This refutes a bound based on these displayed local data alone.
The affine k is not the campaign's globally proper map. No compact completion carrying both maps or whole-A2 polynomial Keller attachment is supplied.
These two statements concern different scopes: the local smooth target is not the compact target of the first statement.

## Dependencies and prior work

The compact premises and the intrinsic cusp are those of the
[finite-factor theorem](finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md) and its
[cusp/index follow-up](cuspidal-boundary-index-swarmHQ-root-astra-20261024T213422Z.md).
The new compact argument removes the earlier ambient-smoothness question by showing that the cusp is necessarily ambient-singular.
The local construction strengthens the previous source-only unbounded-index diagnostic by supplying an actual finite LOCAL h and compatible rational iterates.
It does not strengthen that diagnostic into an actual global Keller example. No novelty assertion is made.
Standard dependencies: compact Serre/proper duality and Leray, canonical-module adjunction via Ext, negative definiteness and adjunction,
Poincare duality, Noether's formula, normal valuation intersections, section-ring contraction, P1 cohomology, graded Nakayama and faithful flatness.
The normalized finite-trace rationality argument is proved in the preceding cusp/index package; no new external paper proof is imported.
The two HQ hostile reviews retained earlier governor/history/nonblind qualifications; they are mathematical critiques, not procedural-compliance certificates.

## Argument or computation

### A. Rationality of the compact target
Compact connected normal Y has only constant global holomorphic functions. Since B is nonempty, H0(Y,omega_Y)=H0(Y,I_B)=0.
Compact Serre duality gives H2(Y,O_Y)=0. Birational normality gives rho_*O_X=O_Y and R1rho_*O_X is supported on finitely many points.
Since H1(X,O_X)=0, the low-degree Leray sequence gives H1(Y,O_Y)=0 and H0(Y,R1rho_*O_X)=0.
Thus R1rho_*O_X=0; this is rationality of the normal surface singularities, and chi(O_Y)=1.

### Local lemma: a smooth canonical-ideal boundary cannot pass through a rational singularity
Let (S,p) be a normal rational surface germ and D a reduced smooth irreducible curve through p, with a genuine identification omega_S=I_D Omega.
Suppose p is singular. Take its minimal resolution pi:M->S and the strict transform D'.
The map D'->D is proper finite birational, hence an isomorphism because D is normal. In particular D' is smooth.
Rationality and proper duality give pi_*omega_M=omega_S and R1pi_*omega_M=0.
The Cartier residue sequence on M therefore pushes to an exact sequence
0 -> omega_S -> pi_*omega_M(D') -> omega_D -> 0.
On the other hand normality and the generic pole divisor of Omega put pi_*omega_M(D') inside O_S Omega: a coefficient regular at every codimension-one point extends across p.
The NON-CARTIER adjunction comparison is justified algebraically: applying Hom(-,omega_S) to 0->I_D->O_S->O_D->0,
using I_D isomorphic to omega_S and Hom(omega_S,omega_S)=O_S, yields 0->omega_S->O_S Omega->omega_D->0.
The maps agree with ordinary residues away from p, hence give the same map of torsion-free dualizing modules on D.
Since D'->D is an isomorphism, the upper residue map surjects onto the whole omega_D. Comparing the two exact sequences forces pi_*omega_M(D')=O_S Omega.
It follows that div_M(Omega)=R-D', where R is an EFFECTIVE exceptional divisor; there are no other nonexceptional zero or pole components locally.
Write the exceptional curves E_i. Rationality makes them P1, and minimality gives E_i^2<=-2.
Adjunction gives K_M.E_i=-2-E_i^2>=0. Thus R.E_i=K_M.E_i+D'.E_i>=D'.E_i>=0 for every i.
If R!=0, then R^2=sum r_i(R.E_i)>=0, contrary to negative definiteness of the exceptional intersection matrix.
If R=0, the same inequalities force D'.E_i=0 for every i. But D' must meet the exceptional fibre over p, also a contradiction.
Hence p was smooth. This proves the local lemma without assuming D Cartier, Q-factoriality or a quotient classification.

### Global exclusion of a smooth ambient cusp
Apply the lemma to every smooth point of B. Y is already smooth off B because its complement is A2, so q is the only possible singular point of Y.
Suppose Y is also smooth at q. The normalization map P1->B is bijective (the cusp is unibranch), hence a homeomorphism; B is a topological S2.
Collapsing B in compact Y gives the one-point compactification of A2, namely S4. The relative homology sequence gives H2(B,Z) isomorphic to H2(Y,Z).
Thus the fundamental class of B generates H2(Y,Z)=Z. Poincare duality makes its rank-one intersection form unimodular, so B^2 is either1 or-1.
Euler additivity gives c2(Y)=chi_top(Y)=chi_c(A2)+chi_top(B)=1+2=3.
Noether's formula for the smooth compact surface, with chi(O_Y)=1, gives K_Y^2=12-3=9.
But the genuine canonical-ideal identity now says K_Y=-B as Cartier divisor classes, so K_Y^2=B^2, a contradiction.
Therefore q is singular. This rules out only the smooth-ambient subcase, not the compact setup itself.

### B. A local finite-map construction
Fix an even integer e>=2. Put P_e(u)=(u+1)^e-(u-1)^e and R_e(u)=((u+1)^e+(u-1)^e)/P_e(u).
Its pole divisor D_e on P1 is reduced of degree e, contains0 and infinity, and is invariant under u->-u.
Define T=direct_sum_{n>=0} s^n H0(P1,O(floor(n/3)D_e)), inside C(s,u), and S=T^iota for iota(s,u)=(-s,-u).
T is normal: it is C(u)[s] intersected with coefficient-pole valuation rings off D_e and the Gauss valuation rings w_a(s)=1,w_a(u-a)=3 at D_e (use1/u at infinity).
Its third Veronese is A=direct_sum_{j>=0} s^(3j)H0(P1,O(jD_e)), the section ring of O(D_e); T=A[s], s^3 in A, finite free of rank3.
Thus T and S are finitely generated normal domains. Their positive-degree homogeneous maximal ideals define vertices; denote the vertex of Spec S by p.
The invariant field is C(s^2,s^3u)=C(x,y); hence k=(x,y)=(s^2,s^3u) is a birational morphism Spec S->A2.
Both generators belong to S because infinity is a simple pole in D_e.
Define h by X=e^2 s^2, Y=e^3 s^3 R_e(u). These are invariant regular functions.
Sections1 and R_e have no common zero as sections of O(D_e); their ratio defines the degree-e morphism R_e:P1->P1.
Consequently A is finite over C[s^3,s^3R_e]; adjoining s shows T finite over C[s,s^3R_e], hence over C[X,Y].
S is also finite over C[X,Y]. The same section argument shows that X=Y=0 has only the vertex above it.
Field degrees give [C(s,u):C(X,Y)]=2e and [C(s,u):Frac S]=2, so h has degree e.

### Rationality and the cusp
Let V=Spec_{P1}(direct_sum_{n>=0} O(floor(n/3)D_e)). It is finite over the total space O(-D_e).
This is the normalized base change of the usual contraction of the zero section to Spec A; therefore V->Spec T is proper birational.
At a point of D_e its local equation is v z=s^3, an `A_2` quotient singularity; away from D_e it is smooth.
`A_2` is rational by the finite quotient C2->C2/mu3 and normalized finite-trace argument already proved in the preceding index package.
Also H1(V,O)=direct_sum_{n>=0} H1(P1,O(floor(n/3)D_e))=0, since all the indicated divisors have nonnegative degree.
Resolving the `A_2` points and applying Leray proves rationality of T; the same normalized finite-trace argument for Spec T->Spec S proves rationality of S.
Let C in Spec S be the image of u=1 and u=-1. Restriction to (s,u)=(t,1) identifies its reduced coordinate ring with C[t^2,t^3].
Indeed degree1 invariants restrict to zero, degree2 contains s^2, degree3 contains s^3u, and every other nonnegative degree is in the semigroup generated by2 and3.
Thus C has one ordinary cusp at p. Both k|C and h|C are isomorphisms onto y^2=x^3 and Y^2=X^3 respectively; h acts on the normalization by t->e t.
Set g=Y^2-X^3. On s!=0, g=0 exactly at u=+/-1, with order e; at the other height-one loci over s=0, Y is generically nonzero.
Therefore div(h*g)=e C, with no other prime component, and the local Cartier index m exists and divides e.

### Exact log forms and index
Write Omega=dx wedge dy/(y^2-x^3). On the double cover it is 2 ds wedge du/(s^2(u^2-1)).
The identity R'_e/(R_e^2-1)=e/(u^2-1) proves h*Omega=k*Omega exactly.
At a finite pole a!=0 of R_e, the Gauss valuation gives order1 for this form; the two opposite poles are interchanged by iota.
At the fixed poles0,infinity, the quotient has generic ramification2; the descended form has order0 there. Elsewhere its sole pole is the simple pole on C.
Thus div(k*Omega)=R-C with R effective and supported on k-exceptional curves (the infinity divisor is not exceptional and has coefficient0).
Put J=s^3 (u^2-1)^(e/2)/P_e(u). Its coefficient is an odd section of O(D_e), so J belongs to S, and h*g=4e^6 J^2.
Hence div J=(e/2)C. In fact m=e/2, as follows.
If aC is Cartier at p, its graded divisorial ideal I_C^(a) has one generator after localization at the homogeneous maximal ideal.
Graded Nakayama gives one homogeneous generator f=s^n F(u) globally; analytic local principality gives the same conclusion by faithful flatness and descent of the one-generator condition.
Pullback to T is unramified generically along the two cusp branches. Vanishing along them is order a; along every pole divisor D_e it must be0.
The Gauss valuations force n=3j and div_{P1}F=a[1]+a[-1]-j D_e. Taking degrees gives2a=je.
Since J realizes j=1, the least positive such a is e/2. In particular both e and m are unbounded, while e=2m fits e<=5m.

### Rational-iterate compatibility

For M(u)=(u+1)/(u-1), one has R_e=M^(-1) composed with the e-th power map composed with M.
Thus R_a composed R_b=R_ab, and F_e(s,u)=(e s,R_e(u)) satisfies F_a composed F_b=F_ab.
A fixed even e0 gives the sequence e=e0^j and the displayed finite local normalizations. These are rational, not polynomial Keller iterates on the whole source plane.

## Replay and negative controls

Desk-only. The proof uses exact divisor, graded-ring, residue and topological arguments; no numerical experiment or formal certificate is claimed.
The canonical artifact manifest records the body/full hashes and frozen basis. The generated collision output is retained below.
The local example itself is the negative control: it has the finite-map data missing from the earlier weighted source-only example,
but does not possess the global proper-k/whole-plane attachment. The compact theorem expressly does not import its local smooth-target setting.

## Limitations and next test

The actual singular-ambient cusp case, missing global descent/finite self-germ, attachment to every Keller map and infinitely-singular case remain open.
The actual compact source still has a global restriction absent from the local model: every k-exceptional curve has a complete finite h-image meeting B at one boundary point.
That point is the cusp only for components meeting C at its cusp preimage; no argument puts every exceptional image there.
The affine chart's omitted branches do not prove that its germ is non-completable. What remains absent is an extension of both maps and the volume to the required compact diagram and whole polynomial plane.
Further work must use those global hypotheses or the singular ambient target. Neither a local index bound alone nor a new name for descent closes the missing implication.
No JC2 proof or counterexample is supplied.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `83b30faaa6b5b12b8a232949e154a5a1f05d5e8b` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13357`.
- Body SHA-256:
  `8872772c72014326d539054528bb74d86d1db5c134ff9be5d2ed56d26f6a2d1d`.
- Frozen basis: `83b30faaa6b5b12b8a232949e154a5a1f05d5e8b`.
