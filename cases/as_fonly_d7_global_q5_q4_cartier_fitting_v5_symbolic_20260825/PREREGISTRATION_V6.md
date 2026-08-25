# V6 preregistration — source-typed restoration assertion parser

V5 failed closed because Z3 4.16 renders each ternary high-bit guard as an
equality `Extract(31,2,q)=0`; the old parser treated every charged non-ULE
equality as a source row.  The exact AWS diagnostic classified the charged
assertions as:

- 63 source-row congruences (`eq-candidate-kind-1034`);
- 30 high-bit-zero ternary guards (`eq-candidate-kind-1059`);
- 30 low-two-bit `ULE <= 2` ternary guards.

V6 must recognize the high-bit guards structurally, retain both guard blocks,
and pass only the 63 source congruences to `mod_three_side`.  It then repeats
the V5 sparse-AST affinity/dependency audit.  Acceptance requires exact counts
`63/30/30`, no mixed restoration multiplication or dependent division in the
63 rows, preservation of all predecessor-dependent coefficient expressions,
and no invalid structural-plus-Frobenius rank specialization.

This is a symbolic compiler checkpoint, not a zero-locus theorem or JC2
claim.  All execution is AWS-only.

