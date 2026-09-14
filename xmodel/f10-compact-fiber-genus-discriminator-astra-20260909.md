# F10 r1 compact-fiber genus discriminator

Basis 0d39df3c9fd69c939a8420c54d03228b9077777d. First action 2026-09-09 15:32:35 UTC; controlling stop 15:44:35 UTC. PRODUCER-ONLY / PENDING INDEPENDENT REVIEW. PURE MANUAL MATHEMATICS; no mathematical subprocess. The two accepted16q/r inputs were pinned before WHOLE reads. This is a conditional geometric discriminator, not a point, exclusion, ideal decision or compute authorization.

## Outcome

For any hypothetical COMPLETE guarded r1 point, the normalized source's generic fiber is geometrically integral and birational to the compact quartic A=lambda. Its genus is **exactly three**, not merely at most three. Moreover the compact critical scheme has length nine, with multiplicities, and is supported scheme-theoretically on Delta=0. These are direct consequences of the accepted full identities. They explain why a generic-small-genus shortcut supplies no exclusion: the potentially exceptional fibers occur at the deleted divisor of the source chart. Chau's all-fiber hypotheses are not supplied. Verdict: PROVED GEOMETRIC REFINEMENT / NO_GAIN toward exclusion by this shortcut.

## 1. The actual birational fiber, including integrality

Work over an arbitrary characteristic-zero coefficient field and then its algebraic closure if desired. Accepted16r gives

    A=St^3+(Sd-u)t^2+(1-ud+Sv)t+k,
    deg d<=1, deg v<=2, deg k<=4, k(0)=0,
    a=k4!=0, deg B=7, B5=S^2, [A,B]=Delta.

The guard also retains the nonzero leading S^7 coefficient of B. Scalar restoration divides A by a and B by its own leading coefficient. Thus the normalized source component A composed with the chart and the restored source P differ only by a nonzero scalar; their fiber parameters are correspondingly relabeled. Actual source degrees remain112/196, not4/7.

Use precisely the accepted16q maps, writing S for its translated R:

    g=V^-1, p=V^3 U-V, d_ref=p^2+ell*p-u,
    W=1-V*d_ref, z=-W/V, t=-V/W,
    S=pz^3-z^2+uz.

Their inverses are p=Pi, g=-Delta/t, V=1/g and U=g^2(1+gp). On source D(VW) and compact D(t Delta) these are mutually inverse regular maps. In particular the common rational function field is unchanged and K(P)=K(A) after the recorded scalar relabeling. The generic fibers contain these dense opens: neither nonzero denominator becomes zero in the generic function field. Consequently their generic curves, not their entire affine fibers, are birational. There is no inference that the degree of (P,Q) is three from a module rank or from a cubic projection.

For completeness, A-lambda is integral over K(lambda): its affine coordinate ring is the localization of the domain K[S,t] along nonzero elements of K[A]. Its projective closure is an integral degree-four plane curve. At O=[S:t:Z]=[0:1:0], the derivative in S of its homogenized equation is one, from the term St^3. Thus O is a K(lambda)-rational smooth point. In characteristic zero, the geometric components of an integral curve are Galois-conjugate; a rational smooth point lies on a unique such component, which every Galois element must fix. Transitivity then leaves only one component. This proves geometric integrality without assuming all special fibers irreducible.

## 2. Full mate identity forces genus three, not a drop

The homogeneous leaders and top bracket are

    A4=S(t^3+d1*S*t^2+v2*S^2*t+k4*S^3),
    [A4,B7]=-S^2*t^7.

The last identity is the total-degree-nine part of [A,B]=Delta; the degree-nine part of Delta is exactly -S^2*t^7. No lower homogeneous term can enter it. The factor S occurs simply in A4 because the cubic evaluates to t^3 at S=0. The factor t does not divide A4 because k4 is nonzero. Any other repeated linear factor L of A4 would divide both partial derivatives of A4, hence divide [A4,B7]. But such L divides neither S nor t, contradicting the displayed target. Therefore A4 is squarefree over the algebraic closure.

Every projective compact fiber consequently has four distinct, smooth points at infinity: squarefreeness ensures its binary leading form has a nonzero tangential derivative at each root, independent of lambda. The two cubics A_S and A_t have no common point at infinity, by Euler's identity and squarefreeness of A4. They have no common curve component either, since the projective closure of such a component would meet infinity. Bezout therefore gives a zero-dimensional affine critical scheme of length3*3=9, counting multiplicity, not necessarily nine distinct points.

All but finitely many compact fibers are smooth in the affine plane as well. Their projective completions are smooth quartics. Plane adjunction gives 2g-2=4, hence g=3. Birational invariance gives the same geometric generic genus for the actual source P. For the critical scheme, the full mate identity reads Delta=A_S B_t-A_t B_S, so Delta belongs to its defining ideal. Its entire scheme is on Delta=0, precisely outside the above chart. This is not an extra independent equation beyond the full Jacobian rows, and its existence is not an obstruction to the source being a submersion.

## 3. Why compact infinity and source infinity differ

Even the point O at compact infinity need not be a puncture of the source fiber. The full A boundary formula is A=k+p+v*x+d*y. On the inverse chart

    S=pz^3-z^2+uz, x=St=u-z+pz^2,
    y=St^2-ut=-1+pz.

At z=0 it gives A'=p+u*v0-d0. Thus on A=lambda this point has p=lambda-u*v0+d0. If p^2+ell*p-u is nonzero, which holds for the generic lambda, the inverse formulas V=1/(p^2+ell*p-u) and U=g^2(1+gp) are regular there. So O corresponds to a finite source point. Conversely Delta=0 can remove finite compact points. Merely counting four points at compact infinity does not count source punctures or establish properness of Q on a source fiber.

The full source Jacobian makes every affine source fiber smooth, but it does not by itself make that fiber connected or irreducible. The birational charts do not identify all special fibers as complete affine curves, nor prevent variation of geometric genus through points on the excluded divisor. No uniform-family claim has been derived from the ten pole equations or the mate reconstruction.

## 4. Primary theorem interface and controls

Chau, arXiv:1005.3866v2, Theorem3 on printed1, requires every fiber to be irreducible and to have the same genus. Its proof on printed2–4 uses these assumptions to control completed special fibers and then an Euler-characteristic identity. A generic genus bound, even exact genus three, does not meet those hypotheses. The primary PDF and exact read scope are retained; no inaccessible Friedland statement or search snippet is imported. [Primary theorem and proof](https://arxiv.org/pdf/1005.3866v2).

The missing arrow is concrete: one would have to prove all actual source fibers irreducible and genus three, despite the compact critical fibers and missing divisor. Neither accepted input provides it. If those two conditions were established, Chau would contradict the conditional source's noninvertible Keller endpoint; that conditional implication is not a proof of its premise.

Manual changed-hypothesis control: drop the leading guard and take u=0,d=v=k=0. Then A=t+St^3 is inverse-ordinary, since it becomes p under S=pz^3-z^2,t=z^-1. Its generic fiber is rational, parametrized by t with S=(lambda-t)/t^3. Its quartic leader St^3 is not squarefree and k4=0. This is not a complete guarded point or a mate construction; it shows exactly why the guard cannot be omitted from the genus-three proof. Conversely the accepted16r section8 family u=ell=d=0,v=S^2,k=S^4 retains upper mate rows, poles and nonzero leading guard but fails the final constant residual by -1. No genus statement on such a relaxed family decides the complete system.

OPEN (existing missing interface, not a new campaign ID): all-fiber uniformity/irreducibility proofs supplied = 0. Cheapest genuinely relevant next check would describe the special source fibers corresponding to the finite critical values on Delta=0, including their missing branches; it is not a generic quartic-genus computation or another exact-differential reformulation. This task authorizes no such continuation. The existing run remains INCONCLUSIVE. Own-only raised-item check records this one existing missing interface, no new global open problem or corpus collision. All writers are idle at terminal handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8376`.
- Body SHA-256:
  `b5df9a9ea7d85459309dc391bc34e0e02ab0a2558ef236c5c5e44413bd9b2da7`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
