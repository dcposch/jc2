# Independent FIRST: SNC shifted-order coprimality

Producer: swarmHQ ROOT. Independent reviewer: retained native Sol5.6-assigned
lane affine_radial_first_sol56_2157; actual hosted model identity unverified.
Reviewer terminal: 2026-10-19 11:24:38 UTC, CONFIRMED at exact stated scope.
ROOT transcription/integration of the received review, not a second independent
review. Evidence: PROMOTED / MANUAL with standard surface imports; novelty UNKNOWN.
Public basis: 15a80a4b9443bc52d7daa4e84ff79086c279fd97.

[Sealed producer](snc-order-coprimality-swarmHQ-root-20261019T111803Z.md)
remains byte-identical, including its historical provisional label. Its later
promotion is recorded here and in AUDIT.md, not by rewriting sealed evidence.

## Statement confirmed

Let S be a smooth projective complex surface, C(S)=C(u,v), and
omega=c du wedge dv with c a nonzero complex constant. At a simple-normal-
crossing point of div(omega) with exactly two components of orders a,b,

    gcd(a+1,b+1)=1.

The gcd is nonnegative and uses absolute values; gcd(0,0)=0. Orders may be
negative. In particular two simple zero curves cannot meet transversely with
no further support component. This is necessary, not a general converse.

## Independent proof audit

Label each boundary curve by lambda=ord(omega)+1. Include EVERY exceptional
curve, including order-zero curves. A blowup at a smooth point of one boundary
component creates label lambda+1 and a primitive edge. At an edge with labels
lambda1,lambda2 it creates lambda1+lambda2; both resulting edges retain the
old gcd, also for negative or zero labels. An off-boundary blowup creates an
isolated label2 component. Its first subsequent edge, if any, is (2,3).
Starting with the infinity line of P2, label -2 and no edges, every edge in
the augmented boundary of any point-blowup model is therefore primitive.

Take a common smooth projective resolution of S and P2, factoring the two
birational morphisms into point blowups. On the S side, strict transforms of
the original crossing remain connected by the chain obtained by successive
edge subdivisions. Blowups elsewhere add branches or do not affect this
chain; none deletes it. Every chain edge retains d=gcd(a+1,b+1).

Both endpoints have nonzero form order. If an intermediate curve has order0,
its label1 immediately forces d=1. Otherwise every chain vertex has nonzero
order and belongs to the P2 augmented boundary: a nonexceptional such curve
can only dominate the infinity line, and every exceptional curve was included.
The actual chain edges are consequently edges of that SNC boundary and have
gcd1. Crucially, a curve exceptional over S was NOT assumed exceptional over
P2; the order-zero alternative explicitly closes that possible gap.

Imports: standard common resolution and point-blowup factorization for smooth
projective surfaces in characteristic zero, as in the earlier positive-cycle
criterion. No new external theorem retrieval or whole-source audit is asserted.

## Checks and consequences

The monomial check is correct. If gcd(m+1,n+1)=1, choose integers r,s with
r(n+1)-s(m+1)=1. Then u=x^r y^s and v=x^(m+1-r)y^(n+1-s) have exponent
determinant1, generate C(x,y), and du wedge dv=x^m y^n dx wedge dy. This
sufficiency concerns only the monomial model, not a general unit factor.

For a finite dominant map pi:X->Y of normal complex surfaces, at smooth
x,y=pi(x) with eta regular/nonvanishing near y, the characteristic-zero
ramification formula gives ord_E(pi*eta)=e_E-1. Thus, if exactly two
ramification components meet transversely at x, rational Darboux coordinates
GENERATING C(X) for pi*eta force gcd(e1,e2)=1.

For the actual finite normalization of a Keller map, C(X)=C(x,y) is the
original source field and the Keller identity supplies those Darboux
coordinates for pi*(dP wedge dQ). The conclusion therefore applies at its
smooth two-component SNC points. It does not automatically apply at singular
or non-SNC points, or survive replacing C(X) by a larger finite source field.
Most importantly, no such forbidden crossing is proved to exist.

The positive-cycle obstruction instead uses several branches of ONE global
positive-order curve and allows tangencies; neither criterion subsumes the
other at the displayed hypotheses. No ruling/basepoint theorem, arbitrary
donor regularization, global B=R argument, JC2 proof or counterexample follows.

## Review custody

ACK 11:23:32; substantive partial 11:24:27; terminal 11:24:38 UTC.
Reviewer reports whole sealed prompt1--72; newly read frozen STATE1--309 and
APPROACHES1--949; only own exact-pin whole-read reuse for unchanged governing
inputs; producer1--93 and manifest whole; artifact verifier passed. No missing
charged scope. Postpins matched. No searches, source calls, CAS, file/Git writes,
model CLI, paid adapters, descendants or protected-tree access were reported.

Producer: 4931 bytes, mode0444, SHA256
3ba0c5ffffb1530a34a2b6e61c1f185f3e477d9dff57d1942a76490013dfce5c.
Manifest: 690 bytes, mode0444, SHA256
0c875cf60cfd5d41b8020019653698f15a062355f3ba131dbd6df9f1d8d64714.
Frozen review STATE basis: 1b9c3fd15d3fc3ed6c563aaf9321a0d19e4afe9e;
STATE SHA256 dfe8ccf691b91f12c10d94824bb57d4ab1de7d12ef9e42d807954993bf3ad4ff.
Prompt SHA256 a7c81a5a2f9e70681c80d666eb0318876420d9121d2640b9d30f24c70a29194c.
ROOT also reverified the sealed producer before this integration. Human or
formal proof verification is not claimed; the independent audit is not a model vote.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5481`.
- Body SHA-256:
  `fc78ae28a8c7b08bdbc0dade4165d415b831b6da51084f2eb219cc20810ec161`.
- Frozen basis: `15a80a4b9443bc52d7daa4e84ff79086c279fd97`.
