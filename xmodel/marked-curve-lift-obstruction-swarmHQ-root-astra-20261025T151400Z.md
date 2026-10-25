# A marked-curve obstruction to full lifts of the index-three cusp filtration

Producer: swarmHQ ROOT and primary Astra co-researcher; configured gpt-6-astra role, actual hosted identity unmeasured.
Date: 2026-10-25 UTC
Basis: db01d6034600ce8e85ed706db2d4e8fa4359f4fe
Evidence tier: MANUAL / CONDITIONAL on the explicitly imported dynamical and compactification results.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending final public artifact and ledger review.

## Statement, notation, and dependencies

The theorem below excludes every degree e>1 full homogeneous lift for this literal filtered algebra, with the specified injective Poisson central map. It does not settle JC2.
A homogeneous map of degree e sends each graded piece S_d into S_(ed). The Poisson bracket on S is
{X,Y}=T^7, {Y,W}=-2X, {X,W}=-5Y^4, with T central; A0=S/(T) has its induced bracket.
The symbol Y in the geometric argument denotes the projective surface, distinct from the generator Y in S.

The proof imports the [divisorial attachment](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md),
[projectivity and ample boundary](divisorial-projectivity-swarmHQ-root-astra-20261025.md),
and the [literal index-three compactification](global-static-index-three-swarmHQ-root-astra-20261025.md), at their stated scopes.
In particular, the Keller dynamical inequality lambda1>=N and the attachment package remain named conditional inputs, not new theorems proved here.
Other standard inputs are the DVR degree inequality, reconstruction from an ample Cartier Veronese,
rational-singularity/Leray vanishing, coherent cohomological dimension for one-dimensional fibres,
and connected local covers plus uniqueness of normal finite extension.
No new external source theorem or claim of literature novelty is made.

The six mathematical sections below are byte-identical to the independently reviewed HQ proof MARKEDCURVE1436.
Its reference CUSPFACTOR0603 denotes the full-lift reduction restated and checked in the appendix here.
The provisional exceptional-fibre assertion is reproved in section5; no assertion of ambient smoothness is imported.
The independent HQ review MARKEDVERIFY1457 returned PASS_CONDITIONAL; final public-artifact scrutiny is recorded separately in AUDIT.md.

## Exact reviewed argument

1. Exact theorem and dependencies
Let S=C[X,Y,W,T]/(X²−Y⁵−WT⁷), weights(5,2,3,1), and A0=S/(T).
There is no full homogeneous algebra lift S→S with T↦T^e, e>1, whose central map is an
injective degree-e Poisson endomorphism of A0 with the bracket specified in CUSPFACTOR0603.
This conclusion is conditional on the adopted Keller dynamical inequality λ1≥N and the
divisorial attachment/projectivity results at their stated scope, together with their named dependencies.
It concerns this literal filtration only: no all-JC2 conclusion, all-target classification, or new source theorem.
The reviewed full-lift reduction, not a truncated relation or localized solution, supplies the polynomial Keller pair.

2. Identify the actual target; do not attach a static example by assumption
Specializing a hypothetical full lift at T=1 gives F=(P,Q) with Jac F=1 and δ(F*f)=eδ(f).
Here w=x²−y⁵ and δ is the maximum weight in the unique normal form Σc_ijk x^i y^j w^k, i∈{0,1}.
The associated graded ring is the domain A0, so δ extends to a discrete valuation with sign reversed.
Its value group is Z, since δ(y)=2 and δ(w)=3. The static normal target Y=Proj S has boundary B=(T=0),
and ord_B(f)=−δ(f): a nonzero initial form does not vanish generically on the reduced integral boundary.
The normal form gives deg f≤(5/3)δ(f), while δ(f)≤5 deg f for nonconstant polynomials.
Applying these bounds to F^j yields λ1(F)=e. The source ord_B extends the target ord_B with index e;
the DVR degree inequality gives e≤N, so N>1 without invoking a birational-Keller theorem.
The normalized ν=ord_B/5 has thinness0 because div_Y(dx∧dy)=−B.
It has positive skewness: on a boundary resolution the class dual to B's strict transform is3ρ*B,
whose square is3 since B²=1/3; the adopted dual-class identity gives α(ν)=3/25>0.
Thus ν lies in the admitted divisorial eigenvaluation scope. With λ1≥N, the attachment theorem gives e=N,
unique boundary extension, and the actual finite h:W→Y' and proper birational k:W→Y' package.
To identify Y' with this Y, both have the whole marked plane and the same primitive boundary valuation.
For every m≥0, normality identifies H0(Y',O(mB')) with {f∈C[x,y]:δ(f)≤m}.
Indeed a section has no poles on the plane and the only remaining divisorial pole condition is along B'.
These spaces form exactly S, via X=xT⁵,Y=yT²,W=wT³; the normal-form basis proves equality degree by degree.
Since B' is ample Q-Cartier, a Cartier Veronese recovers Y' as Proj of this section ring. Hence Y'=Y over the marked plane.
No unknown finite-generation or target-map descent premise has entered this identification.

3. The marked polynomial curve and the degree obstruction
Put Γ=(W=0)⊂Y; in U it is x²=y⁵, parametrized by (x,y)=(t⁵,t²).
On B_smooth use q=W/z³ with X=z⁵,Y=z². Γ meets B only at p0:q=0.
In the Y-coordinate=1 chart X²=1+WT⁷, choose the branch X near1.
The residual μ2 action exchanges that branch with X near−1; W,T are genuine coordinates on the quotient near p0.
Thus p0 is smooth and B∪Γ is the transverse pair T=0 and W=0 there.
Suppose nonconstant polynomial coordinates p(t),q(t) have their infinity limit on B_smooth.
Weighted projective limits force deg p=5m, deg q=2m, deg r≤3m, where r=p²−q⁵ and m≥1 is integral.
Both leading X,Y coordinates must be nonzero; otherwise the boundary point is its singular cusp, not B_smooth.
Now q r'−5q'r=p(2q p'−5p q'). Its left side has degree≤5m−1, but any nonzero right side has degree≥5m.
Therefore both sides vanish. The derivative of r/q⁵ is zero, so r=c q⁵; the strict degree inequality forces c=0.
Every such polynomial image is consequently Γ, with boundary point p0. This is a direct lower-degree obstruction.

4. The actual map preserves Γ with normalization degree one
The adopted package has h^−1(B)_red=C, h*B=eC, and h_C:C→B an isomorphism.
Also k_C is an isomorphism: it is finite birational between the arithmetic-genus-one curves C and B,
so the finite normalization-defect cokernel has length zero. Proper normal birational k has connected fibres.
Its open identity section over U is an isolated point of each fibre, hence k^−1(U)=U.
Lift the normalization P1→Γ to the strict transform in W. Properness extends the lift over infinity.
Its k-image there is p0. The polynomial F(t⁵,t²) is nonconstant by quasi-finiteness, hence its infinity limit
cannot lie in affine U. Its h-image is on B, so the lifted point lies on C and equals a=(k_C)^−1(p0).
The point h(a) is smooth on B; section3 forces h(a)=p0 and F(Γ)=Γ.
The induced map on affine normalizations is a nonconstant polynomial g:C→C.
An ambient étale local isomorphism cannot send a smooth Γ germ to its irreducible singular cusp germ,
nor send that cusp germ to a smooth Γ germ. The image germ, being reduced and one-dimensional, is the entire Γ germ.
Thus g^−1(0)={0}, and the cusp maps to itself by a local curve isomorphism, giving ord_0(g)=1.
Consequently g(t)=a0 t with a0≠0. The strict Γ map has normalization degree one, including at infinity.

5. Every possible branch image through p0 is Γ
For completeness, the needed provisional RAMCURVE fibre assertion follows without ambient smoothness of W.
Resolve W by π:X→W. Rationality of Y gives R1(kπ)_*O_X=0; π_*O_X=O_W and Leray give R1k_*O_W=0.
For the reduced exceptional fibre F_p, the ideal sequence and R2k_*I_Fp=0 give H1(F_p,O_Fp)=0.
The R2 vanishing is the coherent cohomological-dimension bound for this projective morphism with fibres≤1.
For each irreducible reduced component E, O_Fp→O_E and H2 of its coherent kernel=0 imply H1(E,O_E)=0.
Normalization genus plus defect length is therefore zero: E is intrinsically smooth P1, even if W is singular there.
Ampleness of Q-Cartier C forces E∩C nonempty. Since k_C is an isomorphism and k(E) is one point,
E∩C is a singleton; E\C is consequently an intrinsic A1. No SNC structure on W is assumed.
Finite h maps E to a curve D≠B, and D∩B=h(E∩C) is one point, because h^−1(B)=C set-theoretically.
The coordinate functions of h on E\C are polynomials on A1. If D contains p0, section3 gives D=Γ.
There are finitely many exceptional curves. Shrink a target neighborhood of p0 to avoid all other h(E).
Outside B and the h(E), every preimage belongs to actual U, where F is étale; hence the branch locus
in this neighborhood is contained in B∪Γ. This argument needs no purity theorem or singular-branch classification.

6. The fixed-sheet SNC-cover contradiction
The fibre h^−1(p0) is the single point a, since it lies on C and h_C is an isomorphism.
Choose the finite representative over a sufficiently small coordinate bidisc (u,v), with B:u=0 and Γ:v=0.
Remove the FULL inverse of B∪Γ, not merely C or the ramification support.
The normal irreducible source germ minus this analytic divisor is connected; it gives a connected degree-e
unramified cover of (Δ*)². Its two meridians commute and their permutation action on the e sheets is transitive.
The actual strict Γ branch punctured at a lies in U. At a nearby point its ambient map is étale,
so the Γ-meridian fixes one sheet (transport to a common basepoint only conjugates that meridian).
In a transitive abelian permutation group an element fixing one point fixes every point.
Thus the Γ-meridian acts trivially, and the B-meridian is a single e-cycle.
The covering subgroup is eZ×Z. Holomorphic covering equivalence followed by uniqueness of normal finite extension
identifies the germ over the entire bidisc with (s,t)↦(s^e,t).
Its full inverse Γ is one smooth curve t=0, with local normalization degree e over Γ at p0.
The actual strict Γ branch must be that curve, contradicting its normalization degree one from section4.
Therefore no e>1 full lift with the stated central hypotheses exists, conditional on the adopted package.
This uses a fixed sheet only inside one connected local cover; no global sheet labels or missing descent are assumed.
The optional p,q generalization is not pursued or asserted; no coefficient or local-family successor is authorized.

## Appendix: a full lift supplies a polynomial Keller pair

Write U=Phi(X), V=Phi(Y), H=Phi(W), so U^2-V^5=T^(7e)H.
The prime element T does not divide U, since the induced map on A0 is injective.
Bracketing with V gives -2U{U,V}=T^(7e){V,H}, so T^(7e) divides {U,V}.
The bracket is homogeneous of degree zero; U and V have weights5e and2e.
Thus {U,V}=cT^(7e) for a scalar c, and cancellation gives {V,H}=-2cU.
Modulo T, the Poisson property of the central map gives {V0,H0}=-2U0; U0 is nonzero, so c=1.
Specialization T=1 therefore gives polynomial P,Q with {P,Q}=1.
Injectivity of the map on the associated graded ring gives delta(F*f)=e delta(f) for every nonzero f.
This is the exact full-relation reduction previously checked independently in CUSPVERIFY0633; no classification of central maps is needed here.

## Replay, provenance, and negative controls

Desk-only. The argument is uniform in e>1; no coefficient cutoff or sampled computation is used.
The source proof has full SHA256 `25e9c6d423a83882b7c2096f5254df8c2b087809b7a460a712cd300c60c5b55e`, HQ basis `781230fc84169e0e2c9370b43de1020388bd5be8`.
The independent HQ review has full SHA256 `a37abccd2ff8c5d5102fc7cd1876ef95cc6af49c7854fbfa8183563b55a16b2e`, HQ basis `1ccbe69c2fc98e35efb90ce86434d6aa59da95f9`.
The published argument preserves the exact six-section source substring; its own manifest records the public basis and canonical bytes.
Local or punctured-source controls whose affine complement is not the entire marked plane do not satisfy the actual-source hypotheses used here.
Removing only the ramification support instead of the full inverse of both axes would not justify the covering argument.

## Limitations and next test

The other divisorial compactifications and the infinitely singular valuation branch remain open.
The proof needs the unique polynomial curve meeting this smooth boundary, its transverse boundary intersection,
and the actual compactification package. It supplies no general classification or automatic reduction to this target.
No general p,q extension, local/formal-only obstruction, or new unconditional source theorem is asserted.

## OPENS RAISED

None. The remaining campaign gaps are retained; this report creates no new bounded OPEN entry.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `db01d6034600ce8e85ed706db2d4e8fa4359f4fe` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12897`.
- Body SHA-256:
  `271c229fae88a7e42c3e057824cedc3f0eb0659b0767c0b86ba5d790c04922d3`.
- Frozen basis: `db01d6034600ce8e85ed706db2d4e8fa4359f4fe`.
