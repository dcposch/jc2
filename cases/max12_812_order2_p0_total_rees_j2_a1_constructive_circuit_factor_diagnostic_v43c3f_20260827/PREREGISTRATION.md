# V43C3F preregistration: exact top-level factor diagnostic

The frozen V43C3D diagnostic found three surviving final assumption
multipliers, each represented by a top-level `Mul` node.  This diagnostic
reconstructs the immutable V43C3 derivation through its unchanged final
`PruneZeroTerms` boundary, checks the exact registered roots and their direct
factor lists, and expands each distinct direct factor separately over Q.

Registered roots/factors are:

- `assume:ee1`: root 721, factors
  `[118,118,153,153,174,371,371,427,428,428,666]`;
- `assume:rs2`: root 722, factors
  `[118,118,153,153,174,371,371,371,399,428,428,666]`;
- `assume:ez3`: root 723, factors
  `[118,118,153,153,174,371,371,371,401,428,428,666]`.

The run is diagnostic only.  A zero factor is useful input to a future exact
`PruneZeroFactor` rule, but this run neither deletes an assumption term nor
claims `a1^104`.  Every factor is expanded exactly using the V43C3 arithmetic
backend with its one-million-term fail-closed cap.  Results checkpoint after
each factor.  Any root/factor mismatch, cap, exception, or missing terminal
marker gives no mathematical verdict.

AWS only, one core, 4 GiB virtual memory, ten minutes.  Pin the V43C3 producer
SHA-256 `aece88b6a74ac207a031c5b996e8e8d804d2efd464c83a889a91114177aedeed`
and V43C3D diagnostic SHA-256
`bb7d8b9752362714a6f2694ac068ca5486e533bab8de17d910e0fb90fc30b2eb`.
