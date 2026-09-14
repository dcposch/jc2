# Keller field trace: height-one saturation and conditional global module

Owner /root/contact_collision_geometry. MANUAL / UNREVIEWED. Actual first action 2026-09-11 20:02:51 UTC. Original publication reserve 20:22 UTC / HARD 20:25 UTC, unchanged. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Sole scientific input: ROOT TASK, current hash before FRESH WHOLE. No other report, primary source, live ROOT work or linked file is consumed. This report separates manual deductions from named external structural/comparison facts; it does not independently certify those external facts or promote a JC2 result.

## 1. Verdict and structural input

The height-one saturation proof works. The abstract global conclusion also follows, CONDITIONAL on the explicitly named D-module and comparison inputs below. It forces the expected mixed-pole cokernel at an ordinary node and would exclude a faithfully attached FULL mixed-localization trace there. No such mandatory full local trace is proved here, so no actual Keller-map exclusion follows.

Write A=C[p,q], R=C[x,y], K=Frac(A), L=Frac(R), N=[L:K], and M=Tr_(L/K)(R). For an actual Keller map p=P(x,y), q=Q(x,y), N is finite and separable. Use the following STANDARD STRUCTURAL INPUT from finite normalization and Zariski's main theorem: the integral closure B of A in L is finite over A; Spec R is its open source; F is finite over V=Spec A minus its nonproperness divisor D; and a generic point of each component of D has a missing point in that finite normalization. These structural facts are named inputs, not a fresh proof of Zariski's main theorem. No smoothness or flatness of the entire normalization surface is needed below.

## 2. Actual height-one trace saturation

Fix a height-one prime P belonging to D. Let O=A_P, with uniformizer pi and fraction field K, and C=B tensor_A O. Then C is a finite torsion-free O-algebra with fraction field L, and is a semilocal Dedekind domain. Its maximal ideals are the places above P. The open Spec R_P retains some of them and omits at least one, say Q_j.

Choose z in C with valuation one at Q_j and valuation zero at every other maximal ideal. Such z exists by Chinese remainders modulo Q_j^2 and the other maximal ideals, using the DVR at Q_j. Its only zero in Spec C is the omitted place. Therefore z^{-m} belongs to R_P for every m>=1: it is regular on that actual open source.

The trace-dual lattice

    C^vee={b in L : Tr(bC) subset O}

is a finite O-lattice in L. Indeed C is finite free over the DVR O, and the matrix of the nondegenerate separable trace pairing is invertible over K; its inverse sends O^N to exactly this lattice. In particular its Q_j-valuations have a finite lower bound.

Suppose Tr(R_P) were contained in pi^{-b}O for some b>=0. Since C R_P subset R_P, every r in R_P would satisfy

    Tr(pi^b r C) subset O,

so pi^b R_P subset C^vee. This contradicts the unbounded negative Q_j-valuations of pi^b z^{-m}. Consequently Tr(R_P) has valuations unbounded below. It is an O-SUBMODULE of K; a trace of valuation -n generates pi^{-n}O as an O-module. Unboundedness therefore gives

    M_P=Tr(R_P)=K.

Localization commutes with this A-linear trace image. The proof does NOT assert that every Tr(z^{-m}) has a pole: a suitable multiplier c in C may be required. More explicitly, failure of pi^b z^{-m} to lie in C^vee supplies c with Tr(pi^b z^{-m}c) outside O. The algebra closure used was closure of R_P under C-multiplication, not closure of M under products. For example Tr(s^{-1})=0 in the quadratic field extension s^2=pi despite the pole of s^{-1}; this is only a trace-cancellation control, not an actual Keller model.

At primes outside D, the ambient localization A[1/d] is already A_P, so containment A subset M subset A[1/d] gives fullness there in the appropriate sense. "Full at height one" means equality with the ambient localized module, not K at primes outside D.

## 3. The other suggested trace identities

These have direct deductions on the actual Keller source. A subset M because Tr(a/N)=a. Over V the source is finite, so traces of its regular functions belong to the normal ring A[1/d]; hence M subset A[1/d].

If J=P_x Q_y-P_y Q_x is the nonzero constant Jacobian, the unique extensions of partial_p, partial_q to L are

    delta_p=(Q_y partial_x-Q_x partial_y)/J,
    delta_q=(-P_y partial_x+P_x partial_y)/J.

They preserve R and commute. Trace commutes with them: extend the derivation to an algebraic closure; uniqueness on algebraic extensions makes it commute with the K-embeddings whose sum is the separable trace. Thus M is a D_A-submodule of A[1/d]. It is not asserted to be an algebra.

Finally H^2_DR(M)=0 in the UNSHIFTED degrees 0,1,2 convention. For r in R, the form r dp wedge dq=Jr dx wedge dy has a polynomial primitive, obtained by integrating Jr termwise in x. Since dp,dq are an R-basis of differentials, that primitive is f dp+g dq for polynomials f,g. Hence r=delta_p g-delta_q f. Taking traces expresses every element of M as partial_p(Tr g)-partial_q(Tr f), proving the assertion directly.

## 4. Precisely stipulated external module/comparison inputs

For the abstract exercise assume A subset M subset A[1/d], D_A-stability, height-one fullness and H^2_DR(M)=0. The following are NOT independently verified from literature here:

- Regular-holonomic localization: A[1/d] is regular holonomic and the regular-holonomic category is closed under subquotients. This would put the actual trace submodule in the assumed category.
- The stipulated IC description: for H=A[1/d]/A there is a submodule L_D which is the sum of the simple rank-one intersection-cohomology modules of the normalized irreducible components, and an exact sequence

      0 -> L_D -> H -> direct_sum_z delta_z^(r_z-1) -> 0.

  Here z ranges over singular points and r_z counts ANALYTIC branches. The usual IC interpretation on smooth local branches is retained. Simplicity is stipulated for these IC modules, not inferred for arbitrary holonomic modules.
- Algebraic de Rham comparison for the smooth complex affine complement V: H^2_DR(A[1/d]) identifies with H^2(V;C).
- Alexander duality for the closed curve D in R4, in its Borel-Moore form: H^2(V;C) identifies with H_1^BM(D;C). Equivalently the latter is reduced H_1 of the one-point compactification of D.

The deductions below are conditional on these inputs and on EVERY component normalization being A1, exactly as in TASK. No IC exact sequence for other normalization types is substituted.

## 5. The correct topological dimension

Put b=sum_z(r_z-1). Normalize D. Its normalization is a disjoint union of affine lines. The one-point compactification of that disjoint union is a wedge of one 2-sphere for each component, with all infinity points identified. It is connected and has H_1=0.

The proper normalization map induces the quotient giving D's one-point compactification: at each finite singular point identify its r_z distinct branch preimages. A unibranch singularity makes no topological identification of distinct points. After triangulating with these finitely many points as vertices, identifying r points in a connected space adds r-1 independent one-cycles, by the relative homology sequence (equivalently attach a cone on that finite set). The sets for different z are disjoint. Therefore

    dim H_1^BM(D;C)=b,
    dim H^2_DR(A[1/d])=b

using exactly the two comparison/duality inputs just named.

The distinction from ordinary H_1(D) is essential. For D={pq=0}, the two affine axes meet at one point with r=2, so b=1. Their union is contractible by scalar contraction, hence ordinary H_1(D)=0, while V=(C^*)^2 has b_2=1. The common compactification point at infinity is indispensable to the preceding count.

## 6. Global identification of M

Set N_M=M/A subset H. At the generic height-one point of a component D_i, fullness gives (N_M)_P=H_P. Its intersection with the corresponding simple IC submodule L_i is consequently nonzero: localization is exact and (L_i)_P is nonzero. More concretely, a nonzero generic element of L_i can be multiplied by denominators outside P to obtain a nonzero element of N_M intersect L_i. This intersection is a D_A-submodule; simplicity forces L_i subset N_M. Doing this for each i proves

    L_D subset N_M.

Thus Q=A[1/d]/M=H/N_M is a quotient of P_D=H/L_D, the stipulated direct sum of b point-delta modules. It is point-supported and semisimple, with total multiplicity ell<=b.

The needed delta facts can be checked directly. At a translated point, delta is C[xi,eta], with partial_p,partial_q acting by multiplication by xi,eta and p-p_0,q-q_0 acting by minus differentiation. Differentiation extracts a nonzero constant from any nonzero polynomial, then multiplication generates the whole module, so delta is simple. Its unshifted de Rham complex is the Koszul complex for xi,eta: cohomology vanishes below degree two and H^2 is C. Hence dim H^2_DR(Q)=ell.

Apply the de Rham complex to 0 -> M -> A[1/d] -> Q -> 0. It is a termwise exact sequence of complexes, all ending in degree two. Its top long exact sequence reads

    H^2_DR(M) -> H^2_DR(A[1/d]) -> H^2_DR(Q) -> 0.

The first term is zero. Therefore the middle map is an isomorphism, and section 5 gives ell=b. A quotient of the finite semisimple module P_D with the same total length has zero kernel. Thus N_M/L_D=0, and

    M = inverse_image(L_D under A[1/d] -> A[1/d]/A).

No extra simplicity claim about M, no algebra closure of M, and no local-to-global vanishing assertion were used. The external IC sequence and the comparison/topological dimension are load-bearing.

## 7. Ordinary node: exactly one missing mixed-pole delta

At an ordinary node use formal coefficient coordinates S=C[[u,v]] with d a unit times uv. Throughout this paragraph, passage from a global module means the ORDINARY FLAT TENSOR BASE CHANGE S tensor_A M, via localization at the node. It does NOT mean the inverse-limit adic completion of M or of the non-finite A-module R. These operations must not be interchanged.

The two smooth-branch IC modules in S[1/(uv)]/S are S[1/u]/S and S[1/v]/S. Their inverse image is

    M_node=S[1/u]+S[1/v].

The intersection S[1/u] intersect S[1/v] is S. The Cech quotient is

    S[1/(uv)]/M_node = H^2_(u,v)(S).

This can be checked without a computation: modulo the two pure localizations, every formal Laurent expression has a unique finite linear combination of u^{-i}v^{-j}, i,j>=1. All terms with at least one nonnegative exponent lie in a pure localization; only a finite rectangle of doubly negative exponents remains. Differentiating 1/(uv) generates every such basis element with a nonzero factorial coefficient, and multiplication by u or v kills the corresponding boundary term. Thus the quotient is precisely one point-delta module.

This is a sharp control against two tempting inferences. M_node is full in its ambient module at every height-one prime, but it is not all S[1/(uv)]: 1/(uv) survives in the quotient. It is also not an algebra: it contains 1/u and 1/v but not their product. No Hartogs or multiplicative argument for a finite/reflexive O-module may be applied to this D-module without an additional hypothesis.

For the globally identified M of section 6, the stipulated IC interpretation on the two normalized smooth branches gives exactly this local model. Alternatively, the nonzero delta summand of the global Q at the node already suffices: faithful flat coefficient base change cannot erase it. Therefore a correctly attached calculation asserting

    S tensor_A M = S[1/(uv)]

at that node would contradict the global theorem. Tensoring the A-linear trace map by flat S preserves its image, so the relevant local quantity is the image of the base-changed trace on S tensor_A R. A separate escaping-cover model is not that image unless the source and trace identifications are proved.

The prohibition of full mixed poles is CONDITIONAL on the global external inputs and their actual attachment. It is NOT the invalid principle that global H^2(M)=0 implies local de Rham vanishing. Ordinary-node pure-pole traces are entirely consistent with the theorem. No argument here forces a hypothetical Keller map to supply full mixed poles; consequently this restriction alone closes no actual JC2 gap. The point multiplicity r_z-1 is not identified with any other campaign defect.

## 8. Scope and closeout

QUANTITY: actual height-one field-trace fullness, the stipulated global module identification, and its exact ordinary-node restriction. Height-one fullness and the elementary trace identities are proved from the named normalization/open-source structural input. Global identification is proved conditional on the named IC/regularity/comparison/duality facts and the A1 normalization hypothesis. No extension to other normalizations is made.

CHEAPEST TEST performed: manual trace-dual contradiction, generic IC intersection, top de Rham dimension comparison, and the explicit mixed-pole quotient control. A further exclusion would require a source-attached local trace computation forcing the prohibited full localization; none is supplied or authorized. Scientific runtime/feasibility is UNMEASURED. No new OPEN identifier, review, computation, successor or promotion is selected.

TASK was current-pinned before FRESH WHOLE in the first administrative call. No clipping, reuse or additional scientific input occurred. Own report/manifest/PINS/custody targets were absent and ROOT TASK was preserved. Bounded apply_patch writes use only the private lease and owned box. Own WHOLE partial/PINS readback, input postpin, scope/OPEN/QUANTITY/collision checks precede the unique final body marker. Close/finalize/expected verification and sealed WHOLE report/manifest readback precede final custody. All writers are idle before the terminal handoff. No scientific subprocess, code/import/AST/syntax/test/dummy/CAS, coefficient artifact, network/AWS/SSH, protected tree, agent, live report or shared ledger was accessed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14025`.
- Body SHA-256:
  `175fbfe028f2217c4c1d1a9882ba17d30c66894213dfdcbe15db914e83bff7ed`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
