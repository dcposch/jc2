# Invariant-web Keller criterion: independent FIRST integration

Producer/integrator: swarmHQ ROOT, Astra-assigned seat. Independent hostile
reviewer: Fable5.1, requested effortmax. Hosted identities are not independently
attested. September 20, 2026. Evidence: MANUAL with named accepted and classical
imports. Lifecycle: completed FIRST integration; AUDIT owns promotion.
Frozen contribution: 3006516257882da2649f8ccbd28eabd765825d06.

## 1. Verdict and scope

**INVARIANT-WEB-KELLER-1 is CONFIRMED at its stated conditional scope.**
Let F:A2_C -> A2_C be polynomial with ANY nonzero constant Jacobian. If F,
or any positive iterate, preserves a reduced finite algebraic k-web for
any k>=1, F is a polynomial automorphism. The web may initially be
irreducible over C(x,y), have colliding special directions or isolated
coefficient-base points. Preservation concerns the SAME generic web on
the original affine plane, not unrelated source and target webs.

The [producer](invariant-web-keller-swarmHQ-root-20260920T123400Z.md) and
[independent Fable FIRST](invariant-web-first-swarmHQ-fable-20260920T124000Z.md)
remain unchanged. All six interfaces were confirmed. No correction of
the producer statement or proof is required, and no new conclusion beyond
that statement is promoted through this integration.

No invariant web is produced for a hypothetical counterexample. No bounded
direction-orbit growth, local-to-global algebraization, necessity for
automorphy, arbitrary-cover descent, literature novelty or JC2 solution
is asserted.

## 2. Surviving proof and the reviewed interfaces

1. A reduced algebraic k-web is represented by a primitive polynomial
   binary form W(x,y;u,v). Sym^k(DF) is an invertible polynomial matrix.
   If the pullback coefficient vector had a common irreducible factor,
   its curve would map into the finite common-zero set of the original
   coefficients, contradicting quasifiniteness. Therefore F*W is primitive
   too, and rational proportionality gives F*W=lambda W with lambda in C*.
   Coprimality is used, not absence of isolated coefficient zeros or
   properness of F. The k=1 case is the accepted foliation criterion.
2. For k>=2 the nonzero binary discriminant Delta satisfies

       c^(k*(k-1))*Delta(F) = lambda^(2*k-2)*Delta,   c=det DF.

   The exponents follow from squared pairwise determinants of linear
   factors over a splitting field. The identities are polynomial in the
   coefficients, so nonmonic forms and projective roots at infinity are
   included. A NONCONSTANT Delta gives a preserved polynomial pencil;
   accepted RATIONAL-PENCIL-UNIFICATION-1 applies for every c in C*.
3. If Delta is a nonzero constant, H={W=0} inside A2 x P1 has k distinct
   reduced roots over EVERY base point. Zero forms and all root collisions
   are excluded. The incidence projection is projective and quasifinite,
   hence finite; the simple-root criterion in BOTH slope charts makes it
   etale. This properness belongs to H->A2, not to F. No missing roots at
   infinity, coefficient-base points or nonreduced fibers are discarded.
4. Finite etale covers of A2_C split algebraically into copies of A2_C.
   Thus H's components are global direction sections. They give algebraic
   line distributions, hence foliations, on the ORIGINAL plane. The
   derivative-induced map H->H sends each connected component into a
   fixed open-and-closed component. Pointwise invertibility of DF makes
   the resulting index map a permutation, without surjectivity of F.
   An iterate fixes a foliation, and the accepted foliation theorem closes.
5. Positive iterates remain Keller, with Jacobian c^m. A polynomial inverse
   of F^m gives one of F by composing with F^(m-1). Neither accepted
   dependency uses this web statement, so the composition is noncircular.
6. The reviewer recomputed the controls: diagonal maps and a sheet swap;
   the branched web v^2-xu^2, which goes through the nonconstant-discriminant
   pencil branch; the non-Keller map (x^2,y), which breaks constant
   multiplier; and the shear pullback of the standard three-web, which
   is not the same web. Having a Keller coframe alone supplies no premise.

ROOT independently checked the review's reconstruction and distinctions.
No computational or formal verification is claimed.

## 3. Imports and scope clarifications

The accepted [foliation criterion and binding integration](invariant-foliation-first-integration-swarmHQ-root-20260920T103300Z.md)
and [rational-pencil criterion and binding integration](rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md)
retain their named dependencies and review scopes. In particular, the
Favre--Pereira classification input is inherited through the foliation
criterion, not newly reread or extended by this report.

The extra classical inputs are Keller etaleness/quasifiniteness,
proper-quasifinite finiteness, the elementary binary-discriminant identities,
and triviality of finite etale covers of the complex affine plane. The
reviewer's shorthand "Riemann existence/GAGA" is read through its actual
argument: finite etale analytification is a topological covering, connected
algebraic components have connected analytifications, C2 is simply connected,
and a finite degree-one map to normal A2 is an algebraic isomorphism.
No unrestricted nonproper GAGA assertion is used. The review's specific
SGA citation was not independently source-checked here; the classical
comparison fact remains a named import rather than a fresh source audit.
No new external paper or classification theorem was acquired.

This extends the accepted single-foliation exclusion to an unordered finite
algebraic set of directions, without first assuming global splitting.
The remaining global issue is still existence of a preserved structure
under hypothetical noninvertibility, or a different route to properness.
A local analytic or formal direction is not thereby algebraic, and the
standard target web and its Keller pullback are not thereby identical.
No automatic web-existence, finite-cover, classification or control-family
successor is commissioned.

## 4. Evidence custody

Producer full SHA256:
2aa6cea16f98b04be251fed7a4c13bc156d271958583359be58a636a62758ede.
Producer manifest SHA256:
d215629ce966ef0b9b9d8e78a3870468e1ada9384c2434950afd14e01b5161e6.
Fable FIRST body/full SHA256:
21fc3d5b2aaac5c355bd28802efbe7b8d29b6111211164e25759ff8d1303acea.
Retained terminal log SHA256:
1682eca8ab63b3fc248a17e9a268a01268027841606e23ae75eb2a95d28ce6d1.
Retained terminal receipt SHA256:
64c95fb590242836f5e1118b875a6c474639ae466109396eae3d935c90f963d5.

The original review terminated September20 12:54:23 UTC, exit0, DONE,
BODY_SEALED/CLEAN. Inactive supervisor was observed12:55:09; original
processes and cgroup verified absent12:55:21 BEFORE receipt-first
collection. ROOT then read the whole229-line report and25-line log.
Report/log hashes match the terminal receipt; all three retained files
had unchanged hashes after chmod444. All ten canonical charged inputs,
four HQ governance files and the frozen prompt matched their pins.
The trusted collision check returned EMPTY. These establish custody,
not a substitute for mathematical scrutiny or formal proof.

Startup observed the actual executable and both protected read-only masks
at534ms; the separate444 ACK was captured in37.629seconds. The author
reports early draft12:42:42, partial12:50:34, body completion12:53:56 and
final marker12:54:08, meeting the original delivery clocks. Failed initial
apply_patch attempts for ACK, draft and partial were repaired promptly,
with the draft repaired before evidence reading. Two oversized outputs
were persisted by the harness and read in place. These disclosed delivery
events are retained, not erased by the positive mathematical verdict.

The final-only log is not a complete side-effect audit. The two authored
outputs and absence of extra writes are self-reported; model identity,
cost and automatic-memory behavior are not independently attested beyond
the observed child flag. Existing CLI settings warnings do not negate the
observed protected masks or authorize shared settings/launcher changes.
No retry, extension or formalization followed from this review.

## OPEN(S) RAISED

None. No new bounded experiment or unreviewed descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised open entries.

Trusted `ops/open_collision.py` check of this partial returned EMPTY.

Author completion: 2026-09-20 12:58:26 UTC, after whole-body readback,
receipt-first whole-review integration, unchanged pins and collision check.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8661`.
- Body SHA-256:
  `fc8467d3f4a9e9e6a7241d1c0748889436ff894adad501e990ffc67d3cb23114`.
- Frozen basis: `3006516257882da2649f8ccbd28eabd765825d06`.
