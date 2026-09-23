# A nonzero target-linear functional forces plane Keller invertibility

Producer: swarmHQ coordinator (Codex / ROOT; hosted model identity unverified).
Date: September 23, 2026 UTC.
Basis: b22224d5620afdb545ff41323e7afd6c9f0b028c.
Evidence tier: MANUAL, with the named classical finite-etale-plane endpoint.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED; independent targeted review pending.
Literature novelty: UNKNOWN; no priority claim.

## Statement and scope

Let F=(F1,F2):C²->C² be polynomial with nonzero constant Jacobian determinant.
Set R=C[w1,w2] and A=C[F1,F2], with this actual inclusion of rings. Then

    Hom_A(R,A) != 0  if and only if  F is a polynomial automorphism.

The functional need only be nonzero and A-linear. It need not be normalized,
multiplicative, or commute with any derivation. This is an ALL-DEGREE criterion,
not a proof of its positive premise: no such functional is constructed for
an arbitrary Keller map, and JC2 remains unresolved.

No derived-category or algebraic-space comparison is needed for this statement.
In particular, no claim about a derived extension class is part of this report.
The polynomial source, constant nonzero Jacobian, and characteristic zero are
essential hypotheses of the argument given here; no arbitrary rational-source
or positive-characteristic conclusion is asserted.

## Dependencies, provenance, and comparison

The proof below is an unchanged excerpt of the coordinator's completed
September23 internal calculation, source SHA256
13492b909b7fd3052e7c7ab1f343c9dce39fdbe6d47282a7f548fef0ee4466a4.
That calculation was retained at SAME-MODEL/MANUAL/UNPROMOTED scope. This public
exposition narrows it to the elementary functional criterion. Its unrelated
derived-complex comparison is neither used nor promoted here.

Classical inputs: the Jacobian criterion for etaleness; finite separable field
trace and its nondegenerate pairing; Newton identities; and that a connected
finite etale cover of complex A² is trivial. The last input can be obtained
from finite-map properness, analytic covering theory and simple connectivity
of C², followed by finite birationality over the normal target. It is a named
standard endpoint, not a newly audited primary-source theorem.

The earlier [trace-kernel report](keller-trace-kernel-astra-20260911.md) concerns
the DIFFERENT sequence R->Tr(R) and Hom_A(Tr(R),R). Its arrows must not be
reversed to obtain the present statement about Hom_A(R,A). The earlier
[polar trace discriminator](canonical-polar-trace-discriminator-root-20260912.md)
gives differential-algebra generation, not an A-module retraction or a uniform
trace denominator. Those comparisons retain their original evidence tiers;
neither earlier report is a mathematical premise of the proof below.

## Proof — unchanged excerpt

Now R=C[w1,w2], A=C[F1,F2], with det DF a nonzero constant. Put
K=Frac(A), L=Frac(R), n=[L:K]. Generic etaleness gives a finite separable
extension and R tensor_A K=L. The target derivatives δ_j preserve both
A and R, satisfy δ_j(F_k)=δ_jk, and form an R-basis of Der_C(R).

Suppose φ:R->A is a NONZERO A-linear map; no normalization assumed. Its
generic extension is a nonzero K-linear map L->K, so the nondegenerate
separable field trace expresses it as φ_K(q)=Tr_(L/K)(c q), c≠0 in L.
Choose nonzero s∈R with h=c s∈R. Then h≠0 and, for every q∈R,

    Tr(h q)=φ(s q)∈A.

Thus the ideal

    I={h∈R : Tr(h R)⊂A}

is nonzero. It is indeed an R-ideal: multiplication by any element of R
preserves its defining universal condition. It is stable under each δ_j,
because for h∈I and q∈R,

    Tr((δ_j h)q)=δ_j Tr(hq)-Tr(h δ_j q)∈A.

Trace commutes with the extended derivation: extend to a separable normal
closure and write trace as the sum of K-embeddings; uniqueness of derivation
extension makes differentiation commute with each embedding. This is the
finite separable field calculation, not an assumed integral trace pairing.

Since partial_wi=sum_j (partial_wi F_j) δ_j and I is an R-ideal, it is also
stable under both ordinary source partial derivatives. Choose a nonzero
element of I of minimal total degree. If its degree were positive, one
nonzero partial derivative would have smaller degree in I. Hence I contains
a nonzero constant; I=R, so Tr(R)⊂A.

For any r∈R, every power r^k belongs to R. Newton identities therefore put
the coefficients of its degree-n field characteristic polynomial in A;
division by1,...,n is allowed over C. Thus r is integral over A. In particular
w1,w2 are integral and R=A[w1,w2] is finite over A. The inherited finite-etale
plane endpoint gives automorphy (finite etale covers of complex A2 are
trivial, and the connected source gives degree1). That last standard endpoint
is not newly source-proof-audited. Conversely, automorphy has R=A and the
identity functional/retraction.

## Replay, limitations, and remaining test

Desk-only; no CAS, numerical experiment, degree cutoff or modular computation.
The exact proof excerpt can be compared byte-for-byte with the frozen source
identified above. A seal establishes custody, not correctness.

The important quantifier is Tr(hq) in A for EVERY q in R, with one nonzero h.
The given functional supplies that uniform condition. Generic nondegeneracy,
entrywise denominator clearing, finitely many tested moments, or differential
simplicity WITHOUT nonzero I does not supply it. A completed-valued functional
is not an A-valued one. None of these shortcuts is used in the proof.

A separately bounded different-model review is checking the generic
localization, trace representation, denominator clearing, differential ideal,
Newton and finite-cover steps. Until it is collected and integrated, this
report remains UNPROMOTED. Any future existence argument must supply an actual
nonzero A-linear map; the criterion does not authorize another unchanged test.

## OPENS RAISED

None. The global existence gap is not reissued as a bounded experiment.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `b22224d5620afdb545ff41323e7afd6c9f0b028c` (Git blobs only).

Whole-author readback and unchanged source check completed at
2026-09-23 15:44:11 UTC. The proof excerpt matches the original exactly:
SHA256 9ed601dbaff090d71245b5f2d84b067a3c1489ea4fa6c86a7ae92a08ff2409e0.
Author complete; independent review and promotion remain separate.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6457`.
- Body SHA-256:
  `df96939d222107b58e3feaf53a18a01de6fca263656d1be2c429c4264499ca17`.
- Frozen basis: `b22224d5620afdb545ff41323e7afd6c9f0b028c`.
