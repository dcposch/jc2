# Hostile follow-up — D1 double-root correction-enabled Newton rays

Act as a hostile valuation-theory and exact-algebra referee.  A live source
review of the tied toric chart was launched before the following coverage
correction was found.  Adjudicate the correction explicitly and independently.

Read and verify:

```text
466736cdd1a76607e6475c98d9da4b55096e88813d911722954549bdcba702c0  xmodel/max12-912-order3-d1-double-root-newton-fan-correction-firewall-20260825.md
015ed8156197ba4cfac55cbc6d33379d7545739bfe657856febd8e17c8d3913c  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/FREEZE.sha256
c76ef85ac14f81839674368c55a324499832e6cf4b589befa68baf93a42b1490  cases/max12_912_order3_d1_double_root_toric_blowup_20260825/compile_toric_blowup.py
```

Charge these points:

1. Re-derive the first exact negative layers
   `(4/9)QR/K+(2/9)R^2/K^2-(4/81)Q^3/K^2` from the charged ordinary source.
2. With `K=L^2U,N=LU`, verify negative control 1 term by term:
   `Q=t^beta N`,
   `R=t^alpha L+t^(2beta)U/9`,
   `3beta/2<alpha<2beta`.  Check that the first `QR/K` term is polynomial and
   that the weight-`3beta` QR correction cancels `Q^3/K^2` exactly.  Look for
   any omitted term at an earlier or equal weight.
3. Verify negative control 2:
   `alpha=15/2`, `5<beta<6`,
   `Q=t^beta L`,
   `R=t^alpha N-(1/2)t^(15-beta)`.  Check that the lower QR term is polynomial
   and that the complete weight-15 negative tail is exactly `(2/3)/K`, hence
   only row 3 and compatible with `mu=2/3`.  Audit signs, powers, and whether
   motion of K or the exact inverse changes this initial coefficient.
4. Decide whether either example is forbidden by the strict ramified-slope
   equivariance or fixed-load semantics.  Rational valuations may be cleared
   by finite ramification; do not assume integral beta without justification.
5. Determine precisely what follows: these are finite Newton successors, not
   formal lifts, but do they invalidate the claim that only `alpha=2beta`
   survives the low fan?
6. Audit the frozen toric compiler separately.  Are its equations,
   `Q=x Qhat,R=x^2 Rhat,xy=Lambda^6`, axis/cusp motion, exact targets, all Rhat
   directions, and boundary conditions correct for the tied `alpha=2beta`
   chart even though the completeness claim is false?  Identify any source
   equation that must change, as opposed to a scope-only erratum.
7. Propose the minimal complete recurrence state for a successor compiler.
   It must retain higher coefficients of every earlier rational layer and
   must not claim a finite fan/truncation without proof.

Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-newton-correction-review-grok-20260825.md`

End with exactly one verdict token on its own line:
`CORRECTION_CONFIRMED`, `CORRECTION_REPAIRED`, or `CORRECTION_REJECTED`.
