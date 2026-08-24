You are the hostile different-model reviewer for two proof-side route gates in
the JC2 campaign repository `/Users/dc/code/math/jc2`:

1. `xmodel/round1-boundary-passport-20260824.md` with
   `cases/round1_boundary_probe/`;
2. `xmodel/round1-trace-regularity-20260824.md` with
   `cases/round1_trace_probe/`.

Read `COORDINATION.md`'s promotion rules and adjudicate only the registered
scopes. Do not infer a proof or counterexample to JC2. Inspect the code before
running it; use exact arithmetic; put scratch output in a fresh `mktemp -d`
outside the repository; make no network calls, external writes, author contact,
or shared-ledger edits.

For the boundary gate, independently check at least:

- the identity, `T_2`, `T_4`, inverse-composition, Hénon `r=0,1`, and
  non-Keller negative-control formulas;
- the standard and explicit blow-up chart transformations;
- the DVR Smith/Fitting calculations and the claim that the surviving log
  determinant orders follow from `J=1`;
- exactness/residue claims for the two action forms;
- whether `COSTUME` is justified for precisely the tested raw passports, and
  whether the report correctly leaves canonical-minimized, twisted, signed,
  or complete-data variants open.

For TRACE-REG, independently check at least:

- the characteristic-zero Newton-identity implication, converse, finiteness,
  finite-étale, and automorphism steps with every hypothesis explicit;
- the warning that the literal arbitrary-characteristic version is false;
- the local completed-trace/principal-part and residue formula, including
  ramification/residue-field weights and the affine-divisor versus target-
  infinity distinction;
- the triangular-automorphism and `(x^2,xy)` controls;
- the denominator-42 completion collision, including that the varying slot is
  beyond the retained level and leaves support/contact/gcd data fixed while
  changing the quadratic residue;
- whether `INSUFFICIENT-DATA` follows for the current packet, without claiming
  that every possible augmented boundary packet is insufficient.

Run both pinned replay commands and require byte-identical outputs. Record
commands, versions, hashes, any independent calculations, and evidence scope.
Give separate verdicts and one overall verdict from `CONFIRMED`,
`CONFIRMED WITH GAPS`, `GAPS`, or `REFUTED`. State exactly what may enter
`AUDIT.md` and what must remain open.

Write only `xmodel/review-round1-proof-gates-claude.md`. Do not edit the
producer reports, code, generated results, `AUDIT.md`, `APPROACHES.md`,
`PROGRESS.md`, `notes.md`, or any other repository file.
