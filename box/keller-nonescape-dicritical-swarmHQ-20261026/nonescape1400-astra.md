# NONESCAPE1400 — compact thinness, and the dicritical class correction
Status: INTERNAL / MANUAL / UNPROMOTED co-research. JC2 remains unresolved. ROOT co-researched, not independently reviewed.
Launch: 0ce7416c9d8c088e883a5f22b4967bba4e1ea27b; frozen public: 3a60479fcfb114451c6e78da554af39707c518a7.
## Scope and outcome
Let F=(P,Q):A2->A2 be an actual complex polynomial Keller map, det DF=1, with finite field extension K/K0, K0=F*K and degree N. Set Omega=dx wedge dy. Normalize infinity valuations by value -1 on a generic affine linear function. Let A be FJ thinness and d(F,w)=-min{0,w(P),w(Q)}.
At the named plane-valuation foundation tier stated below, we prove d(F,w)>0 on T={w in V0:A(w)<=0}; compactness then gives a constant c_F>0 with d>=c_F on T. This does not prove polynomial properness.
We also identify the exact dicritical coefficient in the finite-model class comparison. It remains outside T and prevents inferring a preimage-only A7 identity from this nonescape statement. Full discrepancy equality for other infinitely singular extensions, and hence their membership in T, remains unproved here.
The Oct16 journal5239–5288 already records divisorial discrepancy conservation and the missing harmonic/uniform-approximation consumer. Those old observations are not counted as new. The present changes are the explicit differential-inequality/compactness argument and the actual dicritical pairing, not a renewed conservation argument.
## Foundations and source limits
We use the FJ plane-valuative tree framework, including its named [28]/[30] foundations: normalized V0 is compact; A is increasing and lower semicontinuous; alpha is decreasing and upper semicontinuous; nondivisorial valuations admit divisorial ancestors along their tree path converging to them. The underlying classification/retraction proofs were not audited and remain a named foundational premise, not a new source admission.
For finite A, these ancestors w_j can be chosen increasing. Monotonicity gives A(w_j)<=A(w), while lower semicontinuity at w gives A(w)<=liminf A(w_j); hence A(w_j)->A(w). This uses both properties, not lower semicontinuity alone. Divisorial w requires no limit.
Curve valuations have A=+infinity: after the finite resolution of their formal plane branch, successive blowups following its smooth strict transform leave the line-pole multiplicity fixed and add 1 to the primitive discrepancy at every step. Thus T consists of field valuations, not polynomial semivaluations with a nonzero kernel. This uses the same formal plane-branch foundation.
FJ244–291 supplies compactness, semicontinuity and V1={alpha>=0,A<=0};327–374 supplies d and the truncated infinity pushforward. A=0 alone is not V1. FJ1420–1539 supplies the boundary class conventions, projection framework, continuity and nefness statements used below. FJ1555–1590 explicitly imposes properness in A7. None of its nonproper conclusion is imported.
## A differential inequality valid at finite thinness
For nonconstant algebraically independent rational functions f,g in K, put df wedge dg=J(f,g) Omega. For every finite-thinness w at infinity,
    A(w) >= w(f)+w(g)-w(J(f,g)).                                      (1)
First take primitive divisorial w=ord_E on a smooth model. At its generic point write a parameter u for E, f=u^m f0 and g=u^n g0, with f0,g0 units; integers m,n may be negative. Differentiation shows ord_E(df wedge dg)>=m+n-1. Since ord_E(Omega)=A(ord_E)-1, this is exactly (1). Positive rescaling gives the normalized statement.
For an arbitrary finite-thinness w use the ancestors above. Values of the three nonzero rational functions converge, because their polynomial numerators and denominators have finite values at w. The equality lim A(w_j)=A(w), already justified using monotonicity and lower semicontinuity, passes (1) to w. No finite-map equality at a limit has been assumed.
## Excluding the whole zero set of d on T
Suppose d(F,w)=0 for w in T. The RAW restriction v(H)=w(H composed F) is nonnegative on C[X,Y]. It is not the zero valuation: a nontrivial valuation on a finite algebraic field extension cannot restrict trivially, since the minimal polynomial of an element of nonzero value would have a unique term of least value. This argument applies to either sign of that value.
The centre prime {H:v(H)>0} is therefore nonzero, hence either an affine closed point or the generic point of an irreducible affine curve. This is the raw valuation, not the zero object assigned by FJ's truncated infinity pushforward when d=0.
At a closed centre (a,b), use f=P-a and g=Q-b. Both values are strictly positive, and J(f,g)=1. Inequality (1) forces A(w)>0, contradicting w in T.
At a generic curve centre C={c(X,Y)=0}, choose an affine linear g0 with g0 not in (c) and J(c,g0) not in (c). Such a choice exists in characteristic zero: an irreducible c cannot divide all of its nonzero first derivatives. Use f=c(P,Q), g=g0(P,Q). Then w(f)>0, w(g)=0 and w(J(f,g))=v(J(c,g0))=0, since det DF=1. Again (1) forces A(w)>0.
Consequently T avoids {d=0}. T is closed by lower semicontinuity and compact because V0 is compact. The displayed finite-minimum formula for d is continuous: polynomial evaluations are continuous in the FJ topology and min with 0 removes any positive-infinite endpoint. Therefore d attains a strictly positive minimum c_F on T.
This controls every sequence or net already lying in T. It gives no positive lower bound on all of V0 and no claim that valuations with A>0 cannot be dicritical.
## The unproved E step
For an actual extension w over the infinitely singular eigenvaluation nu, the reviewed value-group result supplies residue C, infinite singularity and index prime to lambda; the eigenextension has e=f=1. It does not supply A(w)=0. The displayed FJ Jacobian argument restricted to V1 cannot be applied before proving that membership.
An adapted finite normalization/cyclic-cover route would additionally need a separated free target model, control of every extension, analytic-cover classification and exact analytic-to-rational discrepancy transfer. We have not completed those obligations and do not assert the general raw equality A(w)=A(v) in compatible unnormalized scaling. The compact minimum alone does not establish E.
No follow-up on E is automatically proposed: even granting E in its strongest form does not remove the class correction below.
## Exact finite-model dicritical coefficient
Choose admissible smooth compactifications and a morphism g:X->Y resolving the actual polynomial map. Let D be a target boundary prime and nu=ord_D/b_D. Let Z_nu be its FJ dual class, so (Z_nu.D')=delta_(D,D')/b_D for target boundary primes D'. Let E be a source boundary prime mapping onto the closure of an affine irreducible curve C={c=0}, with curve degree f_E=[C(E):C(C)].
Projection and the principal divisor of c on Y give the exact equalities
    (g*Z_nu.E)=f_E (Z_nu.closure(C))=-f_E nu(c).                       (2)
Indeed closure(C) is linearly equivalent to -sum_(D') ord_(D')(c) D'. No properness of the original affine map is used; g is a morphism on the chosen projective models.
For a boundary E mapping onto D itself the corresponding pairing is f_E/b_D; for one mapping onto a different boundary prime or a point it is zero. Thus expansion in the source dual-boundary basis contains the coefficient -f_E nu(c) multiplying Z_ordE for this dicritical E. It is not a term belonging to a boundary valuation preimage of nu.
A sum only of dual classes of boundary divisorial preimages of nu pairs zero with this E on a model containing those divisors. Whenever nu(c)<0, (2) therefore rules out that preimage-only class identity. Under nu in V1 the coefficient is nonnegative, since FJ Lemma A.3 proves nu(c)<=0. At the precise infinitely singular target used here it is strictly positive, as proved below; this is not a statement for arbitrary V1 valuations.
The condition A(E)>0, which follows from the zero-set argument after normalization, merely places E outside T. It does not delete E from the boundary divisor basis, and so cannot set the coefficient in (2) to zero.
## The infinitely singular target: a fixed-divisor statement, not an infinite expansion
For a chosen dicritical E, first take a target model separating the centre of the infinitely singular nu from the strict transform of C. This is a finite separation of a noncurve valuation from a fixed algebraic curve, within the named plane-valuation framework. Resolve the source map to this model. The strict transform of the chosen E still maps onto C and its entire image avoids that centre.
Take divisorial ancestors nu_j after this separation, and refine target models along nu only. These blowups miss C; the source resolutions may be chosen away from E. Thus E is unchanged and its strict transform equals its total pullback for these modifications. This qualification is essential; it is false for arbitrary unrelated refinements meeting E.
The classes Z_nu_j converge to Z_nu in L2. To see the strong assertion, their intersections with the line class are 1 and (Z_nu_i.Z_nu_j)=alpha(nu_i wedge nu_j); decreasing alpha and upper semicontinuity imply alpha(nu_j)->alpha(nu)>=0. The squared Hilbert norm of a difference is therefore |alpha(nu_i)-alpha(nu_j)|. The weak limit identifies the L2 limit with Z_nu.
FJ's bounded L2 pullback and continuity of pairing with the fixed Cartier class E now pass (2) to
    (F*Z_nu.E)=-f_E nu(c).                                           (3)
Every actual valuation preimage w of nu has its centre on this source model over the centre of nu, hence outside E. Therefore (Z_w.E)=w(E)=0, using the dual valuation/Cartier pairing extended by ancestral approximation. A finite preimage-only sum, or a convergent such sum for which the pairing is defined, again has zero pairing with E. Formula (3) is an actual-source obstruction whenever nu(c)<0. The next paragraph proves that strict inequality for the precise target in this task.
We claim only this fixed-E pairing and the finite-model expansion. We do not claim a globally convergent corrected expansion over every dicritical valuation, openness of the restricted valuation map, a degree sum, defectlessness or bounded positive weights for every approximating fibre.
Strictness needs no alpha(nu)>0. The reviewed infinitely singular target has residue field C, with constants mapping identically to C, and nu(P)<=0 for every nonzero polynomial P. If a nonconstant P had value zero, its nonzero residue would be some c0 in C; then P-c0 is a nonzero polynomial of positive value, a contradiction. Therefore nu(P)<0 for every nonconstant P. In particular -f_E nu(c)>0 for every actual dicritical image curve. The preimage-only A7 identity is consequently impossible whenever such an E exists, not merely unproved by compactness.
## Disposition and provenance
The bare implication compact-T nonescape => preimage-only A7 decomposition is retired. It contradicts the strictly positive dicritical pairing whenever an actual dicritical E exists. Any future admission must address this actual correction or provide a different global consumer; repeating E or divisorial conservation alone is not a successor.
The uniform minimum is proved at the stated plane-valuation foundation tier; E remains a gap; the class correction is a scoped projection/limit calculation, not a no-go theorem for all valuation methods. Neither N=1 nor JC2 follows.
Pregates: all26 physical inputs,12 current-launch archive blobs,STATE equality and two canonical verifications passed; whole STATE196 personally read. Oct16 predecessor50LF personally read. Source/coverage/custody and postpins are in the companion receipts. No new external sources, history queries, control families or independent review.
## OPENS RAISED
None newly promoted. The existing actual-source correction/extension gap remains, now with the explicit coefficient above.
## COLLISIONS
Recovered Oct16 discrepancy/conservation predecessor is retained; finite-self-germ and hidden-centre stops remain. Terminal frozen-public collision output is retained separately; lexical absence does not certify novelty.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12193`.
- Body SHA-256:
  `b821d7a62123cc075a54eaa4dab48c7cac27dbd9c5fbd69931b020e18cb1f477`.
- Frozen basis: `0ce7416c9d8c088e883a5f22b4967bba4e1ea27b`.
