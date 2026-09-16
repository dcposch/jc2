# Hostile review: affine binary-form plane sources

Reviewer: gpt-5.6-sol, independent of the gpt-6-astra producers.
Recorder: swarmHQ ROOT (gpt-6-astra), faithful synthesis of the reviewer's
terminal messages, not a verbatim transcript or a Sol-authored file.
Date: September 16, 2026 UTC.
Frozen contribution: a431916d036f2aeab6e12502725258ea466fcec1.
Evidence: MANUAL hostile mathematical review with the producer's named imports.
Verdict: CONFIRMED A--G, including the exact all-degree statement as written.

## Frozen inputs and custody

[Producer report](binary-form-affine-plane-obstruction-swarmHQ-root-20260916T053400Z.md):

- Body SHA256: f5f7b9413aa62ce5fe74d1e11ed0a9b9f0df32fec93effe1382fd65717978613.
- Full SHA256: 862d220b14eaff712e7c5e92a98d02231dd86ce013d4c1208a0df80666f216e6.
- Manifest SHA256: f8b692619d6f2ba81ef0826681f4235b64a3c1ebaa8c82f92ec9fece144a9ba9.
- Original scientific basis: 5e9791860e1515640a494cd271f0c1bc3f454f45.
- FALLACY-v2 SHA256: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

The reviewer read the entire sealed contribution after artifact verification.
Report and manifest modes0444, full/body/manifest pins, governing inputs,
and contribution HEAD matched before and after. Review was message-only.
No file edits, external network requests or executable scientific computations occurred.
This is not computational verification or a new audit of the named external
nonproperness theorem. ROOT had checked that theorem's selected primary text.

## Exact reviewed conclusion

For positive unequal factor degrees j,k and ANY affine two-plane
F0+pU+qV of degree-(j+k) binary forms over C, every entire-A2 irreducible
component of the ORIGINAL source

    LQ=F0+pU+qV, Res(L,Q)=1

maps isomorphically to the parameter plane. Generic-degree>1 Keller maps
cannot arise from these component identifications. Arbitrary source maps
into this space, nonlinear parameter surfaces, equal degrees and general
JC2 are excluded from the statement.

## A. Etaleness of the actual source — CONFIRMED

Coprimality makes the multiplication differential onto, with precisely
the scaling kernel (cL,-cQ). The resultant differential on that kernel
is (k-j)c, so the combined differential is an isomorphism. Smooth
irreducible components are disjoint and open; etaleness makes every
component's image a nonempty open subset of the parameter plane.
Thus each component is dominant, without an assumed normalization map.

## B. Planes through zero — CONFIRMED

The given Gm action preserves product and resultant and every component.
For a prime ell>j+k, its subgroup mu_ell acts freely on the nonzero L
vector. The finite etale quotient has covering degree ell, forcing
chi_c(Z) to be divisible by ell. This contradicts chi_c(A2)=1.
No unproved assertion that a disconnected residual scaling cover is
connected, and no projective torus-localization hypothesis, is used.

## C. Fixed gcd and reduced degrees — CONFIRMED

Each fixed root and its entire fixed multiplicity lie in one coprime
factor. The disjoint closed alternatives give a constant allocation
on an irreducible component. Division by the resulting constant forms
is linear on coefficients and preserves the source ring. Independence
of u,v recovers p,q from the reduced product.

If one reduced degree is zero, its factor is a nonzero unit on A2,
hence constant. The source ring is then C[p,q], proving degree1.
Reduced equal degrees cause no problem: only the ORIGINAL j!=k is
used for etaleness and the finite normalization-scaling cover.

## D. Common-zero directions — CONFIRMED

At a common zero xi of u,v, the reduced f0 is nonzero. Evaluations
A(xi),B(xi) are units and so constants on a putative A2 component.
Choosing xi as infinity makes the factors have constant leading
coefficients. Their monic versions divide a monic polynomial over
C[p,q]; all factor coefficients are integral. Ring generation then
gives finiteness. Connected finite etale covers of complex A2 have
degree1, so the map is an isomorphism.

## E. Polynomial parametrization of the dual — CONFIRMED AS WRITTEN

Polynomial parametrization of the nonlinear dual curve can be placed
in degrees m>r>=1 by linear combinations of p,q. The tangent vector
[q':-p':p'q-q'p] has last degree m+r-1 with nonzero leading coefficient,
so its projective limit at infinity is O=[0:0:1]. Biduality puts O on
the original coefficient curve, contrary to basepoint-free u,v.
No birational-parametrization assumption is hidden here.

The initial review flagged the report's use of AFFINE coordinate
changes as supposedly failing to fix O. ROOT requested a bounded
clarification using the explicit dual-to-primal map. For dual
coordinates h'=M h, with M=[[A,b],[0,1]], primal points transform by
M^(-T), which fixes e3. For p'=p+a,q'=q+b the primal change is

    [X:Y:Z] -> [X:Y:Z-aX-bY],

which fixes O. The reviewer explicitly WITHDREW the flag: it had
mistakenly applied a dual translation directly to primal coordinates.
The frozen report requires no correction. This records the objection
and its mathematical resolution rather than silently erasing it.

## F. Nonproperness for each component — CONFIRMED

For composite phi of degree e, generic main-dual tangency produces e
disjoint root transpositions. Ordered root pairs in different blocks
have irreducible incidence: Delta!=0 solves uniquely for p,q, while
Delta=0 gives inconsistency when their C-images differ. After restricting
to the good parameter open this incidence stays irreducible and dominant.
Root monodromy is therefore transitive on ordered off-block pairs.

The normal closure of tangency inertia is transitive on roots. Hence
no proper nonempty subset is fixed by every conjugate, and each partition
orbit contains a sheet moved by the fixed inertia. Every enhanced
residual-scaling orbit projects onto the full partition orbit, so this
argument applies to EACH original source component, not just their union.

A moved partition splits a colliding pair. Bounded original factors
would limit to nonzero factors sharing that root, contradicting their
constant resultant1. Thus every component escapes over a dense open
part of the main dual curve D. The map is finite etale over the good
open, so its nonproperness set is contained in the complementary curves.
Consequently D is a nonproperness COMPONENT. Fixed-root allocations and
extra removed lines do not invalidate this inference. The named
polynomial-uniruledness theorem for an A2 source now contradicts E.

## G. Controls and exclusions — CONFIRMED

The displayed degree-one A2 component checks the need to allow trivial
maps. The cubic discriminant separates the main dual component from
an extra branch-image line. The residual-scaling warning correctly
rejects a whole-union Euler shortcut. For j=k the key differential
and finite-scaling argument fail, as the report explicitly excludes.
Polynomial, not merely rational, parametrizability is essential.
No arbitrary Keller-source presentation or JC2 conclusion is asserted.

## Review completion and scope

Measured startup: 05:35:53 UTC. Main review terminal: 05:36:59 UTC.
Coordinate-map clarification terminal: 05:38:03 UTC. Pins unchanged
again at clarification. Final verdict is unqualified CONFIRMED A--G
at the precise stated scope, using the named classical imports.
No descendant investigation or additional theorem is part of this review.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7562`.
- Body SHA-256:
  `ff03ed086878fde888b673391eb6ee03061dd843907b2e3d4f8de2d9042f2475`.
- Frozen basis: `a431916d036f2aeab6e12502725258ea466fcec1`.
