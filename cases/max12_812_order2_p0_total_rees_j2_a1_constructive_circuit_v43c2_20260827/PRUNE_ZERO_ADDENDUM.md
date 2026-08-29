# V43C2 additive exact-zero pruning note

Date: 2026-08-27

This note does not alter the frozen mathematical question in
`PREREGISTRATION.md`.  It records a fail-closed representation repair found
after the first arithmetic-DAG producer was launched.

The first attempted DAG build reached the final branch combination

```text
left:  a1^46 modulo (e0,e1)
right: a1^57 modulo (e0,G),   G=e1-4*a1*ell1
split: e1*G = (32/3)*Tg12_2 modulo e0.
```

The right certificate retained a structural `assume:e1` entry even though
expanded exact arithmetic cancels its multiplier to zero.  The strict
`CombineBranches` rule correctly rejected that crossed label.  Removing the
guard or silently dropping the entry is forbidden.

The admissible repair is an explicit `PruneZeroTerms` derivation rule.  For
each named assumption label it recursively expands only that multiplier
arithmetic circuit over exact `Q`, under a registered sparse-term cap; checks
that the canonical sparse polynomial is literally empty; commits the label,
root node, visited-node count, peak sparse-term count, term cap, expanded
polynomial hash, and final term count; and only then deletes the label.  The
serialized verifier independently repeats the same exact expansion and checks
the commitment.  Literal-row multipliers and the final certificate are not
expanded by this rule.

The smallest crossed multiplier is already present immediately after the
`a1^18 modulo ell1` checkpoint.  With

```text
c = A1 coefficient of assume:e1,
m = A1 coefficient of assume:rs1,
d = A2 coefficient of assume:e1,
```

its circuit root denotes

```text
Z = a1^2 * (a1^8 + m*rs1) * c + m^2 * d.
```

The later crossed coefficient is `a1^3*K*Z` for another ordinary polynomial
`K`.  Therefore a successor may apply `PruneZeroTerms` to `Z` immediately
after the `a1^18` checkpoint and propagate the canonical zero.  This is only
a derivation-order optimization: it retains exact expansion, the unchanged
strict branch guard, all source rows, all assumptions, and the final replay
predicate.

Producer history is additive and immutable:

- v1 failed before algebra because its dynamic import was not registered in
  `sys.modules`;
- v2 fixed only that packaging issue and failed closed at the crossed-label
  guard;
- v3 SHA-256
  `da36a572143e3f2d6a970f6b79205db7432b95596d1945bd698bec7696dfa088`
  applies `PruneZeroTerms` at the first *encountered* crossed-label boundary;
- a v4, if required by the registered v3 memory gate, moves the same exact
  check to the smaller `Z` boundary above.  It must be frozen and reported as
  a distinct producer.

