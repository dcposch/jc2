# Relative Jacobian rank is automatic on the unequal-degree two-line locus

Date: 2026-09-06. Author: coordinator Astra. Evidence: elementary proof
and tiny exact controls. Lifecycle: PRODUCER-CHECKED; independent review owed.
No JC2 exclusion, existence result, or new source-to-chart map.

## Why this check

The completed broad sweep located Casey Atwell's *A Relative Jacobian-Rank
Filtration for Keller Maps*, Zenodo 22168498, DOI
https://doi.org/10.5281/zenodo.22168498. Its abstract defines
rho_rel(F,G) as the minimum, over complex basepoints a, of the generic rank
of J(F,G)(x,y)-J(F,G)(a), and states that a nonautomorphic plane Keller map
must have rho_rel=2. This report does NOT validate Atwell's full theorem or
use it as a premise. It tests the suggested extra necessary condition by an
independent identity. It is unnecessary to build or solve a new chart.

## Exact statement

Let k be a field of characteristic zero. Let F,G in k[x,y] satisfy
det J(F,G)=j in k*, and n=deg F>deg G=m>=1. Suppose the top homogeneous
form F_n has no nonzero constant directional derivative that vanishes
identically: for every (v_x,v_y) != (0,0),
v_x partial_x F_n+v_y partial_y F_n != 0. This hypothesis may equivalently
be imposed after passing to the algebraic closure.

Then for EVERY geometric basepoint a,

    deg det(J(F,G)(x,y)-J(F,G)(a)) = n-1.

In particular this determinant is not the zero polynomial, the generic
rank is 2 at every a, and rho_rel(F,G)=2.

The hypothesis holds whenever F_n is a product of powers of two distinct
linear forms, with both exponents positive. It therefore holds in the
normalized two-line unequal-degree setting used by the campaign, including
the exact physical tops y^27(y-x)^72 and y^24(y-x)^84 of the full-direct
clients. This statement is conditional on an actual Keller pair; necessary
numerical rows are not thereby realized or excluded.

## Proof

Write J(F,G)(a)=[[A,B],[C,D]]. Its determinant is j, so (C,D) != (0,0).
Expansion of the two-by-two determinant gives the polynomial identity

    det(J(x,y)-J(a))
      = 2j - D F_x + C F_y + B G_x - A G_y.

Because n>m, the last two terms have degree at most m-1<n-1. Because
n>=2, the constant term also has lower degree. The homogeneous part of
degree n-1 is therefore exactly

    -D partial_x F_n + C partial_y F_n.

The direction (-D,C) is nonzero, so this is nonzero by hypothesis.
Everything else has smaller degree. This proves the claimed exact degree
and hence the generic rank, uniformly in a.

For the two-line hypothesis, make an invertible linear change of coordinates
and write F_n=c y^p(y-x)^q, c!=0, p,q>0. Its derivative in direction
(v_x,v_y), after removing the nonzero factor c y^(p-1)(y-x)^(q-1), is

    p v_y (y-x) + q (v_y-v_x)y.

If zero, its x coefficient gives p v_y=0, so v_y=0; its y coefficient
then gives q v_x=0, so v_x=0. Characteristic zero is used here. More
generally a homogeneous binary form in characteristic zero has a constant
null direction exactly when it is a scalar multiple of a power of one
linear form: straighten that direction to partial_x and differentiate.
Thus any top form with at least two distinct linear factors also suffices.

## Scope and negative controls

The nonlinear automorphism (F,G)=(y+x^2,x), with j=-1, has top F_2=x^2.
At a=(a_x,a_y), the Jacobian difference is

    [[2(x-a_x),0],[0,0]],

so its generic rank is 1 for every a. An affine automorphism has relative
rank 0. These refute the stronger statement that all Keller maps have
relative rank 2 and isolate the load-bearing top-form hypothesis.

No conclusion is drawn here when n=m, when the Jacobian is not a nonzero
constant, or in positive characteristic. In particular one must not apply
the degree calculation to an arbitrary point of an incomplete necessary
chart: the determinant polarization identity still holds there, but the
term det J(x,y) is no longer the scalar j and can have higher degree.

The arithmetic census can only use conditions that all genuine realizing
pairs must meet. For every genuine pair in this normalized two-line setting,
the relative-rank requirement is already automatic before consulting its
characteristic exponents. It cannot exclude one of the 64 finite-window
rows on that basis. This does not say that Atwell's result is false, useless
in other loci, or that all conceivable refinements of matrix variation are
exhausted. It closes precisely the proposed extra rho_rel<=1 test here.

## Reproduction

`box/relative-rank-vacuity-20260906/check.py` checks the unrestricted
two-by-two determinant polarization, the two-line derivative with exponent
pairs (1,1),(2,3),(27,72),(24,84), the constant-direction coefficient
determinant -pq, and both automorphism controls. It writes only stdout and
uses explicit exceptions rather than Python assertions. Run:

    python3 box/relative-rank-vacuity-20260906/check.py
    python3 -O box/relative-rank-vacuity-20260906/check.py
    python3 -OO box/relative-rank-vacuity-20260906/check.py

This finite check is a transcription control, not a substitute for the
uniform proof above. No AWS, heavy CAS, random search, or new source artifact
is needed. The parent sweep is discovery provenance only, not a proof input.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5245`.
- Body SHA-256:
  `b2a3c3f901c1a926090a6954a5daf4716ac2a633b97b42bfcd8f8607cfa7b353`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
