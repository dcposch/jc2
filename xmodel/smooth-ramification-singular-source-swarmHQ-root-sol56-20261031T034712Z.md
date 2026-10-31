# Smooth ramification support does not force a smooth normal source

Producer: swarmHQ (ROOT; configured gpt-6-astra, hosted identity unverified).
Independent hostile reviewer: swarmHQ (configured gpt-5.6-sol, hosted identity unverified).
Date: 2026-10-31T03:47:12.358175+00:00
Basis: 68e87443925f50914a6cbb858d9d2f061dbda8b3
Evidence tier: MANUAL, relative to the named standard foundations below.
Lifecycle: PROVISIONAL. Independent verdict PASS at the exact reduced-support scope.

## Statement and scope

Let X=Spec C[a,b,c]/(ac-b^2), let E=V(b,c), and set

    P=a^2+b,  Q=3c+12ab+8a^3.

The map h=(P,Q):X -> A2 is finite flat of degree4. The source X is normal and singular at its origin. Its entire reduced non-etale support is the single scheme-smooth affine line E, which is non-Cartier at that point. Generically the transverse ramification index is3 and the different divisor is2E. Thus smooth reduced ramification support does not force a normal finite source to be smooth.

This is a counterexample to that local implication, not to JC2: X-E is A1 times G_m, so it fails the whole-A2 source condition. It does not settle smoothness of the actual Keller normalization.

## Dependencies and prior work

The construction is obtained from the [already recorded rank-zero donor](rank-zero-ramification-counterexample-swarmHQ-root-sol56-20261030.md) by a=u^2,b=uv,c=v^2. The equations below give a direct proof independent of any unproved quotient assertion. Historical priority and novelty are unassessed. The old donor's failure of the whole-source condition remains; no repair or family of controls is proposed.

## Exact reviewed argument

The following39LF are byte-identical to lines20-58 of the [sealed independent review](../box/smooth-ramification-singular-source-swarmHQ-20261031T034712Z/independent-review.md): 2202bytes, SHA256 `b1bf9959fbfcc99225314914b7af7455d5b5644dff0d288184ad290cb305ddca`. No mathematical statement or proof was changed during integration.

Let f=T^4-6PT^2+QT-3P^2. The substitutions
a=T, b=P-T^2, c=(Q-12PT+4T^3)/3 give 3(ac-b^2)=f, and substitution
back into P=a^2+b and Q=3c+12ab+8a^3 fixes P,Q,T. Thus
B is exactly C[P,Q,T]/(f). Monicity injects C[P,Q] and makes B free
with basis 1,T,T^2,T^3; h is finite flat of degree four.

The irreducible cone ac-b^2 is a hypersurface domain. Its gradient
(c,-2b,a) vanishes only at the origin. Hypersurface Cohen-Macaulayness
and regularity in codimension one give normality by Serre's criterion.
At the origin, embedding dimension three exceeds dimension two, so X is singular.

For the monogenic presentation,
Omega_(B/C[P,Q])=(B/(f_T))dT and f_T=4a^3-12Pa+Q=3c.
Finite-flat plus unramified iff etale therefore gives etale locus D(c).
Moreover B/(c)=C[a,b]/(b^2), so sqrt((c))=(b,c) and
B/(b,c)=C[a]. Hence E=V(b,c) is the complete reduced non-etale support
and is scheme-smooth. The Fitting/different scheme is V(c), not E;
generically its divisor is 2E. There is no hidden second ramification component
and no conflation of reduced support with the reduced different.

At the generic point of E, a is a unit, b is a DVR parameter, and c=b^2/a.
The image divisor is the irreducible cusp g=Q^2-64P^3=0, and in that DVR
g=b^3(8+9b/a^2). The parenthesized factor is a unit, so the transverse
ramification index is exactly three. Also a=Q/(8P) in the cusp function field,
so the residue degree is one.

With m=(a,b,c), the classes of b,c are independent in
(b,c)/m(b,c). Nakayama therefore rules out a principal ideal at the origin:
E is not Cartier there despite being a smooth curve. Setting P=Q=0 gives
f=T^4, so the finite target-origin fibre is supported only at the source origin.
On E, (P,Q)=(a^2,8a^3); thus a is precisely the cusp-normalization parameter.

Finally, X-E=D(c) and B[c^(-1)]=C[b,c,c^(-1)] via a=b^2/c.
The complement is A1 times G_m, with a nonconstant unit, and is not A2.

Named foundations used: monic-quotient freeness; the Jacobian and Serre
normality criteria; hypersurface Cohen-Macaulayness; monogenic relative
differentials; finite-flat unramified/etale equivalence; DVR ramification;
Nakayama's lemma; and normalization of the plane cusp. No source audit is claimed.

## Replay and negative controls

Desk-only. The monic presentation, relative differential module, full reduced support and unit obstruction are explicitly checked above; no CAS, numerical experiment or parameter sweep is used. [Original candidate, independent review, custody qualification and checksums](../box/smooth-ramification-singular-source-swarmHQ-20261031T034712Z/README.md) preserve the exact evidence. The candidate's original UNREVIEWED label is historical and unchanged. The complement's nonconstant unit is the decisive negative control against a whole-source Keller interpretation.

## Limitations and next test

The source is singular, the support curve is smooth, and the non-etale scheme is nonreduced; these are different properties. This result closes the proposed inference from normality, finiteness and smooth reduced ramification support alone. An argument for smoothness of the actual finite normalization still needs additional hypotheses or global information. No properness, degree-one or JC2 conclusion follows, and no stronger source-realization claim has been reviewed.

## OPENS RAISED

None. The existing actual-normalization smoothness and whole-source gaps retain their scopes.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `68e87443925f50914a6cbb858d9d2f061dbda8b3` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5598`.
- Body SHA-256:
  `152e84b2d33ff3d5728896958447515bec95c9df0133779e33c2946be2b27b6a`.
- Frozen basis: `68e87443925f50914a6cbb858d9d2f061dbda8b3`.
