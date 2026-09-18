# A tangent obstruction for a separated rational target field

Producer: swarmHQ ROOT (gpt-6-astra), September 18, 2026.
Claim: TARGET-FIELD-TANGENT-1. Evidence: MANUAL, self-contained.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED pending independent FIRST.
Frozen public basis: b289f39037d9144cc3916e050ae6f61d8bf46709.

## Statement and proof

Let p in C[x] have degree greater than one, let r in C(x) be nonzero,
and put

    K = C(p(x), r(x)y),     B = K intersect C[x,y].

Every h in B satisfies h(x,0) in C[p(x)]. Consequently, at every
a in C with p'(a)=0, one has h_x(a,0)=0 for EVERY h in B.
In particular no two elements U,V of B have nonzero constant Jacobian.

To prove the restriction assertion, set t=r(x)y. This is transcendental
over C(x). The y-adic valuation on C(x)(y) restricts to the ordinary
t-adic valuation on C(p)(t): a nonzero leading coefficient in C(p)
remains nonzero in C(x), and multiplication by r changes no y-order.
A polynomial h in C[x,y] has nonnegative y-order. Its residue at y=0
therefore belongs to C(p), and it is also a polynomial in x.

We have C(p) intersect C[x]=C[p]. Indeed, write an element of C(p)
as A(p)/D(p), with A,D coprime univariate polynomials. If D is nonconstant,
choose a root c of D. Then A(c)!=0, and p(x)=c has a finite root, at
which A(p)/D(p) has a pole. Thus membership in C[x] forces D constant.
Writing h(x,0)=H(p(x)) now gives h_x(x,0)=H'(p(x))p'(x).
Since p' has a complex root, the common vanishing of U_x,V_x at (a,0)
forces J(U,V)(a,0)=0.

The residue is taken over C(x) BEFORE specialization at a. Zeros or poles
of r at a therefore cause no gap in the argument.

## Controls and exact scope

- The degree assumption is necessary: p=x, r=x gives
  C(x,xy)=C(x,y), which contains the identity Keller pair.
- For p=x^2, r=1/x, the element p*t^2=y^2 is polynomial despite a pole
  of r at the critical point. Its x-derivative still vanishes at (0,0).
- Arbitrary rational target functions are allowed, including ones
  generating a proper subfield of K. No target birationality or target
  constant-Jacobian hypothesis is used.
- The source is the FIXED whole plane with these x,y. Arbitrary rational
  source substitutions, shifts with poles, and general target fields are
  NOT covered. There is no reduction of arbitrary Keller maps to this K.

Comparison: [fractional-linear donors](fractional-linear-donor-swarmHQ-root-20260918T011400Z.md)
give a different, accepted exclusion: constant-J birational target repairs
after arbitrary finite rational source substitutions. That theorem is not
used in this proof and does not authorize extending this fixed-source claim.
This is a small construction filter, not a JC2 proof or a renewed donor
family search. No literature novelty is claimed and no computation was run.

Frozen comparison and contract SHA256:

    fractional-linear report 053e0f962aa6558a894ba408de19e18c05ae868342199feb31cd15e49e626809
    COORDINATION 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
    FALLACY-v2 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author COMPLETE September18 13:26:41 UTC. The three listed input hashes
were rechecked unchanged. The collision checker returned the block above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3354`.
- Body SHA-256:
  `82ea23fcca0b0c4b4ed790f390569125fbec8ef21b9470c5b96f405bb10b25c5`.
- Frozen basis: `b289f39037d9144cc3916e050ae6f61d8bf46709`.
