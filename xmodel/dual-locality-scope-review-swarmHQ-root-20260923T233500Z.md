# Intermediate rings and local splittings: two scope corrections

Producer: swarmHQ ROOT (gpt-6-astra), with native Astra cross-examination.
Assessed assertions: independent Fable5.1 portfolio submission, unpromoted.
Date: 2026-09-23 UTC.
Basis: 7bc4d1adcc88c65acc8d95b18f8f1b8470697bf5.
Evidence tier: MANUAL scope review, with explicitly conditional named imports.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED. No new theorem promotion or JC2 solution.

## Statement and dependencies

For an actual complex polynomial Keller map F, write
A=C[F1,F2] subset R=C[w1,w2]. The accepted
[nonzero-dual criterion](nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md)
and its [generic proof](generic-dual-integration-swarmHQ-root-20260923T163500Z.md)
say that Hom_A(R,A) is nonzero exactly when F is invertible. The generic
lemma applies to a generically finite DOMAIN algebra over a Noetherian domain;
it equates nonzero dual with module finiteness. It does not construct the dual.

This review corrects two extrapolations made in the Fable submission:

1. Monicity of F1 in w1 does not make C[F1,w2] an intermediate A-algebra.
2. A nonzero local punctured-branch extension does not force the diagonal
   unit extension of the full local pushforward to be nonsplit.

The elementary calculations below are self-contained. The global normalization,
regular-holonomic middle-extension and shriek-duality descriptions are NOT
newly primary-verified here. Where used, their conclusions remain conditional
on the stated setup. Agreement between two Astra instances is not different-
model FIRST for these corrections; no promotion is requested. This review
attacks Fable's unpromoted assertions, not either accepted dual theorem.

## 1. The proposed intermediate ring need not contain A

The assessed argument chooses A1=C[F1,w2], observes that R is finite free
over A1 when F1 is monic in w1, and proposes composing a functional down
using Hom_A(A1,A). This requires A subset A1, which was not shown.

Consider the Keller automorphism

    F(x,y)=(x^2+y,-x),   det JF=1.

Its inverse is x=-F2, y=F1-F2^2. Thus A=R=C[x,y], whereas

    A1=C[x^2+y,y]=C[x^2,y].

The latter excludes x: its elements are invariant under x->-x. R is indeed
free over A1 with basis1,x, but A1 is not an A-module under the proposed
inclusion. Consequently Hom_A(A1,A) is not defined as asserted. This is an
exact counterexample to the intermediate-ring inference, NOT to JC2.

The valid ring is B=A[w2]. Then A subset B subset R. Monicity of F1 in w1
gives a monic equation for w1 over B, hence R is finite over B. The accepted
generic lemma applies to B and gives

    Hom_A(B,A) != 0  iff  B is finite over A
                    iff  w2 is integral over A.

This repairs the particular tower while retaining the unproved integrality
premise. It neither constructs a functional nor excludes every intermediate-
ring method. Finite field rank also does not supply a uniform denominator
for the images of every source monomial under a generic functional.

## 2. A local punctured-branch class is not the diagonal extension class

Let B=C[g,h] and P=B directsum B[1/g], with componentwise differentiation.
Embed B diagonally by i(b)=(b,b). Projection to the first factor is a
B-linear AND differential-linear retraction. Explicitly,

    P/i(B) is isomorphic to B[1/g], via (b,c) -> c-b,

so the diagonal unit extension splits. Meanwhile P/B^2=B[1/g]/B, and the
standard extension

    0 -> B -> B[1/g] -> B[1/g]/B -> 0

does not split. Indeed a B-linear map B[1/g]->B sends1 to an element divisible
by every g^m, hence to zero; it is then zero on each g^(-m). Thus a nonzero
punctured-branch extension is compatible with a split diagonal extension.

This is the reduced-product type already used to delimit the domain hypothesis
of the generic-dual lemma. P is NOT a domain or an actual nonautomorphic Keller
source. It tests the claimed local inference, not the global conjecture.
The same projection works with a local analytic target ring O in place of B:
M=O directsum O(*g), with diagonal unit, has a local differential retraction.

The Ext distinction can be stated abstractly. In an abelian category, suppose

    K=O directsum K' subset M,   Q=M/K,   N=M/O.

The unit-extension class e in Ext^1(N,O) restricts to zero on K', since its
pullback is K. The long exact sequence gives a preimage e' in Ext^1(Q,O).
Uniqueness follows if Hom(K',O)=0. However, global vanishing of this Hom
need not persist after restriction to an analytic split neighborhood. The
map Ext^1(Q,O)->Ext^1(N,O) need not remain injective there. A nonzero local
e' therefore need not imply nonzero local e.

## 3. Why retained sheets matter in the proposed Keller local picture

The smooth target T=Spec A and the finite normalization Y of T in Frac R
are different spaces. The assessed D-modules and extension groups are on T,
not the possibly singular Y. A cyclic ramification model (g,v)=(u^e,v)
also requires an appropriate analytic or etale/strict-henselian splitting
away from exceptional points. It is not a global Zariski coordinate identity.
One must include retained sheets and residue-field degrees: a global omitted
divisor of residue degree f is not automatically one trivial O_C summand.

Retained sheets are relevant to an actual Keller map at generic points of
every target curve. Its image is Zariski open, since the map is etale. It
cannot omit an entire irreducible target curve V(q): otherwise q(F1,F2)
would be nowhere zero on C^2 and hence a unit of C[w1,w2]. Dominance makes
A->R injective, so the nonconstant q cannot pull back to a constant.
Thus the image meets the curve, and openness gives a nonempty open subset
of that curve contained in the image. This applies in particular to a
nonproper-curve component, if one exists.

At such an image point, the analytic inverse function theorem provides a
local inverse sheet s:U->C^2 with F composed s=id_U. Evaluation along it

    R tensor_A O_U -> O_U,   r tensor a -> (r composed s)*a,

retracts the unit; differentiation is compatible by the chain rule. This
is a statement in the analytic local setting. It does NOT produce a map
R->A with polynomial values, and after a split base change the generic
field/domain hypothesis used by the global lemma need not be retained.

Accordingly the assessed assertion that the functional obstruction is
locally nonzero along every nonproper component is not supported by its
split-local calculation. This correction does not make a Zariski-local or
global polynomial splitting claim. Nor does it refute a correctly formulated
GLOBAL boundary-Ext relocation with global connected-monodromy hypotheses.
It rejects the transfer of that global uniqueness argument unchanged to the
split local setting, and the resulting purported ban on near-boundary methods.

## Remaining gaps and exact exclusions

No global nonzero target-linear functional, polynomial counterexample, invariant
structure or new closing test is supplied. A local method may still interact
with global descent; this review proves no classification of possible proofs.
The source and target rings, topology and class being split must be specified.
Likewise the accepted invariant-pencil/foliation/web implications are sufficient
criteria for automorphy, not assertions that every automorphism has those
structures. Formal families are not proved the only possible construction
source, and existing donor exclusions retain their individual hypotheses.

The portfolio review found no new qualifying mechanism. This is a bounded
selection outcome, not universal exhaustion. No automatic successor, repeated
moment test, source retry or accepted-bound reverification is justified here.

## Replay, provenance and negative controls

Desk-only. No scientific code, CAS, random seed, finite-field test or new
primary-source retrieval. Check the displayed inverse/determinant, the even-x
subring, diagonal projection, localization Hom calculation and analytic
evaluation directly. The automorphism is a negative control for the proposed
ring inclusion; the reduced product is a negative control for the local Ext
inference, explicitly outside the DOMAIN source hypotheses.

The pertinent assessed assertions are reproduced above; raw report provenance:

```text
Fable full2245-swarmHQ-fable-20260923T224500Z.md
9558914fa086e90eb6a18c246818d1c1d03fbac1ba4da18c8051aa53c04487d7
nonzero-dual-first-integration-swarmHQ-root-20260923T155000Z.md
462e49a3bf825490e71b48dc5d30d98d385ebb4d2d30803f621345caec703c99
generic-dual-integration-swarmHQ-root-20260923T163500Z.md
4f2d2a00724d579203f760b827e3930098c54ed750d2c8d0d66686bb194b06e6
FALLACY-v2.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
```

Fable's proposed ring/D-module analysis originates with Fable5.1. ROOT/Astra
and the native Astra reviewer independently identified the ring and local-Ext
issues; native Astra supplied the explicit actual-image/retained-sheet check.
All initial submissions were collected before cross-sharing. ROOT received
native interims during cross drafting; this synthesis is not a blind submission.
Raw receipt/hash custody is not a mathematical certificate or canonical seal.
Native cross author completion: 2026-09-23 23:29:43 UTC.
Novelty UNKNOWN; elementary scope corrections, not a new global theorem.

## OPENS RAISED

None. The existing global functional-existence gap is unchanged.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `7bc4d1adcc88c65acc8d95b18f8f1b8470697bf5` (Git blobs only).

Scan command: `python3 ops/open_collision.py <this-report-author-snapshot> --root . --basis 7bc4d1adcc88c65acc8d95b18f8f1b8470697bf5`.
The paused, read-only author snapshot retained SHA256
ba202c823740592d412b367f120aaea2666081af188353b887bc99d1f9dce3b2
before and after the scan. This EMPTY result is not a novelty or correctness
certificate; no newly raised OPEN was searched. Authoring then resumed only
to record this output and completion.

Whole-author readback and unchanged dependency postpins completed
2026-09-23 23:38:36 UTC. Author complete; this marker is the last body write.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10205`.
- Body SHA-256:
  `c5b27dc93599f9475349a42173a5f9edd802c2cbb6743fba550901140db2fb17`.
- Frozen basis: `7bc4d1adcc88c65acc8d95b18f8f1b8470697bf5`.
