# AWS verification of `jc2-lean` commit `5f7cc48`

This case records the final AWS/Linux build and axiom audit of nested repository
commit `5f7cc487f446a03c693f43ad81bae4da850b073b`.

- AWS host: `r6d`, public address `100.26.198.153`, recorded hostname
  `ip-172-30-0-45`
- Remote job: `/home/ubuntu/jobs/jc2_lean_final_5f7cc48_20260825T232100Z`
- Source archive SHA-256:
  `a9a5b6ecd0da1bc9170087b4438ac9502eac25de925cb9fc3cd6f243dc59109e`
- Verification interval: `2026-08-25T23:22:34Z` through
  `2026-08-25T23:27:58Z`
- Toolchain: Lean `4.34.0-rc1`, Lake `5.0.0-src+3447a66`
- Concurrency: `AWS_LEAN_JOBS=8`
- Verdict: `PASS`

The verifier ran `lake exe cache get`, `lake build`, and each project's
`scripts/check_axioms.sh` for:

1. `gcd3-69-noncube`: all 45 named solution theorems built and used only the
   permitted axioms `propext`, `Classical.choice`, and `Quot.sound` (individual
   theorems may use a subset).
2. `max11-partial-y`: all four named solution theorems built and used only the
   same permitted axioms.

The `Challenge.lean` warnings about `sorry` are expected challenge scaffolding;
the audited declarations are the named theorems in `Solution.lean`.

Scope matters. The first project formalizes the aligned `(6,9)` noncube
exclusion branch. The second formalizes the abstract finite routing
certificate comprising `Max11RouteClassification`, `Max11UniquePrimitive`,
`Max12FirstPrimitives`, and `MaxPartialDegreeElevenClosure`; its predicate
`Good` is abstract, so this is not by itself a proof of the full automorphism
theorem or of JC2.

`verify.stdout` and `verify.stderr` are the exact captured streams. The source
archive itself is reproducible from the cited nested commit; its remote digest
is retained in `source_archive.sha256`.
