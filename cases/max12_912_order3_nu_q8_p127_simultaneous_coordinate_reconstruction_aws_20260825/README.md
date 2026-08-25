# Simultaneous coordinate reconstruction over `F_127(w)`

The earlier coefficient-by-coefficient rational interpolation is deliberately
not reused: with 123 fibres, each scalar coefficient admits many aliased Pade
representatives and their least common multiple is meaningless.

For one true-centre coordinate at a time, this producer instead solves for a
**single common denominator** `Q(w)` across all 190 coefficients in the
`1,v,...,v^189` basis.  For each denominator degree `d`, it asks whether

```text
Q(w) * coordinate(w,v) = sum_j P_j(w) v^j
```

with `deg(P_j) <= 122-d`.  The strict inequality
`deg(Q)+max_j deg(P_j)<123` makes any passing reconstruction unique from the
123 exact full-degree fibres.  Every sample identity and every nonvanishing
denominator value is rechecked.

A PASS supplies exact candidate rational functions, not membership in the
generic quotient.  Direct substitution modulo the monic candidate `H(w,v)`
remains mandatory.

All substantive runs are AWS-only.

