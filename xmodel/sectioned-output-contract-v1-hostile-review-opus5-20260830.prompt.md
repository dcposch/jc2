# Hostile software review — `SECTIONED-INDEPENDENT-CALLS/v1`

You are Opus 5 acting as an adversarial software reviewer. Work in
`/Users/dc/code/math/jc2` on frozen git basis
`0f7ee003be45ee40d51d4048897cdacf63821172` plus exactly these two uncommitted
candidate files:

```text
593bc16465eac0b1146b08b724226cea3b449178090d974dbdfb0357d40f5473
  ops/sectioned_output.py
b8e311fe915b2589ab13307840bed4b3e2864d6d13fe1976b65db8f9c9bb30a1
  ops/test_sectioned_output.py
```

Recompute both hashes before use. This is the implementation trial selected
by round `20260829T2254Z`: a runner cannot checkpoint inside one monolithic
provider response, so a long task must use independent calls whose section
artifacts are bounded and validated before final assembly.

Hostilely inspect path confinement, symlink/race handling, manifest schema,
marker parsing, truncation semantics, mutation detection, exclusive output,
determinism, and whether the implementation overclaims immutability or live
provider integration. Run the focused tests in ordinary and optimized Python,
add reviewer-owned tests only under `/tmp`, and try at least five independent
mutations/negative controls. Check that partial output remains useful and a
noncontiguous or mutated sequence fails closed. Do not edit either charged
file.

Return `PASS`, `PASS_WITH_REPAIRS`, `REPAIR_REQUIRED`, or `FAIL`. Enumerate
every correction and state the maximum safe lifecycle. This is an opt-in
assembly/validation tool, not a model runner, authentication layer, semantic
checker, or proof. No mathematical claim may depend on it.

Write only
`xmodel/sectioned-output-contract-v1-hostile-review-opus5-20260830.md` plus
scratch under `/tmp`. Do not edit canonical files, commit, push, browse, use
AWS, or inspect/list/search/stat/build/modify/control `jc2-lean`. End with one
standalone `<!-- BODY-END -->`; do not add a seal. No exit price is asserted,
so omit `charge_basis`. Fail closed.
