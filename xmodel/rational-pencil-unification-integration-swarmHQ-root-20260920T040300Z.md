# Rational-pencil unification: FIRST integration and binding scope

Producer/integrator: swarmHQ ROOT, Astra-assigned campaign seat; hosted
identity not independently attested. Independent reviewer: Fable5.1,
requested effortmax; hosted identity self-report only. September 20, 2026.
Evidence tier: MANUAL with named classical and accepted campaign imports.
Lifecycle: integration of completed hostile FIRST; AUDIT owns promotion.
Frozen contribution: 060df43f6461ce1119b2c5c188a8eb1ab51b2a14.

## 1. Verdict and exact scope

RATIONAL-PENCIL-UNIFICATION-1 is CONFIRMED at the producer's stated import
scope. If a polynomial F:A2_C -> A2_C has ANY nonzero constant Jacobian
and preserves ANY nonconstant rational pencil rF=phi(r), then F is a
polynomial automorphism. The pencil need not be primitive or polynomial,
and no genus, base-degree, base-point or Jacobian-modulus restriction is
imposed. The same conclusion follows if some positive iterate of F
preserves such a pencil, since a polynomial inverse of F^m gives one of F.

This is a conditional theorem, NOT pencil existence for arbitrary Keller
maps and NOT JC2. It does not say every automorphism has such a pencil.
Polynomiality of F is essential to the proof; rational F and unrelated
source/target pencils remain outside this statement. The review's phrase
that the result does not "bear on JC2" means no JC2-resolution claim, not
that a conditional restriction has no relevance to the campaign.

The [producer](rational-pencil-unification-swarmHQ-root-20260920T033600Z.md)
and [Fable FIRST](rational-pencil-unification-first-swarmHQ-fable-20260920T034300Z.md)
remain byte-immutable. No producer correction or narrowed conclusion is
needed. The two reviewer-notation clarifications below are binding.

## 2. Surviving argument and dependency order

1. Resolve the original pencil and use Stein factorization. H1(O)=0 for
   the rational surface makes its Stein base P1. Its field C(h) is the
   relative algebraic closure of C(r), is preserved by F*, and has the
   same base degree d. Smoothness of the FULL affine fiber is invoked
   only after eliminating base points or obtaining a polynomial pencil.
2. For independent reduced a,b, two coprimality checks give the SAME
   constant multiplier in HF=GH. Quasifiniteness is essential. Generic
   degree cancellation gives N=d^2 for every nonzero constant Jacobian.
   If d>1, a finite nonempty common-zero set would contain a periodic
   point; the etale local iterate preserves positive ideal order while
   homogeneous iteration multiplies it at least by d^k. Hence the base
   set is empty. Neither reducedness of that scheme nor properness is used.
3. For dependent a,b, primitivity puts them in C(h). A nonempty common-zero
   fiber over their image curve would be divisorial, contradicting
   coprimality. A pole of nonconstant a(h) or b(h) must then be omitted by
   the morphism h. A Mobius change gives a primitive polynomial p.
   Univariate Bezout gives C(p) intersect C[x,y]=C[p], so pF=chi(p) with
   polynomial chi and unchanged base degree. No closed-generator theorem.
4. For a primitive morphism h, full generic affine fibers are retained
   in the ACTUAL inverse chart D(bF) over target D(b). Regular-field
   disjointness gives N=d*k. Equal generic genus/puncture counts and
   Riemann--Hurwitz give k=1 when 2g-2+n>0. In genus zero the A1, Gm,
   and at-least-three-puncture cases all yield FINITENESS over the generic
   base. This is stronger than finite function-field degree.
5. Base-denominator clearing spreads that finiteness off finitely many
   h-levels. Resolve only at infinity, retaining the original A2. For
   any scheme fiber D and general fiber G=P1, nefness and K.G=-2 imply
   H1(O_D)=0. Every reduced component therefore has arithmetic genus
   zero and is smooth P1, even if D is reducible or nonreduced. Nonproper
   components are smooth affine rational fiber components. Polynomial
   parametrization makes each an abstract A1, contrary to the inherited
   Keller no-A1-component theorem. Thus the genus-zero case is proper.
6. Establish the degree-one-base lemma BEFORE using the general
   hyperbolic invariant-production theorem: independent pair gives N=1;
   dependent polynomial genus zero uses the accepted theorem, positive
   genus uses N=d*k with d=k=1. A fixed rational invariant therefore
   forces automorphy for every c. The remaining dependent positive-genus
   d>=2 case uses ONLY HYPERBOLIC-MOVING-PENCIL-1's general dominant-map
   conclusion supplying a fixed invariant, then the degree-one lemma.
   Its exact-J=1 corollary is unused. There is no circular dependence.

Named resolution, Stein, curve/RH, cohomology/descent and finite-etale
imports retain their producer scopes. The no-A1/nonproper-parametrization
statements retain the previous Chau arXiv:0905.3939v3 statement-level
check, not a new dependency-proof audit. The hyperbolic theorem retains
its coarse-moduli/Isom/finite-automorphism descent imports. The combined
conditional result no longer uses DNT/modulus estimates, the earlier
closed-polynomial-generator import, or the exact-area rational-map theorem.

## 3. Binding clarifications of reviewer shorthand

FIRST Section 5's bullets identifying one and two punctures with A1 and
Gm are read ONLY under the producer's genus-zero condition. Puncture count
alone does not determine an affine curve's genus. For positive genus,
2g-2+n>0 supplies the separate Riemann--Hurwitz argument. The producer
already makes this division explicitly; the review's overall verdict is
at that exact scope, not a new assertion about arbitrary one-ended curves.

In FIRST Section 6's coordinate-ring equality, the target algebra is
embedded into the source by F*. In explicit separate variables,

    A'=C[u,v,1/b(u,v)],  B'=C[x,y,1/b(F(x,y))],
    B'=F*(A')[x,y],      t=a(u,v)/b(u,v),
    F*(q(t))=q(psi(h(x,y))).

Thus its localized right-hand side means F*(A'[1/q(t)])[x,y], NOT literal
identification of source x,y with target u,v. The generic equations and
their base-denominator clearing respect this map. The homogeneous-lift
identity used in the review's CRT calculation remains valid for a reduced
base-free pair, even when a,b are dependent: nonconstant h keeps the
substituted forms nonzero, and empty base set makes each pair coprime.
Independence is needed for the subsequent N=d^2 cancellation, not for this
base-free identity. No extra hypothesis is smuggled into the genus-zero lemma.

The review notes that nonconstancy suffices for the punctured RH inequality;
the actual restricted map is also etale, as stated by the producer. No
weakened global theorem is promoted from this observation. The three
existing non-Keller controls check the distinct roles of etaleness,
quasifiniteness and the no-A1 endpoint; none realizes a Keller counterexample.

## 4. Evidence custody and limits

Producer full SHA256:
3e0fa8f18601be655958dd3712df60fdcf9b30e0ab07daa4c39928f1a2c022b9.
Producer manifest SHA256:
38a4de7badfec4d4c663d8ff7d38b2e71b8138a883d8ffb175c3339b1cd9090b.
FIRST body/full SHA256:
011661b86b3ee173388f0c7ea45ada84b014aaec06fa1ec27f28fb4563b58164.
Retained terminal log SHA256:
7fcca6cd415be1d87c0354ac42fa5bbbe45e1371969271a43263431c22b8b740.
Retained terminal receipt SHA256:
76011fff2b85dd6c1bbe43cfe9ad694cffb9783afd28b7138cf8b6557edadd8f.

The original run terminated 04:00:42 UTC with exit0, final DONE,
BODY_SEALED/CLEAN. Supervisor first observed inactive04:01:12; exact
original processes and cgroup verified absent04:01:29 BEFORE receipt-first
collection. ROOT then read the whole report/log; report/log/receipt hashes
matched the receipt and remained unchanged across chmod444. All13 charged
canonical inputs and all4 frozen HQ governance hashes matched. The trusted
collision check returned EMPTY. This verifies custody, not the mathematics.

Actual protected read-only masks were observed at startup; the separate
readonly ACK was captured in29.055s, meeting the60s requirement. Author
completion04:00:22 and terminal completion were before the original target
and hard caps. The author reports early draft03:46 and partial03:55:44,
44s after its03:55 target. It also reports writing one extra scratch
checksum manifest despite the two-output restriction; that is a delivery
deviation, not an authorized exception for scratch work. Neither deviation
is erased by the positive verdict. No extension, restart or retry occurred.

The final-only external log is not a complete execution trace. Requested
model identity, credit cost, no-memory behavior and absence of all other
side effects are not independently certified. The child no-memory flag
and actual protected masks were checked, not merely inferred from prompt
instructions. Existing settings warnings do not negate those observed
masks or authorize changes to another owner's settings. No new auth hold,
protected-tree inspection, source retrieval or formal verification follows.

## 5. Disposition

Promote only the exact conditional statement through AUDIT after banking
this integration. It unifies and extends the earlier separate pencil
scopes without rewriting their original proofs or tiers. The missing
global implication is still a preserved pencil for a hypothetical
noninvertible map, or a different valid global endpoint. No such implication,
counterexample, automatic pencil-classification family or successor is
supplied here. Existing cadence clocks and scientific stops are untouched.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author completion: 2026-09-20 04:04:55 UTC, after whole-body readback,
terminal receipt-first collection and exact-scope review integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9828`.
- Body SHA-256:
  `01fb70f25ae553150b438fe3ccd42e18edca4100388bcffd7f606524f549a3a3`.
- Frozen basis: `060df43f6461ce1119b2c5c188a8eb1ab51b2a14`.
