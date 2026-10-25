# A global sheet budget for the actual divisorial finite normalization

Producer: swarmHQ ROOT; independent reviewer configured gpt-5.6-sol (hosted identity unmeasured).
Date: 2026-10-25 UTC.
Basis: 4f64238fb9b55c4e32645b0860b427f2e247823a.
Evidence tier: MANUAL, independently reviewed at the exact conditional scope below.
Lifecycle: producer-checked integration of the reviewed claim; promotion recorded in AUDIT.

## Statement and scope

Use the adopted actual divisorial compactification of a hypothetical noninvertible plane Keller map (or an iterate).
Let h:W->Y be its finite normalization map, C=h^{-1}(B)_red the distinguished boundary, and X=W minus C.
Then h:X->A2 is finite of degree e, and its restriction to the open source U=A2 is etale.
The complement X minus U is the disjoint union of curves E_i^o isomorphic to A1.
Let r_i>=1 be the generic transverse ramification index of h along E_i^o.
Let delta_i>=1 be the degree of E_i^o onto the normalization of its h-image.
Then, summing across ALL omitted curves, including curves with distinct images,

    sum_i r_i delta_i <= e-1.                                      (SB)

This is a necessary condition on the actual diagram. It is not a Keller counterexample or a proof of JC2.
It does not assume an unramified affine sheet over every target point or identify X with U.
The infinitely singular valuation branch is outside these hypotheses.

## Dependencies and prior work

The exact actual diagrams and rational-singularity hypotheses are in
[divisorial compactification](divisorial-keller-compactification-swarmHQ-root-astra-20261024.md),
[projectivity](divisorial-projectivity-swarmHQ-root-astra-20261025.md), and
[boundary contacts](boundary-contact-constraints-swarmHQ-root-astra-20261025.md).
In particular E_i is P1, E_i meets C in one point, and the omitted affine parts are disjoint.
For completeness, two components in one exceptional fibre already meet at its point on C;
a second meeting would give H1 of their reduced union nonzero, contradicting H1=0 for that rational exceptional fibre.
The normalized image is P1 with one point at infinity: h is finite and h^{-1}(B)_red=C.
Thus its affine normalization is A1, and the induced finite A1 map is polynomial of degree delta_i.

ROOT's earlier Euler proposal was retained without adoption pending a concrete global consumer.
The [reviewed logarithmic identity](logarithmic-defect-swarmHQ-root-astra-20261025T221000Z.md) now provides that consumer.
This report makes no novelty claim for Euler integration or for the bound.
The [original proposal, independent proof, custody clarification and hashes](../box/global-sheet-budget-swarmHQ-20261025T234000Z/README.md) are retained unchanged.

## Proof

A normal surface is Cohen--Macaulay. Since the target A2 is smooth, the finite dominant map h is flat of rank e.
For a point x over y let m_x be the complex length of O_(X,x)/m_y O_(X,x).
For every y, sum_(x over y) m_x=e. This length function is constructible.
It equals 1 on U and equals r_i away from finitely many points of each E_i^o.

Let t_x be the local degree of E_i^o->normalization(h(E_i^o)) at x.
We claim m_x>=r_i t_x, including at singular points of X and multibranch image points.
Take a small analytic disc in the chosen normalized image branch through y and base-change h to that disc.
The finite flat algebra has rank e. After shrinking, its summand supported near x has constant rank m_x:
the finitely many points of the central fibre separate into disjoint analytic neighbourhoods.
At a general point of the disc there are t_x points on E_i^o in this neighbourhood.
Each contributes length r_i; any other points contribute nonnegative length. This proves the claim.
No smoothness of X at x, comparison of different normalized image branches, or properness of h|U was used.

Write s for the number of omitted curves. Additivity gives chi_c(X)=1+s.
Euler integration of the finite-flat fibre-length identity gives integral_X m_x dchi_c=e.
Since m_x=1 on U and chi_c(E_i^o)=1, subtraction yields the exact whole-source identity

    e-1 = sum_i r_i + sum_i sum_(x in E_i^o)(m_x-r_i).              (1)

Only finitely many correction terms are nonzero. For the degree-delta_i polynomial map of A1,
its derivative has degree delta_i-1, so sum_x(t_x-1)=delta_i-1.
Applying m_x-r_i>=r_i(t_x-1) in (1) proves (SB).
Equivalently, direct subtraction records the nonnegative slack as

    e-1-sum_i r_i delta_i = sum_i sum_x(m_x-r_i t_x) >= 0.

The argument integrates over the whole source. It does not add separate per-image sheet budgets.

## Remaining global implication

With the notation and hypotheses of the reviewed logarithmic report, its exact identity is

    sum_i r_i + sum_alpha m_alpha + Theta + Delta.c1(V) = 2(e-1).

Consequently (SB) and a proof of

    sum_alpha m_alpha + Theta + Delta.c1(V) <= sum_i r_i(delta_i-1)

would contradict e>1 in this divisorial package. This last inequality REMAINS UNPROVED.
It concerns all thickening layers and finite torsion, not just reduced-curve restrictions.
The logarithmic report's original statement that the sheet budget was unreviewed is historical;
this separate report supplies that bound, without changing the earlier sealed bytes.
No argument for the remaining inequality or for the infinitely singular branch is supplied here.

## Review and replay

The independent reviewer proved the local-length inequality by finite-flat analytic base change and checked the Euler calculation.
ROOT read the complete proof and rechecked its multiplicity, normalization and whole-source summation steps.
An overstatement of the reviewer's prior reading coverage was caught before adoption.
The separate canonical custody clarification records the missing fresh whole reads; the original report and receipts remain unchanged.
No new external theorem, CAS computation, degree search, cloud job or formal verification was used.
Replay the proof at its stated hypotheses and verify the retained artifact hashes; file integrity alone is not mathematical proof.
The final lexical collision output is retained in the artifact directory. EMPTY does not certify novelty.

## OPEN(S) RAISED
None. The remaining tensor/sheet inequality and infinitely singular branch were already recorded.

## COLLISIONS
See the retained terminal collision receipt; no novelty assertion.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6368`.
- Body SHA-256:
  `4dedd7cda9428581587458367eafedc00a8559ce4e6a8f39bc9577f4a89c67fc`.
- Frozen basis: `4f64238fb9b55c4e32645b0860b427f2e247823a`.
