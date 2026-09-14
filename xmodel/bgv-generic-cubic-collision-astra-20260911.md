# Generic cubic auxiliaries: a transverse collision and a smooth third sheet

Owner /root/contact_collision_geometry. First action2026-09-11 12:53:22UTC. Original reserve13:07/HARD13:10UTC unchanged. Sole charged input is ROOT TASK, SHA3f5d658e2dc5ce5f9ea464a9128a397336c9fff9e81e4e6ee5f1664ab88ad758, read fresh WHOLE after its hash. Own report/manifest/PINS/custody were absent; existing TASK is preserved.

MANUAL CO-RESEARCH / UNREVIEWED. No actual noninvertible Keller map or source point is asserted. ROOT's subsequent scope attestation says generic failure is already KNOWN by BGV contraposition; at most the explicit degree-three finite-etale-locus witness below is a new attachment. This proof does NOT invoke BGV or make a novelty claim.

## The statement is proved, conditionally on the hypothetical actual map

Let k be algebraically closed of characteristic zero, n>=2, F:A^n->A^n a polynomial Keller map of geometric degree N>=3, and d>=3. There is a nonempty Zariski open O in V_d such that EVERY h in O is primitive for k(x)/k(F), and j_h=(h,F) has an irreducible divisorial component D of j_h^-1(Sing Z_h) with F^-1(F(D)) different from D. The witness can be chosen over a finite etale locus of the ACTUAL F: exactly two sheets collide transversely in h, and a third sheet maps to a smooth graph point. This is not a bound on the degree of F or a statement that all auxiliaries fail.

## 1. Actual finite-etale locus and primitive auxiliaries

Write K=k(F), L=k(x). Invert a nonzero target polynomial to make every x_i integral over the target coordinate ring: their algebraic monic equations over K have only finitely many denominators. Thus on a nonempty affine target open U, the ENTIRE preimage X=F^-1(U) is finite over U. The Keller Jacobian makes F etale, so this restriction is finite etale of rank N after shrinking if necessary. U can be taken irreducible and smooth. No finite-morphism claim is made over the omitted target boundary.

The primitive auxiliaries contain a nonempty open O_prim in V_d. Indeed take the N distinct K-embeddings of L into a normal closure. For each pair, the equality of their values on h cuts out a k-linear subspace of V_d. It is proper: some coordinate x_i distinguishes the embeddings, and V_1 is contained in V_d. It is Zariski closed even though the values lie in a function field, because the image of the finite-dimensional k-space V_d is finite-dimensional over k. Outside the finite union of these proper linear subspaces all N conjugate values are distinct, hence [K(h):K]=N and K(h)=L. No rational-point descent or bound on intermediate fields is used.

Let B->U be the finite etale full-labeling cover of the N-point fibres. Choose a connected component; it remains surjective over the connected U, is smooth irreducible, and carries all N labeled sections p_i:B->X. Put h_i(b)=h(p_i(b)). The functions h_i on B are regular, and their dependence on h in V_d is linear. This is the labeling cover of the actual map, not a substitute parameter family.

## 2. Cubic interpolation and an open image of transverse collisions

Fix b0 in B(k). Write p_i=p_i(b0), all distinct. Let l_ij(h)=h(p_i)-h(p_j). For any unordered pair other than {1,2}, l_ij is not proportional to l_12 on V_3. To see this, choose a linear form separating the at most four points in the union of the pairs, and interpolate arbitrary values on these points by a univariate polynomial of degree at most3. In particular one can make l_12=0 and l_ij!=0. Thus each unwanted equality cuts a proper linear subspace of the hyperplane K12=ker l_12.

The differential in the B-direction of h_1-h_2 is not identically zero on K12 either. Choose an affine linear form ell with ell(p1)=0, ell(p2)=1, and a nonconstant affine linear form M with M(p1)=0. The cubic

    h_*=M*(1-ell)^2

has equal zero values at p1,p2, differential dM at p1 and zero differential at p2. Since F is etale, the corresponding differential difference on the target, hence on B, is nonzero. This is an explicit two-point Hermite control, not an assumption of independent arbitrary jets at all N points.

The irreducible vector space K12 cannot be covered by finitely many proper linear subspaces. Hence there exists h0 in K12 for which EVERY other unordered pair is unequal and d_B(h_1-h_2) at b0 is nonzero.

Consider the incidence hypersurface

    I={(b,h) in B x V_d : h_1(b)-h_2(b)=0}.

Let I_good be its open subset where all other unordered pairs have unequal values and d_B(h_1-h_2)!=0. It is nonempty by the cubic construction, also when d>3 since V_3 is contained in V_d. The projection I_good->V_d is smooth: locally B has etale coordinates, and the single defining equation has a nonzero derivative in a B-coordinate. Its relative dimension is n-1. Smooth morphisms are open, so O_coll, its image, is a nonempty Zariski open subset of V_d. Equivalently, one may use this smooth local projection and constructibility to obtain a nonempty open image; mere incidence dimension counting is not the argument.

Set O=O_coll intersect O_prim. Both are nonempty opens in the irreducible affine space V_d, so O is nonempty. For every k-point h of O the corresponding good incidence fibre is nonempty and has a k-point, since k is algebraically closed and the fibre is finite type. Thus every such h has an actual labeled target fibre with exactly one colliding pair, transverse equality, and all remaining values distinct. No degree or cardinality bound on N was needed for the finite union of hyperplanes.

## 3. From the collision to a bad GLOBAL individual divisor

Fix h in O and a good labeled fibre over a in U. Let R=O(U). Since X is finite over U, j_h:X->A1 x U is finite onto its closed image Spec R[h]. This image is exactly the restriction of the GLOBAL closure Z_h to A1 x U: the omitted part of the source maps over the closed complement of U and creates no extra point over U upon taking closure.

Primitivity makes the minimal polynomial f(T) of h over K have degree N. Its coefficients belong to R, since h is integral over R and R is integrally closed. Monic division gives R[h]=R[T]/(f). On the labeling cover,

    f(T)=product_(i=1)^N (T-h_i).

Near the coincident graph point T=h_1=h_2 all other factors are units. Its local equation is therefore a unit times (T-h_1)(T-h_2). The nonzero differential of h_1-h_2 makes the intersection of these two graph branches transverse. The point is singular, and the inverse singular locus on the first source sheet is locally the smooth divisor h_1-h_2=0. These smoothness, singularity and codimension statements descend under the etale base change. Near p3, in contrast, T-h_3 is the ONLY vanishing factor; the T-derivative is a unit, so j_h(p3) is smooth on Z_h.

Let D be an irreducible component of the global closed set j_h^-1(Sing Z_h) through p1 with that local divisor germ. It has codimension1 in A^n. The global closure causes no saturation accident: p3 is outside the ENTIRE inverse singular locus and hence outside D, whereas

    F(p3)=F(p1),       p1 in D.

Consequently p3 belongs to F^-1(F(D)) minus D. This proves the requested failure for an individual irreducible divisorial component. It is saturation under F, not under j_h: indeed h(p3) is different, so j_h(p3) is a different, smooth graph point. Neither global irreducibility of the double locus nor monodromy can include a smooth third sheet in D. No closure of F(D) is required for this set-theoretic witness.

## 4. Required controls and exact limits

Degree-one control: for F=id, every j_h is a smooth graph and the inverse singular locus is empty. Thus no universal claim for degree1 follows. At N=2, the sole collision consumes both sheets; the missing smooth third sheet means THIS argument gives no nonsaturation witness. This is a boundary of the mechanism, not a claim that a degree-two noninvertible Keller map exists or a separate classification.

For the stipulated non-Keller open example e:(x,y)->(x³,y) on G_m x A1, h=x is primitive and its graph T³=s is smooth because T is a unit. Thus not ALL h fail. For h=x²+lambda*x with lambda!=0, choose a primitive cube root omega. At target s=lambda³ the three source x-values are lambda*omega, lambda*omega², lambda. The first two h-values are -lambda²; the third is2lambda². Their difference is nonzero. The colliding equality is transverse: h(x)-h(omega*x)=(1-omega)*x*((1+omega)*x+lambda), which has a simple zero at x=lambda*omega, and ds/dx=3x² is a unit. The divisor x=lambda*omega is bad, with the smooth third sheet x=lambda in its e-saturation but not in the inverse singular locus. The auxiliary is primitive: the degree-three cyclic field extension has no proper intermediate field and this h is not invariant under x->omega*x. This control illustrates the mechanism without asserting a global Keller example.

The proof used cubic interpolation only in the auxiliary space, independently of n, N and the degree of F. It does not optimize d, construct a hypothetical F, supply a BGV-saturating auxiliary, or exclude a Keller source. ROOT's stated BGV contraposition already gives the generic-failure disposition abstractly; the direct contribution here is the uniform cubic transverse-pair/smooth-third-sheet witness on an actual finite-etale locus. No BGV automorphy theorem was used in the proof. No gate or descendant is requested solely to promote this no-go disposition.

## Quantity, custody and stop

QUANTITY: a nonempty open of primitive degree<=d auxiliaries with an actual transverse collision and a smooth third sheet certifying nonsaturation of an individual inverse-singular divisor. CHEAPEST TEST: the manual cubic interpolation, smooth-incidence projection and local graph calculation above; planning15minutes UNMEASURED, no execution or runtime estimate. Result PROVED at manual unreviewed scope, so stop early; no lower-degree optimization, classification or projection farm.

TASK was the sole file input, FRESH_WHOLE after hash and re-pinned at completion. ROOT's history/scope message is an attribution only, not an additional proof premise. Own-only target/OPEN/collision review, WHOLE partial and PINS readback, and current input pin precede the unique final marker. Existing transaction close/finalize/expected verify, sealed WHOLE and custody follow. All writes apply_patch; no scientific subprocess/import/AST/syntax/test/CAS, code/payload, network/AWS, agent, protected/shared edit or extra source. No canonical OPEN identifier, theorem promotion, actual source point, JC2 conclusion or strategy reset.

## COLLISIONS

status: EMPTY

- NONE — own-only target check. Overall generic failure is explicitly KNOWN by ROOT's BGV scope attestation; at most the direct cubic witness is a new attachment, with no novelty certification.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10793`.
- Body SHA-256:
  `ad125f61735a70f7e8023929e99070325bd9bd7bb59fe0e6b9b2a2893412e59d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
