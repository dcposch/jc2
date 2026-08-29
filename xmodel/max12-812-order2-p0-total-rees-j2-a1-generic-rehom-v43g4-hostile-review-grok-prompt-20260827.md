# Hostile review prompt: V43G4 exact total `5*t^6*a1^4` identity

Act as an adversarial algebra, software, and custody reviewer.  Audit the
frozen producer case

`cases/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827/`

in full, especially `PREREGISTRATION.md`, `RESULT.md`, `FREEZE.sha256`,
`rehomogenize_generic_qt_v43g4.py`, `run_aws.sh`, and the complete harvested
evidence under `aws_r6b_rehom_20260827T111531Z/`.  Recompute every hash and
manifest.  The producer report SHA-256 is
`ae7beed3e677a46bda82778ae6bbeb1a8aef74dcbf8db35df07f02d183b70015`
and the case-freeze SHA-256 is
`777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91`.

The narrow claim to attack is exactly:

```text
5*t^6*a1^4 = sum_i H_i Tg_i
```

in the literal total polynomial ring `Q[t,X19_total]`, `t=rho^2`, for the
frozen ordered-`a1` grade-through-19 corpus.  Exactly eleven multipliers are
nonzero and all use rows of grades 11--15.  This is not yet the required
cofactor-nonzero-at-zero certificate because the left coefficient has
positive `t`-valuation.

Attack and independently replay at least these points:

1. Verify custody transitively: the V43G3 freeze and all 58 individual
   Laurent multipliers, the pinned V43 literal-row compiler, the exact 59/66
   and 58/64 censuses, the unique `ez9` pivot, and the read-only AWS source
   manifest.  Detect stale or mutable dependencies.
2. Audit the fail-closed Laurent parser against every serialized multiplier.
   Check signs, parenthesized denominators, powers, rational coefficients,
   negative exponents only for `t`, and that quarantined Singular matrix
   writes are never consumed.
3. Independently replay all four layers over exact rationals:
   raw `Q(t)` dehomogeneous product equals 1; denominator-cleared product
   equals `5*t^6`; sigma-residue projection preserves that product; and
   rehomogenized multiplication by every original literal total row equals
   exactly `5*t^6*a1^4` with zero other terms.
4. Check that the rational LCM is 5, least Laurent `t` clearing for these
   multipliers is 6, removed integer content is 1, product levels are exactly
   3 and 4, and no terms are silently discarded by the residue projection.
   Distinguish these claims from global minimality of support or pole order,
   which a successor—not V43G4—will test.
5. Check the eleven named source rows, all source-row hashes, the zero pivot
   multiplier, and that the `Tg15_7` literal row mutation produces the saved
   nonzero residual.  Look for target-only/tautological mutations, compiler
   aliasing, accidental specialization, or use of reconstructed rather than
   literal total rows at the last layer.
6. Prove or refute the weighted homogenization argument: `wt(t)=0`,
   `wt(a1)=5`, each `Tg_g` has sigma weight `g`, residue projection modulo 5,
   and the level-4 target.  Check that output polynomial serialization cannot
   hide a failed in-memory replay.
7. Audit the intended converter boundary.  V43G4 alone has `q=t^6*5`, so
   `q(0)=0`; it does not close the chart.  Conditional on a separately exact
   special identity `a1^M-B=tH`, verify the formula giving exponent
   `4+6M` and state exactly what must be replayed before promotion.
8. Enforce scope: frozen ordered-`a1` literal rows only.  No terminal receiver,
   source/landing coverage, `G2-PSC`, `G2-BD`, Gate T, order-two,
   maximum-twelve, or JC2 conclusion follows.

Classify each attack as PASS, REPAIRABLE, GAP, or REFUTED.  If possible,
write a small independent exact replay rather than trusting producer status
strings.  Do not mutate any producer or canonical ledger.  Write only the
review report to

`xmodel/max12-812-order2-p0-total-rees-j2-a1-generic-rehom-v43g4-hostile-review-grok-20260827.md`.
