# AWS Lean verification result — frozen C1 cube checkpoint

Verdict: **PASS_BUILD_AND_NO_SORRYAX** at exact nested commit
`d97de48d83cabdb094c708540dcfe0d00f9a0957`.

## Frozen source

- Git-archive SHA-256:
  `40fd09da952ae3d0aca5e8fb53497fd3aa3e259fd3d0a16cb1af3a6c53785c46`.
- `gcd3-69-cube/Solution.lean` SHA-256:
  `dabf4b5b356f637650dfcda293567ee9b1fe382d3e18e06bf45a25a869c9604d`.
- Lean: `4.34.0-rc1`, commit `3447a668...`; Lake:
  `5.0.0-src+3447a66`.

The independently moving nested checkout after this archive was made is not
an input to this result.

## Failed-closed V1 control

The first AWS harness required `Challenge.lean`, but this project deliberately
contains only `Solution.lean`.  It therefore stopped at
`sha256sum: Challenge.lean: No such file or directory`.  It recorded no exit
code and licenses no build or theorem claim.  Its streams are retained under
`aws_v1_r6d_failed/` as a software negative control.

## Corrected V2 result

The corrected verifier removed only that nonexistent-file check and added an
outer wrapper which always writes the timeout/verifier exit code.  On Amazon
EC2 r6d it returned exact `rc=0` and:

1. matched the source-archive and `Solution.lean` hashes above;
2. fetched the pinned mathlib cache and completed `lake build`;
3. ran `lake env lean Solution.lean` directly;
4. emitted 51 named `#print axioms` records;
5. found the three new declarations
   `GCD369CubeC1NoCommonRootOnUZeroChart`,
   `GCD369CubeC1NoCommonRootOnVZeroChart`, and
   `GCD369CubeC1NoCommonRoot`;
6. found no `sorryAx` in the axiom stream or its empty stderr.

All three C1 declarations depend only on the ordinary permitted Lean/mathlib
axioms `[propext, Classical.choice, Quot.sound]`.  The exact axiom stdout SHA
is `de909502ca3dba99e6f1fc8a377fd24dff004c3a4bdb928ff845dfc5d91144c6`;
axiom stderr is empty with SHA
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Scope firewall

This verifies compilation and axiom hygiene of the formal statements in the
frozen file.  It does not independently rederive the mathematical source,
extend the C1 chart theorem to another cube boundary, close all `(6,9)`, or
prove/disprove JC2.
