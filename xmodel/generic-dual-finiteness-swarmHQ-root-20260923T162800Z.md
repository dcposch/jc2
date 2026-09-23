# A nonzero dual detects finiteness for a generically finite domain algebra

Producer: swarmHQ coordinator (Codex / ROOT; hosted identity unverified).
Date: September23,2026 UTC.
Basis: 63639a420f32da31e6f5c52284529723d4eb2db6.
Evidence: MANUAL / PRODUCER-CHECKED. Lifecycle: UNPROMOTED; hostile review pending.
Literature novelty UNKNOWN; no priority claim.

## Exact statement

Let A be a Noetherian domain and A subset R an inclusion of commutative
domains with the same identity. Put K=Frac(A), L=Frac(R), and assume
n=[L:K] is finite. No finite-generation hypothesis on R is assumed. Then

    Hom_A(R,A) is nonzero if and only if R is a finite A-module.

The implication does not require separability, characteristic zero,
normality, smoothness, a Jacobian condition, or compatibility with derivations.
This is a finite-module statement, NOT an automorphism theorem in this scope.

## Direct proof

Set S=A minus {0}. The localization S^-1 R embeds in L, contains K,
and is algebraic over K. Any nonzero element z in this algebra has an
algebraic equation over K with nonzero constant term (its minimal
polynomial); solving that equation for z^-1 puts the inverse in K[z].
Thus S^-1 R is a field, and since it contains R it equals L.
In particular R spans L over K, so we can choose b_1,...,b_n in R
forming a K-basis of L.

Suppose phi:R->A is a nonzero A-linear map. Localizing gives a K-linear
map lambda:L->K, lambda(r/s)=phi(r)/s. It is nonzero because a nonzero
value phi(r) stays nonzero in the fraction field. Define

    T:R -> A^n,   T(r)=(phi(b_1 r),...,phi(b_n r)).

All coordinates lie in A since b_i r belongs to R; T is A-linear.
If r is nonzero and T(r)=0, then K-linearity and the basis imply
lambda(z r)=0 for every z in L. Multiplication by nonzero r is a
bijection of the field L, so lambda would vanish on L, a contradiction.
Therefore T is injective. Since A is Noetherian, every submodule of the
finite A-module A^n is finitely generated. Hence R is a finite A-module.

Conversely, suppose R is finite as an A-module. Choose any nonzero
K-linear functional lambda:L->K and finite A-module generators r_j of R.
There is a common nonzero denominator d in A for the finitely many
lambda(r_j). Then d lambda restricts to an A-linear map R->A.
This restriction is nonzero since R spans L and lambda is nonzero.
This proves both implications.

## Essential scope check

The generic domain/field hypothesis cannot simply be replaced by a reduced
algebra of the same generic rank. For A=k[t], take R=A times A[1/t],
with A embedded diagonally. Its generic algebra is K times K, and projection
onto the first factor is a nonzero A-linear R->A. Nevertheless R is not
finite over A: otherwise its quotient A[1/t] would be finite and hence
integral over A, whereas 1/t is not integral over k[t]. In a monic integral
equation, multiplication by its highest power of t would give 1 in (t).
This single manual boundary check is not a construction-search family.


## Relation to the campaign

For a complex polynomial Keller inclusion A=C[F1,F2] subset R=C[w1,w2],
generic finiteness gives the field hypothesis. The lemma gives finite R/A;
the already accepted finite-etale-complex-plane endpoint gives automorphy.
Thus this is a shorter proof of the SAME
[nonzero target-dual criterion](nonzero-dual-criterion-swarmHQ-root-20260923T154100Z.md),
whose [first integration](nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md)
records its promotion and endpoint scope. It does NOT supply a nonzero
functional for an arbitrary Keller map. JC2 remains unresolved.

The difference is structural: multiplication and a nonzero functional embed
the entire domain into a finite free module, without trace, differential
simplicity, or Newton identities. The wider algebra statement has neither a
Jacobian nor a separability hypothesis; automorphy does not follow in that
generality. The former characteristic-zero Keller proof remains valid and
is not rewritten or retracted.

The older [trace-kernel calculation](keller-trace-kernel-astra-20260911.md)
concerns the different arrows Hom_A(Tr(R),R). Generic field duality there
does not construct the A-valued functional required here.

## Evidence, limitations, and replay

The exact statement, direct proof and essential scope check above are an
unchanged excerpt of the completed producer calculation, full source SHA256
262bfbe318acc2d8880378397d986e620e6e1424401498fb3ffd7376edbedb4a.
Both frozen campaign and operational histories were compared before admission;
the nearest actual calculation was the former differential-ideal proof.
No exhaustive novelty search or literature attribution is claimed.

Desk proof only: no CAS, numerical experiment, degree cutoff, new source
import, or computational certificate. The key is ONE given functional on
ALL of R. Clearing denominators only on finite test elements does not
produce it. In the converse, finite module generation is an explicit premise.
A formal or completed-valued functional is not automatically A-valued.

A different-model hostile review is checking localization, the field basis,
nonvanishing, injectivity, Noetherianity, converse, and the reduced non-domain
control. The wider lemma must not be treated as promoted until that review
is collected and integrated. No positive-premise research or descendant is
licensed by this exposition.

## OPENS RAISED

None. The missing functional is not reissued as a bounded experiment.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `63639a420f32da31e6f5c52284529723d4eb2db6` (Git blobs only).

Whole-author proof readback completed September23,2026 16:29:24 UTC;
the mathematical excerpt was compared unchanged against the frozen producer.
No novelty or correctness claim follows from the collision result.
Author complete; independent review remains pending.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5927`.
- Body SHA-256:
  `e07f3572c62b613edf23b6fae3b56e2c8d7d31d73817d9e3d310836f2965cd53`.
- Frozen basis: `63639a420f32da31e6f5c52284529723d4eb2db6`.
