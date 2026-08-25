# Hostile review request — D1 squarefree common-cubic order-20 obstruction

Act as a hostile algebraic-geometry and valuation-theory referee.  This is a
different-model review of a high-fanout producer theorem.  Read the frozen
target in full:

```text
1b6e629affdc5a73995e0ab2d7f051ad772d92f75bb61e67362782fcb8f5b4ac  xmodel/max12-912-order3-d1-squarefree-common-cubic-order20-obstruction-20260825.md
a9dca05513f308d3d8685b88b957304b95b7f8fdcc7911417bf347531ac7597a  cases/max12_912_order3_d1_normal_tangent_20260825/SOURCE_CLOSURE.sha256
05435f25452b7e6148dff1a65f5abb2e203a12a96cbe8ef2877254503bccb4f1  cases/max12_912_order3_d1_normal_tangent_20260825/FREEZE.sha256
```

Verify the manifest before relying on any charged file.  Read the exact
ordinary source theorem and independent reconstruction charged by that
manifest, plus `verify_firewall_controls.py` and its passing AWS stdout.
Do not treat emitted CAS/Python text as a proof of the valuation theorem.

Charge every one of the following points explicitly.

1. Re-derive the ordinary fixed-load equations with
   `Lambda=tau^3*rho`, weights `kbar=Lambda^6*k`, row-3 load 15, row-6 load
   18, and row-8 load `Lambda^20*(1+tau)`.  Check signs and the exact meaning
   of fixed `k,mu,nu`, including their zero strata and arbitrary strict
   rational/Puiseux slope.
2. Verify that choosing the moving depressed cubic and dividing
   `E=KQ+R`, with both `Q,R` of degree at most two, is an exact normal
   coordinate change even when `p,c` move.  Re-derive the binomial/Faber
   negative layers; distinguish the inverse of `f` from the moving inverse
   of `K`.
3. Audit the valuation lemma line by line.  For every range of
   `alpha/beta`, check the first and next possible negative terms, all
   equal-valuation cancellations, corrections from a previously vanished
   `QR/K` layer, and target coincidences at weights 15, 18, and 20.  Look
   especially for a higher binomial term that could arrive earlier than the
   displayed three candidates.  Decide whether it really follows that
   `beta>=6` and then `alpha>=9`.
4. Charge every use of squarefreeness.  Work componentwise in the split
   residue algebra and verify that nilpotent-free division, degree at most
   two, and products which vanish at different roots justify each claimed
   divisibility.  Do not silently replace squarefree by irreducible.
5. Independently enumerate all negative monomials through Lambda-weight 20
   under weights `(Q,R,kbar)=(6,9,6)`.  Confirm that only the two displayed
   denominator layers occur, that every denominator-power-three term starts
   at weight 21, and that substituting the exact inverse of `f` for the
   moving inverse of `K` cannot change a coefficient through weight 20.
6. Audit the common-numerator step: after reducing over the moving monic
   `K`, does one really obtain `S/K^2` with `deg S<=5`?  Verify directly that
   the first six tails form a triangular unit-diagonal map, and that killing
   their coefficients through weight 20 also kills row 8.  Charge the sharp
   negative control `z/K^3`, whose first nonzero tail is row 8; this is the
   firewall protecting the weight cutoff.
7. Verify the exact target-numerator subtraction and the conclusion that
   row 8 demands a nonzero weight-20 coefficient.  Search for any possible
   motion of `p,c`, `tau`, or a zero/nonzero load which could supply it.
8. Check the claimed remaining locus.  Confirm that a nonirrelevant
   depressed cubic with `Delta=0` has the double-root normal form
   `(z-a)^2(z+2a)` and represents one point of weighted `P(2,3)`, while the
   triple root is the irrelevant origin.  Verify the explicit cancellation
   `Q(9RK-Q^2)=-K^2` at the normalized point and explain precisely why it
   blocks extending the squarefree proof.  Finally audit the conditional
   global-support corollary: use only the previously reviewed common-cubic
   reduced-support theorem plus algebraic curve selection, and do not infer
   that the remaining point lifts.

Name the smallest failing identity or missing hypothesis, if any.  Separate
a repairable exposition defect from a mathematical gap.  Enforce the stated
firewalls: the double-root point, local thickness/accessibility, finite
coefficient load outside this strict gate, other passports, and JC2 remain
open.

Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-squarefree-common-cubic-order20-review-grok-20260825.md`

The report must state the frozen hashes, give an independent argument rather
than a summary, and end with exactly one verdict token on its own line:
`CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `NOT_CONFIRMED`.
