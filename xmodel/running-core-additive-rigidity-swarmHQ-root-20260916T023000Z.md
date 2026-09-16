# The fixed running core admits no additive-group equivariance

Producer: swarmHQ ROOT (gpt-6-astra), with independent native Astra
co-research. September16,2026. MANUAL / PRODUCER-CHECKED, UNPROMOTED;
different-model review is required before promotion. JC2 remains unresolved.

## Exact statement and changed construction test

Over C, set

    P=(1+xy)^3 z+y^2(1+xy)(4+3xy),
    Q=y+3x(1+xy)^2 z+3xy^2(4+3xy),
    R=2x-3x^2 y-x^3 z,
    F=(R,Q,P): A3 -> A3.

Claim: if algebraic additive-group actions rho and tau on the source and
target satisfy F rho_a = tau_a F for every a in Ga, then BOTH actions
are trivial. Source and target actions need not coincide, be linear,
primitive, free, or have polynomial quotient kernels.

The proof rules out every algebraic Ga action preserving the actual
nonproper-value surface of F. Thus the previous one-action failure is
replaced by an all-action obstruction for this fixed map. It does not
classify other maps, stabilizations, arbitrary output projections,
nonalgebraic flows, other groups, or plane Keller maps.

## 1. Exact nonproper-value surface

Use target coordinates (r,s,t)=(R,Q,P). On x!=0 put
v=y+1/x and w=1/x. Direct substitution gives

    s=2w+4v-3rv^2,      t=v^2+vw-rv^3.

The Jacobian of (r,v,w) with respect to (x,y,z) is -x, while that of
(r,s,t) with respect to (r,v,w) is -2w. Hence det DF=2 on this dense
chart, and therefore everywhere as a polynomial identity.

Every x!=0 preimage corresponds bijectively to a simple root of

    p(V)=rV^3-2V^2+sV-2t,
    x=2/p'(v),  y=v-1/x,  z=(2-3xy-r/x)/x^2.

This is the earlier all-fiber reconstruction, with the output change
(R,T,S)=(R,-P/2,Q) and b=z. For r!=0 it gives three, one, or zero
preimages according as the cubic has three simple roots, a double and
a simple root, or a triple root. For r=0 the polynomial is genuinely
quadratic, and there is in addition exactly one x=0 preimage:
(x,y,z)=(0,s,t-4s^2). Thus r=0 is NOT an extra nonproper component.

The cubic discriminant is 4b, where

    b=s^2-rs^3-16t-27r^2t^2+18rst.

At r=0, b=s^2-16t is exactly the quadratic discriminant.
Consequently every fiber has three points off B=V(b), and fewer than
three on B. The triple-root locus is computed below.

These counts identify nonproperness, not merely branching of a chosen
polynomial. At a target with three points, the inverse function theorem
gives three disjoint local inverse neighborhoods. Shrinking the target
neighborhood, every source preimage is in one of them because the global
cardinality bound is three. The inverses take compact subsets to compact
subsets, so F is proper over that neighborhood. At a target with fewer
than three points, approach by targets outside B. If F were proper over
a neighborhood, their three preimages would stay in a compact set.
Limits land in the smaller central fiber, whereas local injectivity
allows at most one nearby preimage per central point, a contradiction.
Therefore the exact nonproper-value locus is B.

## 2. Normalization and its distinguished hyperbola

Regard b as a polynomial in t over C[r,s]. It is primitive: a common
factor of -27r^2 and 18rs-16 would divide r and also -16. Its quadratic
discriminant is 4(4-3rs)^3, nonsquare in C(r,s). Thus b is irreducible.

Define

    nu: A2_(r,v) -> B,
    (r,v) |-> (r, 4v-3rv^2, v^2-rv^3).

Substitution gives b=0, and in this parametrization

    v^2-sv+3t=0,
    (3rs-4)v=9rt-s.

The second identity gives the rational inverse on a dense open set;
the first makes v integral over C[B]. Since r is already in C[B],
C[r,v] is finite over C[B]. It is normal with the same fraction field,
so it is the entire normalization.

There are no singular points at r=0 since b_t=-16 there. For r!=0
put u=rs and zeta=r^2t. The equations b_t=b_s=0 give

    -16-54zeta+18u=0,
    2u-3u^2+18zeta=0.

Eliminating zeta gives (3u-4)^2=0, hence u=4/3 and zeta=4/27.
These values also satisfy b=b_r=0. Thus the reduced singular locus is

    C=V(rs-4/3, r^2t-4/27),

and its reduced inverse image under nu is the hyperbola

    H=V(rv-2/3) in A2.

Indeed rs=4rv-3(rv)^2=4/3 forces rv=2/3, which also yields the
second singular-locus equation. The distinguished curve in the
normalization is not an affine line or a coordinate axis.

## 3. Every additive action on B is trivial

An algebraic Ga action on an integral variety lifts to its normalization.
Here is the needed global justification. The composite Ga x A2 -> B
of normalization and action is dominant; its source is normal. By the
universal property of normalization it factors uniquely through nu.
This factor is a morphism and satisfies the action identities by uniqueness
on the dense normal locus. It is therefore an algebraic action, not just
a rational action or a formal flow. Every automorphism preserves the
singular locus, so the lift preserves the reduced curve H.

Let D be its locally nilpotent derivation on C[r,v]. In a characteristic-
zero domain, the D-degree of a product of nonzero elements is the sum
of the degrees. In particular, D(h) in hA for nonzero h implies D(h)=0:
otherwise deg_D D(h)=deg_D h-1 contradicts deg_D(hk)>=deg_D h.
Apply this to h=rv-2/3, whose principal ideal is preserved. It follows
that D(rv)=0. Factorial closure of ker D, from the same degree identity,
then gives D(r)=D(v)=0. The lifted action, and hence the action on B,
is trivial.

## 4. An ambient action cannot hide by fixing B pointwise

Suppose E is a nonzero LND on C[r,s,t] whose action preserves B.
The preceding D-degree argument gives E(b)=0. Let m be the greatest
integer such that b^m divides all three coefficients E(r),E(s),E(t),
and write E=b^m E0. Then E0 is a polynomial derivation, E0(b)=0,
and E^n(a)=b^(mn) E0^n(a) for every polynomial a. Thus E0 is also
locally nilpotent. At least one of its coefficients is nonzero
modulo b, so it induces a NONZERO LND on C[B]. Section3 excludes this.
Therefore no nontrivial algebraic Ga action on ambient A3 preserves B.

## 5. Equivariance is impossible for the fixed core

For F rho_a=tau_a F, both rho_a and tau_a are polynomial automorphisms.
They preserve properness under pre/postcomposition. Hence tau_a carries
the nonproper-value locus of F to itself. Section4 makes tau trivial.
Now every rho orbit lies in one finite fiber of F. The image of connected
Ga in a finite set is a point, so rho is also trivial. This proves the
claim and excludes the additive-quotient construction for this map without
having to find a primitive action or calculate its full kernel.

The assertion is unchanged by separate polynomial source and target
coordinate automorphisms, which transport the actions. It is NOT unchanged
by stabilization: F x id has translations in the added coordinate.

## 6. Controls and scope attacks

- A nonnormal surface alone need not be Ga-rigid: the cusp cylinder
  V(s^2-r^3) in A3 admits translation in t. Its normalization
  (v,t)->(v^2,v^3,t) has the invariant line v=0, not the above hyperbola.
- Preserving a rigid hypersurface cannot be replaced merely by fixing a
  hypersurface pointwise: E=r partial_s fixes V(r) pointwise and is a
  nonzero ambient LND. The induced nonzero action after division is why
  Section4 needs rigidity of the actual quotient ring.
- Multiplicative symmetry survives: (r,s,t)->(lambda r,s/lambda,
  t/lambda^2) scales b by lambda^-2. The normalization action
  (r,v)->(lambda r,v/lambda) preserves H. No assertion rules out Gm
  or all automorphisms, nor follows merely from H being invariant.
- No low-degree plane Keller theorem is used. This is a fixed explicit
  three-dimensional obstruction, not an arbitrary-source JC2 argument.

## 7. Priority, evidence and replay

The earlier [additive-action report](additive-quotient-descent-swarmHQ-root-20260915T232000Z.md)
excluded one specific source action. The [embedded-plane report](embedded-plane-transfer-root-20260913.md)
already supplied the whole cubic fiber reconstruction. Neither was a
theorem about every algebraic additive action.

External credit: the independent [shadybrook audit, Sections4--5](https://github.com/shadybrook/jacobian-counterexample-audit/blob/main/paper/main.md#5-failure-at-infinity-and-a-finite-completion)
already describes the nonproper surface, its normalization and the
triple-root hyperbola. Its Theorem6.2 excludes complete constant target
directions; that is not the all-algebraic-action statement here. ROOT read
these selected sections on September16, not the whole note or its programs.
The page states revised July21,2026; that date was not Git-history-verified.
The geometry is reconstructed above for proof and provenance, not claimed
as newly discovered. Targeted history/web checks found no identical
all-action result; this is not an exhaustive search or a novelty claim.

Manual replay: check the two chart formulas and Jacobians, the r=0 fiber,
the two normalization identities, all four singularity equations, the
reduced preimage of C, and each LND-degree/division argument. The controls
are exact substitutions. No scientific code, CAS, random prime, finite
degree ansatz or numerical evidence is involved. Standard normalization
and inverse-function facts are used with their hypotheses displayed.

Frozen public basis: f70043e502f4c754671309f1786640113734dcab.
Nearest local inputs, whole-read and unchanged:

- additive-quotient-descent-swarmHQ-root-20260915T232000Z.md:
  a6919a3e38f1e0c9d78b88262435164e7905284d465e4fb94bc37a690642e96e
- embedded-plane-transfer-root-20260913.md:
  dacca2ffa54c839fc4c9c0e20b55033379c3b5bd8defeffd9c58ce3a57af3709
- FALLACY-v2.md:
  e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5

No new open quantity, exit price, automatic symmetry/projection family,
general degree exclusion or JC2 conclusion. Different-model review must
attack the finite normalization, lifted action, maximal-factor argument,
exact nonproperness and the fixed-map quantifier before promotion.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised OPEN identifier. This lexical check does
  not certify mathematical novelty or correctness.

Native co-research completed02:29:26 UTC. Its whole mathematical response
and authoritative COMPLETED state were collected before closure. All five
steps were independently reconstructed and confirmed at same-model scope,
not FIRST. ROOT's mathematical authoring is complete; the final whole
readback, unchanged input pins and transaction verification follow.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10455`.
- Body SHA-256:
  `d0d854cf0c064c15446b3d2839af2b1f14c0437110120f57d5604f00fd4d3425`.
- Frozen basis: `f70043e502f4c754671309f1786640113734dcab`.
