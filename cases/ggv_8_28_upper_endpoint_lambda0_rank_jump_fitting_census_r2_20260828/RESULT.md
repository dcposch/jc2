# Result

Strict overall verdict: **NO_VERDICT_FITTING_CENSUS_ONLY**.

Every genuine stratum has 95 exact rational-unit pivots and an exact 11 by
10 residual matrix:

```text
stratum     residual rank   total receiver rank   residual nonzero slots
C8                    9                    104                         75
P                     9                    104                         75
C8P02                 9                    104                         75
Q1                    6                    101                         36
C8_Q1                 6                    101                         36
Q1P02                 6                    101                         36
Q1P03 (q2)            6                    101                         36
TRIPLE02              6                    101                         36
TRIPLE03 (q2)         6                    101                         36
```

For each rank-9 residual, only 172 of the 550 raw 9 by 9 minor slots are
structurally matchable.  For every rank-6 residual, the support graph splits
exactly into a 4 by 8 block and a 7 by 2 block, of generic ranks 4 and 2.
Thus the 97,020 formal 6 by 6 slots reduce structurally to 1,470 possible
products of a raw 4 by 4 block minor and a raw 2 by 2 block minor.  This is a
combinatorial support statement, not a factorization or rank-locus verdict.

No endpoint pullback was tested here.  In particular, no stratum is declared
endpoint-dead or surviving, and no mathematical conclusion is inferred from
the earlier r1 transport failure.

Frozen core hashes:

```text
d51c84397302e81b4fc8d568b772aebb30d1b63a04002b0e92fb382fcb89bbac  PREREGISTRATION.md
409d0f586e14750df2792ab9c0027dfc4678f4fe1848eba1087dbefbd5ef9ce9  r1 mathematical compiler
9f1abf07ebfde3d51343cc90620f25f0c872cca06705c34bdbbba4affc2193e8  r2 dispatcher
d53329b0bcb2b28ca24a6a39681e45e275760beb6a272c5c2f4eb2cbcec4e960  r2 source archive
```

