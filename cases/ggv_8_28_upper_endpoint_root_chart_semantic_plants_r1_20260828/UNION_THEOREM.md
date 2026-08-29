# Scoped TRIPLE03 geometric-cover union theorem

## Frozen packets

Let the root packet be the terminal archive

`db522621095ca392e65280fe18044924d8566de3e1f30acd0b9e419e0798419d`

from this case, and let the closed-complement packet be the independently planted
R5 archive

`b31a9b145b3bb8af6b6eda1be45c0b8d1cdea3819509c7e86873eb0284c3a2e9`.

Both packets bind the same literal TRIPLE03 root delta, whose artifact SHA is
`9e07a399764ace2008ad89af5c865326b0cdb65ceab1bcc83f5edcc63463144b`.
The R5 input manifest starts its recursion with exactly `(q2, Delta)` and records
the substitutions `q1=0`, `c8=0`, the remaining variables
`(q0,q2,c4,c6)`, and exact rank upper bound four. The new root replay preserves
the original root bytes and all three original mathematical artifacts exactly.

## Assumptions made explicit

The union statement assumes only the packet-local contracts that were checked in
the two archives:

1. the pinned upstream 95-pivot reduction, residual matrix, quotient normal form,
   and rank certificates describe the same literal TRIPLE03 system in both
   packets;
2. `D(Delta)` and `V(Delta)` are interpreted set-theoretically over complex
   geometric points of that literal component;
3. on every nonempty chart, the adjugate construction spans the complete fiberwise
   kernel because the displayed rank witness is nonzero, all next-size minors
   reduce to zero, every residual-row identity reduces to zero, and all 95
   rational-unit pivots are lifted; and
4. each R5 recursion node uses the ordinary open/closed split by its displayed
   delta, its saturation/power certificate is accepted exactly as archived, and
   the final closed successor is the unit ideal.

No equality of schemes, ideals, or radicals is assumed or inferred.

## Exact cover argument

Every complex geometric point of the literal TRIPLE03 component lies either in
the root open `D(Delta)` or in its closed complement `V(Delta)`.

- On `D(Delta)`, the new retrospective packet proves the full pulled-back
  quadratic `E=x14*x72+x1*x97` has 21 zero coefficients. Its planted endpoint and
  bordered controls pass in the same quotient reducer.
- On `V(Delta)`, R5 gives an eight-node finite geometric recursion. Six opens are
  exactly empty by saturation with explicit power certificates; the two nonempty
  charts are endpoint-dead with planted endpoint and bordered controls; the last
  closed successor has delta `1` and is empty.

Therefore, under the four packet-local assumptions above, `E` vanishes on the
complete certified fiberwise kernel at every complex geometric point of the
literal TRIPLE03 component.

## Strict conclusion and exclusions

The conclusion is a scoped, set-theoretic geometric endpoint-death theorem for
the literal `q1=c8=q2=0` TRIPLE03 component only. It does not assert membership of
the endpoint coefficients in the unsaturated component ideal, scheme-theoretic
vanishing, reducedness, radical equality, absence of nilpotents, any conclusion
on another component or intersection presentation, or any ambient HENS-CT
endpoint theorem.
