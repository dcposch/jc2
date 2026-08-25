# B9 normalized `(9,12)` complete-family quadratic gate at `3^11`

This package consumes the complete `3^145` normalized coefficient family
modulo `3^10=59049` over one fixed B9 mod-243 parent.  The first coordinate
uses exactly the total-degree-9 simplex and the second the total-degree-12
simplex, for 146 fresh coefficient slots in total.

For `F=F5+243*T+3^10*W`, the 276 determinant-coefficient equations are

```text
(D5 + 243*A*T)/3^10 + det J(T) + A*W = 0  (mod 3).
```

The stored parent arrays have already divided by the outer factor
`243=3^5`, so the compiler's remaining divided-carry divisor is `3^5`, not
an accidental replacement of `3^10`.

The fresh `276 x 146` operator has rank 85, kernel dimension 61, and
cokernel dimension 191.  An invertible coordinate change on the 145
predecessor directions separates 17 directions visible modulo three from
128 divisible-by-three spectators.  The spectator image has rank 44 and
kernel dimension 84.  The complete constant/linear/quadratic coefficient
space has rank 15 and remains inside that rank-44 image.  Thus the final
post-elimination Kuranishi system has zero equations.

Exactly `3^101` predecessor points lift, each with `3^61` fresh lifts, so
the displayed mod-`3^11` family has cardinality `3^162`.  A literal integer
witness replays every determinant coefficient modulo `177147` and has
honest partial-y and total-degree pairs `(9,12)`.

Box02 and Box03 compiled the same pinned source closure and emitted
byte-identical result SHA-256
`984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539`.
This is custody replication, not an independent mathematical construction.

Scope is the complete displayed normalized family over one fixed B9 mod-243
parent.  This is not the complete earlier mod-243 fibre, a mod-`3^12` result,
an inverse-limit point, a maximum-twelve theorem, a counterexample, or JC2.

Heavy replay is AWS-only.  From a staged transitive source closure, run
`run_aws.sh` with explicit `JC2_ROOT`, `OUTPUT_JSON`,
`PARENT_REPLAY_JSON`, `ANF_OUTPUT`, and `SMT2_OUTPUT` paths.
