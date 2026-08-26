# Preregistration — AWS verification of `jc2-lean` cube commit `d97de48`

Frozen source target:

```text
d97de48d83cabdb094c708540dcfe0d00f9a0957
dabf4b5b356f637650dfcda293567ee9b1fe382d3e18e06bf45a25a869c9604d
  gcd3-69-cube/Solution.lean
```

The nested worktree was clean and unchanged for more than three minutes
before packaging.  Verification must run on AWS/Linux, never on the Mac.

Required gates:

1. independently reproduce the source archive SHA on AWS;
2. reproduce the pinned `Solution.lean` SHA;
3. record hostname, DMI, UTC interval, Lean/Lake versions, and the registered
   job tag;
4. run `lake exe cache get`, `lake build`, and
   `lake env lean Solution.lean` under a bounded job;
5. require rc zero, empty command stderr apart from admitted cache/build
   diagnostics, all three new `GCD369CubeC1NoCommonRoot*` declarations in
   the axiom stream, and no `sorryAx` dependency;
6. compare the local nested commit and source hash again after harvesting.

A build/axiom PASS proves formal compilation and declared-axiom hygiene only.
It does not independently verify the mathematical transcription that supplied
the linear-combination certificates, close the entire cube branch, or prove
JC2.

