# Independent FIRST of the hyperbolic moving-pencil theorem

Independent reviewer: Fable5.1, requested through the campaign's Claude adapter.
Integration and binding wording clarifications: swarmHQ ROOT/Astra.
Date: September 19, 2026 UTC.
Evidence: MANUAL, different-model hostile review with named classical imports.
Verdict: all five charged proof interfaces CONFIRMED; no producer correction.
This is ROOT's structured integration, not a verbatim copy of the raw review.
Promotion authority belongs to HYPERBOLIC-MOVING-PENCIL-1 in AUDIT.md.

## 1. Exact reviewed claim and custody

The [producer](hyperbolic-moving-pencil-swarmHQ-root-20260919T203700Z.md)
was reviewed at public commit0645b42e986b9204270855e8d48c7ee0dd5a35b3.
Its whole-file SHA256 is
bcb4e3c3851f50db05654c9acfcba11131d55df4f29302a28cf89dceeb42370a;
its artifact manifest SHA256 is
eb727b11b0d5202613d77ae98efb700dff99ebcbbb56f597c1beb7e9d2e1fb9c.
The producer's pre-authoring basis remains e0f8b2fb387b10606be17251eaa659d14b8573c7.

Claim: a dominant polynomial F with a nonconstant polynomial h satisfying
C(h) relatively algebraically closed in C(x,y), h F=psi(h), deg(psi)=d>=2,
and smooth FULL geometric generic affine fiber of type 2g-2+n>0, has
N(F)=d and a fixed rational function r not in C(h). The exact-Jacobian1
case is impossible by the accepted rational-area invariant theorem.
Existence of such a pencil for arbitrary Keller maps is NOT asserted.

Reviewer author completion20:53:43 UTC; adapter/parent termination20:53:57,
both exit0. ROOT observed the supervisor inactive/dead20:54:40, verified
absence of the exact processes and original cgroup20:55:00, then collected
the version2 receipt FIRST. The whole246-line review and23-line final-only
log were read by20:55:13. No live report, log or receipt was inspected.
The ten charged snapshots and prompt/launcher/adapter pins were unchanged
in the terminal receipt and ROOT's post-collection measurements. Raw hashes:

- Review: 8e8a0c29ca4b08897a7ad26d964e37568dec5264aa390adc80d5ce4f81300717.
- Final-only log: eab36602c2d8bf7379391679aac7ad32e41e8275aaf784db09911418d3816dec.
- Terminal receipt: c575ccddf87d55f7fc7c5e497283c67a73586bc652aef26898635ef3729553c9.

All three raw files were retained444 with identical hashes after the mode
change. Producer and raw reviewer bytes are not amended by this integration.
The requested/reported model is not independently provider-attested.

## 2. Independent mathematical reconstruction

### Generic degree and full affine isomorphism — CONFIRMED

For K=C(h), K0=C(psi(h)), sigma=F*, regularity of sigma(L)/K0 gives
linear disjointness from K/K0. Thus [sigma(L)K:sigma(L)]=d and
N(F)=d*k, where k=[L:sigma(L)K] is the induced generic CURVE degree.
The morphism p->(F(p),h(p)) into the base-changed source supplies a regular
map on the full affine fiber; no affine boundary is silently discarded.
Source and base-changed target have the same geometric genus and puncture
count. Affine regularity implies f^-1(S_target) subset S_source. The
ramification above target punctures is at least(k-1)n. Riemann--Hurwitz
gives (k-1)(2g-2+n)<=0, hence k=1. Equal puncture counts then give a
FULL pointed isomorphism, not just a projective birational map. N(F)=d.

### Unordered pointed moduli — CONFIRMED

Over a suitable open base, a finite etale cover labels the punctures.
Compose its classifying map with the finite S_n quotient of the classical
quasi-projective coarse moduli space. The composites on the overlap agree
on closed points, hence agree because the overlap is reduced and the target
separated; finite etale descent yields the unordered moduli map m.
The generic pointed isomorphism gives m psi=m as rational maps. A
nonconstant image curve would furnish a nonconstant v in C(t) with
v(psi(t))=v(t), contradicting deg(v)*d=deg(v). Thus m is constant.
The coarse-moduli existence/classifying-map properties remain NAMED
classical imports, checked by ROOT at statement level in the producer's
cited lecture notes. Neither seat claims a moduli-construction proof audit.

### Trivialization and finite full automorphism group — CONFIRMED

For delta=2g-2+n>0 with n>=1, the degree of omega(S)^3 is at least2g+1
in every allowed case. Very ampleness and vanishing of higher cohomology
give relative projective embeddings after shrinking the base. The bundle
is functorial in the pointed pair, so its finite-type projective-linear
Isom scheme represents all pair isomorphisms. Constant coarse moduli makes
its image contain all closed points; constructibility gives a nonempty
generic Isom fiber, hence an isomorphism after a finite extension of K.
There is no fine universal family or original-base trivialization assumed.

The full automorphism group G of a constant pair is a finite-type subgroup
of the corresponding projective linear group. Its tangent space is
H^0(T(-S))=0 because deg T(-S)=-delta<0. It is therefore finite, and in
characteristic zero its geometric automorphisms are already defined over
the algebraically closed constant field C. Unordered punctures only add
a finite permutation action; they do not change this tangent calculation.

### Galois descent and semilinear invariance — CONFIRMED

Choose a geometric trivialization alpha and nonconstant q in C(C0)^G.
Changing alpha by a Galois automorphism changes it by an element of G,
so r=alpha*(q) is Galois invariant. More explicitly, r is defined over
a finite Galois extension K'/K; regularity makes LK'/L Galois with the
same group, whose fixed field is L. Thus r belongs to L, and r is not
in K because it is nonconstant on the geometric generic curve.

The embedding t->psi(t) extends to an automorphism s of Kbar fixing C:
its algebraically closed image contains K0 and Kbar is algebraic over K0.
The induced semilinear map Sigma of Lbar is well defined and injective by
regular-field disjointness. It is surjective because k=1 gives
L=sigma(L)K. It preserves the pointed curve. In the alpha trivialization,
Sigma differs from coefficient action s by an element of G. Both fix q,
so sigma(r)=r. This is invariance for F ITSELF, not merely an iterate.
No chosen finite trivializing cover is assumed psi-stable and no lift of
psi to that cover or fibration section is used.

### Exact-area corollary and scope check — CONFIRMED

For J(F)=1 the [accepted rational-area theorem and binding review](rational-area-first-integration-swarmHQ-root-20260919T121900Z.md)
apply to the constructed invariant and give N(F)=1 against N(F)=d>=2.
The example h=(x^2-1)y, F=(x,(x^2-1)y^2) has h F=h^2, generic fiber
A1 minus two points, N=2 and fixed r=x; its nonconstant Jacobian
2(x^2-1)y correctly keeps it outside the corollary. No CAS was used.
The review checks the explicit exclusions: arbitrary pencil existence,
A1/Gm fibers, d=1, arbitrary constant determinant, classification and JC2.

## 3. Binding clarifications to reviewer additions

ROOT accepts the five mathematical verdicts. Two compressed reviewer
phrases are read as follows; neither changes the producer:

1. The geometric generic affine coordinate ring in the semilinear check
   is the generic fiber ring tensored OVER K with Kbar, including the
   relation h=t. Read the review's shorthand C[x,y] tensor Kbar in this
   sense, not as the free two-variable polynomial ring over Kbar.
2. A one-output normalization MAY destroy the displayed pencil identity;
   it does not automatically preserve it. The review's "would break"
   wording is not an impossibility assertion for every particular
   normalization. The producer already uses the correct no-silent-change
   caution and makes only the exact-J1 corollary.

The review's optional observation about automatic generic smoothness does
not remove a hypothesis from the promoted statement. No enlarged theorem,
degree-one-base extension or new pencil-family investigation is adopted.

## 4. Delivery limits and accepted scope

The reviewer reports an early DRAFT placeholder and one automatically
persisted oversized tool result, left unread; it recovered the clipped
input through bounded rereads. It wrote the report with shell heredocs,
not the requested apply_patch workflow. A malformed first HQ hash command
was corrected. These delivery deviations are retained, not retroactively
certified as compliance. Substantive partial-save timing is not established
by the final-only log. The receipt and ROOT checks confirm unchanged input
bytes; they are not a full write/execution trace or proof of every claimed
output restriction. No memory/settings/credential/Git changes are reported.

The review is mathematical evidence at MANUAL/import-dependent scope,
not formal verification, literature novelty or independent validation of
the classical moduli construction. Accepted: N(F)=d and a fixed rational
invariant for an existing primitive hyperbolic polynomial moving pencil
with d>=2; impossibility of that configuration when J(F)=1. The separate
homogeneous-pencil theorem and the exact-area invariant theorem retain
their own hypotheses. No actual pencil is supplied for a hypothetical
noninvertible Keller map, and no automatic successor is selected.
JC2 remains unresolved.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

ROOT integration author completion: 2026-09-19 20:58:12 UTC, after whole
body readback and the trusted collision check. Sealed inputs stay unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9530`.
- Body SHA-256:
  `b412d98fbbcc0dfbaf8ff39cdb9a4d0b5aa8a1f5317b1ab37d502e3981633bf8`.
- Frozen basis: `0645b42e986b9204270855e8d48c7ee0dd5a35b3`.
