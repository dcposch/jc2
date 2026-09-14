# Global boundary degree on the exact pseudo-plane

MANUAL / UNREVIEWED. First action 2026-09-12 08:46:39 UTC; TASK and four other frozen input hashes matched before body reads. All new owned output targets absent; root TASK retained. Original publication reserve 09:07 / HARD 09:10 UTC unchanged. No scientific execution, external source, worker, or shared edit. General-H question only; no sparse-family successor.

## 1. Outcome: an all-H monodromy obstruction, not a boundary-degree theorem

The arbitrary-H assertion remains GAP: neither its proof nor a boundary-nonlinear global submersion is supplied. The new discriminator is a non-Euler, exact global identity. If H is everywhere submersive on the specified S and p(Z)=H|L has degree d>=1, put

    h(x,y)=H(x^2, x+x^3 y, 2y+x^2 y^2).

Over a suitable punctured base there is a natural short exact sequence of complex local systems

    0 -> H^1(T_c,C) -> H^1(h^-1(c),C) -> C[p^-1(c)] -> 0.       (M)

The last term is the actual degree-d permutation local system of p, not just its dimension. Consequently EVERY finite critical value of p forces nonidentity monodromy on H^1 of the source polynomial fiber. Since h itself is submersive, these are bifurcations at infinity. In particular d>=2 forces at least one such infinity value.

This is a global necessary condition for arbitrary H, without weights, degree caps, mate, connected fibers, or generic genus assumptions. It does not exclude nonlinear p: the attempted inference that submersivity rules out the needed infinity monodromy is false. The exact H=Z control below already has nontrivial order-two infinity monodromy. No new Euler-defect calculation is used; ROOT's historical veto of that route is retained.

## 2. Scheme fiber and verified double cover

Let S=Spec C[A,U,Z]/(U^2-A-A^2 Z). Its displayed gradient never vanishes: A=U=0 leaves the A derivative -1. On A!=0,

    R[A^-1]=C[A,A^-1,U],        Z=(U^2-A)/A^2.

Thus A:S->A1 has general fiber A1. Its zero fiber is Spec C[U,Z]/(U^2), scheme-theoretically 2L. At the generic point of L, 1+AZ is a unit and U^2=A(1+AZ), so ord_L(A)=2. This verifies the global multiple-fiber input; it does not classify unrelated fibrations H.

Set T={t^2-1=x^2 Z} and define pi:T->S by A=x^2, U=xt, Z=Z. The surface T is smooth, as its gradient cannot vanish on the equation. On D(A), adjoining x with x^2=A is finite etale of degree two, with t=U/x. On D(1+AZ), adjoining t with t^2=1+AZ is finite etale of degree two, with x=U/t. These two opens cover S. The formulas identify their rings with the displayed T, proving that pi is finite etale of degree two everywhere, not only away from L.

Its preimage of L is the disjoint union L_+={x=0,t=1} and L_-={x=0,t=-1}, each mapped isomorphically to L via Z. The plane chart

    j:A2_(x,y) -> T,       t=1+x^2 y,       Z=2y+x^2 y^2

is exactly T minus L_-. The inverse is y=(t-1)/x^2 on D(x), and y=Z/(t+1) on D(t+1). They agree because (t-1)(t+1)=x^2 Z, and these opens cover T minus L_-. This is a verified global open immersion, not an assertion that T itself is the plane. The composition pi j is the source map defining h above and is etale. Hence submersivity of H implies submersivity of h and of Htilde=H pi.

## 3. Residues retain the actual permutation monodromy

Assume p nonconstant. For c avoiding its finite critical values, let T_c=Htilde^-1(c). It is a smooth affine curve, possibly disconnected. Let D_c=L_- intersect T_c: these are exactly d distinct points indexed by p^-1(c). The verified plane chart gives h^-1(c)=T_c minus D_c.

The ordinary cohomology localization/Gysin sequence for a smooth curve minus finitely many points gives

    0 -> H^1(T_c,C) -> H^1(T_c minus D_c,C)
      -> direct_sum_(a in D_c) C -> H^2(T_c,C)=0.

The middle-to-right map records small-circle residues, up to one fixed common normalization. H^2 is zero because each smooth affine curve component is noncompact and has the homotopy type of a one-dimensional CW complex. No component connectedness or genus value is imposed. There is NO sum-zero relation among just these d newly removed points: a compactification's residue relation also involves its original points at infinity. This holds componentwise for disconnected T_c. In particular these d puncture classes cannot disappear by cancellation in the rest of the affine curve.

Choose a finite exceptional set so that the algebraic families and their marked complements are topologically locally trivial off it. Precisely, take Sigma to contain CritVal(p), finite topological exceptional sets for h and Htilde, and the exceptional values of a compatible stratified compactification of the marked pair (T,L_-); use the common base V=C minus Sigma. No assertion is made that deleting only CritVal(p) suffices, or that Sigma is minimal. The standard finite stratification/compactification theorem for complex algebraic maps and pairs supplies this choice; it is not a claim of triviality at special fibers or at infinity. Naturality of residues under transport makes the displayed sequences a short exact sequence of local systems, proving (M). The permutation action is exactly that of the finite polynomial map p:L_->A1. This is stronger information than Euler characteristic or a Betti-number difference.

Let c0 be a critical value of p. Take a sufficiently small circle about c0 avoiding all other exceptional values. Local monodromy of p is a product of disjoint ramification cycles, at least one of length greater than one, so its permutation action is not identity. Equation (M) makes it a quotient of source-fiber monodromy. Therefore the latter cannot be identity. If h were topologically locally trivial over a disk about c0, its cohomology monodromy around that circle would be identity, a contradiction. Since h has no affine critical point, this failure is at infinity. We have proved the exact inclusion

    CritVal(p) contained in B_infty(h).                         (B)

Here B_infty means finite values where this submersive polynomial is not locally topologically trivial. For d>=2, p' has a complex zero, so the left set is nonempty. For d=1 it is empty. If p is constant, D_c is empty for generic c and there is no positive-rank permutation quotient; that case is separate, not a degenerate use of a finite map.

## 4. Exact stress-tests and the failed inference

**H=Z.** This is submersive on S: a critical point of the Z projection would require U=0 and 1+2AZ=0, whereas the defining equation would then give A=0, a contradiction. Its plane pullback is h=2y+x^2y^2. For c!=0, choose a local square root of c and write

    w=t+sqrt(c)x,     w^-1=t-sqrt(c)x.

This identifies T_c with C*, and L_- meets it at w=-1. Thus h^-1(c)=C* minus {-1}, a connected curve. Going once around c=0 changes the square-root sign and gives monodromy w->w^-1, preserving the omitted point. The nonzero cohomology class dw/w changes sign, so source-fiber monodromy is genuinely nonidentity, of order two. At c=0, the plane fiber is the disjoint union y=0 and x^2y=-2; it is disconnected. This independently displays the infinity bifurcation despite everywhere nonzero differential. No Euler count is needed. Here p=Z has degree one, so (M)'s puncture quotient itself has trivial monodromy: the nontrivial action is in the ambient-curve part. The distinction between these parts is essential.

**Plane-only stronger control.** Independently checking ROOT's optional formula, f_m(x,y)=y+(xy)^m, m>=2, is submersive: its x derivative can vanish only when x=0 or y=0, where its y derivative is 1. For c!=0, w=xy identifies the fiber with A1 minus {w^m=c}, by y=c-w^m and x=w/(c-w^m). Thus its H^1 is the full m-puncture permutation module, with m-cycle monodromy about zero. Arbitrarily large such cyclic modules are compatible with a nonsingular plane polynomial. This is NOT an H on the specified S, not an invariant-descent claim, and not a scalar mate; it refutes a generic plane-submersion monodromy bound, not the target assertion.

**H=U+q(AZ).** The accepted gate's exact positive control is submersive for every polynomial q, with p=q(0) constant. For generic c!=q(0), D_c is empty and the quotient in (M) has rank zero. Nothing in the argument rules out this family or presumes its fibers have constant topology.

**Local H=u+z^d.** Its differential has du coefficient one. Restricting to the omitted local curve u=0 gives z^d; the d punctures in H=c collide there as c approaches zero without producing a critical point of H. At a critical point of nonconstant p on L_-, submersivity ensures a nonzero transverse derivative, so this same local transverse-versus-restricted-ramification distinction applies. Global residue surjectivity in Section 3, not boundary coprimality, is what proves that the resulting puncture permutation survives in source cohomology.

These controls refute the attempted inference "smooth/submersive H implies no relevant infinity monodromy." Scheme fiber 2L verifies the source geometry but does not make the A-fibration functorial under an arbitrary H. A theorem imposing local triviality of h across every critical value of p would, by (B), yield d<=1; no such theorem follows from submersivity, and a blanket no-infinity-bifurcation version is disproved by H=Z. No connected-fiber, rational-fiber, genus, properness, or locally finite Hamiltonian assumption is inserted.

## 5. Remaining quantity, scope, and custody

Settled at MANUAL/UNREVIEWED tier: the exact cover and plane-open attachment, the residue/permutation sequence (M), and the all-H inclusion (B). This is not a sparse-family theorem or a repetition of Euler cancellation. Named standard topological imports are the cohomology localization/Gysin sequence for punctured smooth curves, vanishing of ordinary H^2 for smooth affine curves, and finite stratified topological triviality for algebraic maps/pairs after a compactification. They are not represented as newly primary-read or completely re-proved.

GAP quantity remains exactly the arbitrary-H boundary-degree assertion. To close it through this discriminator requires an additional restriction on the nontrivial boundary-permutation quotient for these invariant source submersions; merely forbidding affine critical points does not supply that restriction. No proof of this missing global property, and no boundary-nonlinear H, is claimed. The result gives neither a scalar pair nor exclusion of all scalar pairs, and no Keller or JC2 conclusion. The local and global positive controls are not counterexamples to d<=1.

Cheapest next test, only if ROOT separately selects it: one focused manual review of the residue local-system quotient and the exact H=Z monodromy control, approximately 10 minutes UNMEASURED planning, not a computation or runtime forecast. No successor, classification import, degree farm, or additional model is authorized.

Read scope: TASK and the three charged scientific reports were read FRESH_WHOLE after current pins, including their seals/markers. COORDINATION's current matching bytes reuse this agent's prior WHOLE reading of all 806 lines today at 05:51–05:53. The old gate's general-H item F remains GAP. ROOT's history-only Euler veto was followed without opening the cited historical report; no linked scientific input was read or promoted. PINS and READ-SCOPE record all five input hashes and exact modes. Own complete readback, unchanged five postpins, collision/quantity checks, marker LAST, and transaction close/finalize/expected verify precede custody and terminal ALL WRITERS IDLE. Root TASK and every old artifact remain unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11627`.
- Body SHA-256:
  `135d2998cfd2b77611f94388d1fab003bd6f4d21b3541413eec7ecda7b232f8b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
