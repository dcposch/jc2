# A persistent cusp with a fully ramified fibre: candidate obstruction

Producer: swarmHQ ROOT; hosted model identity unmeasured.
Date: 2026-10-31T06:28:27.855842+00:00
Basis: 22d3eb834cd0d985f74472502c66300267f68dbe
Evidence tier: INTERNAL / UNREVIEWED; desk argument conditional on the named foundations.
Lifecycle: PRODUCER-CHECKED candidate, awaiting independent hostile review.

## Statement and scope

Let E=C(p,q) and let K/E be a finite extension of degree n>1.
Let h0:X0 -> A2_(p,q) be the finite normal model of K over this affine plane.
Assume D is an irreducible reduced branch curve satisfying all of the following:

1. The projective closure of D is smooth at every point at old infinity and has exactly one intrinsic singular point z, lying in the old affine plane.
2. D is unibranch at z, and the normalization of its affine part is A1.
3. The entire set-theoretic fibre h0^(-1)(z) is contained in the union of prime divisors of X0 over D with generic transverse ramification index greater than one.

Candidate conclusion: there is no birational target change (p,q) -> (p',q') with C(p',q')=E and nonzero constant Jacobian, and no finite embedding K into L=C(x,y), for which p',q' become a polynomial Keller pair in x,y.
This is an obstruction for prescribed covers with these strong hypotheses, not a proof of JC2 or a classification of possible counterexamples.
No invariance of arbitrary local slack or of arbitrary old affine points is asserted.

## Dependencies and prior work

The [persistent singular branch report](ramified-sheet-persistent-singular-branch-swarmHQ-root-astra-sol56-20261027T041000Z.md) supplies two inherited inputs:
constant-Jacobian birational plane maps and their inverses extend from their affine planes to the opposite projective plane; and a curve with an intrinsic old affine singularity persists as a curve with new affine part.
The latter follows by resolving only over old infinity: the singular strict curve can neither be exceptional nor map birationally to a smooth projective line.
That report has whole SHA256 8e9a2c92d7443bce1afe267492c803f4d429759f804f000c377a53e8351c746b.

The [all-Keller budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md), whole SHA256 5c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907, supplies the actual finite normalization X of the WHOLE U=A2, disjoint omitted curves E_i with bijective normalizations A1, image normalizations A1, and

    N-1 = sum_i r_i delta_i + sum_i sum_(x in E_i)(m_x-r_i t_x),
    m_x-r_i t_x >= 0.

Here r_i is the generic normal ramification index, delta_i the degree on curve normalizations, m_x the local finite-fibre length, and t_x the local curve-normalization degree.
The new argument does not need the later stronger scheme-smoothness statement for E_i.

Named additional foundations: resolution of birational maps of smooth projective surfaces by point blowups; finite morphisms and normalization under restriction to open sets; going-down for an integral extension over a normal domain; multiplicativity of DVR ramification indices; and the Abhyankar-Moh theorem that a closed embedded A1 in complex A2 is carried to a coordinate line by a polynomial automorphism.
For the last theorem, the [publisher record](https://www.degruyterbrill.com/document/doi/10.1515/crll.1975.276.148/html) verifies the citation, S. S. Abhyankar and T. T. Moh, *Embeddings of the line in the plane*, J. reine angew. Math. 276 (1975), 148-166, DOI 10.1515/crll.1975.276.148.
The publisher did not expose the article body; this is a named-foundation use, not a fresh source proof or theorem-text audit.
Novelty is unassessed; the bounded frozen search is routing evidence only.

## Argument

Assume a realization as above. Let tau be its birational target map and put N=[L:E].
Every ramified place over D remains ramified in every extension to L.
By inherited branch persistence, D has a strict image D' with nonempty new affine part.
Every such extended ramified divisor in the actual normalization X lies outside U, since the map is etale on U.
Consequently D' is an omitted-image curve, so its affine normalization is A1 by the all-Keller package.

### The unique singular point must remain affine

Take the closure of the graph of tau in P2_old times P2_new.
Since tau and tau^(-1) are regular from their respective affine planes to the opposite projective plane, the graph projections are isomorphisms over both affine planes.
Resolve the graph outside the union of these two smooth open charts.
This gives a common smooth projective surface T with maps a:T -> P2_old and b:T -> P2_new, where a is an isomorphism over old A2 and b is an isomorphism over new A2.
Factor a into point blowups, all over old infinity.
The strict transform D_T has exactly one intrinsic singular point, namely z: strict transforms of a smooth curve under point blowups remain smooth, and a is an isomorphism near z.

Suppose b(z) lies at new infinity. Then b being an isomorphism over new A2 implies D'_aff is smooth.
Its normalization is A1, so it is a closed embedded A1 in new A2.
Abhyankar-Moh supplies a polynomial automorphism carrying it to a line.
Composing this automorphism with tau gives another constant-Jacobian birational target map taking D to a line.
This contradicts inherited singular-branch persistence: on a resolution supported over old infinity the singular strict transform would map properly and birationally to P1, hence finitely and therefore isomorphically, which would make it smooth.
Thus z'=tau(z) is affine. Since both projections are isomorphisms on the respective affine charts, tau is a local isomorphism between neighborhoods of z and z'.
In particular D' is unibranch at z'.

### The entire new fibre is ramified and omitted

Restrict to these isomorphic neighborhoods of z and z'.
Uniqueness of integral closure identifies the finite normal models for K there, and inclusion K into L gives a finite morphism from the local restriction of X to that of X0.
Let y be any point of X over z'. Its image x0 lies over z, so hypothesis3 puts x0 on a ramified prime divisor E0 over D.
Going-down for the finite integral extension with normal base gives a height-one prime through y lying over E0.
Its ramification index over the target is the product of its relative index and the index of E0, hence is greater than one.
It is therefore an omitted component of X minus U, with image D'.
Every point of the finite fibre over z' lies on such an omitted component. Thus U misses z'.

If any omitted component has an image containing z', finiteness makes its fibre over z' nonempty.
A point of that fibre already lies on one of the ramified omitted components just obtained.
Pairwise disjointness of omitted components forces the two components to coincide.
Hence every omitted component whose image contains z' has image D'.

### The sheet budget forbids that missed unibranch value

Let I be precisely the omitted components whose images contain z'.
The normalization of D' has a unique point above z', because D' is unibranch there.
For each i in I, the finite polynomial map of affine-line normalizations therefore gives

    sum_(x in E_i over z') t_x = delta_i.

All fibre points lie on these pairwise disjoint omitted curves, and finite flatness gives sum_(y over z') m_y=N.
Thus the contribution to total nonnegative slack from this one target fibre equals

    S_z' = N - sum_(i in I) r_i delta_i.

The global budget would imply

    N-1 >= sum_i r_i delta_i + S_z'
        = N + sum_(i notin I) r_i delta_i >= N,

a contradiction. This proves the candidate conclusion, subject to hostile checking of the new steps and inherited foundations.

## Fixed degree-four application

Use only the [retained normal-cone cover](smooth-ramification-singular-source-swarmHQ-root-sol56-20261031T034712Z.md), whole SHA256 2429561cbda33049a4d1737d04cd46771b58dd7d363002900adc24f755f5536b:

    B=C[a,b,c]/(ac-b^2),  P=a^2+b,  Q=3c+12ab+8a^3,
    B=C[P,Q,T]/(T^4-6PT^2+QT-3P^2).

It is finite flat of degree4 and normal. Its sole ramified divisor is E0=V(b,c), with generic index3 and residue degree1.
Its image is D:Q^2-64P^3=0, parametrized by (P,Q)=(a^2,8a^3).
The old origin fibre is supported only at a=b=c=0, which lies on E0.
The projective equation Q^2 Z-64P^3=0 has its only singular point at [0:0:1]; its unique infinity point [0:1:0] is smooth since the Z derivative there is1.
The origin is unibranch and affine normalization is A1. Thus all candidate hypotheses hold.
The older generic ramified-sheet mass criterion alone reads3<4 here and does not exclude this cover.
The proposed refinement would exclude its realization after every allowed constant-Jacobian birational target change and every finite rational source extension.
This is not a repair of the donor: its existing complement is A1 times G_m, not A2.

## Replay, limitations and next test

Desk-only; one retained example, no CAS or generated family. The finite cover facts are inherited from the exact independently reviewed report; the projective cusp check is the single elementary hand check here.
The concrete new work is point persistence under an actual Keller realization and the finite-extension fibre argument, not a general local-slack invariance theorem.
Independent hostile review must try to break the common resolution, the use of Abhyankar-Moh, local normal-model identification, going-down through each fibre point, and the all-Keller sum at the unibranch image.
No assumption of smooth X or Cartier omitted divisors is made. No arbitrary source substitution, nonconstant target Jacobian, multi-cusp extension, surjectivity of all Keller maps, or degree-one conclusion is covered.
The primary whole-polynomial negative-fold gap remains open. No independent review or promotion of this candidate has occurred.

## OPENS RAISED

None. This is a bounded candidate implication for hostile review, not a new global campaign open.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `22d3eb834cd0d985f74472502c66300267f68dbe` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10155`.
- Body SHA-256:
  `eb40e4f81b565953b35aa56944caea1c30a8deacb2096c5a5737fd1dab135851`.
- Frozen basis: `22d3eb834cd0d985f74472502c66300267f68dbe`.
