# Conical singular preimage and normality

MANUAL co-research, not FIRST/promotion. First2026-09-12 13:33:36 UTC; reserve13:45/HARD13:48 unchanged. Both inputs freshly WHOLE after matching pins; clipping recovered. Own outputs absent; no scientific execution.

## Exact question

Let j:A2_C -> Z subset A3_C be a finite birational unramified normalization of an integral surface hypersurface. Does ordinary scaling invariance of D=j^-1(Sing Z)_red force D empty and j an isomorphism?

## Result

The criterion is TRUE by the following manual proof. The conclusion is conditional on the stated global conicality hypothesis; no actual Keller graph is asserted to satisfy it. The proof uses reduced supports, not invariance or reducedness of the conductor ideal itself.

## 1. Local branches: what finite and unramified give

At a closed point z in Z let j^-1(z)={a_0,...,a_r}. Since j is unramified and A2 is smooth, the differential of the composite A2 -> Z -> A3 has rank two at every a_i: the map from ambient differentials onto source differentials is surjective. The holomorphic rank theorem therefore makes j, on a sufficiently small neighborhood of each a_i, an embedding onto a smooth surface germ Z_i in C3.

These germs exhaust the reduced analytic target germ: analytic properness of a finite map permits shrinking so its inverse image lies in the chosen fiber neighborhoods, and surjectivity covers the target. They are distinct, since coincident germs give two preimages on an analytic open surface piece, which meets the algebraic open where the birational map is an isomorphism. A reduced complex algebraic hypersurface is analytically reduced, so this union has no extra nilpotent structure.

One fiber point gives a local analytic isomorphism to one smooth branch. Conversely normalization is an isomorphism over a smooth point. Thus:

    z singular  <=>  its normalization fiber has at least two points.

Unibranch nonnormality is therefore impossible here. Normal crossings are NOT required: smooth branches may be tangent and their intersection nonreduced.

On Z_i the singular preimage is exactly the union of intersections with other Z_j. Each pair meets in a nonempty pure curve: a defining equation of Z_j restricts to a nonzero nonunit holomorphic function on the smooth surface Z_i. Off these intersections the target has one smooth branch; on them it has multiple branches and is singular.

Consequently D is either empty or a pure one-dimensional reduced closed algebraic subset of A2. In particular there are no isolated singular-preimage points to hide in the argument.

## 2. A conical singular preimage cannot have several lines

Assume D nonempty and invariant under ordinary nonzero scaling. For every nonzero a in D, the closure of its scaling orbit is the entire line C*a, including the origin, and is contained in D. A one-dimensional algebraic set has finitely many irreducible components; purity now implies

    D=L_1 union ... union L_k,

where the L_i are distinct lines through the origin and k>=1. No ideal homogeneity was assumed in deriving this support statement.

Suppose k>=2. Put z=j(0). By section1 its fiber is {0,a_1,...,a_r} with r>=1. All a_i lie in D, since z is singular. Each nonzero a_i belongs to exactly one L_i, so its local D germ is one smooth irreducible curve. Under the local embedding into the corresponding surface branch Z_i, call this ambient curve germ C_i. On the origin branch Z_0 the local D has k distinct irreducible germs.

For every i>0 and every j!=i, the reduced intersection Z_i intersect Z_j is a pure curve contained in C_i, hence is C_i itself: a nonempty pure curve germ contained in one irreducible curve germ cannot be a proper subgerm. If r=1 this already says that the origin branch's entire singular-preimage germ is the single irreducible curve C_1. If r>=2, apply the same reasoning from both sides of Z_i intersect Z_j for i,j>0 to obtain C_i=C_j. Also Z_0 intersect Z_i has this same reduced support. Therefore all intersections on Z_0 have one common irreducible curve support. An embedding preserves irreducibility, contradicting its k>=2 local branches.

Thus k<=1. Reducible pair intersections or intersection multiplicities introduce no exception: containment in C_i has already forced their reduced support to have just that one component. Tangency changes multiplicity, not this support argument.

## 3. One line is also impossible

Suppose D=L is a single affine line, and let C=j(L), an irreducible closed curve. The restriction j|L:A1->C is finite and nonconstant. Every point of C is singular in Z, and every preimage of it lies in D=L. Section1 therefore gives at least two distinct preimages. In particular the finite curve map has generic degree at least two.

On the other hand, j|L is an immersion: the rank-two differential of j is injective on the tangent line of L. Write its three coordinate polynomials as p_i(t). They are not all constant and their derivatives have no common zero. The following polynomial-Luroth argument proves their function field is C(t).

Let M=C(p_1,p_2,p_3) and let X be its smooth projective curve. The finite morphism P1_t -> X has, by Riemann-Hurwitz,

    -2=degree*(2 genus(X)-2)+ramification degree,

so X is P1. Choose a nonconstant p_i. Its only pole upstairs is infinity, hence its pole support on X consists of one point q whose entire inverse image has support {infinity}. Choose a coordinate h on X with its unique simple pole at q. Pullback makes h a polynomial in t. Each p_i has no pole off q on X, since any such pole would give a finite pole upstairs. Therefore p_i=P_i(h) with P_i polynomial and M=C(h).

Now p_i'=P_i'(h)*h'. Immersion implies h' has no zero in C. Thus h' is a nonzero constant, h is linear, and M=C(t). The generic degree of j|L is one, contradicting the preceding degree-at-least-two conclusion. This establishes only generic degree one, not global embedding of an arbitrary immersed polynomial curve; nodal parametrizations are not excluded by this step alone.

We conclude D is empty. Then Z is smooth, hence normal, and its finite birational normalization j is an isomorphism.

## 4. Conductor and exact role of the assumptions

Write B=C[Z] subset R=C[x,y]. Its conductor

    I={b in B : bR subset B}=ann_B(R/B)

is also an ideal of R. Because R/B is a finite B-module, V_B(I) is exactly the locus where the finite normalization is not an isomorphism. This equals the nonnormal locus. In this setting it also equals Sing Z: over a normal point normalization is an isomorphism, and the source is smooth; conversely a smooth point is normal. Thus D=V_R(I) as reduced support.

Scaling invariance of this support says its radical ideal is homogeneous (equivalently, here, its support is a union of radial lines). It neither asserts nor needs invariance of the possibly nonradical conductor ideal I. A derivation of Frac(B) supplies neither statement by itself.

The hypersurface-in-C3 hypothesis supplies curve intersections; in higher codimension branches can meet only at a point, invalidating this proof. Finiteness supplies proper shrinking and the finite restriction to L. Unramifiedness supplies embedded smooth branches, not just generic immersiveness. The whole A2 and ordinary scaling supply complete lines through a common origin and polynomial parameters. On C*, t->t^n is everywhere unramified of higher degree. These are essential roles in this proof, not claimed counterexamples to every possible weakening.

## 5. Checked controls and source limit

For the proposed nodal control take R0=C[t,s], u=t^2-1, v=t(t^2-1), and B0=C[u,v,s]. The image equation is v^2=u^2(u+1). We have t^2=u+1 and t=v/u in the fraction field, so R0 is finite birational and is the normalization. The derivatives satisfy

    du=2t dt,       dv=(3t^2-1)dt,       3t du-2dv=2dt.

Together with ds this proves the normalization is unramified everywhere. The target singular locus is u=v=0: its gradient equations v=0 and u(3u+2)=0, combined with the image equation, force u=0. Its preimage is t=1 union t=-1, two parallel lines. It is not preserved by all ordinary scalings of (t,s). The map identifies (1,s) and (-1,s), so is not an isomorphism. This control retains every hypothesis except conicality and verifies that this hypothesis cannot simply be discarded.

To check the necessity of unramifiedness in a conical case, (t,s)->(t^2,t^3,s) normalizes the cusp surface v^2=u^3. It is finite birational with smooth A2 source and singular preimage t=0, a scaling-invariant line, but its differential loses the t direction there. It is not unramified and not an isomorphism. The identity map onto a plane in A3 is the positive empty-conductor check.

No claim follows that an actual finite Keller graph has conical singular-preimage support. That missing invariance remains the source-level quantity; the present theorem decides only the implication once it is independently established. No JC2, global action on the graph, conductor-ideal stability, literature novelty, control farm or further lane follows.

## Quantity and self-check

The implication is proved; actual Keller conicality is not decided. Cheapest check: finite branch exhaustion, pair-intersection supports and polynomial-Luroth generic degree. Five review minutes is UNMEASURED planning, not cost evidence or authority. Tangency, unibranch failure, r=1, nonradical conductor and the controls were checked. No canonical OPEN or charge_basis. Own output collision/postpins precede sealing.

## Read scope and publication

Two inputs only: COORDINATION806lines fresh WHOLE in1–220,221–440,441–660,661–806 (clipped middle reread), then TASK WHOLE. No linked/prior/peer body, corpus, network, protected tree, worker, agent, scientific interpreter/CAS/helper/import/AST/syntax/test or shared edit. Only inert metadata/text, apply_patch and administrative artifact_finalize. Own WHOLE/postpins/quantity/control/collision checks before marker LAST.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10005`.
- Body SHA-256:
  `8fa0b29635d2d8c56f771bd1a6b48af4a4fbb09f12224a70446e02ae5d535f02`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
