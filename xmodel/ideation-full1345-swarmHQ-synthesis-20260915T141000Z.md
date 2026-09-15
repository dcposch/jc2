# FULL1345: two scope corrections, no new closing mechanism

Producer: swarmHQ ROOT (gpt-6-astra), with independent Astra and
gpt-5.6-sol blind assessments and subsequent cross-examination.
Date: September15,2026. Common scientific basis:
a0396ad75966f65d715102c6a10531d83d2c6abb; publication basis:
5cbf8fcd797f5a22d3070c46e6dc7b2ff31c277f.
Evidence: MANUAL/DOCUMENTARY strategy synthesis; PRODUCER-CHECKED,
UNPROMOTED. No new accepted global theorem. JC2 is unresolved.

## Outcome and disagreement

All46 dispositions in the [historical research map](../history/APPROACHES-through-20260915.md)
remain unchanged. No complete characteristic-zero polynomial counterexample,
new actual-source closing implication, or admissible new experiment emerged:
NO_NEW_MECHANISM / NO_TEST. This is not mathematical exhaustion.

ROOT and Sol prefer the next genuinely new complete-construction proposal
over another equivalent normalization endpoint. Astra keeps actual-source
geometry first, construction second. This is a real allocation preference,
not a theorem disagreement or a majority vote. Both fronts remain essential.
Uniform descent, non-Galois blocks, primitive sources and complete F10 retain
their distinct unresolved interfaces; no accepted bound is reverified here.

The new comparison produced two useful corrections to proposed methods:
the generic-automorphism degeneration in Sol's first card is impossible
under its stated hypotheses; its second card's formal-idempotent lifting
test is automatically positive. Neither observation supplies a JC2 proof.

## 1. A generic polynomial inverse cannot develop a pole at a dominant fiber

This corrects Sol's construction card, not the broader construction avenue.
Let \(V=\mathbb C[s]_{(s)}\), \(K=\mathbb C(s)\), and
\(F\in V[x_1,\ldots,x_n]^n\). Assume \(F\) has a polynomial inverse
\(G\in K[u_1,\ldots,u_n]^n\), and its special fiber \(\bar F\) is dominant.
Then \(\bar F\) is a polynomial automorphism.

Indeed, suppose an inverse coordinate \(G_i\) has a coefficient pole at
\(s=0\). Choose the least \(m>0\) such that \(H=s^mG_i\in V[u]\).
At least one coefficient of \(H\) is a unit, so \(\bar H\ne0\).
The inverse composition \(G_i(F)=x_i\) gives
\[
H(F)=s^m x_i,\qquad \bar H(\bar F)=0.
\]
Dominance makes \(\mathbb C[u]\to\mathbb C[x]\), \(u\mapsto\bar F\),
injective, a contradiction. Thus all coordinates of \(G\) lie in \(V[u]\);
both composition identities specialize, giving an inverse for \(\bar F\).

In characteristic zero a constant nonzero special Jacobian implies
dominance. Hence an arc with a polynomial automorphism over \(\mathbb C(s)\)
cannot specialize to a noninvertible Keller map. The argument needs no
inverse-degree estimate, fixed degree bound, or properness theorem.

Sol had classified the inverse-pole possibility as the existing formal
algebraization gap. That identification was too weak: the literal proposed
arc is already excluded by the displayed identity. The nearby
[September13 formal-deformation discussion](../notes.md#2026-09-13-1926-utc-formal-deformation-discriminator-known-equivalent-gap)
concerns inverses over all separate nilpotent truncations. Those do not
supply one polynomial inverse over \(\mathbb C(s)\), so the argument above
does not solve that problem. Nor does it show that the automorphism locus
is dense, or that every coefficient component consists of automorphisms.
No novelty is claimed for this elementary specialization argument.

## 2. Formal idempotent lifting is not the missing step

For a commutative ring \(C\), the maps
\(C/(s^{m+1})\to C/(s^m)\) have nilpotent kernels. A central-fiber
idempotent therefore has unique lifts at every level, automatically
compatible, and hence a unique idempotent in \(\varprojlim_m C/(s^m)\).
This uses no smoothness. The standard nilpotent-lifting statement and
proof are in [Stacks, Lemma10.32.6](https://stacks.math.columbia.edu/tag/00J9).

For the actual Keller difference family, use a suitable general nonzero
direction \(a=(a_1,a_2)\), and the literal ring
\[
C_a=\mathbb C[s,p_1,p_2,q_1,q_2]/
(F_1(q)-F_1(p)-sa_1,\ F_2(q)-F_2(p)-sa_2).
\]
The Jacobian in \(q\) is invertible. Thus this algebra is smooth, in
particular flat, over \(\mathbb C[s]\). The accepted
[branch-disjointness criterion](disjoint-branch-translates-swarmHQ-root-20260915T093700Z.md)
gives integral generic fibers for a suitable general direction; this is
not a statement for every \(a\), notably not \(a=0\).
Flatness embeds \(C_a\) into its generic-fiber domain, so \(C_a\) is a domain.

If the hypothetical Keller degree is greater than one, the diagonal
component of the zero fiber has a nontrivial idempotent \(e_0\).
Its formal lift exists. What would force a contradiction is descent of
that lift to an idempotent of the original domain \(C_a\).
The completion may split even though \(C_a\) is a domain. Accordingly,
Sol's proposed test asking whether \(e_0\) lifts to the completion has
an automatic answer and cannot discriminate JC2. The unresolved issue
is polynomial descent of the formal splitting, not finite-stage
compatibility; no natural reverse map from completion to the original
ring has been supplied. No new lifting, relative-de-Rham or control-family
investigation is earned by rephrasing that same missing implication.

Complete along the ideal \((s)\). If localizing first, localize the base
\(\mathbb C[s]\) at \((s)\); that ideal need not be prime in \(C_a\).
Choosing one source prime could discard the other special-fiber components.
Do not identify the completed generic ring with the original polynomial
generic fiber. The same distinction between formal lifting and bounded
polynomial representatives already appears, at its separate AS109 scope,
in the [August24 secant review](secant-as109-review-grok-20260824.md).

This formal ring statement must not be confused with the different
question of descending the finite-normalization separability idempotent
from \(N\otimes_A R\) to \(N\otimes_A N\). Astra's second card returns to
the [existing trace-duality gap](source-boundary-duality-swarmHQ-astra-20260914.md):
its trace-dual module lies in \(R\), not necessarily in \(N\).

## What survives from the changed packet

The four accepted additions remain useful at their recorded scopes:

| Input | What it supplies | What it does not supply |
| --- | --- | --- |
| [Branch-disjoint translates](disjoint-branch-translates-swarmHQ-root-20260915T093700Z.md) | Integral generic translated fibers; the finite-exception refinement retains its named source qualification | Connectedness at translation zero |
| [Tensor constants](tensor-constants-swarmHQ-root-20260915T111600Z.md) | Exact constants and tensor-map image \(\mathbb C(p)[F(q)]\) | Generation of the full source algebra |
| [General source lines](source-line-translates-swarmHQ-root-20260915T121300Z.md) | Integral generic curve fibers for general fixed complex lines | A generic affine line, a finite exceptional set for that line, or complete flows |
| [Marked-root fixed slices](marked-root-fixed-coefficient-slices-swarmHQ-root-20260915T124800Z.md) | Whole-scheme classification of the specified fixed-high-coefficient slices | An exclusion of arbitrary target constraints, donors, or polynomial substitutions |

The first three describe the same actual-source obstruction from different
directions, without supplying a new specialization or generation theorem.
The fourth excludes a particular extraction: the extra plane components
have affine output coordinates, so arbitrary polynomial substitutions
pass through their own plane Keller pair. It does not classify all donors.
See [AUDIT](../AUDIT.md) for accepted evidence tiers and review qualifications;
this synthesis does not independently re-audit their full dependency proofs.

## Selection consequence

Do not renew these exact inverse-arc, idempotent, trace-square or fixed-slice
tests under another name. A new construction needs an entire source and
its acceptance map; a new proof needs an additional condition derived from
the literal \(\mathbb C[F]\subset\mathbb C[x,y]\), with an explicit place
where that condition removes the known obstruction. A family name,
necessary chart, modular point or formal solution does not provide either.
Other genuinely different constructions and source mechanisms remain open.

No new computation or software mechanism is proposed. The history-first
screen remains useful, but no measured speedup or provider comparison is
claimed. Independent coverage is DEGRADED because Fable did not participate;
that omission does not establish a provider or credit failure.

## Review and provenance

The [ROOT blind](ideation-full1345-swarmHQ-root-20260915T134700Z.md) was
sealed before invitations. Astra and Sol worked from the same frozen
scientific packet without reading peers; both terminal submissions were
collected before cross release. ROOT's two objections were written after
its blind and are not represented as independent blind discoveries.

Sol and Astra each independently CONFIRMED the two corrections, including
the actual-family flatness/domain argument. Sol withdrew its first card
at its literal scope and acknowledged that its second test was automatic.
Astra additionally required the ideal/base-localization wording above
and recovered the earlier formal-versus-polynomial history. Neither
reviewer found a surviving new closing test. Their endorsements concern
these exact arguments, not blanket FIRST on the four accepted dependencies
or a promotion of this strategy report.

All required common strategy/producer inputs were read or whole-read
revalidated as described in the blind submissions. Historical searches
were scoped and not exhaustive. ROOT read the whole statement and both
proofs of Stacks00J9; the inverse-limit application is elementary inference.
The inverse-pole proof is supplied above, not attributed to an unread
paper. No scientific code was executed for these arguments.

Frozen scientific basis and common packet retain the four accepted
additions, source-access qualifications, and all46 dispositions. The
publication basis differs only by banking ROOT's sealed blind. Native
terminal texts and cross provenance are retained by swarmHQ; only useful
mathematics and its scope are published here.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Canonical scan completed exit0 after both cross authors were terminal.
This lexical result does not establish novelty or exhaustive coverage.
The round's mathematical synthesis was completed September15 at14:16:25
UTC; final authoring and publication followed. No later operational event
is represented as additional mathematical research.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10744`.
- Body SHA-256:
  `0023b19224343e963a5ac2733eba46d8ebfe180773d326cf7db7ebddfde3f0d4`.
- Frozen basis: `5cbf8fcd797f5a22d3070c46e6dc7b2ff31c277f`.
