# TD6 V89H3 q14 alternate-pivot/Fitting preregistration

Date: 2026-08-26

Status: producer diagnostic; no result claimed before dual AWS output.

## Input

V89H2 found that adding `q14` to arbitrary `q16,...,q24` changes the
reviewed 38-column FIRST pivot block from the H1 nilpotent graph to one with
the cyclic SCC `{0,1,2,3,4,5,6,13}`. All eight nodes have q14-supported
self-loops. H2 did not invert the resulting q-dependent diagonal factor.

## Exact test

Rebuild the literal tail family and the reviewed q-zero pivot basis. First
emit the exact q14 coefficient of the row-0 self-loop and the division-free
determinant of the eight-dimensional q14 SCC block on the q14 axis.

Then examine every single constant basis exchange between one of the 38
reviewed pivot columns and one of the other 94 retained section columns.
For a replacement column `c` at position `j`, accept the base block only if
its exact determinant ratio is nonzero and its inverse introduces no
denominator outside the registered `U,H,B3` open. Normalize by that constant
inverse only, compute the full tail-q support graph, and record its SCCs,
self-loops, edge count, and digest.

Stop at the first registered acyclic exchange. If none exists, emit the best
single exchange ordered by cyclic-node count, self-loop count, then edge
count. This is a bounded one-exchange diagnostic, not a proof that no
unimodular multi-exchange or Fitting cover exists.

## Fail-closed gates

- Consume the frozen H2/V87 source bytes and all 132 section columns.
- Keep q14 and all q16 through q24 independent; q2 through q13 are explicitly
  zero and q15 remains absent under the reviewed target shear.
- Invert only constant base-block determinant ratios whose denominator
  factors are registered; reject every q-dependent inverse.
- Compute the q14 block determinant by division-free subset DP.
- Emit every tested exchange, including rejected denominator scopes.
- Make no P12, radical-membership, nonintegrability, source-point, or global
  TD6 claim from this diagnostic.
- Require byte-identical exact output on two AWS hosts.

If an acyclic exchange is found, a separate client must still construct the
two-sided polynomial FIRST inverse, reduce literal P12, replay against the
original sources, and pass denominator/omission controls before any collapse
claim.
