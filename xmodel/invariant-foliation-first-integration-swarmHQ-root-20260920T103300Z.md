# Invariant-foliation Keller theorem: FIRST integration and binding scope

Producer/integrator: swarmHQ ROOT, Astra-assigned seat. Independent
reviewer: Fable5.1, requested effortmax. Hosted model identities are not
independently attested. September 20, 2026. Evidence tier: MANUAL with
named accepted campaign, classical and primary-source imports.
Lifecycle: completed hostile FIRST integration; AUDIT owns promotion.
Frozen contribution: d5bc2d536f50caa815ad24049e348ece68f1639d.

## 1. Exact verdict

**INVARIANT-FOLIATION-KELLER-1 is CONFIRMED at the stated import scope.**
A polynomial map of the complex affine plane with any nonzero constant
Jacobian determinant that preserves an algebraic foliation is a polynomial
automorphism. The same conclusion follows if any positive iterate
preserves an algebraic foliation. Preservation is pullback invariance,
not pointwise fixation of leaves; singularities of the foliation are allowed.

The [producer](invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md)
and [independent Fable FIRST](invariant-foliation-first-swarmHQ-fable-20260920T101500Z.md)
remain immutable. All six interfaces were confirmed. This integration
adopts the reviewer's simpler fibration routing below; it neither weakens
the conclusion nor enlarges it beyond the reviewed statement.

No invariant foliation is supplied for a hypothetical noninvertible
Keller map. This does not assert that every automorphism preserves one,
and is neither a JC2 solution nor a literature-novelty claim.

## 2. Surviving argument and binding simplification

1. Restrict an algebraic foliation to the original affine plane and
   choose a primitive polynomial form omega=A dx+B dy. Its common-zero
   set is finite or empty. The polynomial inverse Jacobian matrix and
   quasifiniteness show that F*omega is primitive as well: a common
   divisor would give a curve mapping into that finite set. Rational
   proportionality therefore has a nonzero CONSTANT multiplier lambda.
   Coprimality is used, not the stronger unit-ideal condition; F need
   not be proper or surjective.
2. If d omega=h dx wedge dy and J(F)=c, then c*h(F)=lambda*h.
   Nonconstant h gives a preserved polynomial pencil. If h=0, polynomial
   integration gives omega=dH, H nonconstant, with H(F)=lambda*H+b.
   The only residual case is nonzero constant h, forcing lambda=c.
3. For TWO distinct invariant foliations, unless one already yields a
   pencil, both curls hi are nonzero constants and both multipliers c.
   The form h2*omega1-h1*omega2 is nonzero, closed, polynomial, and
   preserved with multiplier c. Its polynomial primitive yields a pencil.
   Nonzeroness follows from distinctness; no constant wedge or common
   integrating factor is assumed. The combined form need not be primitive.
4. **Route EVERY rational-first-integral case directly to a pencil,
   regardless of the genus of its generic leaf.** Resolve and Stein-factor
   the fibration. Rationality of the surface gives H1(O)=0, so the primitive
   base is P1 and its field C(r) is relatively algebraically closed in
   C(x,y). Preservation gives dr wedge d(rF)=0. Characteristic zero and
   relative closure imply rF=phi(r), with phi nonconstant by dominance.
   Apply accepted RATIONAL-PENCIL-UNIFICATION-1, allowing affine base
   points and any generic genus. This is exactly the producer's fibration
   argument without the unnecessary rational/elliptic genus restriction.
5. If there is NO rational first integral, extend the map and foliation
   to P2. Under generic degree greater than one, invoke Favre--Pereira
   Corollary B to obtain two invariant foliations on the original surface,
   then apply step 3. Degree one uses the inherited birational-Keller
   endpoint. An invertible positive iterate gives an inverse of F by
   composing its polynomial inverse with F^(m-1).

Step 4 avoids the corollary proof's final higher-genus fibration branch
and its separate product/quotient descent discussion. ROOT independently
checked this rerouting; no genus assumption occurs in its field argument.
The reviewer's explanation of that branch is therefore NOT a new imported
dependency. No additional primary source or classification result is used.

The review also observes an iterate-robustness margin. If a two-foliation
conclusion were supplied only for F^k, the independently proved two-form
lemma applies to F^k with determinant c^k, and the polynomial inverse
argument returns invertibility of F. This does not circularly assume the
one-foliation theorem for the iterate. The source actually states the
conclusion for the original map, so no weakened reading is required.

## 3. Imports, comparisons, and remaining gap

The new source import is Corollary B of Favre--Pereira,
[*Foliations invariant by rational maps*](https://www.cmls.polytechnique.fr/perso/favre.charles/ratfol6.pdf),
author PDF July 8, 2009. ROOT and Fable read its statement and complete
corollary proof. Its original-surface conclusion applies to a rational
projective extension, not just a holomorphic projective endomorphism.
Its underlying classification remains a named import, not a reconstructed
proof audit. Agreement with a published version was not separately checked.
The binding argument now uses only the no-first-integral branch.

The accepted [rational-pencil theorem and binding integration](rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md)
retain their exact scope and named dependencies. Birational-Keller,
resolution/Stein, rational-surface cohomology, algebraicity of projective
holomorphic foliations, and characteristic-zero differential dependence
are the other inherited/classical inputs. There is no exact-area,
Jacobian-modulus, or polynomial-conjugacy assumption.

This broadens the campaign's pencil criterion to algebraic foliations
without a first integral. It does not prove existence of either structure.
The earlier Hamiltonian-isotropy criterion has a different premise:
an actual source automorphism commuting with a Hamiltonian field. No
existence of that symmetry follows here. Known controls remain scoped:
(x^2,y) is non-Keller and has nonconstant pullback multiplier; repeated
copies of one foliation cannot supply the nonzero cancellation form.

The global gap is still an actual-source argument forcing invertibility,
possibly by forcing an applicable invariant structure under hypothetical
noninvertibility. No automatic foliation-existence, classification, donor,
or control-family successor is raised by this integration.

## 4. Evidence custody and limits

Producer full SHA256:
1ccc0fc8d9f70ca9d9743efee2d63aa5d390219f0f87fb045be88d543e7a9054.
Producer manifest SHA256:
40cedeb33602a6167ba53ef0a3e0853cf301d7a50f632566d517644bd3245423.
Fable FIRST body/full SHA256:
343c2af486b6bba6089796e9f96f832ee0463e4c293e77c7c105e6ce705e0ad7.
Retained terminal log SHA256:
27d1f1a2e64bb23337088b8dd921460cfdf37421ddd6118f79ab6f3f7cc2d606.
Retained terminal receipt SHA256:
9a14541ed4fe31c4955a07a1bf099cb12ca6ffedf30717aab32efa536b4cf586.
Primary PDF SHA256:
fb63dcf42b7ebe436f819749751011aadbfc6a59e5e790c2be4af41ac2cb2f9a.
The complete copyrighted PDF is not included in the public contribution.

Original run terminated 10:31:09 UTC, exit0, DONE, BODY_SEALED/CLEAN.
Supervisor first observed inactive10:31:27; original processes and cgroup
verified absent10:31:53 BEFORE receipt-first collection. ROOT then read
the whole receipt/report/log. Report and log match the receipt; all three
hashes remained unchanged across chmod444. All nine canonical inputs,
four frozen governance pins, the prompt and private source PDF matched
their prelaunch hashes. Trusted collision check returned EMPTY. These
checks establish custody, not mathematical correctness or formal proof.

The startup ACK was captured in29.253seconds; actual executable paths and
both protected read-only masks were observed. The author reports a failed
first draft write repaired immediately before evidence reading, a saved
partial10:25:29, body completion10:30:28 and marker appended10:30:53.
Partial and final delivery met their original deadlines; no retry or
extension occurred. Initial draft repair was required by the prompt,
not an authorization for extra outputs. The author's claimed output
scope was report plus ACK; absence of all other side effects is not
independently certified by the final-only log. Model identity, cost and
automatic-memory behavior likewise remain unverified beyond the checked
child flag. Existing settings warnings do not negate observed process
masks or authorize changes to another owner's settings.

## OPEN(S) RAISED

None. No new bounded experiment or unreviewed descendant is commissioned.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised open entries.

Trusted `ops/open_collision.py` check of this partial returned EMPTY.

Author completion: 2026-09-20 10:34:59 UTC, after whole-body readback,
terminal receipt-first review collection and all input-pin checks.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9032`.
- Body SHA-256:
  `11d4ba8eed8e49ccd469a20d5bd928d1b13f277db27c19357cc9b98e360db69e`.
- Frozen basis: `d5bc2d536f50caa815ad24049e348ece68f1639d`.
