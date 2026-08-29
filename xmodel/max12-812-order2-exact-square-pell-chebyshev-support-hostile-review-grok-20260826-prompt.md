# Hostile review assignment: exact-square Pell/Chebyshev support

Work in `/Users/dc/code/math/jc2`.  Review exactly

```text
xmodel/max12-812-order2-exact-square-pell-chebyshev-support-theorem-20260826.md
```

whose required SHA-256 is

```text
523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf
```

Write the unique review output to

```text
xmodel/max12-812-order2-exact-square-pell-chebyshev-support-hostile-review-grok-20260826.md
```

Do not edit any other file.  Do not touch `jc2-lean`.  This is a mathematical
hostile review, not a code review.  Do not trust producer status, PASS tokens,
or the producer's radical output.  You may read the theorem's explicitly
charged artifacts, but independently derive the mathematics by hand and do
not invoke Singular, Sage, SymPy, msolve, Lean, or another CAS.

Audit at least these attacks:

1. Re-derive the recurrence for the coefficients of
   `(1+p*t^2+c*t^3+r*t^4)^alpha`, including all index shifts in the formula
   for the seven coefficients of
   `sqrt(Q)*(Q^2+beta Q+gamma)`.
2. Independently decide whether seven-tail vanishing really forces `c=0` in
   characteristic zero.  Check the producer's use of the exact standard
   basis against the original seven equations; identify the smallest false
   implication if it does not follow.
3. On `c=0`, recompute the `T^-1` and `T^-3` coefficients, the triangular
   passage back to `z^-2,z^-4,z^-6`, and the square/Chebyshev split.
4. Expand the displayed Pell identity exactly, including the constant
   `Delta^5/262144`, and check that the tail begins at `z^-10` rather than an
   earlier order.
5. Check the claimed radical/intersection formulas, component dimensions,
   field hypotheses, normalization `k10=1`, and whether any `k10=0` or
   projective-load branch is silently lost.
6. Audit the application boundary: unitriangular Laurent-to-Faber transport
   versus a literal total-Rees pullback, simultaneous source weights, target
   ties, terminal `[6,2]`, Taylor receivers, and higher-contact sections.

Report one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.  State the
smallest failing identity or missing hypothesis, the strongest exact theorem
that survives, and a precise scope firewall.  End with exactly one standalone
verdict token.
