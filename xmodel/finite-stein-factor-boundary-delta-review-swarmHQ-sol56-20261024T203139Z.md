# Delta review: conditional finite Stein factor and boundary

Reviewer: swarmHQ (explicitly requested gpt-5.6-sol; actual hosted identity and cost unmeasured).
Date: 2026-10-24.
Reviewed contribution commit: `686c131b32ae21cea7a3e8a2bc782203f9106990`.
Reviewed artifact: `xmodel/finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md`.
Artifact SHA-256: `6901a645eac8e1a5044b3de7727e06e9b0d5385f8bafa9905166df22b87e3969`.
Producer: swarmHQ coordinator (requested gpt-6-astra).
Evidence tier: MANUAL delta review of a conditional MANUAL theorem.
Lifecycle: REVIEWED / UNPROMOTED; ROOT controls any promotion.

## Verdict

`CONFIRMED` at the exact conditional scope printed in the reviewed artifact.
The final public text faithfully incorporates the premise clarification and the
limitations checked in the earlier Sol review. It makes no stronger mathematical
claim than the already reviewed candidate.

This delta review is not a fresh blind review. The earlier gate's required HQ
history preview exposed one line stating the prior Astra verdict after the Sol
mathematical audit but before its first saved verdict. That process defect and
the earlier history-preview/row-limit defects remain part of the review custody.
The optional Astra report was not read.

## Exact claim and premise comparison

The public theorem still concerns the actual analytic Stein factor
`Z -> W -> Y` of a resolved polynomial Keller iterate. It explicitly retains:

- a smooth projective rational source compactification with the given `A2` open;
- a primitive irreducible target boundary and the genuine ideal equality
  `omega_Y = O_Y(-B)` supplied by the meromorphic volume;
- a resolution `pi` isomorphic over all of the source `A2`;
- the unique source extension represented by the source boundary divisor, with
  ramification `N` and residue degree one.

The conclusions remain exactly that `W` has rational singularities everywhere
and that its unique reduced boundary `C` maps scheme-isomorphically to `B`, with
both curves of arithmetic genus one. The report does not identify a nonreduced
pullback ideal.

## Proof-scope audit

The open-immersion step uses etaleness on the full source and the birational
exceptional-locus theorem. The canonical-section argument correctly makes the
source-valuation identification load-bearing before applying the negative order
of source polynomials. Compact analytic duality and Leray then kill
`R^1 r_* O_Z`, including at infinity.

The boundary calculation uses the genuine canonical ideal to obtain
`p_a(B)=1`. Reflexive Hom and codimension-one Cohen--Macaulay adjunction yield
`0 -> omega_W -> O_W(R) -> omega_C -> 0` without Cartier or Gorenstein
assumptions, so `p_a(C)>=1`. The finite birational cokernel formula gives
`p_a(C)=1-length(Q)<=1`, hence `Q=0` and the reduced scheme isomorphism.

The text expressly allows effective `R` to remain nonzero and does not assume
target projectivity, Q-Cartierness, flatness, log singularities, `W=Y`, a finite
self-germ, properness, descent, omitted-affine-boundary exclusion, or attachment
of these premises to every Keller map. The named dependencies are declared as
standard imports rather than source-paper proofs.

## Comparison and replay

Desk-only delta replay: I verified the producer manifest and canonical artifact
before reading all 125 LF-delimited report lines, then compared the text with the
previously checked 82-line candidate and 9-line binding clarification at their
frozen hashes. No new computation, source read, history search, or mathematical
branch was used. The public formatting adds exposition, dependencies, replay,
limitations, and collision metadata without changing the theorem.

## Limitations

This confirms only the explicit conditional implication. It supplies no proof
that a hypothetical noninvertible Keller map satisfies the compactification,
canonical-ideal, or unique-valuation premises, and it leaves the omitted boundary
and descent problems open. No novelty or JC2-resolution claim is endorsed.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `686c131b32ae21cea7a3e8a2bc782203f9106990` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4245`.
- Body SHA-256:
  `cc429bba65d74f97cb8a783947c3ac2a140ea84f30f47663280e98bb5d9a3b89`.
- Frozen basis: `686c131b32ae21cea7a3e8a2bc782203f9106990`.
