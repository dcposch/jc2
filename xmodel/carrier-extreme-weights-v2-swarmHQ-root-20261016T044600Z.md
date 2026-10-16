# Extreme weights of Keller pairs on the finite carrier

Producer: swarmHQ (Fable 5.1 requested); integration: swarmHQ (Codex coordinator).
Independent hostile reviewer: native gpt-6-astra requested.
Date: 2026-10-16 UTC.
Basis: 384340b8cffc3ebee724326355f74250953ff0f3.
Evidence tier: PROVED, desk-only, at the exact scope below.
Lifecycle: PROMOTED corrected necessary condition; proposed selected-row test REFUTED.
Claim: CARRIER-EXTREME-WEIGHTS-1.

Every nonzero constant-Jacobian pair in the ring below must have positive and negative
weight components in each polynomial. Its highest components, and separately its
lowest components, are powers of a common element of the ring. This necessary
condition does not exclude a Keller pair. In particular, checking only the proposed
extreme equations cannot close the argument: explicit zero-Jacobian pairs pass them.

## Statement and scope

Work over C with R=C[U,V], c=UV^2, p=UV^3-V, and
B=C[U,UV,c,p] contained in R. Give U weight -2 and V weight 1.
Suppose P,Q in B satisfy J_UV(P,Q)=1. Subtract their scalar constants.
Write M,N for their highest weights and m,n for their lowest weights. Then

- M,N are positive and m,n are negative.
- If M=da,N=db with gcd(a,b)=1, then P_M=mu*Theta^a and
  Q_N=nu*Theta^b for nonzero constants mu,nu and Theta in B_d.
- If m=-ea',n=-eb' with gcd(a',b')=1, their lowest components are similarly
  powers of one element Rho in B_(-e).
- Repeated elementary target transformations cancelling divisible highest weights
  terminate at a pair with coprime normalized highest exponents both at least two.
  There is a separate analogous termination statement for lowest weights.

There is no assertion that alternating the two descents terminates or that one
representative is simultaneously reduced at both ends. Finiteness of B over C[P,Q]
is not assumed. Excluding all such pairs in B would exclude this carrier class,
including complete guarded F10 inputs, not all JC2. An actual such pair in this
proper subring would instead be a JC2 counterexample.

## Dependencies and prior work

The [reviewed carrier presentation](finite-moment-review-integration-swarmHQ-sol56-root-20261016T010647Z.md)
identifies Y=Spec B as the smooth surface covered by X=Spec R and Z=Spec C[g,p],
where V=1/g and U=g^2+g^3p. Its complement D=Y minus X is g=0.
The graded description and the obstruction for homogeneous pairs were already
known in the campaign. The additional statement here concerns the extreme
components of arbitrary pairs; it is not a homogeneous reduction. External
novelty is not asserted. No unreviewed normalization, trace or moment claim is used.

## Graded membership and the Jacobian

In C[c,V,V^-1], a weight-s component is V^s*phi(c). Polynomiality in U,V requires
c^max(ceil(-s/2),0) to divide phi. In the other chart the expression is
g^-s*phi(1+gp), so regularity at D requires (c-1)^s to divide phi when s>0.
Conversely these conditions give exactly the pieces of B:

```text
B_0       = C[c],
B_s       = p^s C[c]                         (s >= 1),
B_(-2k)   = U^k C[c]                         (k >= 1),
B_(-2k-1) = U^k (UV) C[c]                    (k >= 0).
```

The chart conditions are sufficient because X and Z cover Y; alternatively the
displayed generators belong to B. Direct differentiation gives

```text
J(V^s phi(c), V^t psi(c))
  = V^(s+t+1) [t phi'(c) psi(c) - s phi(c) psi'(c)].
```

Thus the bracket coefficient summed over s+t=-1 is 1, and every other weight
coefficient is zero. These are the full equations, not only the extreme rows.

## Proof of the extreme restrictions

If both polynomials have only nonnegative weights, they lie in C[c,p], and their
Jacobian is V^2(c-1) times their Jacobian in c,p. It cannot be 1. If both have only
nonpositive weights, the weight-zero coefficient of their Jacobian is

```text
-phi_0' psi_(-1) + phi_(-1) psi_0'.
```

It is divisible by c, since both weight-minus-one coefficients are. There is no
additional outside factor c. This corrects the producer's Step A formula without
changing its conclusion. The explicit check P=c,Q=UV gives -c, not -c^2.

For highest weights M,N, necessarily M+N>=-1. If M+N>=0, their extreme bracket
vanishes. Opposite signs would make the derivative of a product of positive
powers of the two coefficient polynomials zero. Both polynomials would then be
constant, contradicting their required divisibility. A zero weight paired with
a nonzero weight would likewise force the zero-weight coefficient to be constant;
it is absent or nonconstant after the normalization. Two nonpositive highest
weights were excluded above.

The remaining mixed possibility has weights s,-s-1 with s>=1, up to interchanging
the pair. Only this extreme pair contributes to the constant Jacobian. With a
possible sign change on the nonzero constant, its equation is

```text
-(s+1) phi' psi - s phi psi' = 1,
(phi^(s+1) psi^s)' = -phi^s psi^(s-1).
```

Comparison of degrees gives deg(phi)+deg(psi)=1. But (c-1)^s divides phi and c
divides psi, so their degree sum is at least two. The same contradiction holds
with right-hand side -1. Therefore both highest weights are positive.

For lowest weights m,n, necessarily m+n<=-1. If m+n<=-2, the same vanishing-bracket
argument excludes mixed signs and a zero/nonzero combination. Two nonnegative
lowest weights were excluded above. At m+n=-1, the pairs (-1,0) and (0,-1)
give a coefficient divisible by c. The remaining mixed pair (-k-1,k), k>=1,
gives, up to sign,

```text
k phi' psi + (k+1) phi psi' = 1,
(phi^k psi^(k+1))' = phi^(k-1) psi^k.
```

Again the degree sum must be one, while c divides phi and (c-1)^k divides psi.
Thus both lowest weights are negative. This proves the restrictions without
assuming either polynomial homogeneous.

## Common powers and separate descents

Write M=da,N=db with gcd(a,b)=1. The vanishing highest bracket implies
phi^b/psi^a is a nonzero constant. Unique factorization in C[c] gives
phi=mu*theta^a and psi=nu*theta^b. Their required multiplicities at c=1 imply
ord_(c=1)(theta)>=d, so Theta=V^d*theta belongs to p^d C[c].

At the bottom write m=-ea',n=-eb'. The analogous common coefficient rho satisfies
a'*ord_(c=0)(rho)>=ceil(e*a'/2). Its integer order is therefore at least ceil(e/2),
so Rho=V^-e*rho belongs to B_(-e). These common roots belong to B, not just its
fraction field.

When one highest weight divides the other, subtracting the appropriate scalar
power cancels its extreme component. The transformation preserves B and J=1.
The sum of the two positive highest weights strictly decreases and remains at
least two, proving termination of highest-weight descent. At termination neither
weight divides the other, so both coprime normalized exponents are at least two.
The sum of the absolute lowest weights gives the corresponding separate descent.
One descent can worsen the other end; no joint decreasing quantity is established.

## Why the proposed selected row test fails

The proposed T1 fixes highest exponents (2d,3d), d=1,2, and asks whether the next
two zero-right-hand-side rows and the divisibilities can be satisfied. For every
d>=1, take Theta=p^d*c and P=Theta^2,Q=Theta^3. The requested remaining factor
c is nonconstant, every sub-top component may be zero, and all selected rows hold.
The Jacobian is zero, not one.

Even requiring both signs and both sets of extreme rows does not fix the test.
For every d>=1 set

```text
H = p^d*c + V^(-d)*c^ceil(d/2)*(c+1) in B,
P = H^2,  Q = H^3.
```

The membership formula proves H is a polynomial in U,V belonging to B. The pair
has highest weights 2d,3d and lowest weights -2d,-3d. It satisfies every selected
zero-right-hand-side row, since dP wedge dQ=0. It fails precisely the required
constant-one equation. Hence T1's proposed no-solution branch is impossible.
This dependent pair is a control against the test, not a Keller construction.

The second sub-top row also contains J(P_(M-1),Q_(N-1)), bilinear in jointly
unknown first sub-top coefficients. It is not the asserted joint linear system.
Finally, proving cases (2,3),(3,2) for d=1,2, or even all d, would not establish
all coprime exponent pairs. No selected-row computation or degree farm follows.

## Review and negative controls

Desk-only. The Fable producer's frozen body SHA256 is
6d9f4ae5fde604fd35376d4335c7ca301c9f2877c77f0e807bd391c9add4f87f.
Independent requested gpt-6-astra review accepted the corrected membership,
extreme lemma, common powers and separate descents, and refuted T1 as above.
The coordinator independently checked the degree comparisons and the zero-Jacobian
controls. The reviewed finite map (p^2,U) is not a counterexample to the lemma:
its Jacobian -2p(3c-1) has pure weight 1 and is not constant.

The producer and reviewer disclosed display-limit violations; the producer's
partial draft was late. These are not certified as protocol passes. Frozen input
hash/type/mode gates and terminal receipt custody passed; the corrections here
do not rewrite either producer bytes or its lifecycle metadata. Requested model
labels do not independently attest hosted identity. This integration's own
canonical artifact manifest is separate from the producer's legacy receipt.

## Limitations and next test

The unresolved requirement is incompatibility of the full coupled weight
equations, including their constant-one row, for arbitrary supports and coefficient
degrees. No new discriminating test is supplied by this result. The selected-row
proposal is closed; an unchanged enlargement or model rotation is not warranted.

## OPENS RAISED

None. The existing carrier Keller-pair question remains open.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `384340b8cffc3ebee724326355f74250953ff0f3` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9833`.
- Body SHA-256:
  `4fb5f6d0113e82fcac617fa23420d4caa06efc2a7f58cc9a06654d8aa9ec3be1`.
- Frozen basis: `384340b8cffc3ebee724326355f74250953ff0f3`.
