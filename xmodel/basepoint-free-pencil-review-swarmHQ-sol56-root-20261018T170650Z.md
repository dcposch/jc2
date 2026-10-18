# Independent FIRST and integration: basepoint-free target-pencil primitivity

Reviewer: swarmHQ retained native gpt-5.6-sol-assigned independent seat.
Integration/transcription: swarmHQ ROOT; original producers ROOT/Astra-assigned.
Assignments are recorded; hosted model identities were not independently verified.
Review completion: 2026-10-18 17:06:50 UTC.
Basis: 8ece8987819338505aef9103f82a95243944b7c1.
Evidence tier: MANUAL, with the producer's exact named classical/campaign imports.
Lifecycle: PROMOTED for BASEPOINT-FREE-PENCIL-1 and its stated conditional corollary.
External novelty: UNKNOWN. This is not a resolution of JC2.

## Frozen reviewed input

[Producer report](basepoint-free-pencil-swarmHQ-root-astra-20261018T170044Z.md),
148 lines, 8088 bytes, SHA256
2756b24088f46f3948932f35b3d45e9c07aa4d6061707b24069721144404f5f2.
Its body SHA256 is 13c84910985de858896689d0cdbf8106303114462c741b84c231a62f5abcd5c9.
The 707-byte artifact manifest SHA256 is
9450b7560581b9db8f4fc01be5830e1909461585aadbbd877b89f4a86386bc5c.
The producer was author-complete and canonically sealed before the reviewer read it.
The whole report and manifest were read; artifact verification passed and pre/post
hashes and read-only modes matched. Producer bytes have not been rewritten.

## Exact promoted statement

Over C, let F:A2_source -> A2_target be polynomial with nonzero constant Jacobian.
Let f:A2_target -> P1 be a MORPHISM with geometrically integral rational generic
fibre. Then C(f), pulled back by F, is algebraically closed in C(source).
No source-generic-fibre rationality assumption is made. No invariance of f under F
is assumed or concluded. The affine-basepoint-free hypothesis is essential to this
argument's admitted scope. The conclusion is primitivity, not automorphy of F.

## Independent hostile review

The reviewer independently reconstructed the following argument and found no defect
at the named import scope. Put k=C(f), K=C(target), L=C(source). For finite E/k in L:

1. Geometric integrality makes K/k regular, hence K and E linearly disjoint and
   [KE:K]=[E:k]. The normalization Z of the target in M=KE is finite and normal.
2. The smooth projective curve cover corresponding to E/k is etale away from
   finitely many base values. Its base change along f is then finite etale and
   normal, with generic field M. Uniqueness of normalization shows that every
   branch divisor of Z->A2_target is vertical for f.
3. Independently, F is finite etale over A2_target minus its nonproper-value set S_F.
   On this open it is the normalization in L, so the intermediate normalization
   in M is finite etale. Thus every branch divisor is contained in S_F.
   No claim that F is globally finite is used here.
4. Such a divisor is an entire irreducible component of S_F and a reduced affine
   fibre component of f. The accepted genus-zero fibre theorem makes it smooth
   rational on the ACTUAL affine target, because f has no affine basepoints.
5. Polynomial parametrization of S_F supplies a dominant A1 map to that curve.
   A nonconstant unit on a smooth rational affine curve with at least two punctures
   would pull back to a nonconstant unit on A1. Thus it has one puncture and is A1,
   contradicting the accepted Keller no-A1-component theorem.
6. Purity applies: Z is normal, the target is regular, and characteristic zero
   gives generic separability. With no branch divisor, Z->A2 is finite etale.
   Triviality of connected finite etale covers of A2_C gives degree one, hence E=k.

The smoothness step was applied only after verticality, not to arbitrary resolved
or basepointed pencils. Neither a gcd of whole-fibre multiplicities nor preservation
of source-fibre genus is assumed. The reviewer did NOT re-prove all imported source
theorems; in particular the genus-zero fibre lemma and the polynomial-parametrization/
no-A1 package retain precisely the producer's previously accepted import scope.

## Donor corollary and its limit

For D_R(s,t)=(R(s),t/R'(s)), deg R>1, permit an arbitrary birational target
transformation T, even with nonconstant Jacobian. Suppose the expression f for
the old first coordinate on the NEW affine target extends to a morphism to P1.
Its generic fibre is geometrically integral rational since its target field is
C(p,q)=C(p)(q). Then no finite dominant rational source substitution S can make
T composed with D_R composed with S a whole-plane polynomial Keller map.

The independent field-direction check is decisive: S injects C(s,t) into the
new source field, and the pulled-back C(f) is C(R(s)); the proper finite extension
C(R(s)) subsetneq C(s) remains inside that source field. This contradicts the
theorem, without requiring source-fibre genus to survive S.

This does NOT exclude all birational target changes: the stated no-affine-basepoint
condition on f must be supplied. General donors and the actual finite-normalization/
outside-boundary descent problem remain unresolved. The prior same-pencil invariant
theorem and the earlier constant-J target filters retain their separate scopes.

## Replay, controls and binding integration

Desk-only; no CAS or new external source acquisition. The exact sealed producer and
manifest were checked with ops/artifact_finalize.py verify. The three strongest
scope attacks were the two different branch containments, applying fibre smoothness
on the actual affine plane, and reversal of the donor's source-field inclusions;
all were resolved as above. Affine-basepoint pencils remain an explicit excluded
scope control, not a claimed counterexample. FALLACY-v2 applies; no exit-price claim.

ROOT accepts only the exact statement and corollary above as PROMOTED/MANUAL at the
named imports. No existence theorem for an eligible pencil or general Keller normal
form follows. No new descendant, classification programme or global claim is implied.

## OPENS RAISED

None. Existing global questions and excluded stronger conclusions are not new opens.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `8ece8987819338505aef9103f82a95243944b7c1` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6171`.
- Body SHA-256:
  `c8814958c5b5cca2abec325d4b24df4028d2c3ac9be3ce5bb80793f9547ef65f`.
- Frozen basis: `8ece8987819338505aef9103f82a95243944b7c1`.
