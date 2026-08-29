# V43C3 preregistration: rebased exact `rho=0` certificate circuit

Date: 2026-08-27

## Frozen question

Does the exact change of assumption basis missing from the invalidated V43C2
derivation repair the second `e1` branch and produce an honest ordinary-ideal
certificate

```text
a1^104 in I0
```

for the complete frozen raw ordered-`a1`, `rho=0`, grade-through-19 corpus?

The charged predecessor invalidation is
`cases/max12_812_order2_p0_total_rees_j2_a1_constructive_circuit_v43c2_20260827/INVALIDATION.md`
(SHA-256
`dbea733345b2a707ee5834b90889eca6b41013b6694786317f54362e97d96b89`),
with additive freeze SHA-256
`8c3f2ecab6b16ee9c6e3c338f9f88883a33e20baf2cf7aabe69c0bdfca9bd787`.

## New exact rule

Immediately before any exponent-three `ClearPower` on `ell1`, the inherited
certificate has multiplier terms for `e1`, `ee0`, and `ell1`.  The successor
must serialize and independently replay one `RebaseAssumptions` node using

```text
G   = e1-4*a1*ell1,       e1  = G+4*a1*ell1,
Q0  = ee0+4*aa0*ell1,     ee0 = Q0-4*aa0*ell1.
```

For old multipliers `(c_e1,c_ee0,c_ell)`, the node must output

```text
c_G   = c_e1,
c_Q0  = c_ee0,
c_ell = c_ell + 4*a1*c_e1 - 4*aa0*c_ee0,
```

with old labels `assume:e1` and `assume:ee0` absent.  The rule verifies both
generator identities coefficientwise over `Q`; it is not a quotient,
localization, substitution of source rows, or relaxed branch guard.

## Exact acceptance predicate

Accept only if the AWS replay:

1. rehashes the predecessor invalidation/freeze, V43C1 source, V42 sources and
   hostile review, and all 70 frozen row files;
2. verifies the 51-nonzero-row/70-file and 65-variable `rho=0` censuses;
3. checks every row-specialization leaf, arithmetic-DAG node, and all existing
   `Add`, `Scale`, `Mul`, `ClearPower`, and `CombineBranches` rules exactly;
4. commits and replays exactly one `RebaseAssumptions` rule with scalars
   `+4` and `-4`, before the exponent-three `ell1` clear;
5. confirms neither old label survives that rebase and reruns the unchanged
   strict crossed-assumption guard at the final `(e1,G)` split;
6. obtains final target exactly `a1^104`, with no assumption generator and
   only literal frozen row labels in its multiplier map;
7. serializes the complete derivation DAG, reloads it, and independently
   replays it from the frozen bytes; and
8. rejects four negative controls: final-row omission, a changed clearing
   exponent, mutation of `+4` to `-4`, and mutation of `-4` to `+4`.

No zero multiplier may be pruned merely because a prior producer expected it
to cancel.  Any `PruneZeroTerms` node still used must pass its exact sparse
expansion predicate.

## Scope and execution

Ambient ring: `Q[X19_rho0]`, the 65-positive-variable frozen ordered-`a1`
raw ring after `rho=0` and the ordered chart specialization.  The ideal is the
51 nonzero raw rows through grade 19.  A PASS is only this explicit special
ordinary-ideal membership; no total-`rho`, saturated-Rees, Gate-T, bounded
degree, order-two, maximum-twelve, or JC2 conclusion is automatic.

AWS only: one core, 4-GiB virtual-memory cap, ten-minute wall cap.  A complete
PASS may provisionally feed the already reviewed special/generic converter,
but `M=104` and total exponent `628` remain unpromoted until hostile review.

