# Degree-estimate interface: no additional obstruction for the current tower

Root Astra,2026-09-06T10:44Z; post-round-cutoff bounded primary check.
Verdict NO_NEW_MECHANISM at this exact interface, not rejection of every
degree estimate. JC2 and the three current full loci remain unresolved.

Primary source read: S.Venereau, *A parachute for the degree of a polynomial
in algebraically independent ones*, arXiv0704.1561v2, all four pages,
especially the definition/property(2), theorem and Corollary1:
https://arxiv.org/pdf/0704.1561 . This supplies a generalized
Shestakov–Umirbaev estimate. It requires algebraically independent inputs;
three polynomials F,G,Q in two variables cannot be used as three independent
generators. For a Keller pair of degrees n,m, its parachute is n+m-2.
With the present leading relation G^3=F^2, the minimal top degree in G
over k(F_top) is3; consequently a polynomial of G-degree3q+r has lower
degree bound q*(3m-(n+m-2))+r*m. No surjectivity follows from this bound.

Client facts are the already reviewed explicit P2/P3 recurrences in
xmodel/full-ideal-counterexample-gate-fable5-20260906.md,
SHA5fc61ae7f4f78e7d28cde6ac3eaa7c24e7ca98966ebf94de7cbaf5ea69fb059e,
as corrected by AUDIT17(ppppppppppp). Q has G-degree3, while W has
G-degree9 or12; leading terms cannot cancel those formal variable degrees.

| n,m | parachute | Q bound / actual | W bound / allowed | exact d_G W |
|---|---:|---:|---:|---:|
|99,66|163|35 /55|105 /145|242|
|108,72|178|38 /63|152 /227|333|

These bounds do not contradict the current characteristic data. More
sharply, the elementary chain rule itself gives
deg R(F,G)>=deg(partial_G R(F,G))-n+2 when J(F,G) is a nonzero constant.
For Q this returns35/38. For W it returns145/227, exactly the upper
bounds already used to force constant J in the reviewed characteristic
criterion. The attempted composition therefore returns the existing endpoint,
not a new exclusion. Applying the automorphism corollary would instead
ASSUME k[F,G]=k[x,y], the conclusion sought.

History search found previous scoped Davenport–Stothers uses in AUDIT,
including the order-four mu4=0 client near line8725. They involve actual
extremal univariate pairs and cannot be transported to this different
coefficient family without a map. A search also located Formanek's2011
extra-special-pair paper, but the publisher PDF returned403; no theorem
from its abstract was used. This is a targeted interface check, not a new
broad literature sweep and not a clock reset.

Disposition: do not charge a new generic degree-bound lane on these
numbers. A stronger client-specific inequality would need an additional,
independently established hypothesis. No change to the frozen blind packet.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `2751`.
- Body SHA-256:
  `a407247aee91910bf7a4d8276bd1591566c3d64926907115b0f2f18220d9669a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
