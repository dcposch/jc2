# Arbitrary submersions and boundary degree on the exact pseudo-plane

MANUAL BOUNDED TEST / UNREVIEWED. No Keller-pair assumption or source outcome.

Actual first action2026-09-11 08:31:32 UTC; own report/manifest/box absent. Original reserve08:44/HARD08:47 UTC, never reset. Exactly the nominated homogeneous producer and its manifest were freshly hash-pinned before fresh WHOLE reads. Its exact ring/bracket and homogeneous no-mate scope are accepted inputs, not re-proved. The pending linear-U producer and live FIRST report are not inputs and are not consumed.

## Target and scope

Work over C on R=C[A,U,Z]/(U²−A−A²Z), with its displayed nondegenerate bracket. The question is whether every arbitrary regular everywhere-submersive H has affine restriction H|L in C[Z] on L={A=U=0}. This is an H-only assertion, not a consequence assumed from any hypothetical mate. No restriction on the total degree or normal form P(A,Z)+UQ(A,Z) is imposed.

## 1. Verdict and exact open chart

GAP for the arbitrary-H boundary assertion: no globally submersive counterexample with boundary degree≥2 is obtained, and the assertion for arbitrary numbers of homogeneous components is NOT proved. Two unbounded-degree obstructions below are proved manually: the entire two-homogeneous-component case, and the three-component family U+Z^d+q(AZ), with d≥1 and arbitrary polynomial q. These are partial theorems, not a finite degree search or an inference from the pending linear-U result.

Put t=AZ and u=U. The open set U≠0 has coordinate ring C[u,u^−1,t,(1+t)^−1]; t itself is NOT inverted. The two-sided formulas are

A=u²/(1+t), U=u, Z=t(1+t)/u².

Indeed U²=A(1+t) forces both A and1+t nonzero when U≠0. These are actual coordinates on that open set, so vanishing of the two derivatives with respect to u,t is equivalent to a critical point there. The value t=0 is allowed by the chart. Later constructions explicitly avoid t=0 and−1 where required, not by an unproved localization of the target theorem.

At any point of L the relation has differential−dA. For H=P(A,Z)+UQ(A,Z), therefore

dH|_(0,0,z)=Q(0,z)dU+P_Z(0,z)dZ.

This boundary condition alone is insufficient; the arguments below construct critical points OFF L. The homogeneous no-mate theorem is accepted background only and is not used to assert that a submersion has a mate.

## 2. Complete obstruction for two separated weights

For every integer d≥1 and nonzero f,g in C[t], the regular function

H=U f(t)+Z^d g(t)

has a critical point. Set h=t^d(1+t)^d g(t). On the chart,

H=u f(t)+u^(−2d)h(t).

Where f h≠0 its critical equations are exactly

u^(2d+1)=2d h/f,  K=2d h f'+f h'=0.

To produce such a t, let M=h f^(2d). It has at least the two distinct roots0 and−1, and is nonzero. Write its degree N and its number of distinct roots r≥2. At a root of multiplicity e, its derivative has multiplicity exactly e−1 in characteristic zero. Thus M' has N−r zeros on M=0, counted with multiplicity, but degree N−1; it has r−1≥1 zeros away from M=0. Choose one, t0. The identity M'=f^(2d−1)K yields K(t0)=0 and f(t0)h(t0)≠0. In particular t0 is neither0 nor−1. Choose any nonzero (2d+1)st root of 2d h(t0)/f(t0) in C. The resulting chart point satisfies both derivative equations and is critical on the full surface. No simple-root, squarefreeness or f(0)g(0) assumption was used.

Corollary: if an everywhere-submersive H is a constant plus at most two homogeneous components for the exact grading wt(A,U,Z)=(2,1,−2), then H|L is affine. To see this, suppose its boundary degree is d≥2. A component of weight−2d contributes its nonzero leading boundary term and has form Z^d g(t), g(0)≠0. The accepted fixed-point cotangent weights1,−2 imply that the other component must have weight1 or−2; otherwise dH vanishes at the origin. In weight1 it is U f(t), excluded by the theorem. In weight−2 it is Z f(t); both components are even-weight and contain no U in monic normal form. Hence Q(0,z)=0 while H|L has degree d, so its derivative has a complex root and H is critical on L. Constants do not affect differentials. This treats arbitrary component degrees, not bounded total degree.

## 3. A three-weight obstruction with arbitrary weight-zero polynomial

For every d≥1 and every q in C[t],

H=U+Z^d+q(AZ)

has a critical point. This includes an arbitrary nonconstant weight-zero component, so the preceding two-component proof alone does not cover it. Let s=t(t+1), h=s^d and N=2d+1. On U≠0,

H=u+u^(−2d)h(t)+q(t).

The critical equations are u^N=2d h and h'+u^(2d)q'=0. If q'=0 identically, take t=−1/2, where h≠0 and h'=0, and choose u^N=2d h; this is a critical point.

Suppose q' is nonzero. Eliminating u gives the necessary polynomial equation

E(t)=(h')^N+(2d h)^(2d)(q')^N=0.

Since h'=d s^(d−1)(2t+1), this factors EXACTLY as

E=d^(2d) s^((d−1)N) R(t),
R(t)=d(2t+1)^N+2^(2d) s^(d+1)(q')^N.

The second term of R has degree2d+2+N deg(q'), strictly greater than the first term's degree N=2d+1. Therefore R is nonconstant. Moreover R(0)=d and R(−1)=−d. A complex root t0 exists and is neither0 nor−1. Thus h(t0)≠0 and E(t0)=0; no lost s-factor is used to manufacture this root.

Every such root lifts, including exceptions. If q'(t0)=0, then R(t0)=0 forces2t0+1=0, hence h'(t0)=0; any nonzero u with u^N=2d h gives a critical point. If q'(t0)≠0, E(t0)=0 forces h'(t0)≠0. Set

u=−2d h(t0)q'(t0)/h'(t0).

Then E=0 gives u^(2d)=−h'/q'; multiplying by u gives u^N=2d h. Both critical equations hold and u≠0. All divisions are restricted to their proved nonzero cases. This is a global critical-point certificate for the family, not a resultant assertion or a computed coefficient experiment.

## 4. Positive control and precise remaining GAP

For EVERY polynomial q in C[t], H=U+q(AZ) IS everywhere submersive, and H|L=q(0) is constant. On U≠0 its u-derivative in the same chart is1. At U=0,A≠0, the bracket {H,A}=−2A²−4AUq'(AZ) is−2A²≠0. At A=U=0, d(AZ)=Z dA=0 in the surface cotangent space, so dH=dU≠0. These three sets cover the surface. This proves the hinted U+AZ case and a whole family directly, without assuming that mixed functions are homogeneous or have scalar mates. It is also a meaningful control: deleting Z^d from Section3 changes a universally critical family into a universally submersive one. Here affine boundary includes constants; if 'affine' were intended to mean nonconstant degree1, U itself would already refute that stronger wording.

The general claim remains unresolved for arbitrary sums of homogeneous components. In the open chart, an arbitrary regular H becomes a finite Laurent sum in u with coefficients rational in t, with possible poles at t=−1 dictated by the original regular expression. Two separated u powers admit the single derivative polynomial M used above. For Section3 the extra weight-zero term preserves a two-term H_u, permitting the explicit E and a noncancelling leading-degree argument. With additional independent weights, H_u itself may have more terms, and no corresponding one-variable polynomial whose nonboundary roots MUST lift to critical points has been established. Boundary coprimality of Q(0,z),P_Z(0,z) does not supply that missing implication.

Thus no general boundary-degree theorem, explicit boundary-nonlinear submersion, or Keller-pair exclusion beyond the accepted homogeneous scope is claimed. The étale selfmap and ruling/Picard hints are not used; no étale functoriality, unique ruling, rational-deck argument, topological classification or literature premise is imported. No finite degree farm or source/candidate computation occurred. ROOT's bounded history context is not exhaustive novelty certification.

QUANTITY: whether the proved two-component and U+Z^d+q(AZ) obstructions survive independent review, and whether arbitrary additional weights can evade them while retaining a nonlinear boundary restriction. CHEAPEST TEST for the completed partial result: a10-minute UNMEASURED focused manual review of the chart, derivative-root count, exact E-factorization and exceptional-root lifting. A future general-H attempt requires a new bounded choice of a nontrivial global discriminator, not extrapolation from these families; none is authorized here. No canonical OPEN identifier, rank/source result, all-R no-mate theorem or JC2 conclusion follows.

Own-only COLLISIONS: NONE; only the nominated leased report and owned PINS/custody are written. All mathematics is manual; no scientific subprocess/import/AST/syntax/test/CAS/dummy, payload, external/history/linked input, network/AWS/Git/process control, protected/shared edit or agents. The two-weight hint arrived as an untrusted ROOT message and was independently derived here; Section3 and the positive control were independently derived from the same exact ring. No pending producer or live review bytes were consumed.

Closeout08:40:15 UTC: own report/PINS freshly WHOLE without clipping; both input postpins and owned PINS match. Final report/manifest remain absent; no stray standalone marker; QUANTITY/CHEAPEST TEST/numeric UNMEASURED wall and own-only collision check complete. Mathematical status is PARTIAL with exact general-H GAP and the two proved scoped obstructions, all new claims UNREVIEWED. This marker is the final scientific/report write. Only documentary close/finalize/expected verification, sealed readback and custody remain before ORIGINAL08:44 reserve/08:47 hard stop.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9521`.
- Body SHA-256:
  `ad29886d121b5bc36d9c35b9c3e88bb6d2c13f2e5371269bbdd57216efe2162c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
