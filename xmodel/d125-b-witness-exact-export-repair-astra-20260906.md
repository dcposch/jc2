# D125 B witness exact-export erratum

Date: 2026-09-06. Owner: nonemptiness_certificate. Bounded serialization repair only.

## Result and superseded claim

The original `box/d125-minimal-receiver-b-reconstruction-20260906/exact-witnesses.json` is **REFUTED AT EXACT-SERIALIZATION SCOPE**: 57 of its 144 `nonzero_minor` entries contain floating-point numerals and differ from the exact runtime values. No additional integer-only minor is wrong. All recorded Schur values, ranks, selected rows, columns, and degrees agree with the unchanged exact producer. The original report, checker, witness, replay, and custody files are preserved unchanged.

The replacement is `box/d125-b-witness-exact-export-repair-20260906/exact-witnesses-v2.json`, 29,356 bytes, SHA256 `07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246`. These are the unchanged Python checker's raw stdout bytes, including its newline, matching the exact runtime hash supplied by the terminal independent gate. All 144 minors validate as exact rational/field values, with no float types anywhere. This repairs the retained witness, not any mathematical theorem or source equation.

## Confirmed cause

The producer's original tool call parsed the checker output in the functions JavaScript isolate using `JSON.parse(r.output)`, retained that native-number object with `store("brecon_witness", d)`, and later passed `JSON.stringify(d, null, 2)` into `apply_patch`. That is the confirmed original construction path, not a diagnosis inferred merely from decimal formatting. Exact large Python JSON integers became IEEE-754 JavaScript numbers; serialization then printed rounded numbers, sometimes with exponent notation. Python's original exact computation and integer encoder did not introduce these floats.

The old replay's `equal_witness` check compared JavaScript objects after the same lossy conversion, so its truth does not certify exact integer or byte equality. Its ordinary/optimized checker exit statuses remain valid; the precise retained-witness interpretation of that comparison is withdrawn here. Hashes of the old bytes continue to identify those bytes, not their mathematical exactness.

## Replacement path and actual controls

`export_exact.py` verifies the original checker and old-witness hashes, runs the unchanged Python checker under a 25-second subprocess timeout, captures stdout as bytes, and checks the independently supplied runtime hash. Its exclusive `xb` output writes, flush/fsync, reread, and byte comparison never expose the numeric witness to JavaScript parsing/stringifying. Only hashes and small-count receipts cross the tool boundary. The script rejects floating JSON numerals, validates exact integer numerator/denominator types and reduced fractions, and checks every minor against its exact triangular-product/Schur identity. It verifies the 144-entry census: 24 kernel-block minors and 120 full-rank-block minors; the field norm is nonzero in each case. This is not a new independent dense-determinant calculation; the independent gate already checked that interpretation.

Real mutations are fed into this validator. An actual exact numerator `167289062521996800000` becomes `167289062521996804096` after float conversion and return to integer, a difference of `4096`. Both the floating object/JSON mutation and the rounded-integer mutation are rejected. Thus a mere no-float-type check is not being mistaken for exactness. These large examples are recorded as strings in the receipt.

The normal export and optimized `--verify-only` replay passed under local 30-second wall, 25-second CPU, and 512-MiB caps (combined measured batch 0.66 seconds). The latter reruns the unchanged producer and compares raw bytes without rewriting outputs. Replay command from the repository root:

```sh
timeout 30 bash -ec 'ulimit -v 524288; ulimit -t 25; python3 box/d125-b-witness-exact-export-repair-20260906/export_exact.py --verify-only'
timeout 30 bash -ec 'ulimit -v 524288; ulimit -t 25; python3 -O box/d125-b-witness-exact-export-repair-20260906/export_exact.py --verify-only'
```

## Bounded check for the same export defect

I checked the retained tool-history export paths and the 17 top-level JSON files in exactly these four recent terminal owned boxes:

- `box/d125-published-chain-discriminator-20260906/`
- `box/d125-minimal-monomial-receiver-composition-20260906/`
- `box/d125-small-receiver-polynomial-lift-contract-20260906/`
- `box/d125-minimal-receiver-b-reconstruction-20260906/`

The replayable read-only `audit_recent.py` names only those directories, hashes each JSON file, and inventories float paths and integers above 2^53. The sole mathematical exact-number payload in this scope with the confirmed unsafe JavaScript export is the original B `exact-witnesses.json`. The B `replay.json` also used JavaScript serialization of receipt data; its fields contain timing floats and small counts, not large mathematical numbers, but its `equal_witness` interpretation needs the correction above. The other three boxes' JSON exports were manually supplied metadata/receipts, not parsed-and-reserialized mathematical witness streams; their only floating fields are declared wall-time measurements. Outside the old B witness, none of these 17 JSON files contains an integer above 2^53. The old witness's 27 remaining large integer leaves are covered by the exact comparison: there are no wrong integer-only minor entries.

This check is deliberately not a repository-wide audit or a claim about all older artifacts. It does not inspect unrelated current exporter/preflight artifacts, whose rational-string encoding is not implicated by this numeric JSON mechanism. No live peer body, log, code, or receipt was consumed.

## Pins, reading scope, and custody

Read wholly: terminal `xmodel/d125-b-reconstruction-gate-fable5-20260906.md`, SHA256 `3f154e7816deb5de39e727f99cafac3328592c703af246614d4f1e9fe2ccf1ea`; original and replacement export/check code. The gate's independent code/output were not consumed or rerun here. No primary mathematical proof is re-audited by this repair.

| Artifact | SHA256 |
| --- | --- |
| Original `check.py` | `5a3cc2853c04b74faa7b256122a445c5435412c905966fd55ebfc2965e8c67d5` |
| Original `exact-witnesses.json` | `9551e7205d6918e5bf913b70b1ea9e5921b8e8eadeb2d9591b610a78cdc24f77` |
| New `export_exact.py` | `3921fb188b333fadf75dc4f79bdb1be160b9c02d67da53dc72fa916cd0abe064` |
| New `repair-receipt.json` | `6acf120816d98a0cec5bfea49dd3cf62057482dcc356c2294ad362c21d982be0` |
| New `audit_recent.py` | `49b50ec533f1fcada5ae07751af06635029caed48d4279266e319e2c12dd0be0` |
| New `registration.json` | `07a0ec559650d1ecda2fe51c12b456044353ed44ebb66c38b2879f764e881f78` |

All new files are in the new repair box; terminal custody will pin this transaction and all owned artifacts. All arithmetic/export writers are done. No worker, background job, AWS action, symbolic residual expansion, solver, old-file edit, shared-ledger edit, or protected-project edit occurred. Root may independently compare the new literal bytes with the unchanged producer and independent gate. No further generation is authorized or implied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7193`.
- Body SHA-256:
  `acce81421b96c6fdaf371d751f2106b4d095c76077676aa3c45db505114bbde4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
