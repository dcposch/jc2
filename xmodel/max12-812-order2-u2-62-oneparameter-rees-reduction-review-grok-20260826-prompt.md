You are the hostile independent reviewer of a claimed exact one-parameter
reduction of the `(8,12)` order-two `U=2,[6,2]` strict-Rees boundary.  Review
the named bytes and hand algebra; do not run local Singular, Sage, msolve,
Lean, or substantive exact Python.  Do not enumerate the dirty worktree or
print broad `git status`; inspect only the target and its charged sources.

Target:
`xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md`

Required SHA-256:
`5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b`

Charged source:

- source-typed client SHA `e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7`;
- `j!=0` erratum SHA `5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b`;
- V2 compiler source review SHA `b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d`;
- exact tails JSON SHA `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`;
- frozen V2 input SHA `021654e753f1186874f10110d4338e7d9f9457afbfed75419407e87e3b00982c`.

Independently attack:

1. Verify row-by-row that after localizing `R=1+tau`, the automorphism
   `C_even=B_even`, `C_odd=R B_odd`, `J=Rj` and substitution
   `Lambda=tau^3 varrho` turn every exact V2 row into (0.1), including all
   lower-load exponents, all target exponents, twists, signs, and `J/4`.
   Check that no `(9,12)` formula or omitted load enters.
2. Verify `R` is genuinely a unit in the formal boundary chart and that the
   coefficient and `j` changes are invertible there without changing the
   irrelevant ideal on the central fibre.
3. Prove or refute flatness of
   `Q[Lambda] -> Q[tau,varrho,R^-1]`, `Lambda -> tau^3 varrho`.
   Check that torsion-free over the PID is applicable and that extension by
   all retained variables plus the unit automorphism gives the claimed flat
   base change.
4. Check exact scheme equality, not merely equality on the generic chart or
   of reduced supports.  In particular verify
   `D(tau varrho j)=D(Lambda J)`, sequential/product saturation equivalence,
   commutation of the stabilized colon with flat extension, quotient by
   `(tau,varrho)` versus `(Lambda)`, and final irrelevant saturation.  Look
   for extra torsion, embedded components, nilpotents, nonflat specialization,
   or a failure caused by the ramified toric base change.
5. Verify every finite load remains in the one-parameter scheme.  Re-derive
   the toy ideal `(x-Lambda*m)` and decide whether it correctly demonstrates
   that generic-chart projection of a solved load can enlarge the boundary.
   Fail the theorem if its reduction silently makes that projection.
6. Audit the frozen compiler package only for consistency with the theorem:
   it must retain `k10,k6,k2,mu2,mu4,mu6,J`, pin the exact tails, and not
   promote an endpoint.  The live AWS jobs are producer experiments and are
   not evidence for the algebraic reduction.
7. Enforce the scope firewall: equality of boundary schemes is not emptiness,
   Taylor realization, exclusion of `[6,2]`, order-two closure, `(8,12)`,
   maximum twelve, or JC2.

Identify the smallest failing identity or missing hypothesis and state the
strongest corrected theorem.  Write only to
`xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md`.
Include the recomputed target SHA and exact source hashes and end with exactly
one of `CONFIRMED`, `REPAIR`, or `REJECTED`.  Do not edit the target, source
clients, compiler package, or top-level campaign files.
