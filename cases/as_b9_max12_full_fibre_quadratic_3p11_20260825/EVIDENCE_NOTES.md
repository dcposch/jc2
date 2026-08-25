# Evidence map

- `AWS_BOX02_V4/` and `AWS_BOX03_V4/` contain the two byte-identical compiler
  results.  Their `result.json` files are the positive producer endpoints.
- `AWS_BOX02_V4/z3_v2.*` is a Z3 4.16 SAT/model run on the emitted SMT.
- `AWS_BOX02_V4/boolector_v3.*` is the successful Boolector SAT/model run.
  `obstruction.boolector.v3.smt2` differs from the canonical SMT only by
  deletion of commands unsupported by that Boolector version.
- `AWS_BOX02_V4/model_crosscheck.stdout` checks both solver models against
  the active-zero literal witness in `result.json`.
- `AWS_BOX02_V4/solver_model.*`, `boolector_v2.*`, and
  `AWS_BOX03_V4/solver_model.*` are environment/parser negative controls and
  are not mathematical evidence.
- `NEGATIVE_V2_BOX02/` records the missing-parent-helper source failure.
- `NEGATIVE_V3_BOX02/` records the rejected false degree-pair assertion.

All substantive compilation and solving occurred on AWS.  No local CAS or
solver replay is part of this package.
