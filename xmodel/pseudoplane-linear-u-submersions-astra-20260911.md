# All submersions linear in U over k[Z] on the exact pseudo-plane

MANUAL THEOREM / UNREVIEWED new result; no computation, source or JC2 claim.

Actual first action2026-09-11 08:08:59 UTC. Own targets absent. ORIGINAL publication reserve08:19/HARD08:22 UTC, never reset. Exactly four frozen inputs are charged; all hashes matched before bodies. The receipt's corrected path ends .run.v2, not .md.run.v2; the latter exact-path hash failed because absent and read no body. The correct sibling pin matched before its fresh WHOLE read. No other input was opened.

## 1. Statement and differential criterion

Let k be algebraically closed of characteristic zero and

R=k[A,U,Z]/(Phi), Phi=U²−A−A²Z,

with the accepted bracket {A,U}=2A², {A,Z}=4U, {U,Z}=2+4AZ. For arbitrary-degree P,Q in k[Z], put H=P(Z)+UQ(Z). Then H:Spec R→A¹ is everywhere submersive if and only if

H=aU+b or H=aZ+b, with a in k* and b in k.

Consequently no H of this envelope admits ANY regular mate G in R with {H,G} a nonzero scalar. G has no degree, grading or shape restriction. The proof of that consequence uses the accepted homogeneous no-mate theorem only after the new submersion classification. No extension to P(A,Z)+UQ(A,Z), to an added A S(Z), or to arbitrary mixed H is asserted.

The surface is smooth: Phi_Z=−A²=0 forces A=0, where Phi_A=−1−2AZ=−1. The accepted bracket is −2 times the Jacobian bracket against Phi. Its matrix at each point has rank2 and kernel spanned by the nonzero conormal dPhi; hence its induced alternating form on the surface cotangent space is nondegenerate. Thus dH=0 in that cotangent space exactly when {H,A}={H,U}={H,Z}=0. Here submersive means this differential is nonzero at every geometric point, equivalently the rank-one differential condition for a morphism between these smooth k-varieties.

Writing P',Q' for derivatives in Z, the generator brackets are exactly

{H,A}=−4U(P'+UQ')−2A²Q,
{H,U}=−(2+4AZ)(P'+UQ'),
{H,Z}=(2+4AZ)Q.

These follow by Leibniz and do not require Q or a coordinate to be a unit.

## 2. An exact critical-point discriminator off the boundary

For v in k*, the point

p_v=(A,U,Z)=(2v²,v,−1/(4v²))

lies on the surface and has 2+4AZ=0. The last two brackets vanish there and the first equals

−4v[P'(z)+v(Q'(z)−Q(z)/(2z))],  z=−1/(4v²).

Set D(Z)=2ZQ'(Z)−Q(Z) and E(Z)=16Z³(P'(Z))²+D(Z)². For every z in k*, E(z)=0 if and only if at least one of the two points p_v with v²=−1/(4z) is critical for H.

Forward direction, all cases: if D(z)=0 then E(z)=0 forces P'(z)=0, so either square root v gives criticality. If D(z)≠0, set v=−2zP'(z)/D(z). The identity E(z)=0 gives v²=−1/(4z), so v≠0 and P'(z)+vD(z)/(2z)=0. Conversely that equation and v²=−1/(4z) imply E(z)=0 after squaring. No division by a potentially vanishing quantity occurs except in the explicitly nonzero D case; z=0 is deliberately excluded from this chart, not discarded globally.

An everywhere-submersive H therefore forces E to have no nonzero root. If E is identically zero, taking z=1 in the preceding argument supplies a critical point, contradicting submersivity. Since k is algebraically closed, the remaining possibility is

E(Z)=c Z^m, with c≠0 and m≥0.

This includes nonzero constant E. No degree bound on P,Q has entered.

## 3. Monomial-factor parity and the remaining cases

Choose iota in k with iota²=−1. In k[T] define

F(T)=D(T²)+4 iota T³ P'(T²).

Then F(−T)=D(T²)−4 iota T³ P'(T²) and

F(T)F(−T)=E(T²)=c T^(2m).

Both factors are nonzero. Unique factorization in the polynomial ring implies F(T)=alpha T^n for alpha≠0, since every irreducible divisor of F divides T. Its reflected factor is alpha(−1)^n T^n, so n=m. If n is even, F(T)−F(−T)=0 gives P'(T²)=0, hence P'=0. If n is odd, F(T)+F(−T)=0 gives D(T²)=0, hence D=0. Characteristic zero gives, coefficient by coefficient,

D(Z)=sum_j (2j−1)q_j Z^j=0  implies Q=0.

All integers 2j−1 for j≥0 are nonzero in k. Thus an everywhere-submersive H has P'=0 or Q=0. This step treats arbitrary polynomial degrees simultaneously and keeps the m=0 case. It uses an auxiliary indeterminate T, not a source specialization or a restriction to actual coefficients.

Now use the entire boundary line L={(A,U,Z)=(0,0,z):z in k}. On L the relation has differential −dA, so dU,dZ are a cotangent basis and

dH|_(0,0,z)=Q(z)dU+P'(z)dZ.

If P'=0, then P=b is constant in characteristic zero. Submersivity forces Q(z)≠0 for every z in k, so algebraic closedness implies Q=a in k*. This gives H=b+aU. If Q=0, submersivity forces P'(z)≠0 for every z, hence P'=a in k* and P=aZ+b. Constants fail because their differential is identically zero. Roots at Z=0, excluded only from the preceding chart, are explicitly retained by this boundary argument.

Conversely U and Z really are everywhere submersive. For U, simultaneous vanishing of {U,A}=−2A² and {U,Z}=2+4AZ is impossible: A=0 makes the latter2. For Z, simultaneous vanishing requires U=0 and 1+2AZ=0. The surface relation at U=0 gives A(1+AZ)=0; A=0 contradicts 1+2AZ=0, while A≠0 forces AZ=−1, again contradicting it. Nonzero affine rescaling preserves submersivity. This proves both directions of the classification.

## 4. Unrestricted regular mates and field scope

A nonzero scalar bracket {H,G}=c forces dH nonzero everywhere: at any point where H−H(p) lies in the square of the maximal ideal, Leibniz puts {H,G} in that maximal ideal, contrary to c≠0. Equivalently use the nondegenerate cotangent bracket above. Therefore H in this envelope must be one of the two classified forms. For H=aU+b, the same equality gives {U,G}=c/a; for H=aZ+b it gives {Z,G}=c/a. U and Z are homogeneous of weights1 and−2 for the parent's exact grading. The accepted homogeneous no-mate theorem excludes both equalities for every regular G in R. The additive constant b is removed by the bracket, not falsely called homogeneous. Antisymmetry covers the envelope appearing as the other coordinate of a pair.

The classification also holds for geometric submersions over any characteristic-zero field K: extend scalars to an algebraic closure, apply the proof there, and compare coefficients in the unique normal form over K. The resulting a,b already belong to K. In particular a scalar-bracket pair over K would stay such a pair over its algebraic closure, since K embeds and a nonzero scalar stays nonzero; hence the no-mate consequence holds over every such K. A condition testing only K-rational points is weaker and is NOT substituted for geometric submersivity. Characteristic zero is essential to the coefficient argument and the imported no-mate theorem; no positive-characteristic extension is claimed.

Neither H nor G is localized: regularity on the whole surface, including A=0 and Z=0, is retained. No nilpotent quotient, degree truncation, leading-form replacement, locally-finite aside or extra source theorem is used. The accepted plane pullback remains only a sufficient counterexample interface. This result excludes that interface when either surface coordinate has this envelope; it does not classify all R, all Keller pairs or JC2.

## 5. Nonlinear control, classical boundary and next test

Take H=Z²+U/4. It is submersive at EVERY point of L, because dH there is (1/4)dU+2z dZ. Nevertheless p=(2,1,−1/4) lies on the surface and is critical. At p,

dPhi=(0,2,−4),   dH=(0,1/4,−1/2)=(1/8)dPhi,

so dH is zero in the surface cotangent space. This also checks the sign in the discriminator: D=−1/4 and E=64Z^5+1/16 vanishes at Z=−1/4. The chart is therefore doing work that the boundary differential test misses; replacing the mixed expression by its nonzero constant U coefficient would give a false conclusion. These are manual rational identities, not an executed fixture.

This argument is not merely restriction to the one affine line L. On that line the necessary differential condition only says P' and Q have no common zero, which the nonlinear control satisfies. The additional ramification curve and polynomial-factor parity rule out the mixed case. No assertion is made that no other classical theorem could imply the result. ROOT's bounded history check is context, not exhaustive novelty certification; this task performs no literature/history search and does not reopen the stopped affine-linear A,U,Z extension.

OPEN quantity: does the new all-degree submersion classification and its accepted-parent no-mate composition survive an independent static review? CHEAPEST TEST: one focused different-model manual check of the chart lifting including D=0/E=0/Z=0, reflected monomial parity, U/Z submersivity and unrestricted-mate/base-change scope. Planning wall10 minutes UNMEASURED, not a runtime forecast or review launch. No new canonical OPEN identifier, numerical degree farm, general mixed-H task, implementation or follow-on is authorized here.

Own-only COLLISIONS: none; report/manifest/box were absent at08:08:59. Exact four fresh-WHOLE pins, own report readback and terminal custody govern publication; no linked provenance, mutable ledger, old report, coefficient payload, scientific subprocess, import/AST/syntax/test/CAS, network/AWS, process control, Git, protected/shared edit or agent was used. Only this leased report and owned PINS/custody may be written. The external parent's BODY-END-only report is accepted through its charged lane receipt; no inappropriate local Seal verifier was applied to it.

Closeout08:13:07 UTC: own report and PINS were freshly read WHOLE without clipping; all four input postpins and owned PINS remained exact. Final report/manifest still absent, no stray standalone marker, OPEN quantity/cheapest test/numeric UNMEASURED wall present. The theorem and exceptional cases are complete as a manual candidate, not promoted. This final marker ends scientific/report authorship; only documentary close/finalize/expected verification, sealed readback and custody remain. Original08:19 reserve/08:22 hard stop unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10042`.
- Body SHA-256:
  `4fc13293aa49b8c4444c4624c2d892ce837441500c76870ab19d15e765baf8fd`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
