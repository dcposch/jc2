# Hostile review: order-one terminal `r7` component criterion

You are an independent hostile mathematical reviewer.  Work in
`/Users/dc/code/math/jc2`.  Read the target in full:

```text
xmodel/max12-812-order1-terminal-r7-pure-power-component-criterion-20260826.md
SHA-256 bbd744fa0c3875f11d5f0038dbbdea461e2656c6a9eb98d2b9050c1eae31712a
```

Read the three frozen parents named in target section 0.  Do not use any
other review verdict as authority; rederive the result.  Do not run CAS,
Python algebra, Lean, or other heavy computation.  Do not print or inspect a
full dirty-worktree status.  The only permitted write is one review report:

```text
xmodel/max12-812-order1-terminal-r7-pure-power-component-criterion-review-grok-20260826.md
```

Attack every load-bearing point:

1. Re-derive the exact source formula and divisor, including constants,
   signs, `U=2`, the empty `U=1` case, and separation of `U=0`.
2. Check that a rational coefficient map from the complete source line
   extends to the normalization of the projective component and that
   nonconstancy of the pulled-back `r7` makes both maps nonconstant.
3. Prove or refute that singleton support of the pullback zero and pole
   divisors forces singleton support downstairs, equal downstairs orders,
   unique preimages, total ramification, and `d*n=U-1`.  Look for failures
   from inseparability, constants, cancellation, singular affine charts,
   or omitted points at infinity.
4. Check the genus-zero conclusion and the coordinate statement
   `R=lambda+delta*t^d`.  Check exactly when the branch-value set has two
   elements and the degree-one exception.
5. Check the claim that `phi` is conjugate to a power map: charge the full
   Riemann--Hurwitz count, not just the two visible points.
6. Try hard to derive the overstrong downstairs exponent `U-1` without
   birationality; confirm or refute the firewall that only `d*n=U-1` is
   licensed in general.
7. Check the proposed component falsifier and identify every premise needed
   to consume a modular projection (actual component, exact normalization,
   complete graph of the actual `r7`, chart complements, characteristic-zero
   lift).
8. Enforce the terminal-only scope.  No order-one emptiness, Taylor/Rees
   closure, `(8,12)`, maximum-twelve, or JC2 claim may slip through.

Give one verdict `CONFIRMED`, `REPAIR`, or `REFUTED`.  If not confirmed,
state the smallest failing sentence and a clean corrected theorem.  Pin the
target and parent hashes in the report.
