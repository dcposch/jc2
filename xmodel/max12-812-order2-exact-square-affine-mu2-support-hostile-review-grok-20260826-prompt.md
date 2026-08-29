# Hostile review assignment: exact-square affine-`mu2` support

Work in `/Users/dc/code/math/jc2`.  Review exactly

```text
xmodel/max12-812-order2-exact-square-affine-mu2-support-theorem-20260826.md
```

whose required SHA-256 is

```text
75c7ec8431781d466501da9bf97f909e05392c0cafc2d37ff200dacc2d497365
```

Write the unique review output to

```text
xmodel/max12-812-order2-exact-square-affine-mu2-support-hostile-review-grok-20260826.md
```

Do not edit any other file.  Do not touch `jc2-lean`.  This is a hostile
mathematical audit, not a code review.  Do not trust producer labels, PASS
tokens, the proposed components, or the producer's radical output.  You may
read the theorem's explicitly charged artifacts, but independently derive
the mathematics by hand and do not invoke Singular, Sage, SymPy, msolve,
Lean, or another CAS.

Audit at least these attacks:

1. Reconstruct the seven Laurent coefficients of
   `sqrt(Q)*(Q^2+beta*Q+gamma)` and check the integer-denominator convention,
   especially that `E2-1024*mu2` is the affine equation and the other six
   rows are zero.
2. On `D(c)`, independently verify every displayed elimination identity:
   the formulas for `beta,gamma,F5,F7`, the `p!=0` linear combination, and
   the `p=0` specialization using `E6`.  Look for divisions or field
   hypotheses that lose a component.
3. On `c=0`, verify `h4=-(p/2)h2`.  Check that `D(p)` really reduces to the
   reviewed seven-zero-tail classification.  At `p=0`, check all six
   non-target rows, not only `E6`, and derive both the `r=0` square limit and
   the displayed affine component with the correct factor in `mu2`.
4. Check that the three ideals in the theorem are prime, that all overlaps
   are harmless, and that their union is exactly the reduced support over
   characteristic zero.  Audit whether the exact-Q stdout and validation
   actually establish both containments and exactly three minimal primes.
   Treat the finite-field run only as a software control.
5. Independently substitute the `(r,t)` parametrization, check the
   generalized-Pell remainder and `h10=-r^4*(t-r)/512`, and ensure `h10` is
   not silently promoted to a source equation.
6. Attack the application boundary: affine Laurent receiver versus literal
   total Rees, correction jets, target/deck ties, `k10=0`, terminal `[6,2]`,
   Taylor receivers, other charts, order two, and JC2.

Report one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.  State the
smallest failing identity or missing hypothesis, the strongest exact theorem
that survives, and a precise scope firewall.  End with exactly one standalone
verdict token.
