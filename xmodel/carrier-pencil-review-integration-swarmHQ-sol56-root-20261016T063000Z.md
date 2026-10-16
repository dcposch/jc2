# Review of the carrier pencil obstruction

Claim ID: CARRIER-PENCIL-OBSTRUCTION-1. PROVED / PROMOTED, exact scope below.
Producer: swarmHQ coordinator ROOT. Independent requested model: gpt-5.6-sol,
native handle /root/carrier_pencil_review_sol56_0623. Integration by ROOT,
not a claim that the reviewer authored this file. Date: 2026-10-16.
Terminal verdict CONFIRMED, collected by 06:29:54 UTC.
Requested model routing was not independently provider-attested.

## Binding statement

Put p=UV^3-V and B=C[U,UV,UV^2,p] inside C[U,V]. Every nonzero pencil
member aU+bp^2, with a,b in C, has no B-valued nonzero-constant Jacobian
mate. If ab!=0, it has no rational mate in C(U,V) either.
For all alpha,beta in C and H in B, the pair
(p^2+alpha H,U+beta H) therefore has no nonzero constant Jacobian.
There is no bound on the degree of H.

This excludes constant-vector-direction perturbations of this one finite-map
control. It does not exclude general dependent increments, general deformations,
all pairs in B, or JC2 counterexamples. External novelty remains UNKNOWN.

## Shorter proof for polynomial mates

For lambda!=0, let T=U-lambda p^2. Choose a nonzero complex V with

    V^4=-3/(4lambda),  U=1/(3V^2).

Then p=-2V/3 and

    T_V=-2lambda p(3UV^2-1)=0,
    T_U=1-2lambda pV^3=1+(4lambda/3)V^4=0.

Thus T has a critical point, excluding a polynomial Jacobian mate even
in the entire ring C[U,V]. ROOT proposed this simpler test during review;
Sol independently recomputed it and confirmed both vanishing derivatives.
It does not exclude rational mates, which may have poles at that point.

The endpoints require separate statements. If J(U,Q)=kappa!=0 and Q is
polynomial, Q=kappa V+h(U). Substitution U=g^2+g^3p,V=1/g shows a pole,
whereas every generator of B is polynomial in g,p; hence Q is not in B.
For p^2, the factorization J(p^2,Q)=2p J(p,Q) excludes polynomial Q.
These endpoint scopes cannot be strengthened to rational exclusion:
J(U,V)=1 and J(p^2,-1/(4pV^2))=1.

For (alpha,beta)!=(0,0), P=p^2+alpha H and Q=U+beta H have the nonzero fixed combination
L=beta P-alpha Q=beta p^2-alpha U would have a B-valued mate if
J(P,Q)!=0 were constant: J(L,Q)=beta J(P,Q), or, when beta=0 and
alpha!=0, J(L,P)=alpha J(P,Q). The zero-direction case is the original
NON-KELLER pair. This proves the asserted perturbation exclusion directly.

## Review of the stronger rational exclusion

Sol independently checked the full [producer proof](carrier-pencil-obstruction-swarmHQ-root-20261016T062100Z.md),
including the inverse field substitution and every place on the generic curve.
For T=t, w=2lambda p-g^3 gives

    w^2=g^6+4lambda g^2-4lambda t,  dQ=kappa g dg/w.

The sextic is squarefree over the algebraic closure of C(t). Its finite
points have no pole of g dg/w. At BOTH infinity points, s=1/g and z=ws^3
give z=+1 or -1 and g dg/w=-ds/z, regular and nonzero.
A pole of a rational primitive would give a pole of its derivative in
characteristic zero; a pole-free function on the projective integral curve
is constant. The resulting contradiction proves the mixed rational exclusion.
No mathematical correction to the producer proof was required.

The strongest falsification checks targeted the Jacobian sign, possible
repeated roots, missed infinity places, primitive poles, the B-versus-R
endpoint, and the distinction between constant-direction and arbitrary
rank-one/dependent deformations. All survived at the stated scope.

## Frozen evidence and custody

Reviewed contribution commit: 18dbb2b9d3651e2e2fef7384f1e874aac896af9e.
Producer report:6755bytes,mode444;
full SHA256 a30a2ea73c5c150380c837018a5d13075bf6549ab8291285aebf456546660b7d.
Body6423bytes/SHA256 b38e88422b66cba86f632418a8e61567b6ae2d79cd8af9281bcaa3d9e7f434fe.
Manifest707bytes,mode444;
SHA2562bf91fbda68129be5dd096bf9c52e7954ca51119edf9d3561f84a8f19c1b68a4.
Frozen artifact basis4eb6f7792a1b87006b5fa365e8d74b97cd39fca5.

The reviewer reported whole-set metadata and nonsymlink checks before reading,
manifest-first collection, whole report/seal reading, canonical verification,
unchanged postpins and no deviations. ROOT independently rechecked the same
report/manifest and shared-original hashes at terminal collection; verification
returned VERIFIED. The sealed producer header remains unchanged; this report
records its reviewed lifecycle, without retroactively editing its bytes.

Read scope: required HQ policy/state and runbook sections; whole public
README,AGENTS,COORDINATION,FALLACY-v2; APPROACHES805--836; the whole frozen
manifest and producer report. No external source, CAS, protected-tree access,
file write or further research task occurred in the reviewer lane.
Neither review nor collision screening establishes external novelty.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `18dbb2b9d3651e2e2fef7384f1e874aac896af9e` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4937`.
- Body SHA-256:
  `f5ef1af1f11073f7ee97d4ef60f2dd972d624a8c30115ddf8cdd1459fb460df7`.
- Frozen basis: `18dbb2b9d3651e2e2fef7384f1e874aac896af9e`.
