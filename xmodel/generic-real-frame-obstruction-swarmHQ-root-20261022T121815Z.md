# Generic real-affine frames: a fewnomial-face obstruction

ROOT — 2026-10-22. INTERNAL / MANUAL / UNREVIEWED / UNPROMOTED.
External novelty unknown. This is an applicability obstruction, not JC2.

## Exact statement

Identify C^2 with R^4 by a fixed realification rho. Let F=(P,Q):C^2->C^2
be polynomial with det_C DF=c!=0 constant and degree D>=2.
Write H_D for its highest homogeneous vector part, of common degree D
(put zero in a component whose degree is smaller).
Let L be an invertible real-linear map R^4->R^4, let b,q belong to C^2,
and let T be an invertible real-linear target map. Assume

1. H_D(rho^{-1}(L e_i))!=0 for each i=1,...,4;
2. F(b)!=q.

Set G(x)=T rho(F(b+rho^{-1}(Lx))-q).
If G has a zero in (0,infinity)^4, then G FAILS condition(H), defined as:
on every proper face of its vector-support Newton polytope, the nonzero
coefficient vectors lie in some strict open half-space through the origin.
Equivalently, (H) requires their convex hull not to contain zero.

The condition on L is nonempty real-Zariski open among invertible frames.
Thus arbitrary *generic* real-affine source mixing does not restore this
face condition while retaining even one positive Keller preimage.
Exceptional frames with a missing pure degree-D monomial are NOT excluded.

## 1. Highest homogeneous image is a complex line

If only one component has degree D, the assertion is immediate.
Otherwise put p=P_D and q0=Q_D. The homogeneous part of degree 2D-2
of det DF vanishes, since D>=2, so p_x*q0_y-p_y*q0_x=0.
Euler's identities give
D*(p*q0_x-q0*p_x)=y*(p_y*q0_x-q0_y*p_x)=0,
and similarly p*q0_y-q0*p_y=0.
Hence both derivatives of q0/p vanish in C(x,y), so q0/p is constant.
Thus H_D=a*h for a fixed nonzero a in C^2 and a homogeneous h!=0.
Its realification takes values in the fixed real two-plane U=rho(C*a).
No Hessian claim, valuation condition or source completeness is used.

The frame condition excludes the proper real-algebraic zero set of h in
each column. Four independent columns can be chosen outside it, successively;
its intersection with GL_4(R) is therefore nonempty real-Zariski open.

## 2. A self-contained vertex homotopy lemma

Let A be a finite subset of R^n with full-dimensional convex hull P.
Let f(x)=sum_{alpha in A} c_alpha*x^alpha on the positive orthant,
with c_alpha in R^n nonzero, and suppose (H) holds.
For t in [0,1], keep every vertex coefficient fixed and multiply every
nonvertex coefficient by t. Denote this homotopy by f_t, and f_0=f_V.

All zeros of all f_t lie in one compact subset of the positive orthant.
Indeed, otherwise choose zeros with u_k=log(x_k) and ||u_k||->infinity.
After passage to a subsequence, u_k/||u_k|| tends to a nonzero unit vector u.
Let E be the proper exposed face of P maximizing <alpha,u>.
Write lambda_alpha(t)=1 at vertices and t otherwise, and normalize the
nonnegative numbers lambda_alpha(t_k)*exp(<alpha,u_k>) to have sum 1.
The denominator is positive because all vertex weights remain positive.
For alpha outside E, choose a vertex v in E. The normalized alpha weight
is at most exp(<alpha-v,u_k>), which tends to zero.
A subsequence of the normalized vectors therefore tends to a probability
vector beta supported on E. The equations f_tk(x_k)=0 imply
sum beta_alpha*c_alpha=0. This contradicts (H) on E.

This also covers t_k->0: no lower bound on nonvertex weights was used.
The total zero set is closed and log-bounded, hence compact.
Choose one bounded open box in the positive orthant containing it.
Ordinary Brouwer-degree homotopy invariance then gives deg(f)=deg(f_V).
This supplies the needed polynomial case directly; it does not certify
the external paper's other statements or proofs.

## 3. Apply the lemma

The constant coefficient C_0=T rho(F(b)-q) is nonzero.
Each pure monomial x_i^D has coefficient
v_i=T rho(H_D(rho^{-1}(L e_i)))!=0.
Every exponent is nonnegative with total degree at most D, so the Newton
polytope is exactly the full simplex conv(0,D e_1,...,D e_4).
Its vertex truncation is
G_V(x)=C_0+sum_{i=1}^4 v_i*x_i^D.
All v_i belong to T(U). Thus G_V has image in C_0+T(U), an affine subspace
of real dimension at most two.

Assume (H). Section 2 makes the vertex homotopy admissible for degree.
The degree of G_V is zero: within a sufficiently small target ball around
zero avoiding the image of the boundary of the chosen box, choose a value
outside its proper affine image. It has no preimage, so its degree is zero.
Consequently deg(G)=0.

But every zero of G is nondegenerate and has the same local degree sign,
because det_R DG=det(T)*det(L)*|c|^2 is a fixed nonzero constant.
There are finitely many zeros in the chosen box (isolated and compact).
If at least one positive zero exists, their signed sum is nonzero.
This is the contradiction.

## 4. Scope, source and remaining gap

The proof is independent of a presumed truth of JC2 and includes nonlinear
automorphisms. It excludes neither those maps nor hypothetical counterexamples.
It gives no B=R, surjectivity, global properness or fibre-degree-one theorem.
It does not cover exceptional L, b with F(b)=q, nonlinear preprocessing,
auxiliary variables, or degree formulas with weaker face hypotheses.
Support-changing perturbations cannot silently remove these exceptions.

For context and attribution: Frederic Bihan, Topological degree of fewnomial
maps, arXiv:2610.29808v1, states (H) and vertex reduction.
Only the already-retained rendered lines93--108 were reused here.
No new paper section, endpoint, proof or version was read. Section 2 is the
explicit compactness/homotopy argument used above, not an appeal to an
unreviewed source proof. External novelty of this application is UNKNOWN.

Nearest campaign note: briefs/bihan-realification-source-fit-20261022.md,
which only treats complex-affine source frames by opposite coefficients.
The current argument uses leading-image rank plus the full-simplex support;
it is not a rewording of that coefficient-pair proof.
Independent hostile review is required before promotion or load-bearing use.

Indeed, the old top-face obstruction alone need not survive arbitrary real
mixing: choose v with H_D(v)!=0 and a real functional ell positive there.
The polarized degree-D form is continuous. Taking every column close to v
makes ell positive on every top-degree monomial coefficient, and invertible
frames exist arbitrarily close to that repeated-column matrix. The full-face
degree obstruction above, not the old opposite-pair proof, is needed.
