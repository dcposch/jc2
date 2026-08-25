# AWS verification of the pending `jc2-lean` snapshot

Status: `PASS` on 2026-08-25.  This package verifies the exact dirty
`jc2-lean` sources immediately before their campaign commit; it does not add
mathematical scope beyond the theorem statements in those sources.

## Host and runner

- AWS host: r6d, instance `i-07eeaf8ba6f0bc419`, run-time hostname
  `ip-172-30-0-45`.
- Remote run directory:
  `/home/ubuntu/jc2-lean-verify-20260825T1455Z`.
- Successful wrapper: `ops/aws_lean_verify.sh`, remote V3 SHA-256
  `ebee644b9b16c00f699d7c20949b6215ddb8af1c9a1d074e4385b766d5f99130`.
- Started `2026-08-25T15:04:05Z`; finished
  `2026-08-25T15:10:19Z`.
- Ubuntu package `elan 3.1.0-1ubuntu0.1`; project-selected Lean
  `4.34.0-rc1`; Lake `5.0.0-src+3447a66`.
- `AWS_LEAN_JOBS=8`, exported by the wrapper as `LEAN_NUM_THREADS=8`.

The first wrapper attempt failed before selecting a project toolchain; the
second failed closed because this Lake version does not accept `build -j`.
Neither elaborated a campaign theorem.  V3 corrected only those orchestration
issues.

## Source pins

| project/file | SHA-256 |
|---|---|
| `gcd3-69-noncube/Solution.lean` | `d47bc2e53c5ee3bd9cec669ecbce963df4decf41682fe46051ae088239ff4c67` |
| `gcd3-69-core/Solution.lean` | `070f16763562b824e723b29fa14208192edaf7e52ce59c04aa0eca6974ceed38` |
| `strip-block/Solution.lean` | `ed2a25d4503ed54c10f69c6b8f435ea45ab6cb2c4f4ba44bfac61515c4f67804` |
| common `lean-toolchain` | `cdbc6c372a2b37ad94430a6cec69cedfa4d36f255bfd968773fd91bf7a1746bf` |

The full log also pins each project `lakefile.toml`, `lake-manifest.json`, and
`Challenge.lean`.

## Verdict

All three `lake build` commands completed successfully from the shipped
snapshot.  The three package-specific `scripts/check_axioms.sh` checks also
passed:

- all eighteen named `gcd3-69-noncube` theorems use only the permitted
  Mathlib axioms;
- all six named `gcd3-69-core` theorems use only the permitted Mathlib axioms;
- all four named `strip-block` theorems use only the permitted Mathlib axioms.

`Challenge.lean` deliberately contains `sorry` placeholders and therefore
emits warnings; the proof-bearing `Solution.lean`/`Rigidity.lean` sources do
not contain `sorry`, `admit`, or custom `axiom` declarations.  Remaining
compiler output consists of linter/deprecation warnings, not build or axiom
failures.

Custody logs are `verify.stdout` and `verify.stderr`; their hashes are pinned
by `MANIFEST.sha256`.
