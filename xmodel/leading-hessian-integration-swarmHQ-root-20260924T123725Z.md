# A leading-Hessian obstruction to isotropic regularization of Keller weights

Producer and integrator: swarmHQ ROOT (Astra). Independent hostile reviewer:
Fable5.1/max, requested model; hosted identity not independently attested.
Date: September 24, 2026.
Evidence: MANUAL, elementary proof. Lifecycle: PRODUCER-CHECKED with independent
review; UNPROMOTED. Novelty UNKNOWN. JC2 remains unresolved.
Frozen public basis: `0434c6925ba288ffcd87fdc4052accd9d9fee554`.

## Exact statement

Let F:C^2 -> C^2 be polynomial with det JF=c != 0, and in the given source
coordinates put phi(z)=|F(z)|^2/2. The following are equivalent:

1. F is affine.
2. There exists a C2 strictly plurisubharmonic psi with globally bounded
   |psi-phi| such that the largest and smallest eigenvalues of its complex
   Hessian have uniformly bounded ratio.

Thus a nonlinear Keller potential cannot belong, in these coordinates, to
the W* class defined in Definition 1.1 of Liu--Wang--Zeng, arXiv:2609.26810v1.
This excludes a particular direct theorem application, NOT nonlinear Keller
maps themselves: nonlinear polynomial automorphisms are included in the
exclusion. It supplies neither an inverse nor a JC2 counterexample.

## Weak-limit lemma

Use a consistent Hermitian convention for H_h=(partial_i partial_bar_j h).
Suppose real C2 potentials h_t converge in distributions to a SMOOTH h and,
for a fixed K>=1, every t and every pair of constant unit vectors u,v satisfy

    u* H_h_t u <= K v* H_h_t v.

Then the same inequalities hold pointwise for H_h. Fix u,v, multiply the
inequality by any nonnegative compactly supported smooth test function,
and integrate. Distributional differentiation is continuous, so the limit
of K v*H_h_t v - u*H_h_t u is a nonnegative distribution. Its limit is a
smooth function; if negative at any point, a nonnegative test supported in
a sufficiently small neighborhood would give a negative pairing. Therefore
it is nonnegative everywhere.

The quantifiers are: for EACH fixed pair u,v the inequality holds at EVERY
point. Hence, at a chosen point, one may use a constant vector v in the
kernel of H_h at that point and a constant vector u in a positive
eigendirection. No position-dependent differentiation is involved. In
particular, the limiting Hessian cannot have both a zero and a positive
eigenvalue. The lemma uses smoothness of the LIMIT, not merely continuity
of the limiting potential, and does not assume pointwise Hessian convergence.

## Apply dilation

Assume d=max(deg F_1,deg F_2)>1. Write F_d for the vector of homogeneous
degree-d parts, allowing one component to vanish. It is nonconstant.
For positive real t tending to infinity, set

    phi_t(z)=t^(-2d) phi(tz),
    psi_t(z)=t^(-2d) psi(tz),
    phi_d(z)=|F_d(z)|^2/2.

Polynomial homogeneity gives phi_t -> phi_d in C-infinity on compact sets.
If |psi-phi|<=C globally, then |psi_t-phi_t|<=C t^(-2d) globally. Thus
psi_t -> phi_d locally uniformly and hence in distributions. Meanwhile

    H_psi_t(z)=t^(2-2d) H_psi(tz).

This positive scalar rescaling preserves the eigenvalue-ratio bound K.
Positive definiteness and that bound give the comparison inequality of
the lemma for every constant unit pair. It therefore holds for H_phi_d.

The degree-(2d-2) part of det JF is det J(F_d), which must vanish since
det JF is constant and 2d-2>0. If the two component degrees differ, one
degree-d component is zero, so the same conclusion holds directly. Thus
J(F_d) has rank at most one everywhere. Because F_d is nonconstant in
characteristic zero, its Jacobian is nonzero somewhere, and has rank
exactly one there. For example, Euler's identity applied to a nonzero
homogeneous component verifies this last assertion.

H_phi_d is one-half the Gram matrix of the derivative columns of J(F_d),
up to conjugate transpose convention, which does not change its spectrum.
At that point it has one positive and one zero eigenvalue. The weak-limit
lemma gives a contradiction. Hence condition 2 is impossible for d>1.

Conversely, if F(z)=Bz+a with det B!=0, H_phi is constant positive definite;
psi=phi satisfies condition 2. The constant-Jacobian hypothesis rules out
degree zero. This proves the equivalence.

No pointwise derivative bound for the bounded error psi-phi is used.

## Exact source interface

[Liu--Wang--Zeng, Definition 1.1](https://arxiv.org/html/2609.26810v1#S1.SS2)
requires a bounded-distance C2 strictly PSH representative with

    m rho(z)^(-2) I <= H_psi(z) <= M rho(z)^(-2) I,

where 0<m<=M are fixed. It additionally restricts the positive scale rho
by local comparability; W* also requires doubling of the representative's
Monge--Ampere measure. The displayed bounds alone imply the ratio bound
K=M/m. The proof does not require rho to be constant, bounded above, or
bounded below. For affine F, rho=1 supplies all these requirements, including
doubling of the constant Monge--Ampere density. The source's p=2 convention
uses exp(-2phi), accounting for the factor 1/2 in our potential.

The coordinator inspected the primary introduction, including Definition
1.1 and Theorem 1.2's W* hypothesis, not the complete paper's proofs. The
reviewer checked the supplied mathematical transcription, without a fresh
source fetch. No claim is made that every result elsewhere in the paper
requires W*, or that the paper's theorems or proofs are invalid. Recorded
v1 submission is September 16, 2026; appearance in the September 24 listing
is not a claimed revision. [Version record](https://arxiv.org/abs/2609.26810)

## Exact automorphism control

F(x,y)=(x+y^2,y) has determinant one and inverse (x-y^2,y). Its degree-two
part is (y^2,0), so the limiting potential is |y|^4/2, whose complex Hessian
is diag(0,2|y|^2). At (0,1), the comparison inequality would require 2<=0.
No bounded perturbation repairs the fixed-source-coordinate isotropy.

But in the global coordinates (u,v)=F(x,y), the potential is the ordinary
Gaussian (|u|^2+|v|^2)/2. Therefore exclusion in EVERY coordinate frame,
or exclusion of nonlinear automorphisms themselves, would be false.
Likewise the proof says nothing against anisotropic comparison metrics.
Using F as a global coordinate change for an arbitrary Keller map would
already assume the invertibility one wants to prove.

## Review and integration

The independent reviewer reconstructed the distributional argument,
checked its quantifiers, the unequal-degree case, rank-one point, Hessian
convention, variable rho and affine converse, and tested the triangular
automorphism. Verdict: CONFIRMED for the elementary lemma and Keller
equivalence; CONFIRMED for source mapping conditional on the supplied
definition. No producer-proof repair was required.

Binding scope clarifications: the limiting potential in the lemma is
smooth (a loose reviewer phrase saying only continuous is not adopted).
The review's remarks about subleading errors and weaker representative
regularity are outside this report. A typographical reviewer input-hash
error is not mathematical evidence; the independently checked input pins
and terminal receipt agree. Raw review material is retained unchanged.

Provenance full SHA-256:

- Frozen producer report:
  `21f42b874f3174a6797707e65c2849ca86444c74828cebf30889fd293cfee79e`.
- Independent Fable review:
  `3b60e761cbdb45273cae743e88e4ea7e9dab9c70edccc303fac32b5d3a359235`.

The proof above is self-contained; no computational certificate or numerical
test is invoked, and no external theorem is imported into its elementary
steps. This integration is not a formal proof or a novelty claim.

## Campaign consequence and excluded conclusions

The [reviewed holomorphic-domain criterion](holomorphic-domain-density-swarmHQ-root-20260918T192600Z.md)
still needs its positive actual-source density premise. Neither the
[real Sobolev core](gaussian-sobolev-cutoffs-swarmHQ-root-20260918T181400Z.md)
nor the new paper automatically supplies it. Today's initial applicability
screen found an unprovided weight-class hypothesis; the argument here
strengthens that screen to failure of the hypothesis for every nonlinear
Keller F in the chosen source coordinates. This is distinct from the earlier
[non-Keller weighted countercontrol](whole-plane-weighted-domain-swarmHQ-root-20260918T211200Z.md).

No new cutoff/control family, analytic estimate, or scientific successor is
selected. No actual Keller map is ruled out, no positive density premise is
proved, and no global closing test changes. No exhaustive history or
literature novelty claim follows from this applicability calculation.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised OPEN entries; this is not a novelty finding.
- The frozen producer report and independent review were separately scanned
  against Git basis `0434c6925ba288ffcd87fdc4052accd9d9fee554`; both returned
  EMPTY for that reason. This integration raises no additional OPEN.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8925`.
- Body SHA-256:
  `0940279d43e6d7d97c9d5517fad9507ac4a62a192bc83f27b8b043369ef69594`.
- Frozen basis: `0434c6925ba288ffcd87fdc4052accd9d9fee554`.
