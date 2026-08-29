# D5G35 preregistration: complete raw determinant and R7R1 cutoffs

Date: 2026-08-27

## Frozen question

Extend reviewed D5G additively from `D0,...,D22` to the complete determinant
range `D0,...,D35`, using exactly the frozen D3 raw alphabet.  Independently
verify that the D3 list exhausts both source polygons, that `F` stops at raw
weight 14 and `G` at raw weight 21, and that no determinant row beyond 35
can occur.

The extension must preserve all D5G bytes and provenance through weight 22,
serialize every new contribution, independently dense-check all 36 rows, and
freeze the unsolved exact target gate

```text
D0=...=D21=0, D22=1, D23=...=D35=0.
```

## R7R1 interface

Under the corrected R7R1 truncation theorem:

```text
through D22 target -> E=t^22+O(t^23) -> q0 only;
plus D23=0         -> E=t^22+O(t^24) -> q0,q1;
plus D24=0         -> E=t^22+O(t^25) -> q0,q1,q2.
```

Mutations `D23 -> D23+1` and `D24 -> D24+1` must respectively revoke the
`q1` and `q2` licenses.  R7R1 remains provisional until its different-model
review; this computation proceeds review-independently and may consume only
the exact cutoff semantics already established by the same-model audit.

## Controls and scope

- Byte-compare rows `D0,...,D22` with frozen reviewed D5G.
- Serialize every contribution at every weight `0,...,35`.
- Independently specialize all 400 raw slots to deterministic nonzero
  rationals and recompute the full bivariate determinant without calling the
  sparse recurrence.
- Enumerate every coefficient generator of the exact target gate.
- Preserve D5G's `D22=H*Q22+R22` certificate and `H` mutation.
- Reject any claim that the gate is solved or that bounded source support
  makes the R7R1 de Rham tower finite.

A PASS proves only the complete direct determinant compiler, exact target
gate, and cutoff interface.  It proves no specialization, landing, face or
family result, `G2-PSC`, `G2-BD`, counterexample, or JC2.
