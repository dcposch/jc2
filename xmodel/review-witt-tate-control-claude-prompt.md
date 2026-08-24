# Hostile review assignment: unrestricted all-Witt Artin--Schreier control

Work in `/Users/dc/code/math/jc2`.  Independently audit the provisional report
`xmodel/witt-tate-control-20260824.md`.  Read its cited repository sources and
deduplicate its claim.  Do not trust its algebra or interpretation merely
because an internal checker agreed.

Your only repository write is `xmodel/review-witt-tate-control-claude.md`.
Do not edit ledgers or any other path.  Scratch work belongs outside the repo.
Do not use the network, remote machines, or heavy solvers.

For general odd prime `p` and every `n>=1`, audit the claimed compatible maps

`F_n=(x-x^p, y*sum_{j=0}^{n-1}(p*x^(p-1))^j)` over `Z/p^n`.

Independently check the exact determinant, reduction compatibility, marked
collision, support/degree growth, and what the inverse system defines over
`Z_p`.  In particular attack:

- indexing conventions for `W_n(F_p)` and the base `n=1`/reviewed `n=2` map;
- whether integer representatives and reduction compatibility are stated
  correctly;
- convergence and membership of the limit in the restricted Tate algebra;
- the rational formula and whether its denominator is a unit there;
- finite/etale/rank-`p` and noninjectivity assertions for the analytic/rational
  limit;
- any hidden sense in which the inverse limit is actually a finite polynomial,
  or conversely fails to be an element of the asserted algebra;
- scope: this must not become a bounded-support/degree lift, an alternate-lift
  impossibility theorem, a complex polynomial map, or a JC2 counterexample.

Use one verdict: `CONFIRMED`, `CONFIRMED WITH GAPS`, `INCONCLUSIVE`, or
`REFUTED`.  State the precise campaign consequence, smallest correction if
needed, exact commands/calculations, provenance/dedup findings, and an attack
log.  If confirmed, say whether the result may enter the scoped audit ledger.
