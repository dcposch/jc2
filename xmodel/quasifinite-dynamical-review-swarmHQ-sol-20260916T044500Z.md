# Different-model review: finite fibers and dynamical minimization

Reviewer: swarmHQ gpt-5.6-sol, native task torus_quotient_sol_review.
Recorder: ROOT, recording the terminal mathematical review and final verdict;
this is not a verbatim log or a Sol-authored file.
Evidence: MANUAL hostile proof review, with classical Jung generation import.
Verdict: CONFIRMED, A-E. Mathematical completion: 2026-09-16T04:43:17Z.
Reviewed contribution: 3fbf3ba0b43fa3ca153a7466d099d6cf96ea5d3b.

## Frozen scope and custody

The [producer report](quasifinite-dynamical-minimum-swarmHQ-root-20260916T043600Z.md)
was complete and sealed before review. Sol read it wholly, checked finalizer
verification, the charged pins and 0444 modes, and unchanged public HEAD.
ROOT collected the full mathematical message and final verdict and observed
authoritative COMPLETED before recording this review.

- Producer full SHA256: 0005828cec9ecf9800754beccd2d39825841afb51f3b6def019f286155e1cd9b.
- Producer body SHA256: 8fe99c990d7b67b1f96fbdf0bfccf5c0924ea300c9388365cbd3d71e960e92a7.
- Producer manifest SHA256: 211b30d60d5647931cba0724fcb134c9c5554cff098b37522cc76a07bb9e9d60.
- Producer embedded basis: 938c328ac4c95b4983e8bdd3072dfdbed5053feb.
- FALLACY-v2 SHA256: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

## A. Finite fibers, degree and non-Keller status — CONFIRMED

For F=(x+x^2*y,y+x*y), off x=-1 the fiber over(s,t) is given by

    y=t/(1+x), (1+t)x^2+(1-s)x-s=0.

The quadratic cannot vanish identically. On x=-1, a unique point exists
only when t=0; it replaces the excluded root of(x+1)(x-s). Every fiber
therefore has at most two points. For generic(s,t), the discriminant is
nonzero and two valid roots give generic degree2. The omitted value(1,-1)
shows that quasi-finiteness is not finiteness. The Jacobian
1+x+(2x+x^2)y vanishes at(-1,0); the map is explicitly NON-KELLER.

## B. Uniform automorphism cone lemma — CONFIRMED

Jung generation and a shortest alternating affine/triangular word, with
the two GL2 Bruhat cells, give arbitrary affine ends and factors

    H_i(U,V)=(b_i V+c_i, a_i U+R_i(V)), deg R_i>=2.

For weights q<p<2q, the first R_i(A_2) strictly outweighs A_1. Its two
output leaders are powers of one variable T, selected by the second
affine coordinate. Subsequent factors change an unequal exponent pair
(r,s), s>r, to(s,m_i*s). At the final invertible affine factor, the larger
term can be suppressed in at most one output; that output still has the
smaller power of the same variable. There is no equal-weight cancellation.
This covers arbitrary automorphism length and degree, not a finite scan.

The named classical import is Jung generation. ROOT checked its statement
and reduced affine/triangular expressions in selected pages1 and4 of the
Furter author manuscript linked in the producer report. Sol accepted this
named standard import and checked the supplied Bruhat/weight argument;
Sol did not freshly audit that primary source or the original Jung proof.

## C. Corner iteration — CONFIRMED

The unique leaders of F are x^2*y and x*y. For every positive source
weight(s,t), their weights p=2s+t,q=s+t satisfy q<p<2q. Thus the cone
leaders become true coordinatewise greatest monomials after substitution.
Their exponent matrices multiply exactly under iteration: decreasing an
outer exponent strictly decreases its substituted weight, and the unique
product of inner leaders has nonzero coefficient. This works also for
rank-one matrices and proves the claimed ordinary degree growth.

For nonaffine left changes the matrices are

    [[2a,a],[2b,b]], spectral radius2a+b>=4;
    [[a,a],[b,b]], spectral radius a+b>=3,

where a,b>=1 and max(a,b)>=2. In the rank-one cases the identity
M^n=(w^T*v)^(n-1)*M gives the same rates directly. There is no unstated
algebraic-stability assumption or cancellation deferred to large n.

## D. Exact two-sided minimum — CONFIRMED

The conjugacy identity beta(alpha F beta)beta^-1=(beta alpha)F reduces
the two-sided value set to the left-composition value set. Fixed polynomial
conjugacy changes iterate degrees by at most constant factors. The same
reduction works for determinant-one automorphisms.

Affine left changes have exactly the corner-row types(P,Q),(Q,P),(P,P),
with respective dynamical degrees(3+sqrt(5))/2, 1+sqrt(2), and3.
Two Q rows contradict invertibility of the affine linear part. Nonaffine
changes have the lower bounds above. The signed swap(U,V)->(V,-U) has
determinant1 and attains1+sqrt(2). Thus

    min_{alpha,beta in Aut(A2)} lambda1(alpha F beta)=1+sqrt(2)>2,

and the identical minimum holds on the determinant-one subgroup.

## E. Exact excluded inference — CONFIRMED

Finite fibers alone do not imply that the coordinate-minimized dynamical
degree is at most generic mapping degree. This strengthens the earlier
non-Keller control's scope by removing its contracted curves, not by
supplying any Keller hypothesis. It gives no Keller counterexample,
refutation of a Keller-specific lowering theorem, or proof of JC2.
No literature novelty is certified. No error or mathematical GAP was found
in A-E at the named-import scope. No successor or control family was tested.

The review used no files of its own, scientific subprocesses, CAS, AWS,
paid external launcher, or dependent research. Integrity checks establish
custody, not mathematical correctness in place of the proof.

## OPENS RAISED

None. The existing Keller-specific gap is unchanged.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

This lexical check is not a mathematical novelty certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5665`.
- Body SHA-256:
  `67751537d08f59506cd163eb0d3f17f545805fc1425b02396dd90146d1faf03b`.
- Frozen basis: `3fbf3ba0b43fa3ca153a7466d099d6cf96ea5d3b`.
