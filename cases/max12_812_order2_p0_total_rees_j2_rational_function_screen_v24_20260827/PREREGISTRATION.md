# V24 preregistration: degree-15 J2 rational-function membership screen

Date: 2026-08-27

Status: **FROZEN SCREEN DESIGN; NO CHART VERDICT WITHOUT DENOMINATOR REVIEW.**

## Question

For each V23R1 specialization of the promoted exact-Q rows through grade 15,
test the smallest possible direct exceptional target:

```text
T-a0:       a0^3  in I * Q(qa1,rho)[positive-weight variables]
ordered a1: a1^3  in I * Q(rho)[positive-weight variables].
```

The coefficient-field move is a bounded homogeneous screen.  Every source
row is homogeneous for the reviewed sigma grading and every nonzero
specialized generator has weight at least 11.  Thus weight-15 membership uses
only cofactor weights 0 through 4 and cannot require a higher-weight row.

## Interpretation

- A nonmembership result rules out every polynomial certificate with
  exceptional exponent 3 and factor `1+rho*W`: its weight-15 component would
  make the cubic a member after passing to the rational-function coefficient
  field.
- A membership result is only a candidate.  Its rational-function cofactors
  must be replayed exactly, their common denominator cleared, and the cleared
  denominator must have rho-constant term a nonzero rational constant
  independent of `qa1`.  Only then can it be normalized to `1+rho*W`.
- No denominator in `rho`, `qa1`, a jet, or an exceptional coordinate is
  silently treated as a chart localizer.

## Frozen computation

The compiler rehashes V23R1 `RESULT.json` and all 84 literal chart-polynomial
files, reparses them with the hash-pinned restricted-AST parser, rechecks
sigma homogeneity and rho parity, and emits a Singular ring with
`qa1,rho` (a0 chart) or `rho` (a1 chart) in the coefficient field.  A weighted
degree-compatible order and `degBound=15` compute the degree-15 standard
basis screen.

Controls:

1. all seven specialized grade-10 rows must be literal zero;
2. a nonzero grade-11 generator must reduce to zero;
3. the exceptional square of weight 10 must remain unchanged;
4. any reported membership must include a `lift` matrix whose direct replay
   against the original ideal has zero residual;
5. any reported nonmembership must preserve the nonzero normal form.

## Resources and stop rule

AWS only.  One exact-Q lane per chart, each under a four-hour engine cap and
an explicit virtual-memory cap no larger than the audited free memory of its
host.  Stop after the cubic verdict.  Do not raise the exceptional exponent,
change coefficient fields, or launch a broad saturation/Groebner successor
without reviewing this result and the independent Fable5/Grok designs.

This screen supplies no J2-chart theorem, no radical computation, no source
rows above grade 15, no Rees saturation, and no conclusion about Gate T,
order two, maximum twelve, or JC2.

