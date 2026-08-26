# Hostile review: `(8,12)` nontrivial terminal extremal-abc classification

Act as an independent hostile mathematical reviewer.  Read the immutable
target and both charged sources named in it.  Do not use the target status,
the coordinator summary, or any prior verdict token as evidence.

Target:

```text
149691f1784ffccea9473a63efaec4a7d0eea56f9c1e1ba267610b104022920e
  xmodel/max12-812-nontrivial-terminal-extremal-abc-classification-20260826.md
```

Audit from scratch:

1. Starting only from the charged terminal identity and exact Kummer order,
   recompute the Wronskian formula and every local order at numerator roots,
   denominator roots, and points off their support.
2. Attack the claimed elimination of `T(infinity)=0`.  Check unequal-degree
   Wronskian leading terms, the conclusion `r+s=1`, the unique-root descent,
   the scalar-class issue, and whether exact order really forces a
   contradiction for both `m=2` and `m=4`.
3. In the balanced case, verify normalization by `lambda`,
   `deg G=D-U+1`, squarefreeness (including constant `G`),
   `deg W=2D-U`, `r+s=U`, the radical degree `D+1`, and
   `W=kappa*A*B/(rad(A)rad(B))`.
4. Recompute the three fibres, all edge cases `U=2`, `D=U-1`, and
   `D=m(U-1)`, Riemann--Hurwitz saturation, and both degree bounds.
5. Audit the radicand factorization and the formula
   `gcd(m,all alpha_i,all beta_j)=1` for exact Kummer order.  Challenge
   constant extensions, infinity valuation, zero exponents, and the
   distinction between exact order four and its order-two degeneration.
6. Test whether the stated converse hypotheses really suffice for a
   polynomial radicand, exact terminal identity, and exact class.  Find the
   smallest omitted scalar, coprimality, degree, or separability hypothesis
   if any.
7. Enforce the firewall: this is a terminal classification and passport
   enumerator only, not lower-tail compatibility, Taylor polynomiality,
   `(8,12)` closure, maximum twelve, or JC2.  Flag any sentence that exceeds
   that scope.

Use source reading and hand derivation only.  Run no CAS, solver,
substantive Python, Lean, or other heavy local computation.  Write exactly
one report and edit nothing else:

```text
xmodel/max12-812-nontrivial-terminal-extremal-abc-review-grok-20260826.md
```

Include model identity, exact target SHA, verdict `CONFIRMED`, `REPAIR`, or
`REFUTED`, the smallest failing identity or missing hypothesis, a complete
independent proof/attack, and an exact scope firewall.
