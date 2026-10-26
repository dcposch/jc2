# Smooth image branches carry no slack; an irreducible nonproper curve needs a nonimmersed branch
Producer: swarmHQ coordinator and configured gpt-6-astra co-research; independent configured gpt-5.6-sol review. Hosted model identities unmeasured.
Date: 2026-10-26 UTC. Basis: d6a4dceea8f02bf9ce04a934e3b0b6a1102e9b84.
Evidence tier: PROMOTED / MANUAL / CONDITIONAL. Lifecycle: independently reviewed at the exact scope below.

## Statement and scope
Let F=(P,Q):C^2->C^2 be a polynomial Keller map, and let h:X->C^2 be its normal finite target normalization of degree e, with the whole source U=C^2 open in X.
Use the admitted all-Keller boundary package: X\U is a union of disjoint omitted curves E_i, their normalizations are finite-bijective copies of A1, and the image curves D_i=h(E_i) have normalization A1.
The D_i need not be distinct. Put r_i=generic transverse ramification order, delta_i=degree(E_i^nu->D_i^nu), t_x=local degree of that normalization map, and m_x=local fibre length of h at x in E_i.
A selected image branch is **immersed** when its normalization map to C^2 has nonzero derivative there; this permits nodes, tangencies and crossings with other branches.

1. If the selected image branch at h(x) is immersed, the finite analytic germ at x is cyclic: (s,v)->(s^{r_i},v). Thus X and E_i are smooth at x, t_x=1, m_x=r_i, and the local slack m_x-r_i t_x is zero.
2. Consequently all excess in e-1-sum_i r_i is supported above intrinsically nonimmersed image branches.
3. If the nonempty actual nonproper-value set of F is irreducible, it must have an intrinsically nonimmersed branch, conditional on the external embedded-A1 exclusion stated below.
The last claim does not exclude an individual immersed component of a reducible nonproper-value set. JC2 remains unresolved.

## Dependencies and prior work
The [all-Keller sheet identity](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md) and [pointwise fibre corollary](pointwise-fibre-count-swarmHQ-root-sol56-20261026.md) are accepted parent inputs, with their original review and hypotheses.
They supply e-1=sum_i r_i delta_i+S, S=sum_(i,x)(m_x-r_i t_x)>=0, and

    #F^{-1}(y)=1+sum_i r_i delta_i(1-b_i(y))+S_off(y).

Here b_i(y) is the number of normalization branches of the individual D_i over y, zero off D_i; repeated E_i are counted separately. S_off is total slack away from h^{-1}(y).
External interface: a nonconstant polynomial map C^2->C^2 with an irreducible nonproper-value component isomorphic to A1 must have a critical point.
This is the statement preceding Theorem1.2 on page3 of [Nguyen Van Chau, arXiv:0710.5212v1](https://arxiv.org/abs/0710.5212v1), *A note on singularity and non-proper value set of polynomial maps of C2* (2007).
ROOT and reviewer read only the selected statement/interface (local extracted text96-114); the source proof and Abhyankar-Moh/dicritical-series dependencies were not independently audited. Reliance on this external theorem remains explicit.
The [source-scope record](../box/smooth-branch-slack-swarmHQ-20261026/purity0820-chau-source-scope.md) and fetch receipt fix the exact version. No general immersion exclusion or novelty is claimed.

## Local cyclicity
Fix x in E_i and a smooth selected analytic image branch through y=h(x). Choose target coordinates (u,v) in which this branch is u=0.
Finiteness separates the points of h^{-1}(y): after shrinking a bidisc V, take the finite local block X_x over V containing x.
Disjointness and unibranchness of the omitted E_i allow this block to be chosen with its omitted locus lying over u=0. Other omitted points above y occupy different blocks.
Off u=0 the block lies in U, where h=F is etale. Normality makes the local germ irreducible; removing a complex divisor leaves the sufficiently small local block connected.
We therefore have a connected finite etale cover of Delta* times Delta. Its fundamental group is Z, so a transitive finite permutation representation is one cycle.
The punctured cover is analytically (s,v)->(s^m,v). The normal finite extension is unique as integral closure, so the same model extends over u=0.
Since the omitted curve dominates u=0, it is the model divisor s=0. The generic transverse index is m=r_i, and its map to the selected image branch has local degree t_x=1.
Finite flatness of h (normal surface Cohen-Macaulay over a smooth surface) identifies the local rank with the fibre length m_x=m=r_i.
Other target branches may have harmless non-omitted inverse-image divisors in this same block. The argument excludes extra omitted boundary branches; it does not exclude all such divisors.
This qualification is also the mandatory [review wording correction](../box/smooth-branch-slack-swarmHQ-20261026/purityreview0905-sol56-wording-clarification.json).

## Localization of excess
Let B denote the finite set of omitted points whose selected image normalization branch is nonimmersed. The admitted polynomial maps A1->A1 satisfy sum_x(t_x-1)=delta_i-1.
Combining this with the sheet identity gives

    e-1=sum_i r_i+sum_(i,x in B)(r_i(t_x-1)+m_x-r_i t_x)
       =sum_i r_i+sum_(i,x in B)(m_x-r_i).

Each summand is nonnegative by the admitted local length inequality and t_x>=1. The local lemma removes every other point from this sum.
If every image branch is immersed, all t_x=1. A finite polynomial A1->A1 with no finite ramification has degree1, hence every delta_i=1, S=0, and e=1+sum_i r_i.

## One common image
Suppose all omitted curves have one common irreducible image D and every branch of D is immersed. Set W=sum_i r_i=e-1. Nonempty boundary gives W>=1 and e>=2.
For y in D the pointwise identity becomes

    #F^{-1}(y)=e-(e-1)b(y),

where b(y) counts the branches of D at y. If b(y)>=2, nonnegativity forces e<=2, hence e=2 and W=1.
There is then exactly one omitted curve and its r is1. Local cyclicity makes h etale everywhere on this curve; h is already etale on U.
Thus h is a connected finite etale cover of C^2, which has degree1 by simple connectedness. This contradicts e=2.
So D is unibranch everywhere. Together with immersion this makes D smooth, and its A1 normalization is an isomorphism: D is a smooth embedded A1.
The external Chau interface excludes such a component for a Keller map. Therefore the assumed immersed one-common-image case is impossible.
For the actual finite normalization, h(X\U) is exactly the nonproper-value set. Indeed h is finite/proper, so the restriction is proper away from that image; an omitted point is approachable from dense U and produces a sequence escaping compact subsets of U with bounded target limit.
The accepted boundary package has no isolated omitted points. Thus irreducibility of the nonempty nonproper-value set is exactly the one-common-image situation used here.

## Review, replay and limitations
Desk-only; no computation or formal proof is asserted. The [evidence README](../box/smooth-branch-slack-swarmHQ-20261026/README.md) links byte-identical producer, addendum, independent review, qualifications and checksums.
The reviewer checked the new arguments using the accepted sheet identities; it did not freshly audit the later published parent bodies. Exact earlier personal framework reuse is documented in the coverage supplement.
The review's initial archive gate and metadata batching omissions were disclosed, then repaired with matching hashes. ROOT separately verified all31 fixed inputs plus12 archive blobs and read the complete new mathematical evidence and corrections.
The producer's general reducible-image GAP remains valid. The one-image addendum adds a restricted consequence; it does not overturn that gap.
No global inertia-generation hypothesis, abstract surface control, source realization, or general properness conclusion is introduced.
The next mathematical obstacle remains controlling nonimmersed branches or obtaining an actual-global constraint across several distinct image components. No successor test is asserted here.

## OPENS RAISED
None. The existing nonimmersed and reducible-image gaps remain.

## COLLISIONS
```text
## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `d6a4dceea8f02bf9ce04a934e3b0b6a1102e9b84` (Git blobs only).
```
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8270`.
- Body SHA-256:
  `5479382b270e8038a33a5e6f15ab8d6e1ea194582ed7fa081739761dad9fe37d`.
- Frozen basis: `d6a4dceea8f02bf9ce04a934e3b0b6a1102e9b84`.
