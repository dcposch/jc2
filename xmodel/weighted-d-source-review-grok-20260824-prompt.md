# Hostile review charge — weighted D-source gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at basis
`dd11599b07eb05591b5c006791005eef19457d8e`.

Read in full:

- `xmodel/weighted-d-source-gate-20260824.md`
- `cases/weighted_d_source_gate_20260824/PREREGISTRATION.md`
- `cases/weighted_d_source_gate_20260824/replay.py`
- `cases/weighted_d_source_gate_20260824/results.json`
- every producer artifact whose hash or exact field is used by the report

Then independently:

1. run the registered replay and verify every recorded artifact hash;
2. inspect the actual producer interfaces and decide whether a named normalized
   full-polynomial source point and typed tangent maps for
   `alpha_1,beta_1,alpha_2,beta_2` exist anywhere in the frozen perimeter;
3. recompute equations (4.1)--(4.8), including all chain-rule terms, over an
   exact coefficient ring;
4. attack the distinction between formal ambient symbols and a producer-typed
   source tangent, and decide whether `NO-TYPED-SOURCE/NO-QUOTIENT` is the
   first honest stop;
5. report any smallest failing identity, omitted source artifact, overclaim, or
   scope correction. Do not widen into band 28, deeper D, D43 integral work,
   syzygies, a generic state search, or a new source construction.

Write exactly one file:

`xmodel/weighted-d-source-review-grok-20260824.md`

Give an overall `CONFIRMED`, `REFUTED`, or `GAP` verdict; a per-subclaim table;
the exact replay command/output and hashes; promotion advice; and explicit
exclusions. Do not edit any canonical ledger or any other file.
