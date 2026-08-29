# Hostile review assignment: corrected affine-`mu2` Faber support

Work in `/Users/dc/code/math/jc2`.  Review exactly

```text
xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md
```

whose required SHA-256 is

```text
77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e
```

Write the unique review output to

```text
xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-hostile-review-grok-20260826.md
```

Do not edit any other file.  Do not touch `jc2-lean`.  This is a hostile
mathematical audit, not a code review.  Do not trust producer labels, PASS
tokens, the proposed components, or the prior Laurent calculation.  You may
read explicitly charged artifacts, but independently derive the mathematics
by hand and do not invoke Singular, Sage, SymPy, msolve, Lean, or another
CAS.

Audit at least these attacks:

1. Derive the inverse series `z(w)` from `Q(z(w))=w^4` and independently
   derive every connection `R1,...,R7` in (1.4), including signs and the
   missing `w^-4` term.  Check that these are the same ordinary Faber tails
   represented by the frozen source, not merely another Laurent convention.
2. Verify the raw identity
   `c^5+128 R5-96 p R3-(12 p^2+32 r)R1=0` directly.  Check whether it holds
   before any predecessor equation, radical, localization, or geometric
   base change, and whether it really excludes reduced support on `D(c)`.
3. On `c=0`, recompute the `T^-1,T^-3` Laurent coefficients, substitute
   `T(w)=sqrt(w^4+D)`, and derive `R2,R6`.  Check every factor in the square
   versus affine-Faber union, especially the coefficient `2048*mu2`, the
   free parameter `p`, and the Chebyshev zero-target sublocus.
4. Check primality and dimensions of the two proposed component ideals and
   audit the exact-Q evidence: all seven connections, both radical
   containments, `D(c)`, and exactly two minimal primes.  Treat the finite
   field lane only as a software control and V1 only as negative custody.
5. Independently expand the generalized Pell identity, its discriminant,
   and `R10=-D^4*(s+D)/512`.  Ensure none is silently promoted to one of the
   seven source rows.
6. Attack the weighted-section and application boundary.  Distinguish raw
   Laurent `h` from Faber `R`, normalized source support from actual
   total-Rees accessibility, and a `J=0` exact section from a generically
   nonzero-`J` strict arc.  Audit square-normal forcing, `k10=0`, terminal
   `[6,2]`, Taylor, order two, and JC2 scope.

Report one overall verdict: `CONFIRMED`, `REPAIR`, or `REFUTED`.  State the
smallest failing identity or missing hypothesis, the strongest exact theorem
that survives, and a precise scope firewall.  End with exactly one standalone
verdict token.
