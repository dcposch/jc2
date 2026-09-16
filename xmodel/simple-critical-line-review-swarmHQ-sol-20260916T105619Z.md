# Hostile review: simple critical line and its F10 attachment

Reviewer: native gpt-5.6-sol, task torus_quotient_sol_review.
Recorder: swarmHQ ROOT (gpt-6-astra).
Review terminal: 2026-09-16 10:56:19 UTC; independently collected COMPLETED.
Basis: 356a997eab52cceaeea9b68d85b40c2ab2f4c886.
Evidence tier: MANUAL hostile review, named classical inputs retained.
Lifecycle: completed review. This is ROOT's faithful intake of the
reviewer's terminal messages, not a verbatim transcript or Sol-authored file.

## Frozen input and verdict

[Producer](simple-critical-line-f10-swarmHQ-root-20260916T105500Z.md):
full SHA256 384d64ee500f6165f93d2017ba766c940881da02e07ec7cd300be66942168fa5;
body cd6c5a0d0761db43f5c07481b7085a26b19e50df730d54960d5913bcdb66d975;
manifest 17670fef4587a52d07bf28d03c659236ef43dbb6bc2aadaae51255bd0b6db1cf.
Report and manifest modes0444, administrative verification successful,
pre/post hashes unchanged. ROOT independently reverified after collection.

C1--C4 are CONFIRMED at their exact scopes. No computational certificate
or literature novelty was asserted. The producer's standard normalization,
Luroth and projective-completion inputs are retained.

## C1: birational normalization — CONFIRMED

The constant and linear g coefficients are exactly
b*A'-a'*B=0 and b*B'-b'*B+2*d*A'-2*D*a'=c.
At a critical parameter, a'=A'=0 and (b,B) cannot both vanish.
Choose b!=0; lambda=B/b=A'/a' and lambda'=c/b^2!=0 there.
A ramified normalization parameter would make every regular function
of that parameter have zero p derivative. The meromorphic lambda
has no pole on the normalization because its pullback B/b is regular,
giving the contradiction. Immersive points cannot ramify either.

The lift is finite because a nonconstant coordinate makes p integral.
Luroth gives rational normalization. In the projective extension all
preimages of omitted target points must lie at the sole source point
at infinity; there is at most one omitted point and at least one
because the normalization is affine. It is therefore A1. An everywhere
unramified polynomial A1->A1 has constant nonzero derivative and degree1.

## C2: singular branch orders — CONFIRMED

At an intrinsically singular branch, regular lambda makes ord A>=ord a=m.
Here m>=2, lambda-lambda(0) has order1, and
(A-lambda(0)*a)'=a'*(lambda-lambda(0)) has order m.
The tangent-subtracted coordinate has order m+1. The producer correctly
excludes a smooth branch passing through a multibranch singular point
from this singular-branch conclusion.

## C3: the specified valuation — CONFIRMED

For a transverse target equation h, write h(P,Q)=g^e*w.
A target along-curve parameter v has nonzero p derivative generically.
The Jacobian of this pulled-back pair has g-order e-1, while the
chain rule gives order1. Thus e=2; C1 gives residue degree1.
This concerns the g=0 divisor only, not every omitted divisor.

## C4: literal F10 client — CONFIRMED conditionally

The reviewer checked the compact contract hash
6c6fe089033832c9d33639f8438a43c3dbfd8a28d06e05ef76ee141438de6d7f
and read its sections1--4. Full inverse polynomiality and the chain
orientation supply ordinary A,B and J=c*g.
On g=0, z=d=p^2+ell*p-u, R has degree7 and leading coefficient1,
and t has rational degree-2. Every monomial satisfies
7i-2k<=7e-(7r+2)k. The sole monic R^e term supplies degree7e
for e=m,n, so the restriction is nonconstant.
At fixed p, U=g^2*(1+gp) tends to0 and V=g^-1 tends to infinity
as g tends to0, proving the claimed image values are nonproper.

No whole-nonproper-set classification, unique-dicritical assertion,
new trace inequality, F10 solution/exclusion or JC2 result follows.

## Controls and read scope

Direct differentiation checked both controls:
(g+p^m, gp+m*p^(m+1)/(m+1)) has J=g and cusp orders(m,m+1);
(g,gp) has J=g but contracts the critical line. Higher Jacobian
multiplicity removes the nonzero right side of the linear coefficient;
the report correctly does not claim a counterexample to every weaker
birationality statement.

Whole producer and manifest, selected exact contract sections1--4,
and current governing scope were read. Desk-only: no network, scientific
execution, worker, paid launcher, descendant or file writing by the reviewer.
No remaining GAP within C1--C4 was reported. ROOT's integration preserves
the separate one-dicritical and global transport gaps.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4518`.
- Body SHA-256:
  `8fa045e3146e7eda47e45a0380a99e64cda784620b088571b14b9e97c4e935c6`.
- Frozen basis: `356a997eab52cceaeea9b68d85b40c2ab2f4c886`.
