# Task: "Theorem B" — functional-level rigidity WITH tails (primary research)

You are GPT 5.6 Sol doing PRIMARY RESEARCH on the plane Jacobian Conjecture
campaign in /Users/dc/code/math/jc72108 (full read access).

## Background (read in this order)
1. `MATHIEU.md` — Theorem A (PROMOTED): if A,C in k[w] satisfy
   AC' - wA'C = c != 0 (char 0) then deg A <= 1, proved via the
   Duistermaat-van der Kallen / Mathieu-Zhao mechanism. This killed the
   residue functional's zero-tail world and made strip theory uniform.
2. `SHEET6-DIRECTIONB.md` — the direction-b zero-tail theorem: the J-jet
   identity (t Phi_t - 12 Phi) Gamma_eta - Phi_eta (t Gamma_t - 18 Gamma)
   = -(42/c_f c_g) t^20 forces, in the pure-dead-stretch sector, first
   w_i^4 = 0 and then the contradiction 0 = -42. Section 6 (end of file)
   documents the CURRENT frontier: with nonzero tails, Row_20 demands the
   tails cancel the -42 in all 10 eta-components; the slot-20-LINEAR
   stratum is already INCONSISTENT (rank 4/10, target outside image), so
   any survivor needs deeper tail loading (level-42 quadratic block,
   level-38..46 cross-terms).
3. `SHEET6-TEMPLATE.md` + `SHEET6-CAMPAIGN.md` (skim) — what "residue-A,
   IIa(2,3,1)M2@w2, a1/a2 = 2+-sqrt(3)" means; the 7 rigid on-axis
   survivors all have this shape; residue-A survives ONLY on the
   forced-nonzero-tail locus.

## The question
Theorem A operates at the FUNCTIONAL level (no coefficient bash) but only
sees the tail-free skeleton. Is there a strengthening — a "Theorem B" —
that constrains or kills the forced-nonzero-tail sector at the same
structural level? Directions worth genuine attempts (pick the most
promising, don't survey all):
- DvdK Newton-polygon-at-infinity argument applied to the PAIR
  (skeleton, tail) jointly, e.g. treating tails as a filtered deformation
  and proving the associated graded already obstructs;
- Mathieu-subspace / Gaussian-moments formulation of the -42 identity:
  is t^20's coefficient forced to lie in a Mathieu subspace that excludes
  nonzero constants?
- D-module or p-curvature reformulation of the J-jet identity;
- A conserved quantity like the depth invariant w=(kappa-rho)/nu that
  survives tail-loading and rules out the level-42 quadratic escape.

## Deliverable
Write `/Users/dc/code/math/jc72108/xmodel/sol-thmB.md`:
- Either: candidate Theorem B (precise statement), proof strategy, and the
  FIRST LEMMA actually proved in full;
- Or: a precise obstruction theorem ("the functional level cannot
  distinguish X from Y because ...") — equally valuable;
- 5-line executive summary at top; everything unproven labeled
  **CONJECTURE**; cite files/lines for every campaign fact used.

## Rules
- Do NOT modify any repo file except your one output file. No git.
- Do not spend effort re-verifying promoted results; trust MATHIEU.md and
  the SHEET6-* promoted docs as stated, cite them.
- Depth over breadth: one serious attempt beats four sketches.
