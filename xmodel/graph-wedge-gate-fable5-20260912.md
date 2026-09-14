# graph-wedge-gate-fable5-20260912 — FIRST hostile gate: unbounded graph wedge, arbitrary polynomial outputs

Reviewer: Fable5.1 (independent, different model from ROOT/Astra). Skeleton opened 2026-09-12 01:31 UTC; body written 01:35 UTC. Reserve 01:45 UTC, HARD 01:48 UTC. Manual text/hash reads only; no code, CAS, network, other reports or models.

Claim under audit (GRAPH-WEDGE-1): for the three explicit P,Q,R in ROOT, on every entire graph z=H(x,y)=y^2 K(xy,y) with K an arbitrary polynomial over C, with p,q,r the restrictions and B=C[p,q,r] inside C[x,y], the module M=B J(p,q)+B J(p,r)+B J(q,r) meets C only in 0; hence no two polynomial combinations of p,q,r have nonzero constant Jacobian; no degree bound; invertible polynomial parameter changes preserve it. Out of scope: other H, embedded planes, rational targets, ambient-map claims, novelty, JC2.

## Input custody (prepins)

Hashed at /tmp/jc2-lane.IlmR6j/inputs BEFORE the fresh WHOLE reads; both equal the expected values.

    equivariant-graph-nonlinear-obstruction-root-20260912.md  8ae6ee53450d7a7ef4e688cf768903ca9900f8e4f176088076c3c8bf9cdde828  (10383 B, 1381 w)
    equivariant-graph-nonlinear-obstruction-astra-20260912.md 4c253ddf7fd1cc6c5cfad90dbefec5f609a5ea2d4dcdb5a300b2feb35a94200d  (7217 B, 994 w)

## A. Wedge / coordinate substitution — CONFIRMED

Monomial x^i y^j equals y^2 (xy)^i y^(j-i-2) exactly when j-i>=2; conversely y^2 (xy)^a y^b has j-i=b+2>=2. So the wedge and the K-representation are the same class. Under x=t^-1, y=tw the monomial becomes t^(j-i-2) w^j after the t^-2 factor, so T=t^-2 H(t^-1,tw)=w^2 K(w,tw) is a polynomial exactly on this wedge; the wedge is precisely the scope in which k is a polynomial and k0 is defined. Substitution: xy=w, H=t^2 T, so p=t^2[(1+w)^3 T+w^2(1+w)(4+3w)]=t^2 a; q=tw+3t^-1(1+w)^2 t^2 T+3t^-1 t^2 w^2(4+3w)=t b; r=2t^-1-3t^-1 w-t^-1 T=t^-1 k with k=2-3w-T. All three match ROOT. Identity (3): with T=2-3w-k, 3(1+w)^2(2-3w)=6+3w-12w^2-9w^3, and adding w+12w^2+9w^3 gives 4w+6, so b=4w+6-3(1+w)^2 k. Confirmed by hand.

Origin jets: H is in (y^2), so p is in (y^2) with zero first jet; q=y+O(xy^2), dq=dy; r=2x+O(x^2 y), dr=2dx. Hence J(p,q)=J(p,r)=0 and J(q,r)=q_x r_y-q_y r_x=0-2=-2 at the origin, so C1(0,0,0)=-c0/2. Chart Jacobian: dx=-t^-2 dt, dy=w dt+t dw, so dx wedge dy=-t^-1 dt wedge dw and J_xy=-t J_tw. I recomputed all three lines of ROOT (4) from p_t=2ta+t^2 a_t, p_w=t^2 a_w, q_t=b+tb_t, q_w=tb_w, r_t=-t^-2 k+t^-1 k_t, r_w=t^-1 k_w; every bracket and every sign agrees, including the factor -t^3, -t and -1.

## B. Root approach and limit argument — CONFIRMED

k(t,w)=2-3w-w^2 K(w,tw) is a polynomial in (t,w); k(t,w)-k0(w)=t m(t,w) with m polynomial, so on any compact circle the convergence to k0 is uniform. k0(0)=2, so k0 is not identically zero and its zeros are isolated; a circle about alpha avoiding zeros on its boundary and containing no other distinct root exists at every radius below some bound. Rouche then gives k(t,.) exactly mult(alpha)>=1 zeros inside for all small t, whatever the degree of k(t,.) in w and whatever the multiplicity of alpha. Shrinking radii with |t_n|<1/n gives t_n!=0, t_n->0, w_n->alpha, k(t_n,w_n)=0. No root branch, Puiseux expansion or derivative is used. The supplied proof is complete.

Actual graph points: x_n=1/t_n, y_n=t_n w_n are genuine points of C^2 with x_n!=0. There p=t^2 a->0, q=tb->0, r=t^-1 k=0 exactly, so the target tends to (0,0,0). From (4) with k=0: J(p,q)=-t^3[bounded]->0; J(p,r)=-t[(2a+ta_t)k_w-ta_w k_t]->0; J(q,r)=-[(b+tb_t)k_w-tb_w k_t]->-b(0,alpha)k0'(alpha), and (3) at t=0 gives b(0,alpha)=4alpha+6 because k0(alpha)=0. All three limits are as ROOT states.

Coefficients: A,B1,C1 are fixed elements of C[U,V,W]; their values at a point depend only on (p,q,r) at that point, so they tend to A(0),B1(0),C1(0), the same values used at the actual source origin. Relations in B or singularity of Spec B are irrelevant once representatives are fixed, and ROOT fixes them once. The identity (2) is an equation in C[x,y], valid at every point of C^2; it is evaluated at the origin and at the points (x_n,y_n), and limits are taken of complex numbers. No source point is deleted and no ring is localized. So c0=C1(0).(-(4alpha+6)k0'(alpha))=(c0/2)(4alpha+6)k0'(alpha), giving (5) at every root of k0. Legitimate.

## C. Repeated roots, k0 divisibility, leading coefficient, D>=1, contradiction — CONFIRMED

(5) is a product equation; no division by b, 4alpha+6 or k0' occurs. If k0'(alpha)=0 then 0=2; if 4alpha+6=0 then 0=2. So every root is simple and k0 is squarefree, with D=deg k0 distinct roots. k0(0)=2 and k0'(0)=-3 for every h (the w^2 h term has zero first jet), so k0 is nonconstant and D>=1 with no genericity: D=1 for h=0, D=deg h+2 for h!=0. L=(4w+6)k0'-2 vanishes at the D distinct roots, so k0 divides L. deg k0'=D-1 with leading coefficient D c_D (characteristic zero, D>=1), so L has degree exactly D and leading coefficient 4D c_D; hence L=4D k0. At w=0: 6(-3)-2=-20 versus 8D. Impossible. The argument starts from a supposed nonzero constant in M with fixed B-coefficients; it never assumes a pair, a nonzero b, or generic h. Cauchy–Binet (df wedge dg expanded in du_i wedge du_j) puts every J(F(p,q,r),G(p,q,r)) in M with coefficients F_i G_j-F_j G_i evaluated on (p,q,r), so the pair statement follows from (1).

## D. Astra homogeneous-only argument — CONFIRMED, as the t=0 slice only

Independently checked: C[x,y,y^-1]=C[w,y,y^-1] is a faithful localization of a domain; x=w/y gives p=y^2 a(w), q=y b(w), r=y^-1 w k(w) with Astra's a,b,c=wk. Note Astra's b is ROOT's b(0,w)/w and Astra's c is ROOT's k0 times w; ROOT (3) and Astra's wb=4w+6-3(1+w)^2 k are the same identity. With wt(x)=-1, wt(y)=1, C[x,y] is a direct sum of weight spaces with C[x,y]_0=C[w]; homogeneous generators of weights 2,1,-1 make B graded regardless of relations or freeness, and weight projection of a module expression is componentwise. p^i q^j r^k with 2i+j-k=-m equals r^m (pr^2)^i (qr)^j, so B_0=C[bc,ac^2], B_-1=rB_0, B_-3=r^3 B_0 as subspaces. J_xy(w,y)=y and the F=y^m A, G=y^n B formula give y^(m+n)(nA'B-mAB'); the three generator Jacobians and weights 3,1,0 check. Equation (1), d3(0,0)=-C0/2 from c(0)=0, b(0)=1, c'(0)=2, and evaluation at a root alpha (bc and ac^2 both vanish, so the same d3(0,0) appears) give b(alpha)c'(alpha)=2 with c'(alpha)=alpha k'(alpha), hence the same (3) and the same -20=8D. Controls -2 at 0 and 26 at 2/3 recomputed (b(2/3)=13, c'(2/3)=-2).

This covers H=y^2 h(xy) only: y^3 has weight 3, so a general wedge H is not homogeneous and the grading projection is unavailable. ROOT replaces the projection by the t->0 limit at actual points; confirming D does not confirm ROOT, and I audited ROOT's limit route separately in B.

## E. Controls, reparametrization, exact scope — CONFIRMED

H=0: k=2-3w has no t-dependence, r=0 is exactly w=2/3, b_t=0, and (4) gives J(q,r)=3b(2/3)=3(26/3)=26 on the whole line, versus -2 at the origin; (5) reads -26=2. H=y^3+y^4: K(w,v)=v+v^2, T=tw^3+t^2 w^4, k0=2-3w, same conflict; it is not of the form y^2 h(xy), so it lies outside Astra's family and inside ROOT's. Plane x=0: (P,Q,R) restrict to (z+4y^2,y,0); in coordinates (y,z), J(z+4y^2,y)=-1 (ROOT's "Jacobian-1" reads as -1 with the sign lost to formatting; Astra prints -1; the ordering-dependent sign is immaterial). p=y^2,q=y,r=x gives J(q,r)=-1, so no blanket three-generator claim is available or used. Reparametrization: J(f o psi, g o psi)=(J(f,g) o psi) J(psi), J(psi) a nonzero constant by the polynomial inverse; the transformed module is J(psi) psi^*M, and psi^* fixes C, so a constant in it pulls back to a constant in M. Exact scope: entire polynomial graph, wedge j-i>=2, polynomial target coefficients; nothing is claimed for other H, other planes, rational coefficients or ambient maps, and ROOT says so.

Old versus new: the September 6 theorem is all H, linear outputs only; the new result is wedge H, all polynomial outputs; neither subsumes the other, and the wedge result subsumes Astra's homogeneous theorem as the K(w,0) slice. ROOT states this correctly.

## Verdict

GRAPH-WEDGE-1: CONFIRMED on every step A–E, with no GAP, at the stated scope. No step fails, so no weaker surviving claim is needed. Cosmetic only: ROOT's "Jacobian-1" sign formatting and "4w+6" spacing. No theorem hunt, experiment, next family or descendant was performed. No charge_basis line: no exit-price assertion is made here.

## Postpins and readback

Recorded below after the final WHOLE readback of this report and the re-hash of both inputs.

WHOLE readback of this report done 2026-09-12 01:36 UTC. Input postpins re-hashed at /tmp/jc2-lane.IlmR6j/inputs after the readback; both identical to the prepins:

    equivariant-graph-nonlinear-obstruction-root-20260912.md  8ae6ee53450d7a7ef4e688cf768903ca9900f8e4f176088076c3c8bf9cdde828
    equivariant-graph-nonlinear-obstruction-astra-20260912.md 4c253ddf7fd1cc6c5cfad90dbefec5f609a5ea2d4dcdb5a300b2feb35a94200d

No artifact_finalize; launcher owns custody. No edits after the marker.

<!-- BODY-END -->
