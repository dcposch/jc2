# Task: clean-room K00 valuation-five v2 repair producer

You are Opus 5, acting as a primary mathematical researcher.  Work on
repository basis commit `31777ce90994a106aade85064c0d868e32863f94`.
Write exactly one deliverable:

`xmodel/k00-r5-jetfan-v2-repair-opus5-20260829.md`

Write no other repository file, do not edit canonical ledgers, do not use git,
and do not enter, enumerate, search, read, build, status, modify, or control
`jc2-lean`.  Temporary scratch outside the repository is permitted.  Do not
run Singular or any heavy/uncertain computation locally.  Existing K00 stdlib
replays are known desk-scale; independent exact Python scratch is permitted.
If a necessary discriminator is heavy, freeze an AWS-ready packet and report
the gap rather than guessing.

Frozen inputs:

- rejected producer `xmodel/k00-r5-jetfan-provisional-sol56-20260829.md`,
  full SHA-256
  `82e6512d4a80ae4bdcf8847e6b0a6ed45ed6d03b4898479e946cab3084fd24a0`;
- its replay, SHA-256
  `eb8513b622e9c6fa839f9f20f32ff4c4fc9207a8591cdb6b292ab141f159522b`;
- binding internal hostile audit
  `xmodel/k00-r5-jetfan-internal-hostile-audit-sol56-20260829.md`, full
  SHA-256
  `fee02eb08d44432cc447d252a1bbd43233435bc961092b4ab70c3b9859b1affc`;
- frozen tails and compiler, SHA-256 respectively
  `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`
  and `2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b`.

Rebuild rather than merely paraphrasing the audit.  Produce the cleanest
replacement `K00-R5-R0-RESIDUAL/v2` packet you can justify.  Required gates:

1. independently rederive the leading cone and rank-two exclusion;
2. restore all seven grade-12 and grade-13 equations on rank one, derive the
   missing `tau*f=0` split, and verify both branches through grade 14;
3. define the literal row equations from the immutable tails, with signs and
   shifts for `mu2`, `mu4`, `mu6`, and `Jdet/4` explicit;
4. choose and state exactly one residual type: preferably the minimal
   coefficient projection actually used through grade 19, while recording
   every omitted coefficient as a free affine factor; alternatively give the
   full jet locus with every free coordinate genuinely free.  Do not mix the
   two;
5. give canonical public serialization bytes (or a completely unambiguous
   line-oriented serialization rule), byte count, and SHA-256 covering every
   defining equation, coefficient range, target/load convention, open, and
   localization.  A private shorthand is forbidden;
6. independently derive the grade calendar and dependency ranges rather than
   hard-code them; verify the contracted grade-19 identity and explain its
   exact scope;
7. give executable desk-scale replay logic or sufficiently literal code in
   the report, with source-hash checks and mutations that fail on the missing
   grade-13 equation, a target sign/shift change, a live tail change, and a
   residual-serialization change.

If the full v2 residual cannot be made exact in this lane, fail closed: bank
only the maximum independently proved leading-rank theorem and specify the
smallest remaining repair.  Do not claim a residual point, arc, map,
counterexample, or JC2 consequence.  End with one standalone
`<!-- BODY-END -->` line and no seal block.

