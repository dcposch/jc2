# FIBERNORMAL0150 — smooth omitted curves from the marked projective ruling

Status: INTERNAL / ROOT-MANUAL / UNREVIEWED. This is a proposed structural strengthening of the affine-extension package. It is not a Keller exclusion, a novelty claim, or a proof of JC2.

## Statement and inputs

Let X be a normal integral affine complex surface containing a specified dense open U=A2 with linear coordinates (ell,v). Suppose q:X->P1 is a morphism with q|U=ell and q^-1(A1)=U. The reviewed PROJECTIVEBASE2305 lemma supplies this q for every such marked normal affine extension; it does not require the Keller identity.

Claim: every irreducible curve E in X minus U is smooth. Using the retained affine-boundary theorem that the normalization A1->E is finite birational and bijective, it follows that E is isomorphic to A1. Thus the reduced omitted curves of the actual finite normalization of a plane Keller map are smooth affine lines, conditional only on the already attached marked open-immersion and affine-boundary packages.

The proof below does not require a rational-singularity assumption on X. It does not claim that X is smooth along E, that the total infinity fibre is reduced or connected, or that X->A2 is etale along E.

## 1. A proper model over the same base

Embed X as a closed subvariety of A^m. Its graph under q is closed in A^m x P1. Take its closure in P^m x P1 and normalize; call the resulting normal projective surface T. Normalization is finite here and is an isomorphism over the normal open X. Thus X is an open subscheme of T, and the second projection extends q to a projective morphism f:T->P1.

Put S=P1 x P1, with projection p to its first factor. The coordinates (ell,v) identify the common open U with A1 x A1 in S. Resolve the resulting birational map S -->> T by point blowups on the smooth surface S. This gives a smooth projective surface Z and morphisms pi:Z->S and rho:Z->T, with pi a finite sequence of point blowups and rho proper birational. Resolution of indeterminacy of a surface rational map is the named standard surface-theory input. The morphisms f rho and p pi agree on the dense common open, hence agree everywhere.

For context, the common-resolution and point-blowup framework is recorded in [Stacks, Section54.17](https://stacks.math.columbia.edu/tag/0C5Q). The use here permits the target T to be normal: resolve T first and then use common resolution, or resolve the rational map from S directly. No smoothness of T is assumed.

## 2. Cohomology on an affine base neighbourhood

Fix b in P1, and choose an affine open neighbourhood V of b, shrinking it below when needed. Write T_V=f^-1(V) and Z_V=(f rho)^-1(V).

For a blowup beta of a smooth surface at a point, beta_*O=O and R^j beta_*O=0 for j>0. Here is the local calculation needed for the latter assertion. Near the point choose regular parameters x,y generating its ideal. The blowup has the two affine charts A[t]/(xt-y) and A[s]/(ys-x); their overlap is represented by A[t,t^-1]/(xt-y), with s=t^-1. Every Laurent-polynomial representative on the overlap splits into nonnegative and negative powers, coming respectively from the two charts. Therefore its Cech H1 is zero; the two-chart cover also kills higher cohomology. Away from the point beta is an isomorphism. The degree-zero assertion follows from proper birationality and normality. The regular-sequence chart presentation is the usual point-blowup presentation. [Stacks Lemma50.16.3](https://stacks.math.columbia.edu/tag/0G5H), at i=0, records the corresponding structure-sheaf vanishing in its local model; the chart argument here specifies the needed application independently of omitted setup on that page.

Iterating this calculation for pi and using H1(P1 x V,O)=0 gives H1(Z_V,O)=0. Since T is normal, rho_*O_Z=O_T. The low-degree Leray sequence therefore gives an injection H1(T_V,O)->H1(Z_V,O), so

    H1(T_V,O)=0.

Also H2(T_V,F)=0 for every quasicoherent sheaf F after shrinking V suitably around b. Indeed, choose a projective embedding of T over V and two hyperplanes whose common zero set misses the one-dimensional fibre over b. Such hyperplanes exist over C. The common zero set has closed image in V by properness, so remove that image. The two hyperplane complements now cover T_V; each is affine, as is their intersection. Their Cech complex has length one. Dominance and integrality ensure that every fibre of f has dimension one.

## 3. The full fibre and each reduced component

Choose a regular parameter tau on V vanishing exactly at b. Since T is integral and f is dominant, multiplication by f^*tau is injective. For the full scheme-theoretic fibre F_b this gives

    0 -> O_(T_V) --tau--> O_(T_V) -> O_(F_b) -> 0.

The preceding H1 and H2 vanishings give H1(F_b,O_(F_b))=0. No reducedness of F_b or nonproper specialisation theorem is used.

Let C be any reduced irreducible component of F_b. The quotient O_(F_b)->O_C has a coherent kernel K on F_b. The inherited two-affine-open cover gives H2(F_b,K)=0, so its exact sequence yields

    H1(C,O_C)=0.

The curve C is integral and projective over C. Its finite normalization nu:Ctilde->C has a zero-dimensional cokernel Q in

    0 -> O_C -> nu_*O_(Ctilde) -> Q -> 0.

Both spaces of global functions are C. The cohomology sequence and H1(C,O_C)=0 force H0(Q)=0, hence Q=0. Thus C is normal; over C it is a smooth projective curve of genus zero, and consequently C is P1.

## 4. Return to the omitted curve

For an omitted prime curve E in X, q(E) is infinity. Its closure C in T is a reduced irreducible component of F_infinity. Since E is closed in X, C intersect X=E. The preceding argument makes C smooth, so E is smooth. The retained finite birational normalization A1->E is therefore an isomorphism.

This closes only the scheme-smoothness qualification on the omitted prime curves. Their embeddings can pass through singular points of X. Their finite images in the target plane can still have cusps, and normal ramification, image-branch degrees, nonreduced total fibres and the existing sheet-budget slack remain unrestricted by this lemma. E may be nonempty. No N=1, surjectivity, properness or polynomial inverse follows.

## Custody and foundation scope

PROJECTIVEBASE2305 was read in full and its seal checked; its independent review remains the inherited input, with the actual-normalization attachment conditional as before. AFFINETREE0015's selected audited argument supplies finite-bijective A1 normalization and explicitly left scheme smoothness unproved. The present proper-model cohomology argument is the proposed added step, not a reproof of the sheet budget.

Named standard foundations: finite normalization of a complex projective variety; resolution of surface rational maps by point blowups; proper birational pushforward of O to a normal target; low-degree Leray; affine Cech cohomology; finite normalization of curves; and genus-zero classification over C. The point-blowup vanishing and the H2/fibre arguments are spelled out above. The two selected Stacks pages were read only at the recorded windows; their referenced foundation chains were not exhaustively audited. Independent hostile review is required before adoption or publication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7245`.
- Body SHA-256:
  `1ff97f73faf8199e750faf246b1f73e2e98286b65d0a0a69f6cd247138ccc362`.
- Frozen basis: `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
